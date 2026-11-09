<!-- Converted from tutorial/limit-number-of-items-scanned-for-text-search.txt (reStructuredText). Includes are inlined. -->

# Limit Number of Text Index Entries Scanned on Self-Managed Deployments

This tutorial describes how to create indexes to limit the number of
index entries scanned for queries that includes a `$text`
expression and equality conditions.

A collection `inventory` contains the following documents:

```javascript
{ _id: 1, dept: "tech", description: "lime green computer" }
{ _id: 2, dept: "tech", description: "wireless red mouse" }
{ _id: 3, dept: "kitchen", description: "green placemat" }
{ _id: 4, dept: "kitchen", description: "red peeler" }
{ _id: 5, dept: "food", description: "green apple" }
{ _id: 6, dept: "food", description: "red potato" }
```

Consider the common use case that performs text searches by
*individual* departments, such as:

```javascript
db.inventory.find( { dept: "kitchen", $text: { $search: "green" } } )
```

To limit the text search to scan only those documents within a specific
`dept`, create a compound index that *first* specifies an
ascending/descending index key on the field `dept` and then a
`text` index key on the field `description`:

```javascript
db.inventory.createIndex(
   {
     dept: 1,
     description: "text"
   }
)
```

Then, the text search within a particular department
will limit the scan of indexed documents. For example, the following
query scans only those documents with `dept` equal to `kitchen`:

```javascript
db.inventory.find( { dept: "kitchen", $text: { $search: "green" } } )
```

**Note:**

- A compound `text` index cannot include any other special index
  types, such as multi-key or
  geospatial index fields.

- If the compound text index includes keys **preceding** the text index
  key, to use `$text`, the query predicate must
  include **equality match conditions** on the preceding keys.

- When creating a compound `text` index, all `text` index keys must
  be listed adjacently in the index specification document.

**See also:**

/core/index-text
