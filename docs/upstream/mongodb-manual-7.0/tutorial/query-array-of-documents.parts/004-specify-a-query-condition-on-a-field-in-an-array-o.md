<!-- Part 4 of 4 of tutorial/query-array-of-documents.md (split because the page is big). -->

## Specify a Query Condition on a Field in an Array of Documents

### Specify a Query Condition on a Field Embedded in an Array of Documents

If you do not know the index position of the document nested in the
array, concatenate the name of the array field, with a dot (`.`) and
the name of the field in the nested document.

The following example selects all documents where the `instock` array
has at least one embedded document that contains the field `qty`
whose value is less than or equal to `20`:

Copy the following filter into the Compass query bar and click
Find:

```javascript
{ 'instock.qty': { $lte: 20 } }
```

(Figure: /images/compass-find-arr-embedded-field.png)

### Use the Array Index to Query for a Field in the Embedded Document

Using dot notation, you can specify query conditions for a
field in a document at a particular index or position of the array.
The array uses zero-based indexing.

**Note:**

When querying using dot notation, the field and index must be
inside quotation marks.

The following example selects all documents where the `instock` array
has as its first element a document that contains the field `qty`
whose value is less than or equal to `20`:

Copy the following filter into the Compass query bar and click
Find:

```javascript
{ 'instock.0.qty': { $lte: 20 } }
```

(Figure: /images/compass-find-embedded-field-arr-index.png)


## Specify Multiple Conditions for Array of Documents

When you specify conditions on more than one field nested in an array
of documents, you can specify the query such that either a single
document meets these conditions or any combination of documents in the
array meets the conditions.

### A Single Nested Document Meets Multiple Query Conditions on Nested Fields

Use the `$elemMatch` operator to specify multiple criteria on
an array of embedded documents such that at least one embedded
document satisfies all the specified criteria.

The following example queries for documents where the `instock` array
has at least one embedded document that contains both the field
`qty` equal to `5` and the field `warehouse` equal
to `A`:

Copy the following filter into the Compass query bar and click
Find:

```javascript
{ "instock": { $elemMatch: { qty: 5, warehouse: "A" } } }
```

(Figure: /images/compass-multiple-query-conditions-nested-fields.png)

The following example queries for documents where the `instock` array
has at least one embedded document that contains the field `qty` that
is greater than `10` and less than or equal to `20`:

Copy the following filter into the Compass query bar and click
Find:

```javascript
{ "instock": { $elemMatch: { qty: { $gt: 10, $lte: 20 } } } }
```

(Figure: /images/compass-multiple-query-conditions-nested-fields-2.png)

### Combination of Elements Satisfies the Criteria

If the compound query conditions on an array field do not use the
`$elemMatch` operator, the query selects those documents whose
array contains any combination of elements that satisfies the
conditions.

For example, the following query matches documents where any document
nested in the `instock` array has the `qty` field greater than
`10` and any document (but not necessarily the same embedded
document) in the array has the `qty` field less than or equal to
`20`:

Copy the following filter into the Compass query bar and click
Find:

```javascript
{ "instock.qty": { $gt: 10,  $lte: 20 } }
```

(Figure: /images/compass-arr-match-combo-of-elements.png)

The following example queries for documents where the `instock` array
has at least one embedded document that contains the field `qty`
equal to `5` and at least one embedded document (but not necessarily
the same embedded document) that contains the field `warehouse` equal
to `A`:

Copy the following filter into the Compass query bar and click
Find:

```javascript
{ "instock.qty": 5, "instock.warehouse": "A" }
```

(Figure: /images/compass-arr-match-combo-of-elements-2.png)


## Query an Array of Documents with MongoDB Atlas

This example uses the sample training dataset. To load the sample dataset into your
MongoDB Atlas deployment, see Load Sample Data.

To query an array of documents in MongoDB Atlas, follow these steps:

**Step 1: In the MongoDB Atlas UI, go to the Clusters page for your project.**

a. If it's not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it's not already displayed, select your project
   from the Projects menu in the navigation bar.

#. In the sidebar, click Clusters under 
   the Database heading.

   The [Clusters](https://cloud.mongodb.com/go?l=https%3A%2F%2Fcloud.mongodb.com%2Fv2%2F%3Cproject%3E%23%2Fclusters) page displays.

**Step 2: Navigate to the collection**

a. For the cluster that contains the sample data,
   click Browse Collections.
#. In the left navigation pane, select the
   sample_training database.
#. Select the grades collection.

**Step 3: Specify the Filter field**

Specify the query filter document
in the Filter field. A query filter document uses 
query operators to specify
search conditions.

Copy the following query filter document into the 
Filter search bar:

```javascript
{"scores.type": "exam"}
```

**Step 4: Click Apply**

This query filter returns all documents in the
`sample_training.grades` collection that contain a subdocument
in the `scores` array where `type` is set to `exam`. The
full document, including the entire `scores` array, is
returned. For more information on modifying the returned array,
see project-array-elements-in-returned-array.


## Additional Query Tutorials

For additional query examples, see:

- /tutorial/query-arrays

- /tutorial/query-documents

- /tutorial/query-embedded-documents
