<!-- Converted from watcher/java/service.asciidoc (AsciiDoc). Includes are inlined. -->

### Watcher service API

The Watcher `service` API allows the control the lifecycle of the Watcher
service. The following example starts the watcher service:

```java
WatcherServiceResponse watcherServiceResponse = watcherClient.prepareWatchService().start().get();
```

The following example stops the watcher service:

```java
WatcherServiceResponse watcherServiceResponse = watcherClient.prepareWatchService().stop().get();
```

The following example restarts the watcher service:

```java
WatcherServiceResponse watcherServiceResponse = watcherClient.prepareWatchService().restart().get();
```
