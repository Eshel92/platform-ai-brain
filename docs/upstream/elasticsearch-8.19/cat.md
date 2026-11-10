<!-- Converted from cat.asciidoc (AsciiDoc). Includes are inlined. -->

## Compact and aligned text (CAT) APIs

**New API reference**
For the most up-to-date API details, refer to [Compact and aligned text (CAT) APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cat).

### Introduction

JSON is great... for computers. Even if it's pretty-printed, trying
to find relationships in the data is tedious. Human eyes, especially
when looking at a terminal, need compact and aligned text. The compact and
aligned text (CAT) APIs aim to meet this need.

**Important:**
cat APIs are only intended for human consumption using the
[Kibana console](https://www.elastic.co/guide/en/kibana/8.19/console-kibana.html) or command line. They are _not_
intended for use by applications. For application consumption, we recommend
using a corresponding JSON API.

All the cat commands accept a query string parameter `help` to see all
the headers and info they provide, and the `/_cat` command alone lists all
the available commands.

### Common parameters

#### Verbose

Each of the commands accepts a query string parameter `v` to turn on
verbose output. For example:

```console
GET _cat/master?v=true
```

Might respond with:

```txt
id                     host      ip        node
u_n93zwxThWHi1PDBJAGAg 127.0.0.1 127.0.0.1 u_n93zw
```

#### Help

Each of the commands accepts a query string parameter `help` which will
output its available columns. For example:

```console
GET _cat/master?help
```

Might respond with:

```txt
id   |   | node id
host | h | host name
ip   |   | ip address
node | n | node name
```

**Note:** `help` is not supported if any optional url parameter is used.
For example `GET _cat/shards/my-index-000001?help` or `GET _cat/indices/my-index-*?help`
results in an error. Use `GET _cat/shards?help` or `GET _cat/indices?help`
instead.

#### Headers

Each of the commands accepts a query string parameter `h` which forces
only those columns to appear. For example:

```console
GET _cat/nodes?h=ip,port,heapPercent,name
```

Responds with:

```txt
127.0.0.1 9300 27 sLBaIGK
```

You can also request multiple columns using simple wildcards like
`/_cat/thread_pool?h=ip,queue*` to get all headers (or aliases) starting
with `queue`.

#### Numeric formats

Many commands provide a few types of numeric output, either a byte, size
or a time value. By default, these types are human-formatted,
for example, `3.5mb` instead of `3763212`. The human values are not
sortable numerically, so in order to operate on these values where
order is important, you can change it.

Say you want to find the largest index in your cluster (storage used
by all the shards, not number of documents). The `/_cat/indices` API
is ideal. You only need to add three things to the API request:

. The `bytes` query string parameter with a value of `b` to get byte-level resolution.
. The `s` (sort) parameter with a value of `store.size:desc` and a comma with `index:asc` to sort the output
by shard storage descending order and then index name in ascending order.
. The `v` (verbose) parameter to include column headings in the response.

```console
GET _cat/indices?bytes=b&s=store.size:desc,index:asc&v=true
```

The API returns the following response:

```txt
health status index            uuid                   pri rep docs.count docs.deleted store.size pri.store.size dataset.size
yellow open   my-index-000001  u8FNjxh8Rfy_awN11oDKYQ   1   1       1200            0      72171         72171         72171
green  open   my-index-000002  nYFWZEO7TUiOjLQXBaYJpA   1   0          0            0        230          230            230
```

If you want to change the time units, use `time` parameter.

If you want to change the size units, use `size` parameter.

If you want to change the byte units, use `bytes` parameter.

#### Response as text, json, smile, yaml or cbor

```sh
% curl 'localhost:9200/_cat/indices?format=json&pretty'
[
  {
    "pri.store.size": "650b",
    "health": "yellow",
    "status": "open",
    "index": "my-index-000001",
    "pri": "5",
    "rep": "1",
    "docs.count": "0",
    "docs.deleted": "0",
    "store.size": "650b"
  }
]
```

Currently supported formats (for the `?format=` parameter):
- text (default)
- json
- smile
- yaml
- cbor

Alternatively you can set the "Accept" HTTP header to the appropriate media format.
All formats above are supported, the GET parameter takes precedence over the header.
For example:

```sh
% curl '192.168.56.10:9200/_cat/indices?pretty' -H "Accept: application/json"
[
  {
    "pri.store.size": "650b",
    "health": "yellow",
    "status": "open",
    "index": "my-index-000001",
    "pri": "5",
    "rep": "1",
    "docs.count": "0",
    "docs.deleted": "0",
    "store.size": "650b"
  }
]
```

#### Sort

Each of the commands accepts a query string parameter `s` which sorts the table by
the columns specified as the parameter value. Columns are specified either by name or by
alias, and are provided as a comma separated string. By default, sorting is done in
ascending fashion. Appending `:desc` to a column will invert the ordering for
that column. `:asc` is also accepted but exhibits the same behavior as the default sort order.

For example, with a sort string `s=column1,column2:desc,column3`, the table will be
sorted in ascending order by column1, in descending order by column2, and in ascending
order by column3.

```console
GET _cat/templates?v=true&s=order:desc,index_patterns
```

returns:

```txt
name                  index_patterns order version
pizza_pepperoni       [*pepperoni*]  2
sushi_california_roll [*avocado*]    1     1
pizza_hawaiian        [*pineapples*] 1
```

(See `cat/alias.md`)
(See `cat/allocation.md`)
(See `cat/anomaly-detectors.md`)
(See `cat/component-templates.md`)
(See `cat/count.md`)
(See `cat/dataframeanalytics.md`)
(See `cat/datafeeds.md`)
(See `cat/fielddata.md`)
(See `cat/health.md`)
(See `cat/indices.md`)
(See `cat/master.md`)
(See `cat/nodeattrs.md`)
(See `cat/nodes.md`)
(See `cat/pending_tasks.md`)
(See `cat/plugins.md`)
(See `cat/recovery.md`)
(See `cat/repositories.md`)
(See `cat/segments.md`)
(See `cat/shards.md`)
(See `cat/snapshots.md`)
(See `cat/tasks.md`)
(See `cat/templates.md`)
(See `cat/thread_pool.md`)
(See `cat/trainedmodel.md`)
(See `cat/transforms.md`)
