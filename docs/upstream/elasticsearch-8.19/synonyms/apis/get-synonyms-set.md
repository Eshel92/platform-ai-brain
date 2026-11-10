<!-- Converted from synonyms/apis/get-synonyms-set.asciidoc (AsciiDoc). Includes are inlined. -->

### Get synonyms set

**New API reference**
For the most up-to-date API details, refer to [Synonyms APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-synonyms).

Retrieves a synonyms set.

#### Request

`GET _synonyms/<synonyms_set>`

#### Prerequisites

Requires the `manage_search_synonyms` cluster privilege.

#### Path parameters

`<synonyms_set>`::
(Required, string)
Synonyms set identifier to retrieve.

#### Query parameters

`from`::
(Optional, integer) Starting offset for synonyms rules to retrieve. Defaults to `0`.

`size`::
(Optional, integer) Specifies the maximum number of synonyms rules to retrieve. Defaults to `10`.

#### Response codes

`400`::
The `synonyms_set` identifier was not provided.

`404` (Missing resources)::
No synonyms set with the identifier `synonyms_set` was found.

#### Examples

The following example retrieves a synonyms set called `my-synonyms-set`:

```console
GET _synonyms/my-synonyms-set
```

The synonyms set information returned will include the total number of synonyms rules that the synonyms set contains, and the synonyms rules according to the `from` and `size` parameters.

A sample response:

```console-result
{
  "count": 3,
  "synonyms_set": [
    {
      "id": "test-1",
      "synonyms": "hello, hi"
    },
    {
      "id": "test-2",
      "synonyms": "bye, goodbye"
    },
    {
      "id": "test-3",
      "synonyms": "test => check"
    }
  ]
}
```
