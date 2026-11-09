<!-- Converted from data-modeling/design-antipatterns.txt (reStructuredText). Includes are inlined. -->

# Schema Design Anti-Patterns

Schema design anti-patterns are inefficient ways to structure your database 
schema. They can create unnecessary complexity and cause performance issues. 
Recognizing and avoiding schema design anti-patterns can help create 
applications with better performance. 

## Get Started

To learn more about schema design anti-patterns, see the following pages:

| Schema Design Anti-Pattern | Definition |
|---|---|
| Avoid Unbounded Arrays | A document stores an unbounded array that can grow to be too large. The large array can exceed the document size limit and cause a decrease in index performance. |
| Reduce Number of Collections | You create a large number of collections in your database. Having too many collections can decrease storage engine performance. |
| Remove Unnecessary Indexes | Your collection contains unnecessary indexes. Unnecessary indexes consume additional disk space and can degrade write performance. |
| Reduce Bloated Documents | Your collection has excessively large documents. The large documents can degrade the performance of your most common queries. |
| Reduce $lookup Operations | You are running too many $lookup operations on your data. This increases query complexity and reduces query performance. |

## Details

The MongoDB Atlas Performance Advisor (available for 
M10 clusters or higher) and `MongoDB Compass Performance Insights` identify schema design anti-patterns in your 
database. It is important to understand the Atlas anti-pattern warnings in order to 
properly correct the issues and prevent the use of anti-patterns. 

## Learn More

For recommended schema design patterns, see the following: schema-design-patterns and 
data-modeling-apply-patterns.
