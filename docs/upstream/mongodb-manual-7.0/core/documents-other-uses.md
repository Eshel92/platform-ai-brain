<!-- Converted from core/documents-other-uses.txt (reStructuredText). Includes are inlined. -->

# Document Structure Use Cases

In addition to defining data records, MongoDB uses the document
structure throughout, including but not limited to: query filters, update specifications documents, and index specification
documents

## Query Filter Documents

Query filter documents specify the conditions that determine which
records to select for read, update, and delete operations.

You can use `<field>:<value>` expressions to specify the equality
condition and query operator
expressions.

```javascript
{
  <field1>: <value1>,
  <field2>: { <operator>: <value> },
  ...
}
```

For examples, see:

- /tutorial/query-documents

- /tutorial/query-embedded-documents

- /tutorial/query-arrays

- /tutorial/query-array-of-documents/

## Update Specification Documents

Update specification documents use update operators to specify the data modifications to perform on
specific fields during an update operation.

```javascript
{
  <operator1>: { <field1>: <value1>, ... },
  <operator2>: { <field2>: <value2>, ... },
  ...
}
```

For examples, see Update specifications.

## Index Specification Documents

Index specification documents define the field to index and the index
type:

```javascript
{ <field1>: <type1>, <field2>: <type2>, ...  }
```
