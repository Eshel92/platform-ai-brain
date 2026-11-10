<!-- Converted from rest-api/watcher/update-settings.asciidoc (AsciiDoc). Includes are inlined. -->

### Update Watcher index settings

**New API reference**
For the most up-to-date API details, refer to [Watcher APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-watcher).

This API allows a user to modify the settings for the Watcher internal index (`.watches`). Only a subset of settings
are allowed to be modified. This includes:

- `index.auto_expand_replicas`
- `index.number_of_replicas`
- Any setting with the prefix `index.routing.allocation.exclude.`
- Any setting with the prefix `index.routing.allocation.include.`
- Any setting with the prefix `index.routing.allocation.require.`

Modification of `index.routing.allocation.include._tier_preference` is an exception and is not allowed as the Watcher
shards must always be in the `data_content` tier.

An example of modifying the Watcher settings:

```console
PUT /_watcher/watch/test_watch
{
  "trigger": {
    "schedule": {
      "hourly": {
        "minute": [ 0, 5 ]
        }
      }
  },
  "input": {
    "simple": {
      "payload": {
        "send": "yes"
      }
    }
  },
  "condition": {
    "always": {}
  }
}
```

```console
PUT /_watcher/settings
{
  "index.auto_expand_replicas": "0-4"
}
```

The configurable settings can be retrieved using the Get Watcher index settings API.
