<!-- Converted from core/schema-validation/specify-json-schema.txt (reStructuredText). Includes are inlined. -->

# Specify JSON Schema Validation

JSON Schema is a vocabulary that allows you to annotate and validate
JSON documents. You can use JSON schema to specify validation rules for
your fields in a human-readable format.

## Compatibility

You can use JSON schema validation for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Context

MongoDB supports draft 4 of JSON Schema, including [core specification](https://tools.ietf.org/html/draft-zyp-json-schema-04) and [validation specification](https://tools.ietf.org/html/draft-fge-json-schema-validation-00),
with some differences. For details, see jsonSchema-extension and
json-schema-omission.

For more information about JSON Schema, see the [official website](http://json-schema.org/).

## Restrictions

You can't specify schema validation for:

- Collections in the `admin`, `local`, and `config` databases

- System collections

If you have Client-Side Field Level Encryption or Queryable Encryption enabled on a collection, validation is
subject to the following restrictions:

* For CSFLE, when running `collMod`, the 
  libmongocrypt library prefers the the JSON
  encryption schema specified in the
  command. This enables setting a schema on a collection that does not yet
  have one.

* For Queryable Encryption, any JSON schema that includes an encrypted field results in a
  query analysis error.

## Steps

In this example, you create a `students` collection with validation
rules and observe the results after you attempt to insert an invalid
document.

**Step 1: Connect to your MongoDB deployment.**

To connect to a local MongoDB instance or
MongoDB Atlas deployment using `mongosh`,
refer to the steps in `Connect to a Deployment`
or Connect via mongosh.

**Step 2: Create a collection with validation.**

In `mongosh`, run the following command to 
create a `students` collection and use the 
`$jsonSchema` operator to set schema validation rules:

```javascript
db.createCollection("students", {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         title: "Student Object Validation",
         required: [ "address", "major", "name", "year" ],
         properties: {
            name: {
               bsonType: "string",
               description: "'name' must be a string and is required"
            },
            year: {
               bsonType: "int",
               minimum: 2017,
               maximum: 3017,
               description: "'year' must be an integer in [ 2017, 3017 ] and is required"
            },
            gpa: {
               bsonType: [ "double" ],
               description: "'gpa' must be a double if the field exists"
            }
         }
      }
   }
} )
```

**Tip:** Clarify Rules with Title and Description Fields

You can use `title` and `description` fields to provide an
explanation of validation rules when the rules are not
immediately clear. When a document fails validation, MongoDB
includes these fields in the error output.

**Step 3: Confirm that the validation prevents invalid documents.**

Run the following command. The insert operation fails 
because `gpa` is an integer when the `validator` requires a 
`double`.

```javascript
db.students.insertOne( {
   name: "Alice",
   year: Int32( 2019 ),
   major: "History",
   gpa: Int32(3),
   address: {
      city: "NYC",
      street: "33rd Street"
   }
} )
```

Output:

```json
MongoServerError: Document failed validation

Additional information: {
  failingDocumentId: ObjectId("630d093a931191850b40d0a9"),
  details: {
    operatorName: '$jsonSchema',
    title: 'Student Object Validation',
    schemaRulesNotSatisfied: [
      {
        operatorName: 'properties',
        propertiesNotSatisfied: [
          {
            propertyName: 'gpa',
            description: "'gpa' must be a double if the field exists",
            details: [
              {
                operatorName: 'bsonType',
                specifiedAs: { bsonType: [ 'double' ] },
                reason: 'type did not match',
                consideredValue: 3,
                consideredType: 'int'
              }
            ]
          }
        ]
      }
    ]
  }
}
```

**Step 4: Insert a valid document.**

If you change the `gpa` field value to a `double` type, the 
insert operation succeeds. Run the following command to
insert the valid document:

```javascript
db.students.insertOne( {
   name: "Alice",
   year: NumberInt(2019),
   major: "History",
   gpa: Double(3.0),
   address: {
      city: "NYC",
      street: "33rd Street"
   }
} )
```

**Step 5: Query for the valid document.**

To confirm that you've successfully inserted the document, run
the following command to query the `students` collection:

```javascript
db.students.find()
```

Output:

```json
[
   {
      _id: ObjectId("62bb413014b92d148400f7a5"),
      name: 'Alice',
      year: 2019,
      major: 'History',
      gpa: 3,
      address: { city: 'NYC', street: '33rd Street' }
   }
]
```

**Tip:**

If you're connected to an Atlas deployment, you can also 
view and filter for the document in the Atlas UI.

## Additional Information

You can combine JSON Schema validation with query operator
validation.

For example, consider a `sales` collection with this schema
validation:

```javascript
 db.createCollection("sales", {
   validator: {
     "$and": [
       // Validation with query operators
       {
         "$expr": {
           "$lt": ["$lineItems.discountedPrice", "$lineItems.price"]
         }
       },
       // Validation with JSON Schema
       {
         "$jsonSchema": {
           "properties": {
             "items": { "bsonType": "array" }
           }
          }
        }
      ]
    }
  }
)
```

The preceding validation enforces these rules for documents in the
`sales` collection:

- `lineItems.discountedPrice` must be less than `lineItems.price`.
  This rule is specified using the `$lt` operator.

- The `items` field must be an array. This rule is specified using
  `$jsonSchema`.

## Learn More

- To see the complete list of allowed keywords in a JSON schema, see
  jsonSchema-keywords.

- To restrict what values a certain field can contain, see
  schema-allowed-field-values.

- To avoid issues with JSON schema validation, see
  json-schema-tips.
