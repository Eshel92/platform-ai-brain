<!-- Converted from data-explorer/documents.txt (reStructuredText). Includes are inlined. -->

# Manage Documents in Data Explorer

You can use the Data Explorer to manage documents inside
your cluster collections.

To interact with data in the Ops Manager UI:

1. Click Deployment in the left navigation.

#. Select the desired MongoDB deployment.

#. Select the Data tab.

## Required Roles

To insert, edit,
or delete documents, you must have been
granted access through one of the following roles:

- `Project Owner` or `Organization Owner`

- `Project Data Access Admin`

- `Project Data Access Read/Write`

## View Documents

From the Collections tab, you can view documents in a
collection. To view documents for a collection:

**Step 1: Select the database for the collection.**

The main panel and Namespaces on the left side list the
collections in the database.

(Figure: /images/data-explorer-dbs.png)

**Step 2: Select the collection on the left-hand side or in the main panel.**

The main panel displays the Find view and the
Indexes view.

**Step 3: Select the Find view.**

The panel displays the documents in the collection. Each page
displays up to 20 documents.

**Step 4: Specify a query to find specific documents.**

You can use the query bar to search for specific documents in your 
collection. You can specify one or more of the following in the 
query bar: 

- A filter condition
- A project document to include and exclude specific fields in the 
  results
- A sort order for the documents in the results
- A collation document for language specific rules.

**filter:**

To specify a filter condition, type in a query filter document in the 
Filter field. For example, to specify equality 
condition, use a filter document of the form:

```javascript
{ <field1>: <value1>, ... }
```

To use query operators to specify a 
filter condition, use a filter document of the form:

```javascript
{ <field1>: { <queryoperator>: <value1> }, ... }
```

**Note:**

Data Explorer does not support date queries 
that use the `IsoDate()` function. Instead, use the 
MongoDB Extended JSON (v2) `$date` data type 
for date queries.

For example, the following query returns all documents where 
the date added to a `created_at` field is equal to or more 
recent than midnight on January 1, 2019, UTC (Coordinated Universal Time) time:

```javascript
{ created_at: { $gte: { $date: "2019-01-01T00:00-00:00" } } }
```

For more information on specifying query filters, including 
compound conditions, see Query Documents.

**project:**

To specify the document fields to include or exclude in the 
results, click Options in the query bar and 
specify the document fields in the Project field. 

To include fields, specify the field name and set to `1` in 
the project document. For example, to include the `year` and 
`name` fields in the documents:

```javascript
{ year: 1, name: 1 }
```

Ops Manager returns the fields specified in the Project 
field and the `_id` field, which is returned unless it is 
explicitly excluded.

To exclude fields, specify the field name and set to `0` in 
the project document. For example, to exclude the `year` and 
`name` fields in the documents:

```javascript
{ year: 0, name: 0 }
```

Ops Manager returns all fields except the fields specified in 
Project.

To learn more about project documents, see 
`$project`.

**sort:**

To sort the order of the documents in the results, click 
Options in the query bar and enter the `sort` 
document in the Sort field. 

- To specify ascending order for a field, set the field to 
  `1` in the sort document.
- To specify descending order for a field, set the field to 
  `-1` in the sort documents.

For example, the following `sort` document sorts results 
first by `year` in descending order, and within each year, 
sorts by `name` in ascending order:

```javascript
{ year: -1, name: 1 }
```

To learn more about sort documents, see 
`$sort`.

**collation:**

To specify language-specific rules for string comparison, such 
as rules for lettercase and accent marks, click 
Options in the query bar and enter the collation 
document in the Collation field. Use the 
`locale` field in the collation document to specify the [ICU Locale code](http://userguide.icu-project.org/locale) for 
the desired language. For example, to use the `pinyin` 
variant of the Chinese collation, use the following collation 
document:

```javascript
{ "locale" : "zh@collation=pinyin" }
```

To learn more about collation documents, see 
Collation.

**Note:**

As you type, the Apply button is disabled and the 
field name in the User Interface turns red until a valid query is 
entered.

**Step 5: Click Apply to run your query.**

### Number of Documents Displayed per Page

Ops Manager limits the *total byte size* of documents shown per page in the
Data Explorer. As a result, you may see varying numbers
of documents per page, especially if your documents vary
significantly in size.

## Insert Documents

To add one or more documents to a collection through the
Data Explorer, you can specify the document(s) to insert
from scratch or you can clone an existing document and modify its
fields and values as needed.

### Insert One Document

**Step 1: Go to the Find tab in Data Explorer.**

Select the collection and go to the Find tab.

**Step 2: Click Insert Document.**

The document editor appears with the `_id` field with an
objectid value that reflects the time of its generation and
not the insertion time of the document. As such, the objectid
does not represent a strict insertion order.

**Step 3: Modify the document.**

- To add a new field after an existing field, hover over the field
  and click on the plus sign that appears over the field's line
  number.

- To delete a field, hover over the field and click on the x sign
  that appears to the left of the field's line number. You cannot
  delete the `_id` field.

- To edit a field name, value, or type, click on the field name,
  value, or type.

**Step 4: Click Insert.**

### Insert Multiple Documents

**Step 1: Go to the Find tab in Data Explorer.**

Select the collection and go to the Find tab.

**Step 2: Click Insert Document.**

Data Explorer opens the Insert to Collection dialog.

**Step 3: Select the JSON View.**

**Step 4: Type or paste an array of documents to insert.**

**Example:**

The following array of documents inserts three documents into
the collection:

```json
[
  {
    "name": "Alice",
    "age": 26,
    "email": "alice@abc.com"  
  },
  {
    "name": "Bob",
    "age": 43,
    "email": "bob@def.com"  
  },
  {
    "name": "Carol",
    "age": 19,
    "email": "carol@xyz.com"  
  }
]
```

**Step 5: Click Insert.**

### Clone One Document

**Step 1: Go to Find tab in Data Explorer.**

Select the collection and go to the Find tab.

Up to 20 documents displays in the tab.

**Step 2: Optional. Specify a filter.**

To specify filter condition, type in a query filter document in the filter bar. For
example, to specify equality condition, use a filter document of the
form:

```javascript
{ <field1>: <value1>, ... }
```

To use query operators to specify a filter condition, use a filter
document of the form:

```javascript
{ <field1>: { <queryoperator>: <value1> }, ... }  
```

**Step 3: Clone the document.**

To clone a document displayed in the query results, hover over the
document and click on its clone document icon.

(Figure: /images/clone-document.png)

The document editor appears with the `_id` field with an
objectid value that reflects the time of its generation and
not the insertion time of the document. As such, the objectid
does not represent a strict insertion order.

**Step 4: Modify the document.**

- To add a new field after an existing field, hover over the field
  and click on the plus sign that appears over the field's line
  number.

- To delete a field, hover over the field and click on the x sign
  that appears to the left of the field's line number. You cannot
  delete the `_id` field.

- To edit a field name, value, or type, click on the field name,
  value, or type.

**Step 5: Click Insert.**

## Edit One Document

To edit a document from a collection through the Data
Explorer:

**Step 1: Go to Find tab in Data Explorer.**

Select the collection and go to the Find tab.

Up to 20 documents displays in the tab.

**Step 2: Optional. Specify a filter.**

To specify filter condition, type in a query filter document in the filter bar. For
example, to specify equality condition, use a filter document of the
form:

```javascript
{ <field1>: <value1>, ... }
```

To use query operators to specify a filter condition, use a filter
document of the form:

```javascript
{ <field1>: { <queryoperator>: <value1> }, ... }  
```

**Step 3: Edit the document.**

To edit a document displayed in the query results, hover over the
document to edit and click on the pencil icon.

The document appears in the document editor:

- To add a new field, hover over the field and click on the plus
  sign that appears over the field's line number.

- To delete a field, hover over the field and click on the x sign
  that appears to the left of the field's line number. You cannot
  delete the `_id` field.

- To edit a field name, value, or type, click on the field name,
  value, or type.

- To revert a specific change, hover over the edited field and click the
  revert icon that appears to the left of the field's line number.

**Step 4: Save or cancel changes.**

To confirm and save changes, click the Update button.

To cancel all modifications to the document, click the
Cancel button.

## Delete One Document

To delete a document from a collection through the Data
Explorer:

**Step 1: Go to Find tab in Data Explorer.**

Select the collection and go to the Find tab.

Up to 20 documents displays in the tab.

**Step 2: Optional. Specify a filter.**

To specify filter condition, type in a query filter document in the filter bar. For
example, to specify equality condition, use a filter document of the
form:

```javascript
{ <field1>: <value1>, ... }
```

To use query operators to specify a filter condition, use a filter
document of the form:

```javascript
{ <field1>: { <queryoperator>: <value1> }, ... }  
```

**Step 3: Delete the document.**

To delete a document displayed in the query results, hover over the
document to delete and click on the trash can icon.

The document is flagged for deletion.

**Step 4: To confirm, click the Delete button.**
