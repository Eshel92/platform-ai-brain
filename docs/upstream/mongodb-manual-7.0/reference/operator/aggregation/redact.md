<!-- Converted from reference/operator/aggregation/redact.txt (reStructuredText). Includes are inlined. -->

# $redact (aggregation stage)

## Definition

**`$redact`**

Restricts entire documents or content within documents from being outputted 
based on information stored in the documents themselves.

(Figure: /images/redact-security-architecture.bakedsvg.svg)

The `$redact` stage has the following prototype form:

```javascript
{ $redact: <expression> }
```

The argument can be any valid expression as long as it resolves to the
`$$DESCEND`, `$$PRUNE`, or `$$KEEP` system variables. For more
information on expressions, see aggregation-expressions.

| System Variable | Description |
|---|---|
| _`$$DESCEND` | `$redact` returns the fields at the current document level, excluding embedded documents. To include embedded documents and embedded documents within arrays, apply the `$cond` expression to the embedded documents to determine access for these embedded documents. |
| _`$$PRUNE` | `$redact` excludes all fields at this current document/embedded document level, **without** further inspection of any of the excluded fields. This applies even if the excluded field contains embedded documents that may have different access levels. |
| _`$$KEEP` | `$redact` returns or keeps all fields at this current document/embedded document level, **without** further inspection of the fields at this level. This applies even if the included field contains embedded documents that may have different access levels. |

## Examples

**shell:**

The examples in this section use the
`db.collection.aggregate()` helper.

### Evaluate Access at Every Document Level

A `forecasts` collection contains documents of the following form
where the `tags` field lists the different access values for that
document/embedded document level; i.e. a value of `[ "G", "STLW" ]`
specifies either `"G"` or `"STLW"` can access the data:

```javascript
db.forecasts.insertOne( 
   {
      _id: 1,
      title: "123 Department Report",
      tags: [ "G", "STLW" ],
      year: 2014,
      subsections: [
         {
         subtitle: "Section 1: Overview",
         tags: [ "SI", "G" ],
         content:  "Section 1: This is the content of section 1."
         },
         {
         subtitle: "Section 2: Analysis",
         tags: [ "STLW" ],
         content: "Section 2: This is the content of section 2."
         },
         {
         subtitle: "Section 3: Budgeting",
         tags: [ "TK" ],
         content: {
            text: "Section 3: This is the content of section 3.",
            tags: [ "HCS" ]
         }
         }
      ]
   }
)
```

A user has access to view information with either the tag `"STLW"` or
`"G"`. To run a query on all documents with year `2014` for this
user, include a `$redact` stage as in the following:

```javascript
var userAccess = [ "STLW", "G" ];
db.forecasts.aggregate(
   [
   { $match: { year: 2014 } },
   { $redact: {
      $cond: {
         if: { $gt: [ { $size: { $setIntersection: [ "$tags", userAccess ] } }, 0 ] },
         then: "$$DESCEND",
         else: "$$PRUNE"
         }
      }
   }
   ]
);
```

The aggregation operation returns the following "redacted" document:

```javascript
{
   _id: 1,
   title: "123 Department Report",
   tags: [ "G", "STLW" ],
   year: 2014,
   subsections: [
      {
      subtitle: "Section 1: Overview",
      tags: [ "SI", "G" ],
      content: "Section 1: This is the content of section 1."
      },
      {
      subtitle: "Section 2: Analysis",
      tags: [ "STLW" ],
      content : "Section 2: This is the content of section 2."
      }
   ]
}
```

**See also:**

- `$size`
- `$setIntersection`

### Exclude All Fields at a Given Level

A collection `accounts` contains the following document:

```javascript
db.accounts.insertOne(
   {
      _id: 1,
      level: 1,
      acct_id: "xyz123",
      cc: {
         level: 5,
         type: "yy",
         num: 000000000000,
         exp_date: ISODate("2015-11-01T00:00:00.000Z"),
         billing_addr: {
         level: 5,
         addr1: "123 ABC Street",
         city: "Some City"
         },
         shipping_addr: [
         {
            level: 3,
            addr1: "987 XYZ Ave",
            city: "Some City"
         },
         {
            level: 3,
            addr1: "PO Box 0123",
            city: "Some City"
         }
         ]
      },
      status: "A"
   }
)
```

In this example document, the `level` field determines the access
level required to view the data.

To run a query on all documents with status `A` and exclude *all*
fields contained in a document/embedded document at level `5`, include a
`$redact` stage that specifies the system variable
`"$$PRUNE"` in the `then` field:

```javascript
db.accounts.aggregate(
   [
      { $match: { status: "A" } },
      {
         $redact: {
         $cond: {
            if: { $eq: [ "$level", 5 ] },
            then: "$$PRUNE",
            else: "$$DESCEND"
         }
         }
      }
   ]
);
```

The `$redact` stage evaluates the `level` field to
determine access. If the `level` field equals `5`, then exclude all
fields at that level, even if the excluded field contains embedded documents
that may have different `level` values, such as the `shipping_addr`
field.

The aggregation operation returns the following "redacted" document:

```json
:copyable; false

{
   _id: 1,
   level: 1,
   acct_id: "xyz123",
   status: "A"
}
```

The result set shows that the `$redact` stage excluded
the field `cc` as a whole, including the `shipping_addr` field
which contained embedded documents that had `level` field values equal to
`3` and not `5`.

**See also:**

/tutorial/implement-field-level-redaction for
steps to set up multiple combinations of access for the same data.

**nodejs:**

The Node.js examples on this page use the `sample_mflix` database from the
Atlas sample datasets. To learn how to create a free
MongoDB Atlas cluster and load the sample datasets, see `Get Started` in the MongoDB Node.js driver documentation.

To use the MongoDB Node.js driver to add a `$redact` stage to an aggregation
pipeline, use the `$redact` operator in a pipeline object.

The following example creates a pipeline stage that keeps documents in which the value of the `imdb.rating` field is
greater than or equal to `9`. The stage excludes all other
documents. The
example then runs the aggregation pipeline:

```javascript
const pipeline = [
  { 
    $redact: {
      $cond: {  
        if: { $gte: ["$imdb.rating", 9] }, 
        then: "$$KEEP", 
        else: "$$PRUNE"  
      }
    }
  }
];

const cursor = collection.aggregate(pipeline);
return cursor;
```

## Learn More

To learn more about the system variables in this guide, see the
Aggregation Variables page.
