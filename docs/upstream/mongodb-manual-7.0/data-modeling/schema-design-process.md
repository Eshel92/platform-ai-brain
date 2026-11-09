<!-- Converted from data-modeling/schema-design-process.txt (reStructuredText). Includes are inlined. -->

# Designing Your Schema

The schema design process helps you identify the data your 
application needs and organize it to optimize performance.

## Use Cases

Plan and design your schema early in the development process.
This helps prevent performance issues as your application grows.

MongoDB's flexible schema lets you evolve your data model iteratively.
You can add new fields and new content types without rewriting existing
documents or migrating data. Depending on your application, you may want
to establish a simple schema to cover basic functionality before optimizing.

## Tasks

The schema design process consists of the following steps:

**Step 1: Identify your workload**

Identify the operations that your application runs most
frequently. See data-modeling-identify-workload.

**Step 2: Map relationships**

Identify the relationships in your application's data and decide
whether to link or embed related data. See
data-modeling-map-relationships.

**Step 3: Apply design patterns**

Apply schema design patterns to optimize reads and writes. See
data-modeling-apply-patterns.
