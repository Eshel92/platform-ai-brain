<!-- Converted from watcher/java/activate-watch.asciidoc (AsciiDoc). Includes are inlined. -->

### Activate watch API

A watch can be either active or inactive. This API
enables you to activate a currently inactive watch.

The status of an inactive watch is returned with the watch definition
when you call the get watch API:

```java
GetWatchResponse getWatchResponse = watcherClient.prepareGetWatch("my-watch").get();
boolean active = getWatchResponse.getStatus().state().isActive();
```

The following snippet shows how you can activate a watch:

```java
ActivateWatchResponse activateResponse = watcherClient.prepareActivateWatch("my-watch", true).get();
boolean active = activateResponse.getStatus().state().isActive();
```

The new state of the watch is returned as part of its overall status.
