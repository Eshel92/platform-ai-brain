<!-- Converted from rest-api/watcher/get-settings.asciidoc (AsciiDoc). Includes are inlined. -->

### Get Watcher index settings

**New API reference**
For the most up-to-date API details, refer to [Watcher APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-watcher).

This API allows a user to retrieve the user-configurable settings for the Watcher internal index (`.watches`). Only a subset of the index settings—those that are user-configurable—will be shown. This includes:

- `index.auto_expand_replicas`
- `index.number_of_replicas`

An example of retrieving the Watcher settings:

```console
GET /_watcher/settings
```

The configurable settings can be modified using the Update Watcher index settings API.
