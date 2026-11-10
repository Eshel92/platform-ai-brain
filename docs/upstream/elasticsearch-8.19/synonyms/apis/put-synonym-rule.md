<!-- Converted from synonyms/apis/put-synonym-rule.asciidoc (AsciiDoc). Includes are inlined. -->

### Create or update synonym rule

**New API reference**
For the most up-to-date API details, refer to [Synonyms APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-synonyms).

Creates or updates a synonym rule for a synonym set.

#### Request

`PUT _synonyms/<synonyms_set>/<synonym_rule>`

#### Prerequisites

Requires the `manage_search_synonyms` cluster privilege.

#### Path parameters

`<synonyms_set>`::
(Required, string)
Synonyms set identifier to update.

`<synonym_rule>`::
(Required, string)
Synonym rule identifier to create or update.

#### Request body

`synonyms`::
(Required, string)
The synonym rule definition.
This needs to be in Solr format. Some examples are:

* "i-pod, i pod => ipod",
* "universe, cosmos"

#### Examples

The following example updates an existing synonym rule called `test-1` for the synonyms set `my-synonyms-set`:

```console
PUT _synonyms/my-synonyms-set/test-1
{
  "synonyms": "hello, hi, howdy"
}
```

```console-result
{
  "result": "updated",
  "reload_analyzers_details": {
    "_shards": {
      "total": 2,
      "successful": 1,
      "failed": 0
    },
    "reload_details": [
      {
        "index": "test-index",
        "reloaded_analyzers": [
          "my_search_analyzer"
        ],
        "reloaded_node_ids": [
          "1wYFZzq8Sxeu_Jvt9mlbkg"
        ]
      }
    ]
  }
}
```

All analyzers using this synonyms set will be reloaded automatically to reflect the new rule.

If any of the synonym rules included is invalid, the API will return an error.

```console
PUT _synonyms/my-synonyms-set/test-1
{
  "synonyms": "hello => hi => howdy"
}
```

```console-result
{
  "error": {
    "root_cause": [
      {
        "type": "action_request_validation_exception",
        "reason": "Validation Failed: 1: More than one explicit mapping specified in the same synonyms rule: [hello => hi => howdy];",
        "stack_trace": ...
      }
    ],
    "type": "action_request_validation_exception",
    "reason": "Validation Failed: 1: More than one explicit mapping specified in the same synonyms rule: [hello => hi => howdy];",
    "stack_trace": ...
  },
  "status": 400
}
```
