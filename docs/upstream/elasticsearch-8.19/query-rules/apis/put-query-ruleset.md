<!-- Converted from query-rules/apis/put-query-ruleset.asciidoc (AsciiDoc). Includes are inlined. -->

### Create or update query ruleset

**New API reference**
For the most up-to-date API details, refer to [Query rules APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-query_rules).

Creates or updates a query ruleset.

#### Request

`PUT _query_rules/<ruleset_id>`

#### Prerequisites

Requires the `manage_search_query_rules` privilege.

(Required, object) Contains parameters for a query ruleset:

#### Request body

`rules`::
(Required, array of objects) The specific rules included in this query ruleset.

There is a limit of 100 rules per ruleset.
This can be increased up to 1000 using the `xpack.applications.rules.max_rules_per_ruleset` cluster setting.

Each rule must have the following information:

- `rule_id` (Required, string) A unique identifier for this rule.
- `type` (Required, string) The type of rule.
At this time only `pinned` and `exclude` query rule types are allowed.
- `criteria` (Required, array of objects) The criteria that must be met for the rule to be applied.
If multiple criteria are specified for a rule, all criteria must be met for the rule to be applied.
- `actions` (Required, object) The actions to take when the rule is matched.
The format of this action depends on the rule type.

Criteria must have the following information:

- `type` (Required, string) The type of criteria.
The following criteria types are supported:
- `exact`
Only exact matches meet the criteria defined by the rule.
Applicable for string or numerical values.
- `fuzzy`
Exact matches or matches within the allowed [Levenshtein Edit Distance](https://en.wikipedia.org/wiki/Levenshtein_distance) meet the criteria defined by the rule.
Only applicable for string values.
- `prefix`
Matches that start with this value meet the criteria defined by the rule.
Only applicable for string values.
- `suffix`
Matches that end with this value meet the criteria defined by the rule.
Only applicable for string values.
- `contains`
Matches that contain this value anywhere in the field meet the criteria defined by the rule.
Only applicable for string values.
- `lt`
Matches with a value less than this value meet the criteria defined by the rule.
Only applicable for numerical values.
- `lte`
Matches with a value less than or equal to this value meet the criteria defined by the rule.
Only applicable for numerical values.
- `gt`
Matches with a value greater than this value meet the criteria defined by the rule.
Only applicable for numerical values.
- `gte`
Matches with a value greater than or equal to this value meet the criteria defined by the rule.
Only applicable for numerical values.
- `always`
Matches all queries, regardless of input.
- `metadata` (Optional, string) The metadata field to match against.
This metadata will be used to match against `match_criteria` sent in the query-dsl-rule-query.
Required for all criteria types except `always`.
- `values` (Optional, array of strings) The values to match against the metadata field.
Only one value must match for the criteria to be met.
Required for all criteria types except `always`.

Actions depend on the rule type.
The following actions are allowed for `pinned` or `exclude` rules:

- `ids` (Optional, array of strings) The unique document IDs of the documents to apply the rule to.
Only one of `ids` or `docs` may be specified, and at least one must be specified.
- `docs` (Optional, array of objects) The documents to apply the rule to.
Only one of `ids` or `docs` may be specified, and at least one must be specified.
There is a maximum value of 100 documents in a rule.
You can specify the following attributes for each document:
- `_index` (Required, string) The index of the document to pin.
- `_id` (Required, string) The unique document ID.

**Important:** Due to limitations within Pinned queries, you can only select documents using `ids` or `docs`, but cannot use both in single rule.
It is advised to use one or the other in query rulesets, to avoid errors.
Additionally, pinned queries have a maximum limit of 100 pinned hits.
If multiple matching rules pin more than 100 documents, only the first 100 documents are pinned in the order they are specified in the ruleset.

#### Examples

The following example creates a new query ruleset called `my-ruleset`.

Two rules are associated with `my-ruleset`:

- `my-rule1` will pin documents with IDs `id1` and `id2` when `user_query` contains `pugs` _or_ `puggles` **and** `user_country` exactly matches `us`.
- `my-rule2` will exclude documents from different, specified indices with IDs `id3` and `id4` when the `query_string` fuzzily matches `rescue dogs`.

```console
PUT _query_rules/my-ruleset
{
    "rules": [
        {
            "rule_id": "my-rule1",
            "type": "pinned",
            "criteria": [
                {
                    "type": "contains",
                    "metadata": "user_query",
                    "values": [ "pugs", "puggles" ]
                },
                {
                    "type": "exact",
                    "metadata": "user_country",
                    "values": [ "us" ]
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
            "type": "exclude",
            "criteria": [
                {
                    "type": "fuzzy",
                    "metadata": "user_query",
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

```console
DELETE _query_rules/my-ruleset
```
