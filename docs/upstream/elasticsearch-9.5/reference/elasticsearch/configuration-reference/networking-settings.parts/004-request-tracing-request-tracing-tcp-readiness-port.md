<!-- Part 4 of 4 of reference/elasticsearch/configuration-reference/networking-settings.md (split because the page is big). -->

## Request tracing [_request_tracing]

You can trace individual requests made on the HTTP and transport layers.

::::{warning}
Tracing can generate extremely high log volumes that can destabilize your cluster. Do not enable request tracing on busy or important clusters.
::::


### REST request tracer [http-rest-request-tracer]

The HTTP layer has a dedicated tracer that logs incoming requests and the corresponding outgoing responses. Activate the tracer by setting the level of the `org.elasticsearch.http.HttpTracer` logger to `TRACE`:

```console
PUT _cluster/settings
{
   "persistent" : {
      "logger.org.elasticsearch.http.HttpTracer" : "TRACE"
   }
}
```

You can also control which URIs will be traced, using a set of include and exclude wildcard patterns. By default every request will be traced.

```console
PUT _cluster/settings
{
   "persistent" : {
      "http.tracer.include" : "*",
      "http.tracer.exclude" : ""
   }
}
```

By default, the tracer logs a summary of each request and response which matches these filters. To record the body of each request and response too, set the system property `es.insecure_network_trace_enabled` to `true`, and then set the levels of both the `org.elasticsearch.http.HttpTracer` and `org.elasticsearch.http.HttpBodyTracer` loggers to `TRACE`:

```console
PUT _cluster/settings
{
   "persistent" : {
      "logger.org.elasticsearch.http.HttpTracer" : "TRACE",
      "logger.org.elasticsearch.http.HttpBodyTracer" : "TRACE"
   }
}
```

Each message body is compressed, encoded, and split into chunks to avoid truncation:

```text
[TRACE][o.e.h.HttpBodyTracer     ] [master] [276] response body [part 1]: H4sIAAAAAAAA/9...
[TRACE][o.e.h.HttpBodyTracer     ] [master] [276] response body [part 2]: 2oJ93QyYLWWhcD...
[TRACE][o.e.h.HttpBodyTracer     ] [master] [276] response body (gzip compressed, base64-encoded, and split into 2 parts on preceding log lines)
```

Each chunk is annotated with an internal request ID (`[276]` in this example) which you should use to correlate the chunks with the corresponding summary lines. To reconstruct the output, base64-decode the data and decompress it using `gzip`. For instance, on Unix-like systems:

```sh
cat httptrace.log | sed -e 's/.*://' | base64 --decode | gzip --decompress
```

::::{warning}
HTTP request and response bodies may contain sensitive information such as credentials and keys, so HTTP body tracing is disabled by default. You must explicitly enable it on each node by setting the system property `es.insecure_network_trace_enabled` to `true`. This feature is primarily intended for test systems which do not contain any sensitive information. If you set this property on a system which contains sensitive information, you must protect your logs from unauthorized access.
::::



### Transport tracer [transport-tracer]

The transport layer has a dedicated tracer that logs incoming and outgoing requests and responses. Activate the tracer by setting the level of the `org.elasticsearch.transport.TransportService.tracer` logger to `TRACE`:

```console
PUT _cluster/settings
{
   "persistent" : {
      "logger.org.elasticsearch.transport.TransportService.tracer" : "TRACE"
   }
}
```

You can also control which actions will be traced, using a set of include and exclude wildcard patterns. By default every request will be traced except for fault detection pings:

```console
PUT _cluster/settings
{
   "persistent" : {
      "transport.tracer.include" : "*",
      "transport.tracer.exclude" : "internal:coordination/fault_detection/*"
   }
}
```




## Networking threading model [modules-network-threading-model]

This section describes the threading model used by the networking subsystem in Elasticsearch. This information isn’t required to use Elasticsearch, but it may be useful to advanced users who are diagnosing network problems in a cluster.

Elasticsearch nodes communicate over a collection of TCP channels that together form a transport connection. Elasticsearch clients communicate with the cluster over HTTP, which also uses one or more TCP channels. Each of these TCP channels is owned by exactly one of the `transport_worker` threads in the node. This owning thread is chosen when the channel is opened and remains the same for the lifetime of the channel.

Each `transport_worker` thread has sole responsibility for sending and receiving data over the channels it owns. Additionally, each http and transport server socket is assigned to one of the `transport_worker` threads. That worker has the responsibility of accepting new incoming connections to the server socket it owns.

If a thread in Elasticsearch wants to send data over a particular channel, it passes the data to the owning `transport_worker` thread for the actual transmission.

Normally the `transport_worker` threads will not completely handle the messages they receive. Instead, they will do a small amount of preliminary processing and then dispatch (hand off) the message to a different [threadpool](/reference/elasticsearch/configuration-reference/thread-pool-settings.md) for the rest of their handling. For instance, bulk messages are dispatched to the `write` threadpool, searches are dispatched to one of the `search` threadpools, and requests for statistics and other management tasks are mostly dispatched to the `management` threadpool. However in some cases the processing of a message is expected to be so quick that Elasticsearch will do all of the processing on the `transport_worker` thread rather than incur the overhead of dispatching it elsewhere.

By default, there is one `transport_worker` thread per CPU. In contrast, there may sometimes be tens-of-thousands of TCP channels. If data arrives on a TCP channel and its owning `transport_worker` thread is busy, the data isn’t processed until the thread finishes whatever it is doing. Similarly, outgoing data are not sent over a channel until the owning `transport_worker` thread is free. This means that we require every `transport_worker` thread to be idle frequently. An idle `transport_worker` looks something like this in a stack dump:

```text
"elasticsearch[instance-0000000004][transport_worker][T#1]" #32 daemon prio=5 os_prio=0 cpu=9645.94ms elapsed=501.63s tid=0x00007fb83b6307f0 nid=0x1c4 runnable  [0x00007fb7b8ffe000]
   java.lang.Thread.State: RUNNABLE
	at sun.nio.ch.EPoll.wait(java.base@17.0.2/Native Method)
	at sun.nio.ch.EPollSelectorImpl.doSelect(java.base@17.0.2/EPollSelectorImpl.java:118)
	at sun.nio.ch.SelectorImpl.lockAndDoSelect(java.base@17.0.2/SelectorImpl.java:129)
	- locked <0x00000000c443c518> (a sun.nio.ch.Util$2)
	- locked <0x00000000c38f7700> (a sun.nio.ch.EPollSelectorImpl)
	at sun.nio.ch.SelectorImpl.select(java.base@17.0.2/SelectorImpl.java:146)
	at io.netty.channel.nio.NioEventLoop.select(NioEventLoop.java:813)
	at io.netty.channel.nio.NioEventLoop.run(NioEventLoop.java:460)
	at io.netty.util.concurrent.SingleThreadEventExecutor$4.run(SingleThreadEventExecutor.java:986)
	at io.netty.util.internal.ThreadExecutorMap$2.run(ThreadExecutorMap.java:74)
	at java.lang.Thread.run(java.base@17.0.2/Thread.java:833)
```

In the [Nodes hot threads](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-nodes-hot-threads) API an idle `transport_worker` thread is reported like this:

```text
   0.0% [cpu=0.0%, idle=100.0%] (500ms out of 500ms) cpu usage by thread 'elasticsearch[instance-0000000004][transport_worker][T#1]'
     10/10 snapshots sharing following 9 elements
       java.base@17.0.2/sun.nio.ch.EPoll.wait(Native Method)
       java.base@17.0.2/sun.nio.ch.EPollSelectorImpl.doSelect(EPollSelectorImpl.java:118)
       java.base@17.0.2/sun.nio.ch.SelectorImpl.lockAndDoSelect(SelectorImpl.java:129)
       java.base@17.0.2/sun.nio.ch.SelectorImpl.select(SelectorImpl.java:146)
       io.netty.channel.nio.NioEventLoop.select(NioEventLoop.java:813)
       io.netty.channel.nio.NioEventLoop.run(NioEventLoop.java:460)
       io.netty.util.concurrent.SingleThreadEventExecutor$4.run(SingleThreadEventExecutor.java:986)
       io.netty.util.internal.ThreadExecutorMap$2.run(ThreadExecutorMap.java:74)
       java.base@17.0.2/java.lang.Thread.run(Thread.java:833)
```

Note that `transport_worker` threads should always be in state `RUNNABLE`, even when waiting for input, because they block in the native `EPoll#wait` method. The `idle=` time reports the proportion of time the thread spent waiting for input, whereas the `cpu=` time reports the proportion of time the thread spent processing input it has received.

If a `transport_worker` thread is not frequently idle, it may build up a backlog of work. This can cause delays in processing messages on the channels that it owns. It’s hard to predict exactly which work will be delayed:

* There are many more channels than threads. If work related to one channel is causing delays to its worker thread, all other channels owned by that thread will also suffer delays.
* The mapping from TCP channels to worker threads is fixed but arbitrary. Each channel is assigned an owning thread in a round-robin fashion when the channel is opened. Each worker thread is responsible for many different kinds of channel.
* There are many channels open between each pair of nodes. For each request, Elasticsearch will choose from the appropriate channels in a round-robin fashion. Some requests may end up on a channel owned by a delayed worker while other identical requests will be sent on a channel that’s working smoothly.

If the backlog builds up too far, some messages may be delayed by many seconds. The node might even [fail its health checks](docs-content://deploy-manage/distributed-architecture/discovery-cluster-formation/cluster-fault-detection.md) and be removed from the cluster. Sometimes, you can find evidence of busy `transport_worker` threads using the [Nodes hot threads](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-nodes-hot-threads) API. However, this API itself sends network messages so may not work correctly if the `transport_worker` threads are too busy. It is more reliable to use `jstack` to obtain stack dumps or use Java Flight Recorder to obtain a profiling trace. These tools are independent of any work the JVM is performing.

It may also be possible to identify some reasons for delays from the server logs. See for instance the following loggers:

`org.elasticsearch.transport.InboundHandler`
:   This logger reports a warning if processing an inbound message occupies a network thread for unreasonably long, which is almost certainly a bug. The warning includes some information which can be used to identify the message that took unreasonably long to process.

`org.elasticsearch.transport.OutboundHandler`
:   This logger reports a warning if sending an outbound message takes longer than expected. This duration includes time spent waiting for network congestion to clear, and time spent processing other work on the same network thread, so does not always indicate the presence of a bug related to the outbound message specified in the log entry.

`org.elasticsearch.common.network.ThreadWatchdog`
:   This logger reports a warning and a thread dump when it notices that a network thread has not made progress between two consecutive checks, which is almost certainly a bug:

    ```text
    [WARN ][o.e.c.n.ThreadWatchdog   ] the following threads are active but did not make progress in the preceding [5s]: [elasticsearch[instance-0000000004][transport_worker][T#1]]]
    [WARN ][o.e.c.n.ThreadWatchdog   ] hot threads dump due to active threads not making progress [part 1]: H4sIAAAAAAAA/+1aa2/bOBb93l8hYLUYFWgYvWw5AQbYpEkn6STZbJyiwAwGA1qiY8US6ZJUHvPr90qk/JJky41TtDMuUIci...
    [WARN ][o.e.c.n.ThreadWatchdog   ] hot threads dump due to active threads not making progress [part 2]: LfXL/x70a3eL8ve6Ral74ZBrp5x7HmUD9KXQz1MaXUNfFC6SeEysxSw1cNXL9JXYl3AigAE7ywbm/AZ+ll3Ox4qXJHNjVr6h...
    [WARN ][o.e.c.n.ThreadWatchdog   ] hot threads dump due to active threads not making progress (gzip compressed, base64-encoded, and split into 2 parts on preceding log lines; ...
    ```

    To reconstruct the thread dump, base64-decode the data and decompress it using `gzip`. For instance, on Unix-like systems:

    ```sh
    cat watchdog.log | sed -e 's/.*://' | base64 --decode | gzip --decompress
    ```

    This mechanism can be controlled with the following settings:

    `network.thread.watchdog.interval`
    :   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), [time value](/reference/elasticsearch/rest-apis/api-conventions.md#time-units)) Defines the interval between watchdog checks. Defaults to `5s`. Set to `0` to disable the network thread watchdog.

    `network.thread.watchdog.quiet_time`
    :   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), [time value](/reference/elasticsearch/rest-apis/api-conventions.md#time-units)) Defines the interval between watchdog warnings. Defaults to `10m`.




## TCP readiness port [tcp-readiness-port]

If configured, a node can open a TCP port when the node is in a ready state. A node is deemed ready when it has successfully joined a cluster. In a single node configuration, the node is said to be ready, when it’s able to accept requests.

To enable the readiness TCP port, use the `readiness.port` setting. The readiness service will bind to all host addresses.

If the node leaves the cluster, or the [Shutdown API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-shutdown-put-node) is used to mark the node for shutdown, the readiness port is immediately closed.

A successful connection to the readiness TCP port signals that the Elasticsearch node is ready. When a client connects to the readiness port, the server simply terminates the socket connection. No data is sent back to the client. If a client cannot connect to the readiness port, the node is not ready.
