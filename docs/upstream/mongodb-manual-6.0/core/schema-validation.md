<!-- Converted from core/schema-validation.txt (reStructuredText). Includes are inlined. -->

# Schema Validation

Schema validation lets you create validation rules for your fields, such
as allowed data types and value ranges.

MongoDB uses a flexible schema model, which means that documents in a
collection do not need to have the same fields or data types by default.
Once you've established an application schema, you can use schema
validation to ensure there are no unintended schema changes or improper
data types.

You can implement schema validation in the UI for deployments hosted in [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server).

## When to Use Schema Validation

Your schema validation needs depend on how users use your application.
When your application is in the early stages of development, schema
validation may impose unhelpful restrictions because you don't know how
you want to organize your data. Specifically, the fields in your
collections may change over time.

Schema validation is most useful for an established application where
you have a good sense of how to organize your data. You can use schema
validation in the following scenarios:

- For a users collection, ensure that the `password` field is only
  stored as a string. This validation prevents users from saving their
  password as an unexpected data type, like an image.

- For a sales collection, ensure that the `item` field belongs to a
  list of items that your store sells. This validation prevents a user
  from accidentally misspelling an item name when entering sales data.

- For a students collection, ensure that the `gpa` field is always a
  positive number. This validation prevents errors during data entry.

## When MongoDB Checks Validation

After you add schema validation rules to a collection:

- All document inserts must match the rules.
- The schema validation level defines how the rules are applied to
  existing documents and document updates. To learn more, see
  schema-specify-validation-level.

To find documents in a collection that don't match the schema validation
rules, see use-json-schema-query-conditions-find-documents.

## What Happens When a Document Fails Validation

By default, when an insert or update operation would result in an
invalid document, MongoDB rejects the operation and does not write the
document to the collection.

Alternatively, you can configure MongoDB to allow invalid documents and
log warnings when schema violations occur.

To learn more, see schema-validation-handle-invalid-docs.

## Tasks

For common tasks involving schema validation, see the following pages:

- schema-validation-json
- schema-validation-query-expression
- schema-allowed-field-values
- schema-view-validation-rules
- schema-update-validation
- use-json-schema-query-conditions
- schema-bypass-document-validation

## Learn More

To learn about MongoDB's flexible schema model, see
manual-data-modeling-intro.
