<!-- Converted from core/indexes/index-types/index-text/text-index-restrictions.txt (reStructuredText). Includes are inlined. -->

# Text Index Restrictions on Self-Managed Deployments

Text indexes have these restrictions:

## One Text Index per Collection

A collection can have at most one text index.

Atlas Search (available in [MongoDB Atlas](https://www.mongodb.com/atlas/database)) supports
multiple full-text search indexes on a single collection. To learn more,
see the Atlas Search documentation.

## Text Search and Hints

If a query includes a `$text` expression, you cannot use
`hint()` to specify which index to use for the query.

## Text Search and Multi-Word Strings

If the `$search` string of a `$text` operation includes a multi-word string
and individual terms, `$text` only matches the documents that include the
multi-word string.

For an example of text search with multi-word strings, see
text-operator-exact-string.  

## Text Index and Sort

Text indexes cannot improve performance for sort operations. This
restriction applies to both single-field and compound text indexes.

## Compound Text Index

A compound index can include a text index
key in combination with ascending and descending index keys. However,
compound text indexes have these restrictions:

- A compound text index cannot include any other special index types,
  such as multikey or geospatial index fields.

- If the compound text index includes keys **preceding** the text index
  key, to use `$text`, the query predicate must
  include **equality match conditions** on the preceding keys.

- When you create a compound text index, all text index keys must be
  listed adjacently in the index specification document.

For examples of compound text indexes, see these pages:

- compound-text-index-example
- limit-entries-scanned

## Collation Option

Text indexes only support binary comparison, and do not support the
collation option. Binary comparison compares the
numeric Unicode value of each character in each string, and does not
account for letter case or accent marks.

To create a text index on a collection that has a non-simple
collation, you must explicitly specify ``{ collation: { locale: "simple"
} }`` when you create the index.

For example, consider a collection named `collationTest` with a
collation of `{ locale: "en" }`:

```javascript
db.createCollection(
   "collationTest",
   {
      collation: { locale: "en" }
   }
)
```

To create a text index on the `collationTest` collection, you must
specify `{ collation: { locale: "simple" } }`. The following command
creates a text index on the `quotes` field:

```javascript
db.collationTest.createIndex(
   {
      quotes: "text"
   },
   {
      collation: { locale: "simple" }
   }
)
```
