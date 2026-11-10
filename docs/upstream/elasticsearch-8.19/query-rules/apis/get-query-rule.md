<!-- Converted from query-rules/apis/get-query-rule.asciidoc (AsciiDoc). Includes are inlined. -->

### Get query rule

**New API reference**
For the most up-to-date API details, refer to [Query rules APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-query_rules).

Retrieves information about an individual query rule within a query ruleset.

#### Request

`GET _query_rules/<ruleset_id>/_rule/<rule_id>`

#### Prerequisites

Requires the `manage_search_query_rules` privilege.

#### Path parameters

`<ruleset_id>`::
(Required, string)

`<rule_id>`::
(Required, string)

#### Response codes

`400`::
Missing `ruleset_id` or `rule_id`, or both.

`404` (Missing resources)::
Either no query ruleset matching `ruleset_id` could be found, or no rule matching `rule_id` could be found within that ruleset.

#### Examples

The following example gets the query rule with ID `my-rule1` from the ruleset named `my-ruleset`:

```console
GET _query_rules/my-ruleset/_rule/my-rule1
```

A sample response:

```console-result
{
    "rule_id": "my-rule1",
    "type": "pinned",
    "criteria": [
        {
            "type": "contains",
            "metadata": "query_string",
            "values": [ "pugs", "puggles" ]
        }
    ],
    "actions": {
        "ids": [
            "id1",
            "id2"
        ]
    }
}
```
