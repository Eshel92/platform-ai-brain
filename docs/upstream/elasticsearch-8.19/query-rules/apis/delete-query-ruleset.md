<!-- Converted from query-rules/apis/delete-query-ruleset.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete query ruleset

**New API reference**
For the most up-to-date API details, refer to [Query rules APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-query_rules).

Removes a query ruleset and its associated data.
This is a destructive action that is not recoverable.

#### Request

`DELETE _query_rules/<ruleset_id>`

#### Prerequisites

Requires the `manage_search_query_rules` privilege.

#### Path parameters

`<ruleset_id>`::
(Required, string)

#### Response codes

`400`::
The `ruleset_id` was not provided.

`404` (Missing resources)::
No query ruleset matching `ruleset_id` could be found.

#### Examples

The following example deletes the query ruleset named `my-ruleset`:

```console
DELETE _query_rules/my-ruleset/
```
