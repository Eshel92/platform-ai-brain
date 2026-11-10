<!-- Converted from synonyms/apis/get-synonym-rule.asciidoc (AsciiDoc). Includes are inlined. -->

### Get synonym rule

**New API reference**
For the most up-to-date API details, refer to [Synonyms APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-synonyms).

Retrieves a synonym rule from a synonyms set.

#### Request

`GET _synonyms/<synonyms_set>/<synonym_rule>`

#### Prerequisites

Requires the `manage_search_synonyms` cluster privilege.

#### Path parameters

`<synonyms_set>`::
(Required, string)
Synonyms set identifier to retrieve the synonym rule from.

`<synonym_rule>`::
(Required, string)
Synonym rule identifier to retrieve.

#### Response codes

`404` (Missing resources)::
The `synonyms_set` identifier was not found, or the synonym rule specified by `synonym_rule` was not found in the synonyms set.

#### Examples

The following example retrieves an existing synonym rule called `test-1` for the synonyms set `my-synonyms-set`:

```console
GET _synonyms/my-synonyms-set/test-1
```

```console-result
{
  "id": "test-1",
  "synonyms": "hello, hi"
}
```
