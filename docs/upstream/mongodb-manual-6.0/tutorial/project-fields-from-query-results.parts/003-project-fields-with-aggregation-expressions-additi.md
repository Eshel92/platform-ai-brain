<!-- Part 3 of 3 of tutorial/project-fields-from-query-results.md (split because the page is big). -->

## Project Fields with Aggregation Expressions

You can specify aggregation expressions
in a query projection. Aggregation expressions let you project new
fields and modify the values of existing fields.

For example, the following operation uses aggregation expressions to
override the value of the `status` field, and project new fields
`area` and `reportNumber`.

**Note:**

The following example uses MongoDB Shell syntax. For driver examples
of projection with aggregation, see your `driver
documentation`.

```javascript
db.inventory.find(
   { },
   {
      _id: 0,
      item: 1,
      status: {
         $switch: {
            branches: [
               {
                  case: { $eq: [ "$status", "A" ] },
                  then: "Available"
               },
               {
                  case: { $eq: [ "$status", "D" ] },
                  then: "Discontinued"
               },
            ],
            default: "No status found"
         }
      },
      area: {
         $concat: [
            { $toString: { $multiply: [ "$size.h", "$size.w" ] } },
            " ",
            "$size.uom"
         ]
      },
      reportNumber: { $literal: 1 }
   }
)
```

Output:

```javascript
[
   {
      item: 'journal',
      status: 'Available',
      area: '294 cm',
      reportNumber: 1
   },
   {
      item: 'planner',
      status: 'Discontinued',
      area: '685.5 cm',
      reportNumber: 1
   },
   {
      item: 'notebook',
      status: 'Available',
      area: '93.5 in',
      reportNumber: 1
   },
   {
      item: 'paper',
      status: 'Discontinued',
      area: '93.5 in',
      reportNumber: 1
   },
   {
      item: 'postcard',
      status: 'Available',
      area: '152.5 cm',
      reportNumber: 1
   }
]
```


## Additional Considerations

MongoDB enforces additional restrictions with regards to projections. 
See `Projection Restrictions` for details.

**See also:**

- find-projection

- /tutorial/query-documents
