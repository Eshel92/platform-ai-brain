<!-- Converted from query-rules/apis/test-query-ruleset.asciidoc (AsciiDoc). Includes are inlined. -->

### Test query ruleset

**New API reference**
For the most up-to-date API details, refer to [Query rules APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-query_rules).

Evaluates match criteria against a query ruleset to identify the rules that would match that criteria.

preview::[]

#### Request

`POST _query_rules/<ruleset_id>/_test`

#### Prerequisites

Requires the `manage_search_query_rules` privilege.

#### Path parameters

`<ruleset_id>`::
(Required, string)

#### Request body

`match_criteria`::
(Required, object) Defines the match criteria to apply to rules in the given query ruleset.
Match criteria should match the keys defined in the `criteria.metadata` field of the rule.

#### Response codes

`400`::
The `ruleset_id` or `match_criteria` were not provided.

`404` (Missing resources)::
No query ruleset matching `ruleset_id` could be found.

#### Examples

To test a ruleset, provide the match criteria that you want to test against:

```console
POST _query_rules/my-ruleset/_test
{
    "match_criteria": {
        "query_string": "puggles"
    }
}
```

A sample response:

```console-result
{
    "total_matched_rules": 1,
    "matched_rules": [
        {
            "ruleset_id": "my-ruleset",
            "rule_id": "my-rule1"
        }
    ]
}
```
