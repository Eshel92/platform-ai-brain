<!-- Converted from reference/bson-type-comparison-order.txt (reStructuredText). Includes are inlined. -->

# Comparison/Sort Order

When comparing values of different BSON types in
sort operations, MongoDB uses the following comparison order, from
lowest to highest:

#. MinKey (internal type)
#. Null
#. Numbers (ints, longs, doubles, decimals)
#. Symbol, String
#. Object
#. Array
#. BinData
#. ObjectId
#. Boolean
#. Date
#. Timestamp
#. Regular Expression
#. JavaScript Code
#. JavaScript Code with Scope
#. MaxKey (internal type)

Aggregation expressions make comparisons across types. 
For more information, see aggregation-comparison-operators.

**Note:**

MongoDB enforces comparisons with query-selectors-comparison
only on documents where the BSON type of the target field 
matches the query operand type through type-bracketing.

## Numeric Types

MongoDB treats some types as equivalent for comparison purposes.
For instance, all numeric types are considered equivalent in comparisons.

## Strings

### Binary Comparison

By default, MongoDB uses the simple binary comparison to compare
strings.

### Collation

Collation allows users to specify
language-specific rules for string comparison, such as rules for
lettercase and accent marks.

Collation specification has the following syntax:

```none
{
   locale: <string>,
   caseLevel: <boolean>,
   caseFirst: <string>,
   strength: <int>,
   numericOrdering: <boolean>,
   alternate: <string>,
   maxVariable: <string>,
   backwards: <boolean>
}
```

When specifying collation, the `locale` field is mandatory; all
other collation fields are optional. For descriptions of the fields,
see collation-document-fields.

If no collation is specified for the collection or for the
operations, MongoDB uses the simple binary comparison used in prior
versions for string comparisons.

## Arrays

### Sort Order

When you sort on a field that contains an array:

- An ascending sort compares the smallest elements of the array
  according to the BSON type sort order.

- A descending sort compares the largest elements of the array
  according to the reverse BSON type sort order.

- A sort on a field whose value is a one element array (for example,
  `[ 1 ]`) and a field whose value is not an array (for example,
  `2`) sorts on `1` and `2`.

- A sort places an empty array (for example, `[ ]`) before a
  `null` value or a missing field value.

- A sort of a nested array (for example, `[[1, 2], [3, 4]]`) sorts
  any array after the outermost array lexicographically.

### Comparison Operators

When you query a field that contains an array:

- Comparison query predicate operators,
  such as `$lt` and `$gt`, enforce
  type bracketing when the query value is an
  array.

- If the target field's value is an array, the operator performs a
  type-bracketed comparison element-wise over the array.

- Comparison operators compare arrays lexicographically.

## Objects

MongoDB's comparison of BSON objects uses the following order:

#. Recursively compare key-value pairs in the order that they appear
   within the BSON object.

#. Compare the field types. MongoDB uses the following comparison
   order for field types, from lowest to highest:

   a. MinKey (internal type)
   #. Null
   #. Numbers (ints, longs, doubles, decimals)
   #. Symbol, String
   #. Object
   #. Array
   #. BinData
   #. ObjectId
   #. Boolean
   #. Date
   #. Timestamp
   #. Regular Expression
   #. JavaScript Code
   #. JavaScript Code with Scope
   #. MaxKey (internal type)

#. If the field types are equal, compare the
   key field names.

#. If the key field names are equal, compare the field values.

#. If the field values are equal, compare the next key/value pair
   (return to step 1). An object without further pairs is less than an
   object with further pairs.

## Dates and Timestamps

Date objects sort before Timestamp objects.

## Non-existent Fields

The comparison treats a non-existent field as if it were null. A
sort on the `a` field in documents `{ }` and `{ a: null }` 
would treat the documents as equivalent in sort order.

## BinData

MongoDB sorts `BinData` in the following order:

#. First, the length or size of the data.

#. Then, by the BSON one-byte subtype.

#. Finally, by the data, performing a byte-by-byte comparison on unsigned bytes.
