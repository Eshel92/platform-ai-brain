<!-- Converted from reference/method/db.getLastError.txt (reStructuredText). Includes are inlined. -->

:orphan:

# db.getLastError()

Removed in MongoDB 5.1. 

Any code explicitly using `getLastError`,  `db.getLastError()`, or
`db.getLastErrorObj()` should instead use the CRUD API to issue the
write with the desired write concern.
Information about the success or failure of the write operation will be
provided directly by the driver as a return value.
