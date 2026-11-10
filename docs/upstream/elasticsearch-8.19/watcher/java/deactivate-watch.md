<!-- Converted from watcher/java/deactivate-watch.asciidoc (AsciiDoc). Includes are inlined. -->

### Deactivate watch API

A watch can be either active or inactive. This API
enables you to deactivate a currently active watch.

The status of an active watch is returned with the watch definition
when you call the get watch API:

```java
GetWatchResponse getWatchResponse = watcherClient.prepareGetWatch("my-watch").get();
boolean active = getWatchResponse.getStatus().state().isActive();
```

The following snippet shows how you can deactivate a watch:

```java
ActivateWatchResponse activateResponse = watcherClient.prepareActivateWatch("my-watch", false).get();
boolean active = activateResponse.getStatus().state().isActive();
```

The new state of the watch is returned as part of its overall status.
