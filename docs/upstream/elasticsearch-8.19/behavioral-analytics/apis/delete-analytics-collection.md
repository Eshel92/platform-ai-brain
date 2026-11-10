<!-- Converted from behavioral-analytics/apis/delete-analytics-collection.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete Analytics Collection

beta::[]

**New API reference**
For the most up-to-date API details, refer to [Behavioral analytics APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-analytics).

Removes a Behavioral Analytics Collection and its associated data stream.

#### Request

`DELETE _application/analytics/<name>`

#### Prerequisites

Requires the `manage_behavioral_analytics` cluster privilege.

#### Path parameters

`<name>`::
(Required, string)

#### Response codes

`400`::
The `name` was not provided.

`404` (Missing resources)::
No Analytics Collection matching `name` could be found.

#### Examples

The following example deletes the Analytics Collection named `my_analytics_collection`:

```console
DELETE _application/analytics/my_analytics_collection/
```
