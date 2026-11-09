<!-- Converted from performance-advisor/schema-advisor.txt (reStructuredText). Includes are inlined. -->

# Improve Your Schema

Your schema is the architecture of your cluster, including your
collections, indexes and
documents.

## Schema Design Patterns

You can model your schema based on frequently used design patterns. The 
*Building with Patterns* blog series discusses the following frequently used design patterns.

To read about situations in which arrays work well, see the 
following design patterns:

- Use
  [The Attribute Pattern](https://www.mongodb.com/blog/post/building-with-patterns-the-attribute-pattern) for handling data 
  with unique combinations of attributes, such as movie data where each 
  movie is released in a subset of countries.

- Use
  [The Bucket Pattern](https://www.mongodb.com/blog/post/building-with-patterns-the-bucket-pattern) for handling tightly 
  grouped or sequential data, such as time span data.

- Use 
  [The Polymorphic Pattern](https://www.mongodb.com/blog/post/building-with-patterns-the-polymorphic-pattern) for handling 
  differently shaped documents in the same collection, such as athlete 
  records across several sports.

To read about strategies for keeping documents in your working set at 
a manageable size, see the following patterns:

- Use 
  [The Extended Reference Pattern](https://www.mongodb.com/blog/post/building-with-patterns-the-extended-reference-pattern) to 
  duplicate a frequently-read portion of data from large documents to 
  smaller ones.

- Use 
  [The Subset Pattern](https://www.mongodb.com/blog/post/building-with-patterns-the-subset-pattern)  
  to reduce the size of documents with large array fields.

- Use 
  [The Outlier Pattern](https://www.mongodb.com/blog/post/building-with-patterns-the-outlier-pattern) to handle a few 
  large documents in an otherwise standard collection.

To learn how to incorporate the flexible data model into your schema,
see the following presentations from **MongoDB.live 2020**:

- Learn about entity relationships in MongoDB and examples of their
  implementations with
  [Data Modeling with MongoDB](https://www.mongodb.com/presentations/data-modeling-with-mongodb).
- Learn advanced data modeling design patterns you can incorporate
  into your schema with
  [Advanced Schema Design Patterns](https://www.mongodb.com/presentations/advanced-schema-design-patterns).

## Schema Suggestions

Ops Manager offers two ways to detect common
schema design issues and suggests modifications that follow MongoDB’s
best practices:

- The Performance Advisor provides
  holistic schema recommendations for your cluster by sampling documents
  in your most active collections and collections with slow-running
  queries.

- The Data Explorer offers schema
  suggestions for a specific collection by sampling documents in that
  collection.

To learn more about how to apply the suggestions offered in either the
Performance Advisor or Data Explorer, refer to the following pages:

| Schema Improvement | Reason for Suggestion |
|---|---|
| embedded-documents-arrays-anti-pattern | You are running too many `$lookup` operations on your data. Take advantage of MongoDB's rich schema model to embed related data in a single collection. |
| unbounded-arrays-anti-pattern | Your documents contain array fields with many elements, which can degrade query performance. |
| indexes-anti-pattern | You have unnecessary indexes in your collection, which can consume disk space and degrade write performance. |
| reduce-document-size-anti-pattern | You have excessively large documents, which can degrade the performance of your most frequent queries. |
| too-many-namespaces-anti-pattern | You have an exceedingly high number of collections in a database, which can result in unnecessary disk space usage. |

## Limitations of Schema Suggestions

- Schema suggestions for a collection are partly driven by a random
  sampling of documents from that collection. Because this sampling is
  performed each time your schema is analyzed, you may see different
  suggestions at different times for the same collection.

- The Performance Advisor uses slow query
  logs as an input to recognize certain schema issues, namely too many
  `$lookup` operations and not utilizing an index for
  case-sensitive regex queries. If a collection does not have any
  operations that last longer than 100 milliseconds, the Performance
  Advisor may not suggest all potential improvements for that
  collection, or may not show all reasons why an improvement is being
  suggested.

- The Performance Advisor analyzes
  the 20 most active collections based on the output of the
  `top` command. To see suggestions for a specific
  collection, view that collection in the
  Data Explorer.
