<!-- Converted from api/upgrade-assistant/status.asciidoc (AsciiDoc). Includes are inlined. -->

### Upgrade readiness status API

experimental["The underlying Upgrade Assistant concepts are stable, but the APIs for managing Upgrade Assistant are experimental."]

Check the status of your cluster.

#### Request

`GET <kibana host>:<port>/api/upgrade_assistant/status?targetVersion=9.0.0`

`targetVersion`::
(optional, string): Version to upgrade to.

#### Response codes

`200`::
  Indicates a successful call.
  
`403`::
  Indicates a forbidden request when the upgrade path is not supported (e.g. upgrading more than 1 major or downgrading)

#### Example

The API returns the following:

```sh
{
  "readyForUpgrade": false,
  "details":"The following issues must be resolved before upgrading: 1 Elasticsearch deprecation issue."
}
```
