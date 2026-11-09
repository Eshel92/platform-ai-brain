<!-- Converted from reference/operator/aggregation/replaceAll.txt (reStructuredText). Includes are inlined. -->

# $replaceAll  (expression operator)

   

## Definition

**`$replaceAll`**

Replaces all instances of a search string in an input string with a
replacement string.

`$replaceAll` is both case-sensitive and
diacritic-sensitive, and ignores any collation present on a
collection.

## Syntax

The `$replaceAll` operator has the following
operator expression syntax:

```javascript
{ $replaceAll: { input: <expression>, find: <expression>, replacement: <expression> } }
```

### Operator Fields

| Field | Description |
|---|---|
| input | .. _replaceAll-input: The string on which you wish to apply the find. Can be any valid expression that resolves to a string or a `null`. If `input` refers to a field that is missing, `$replaceAll` returns `null`. |
| find | .. _replaceAll-find: The string to search for within the given input. Can be any valid expression that resolves to a string or a `null`. If `find` refers to a field that is missing, `$replaceAll` returns `null`. |
| replacement | .. _replaceAll-replacement: The string to use to replace all matched instances of find in input. Can be any valid expression that resolves to a string or a `null`. |

## Behavior

The input, find, and
replacement expressions must evaluate to
a string or a `null`, or `$replaceAll` fails with an
error.

### `$replaceAll` and Null Values

If input or find
refer to a field that is missing, they return `null`.

If *any one* of input,
find, or
replacement evaluates to a `null`, the
entire `$replaceAll` expression evaluates to `null`:

| Example | Result |
|---|---|
| `{ $replaceAll: { input: null, find: "abc", replacement: "ABC" } }` | `null` |
| `{ $replaceAll: { input: "abc", find: null, replacement: "ABC" } }` | `null` |
| `{ $replaceAll: { input: "abc", find: "abc", replacement: null } }` | `null` |

### $replaceAll and Collation

String matching for `$replaceAll` expressions is always case-sensitive
and diacritic-sensitive. Any collation configured is
ignored when performing string comparisons with `$replaceAll`.

For example, create a sample collection with collation strength `1`:

```javascript
db.createCollection( "restaurants", { collation: { locale: "fr", strength: 1 } } )
```

A collation strength of `1` compares base character only and ignores
other differences such as case and diacritics.

Next, insert example documents:

```javascript
db.restaurants.insertMany( [
   { _id: 1, name: "cafe" },
   { _id: 2, name: "Cafe" },
   { _id: 3, name: "café" }
] )
```

The following `$replaceAll` operation tries to find and replace all
instances of "Cafe" in the `name` field:

```javascript
db.restaurants.aggregate( [
{
   $addFields:
      {
         resultObject: {
            $replaceOne: {
               input: "$name",
               find: "Cafe",
               replacement: "CAFE"
            }
         }
      }
}
] )
```

Output:

```javascript
{ "_id" : 1, "name" : "cafe", "resultObject" : "cafe" }
{ "_id" : 2, "name" : "Cafe", "resultObject" : "CAFE" }
{ "_id" : 3, "name" : "café", "resultObject" : "café" }
```

Because `$replaceAll` ignores the collation configured for
this collection, the operation only matches the instance of "Cafe" in
document `2`:

```javascript
{ _id: 1, name: "cafe", resultObject: "cafe" }
{ _id: 2, name: "Cafe", resultObject: "CAFE" }
{ _id: 3, name: "café", resultObject: "café" }
```

Operators that respect collation, such as `$match`, would
match all three documents when performing a string comparison against
"Cafe" due to this collection's collation strength of `1`.

### `$replaceAll` and Unicode Normalization

The `$replaceAll` aggregation expression does not perform
any unicode normalization. This means that string matching for all
`$replaceAll` expressions will consider the number of code points used
to represent a character in unicode when attempting a match.

For example, the character `é` can be represented in unicode using
either one code point or two:

| Unicode | Displays as | Code points |
|---|---|---|
| `\xe9` | `é` | 1 ( `\xe9` ) |
| `e\u0301` | `é` | 2 ( `e` + `\u0301` ) |

Using `$replaceAll` with a find
string where the character `é` is represented in unicode with one code
point will not match any instance of `é` that uses two code points in
the input string.

The following table shows whether a match occurs for a
find string of "café" when compared to
input strings where `é` is represented
by either one code point or two. The find
string in this example uses one code point to represent the `é`
character:

| Example | Match |
|---|---|
| `{ $replaceAll: { input: "caf\xe9", find: "café", replacement: "CAFE" } }` | yes |
| `{ $replaceAll: { input: "cafe\u0301", find: "café", replacement: "CAFE" } }` | no |

Because `$replaceAll` does not perform any unicode
normalization, only the first string comparison matches, where both the
find and input
strings use one code point to represent `é`.

## Example

Create an `inventory` collection with the following documents:

```javascript
db.inventory.insertMany( [
   { _id: 1, item: "blue paint" },
   { _id: 2, item: "blue and green paint" },
   { _id: 3, item: "blue paint with blue paintbrush" },
   { _id: 4, item: "blue paint with green paintbrush" },
] )
```

The following example replaces each instance of "blue paint" in the
`item` field with "red paint":

```javascript
db.inventory.aggregate([
   {
     $project:
      {
         item: { $replaceAll: { input: "$item", find: "blue paint", replacement: "red paint" } }
      }
   }
])
```

The operation returns the following results:

```javascript
{ _id: 1, item: "red paint" }
{ _id: 2, item: "blue and green paint" }
{ _id: 3, item: "red paint with red paintbrush" }
{ _id: 4, item: "red paint with green paintbrush" }
```
