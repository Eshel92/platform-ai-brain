<!-- Converted from query-rules/apis/list-query-rulesets.asciidoc (AsciiDoc). Includes are inlined. -->

### List query rulesets

**New API reference**
For the most up-to-date API details, refer to [Query rules APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-query_rules).

Returns information about all stored query rulesets.
Summary information on the number of rules per ruleset will be returned, and full details can be returned with the get-query-ruleset command.

#### Request

`GET _query_rules/`

#### Prerequisites

Requires the `manage_search_query_rules` privilege.

#### Path parameters

`size`::
(Optional, integer) Maximum number of results to retrieve.

`from`::
(Optional, integer) The offset from the first result to fetch.

#### Examples

The following example lists all configured query rulesets:

```console
GET _query_rules/
```

The following example lists the first three query rulesets:

```console
GET _query_rules/?from=0&size=3
```

A sample response:

```console-result
{
    "count": 3,
    "results": [
        {
            "ruleset_id": "ruleset-1",
            "rule_total_count": 1,
            "rule_criteria_types_counts": {
                "exact": 1
            },
            "rule_type_counts": {
                "pinned": 1
            }
        },
        {
            "ruleset_id": "ruleset-2",
            "rule_total_count": 2,
            "rule_criteria_types_counts": {
                "exact": 1,
                "fuzzy": 1
            },
            "rule_type_counts": {
                "pinned": 2
            }
        },
        {
            "ruleset_id": "ruleset-3",
            "rule_total_count": 3,
            "rule_criteria_types_counts": {
                "exact": 1,
                "fuzzy": 2
            },
            "rule_type_counts": {
                "pinned": 2,
                "exclude": 1
            }
        }
    ]
}
```

The counts in `rule_criteria_types_counts` may be larger than the value of `rule_total_count`, because a rule may have multiple criteria.
