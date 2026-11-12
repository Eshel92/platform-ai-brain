<!-- Part 3 of 4 of reference/elasticsearch/configuration-reference/networking-settings.md (split because the page is big). -->

## Advanced transport settings [transport-settings]

Use the following advanced settings to configure the transport interface independently of the [HTTP interface](#http-settings). Use the [network settings](#common-network-settings) to configure both interfaces together.

`transport.host`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), string) Sets the address of this node for transport traffic. The node will bind to this address and will also use it as its transport publish address. Accepts an IP address, a hostname, or a [special value](#network-interface-values). Use this setting only if you require different configurations for the transport and HTTP interfaces.

    Defaults to the address given by `network.host`.


`transport.bind_host`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), string) The network address(es) to which the node should bind in order to listen for incoming transport connections. Accepts a list of IP addresses, hostnames, and [special values](#network-interface-values). Defaults to the address given by `transport.host` or `network.bind_host`. Use this setting only if you require to bind to multiple addresses or to use different addresses for publishing and binding, and you also require different binding configurations for the transport and HTTP interfaces.

`transport.publish_host`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), string) The network address at which the node can be contacted by other nodes. Accepts an IP address, a hostname, or a [special value](#network-interface-values). Defaults to the address given by `transport.host` or `network.publish_host`. Use this setting only if you require to bind to multiple addresses or to use different addresses for publishing and binding, and you also require different binding configurations for the transport and HTTP interfaces.

`transport.publish_port`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), integer) The port of the [transport publish address](#modules-network-binding-publishing). Set this parameter only if you need the publish port to be different from `transport.port`. Defaults to the port assigned via `transport.port`.

`transport.connect_timeout`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), [time value](/reference/elasticsearch/rest-apis/api-conventions.md#time-units)) The connect timeout for initiating a new connection (in time setting format). Defaults to `30s`.

$$$transport-settings-compress$$$

`transport.compress` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), string) Determines which transport requests are compressed before sending them to another node. Elasticsearch will compress transport responses if and only if the corresponding request was compressed. See also `transport.compression_scheme`, which specifies the compression scheme which is used. Accepts the following values:

    `false`
    :   No transport requests are compressed. This option uses the most network bandwidth, but avoids the CPU overhead of compression and decompression.

    `indexing_data`
    :   Compresses only the raw indexing data sent between nodes during ingest, CCR following (excluding bootstrapping) and operations-based shard recovery (excluding file-based recovery which copies the raw Lucene data). This option is a good trade-off between network bandwidth savings and the extra CPU required for compression and decompression. This option is the default.

    `true`
    :   All transport requests are compressed. This option may perform better than `indexing_data` in terms of network bandwidth, but will require the most CPU for compression and decompression work.


$$$transport-settings-compression-scheme$$$

`transport.compression_scheme` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), string) Configures the compression scheme for requests which are selected for compression by to the `transport.compress` setting. Accepts either `deflate` or `lz4`, which offer different trade-offs between compression ratio and CPU usage. Elasticsearch will use the same compression scheme for responses as for the corresponding requests. Defaults to `lz4`.

`transport.tcp.keep_alive`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), boolean) Configures the `SO_KEEPALIVE` option for transport sockets, which determines whether they send TCP keepalive probes. Defaults to `network.tcp.keep_alive`.

`transport.tcp.keep_idle`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), integer) Configures the `TCP_KEEPIDLE` option for transport sockets, which determines the time in seconds that a connection must be idle before starting to send TCP keepalive probes. Defaults to `network.tcp.keep_idle` if set, or the system default otherwise. This value cannot exceed `300` seconds. In cases where the system default is higher than `300`, the value is automatically lowered to `300`. Only applicable on Linux and macOS.

`transport.tcp.keep_interval`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), integer) Configures the `TCP_KEEPINTVL` option for transport sockets, which determines the time in seconds between sending TCP keepalive probes. Defaults to `network.tcp.keep_interval` if set, or the system default otherwise. This value cannot exceed `300` seconds. In cases where the system default is higher than `300`, the value is automatically lowered to `300`. Only applicable on Linux and macOS.

`transport.tcp.keep_count`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), integer) Configures the `TCP_KEEPCNT` option for transport sockets, which determines the number of unacknowledged TCP keepalive probes that may be sent on a connection before it is dropped. Defaults to `network.tcp.keep_count` if set, or the system default otherwise. Only applicable on Linux and macOS.

`transport.tcp.no_delay`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), boolean) Configures the `TCP_NODELAY` option on transport sockets, which determines whether [TCP no delay](https://en.wikipedia.org/wiki/Nagle%27s_algorithm) is enabled. Defaults to `true`.

`transport.tcp.reuse_address`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), boolean) Configures the `SO_REUSEADDR` option for network sockets, which determines whether the address can be reused or not. Defaults to `network.tcp.reuse_address`.

`transport.tcp.send_buffer_size`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), [byte value](/reference/elasticsearch/rest-apis/api-conventions.md#byte-units)) The size of the TCP send buffer for transport traffic. Defaults to `network.tcp.send_buffer_size`.

`transport.tcp.receive_buffer_size`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), [byte value](/reference/elasticsearch/rest-apis/api-conventions.md#byte-units)) The size of the TCP receive buffer for transport traffic. Defaults to `network.tcp.receive_buffer_size`.

`transport.ping_schedule`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), [time value](/reference/elasticsearch/rest-apis/api-conventions.md#time-units)) Configures the time between sending application-level pings on all transport connections to promptly detect when a transport connection has failed. Defaults to `-1` meaning that application-level pings are not sent. You should use TCP keepalives (see `transport.tcp.keep_alive`) instead of application-level pings wherever possible.

### Transport profiles [transport-profiles]

Elasticsearch allows you to bind to multiple ports on different interfaces by the use of transport profiles. See this example configuration

```yaml
transport.profiles.default.port: 9300-9400
transport.profiles.default.bind_host: 10.0.0.1
transport.profiles.client.port: 9500-9600
transport.profiles.client.bind_host: 192.168.0.1
transport.profiles.dmz.port: 9700-9800
transport.profiles.dmz.bind_host: 172.16.1.2
```

The `default` profile is special. It is used as a fallback for any other profiles, if those do not have a specific configuration setting set, and is how this node connects to other nodes in the cluster. Other profiles can have any name and can be used to set up specific endpoints for incoming connections.

The following parameters can be configured on each transport profile, as in the example above:

* `port`: The port to which to bind.
* `bind_host`: The host to which to bind.
* `publish_host`: The host which is published in informational APIs.

Profiles also support all the other transport settings specified in the [transport settings](#transport-settings) section, and use these as defaults. For example, `transport.profiles.client.tcp.reuse_address` can be explicitly configured, and defaults otherwise to `transport.tcp.reuse_address`.


### Long-lived idle connections [long-lived-connections]

A transport connection between two nodes is made up of a number of long-lived TCP connections, some of which may be idle for an extended period of time. Nonetheless, Elasticsearch requires these connections to remain open, and it can disrupt the operation of your cluster if any inter-node connections are closed by an external influence such as a firewall. It is important to configure your network to preserve long-lived idle connections between Elasticsearch nodes, for instance by leaving `*.tcp.keep_alive` enabled and ensuring that the keepalive interval is shorter than any timeout that might cause idle connections to be closed, or by setting `transport.ping_schedule` if keepalives cannot be configured. Devices which drop connections when they reach a certain age are a common source of problems to Elasticsearch clusters, and must not be used.

If an Elasticsearch node is temporarily unable to handle network traffic it may stop reading data from the network and advertise a zero-length TCP window to its peers so that they pause the transmission of data to the unavailable node. This is the standard backpressure mechanism built into TCP. When the node becomes available again, it will resume reading from the network. Configure your network to permit TCP connections to exist in this paused state without disruption. Do not impose any limit on the length of time that a connection may remain in this paused state.

For information about troubleshooting unexpected network disconnections, see [Diagnosing other network disconnections](docs-content://troubleshoot/elasticsearch/troubleshooting-unstable-cluster.md#troubleshooting-unstable-cluster-network).


### Request compression [request-compression]

The default `transport.compress` configuration option `indexing_data` will only compress requests that relate to the transport of raw indexing source data between nodes. This option primarily compresses data sent during ingest, ccr, and shard recovery. This default normally makes sense for local cluster communication as compressing raw documents tends significantly reduce inter-node network usage with minimal CPU impact.

The `transport.compress` setting always configures local cluster request compression and is the fallback setting for remote cluster request compression. If you want to configure remote request compression differently than local request compression, you can set it on a per-remote cluster basis using the [`cluster.remote.${cluster_alias}.transport.compress` setting](docs-content://deploy-manage/remote-clusters/remote-clusters-settings.md).


### Response compression [response-compression]

The compression settings do not configure compression for responses. Elasticsearch will compress a response if the inbound request was compressed— even when compression is not enabled. Similarly, Elasticsearch will not compress a response if the inbound request was uncompressed— even when compression is enabled. The compression scheme used to compress a response will be the same scheme the remote node used to compress the request.




## Advanced remote cluster (API key based model) settings [remote-cluster-network-settings]

The section describes the advanced settings to configure the remote cluster interface ([API key-based security model](docs-content://deploy-manage/remote-clusters/remote-clusters-api-key.md)) independently of the [transport interface](#transport-settings). You can also configure both interfaces together using the [network settings](#common-network-settings).

For client settings that control how your local cluster connects to remote clusters, refer to [Remote cluster settings](/reference/elasticsearch/configuration-reference/remote-clusters.md).

`remote_cluster_server.enabled`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), boolean) Determines whether the remote cluster server should be enabled. This setting must be `true` for `remote_cluster.port` and all following remote cluster settings to take effect. Enabling it allows the cluster to serve cross-cluster requests using the API key based model. Defaults to `false`.

`remote_cluster.host`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), string) Sets the address of this node for remote cluster server traffic. The node will bind to this address and will also use it as its remote cluster server publish address. Accepts an IP address, a hostname, or a [special value](#network-interface-values). Use this setting only if you require different configurations for the remote cluster server and transport interfaces.

    Defaults to the address given by `transport.bind_host`.


`remote_cluster.bind_host`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), string) The network address(es) to which the node should bind in order to listen for incoming remote cluster connections. Accepts a list of IP addresses, hostnames, and [special values](#network-interface-values). Defaults to the address given by `remote_cluster.host`. Use this setting only if you require to bind to multiple addresses or to use different addresses for publishing and binding, and you also require different binding configurations for the remote cluster server and transport interfaces.

`remote_cluster.publish_host`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), string) The network address at which the node can be contacted by other nodes. Accepts an IP address, a hostname, or a [special value](#network-interface-values). Defaults to the address given by `remote_cluster.host`. Use this setting only if you require to bind to multiple addresses or to use different addresses for publishing and binding, and you also require different binding configurations for the remote cluster server and transport interfaces.

`remote_cluster.publish_port`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), integer) The port of the [remote cluster server publish address](#modules-network-binding-publishing). Set this parameter only if you need the publish port to be different from `remote_cluster.port`. Defaults to the port assigned via `remote_cluster.port`.

`remote_cluster.tcp.keep_alive`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), boolean) Configures the `SO_KEEPALIVE` option for remote cluster sockets, which determines whether they send TCP keepalive probes. Defaults to `transport.tcp.keep_alive`.

`remote_cluster.tcp.keep_idle`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), integer) Configures the `TCP_KEEPIDLE` option for transport sockets, which determines the time in seconds that a connection must be idle before starting to send TCP keepalive probes. Defaults to `transport.tcp.keep_idle` if set, or the system default otherwise. This value cannot exceed `300` seconds. In cases where the system default is higher than `300`, the value is automatically lowered to `300`. Only applicable on Linux and macOS.

`remote_cluster.tcp.keep_interval`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), integer) Configures the `TCP_KEEPINTVL` option for transport sockets, which determines the time in seconds between sending TCP keepalive probes. Defaults to `transport.tcp.keep_interval` if set, or the system default otherwise. This value cannot exceed `300` seconds. In cases where the system default is higher than `300`, the value is automatically lowered to `300`. Only applicable on Linux and macOS.

`remote_cluster.tcp.keep_count`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), integer) Configures the `TCP_KEEPCNT` option for transport sockets, which determines the number of unacknowledged TCP keepalive probes that may be sent on a connection before it is dropped. Defaults to `transport.tcp.keep_count` if set, or the system default otherwise. Only applicable on Linux and macOS.

`remote_cluster.tcp.no_delay`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), boolean) Configures the `TCP_NODELAY` option on transport sockets, which determines whether [TCP no delay](https://en.wikipedia.org/wiki/Nagle%27s_algorithm) is enabled. Defaults to `transport.tcp.no_delay`.

`remote_cluster.tcp.reuse_address`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), boolean) Configures the `SO_REUSEADDR` option for network sockets, which determines whether the address can be reused or not. Defaults to `transport.tcp.reuse_address`.

`remote_cluster.tcp.send_buffer_size`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), [byte value](/reference/elasticsearch/rest-apis/api-conventions.md#byte-units)) The size of the TCP send buffer for transport traffic. Defaults to `transport.tcp.send_buffer_size`.

`remote_cluster.tcp.receive_buffer_size`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), [byte value](/reference/elasticsearch/rest-apis/api-conventions.md#byte-units)) The size of the TCP receive buffer for transport traffic. Defaults to `transport.tcp.receive_buffer_size`.
