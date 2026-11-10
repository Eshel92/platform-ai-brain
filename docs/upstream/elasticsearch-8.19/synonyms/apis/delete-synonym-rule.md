<!-- Converted from synonyms/apis/delete-synonym-rule.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete synonym rule

**New API reference**
For the most up-to-date API details, refer to [Synonyms APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-synonyms).

Deletes an individual synonym rule from a synonyms set.

#### Request

`DELETE _synonyms/<synonyms_set>/<synonym_rule>`

#### Prerequisites

Requires the `manage_search_synonyms` cluster privilege.

#### Path parameters

`<synonyms_set>`::
(Required, string)
Synonyms set identifier to update.

`<synonym_rule>`::
(Required, string)
Synonym rule identifier to delete.

#### Response codes

`404` (Missing resources)::
The `synonyms_set` identifier was not found, or the synonym rule specified by `synonym_rule` was not found in the synonyms set.

#### Examples

The following example deletes an existing synonym rule called `test-1` for the synonyms set `my-synonyms-set`:

```console
DELETE _synonyms/my-synonyms-set/test-1
```

```console-result
{
  "result": "deleted",
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

All analyzers using this synonyms set will be reloaded automatically to reflect the rule being deleted.
