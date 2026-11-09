<!-- Converted from mongoimport/mongoimport-behavior.txt (reStructuredText). Includes are inlined. -->

# mongoimport Behavior, Access, and Usage

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

### JSON Format

`mongoimport` requires import data to be in either
Extended JSON v2.0 (Canonical) or
Extended JSON v2.0 (Relaxed) format by default. For import data
formatted using Extended JSON v1.0, specify the
`--legacy` option.

**Tip:**

In general, the versions of `mongoexport` and
`mongoimport` should match. That is, to import data
created from `mongoexport`, you should use the
corresponding version of `mongoimport`.

### Document Order

By default, `mongoimport` may insert documents in a random order. To
preserve document order during the restore process, use
`--maintainInsertionOrder`.

### Encoding

`mongoimport` only supports data files that are UTF-8 encoded.
Using other encodings produces errors.

### FIPS

`mongoimport` automatically creates FIPS-compliant
connections to a `mongod`/`mongos` that is
configured to use FIPS mode.

### Write Concern

If you specify write concern in both the
`--writeConcern` option and the
`--uri connection string` option, the
`--writeConcern` value overrides
the write concern specified in the URI string.

### Batches

`mongoimport` uses a maximum batch size of 100,000 to
perform bulk insert/upsert operations.

### Time Series Collections

To import time series data, you must create a time series collection
before running `mongoimport`. `mongoimport` does not support creating time series collections
automatically. For more information about creating a collection, see `createCollection()`.

### Crash Behavior

If `mongoimport` crashes, it can leave the system in an 
inconsistent state where only *some* of the data was imported, 
but not all of it. After a crash, delete any imported data and 
rerun the process from the beginning.

## Required Access

In order to connect to a `mongod` that enforces authorization
with the `--auth` option, you must use the
`--username` and `--password` options. The connecting user must
possess, at a minimum, the `readWrite` role on the database
into which they are importing data.

## Learn More

- mongoimport
- mongoimport-compatibility-and-installation
- mongoimport-examples
