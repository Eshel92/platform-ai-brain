<!-- Converted from core/indexes/index-types/index-wildcard/reference/wildcard-projection-signature.txt (reStructuredText). Includes are inlined. -->

# Wildcard Index Signature

Starting in MongoDB 5.0, the `wildcardProjection` option for
wildcard indexes is included in the
index signature. This means that you can create multiple
wildcard indexes with the same key pattern as long
as the `wildcardProjection` options do not contain the same fields.

## Projection Signature Display

Starting in MongoDB 6.3, 6.0.5, and 5.0.16, the `wildcardProjection`
field stores the index projection in its submitted form. Earlier
versions of the server may have stored the projection in a normalized
form.

The server uses the index the same way, but you may notice a difference
in the output of the `listIndexes` and
`db.collection.getIndexes()` commands.

## Example

Consider the following wildcard index on a `books` collection:

```javascript
db.books.createIndex( 
   {
      "$**": 1
   }, 
   {
      wildcardProjection: {
         "author.name": 1,
         "author.website": 1   
      },
      name: "authorWildcard"
   }
)
```

The index key pattern is `"$**"`. You can create another wildcard
index with the same key pattern if you specify a different
`wildcardProjection`. For example:

```javascript
db.books.createIndex( 
   {
      "$**": 1
   }, 
   {
      wildcardProjection: {
         "publisher.name": 1
      },
      name: "publisherWildcard"
   }
)
```

To view the created indexes, run the
`getIndexes()` method:

```javascript
db.books.getIndexes()
```

Output:

```javascript
[
   { v: 2, key: { _id: 1 }, name: '_id_' },
   {
      v: 2,
      key: { '$**': 1 },
      name: 'authorWildcard',
      wildcardProjection: { author: { website: true, name: true }, _id: false }
   },
   {
      v: 2,
      key: { '$**': 1 },
      name: 'publisherWildcard',
      wildcardProjection: { publisher: { name: true }, _id: false }
   }
]
```

## Learn More

- createIndex-method-wildcard-option

- wildcard-index-restrictions
