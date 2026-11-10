<!-- Converted from sql/apis/delete-async-sql-search-api.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete async SQL search API

**New API reference**
For the most up-to-date API details, refer to [SQL APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-sql).

Deletes an async SQL search or a <<sql-store-searches,stored
synchronous SQL search>>. If the search is still running, the API cancels it.

```console
DELETE _sql/async/delete/FkpMRkJGS1gzVDRlM3g4ZzMyRGlLbkEaTXlJZHdNT09TU2VTZVBoNDM3cFZMUToxMDM=
```

#### Request

`DELETE _sql/async/delete/<search_id>`

#### Prerequisites

* If the Elasticsearch security features are enabled, only the following users can
use this API to delete a search:

** Users with the `cancel_task` cluster privilege
** The user who first submitted the search

##### Limitations

See sql-limitations.

#### Path parameters

`<search_id>`::
(Required, string) Identifier for the search.
