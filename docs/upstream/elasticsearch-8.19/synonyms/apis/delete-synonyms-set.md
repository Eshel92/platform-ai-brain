<!-- Converted from synonyms/apis/delete-synonyms-set.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete synonyms set

**New API reference**
For the most up-to-date API details, refer to [Synonyms APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-synonyms).

Deletes a synonyms set.

#### Request

`DELETE _synonyms/<synonyms_set>`

#### Prerequisites

* Requires the `manage_search_synonyms` cluster privilege.
* You can only delete a synonyms set that is not in use by any index analyzer. See delete-synonym-set-analyzer-requirements for more information.

#### Path parameters

`<synonyms_set>`::
(Required, string)
Synonyms set identifier to delete.

#### Response codes

`400`::
The `synonyms_set` identifier was not provided, or the synonyms set can't be deleted because it does not meet the specified requirements.

`404` (Missing resources)::
No synonyms set with the identifier `synonyms_set` was found.

#### Examples

The following example deletes a synonyms set called `my-synonyms-set`:

```console
DELETE _synonyms/my-synonyms-set
```

#### Delete synonyms set analyzer requirements

synonyms sets can be used in  synonym graph token filters and synonym token filters.
These synonym filters can be used as part of search analyzers.

Analyzers need to be loaded when an index is restored (such as when a node starts, or the index becomes open).
Even if the analyzer is not used on any field mapping, it still needs to be loaded on the index recovery phase.

If any analyzers cannot be loaded, the index becomes unavailable and the cluster status becomes red or yellow as index shards are not available.

To prevent that, synonyms sets that are used in analyzers can't be deleted.
A delete request in this case will return a `400` response code with the following error message:

```console-result
{
  "error": {
    "root_cause": [
      {
        "type": "illegal_argument_exception",
        "reason": "synonyms set [my-synonyms-set] cannot be deleted as it is used in the following indices: index-1, index-2",
        "stack_trace": ...
      }
    ],
    "type": "illegal_argument_exception",
    "reason": "synonyms set [my-synonyms-set] cannot be deleted as it is used in the following indices: index-1, index-2",
    "stack_trace": ...
  },
  "status": 400
}
```

To remove a synonyms set, you must first remove all indices that contain analyzers using it.
You can migrate an index by creating a new index that does not contain the token filter with the synonyms set, and use the docs-reindex in order to copy over the index data.
Once finished, you can delete the index.

When the synonyms set is not used in analyzers, you will be able to delete it.
