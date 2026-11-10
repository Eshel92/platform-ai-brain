<!-- Converted from api/upgrade-assistant/cancel_reindex.asciidoc (AsciiDoc). Includes are inlined. -->

### Cancel reindex API

experimental["The underlying Upgrade Assistant concepts are stable, but the APIs for managing Upgrade Assistant are experimental."]

Cancel reindexes that are waiting for the Elasticsearch reindex task to complete. For example, `lastCompletedStep` set to `40`.

#### Request

`POST <kibana host>:<port>/api/upgrade_assistant/reindex/myIndex/cancel`

#### Response codes

`200`::
  Indicates a successful call.

#### Example

The API returns the following:

```sh
{
  "acknowledged": true
}
```
