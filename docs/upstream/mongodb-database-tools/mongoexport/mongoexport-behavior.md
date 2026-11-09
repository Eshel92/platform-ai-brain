<!-- Converted from mongoexport/mongoexport-behavior.txt (reStructuredText). Includes are inlined. -->

# mongoexport Behavior, Access, and Usage

**Warning:** Data Import and Export Conflicts With (`$`) and (`.`)

Starting in MongoDB 5.0, document field names can be prefixed with a
dollar character (`$`) and can contain a period character (`.`).
However, `mongoimport` and `mongoexport`
won't work with field names that use those characters.

MongoDB Extended JSON v2
cannot differentiate between type wrappers and fields that happen to
have the same name as type wrappers. Do not use Extended JSON
formats in contexts where the corresponding BSON representations
might include (`$`) prefixed keys. The
DBRef mechanism is an exception to this
general rule. 

There are also restrictions on using `mongoimport` and
`mongoexport` with (`.`) in field names. Since CSV
files use the (`.`) to represent data hierarchies, a (`.`) in a
field name will be misinterpreted as a level of nesting.

   

## Behavior

### Type Fidelity

If you need to preserve all rich BSON data types when using
`mongoexport` to perform full instance backups,
specify Extended JSON v2.0 (Canonical mode) 
to the `--jsonFormat` option:

```javascript
mongoexport --jsonFormat=canonical --collection=<coll> <connection-string>
```

If you don't specify `--jsonFormat`, `mongoexport` outputs data 
in Extended JSON v2.0 (Relaxed mode) by 
default.

`mongoimport` automatically uses the JSON
format found in the specified target data file when restoring. For
example, if the target data export file was created by `mongoexport` 
with `--jsonFormat=canonical` specified, it uses Canonical mode).

### FIPS

`mongoexport` automatically creates FIPS-compliant
connections to a `mongod`/`mongos` that is
configured to use FIPS mode.

### Read Preference

By default, `mongoexport` uses read preference
`primary`. To override the default, you can specify the
read preference in the
`--readPreference` command line
option or in the `--uri connection string`.

If you specify read preference in the URI string and the
`--readPreference`, the
`--readPreference` value
overrides the read preference specified in the URI string.

## Required Access

`mongoexport` requires read access on the target database.

Ensure that the connecting user possesses, at a minimum, the `read`
role on the target database.

When connecting to a `mongod` or `mongos` that enforces
Authentication, ensure you use the required security
parameters based on the configured
authentication mechanism.

## Learn More

- mongoexport
- mongoexport-compatibility-and-installation
- mongoexport-examples
