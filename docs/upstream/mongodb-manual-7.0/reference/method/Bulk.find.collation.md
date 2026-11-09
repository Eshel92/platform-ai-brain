<!-- Converted from reference/method/Bulk.find.collation.txt (reStructuredText). Includes are inlined. -->

# Bulk.find.collation() (mongosh method)

## Description

**`Bulk.find.collation(<document>)`**

Specifies the collation for the bulk writes.
Append to `Bulk.find()` method to specify collation for the find operation.

The `Bulk.find.collation()` accepts the following collation
document:

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

  - Optional. The level of comparison to perform.
    Corresponds to [ICU Comparison Levels](https://unicode-org.github.io/icu/userguide/collation/concepts.html#comparison-levels).
    Possible values are:

    - `1`: Primary level of comparison. Collation performs
      comparisons of the base characters only, ignoring other
      differences such as diacritics and case.

    - `2`: Secondary level of comparison. Collation performs
      comparisons up to secondary differences, such as diacritics.
      That is, collation performs comparisons of base characters
      (primary differences) and diacritics (secondary differences).
      Differences between base characters takes precedence over
      secondary differences.

    - `3`: Tertiary level of comparison. Collation performs
      comparisons up to tertiary differences, such as case and
      letter variants. That is, collation performs comparisons of
      base characters (primary differences), diacritics (secondary
      differences), and case and variants (tertiary differences).
      Differences between base characters takes precedence over
      secondary differences, which takes precedence over tertiary
      differences. This is the default level.

    - `4`: Quaternary Level. Limited for specific use case to
      consider punctuation when levels 1-3 ignore punctuation
      or for processing Japanese text.

    - `5`: Identical Level. Limited for specific use case of tie
      breaker.

    See [ICU Collation: Comparison Levels](https://unicode-org.github.io/icu/userguide/collation/concepts.html#comparison-levels)
    for details.

* - `caseLevel`

  - boolean

  - Optional. Flag that determines whether to include case comparison at
    `strength` level `1` or `2`.

    If `true`, include case comparison; i.e.

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

    - `"upper"`: Uppercase sorts before lowercase.

    - `"lower"`: Lowercase sorts before uppercase.

    - `"off"`: Default value. Similar to `"lower"` with slight
      differences. See the [ICU customization options](https://unicode-org.github.io/icu/userguide/strings/properties.html#customization)
      for details of the differences.

* - `numericOrdering`

  - boolean

  - Optional. Flag that determines whether to compare numeric strings as numbers
    or as strings.

    If `true`, compare as numbers; i.e. `"10"` is greater than
    `"2"`.

    If `false`, compare as strings; i.e. `"10"` is less than `"2"`.

    Default is `false`.

* - `alternate`

  - string

  - Optional. Field that determines whether collation should consider whitespace
    and punctuation as base characters for purposes of comparison.

    Possible values are:

    - `"non-ignorable"`: Whitespace and punctuation are considered
      base characters.

    - `"shifted"`: Whitespace and punctuation are not considered
      base characters and are only distinguished at strength levels
      greater than 3.

    See [ICU Collation: Comparison Levels](https://unicode-org.github.io/icu/userguide/collation/concepts.html#comparison-levels)
    for more information.

    Default is `"non-ignorable"`.

* - `maxVariable`

  - string

  - Optional. Field that determines up to which characters are considered
    ignorable when `alternate: "shifted"`. Has no effect if
    `alternate: "non-ignorable"`

    Possible values are:

    - `"punct"`: Both whitespace and punctuation are ignorable
      and not considered base characters.

    - `"space"`: Whitespace is ignorable and not considered to
      be base characters.

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

    See [ICU Collation: Normalization](https://unicode-org.github.io/icu/userguide/collation/concepts.html#normalization)
    for details.
          
          
   

## Compatibility

This command is available in deployments hosted in the following
environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

  

## Example

A `restaurants` collection has the following documents:

```javascript
db.restaurants.insertMany( [
   { _id: 1, category: "café", status: "Open" },
   { _id: 2, category: "cafe", status: "open" },
   { _id: 3, category: "cafE", status: "open" }
] )
```

The following example initializes a `Bulk()` operations builder
for the `restaurants` collection and specifies a collation for the
find filter.

```javascript
var bulk = db.restaurants.initializeUnorderedBulkOp();

bulk.find(
   { category: "cafe" }
).collation( 
   { locale: "fr", strength: 1 } 
).update(
   { $set: { status: "closed", points: "0" } }
);

bulk.execute();
```

Output:

```javascript
   {
      acknowledged: true,
      insertedCount: 0,
      insertedIds: {},
      matchedCount: 3,
      modifiedCount: 3,
      deletedCount: 0,
      upsertedCount: 0,
      upsertedIds: {}
   }
```

The operation specifies a collation with `strength: 1`, which
means the collation ignores differences between case and letter
variants. As a result, even though there is only one document that has
an exact match as the string specified in the filter (`cafe`), the
operation matches and updates all documents in the collection.

After the bulk operation completes, the collection contains these
documents:

```javascript
[
   { _id: 1, category: 'café', status: 'closed', points: '0' },
   { _id: 2, category: 'cafe', status: 'closed', points: '0' },
   { _id: 3, category: 'cafE', status: 'closed', points: '0' }
]
```

## Learn More

- `db.collection.initializeUnorderedBulkOp()`
- `db.collection.initializeOrderedBulkOp()`
- `Bulk.find()`
- `Bulk.find.updateOne()`
- `Bulk.execute()`
- All Bulk Methods
