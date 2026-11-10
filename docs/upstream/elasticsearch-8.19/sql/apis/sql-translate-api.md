<!-- Converted from sql/apis/sql-translate-api.asciidoc (AsciiDoc). Includes are inlined. -->

### SQL translate API

**New API reference**
For the most up-to-date API details, refer to [SQL APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-sql).

Translates an SQL search into a search API
request containing Query DSL. See sql-translate.

```console
POST _sql/translate
{
  "query": "SELECT * FROM library ORDER BY page_count DESC",
  "fetch_size": 10
}
```

#### Request

`GET _sql/translate`

`POST _sql/translate`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `read`
index privilege for the data stream, index,
or alias you search.

##### Limitations

See sql-limitations.

#### Request body

The SQL translate API accepts the same request body parameters as the
SQL search API, excluding `cursor`.

#### Response body

The SQL translate API returns the same response body as the
search API.
