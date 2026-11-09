<!-- Converted from reference/operator/query/jsonSchema.txt (reStructuredText). Includes are inlined. -->

# $jsonSchema

## Definition

**`$jsonSchema`**

The `$jsonSchema` operator matches documents that satisfy
the specified JSON Schema.

## Syntax

The `$jsonSchema` operator expression has the following syntax:

```javascript
{ $jsonSchema: <JSON Schema object> }
```

Where the JSON Schema object is formatted according to [draft 4 of the JSON Schema standard](https://tools.ietf.org/html/draft-zyp-json-schema-04).

```javascript
{ <keyword1>: <value1>, ... }
```

For example:

```javascript
{
  $jsonSchema: {
     required: [ "name", "major", "gpa", "address" ],
     properties: {
        name: {
           bsonType: "string",
           description: "must be a string and is required"
        },
        address: {
           bsonType: "object",
           required: [ "zipcode" ],
           properties: {
               "street": { bsonType: "string" },
               "zipcode": { bsonType: "string" } 
           }
        }
     }
  }
}
```

## JSON Schema

MongoDB supports draft 4 of JSON Schema, including [core specification](https://tools.ietf.org/html/draft-zyp-json-schema-04) and [validation specification](https://tools.ietf.org/html/draft-fge-json-schema-validation-00),
with some differences. For details, see jsonSchema-extension and
json-schema-omission.

For more information about JSON Schema, see the [official website](http://json-schema.org/).

### Available Keywords

You can specify the following keywords in your JSON Schema.

**Note:**

MongoDB implements a subset of keywords available in JSON Schema.
For a complete list of omissions, see json-schema-omission.

| Keyword | Type | Definition | Behavior |
|---|---|---|---|
| additionalItems | arrays | boolean or object | If an object, must be a valid JSON Schema |
| additionalProperties | objects | boolean or object | If `true`, additional fields are allowed. If `false`, they are not. If a valid JSON Schema object is specified, additional fields must validate against the schema. Defaults to `true`. |
| allOf | all types | array of JSON Schema objects | Field must match all specified schemas |
| anyOf | all types | array of JSON Schema objects | Field must match at least one of the specified schemas |
| bsonType | all types | string alias or array of string aliases | Accepts same string aliases used for the `$type` operator |
| dependencies | objects | object | Describes field or schema dependencies |
| description | N/A | string | A string that describes the schema and has no effect on validation. Starting in MongoDB 5.1, if the `description` field is specified, MongoDB includes the `description` in the error output when a document fails validation. |
| enum | all types | array of values | Enumerates all possible values of the field |
| exclusiveMaximum | numbers | boolean | If true and field is a number, `maximum` is an exclusive maximum. Otherwise, it is an inclusive maximum. |
| exclusiveMinimum | numbers | boolean | If true, `minimum` is an exclusive minimum. Otherwise, it is an inclusive minimum. |
| items | arrays | object or array | Must be either a valid JSON Schema, or an array of valid JSON Schemas |
| maximum | numbers | number | Indicates the maximum value of the field |
| maxItems | arrays | integer | Indicates the maximum length of array |
| maxLength | strings | integer | Indicates the maximum length of the field |
| maxProperties | objects | integer | Indicates the field's maximum number of properties |
| minimum | numbers | number | Indicates the minimum value of the field |
| minItems | arrays | integer | Indicates the minimum length of array |
| minLength | strings | integer | Indicates the minimum length of the field |
| minProperties | objects | integer | Indicates the field's minimum number of properties |
| multipleOf | numbers | number | Field must be a multiple of this value |
| not | all types | a JSON Schema object | Field must not match the schema |
| oneOf | all types | array of JSON Schema objects | Field must match exactly one of the specified schemas |
| pattern | strings | string containing a regex | Field must match the regular expression |
| patternProperties | objects | object | In addition to `properties` requirements, each property name of this object must be a valid regular expression |
| properties | objects | object | A valid JSON Schema where each value is also a valid JSON Schema object |
| required | objects | array of unique strings | Object's property set must contain all the specified elements in the array |
| title | N/A | string | A descriptive title string with no effect. |
| type | all types | string or array of unique strings | Enumerates the possible JSON types of the field. Available types are "object", "array", "number", "boolean", "string", and "null". MongoDB's implementation of the JSON Schema does not support the "integer" type. Use the `bsonType` keyword and the "int" or "long" types instead. |
| uniqueItems | arrays | boolean | If true, each item in the array must be unique. Otherwise, no uniqueness constraint is enforced. |

### Extensions

MongoDB's implementation of JSON Schema includes the addition of the `bsonType`
keyword, which allows you to use all BSON types in the
`$jsonSchema` operator. `bsonType` accepts the same string aliases used
for the `$type` operator.

### Omissions

The following are not supported in MongoDB's implementation of JSON Schema:

- [Hypertext definitions](https://tools.ietf.org/html/draft-luff-json-hyper-schema-00)
  in draft 4 of the JSON Schema spec.

- The keywords:

  - `$ref`

  - `$schema`

  - `default`

  - `definitions`

  - `format`

  - `id`

- The `integer` type. You must use the BSON type `int` or `long`
  with the `bsonType` keyword.

- Hypermedia and linking properties of JSON Schema, including the use of
  JSON References and JSON Pointers.

- Unknown keywords.

## Examples

For examples using `$jsonSchema`, see the following pages:

- schema-validation-json
- use-json-schema-query-conditions
