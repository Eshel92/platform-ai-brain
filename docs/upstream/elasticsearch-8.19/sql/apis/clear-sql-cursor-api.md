<!-- Converted from sql/apis/clear-sql-cursor-api.asciidoc (AsciiDoc). Includes are inlined. -->

### Clear SQL cursor API

**New API reference**
For the most up-to-date API details, refer to [SQL APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-sql).

Clears an SQL search cursor.

```console
POST _sql/close
{
  "cursor": "sDXF1ZXJ5QW5kRmV0Y2gBAAAAAAAAAAEWYUpOYklQMHhRUEtld3RsNnFtYU1hQQ==:BAFmBGRhdGUBZgVsaWtlcwFzB21lc3NhZ2UBZgR1c2Vy9f///w8="
}
```

#### Request

`POST _sql/close`

##### Limitations

See sql-limitations.

#### Request body

`cursor`::
(Required, string) Cursor to clear.
