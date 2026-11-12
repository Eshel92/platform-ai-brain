<!-- Part 1 of 6 of reference/program/mongod.md (split because the page is big). -->

## Synopsis

`mongod` is the primary daemon process for the MongoDB
system. It handles data requests, manages data access, and performs
background management operations.

This document provides a complete overview of all command line options
for `mongod`. These command line options are primarily useful
for testing: In common operation, use the configuration file
options to control the behavior of
your database.

**See also:**

conf-file-command-line-mapping

**Note:**

MongoDB disables support for TLS 1.0
encryption on systems where TLS 1.1+ is available. 


## Compatibility

Deployments hosted in the following environments use `mongod`:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

MongoDB Atlas manages the `mongod` for all MongoDB Atlas deployments.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB


## Considerations

- .. include:: /includes/fact-mongod-mongos-ftdc-thread.rst


## Options

**Changed in version:** 5.2

- MongoDB removes the `--cpu` command-line option.

**Changed in version:** 5.0

- MongoDB removes the `--serviceExecutor` command-line option and the
  corresponding `net.serviceExecutor` configuration option.
