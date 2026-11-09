<!-- Converted from core/dot-dollar-considerations.txt (reStructuredText). Includes are inlined. -->

# Field Names with Periods and Dollar Signs

Avoid using dollar signs (`$`) or periods (`.`) in your field
names. MongoDB stores documents that use these characters in field
names, but discourages them for these reasons:

- **Query performance.** You can't index these fields, which can
  make queries on them less efficient. To learn which other features
  these fields can't use, see dot-dollar-general-restrictions.

- **Queryability.** You can't query these fields directly. To read or
  modify them, you need helper methods like `$getField`,
  `$setField`, and `$literal`. Without those
  helpers, MongoDB interprets a field name that contains a period as
  a path to an embedded field.

The field name validation rules are not the same for all types of
storage operations.

## General Restrictions

There are some general restrictions on using dollar (`$`) prefixed field names
or field names that contain a period (`.`). These fields cannot: 

- Be indexed
- Be used as part of a shard key
- Be validated using `$jsonSchema`
- Be modified with an escape sequence
- Be used with
  `Field Level Encryption`
- Be used as a subfield in an `_id` document
- Have more than 255 words separated by periods in field names
- (`$`-prefix only) Be relied on at the root level of a document if
  the field name collides with a field name MongoDB reserves for
  internal document metadata

MongoDB reserves a set of `$`-prefixed field names for internal
document metadata. If a root-level field name in your data collides
with one of those reserved names, MongoDB might not preserve the field
or return it to queries, and in some cases removes the field from
results. These reserved names are internal and can change between
releases, so don't store data in root-level `$`-prefixed field names
or rely on being able to read them back.

**Warning:** Possible Data Loss With Dollar Signs (`$`) and Periods (`.`)

There is a small chance of data loss when using dollar (`$`) prefixed
field names or field names that contain periods (`.`) if these
field names are used in conjunction with unacknowledged writes
(write concern `w=0`) on servers
that are older than MongoDB 5.0.

When running `insert`, `update`, and 
`findAndModify` commands, drivers that are 5.0 compatible 
remove restrictions on using documents with field names that are 
dollar (`$`) prefixed or that contain periods (`.`). These field 
names generated a client-side error in earlier driver versions.

The restrictions are removed regardless of the server version the
driver is connected to. If a 5.0 driver sends a document to an older
server, the document will be rejected without sending an error.

**Warning:** Import and Export Concerns With Dollar Signs (`$`) and Periods (`.`)

Starting in MongoDB 5.0, document field names can be dollar (`$`)
prefixed and can contain periods (`.`). However,
`mongoimport` and `mongoexport` may not work
as expected in some situations with field names that make use of these
characters.

MongoDB Extended JSON v2
cannot differentiate between type wrappers and fields that happen to
have the same name as type wrappers. Do not use Extended JSON
formats in contexts where the corresponding BSON representations
might include dollar (`$`) prefixed keys. The
DBRef mechanism is an exception to this
general rule. 

There are also restrictions on using `mongoimport` and
`mongoexport` with periods (`.`) in field names. Since
CSV files use the period (`.`) to represent data hierarchies, a
period (`.`) in a field name will be misinterpreted as a level of
nesting.

## Learn More

For examples of how to handle field names that contain periods and
dollar signs, see these pages:

- dollar-prefix-field-names

- period-field-names
