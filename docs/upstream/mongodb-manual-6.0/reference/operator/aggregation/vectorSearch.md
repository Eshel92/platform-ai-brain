<!-- Converted from reference/operator/aggregation/vectorSearch.txt (reStructuredText). Includes are inlined. -->

# $vectorSearch (aggregation)

## Definition

**Important:**

The `$vectorSearch` aggregation pipeline stage is only available
for collections hosted on MongoDB Atlas cluster tiers 
running MongoDB version 6.0.11 or later. To learn more, see 
Atlas Vector Search. 

**`$vectorSearch`**

`$vectorSearch` performs a semantic search on data in your Atlas
cluster. 

If you store vector embeddings on your Atlas cluster, you can
seamlessly index the vector data along with your other collection
data. You can use the `$vectorSearch` stage to pre-filter
your data and perform semantic search against the indexed fields. 

Your vector data must be less than or equal to 4096 dimensions in
width.

## Behavior

Starting in MongoDB 8.0, you can use a `$vectorSearch` stage in a
`$unionWith` stage. 

## Limitations

You cannot use a `$vectorSearch` stage in a `$facet`
stage or a `$lookup` stage. 

## Learn More

- To learn more about creating Atlas Vector Search indexes, see
  Index Vector Embeddings. 

- To learn more about `$vectorSearch` pipeline stage syntax
  and usage, see Vector Search Queries.
