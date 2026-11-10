<!-- Converted from eql/delete-async-eql-search-api.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete async EQL search API

**New API reference**
For the most up-to-date API details, refer to [EQL APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-eql).

Deletes an async EQL search or a
stored synchronous EQL search. The API also
deletes results for the search.

```console
DELETE /_eql/search/FkpMRkJGS1gzVDRlM3g4ZzMyRGlLbkEaTXlJZHdNT09TU2VTZVBoNDM3cFZMUToxMDM=
```

#### Request

`DELETE /_eql/search/<search_id>`

#### Prerequisites

* If the Elasticsearch security features are enabled, only the following users can
use this API to delete a search:

** Users with the `cancel_task` cluster privilege
** The user who first submitted the search

* See eql-required-fields.

##### Limitations

See EQL limitations.

#### Path parameters

`<search_id>`::
(Required, string)
Identifier for the search to delete.
A search ID is provided in the EQL search API's response for
an async search. A search ID is also provided if the
request's `keep_on_completion` parameter
is `true`.
