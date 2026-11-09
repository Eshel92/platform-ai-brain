<!-- Converted from reference/operator/aggregation/changeStreamSplitLargeEvent.txt (reStructuredText). Includes are inlined. -->

# $changeStreamSplitLargeEvent (aggregation)

## Definition

**`$changeStreamSplitLargeEvent`**

**New in version:** 6.0.9

If a change stream has large events that exceed
16 MB, a `BSONObjectTooLarge` exception is returned. Starting in
MongoDB 6.0.9, you can use a `$changeStreamSplitLargeEvent` stage to
split the events into smaller fragments.

You should only use `$changeStreamSplitLargeEvent` when strictly
necessary. For example, if your application requires full document pre-
or post-images, and generates large events that exceed 16 MB, use
`$changeStreamSplitLargeEvent`.

Before you decide to use `$changeStreamSplitLargeEvent`, you should
first try to reduce the change event size. For example:

- Don't request document pre- or post-images unless your application
  requires them. This generates `fullDocument` and
  `fullDocumentBeforeChange` fields in more cases, which are typically
  the largest objects in a change event.

- Use a `$project` stage to include only the fields necessary
  for your application. This reduces the change event size and avoids
  the additional time to split large events into fragments. This allows
  more change events to be returned in each batch.

You can only have one `$changeStreamSplitLargeEvent` stage in
your pipeline, and it must be the last stage. You can only use
`$changeStreamSplitLargeEvent` in a `$changeStream` pipeline.

`$changeStreamSplitLargeEvent` syntax:

```javascript
{
  $changeStreamSplitLargeEvent: {}
}
```

## Behavior

`$changeStreamSplitLargeEvent` splits events that exceed 16 MB
into fragments and returns the fragments sequentially using the change
stream cursor.

The fragments are split so that the maximum number of fields are
returned in the first fragment. This ensures the event context is
returned as quickly as possible.

When the change event is split, only the size of top-level fields are
used. `$changeStreamSplitLargeEvent` does not recursively process or
split subdocuments. For example, if you use a `$project` stage to
create a change event with a single field that is 20 MB in size, the
event is not split and the stage returns an error.

Each fragment has a resume token. A stream that is resumed using a
fragment's token will either:

- Begin a new stream from the subsequent fragment.
- Start at the next event if resuming from the final fragment in the
  sequence.

Each fragment for an event includes a `splitEvent` document:

```javascript
splitEvent: {
   fragment: <int>,
   of: <int>
}
```

The following table describes the fields.

| Field | Description |
|---|---|
| `fragment` | Fragment index, starting at 1. |
| `of` | Total number of fragments for the event. |

## Example

**shell:**

The example scenario in this section shows the use of
`$changeStreamSplitLargeEvent` with a new collection named
`myCollection`.

Create `myCollection` and insert one document with just under 16 MB of
data:

```javascript
db.myCollection.insertOne(
   { _id: 0, largeField: "a".repeat( 16 * 1024 * 1024 - 1024 ) }
)
```

`largeField` contains the repeated letter `a`.

Enable changeStreamPreAndPostImages for `myCollection`, which
allows a change stream to retrieve a document as it was before an update
(pre-image) and after an update (post-image):

```javascript
db.runCommand( {
   collMod: "myCollection",
   changeStreamPreAndPostImages: { enabled: true }
} )
```

Create a change stream cursor to monitor changes to `myCollection`
using `db.collection.watch()`:

```javascript
myChangeStreamCursor = db.myCollection.watch(
   [ { $changeStreamSplitLargeEvent: {} } ],
   { fullDocument: "required", fullDocumentBeforeChange: "required" }
)
```

For the change stream event:

- `fullDocument: "required"` includes the document post-image.
- `fullDocumentBeforeChange: "required"` includes the document
  pre-image.

For details, see `$changeStream`.

Update the document in `myCollection`, which also produces a change
stream event with the document pre- and post-images:

```javascript
db.myCollection.updateOne(
   { _id: 0 },
   { $set: { largeField: "b".repeat( 16 * 1024 * 1024 - 1024 ) } }
)
```

`largeField` now contains the repeated letter `b`.

Retrieve the fragments from `myChangeStreamCursor` using the
`next()` method and store the fragments in objects named
`firstFragment`, `secondFragment`, and `thirdFragment`:

```javascript
const firstFragment = myChangeStreamCursor.next()
const secondFragment = myChangeStreamCursor.next()
const thirdFragment = myChangeStreamCursor.next()
```

Show `firstFragment.splitEvent`:

```javascript
firstFragment.splitEvent
```

Output with the fragment details:

```javascript
splitEvent: { fragment: 1, of: 3 }
```

Similarly, `secondFragment.splitEvent` and
`thirdFragment.splitEvent` return:

```javascript
splitEvent: { fragment: 2, of: 3 }
splitEvent: { fragment: 3, of: 3 }
```

To examine the object keys for `firstFragment`:

```javascript
Object.keys( firstFragment )
```

Output:

```javascript
[
   '_id',
   'splitEvent',
   'wallTime',
   'clusterTime',
   'operationType',
   'documentKey',
   'ns',
   'fullDocument'
]
```

To examine the size in bytes for `firstFragment.fullDocument`:

```javascript
bsonsize( firstFragment.fullDocument )
```

Output:

```javascript
16776223
```

`secondFragment` contains the `fullDocumentBeforeChange` pre-image,
which is approximately 16 MB in size. The following example shows the
object keys for `secondFragment`:

```javascript
Object.keys( secondFragment )
```

Output:

```javascript
[ '_id', 'splitEvent', 'fullDocumentBeforeChange' ]
```

`thirdFragment` contains the `updateDescription` field, which is
approximately 16 MB in size. The following example shows the object keys
for `thirdFragment`:

```javascript
Object.keys( thirdFragment )
```

Output:

```javascript
[ '_id', 'splitEvent', 'updateDescription' ]
```

**csharp:**

The C# examples on this page use the `sample_mflix` database
from the Atlas sample datasets. To learn how to create a
free MongoDB Atlas cluster and load the sample datasets, see
`Get Started` in the MongoDB .NET/C#
Driver documentation.

The following `Movie` class models the documents in the `sample_mflix.movies`
collection:

```csharp
public class Movie
{
    public string Id { get; set; }

    public int Runtime { get; set; }

    public string Title { get; set; }

    public string Rated { get; set; }

    public List<string> Genres { get; set; }

    public string Plot { get; set; }

    public ImdbData Imdb { get; set; }

    public int Year { get; set; }

    public int Index { get; set; }

    public string[] Comments { get; set; }

    [BsonElement("lastupdated")]
    public DateTime LastUpdated { get; set; }
}
```

To use the MongoDB {+csharp-driver-short+} to add a `$changeStreamSplitLargeEvent` stage to an aggregation
pipeline, call the [ChangeStreamSplitLargeEvent()](https://mongodb.github.io/mongo-csharp-driver/3.3.0/api/MongoDB.Driver/MongoDB.Driver.PipelineStageDefinitionBuilder.ChangeStreamSplitLargeEvent.html) method on a `PipelineDefinition` object.

The following example creates a pipeline stage that splits events exceeding 16 MB into fragments and returns them sequentially in
a change stream cursor:

```csharp
var pipeline = new EmptyPipelineDefinition<ChangeStreamDocument<Movie>>()
    .ChangeStreamSplitLargeEvent();
```

For more information about change streams and events, see Change
Events.
