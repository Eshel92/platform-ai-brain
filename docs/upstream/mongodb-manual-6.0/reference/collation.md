<!-- Converted from reference/collation.txt (reStructuredText). Includes are inlined. -->

# Collation

Collation allows users to specify language-specific rules for string
comparison, such as rules for lettercase and accent marks.

You can specify collation for a collection or a view, an index, or
specific operations that support collation.

To specify collation when you query documents in the MongoDB Atlas UI, see
Specify Collation.

## Collation Document

A collation document has the following fields:

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

Default collation parameter values vary depending on which
locale you specify. For a complete list of default collation
parameters and the locales they are associated with, see
Collation Default Parameters.

* - Field

  - Type

  - Description

* - `locale`

  - string

  - The ICU locale. See collation-languages-locales for a
    list of supported locales.

    To specify simple binary comparison, specify `locale` value of
    `"simple"`.

* - `strength`

  - integer

  - .. _collation-parameter-strength:

    Optional. The level of comparison to perform.
    Corresponds to [ICU Comparison Levels](https://unicode-org.github.io/icu/userguide/collation/concepts.html#comparison-levels).
    Possible values are:

    | Value | Description |
    |---|---|
    | 1 | Primary level of comparison. Collation performs comparisons of the base characters only, ignoring other differences such as diacritics and case. |
    | 2 | Secondary level of comparison. Collation performs comparisons up to secondary differences, such as diacritics. That is, collation performs comparisons of base characters (primary differences) and diacritics (secondary differences). Differences between base characters takes precedence over secondary differences. |
    | 3 | Tertiary level of comparison. Collation performs comparisons up to tertiary differences, such as case and letter variants. That is, collation performs comparisons of base characters (primary differences), diacritics (secondary differences), and case and variants (tertiary differences). Differences between base characters takes precedence over secondary differences, which takes precedence over tertiary differences. This is the default level. |
    | 4 | Quaternary Level. Limited for specific use case to consider punctuation when levels 1-3 ignore punctuation or for processing Japanese text. |
    | 5 | Identical Level. Limited for specific use case of tie breaker. |

    See [ICU Collation: Comparison Levels](https://unicode-org.github.io/icu/userguide/collation/concepts.html#comparison-levels)
    for details.

* - `caseLevel`

  - boolean

  - Optional. Flag that determines whether to include case comparison 
    at `strength` level `1` or `2`.

    If `true`, include case comparison:

    - When used with `strength:1`, collation compares base characters
      and case.

    - When used with `strength:2`, collation compares base characters,
      diacritics (and possible other secondary differences) and case.

    If `false`, do not include case comparison at level `1` or
    `2`. The default is `false`.

    For more information, see [ICU Collation: Case Level](https://unicode-org.github.io/icu/userguide/collation/concepts.html#caselevel).

* - `caseFirst`

  - string

  - Optional. A field that determines sort order of case differences during
    tertiary level comparisons.

    Possible values are: 

    | Value | Description |
    |---|---|
    | `"upper"` | Uppercase sorts before lowercase. |
    | `"lower"` | Lowercase sorts before uppercase. |
    | `"off"` | Default value. Similar to `"lower"` with slight differences. See <https://unicode-org.github.io/icu/userguide/strings/properties.html#customization> for details of differences. |

* - `numericOrdering`

  - boolean

  - Optional. Flag that determines whether to compare numeric strings as numbers
    or as strings.

    If `true`, compare as numbers. For example,
    `"10"` is greater than `"2"`.

    If `false`, compare as strings. For example,
    `"10"` is less than `"2"`.

    Default is `false`.

    See numericOrdering Restrictions.

* - `alternate`

  - string

  - Optional. Field that determines whether collation should consider whitespace
    and punctuation as base characters for purposes of comparison.

    Possible values are:

    | Value | Description |
    |---|---|
    | `"non-ignorable"` | Whitespace and punctuation are considered base characters. |
    | `"shifted"` | Whitespace and punctuation are not considered base characters and are only distinguished at strength levels greater than 3. |

    See [ICU Collation: Comparison Levels](https://unicode-org.github.io/icu/userguide/collation/concepts.html#comparison-levels)
    for more information.

    Default is `"non-ignorable"`.

* - `maxVariable`

  - string

  - Optional. Field that determines up to which characters are considered
    ignorable when `alternate: "shifted"`. Has no effect if
    `alternate: "non-ignorable"`

    Possible values are:

    | Value | Description |
    |---|---|
    | `"punct"` | Both whitespace and punctuation are ignorable and not considered base characters. |
    | `"space"` | Whitespace is ignorable and not considered to be base characters. |

* - `backwards`

  - boolean

  - Optional. Flag that determines whether strings with diacritics sort from back
    of the string, such as with some French dictionary ordering.

    If `true`, compare from back to front.

    If `false`, compare from front to back.

    The default value is `false`.

* - `normalization`

  - boolean

  - Optional. Flag that determines whether to check if text require normalization
    and to perform normalization. Generally, majority of text does not
    require this normalization processing.

    If `true`, check if fully normalized and perform normalization to
    compare text.

    If `false`, does not check.

    The default value is `false`.

    See
    <https://unicode-org.github.io/icu/userguide/collation/concepts.html#normalization> for details.
       
          
   

## Operations that Support Collation

You can specify collation for the following operations:

**Note:**

You cannot specify multiple collations for an operation. For
example, you cannot specify different collations per field, or if
performing a find with a sort, you cannot use one collation for the
find and another for the sort.

| Commands | `mongosh` Methods |
|---|---|
| `create` | \| `db.createCollection()` \| `db.createView()` |
| `createIndexes` [#index-restriction]_ | `db.collection.createIndex()` [#index-restriction]_ |
| `aggregate` | `db.collection.aggregate()` |
| `distinct` | `db.collection.distinct()` |
| `findAndModify` | \| `db.collection.findAndModify()` \| `db.collection.findOneAndDelete()` \| `db.collection.findOneAndReplace()` \| `db.collection.findOneAndUpdate()` |
| `find` | `cursor.collation()` to specify collation for `db.collection.find()` |
| `mapReduce` | `db.collection.mapReduce()` |
| `delete` | \| `db.collection.deleteOne()` \| `db.collection.deleteMany()` \| `db.collection.remove()` |
| `update` | \| `db.collection.updateOne()`, \| `db.collection.updateMany()`, \| `db.collection.replaceOne()` |
| `shardCollection` | \| `sh.shardCollection()` |
| `count` | \| `db.collection.count()` |
|  | Individual update, replace, and delete operations in `db.collection.bulkWrite()`. |

       

## Behavior

### Local Variants

Some collation locales have variants, which employ special
language-specific rules. To specify a locale variant, use the following
syntax:

```javascript
{ "locale" : "<locale code>@collation=<variant>" }
```

For example, to use the `unihan` variant of the Chinese collation:

```javascript
{ "locale" : "zh@collation=unihan" }
```

For a complete list of all collation locales and their variants, see
Collation Locales.

### Collation and Views

- You can specify a default collation
  for a view at creation time. If no collation is specified, the
  view's default collation is the "simple" binary comparison
  collator. That is, the view does not inherit the collection's
  default collation.

- String comparisons on the view use the view's default collation.
  An operation that attempts to change or override a view's default
  collation will fail with an error.

- If creating a view from another view, you cannot specify a
  collation that differs from the source view's collation.

- .. include:: /includes/extracts/views-collation-agg.rst

### Collation and Index Use

To use an index for string comparisons, an operation must also
specify the same collation. That is, an index with a collation
cannot support an operation that performs string comparisons on the
indexed fields if the operation specifies a different collation.

**Warning:**

Because indexes that are configured with collation use ICU
collation keys to achieve sort order, collation-aware index keys
may be larger than index keys for indexes without collation. 

A `restaurants` collection has the following documents:

```javascript
db.restaurants.insertMany( [
   { _id: 1, category: "café", status: "Open" },
   { _id: 2, category: "cafe", status: "open" },
   { _id: 3, category: "cafE", status: "open" }
] )
```

The `restaurants` collection has an index on a string field
`category` with the collation locale `"fr"`.

```javascript
db.restaurants.createIndex( { category: 1 }, { collation: { locale: "fr" } } )
```

The following query, which specifies the same collation as the index,
can use the index:

```javascript
db.restaurants.find( { category: "cafe" } ).collation( { locale: "fr" } )
```

However, the following query operation, which by default uses the
"simple" binary collator, cannot use the index:

```javascript
db.restaurants.find( { category: "cafe" } )
```

For a compound index where the index prefix keys are not strings,
arrays, and embedded documents, an operation that specifies a
different collation can still use the index to support comparisons
on the index prefix keys.

For example, the collection `restaurants` has a compound index on the
numeric fields `score` and `price` and the string field
`category`; the index is created with the  collation locale
`"fr"` for string comparisons:

```javascript
db.restaurants.createIndex(
   { score: 1, price: 1, category: 1 },
   { collation: { locale: "fr" } } )
```

The following operations, which use `"simple"` binary collation
for string comparisons, can use the index:

```javascript
db.restaurants.find( { score: 5 } ).sort( { price: 1 } )
db.restaurants.find( { score: 5, price: { $gt: NumberDecimal( "10" ) } } ).sort( { price: 1 } )
```

The following operation, which uses `"simple"` binary collation
for string comparisons on the indexed `category` field, can use
the index to fulfill only the `score: 5` portion of the query:

```javascript
db.restaurants.find( { score: 5, category: "cafe" } )
```

To confirm whether a query used an index, run the query with the
`explain()` option.

**Important:**

Matches against document keys, including embedded document keys, 
use simple binary comparison. This means that a query for a key  
like "type.café" will not match the key "type.cafe", regardless of
the value you set for the strength parameter.

#### Collation and Unsupported Index Types

The following indexes only support simple binary comparison and do
not support collation:

- text indexes, 

- 2d indexes, and 

- geoHaystack indexes.

**Tip:**

To create a `text`, a `2d`, or a `geoHaystack` index on a
collection that has a non-simple collation, you must explicitly
specify `{collation: {locale: "simple"} }` when creating the
index.

## Restrictions

### numericOrdering

When specifying the `numericOrdering` as `true` the following 
restrictions apply:

- Only contiguous non-negative integer substrings of digits are 
  considered in the comparisons. 

  `numericOrdering` does not support:

  - `+`
  - `-`
  - decimal separators, like decimal points and decimal commas
  - exponents

- Only Unicode code points in the Number or Decimal Digit (Nd) category 
  are treated as digits.

- If a digit length exceeds 254 characters, the excess characters are 
  treated as a separate number.

Consider a collection with the following string number and decimal 
values:

```javascript
db.c.insertMany(
  [
      { "n" : "1" },
      { "n" : "2" },
      { "n" : "2.1" },
      { "n" : "-2.1" },
      { "n" : "2.2" },
      { "n" : "2.10" },
      { "n" : "2.20" },
      { "n" : "-10" },
      { "n" : "10" },
      { "n" : "20" },
      { "n" : "20.1" }
  ]
)
```

The following `find` query uses a 
collation document containing the `numericOrdering` parameter:

```javascript
db.c.find(
   { }, { _id: 0 }
).sort(
  { n: 1 }
).collation( {
  locale: 'en_US',
  numericOrdering: true
} )
```

The operation returns the following results:

```javascript
[
    { n: '-2.1' },
    { n: '-10' },
    { n: '1' },
    { n: '2' },
    { n: '2.1' },
    { n: '2.2' },
    { n: '2.10' },
    { n: '2.20' },
    { n: '10' },
    { n: '20' },
    { n: '20.1' }
]
```

- `numericOrdering: true` sorts the string values in ascending 
  order as if they were numeric values.
- The two negative values `-2.1` and `-10` are not sorted in the 
  expected sort order because they have unsupported `-` characters.
- The value `2.2` is sorted before the value `2.10`, due to the fact
  that the `numericOrdering` parameter does not support decimal 
  values.
- As a result, `2.2` and `2.10` are sorted in lexicographic order.

## Example

A `restaurants` collection has the following documents:

```javascript
db.restaurants.insertMany( [
   { _id: 1, category: "café", status: "Open" },
   { _id: 2, category: "cafe", status: "open" },
   { _id: 3, category: "cafE", status: "open" }
] )
```

The following `find()` operation uses
collation:

```javascript
db.restaurants.find(
   { category: "cafe", status: "Open" }
).collation( { locale: "fr", strength: 1 } )
```

Output:

```javascript
[
   { _id: 1, category: 'café', status: 'Open' },
   { _id: 2, category: 'cafe', status: 'open' },
   { _id: 3, category: 'cafE', status: 'open' }
]
```

The filter specifies a collation with `strength: 1`, which means the
query ignores differences between case and letter variants. As a result,
even though there is not a document that has an exact match with the
specified case and letter variants in the filter, the operation returns
all documents in the collection.
