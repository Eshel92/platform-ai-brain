<!-- Converted from data-modeling/design-patterns/polymorphic-data/inheritance-schema-pattern.txt (reStructuredText). Includes are inlined. -->

# Use the Inheritance Pattern

Use the inheritance pattern when your documents are mostly similar and
you want to keep them in the same collection so they can be read
together. The inheritance pattern uses a parent entity with common
fields to group child entities that have variable forms. The child
entities can have unique fields, but are closely related to one another
due to their common fields.

## About this Task

In this example, a book store uses the inheritance pattern to store
different types of media. A `book` parent entity stores common fields
like `title` and `author`, and multiple child entities inherit from
the `book` entity. For example audio books, printed books, and ebooks
have common fields, and also have unique fields specific to the media
type.

The inheritance pattern stores these slightly different entities in the
same collection, which improves performance for queries that need to
access all books, regardless of type.

## Steps

**Step 1: Insert the sample data.**

```javascript
db.books.insertMany( [
   {
      product_type: "ebook",
      title: "Practical MongoDB Aggregations",
      author: "Paul Done",
      rating: 4.8,
      genres: [ "programming" ],
      pages: 338,
      download_url: "<url>"
   },
   {
      product_type: "audiobook",
      title: "Practical MongoDB Aggregations",
      author: "Paul Done",
      rating: 4.6,
      genres: [ "programming" ],
      narrators: [ "Paul Done" ],
      duration: {
         hours: 21,
         minutes: 8
      },
      time_by_chapter: [
         {
            chapter: 1,
            start: "00:00:00",
            end: "01:00:00"
         },
         {
            chapter: 2,
            start: "01:00:00",
            end: "01:55:00"
         }
      ]
   },
   {
      product_type: "physical_book",
      title: "Practical MongoDB Aggregations",
      author: "Paul Done",
      rating: 4.9,
      genres: [ "programming" ],
      pages: 338,
      stock: 12,
      delivery_time: 2
   }
] )
```

The preceding documents share some common fields, and have unique
fields depending on the `product_type`. For example:

- `ebook` documents have a `download_url` field.
- `audiobook` documents have a `time_by_chapter` field.
- `physical_book` documents have a `delivery_time` field.

**Step 2: Query all documents.**

Even though the documents in the `books` collection have
different shapes, you can return all documents with a single
query:

```javascript
db.books.find()
```

Output:

```javascript
[
   {
      _id: ObjectId('66eb4160ef006be6eda8e2ee'),
      product_type: 'ebook',
      title: 'Practical MongoDB Aggregations',
      author: 'Paul Done',
      rating: 4.8,
      genres: [ 'programming' ],
      pages: 338,
      download_url: '<url>'
   },
   {
      _id: ObjectId('66eb4160ef006be6eda8e2ef'),
      product_type: 'audiobook',
      title: 'Practical MongoDB Aggregations',
      author: 'Paul Done',
      rating: 4.6,
      genres: [ 'programming' ],
      narrators: [ 'Paul Done' ],
      duration: { hours: 21, minutes: 8 },
      time_by_chapter: [
         { chapter: 1, start: '00:00:00', end: '01:00:00' },
         { chapter: 2, start: '01:00:00', end: '01:55:00' }
      ]
   },
   {
      _id: ObjectId('66eb4160ef006be6eda8e2f0'),
      product_type: 'physical_book',
      title: 'Practical MongoDB Aggregations',
      author: 'Paul Done',
      rating: 4.9,
      genres: [ 'programming' ],
      pages: 338,
      stock: 132,
      delivery_time: 2
   }
]
```

**Step 3: Query unique fields.**

The inheritance pattern does not require additional logic to
query on fields that are specific to a particular media type. For
example, the following query returns books that have a duration
longer than 20 hours, which only applies to the product type
`audio_book`:

```javascript
db.books.find(
   {
      "duration.hours": { $gt: 20 }
   }
)
```

Output:

```javascript
[
   {
      _id: ObjectId('66eb4160ef006be6eda8e2ef'),
      product_type: 'audiobook',
      title: 'Practical MongoDB Aggregations',
      author: 'Paul Done',
      rating: 4.6,
      genres: [ 'programming' ],
      narrators: [ 'Paul Done' ],
      duration: { hours: 21, minutes: 8 },
      time_by_chapter: [
         { chapter: 1, start: '00:00:00', end: '01:00:00' },
         { chapter: 2, start: '01:00:00', end: '01:55:00' }
      ]
   }
]
```

## Learn More

- polymorphic-schema-pattern

- schema-validation-overview

- create-indexes-to-support-queries
