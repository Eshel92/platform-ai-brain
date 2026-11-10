<!-- Converted from search-application/apis/list-search-applications.asciidoc (AsciiDoc). Includes are inlined. -->

### List Search Applications

**New API reference**
For the most up-to-date API details, refer to [Search application APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-search_application).

beta::[]

Returns information about Search Applications.

#### Request

`GET _application/search_application/`

#### Prerequisites

Requires the `manage_search_application` cluster privilege.

#### Path parameters

`q`::
(Optional, string) Query in the Lucene query string syntax, to return only search applications matching the query.

`size`::
(Optional, integer) Maximum number of results to retrieve.

`from`::
(Optional, integer) The offset from the first result to fetch.

#### Response codes

#### Examples

The following example lists all configured search applications:

```console
GET _application/search_application/
```

The following example queries the first three search applications whose names start with `app`:

```console
GET _application/search_application?from=0&size=3&q=app*
```

A sample response:

```console-result
{
  "count": 2,
  "results": [
    {
      "name": "app-1",
      "updated_at_millis": 1690981129366
    },
    {
      "name": "app-2",
      "updated_at_millis": 1691501823939
    }
  ]
}
```
