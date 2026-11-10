<!-- Converted from watcher/java/delete-watch.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete watch API

The delete watch API removes a watch (identified by its `id`) from Watcher.
Once removed, the document representing the watch in the `.watches` index is
gone and it will never be executed again.

Please note that deleting a watch **does not** delete any watch execution records
related to this watch from the watch history.

**Important:** Deleting a watch must be done via this API only. Do not delete the
            watch directly from the `.watches` index using Elasticsearch's DELETE
            Document API. If the Elasticsearch security features are enabled, make sure
            no `write` privileges are granted to anyone over the `.watches` index.

The following example deletes a watch with the `my-watch` id:

```java
DeleteWatchResponse deleteWatchResponse = watcherClient.prepareDeleteWatch("my-watch").get();
```
