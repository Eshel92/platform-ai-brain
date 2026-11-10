<!-- Converted from query-rules/apis/delete-query-rule.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete query rule

**New API reference**
For the most up-to-date API details, refer to [Query rules APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-query_rules).

Removes an individual query rule within an existing query ruleset.
This is a destructive action that is only recoverable by re-adding the same rule via the create or update query rule API.

#### Request

`DELETE _query_rules/<ruleset_id>/_rule/<rule_id>`

#### Prerequisites

Requires the `manage_search_query_rules` privilege.

#### Path parameters

`<ruleset_id>`::
(Required, string)

`<rule_id>`::
(Required, string)

#### Response codes

`400`::
Missing `ruleset_id`, `rule_id`, or both.

`404` (Missing resources)::
No query ruleset matching `ruleset_id` could be found, or else no rule matching `rule_id` was found in that ruleset.

#### Examples

The following example deletes the query rule with ID `my-rule1` from the query ruleset named `my-ruleset`:

```console
DELETE _query_rules/my-ruleset/_rule/my-rule1
```
