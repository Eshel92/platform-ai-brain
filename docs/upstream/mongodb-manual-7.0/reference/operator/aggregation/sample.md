<!-- Converted from reference/operator/aggregation/sample.txt (reStructuredText). Includes are inlined. -->

# $sample (aggregation stage)

## Definition

**`$sample`**

Randomly selects the specified number of documents from the
input documents.

`$sample` stage syntax: 

```javascript
{ $sample: { size: <positive integer N> } }
```

`N` is the number of documents to randomly select.
Set `N` to an integer greater than or equal to `1`.

## Behavior

If all of the following conditions are true, `$sample` uses a
pseudo-random cursor to select the `N` documents:

- `$sample` is the first stage of the pipeline.
- `N` is less than 5% of the total documents in the collection.

  **Note:**

  You can't configure the threshold that `$sample` uses to
  determine when to scan the entire collection. The threshold is 5%.
  If the size is greater than 5% of the total number of documents in
  the collection, `$sample` performs a 
  top-k sort by a generated random value.
  The top-k sort could spill to disk if the sample documents are
  larger than 100 MB.

- The collection contains more than 100 documents.

If any of the previous conditions are false, `$sample`:

- Reads all documents that are output from a preceding aggregation
  stage or a collection scan.
- Performs a random sort to select `N` documents. Random sorts are 
  subject to the sort memory restrictions.

  **Note:**

  Views are the result of aggregation 
  pipelines. When you use `$sample` on a view, MongoDB appends the stage
  to the end of the view's aggregation pipeline syntax. Therefore, the 
  `$sample` stage on a view is never the first stage and always 
  results in a collection scan.

If you use `$sample` in a sharded cluster, each shard performs
the sample operation independently. `mongos` samples
the merged result of each shard's sample operation and returns the
requested number of documents.

## Examples

**shell:**

The following example uses the `movies` collection from the sample_mflix
sample dataset.  For details on how to load this dataset into
your deployment, see Load the sample dataset.

The following aggregation operation randomly selects `3`
documents from the `movies` collection:

```javascript
db.movies.aggregate(
   [
      { $sample: { size: 3 } },
      { $project: { _id: 0, title: 1, year: 1, genres: 1 } }
   ]
)
```

The operation returns three random documents.

**See also:**

`$rand (aggregation)`

**csharp:**

(Text shared from another MongoDB docs repo, not available offline: dbx/csharp/aggregation/rst-files/method-intro.rst)

```csharp
var pipeline = new EmptyPipelineDefinition<Movie>()
    .Sample(5);
```

**nodejs:**

To use the MongoDB Node.js driver to add a `$sample` stage to an aggregation
pipeline, use the `$sample` operator in a pipeline object.

The following example creates a pipeline stage that returns five random documents from the input collection. The
example then runs the aggregation pipeline:

```javascript
const pipeline = [{ $sample: { size: 5 } }];

const cursor = collection.aggregate(pipeline);
return cursor;
```
