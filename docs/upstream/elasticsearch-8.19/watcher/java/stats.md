<!-- Converted from watcher/java/stats.asciidoc (AsciiDoc). Includes are inlined. -->

### Watcher stats API

The `stats` API returns the current Watcher metrics. You can control what
metrics this API returns using the `metric` parameter.

The following example queries the `stats` API :

```java
WatcherStatsResponse watcherStatsResponse = watcherClient.prepareWatcherStats().get();
```

A successful call returns a response structure that can be accessed as shown:

```java
WatcherBuild build = watcherStatsResponse.getBuild();

// The current size of the watcher execution queue
long executionQueueSize = watcherStatsResponse.getThreadPoolQueueSize();

// The maximum size the watch execution queue has grown to
long executionQueueMaxSize = watcherStatsResponse.getThreadPoolQueueSize();

// The total number of watches registered in the system
long totalNumberOfWatches = watcherStatsResponse.getWatchesCount();

// {watcher} state (STARTING,STOPPED or STARTED)
WatcherState watcherState = watcherStatsResponse.getWatcherState();
```
