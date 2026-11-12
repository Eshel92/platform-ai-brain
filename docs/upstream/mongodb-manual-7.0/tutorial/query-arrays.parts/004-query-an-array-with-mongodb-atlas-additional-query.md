<!-- Part 4 of 4 of tutorial/query-arrays.md (split because the page is big). -->

## Query an Array with MongoDB Atlas

The example in this section uses the sample movies dataset. To learn how to load the sample dataset 
into your MongoDB Atlas deployment, see Load Sample Data.

To query an array in MongoDB Atlas, follow these steps:

**Step 1: In the MongoDB Atlas UI, go to the Clusters page for your project.**

a. If it's not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it's not already displayed, select your project
   from the Projects menu in the navigation bar.

#. In the sidebar, click Clusters under 
   the Database heading.

   The [Clusters](https://cloud.mongodb.com/go?l=https%3A%2F%2Fcloud.mongodb.com%2Fv2%2F%3Cproject%3E%23%2Fclusters) page displays.

**Step 2: Navigate to the collection.**

a. For the cluster that contains the sample data,
   click Browse Collections.
#. In the left navigation pane, select the
   `sample_mflix` database.
#. Select the `movies` collection.

**Step 3: Specify a query filter document.**

To query a document that contains an array, 
specify a query filter document.
A query filter document uses query operators to specify search conditions.
Use the following example documents to query array fields in the 
`sample_mflix.movies` collection.

To apply a query filter, copy an example document into the 
Filter search bar and click Apply.

**match:**

To specify an equality condition on an array, use the query
document `{ <field>: <value> }` where `<value>` is the
exact array to match, including the order of the elements.
The following example finds documents where `genres`
contains the `["Action", "Comedy"]` array in the specified
order:

```
{ genres: ["Action", "Comedy"] }
```

To find an array that contains both `Action` and
`Comedy` regardless of order or other elements in the
array, use the `$all` operator:

```
{ genres: { $all: ["Action", "Comedy"] } }
```

**element:**

To query if the array field contains at least one element with the 
specified value, use the filter `{ <field>: <value> }` where 
`<value>` is the element value.

The following example queries for all documents where the
`genres` field contains the string `Short` as one 
of its elements:

```
{ genres: "Short" }
```

To specify conditions on the elements in the array field,
use query operators in the
query filter document:

```
{ <array field>: { <operator1>: <value1>, ... } }
```

The following example uses the `$nin` operator to
query for all documents where the `genres` field does 
not contain `Drama`:

```
{ genres: { $nin: ["Drama"] } }
```

**multiple:**

When you specify compound conditions on array elements, you
can query for either a single array element that meets all
conditions or any combination of array elements that together
meet the conditions.

### Query an Array with Compound Filter Conditions on the Array Elements

The following example queries for documents where the
`cast` array contains elements that in some combination
satisfy the query conditions. The following filter uses the
`$regex` and `$eq` operators to return
documents where a single array element ends in `Olsen` and
another element equals `Mary-Kate Olsen` or a single
element that satisfies both conditions:

```
{ cast: { $regex: "Olsen$", $eq: "Mary-Kate Olsen" } }
```

This query filter returns movies that include ``Mary-Kate
Olsen`` in their cast, and movies that include both
`Mary-Kate Olsen` and `Ashley Olsen` in their cast.

### Query for an Array Element that Meets Multiple Criteria

Use the `$elemMatch` operator to specify multiple
criteria on array elements such that at least one array
element satisfies all the specified criteria.

The following example uses the `$elemMatch` and
`$ne` operators to query for documents where
`languages` contains at least one element that is both not
`null` and does not equal `English`:

```
{ languages: { $elemMatch: { $ne: null, $ne: "English" } } }
```

### Query for an Element by the Array Index Position

Use dot notation to specify query conditions for an
element at a particular index or position of the array. The
array uses zero-based indexing.

**Note:**

When you query using dot notation, the field and nested
field must be inside quotation marks.

The following example uses the `$ne` operator to
query for all documents where the first element in
the `countries` array is not equal to `USA`:

```
{ "countries.0": { $ne: "USA" } }
```

### Query an Array by Array Length

Use the `$size` operator to query for arrays by
number of elements. The following example selects documents
where `genres` has 3 elements:

```
{ genres: { $size: 3 } }
```

      


## Additional Query Tutorials

For additional query examples, see:

- /tutorial/query-documents

- /tutorial/query-embedded-documents

- /tutorial/query-array-of-documents
