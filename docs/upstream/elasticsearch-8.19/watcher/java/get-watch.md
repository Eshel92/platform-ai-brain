<!-- Converted from watcher/java/get-watch.asciidoc (AsciiDoc). Includes are inlined. -->

### Get watch API

This API retrieves a watch by its id.

The following example gets a watch with `my-watch` id:

```java
GetWatchResponse getWatchResponse = watcherClient.prepareGetWatch("my-watch").get();
```

You can access the watch definition by accessing the source of the response:

```java
XContentSource source = getWatchResponse.getSource();
```

The `XContentSource` provides you methods to explore the source:

```java
Map<String, Object> map = source.getAsMap();
```

Or get a specific value associated with a known key:

```java
String host = source.getValue("input.http.request.host");
```
