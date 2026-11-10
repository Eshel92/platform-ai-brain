<!-- Converted from indices/apis/unfreeze.asciidoc (AsciiDoc). Includes are inlined. -->

### Unfreeze index API

**Deprecated in 7.14**

**Warning:**
In 8.0, we removed the ability to freeze an index. In previous versions,
freezing an index reduced its memory overhead. However, frozen indices are no
longer useful due to
https://www.elastic.co/blog/significantly-decrease-your-elasticsearch-heap-memory-usage[recent
improvements in heap memory usage].
You can use this API to unfreeze indices that were frozen in 7.x. Frozen indices
are not related to the frozen data tier.

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Unfreezes an index.

#### Request

`POST /<index>/_unfreeze`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
index privilege for the target index or index alias.

#### Description

When a frozen index is unfrozen, the index goes through the normal recovery
process and becomes writeable again.

#### Path parameters

`<index>`::
  (Required, string) Identifier for the index.

#### Examples

The following example unfreezes an index:

```console
POST /my-index-000001/_unfreeze
```
