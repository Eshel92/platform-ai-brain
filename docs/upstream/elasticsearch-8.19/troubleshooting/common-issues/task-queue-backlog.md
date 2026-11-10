<!-- Converted from troubleshooting/common-issues/task-queue-backlog.asciidoc (AsciiDoc). Includes are inlined. -->

### Task queue backlog

A backlogged task queue can prevent tasks from completing and put the cluster
into an unhealthy state. Resource constraints, a large number of tasks being
triggered at once, and long running tasks can all contribute to a backlogged
task queue.

#### Diagnose a task queue backlog

**Check the thread pool status**

A depleted thread pool can result in
rejected requests. 

Thread pool depletion might be restricted to a specific data tier. If hot spotting is occuring, one node might experience depletion faster than other nodes, leading to performance issues and a growing task backlog.

You can use the cat thread pool API to see the number of
active threads in each thread pool and how many tasks are queued, how many
have been rejected, and how many have completed.

```console
GET /_cat/thread_pool?v&s=t,n&h=type,name,node_name,active,queue,rejected,completed
```

The `active` and `queue` statistics are instantaneous while the `rejected` and
`completed` statistics are cumulative from node startup.

**Inspect the hot threads on each node**

If a particular thread pool queue is backed up, you can periodically poll the
Nodes hot threads API to determine if the thread
has sufficient resources to progress and gauge how quickly it is progressing.

```console
GET /_nodes/hot_threads
```

**Look for long running node tasks**

Long-running tasks can also cause a backlog. You can use the <<tasks,task
management>> API to get information about the node tasks that are running.
Check the `running_time_in_nanos` to identify tasks that are taking an
excessive amount of time to complete.

```console
GET /_tasks?pretty=true&human=true&detailed=true
```

If a particular `action` is suspected, you can filter the tasks further. The most common long-running tasks are bulk index- or search-related.

* Filter for bulk index actions:
```console
GET /_tasks?human&detailed&actions=indices:data/write/bulk
```

* Filter for search actions:
```console
GET /_tasks?human&detailed&actions=indices:data/write/search
```

The API response may contain additional tasks columns, including `description` and `header`, which provides the task parameters, target, and requestor. You can use this information to perform further diagnosis.

**Look for long running cluster tasks**

A task backlog might also appear as a delay in synchronizing the cluster state. You
can use the cluster pending tasks API to get information
about the pending cluster state sync tasks that are running. 

```console
GET /_cluster/pending_tasks
```

Check the `timeInQueue` to identify tasks that are taking an excessive amount 
of time to complete.

#### Resolve a task queue backlog

**Increase available resources** 

If tasks are progressing slowly and the queue is backing up, 
you might need to take steps to reduce-cpu-usage. 

In some cases, increasing the thread pool size might help.
For example, the `force_merge` thread pool defaults to a single thread.
Increasing the size to 2 might help reduce a backlog of force merge requests.

**Cancel stuck tasks**

If you find the active task's hot thread isn't progressing and there's a backlog, 
consider canceling the task.
