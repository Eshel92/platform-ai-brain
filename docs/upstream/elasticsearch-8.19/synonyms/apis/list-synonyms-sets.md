<!-- Converted from synonyms/apis/list-synonyms-sets.asciidoc (AsciiDoc). Includes are inlined. -->

### List synonyms sets

**New API reference**
For the most up-to-date API details, refer to [Synonyms APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-synonyms).

Retrieves a summary of all defined synonyms sets.

This API allows to retrieve the total number of synonyms sets defined.
For each synonyms set, its identifier and the total number of defined synonym rules is returned.

#### Request

`GET _synonyms`

#### Prerequisites

Requires the `manage_search_synonyms` cluster privilege.

#### Query parameters

`from`::
(Optional, integer) Starting offset for synonyms sets to retrieve. Defaults to `0`.

`size`::
(Optional, integer) Specifies the maximum number of synonyms sets to retrieve. Defaults to `10`.

#### Examples

The following example retrieves all defined synonyms sets:

```console
GET _synonyms
```

A sample response:

```console-result
{
  "count": 3,
  "results": [
    {
      "synonyms_set": "ecommerce-synonyms",
      "count": 2
    },
    {
      "synonyms_set": "my-synonyms-set",
      "count": 3
    },
    {
      "synonyms_set": "new-ecommerce-synonyms",
      "count": 1
    }
  ]
}
```
