<!-- Converted from query-rules/apis/get-query-ruleset.asciidoc (AsciiDoc). Includes are inlined. -->

### Get query ruleset

**New API reference**
For the most up-to-date API details, refer to [Query rules APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-query_rules).

Retrieves information about a query ruleset.

#### Request

`GET _query_rules/<ruleset_id>`

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

The following example gets the query ruleset named `my-ruleset`:

```console
GET _query_rules/my-ruleset/
```

A sample response:

```console-result
{
    "ruleset_id": "my-ruleset",
    "rules": [
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
        },
        {
            "rule_id": "my-rule2",
            "type": "pinned",
            "criteria": [
                {
                    "type": "fuzzy",
                    "metadata": "query_string",
                    "values": [ "rescue dogs" ]
                }
            ],
            "actions": {
                "docs": [
                    {
                        "_index": "index1",
                        "_id": "id3"
                    },
                    {
                        "_index": "index2",
                        "_id": "id4"
                    }
                ]
            }
        }
    ]
}
```
