<!-- Converted from core/server-side-javascript.txt (reStructuredText). Includes are inlined. -->

:orphan:

# Server-side JavaScript

## Overview

MongoDB provides the following commands, methods, and operator that
perform server-side execution of JavaScript code:

- `mapReduce` and the corresponding `mongosh`
  method `db.collection.mapReduce()`.  For more
  information, see /core/map-reduce.

- `$where` operator that evaluates a JavaScript expression or a
  function in order to query for documents.

- `$accumulator` and `$function` aggregation
  operations that allows users to define custom aggregation expressions.

You can also specify a JavaScript file to `mongosh` to
run on the server. For more information, see
running-js-scripts-in-mongo-on-mongod-host

**Note:** JavaScript in MongoDB

Although these methods use JavaScript, most
interactions with MongoDB do not use JavaScript but use an
`idiomatic driver` in the language
of the interacting application.

If you do not need to perform server-side execution of JavaScript code,
see disable-server-side-js.

**Note:**

If you are using SELinux, any MongoDB operation that requires
server-side JavaScript will
result in segfault errors. disable-server-side-js describes
how to disable execution of server-side JavaScript.

## Running `.js` files via a `mongosh` Instance on the Server

You can specify a JavaScript (`.js`) file to `mongosh`
to execute the file on the server. This is a good technique
for performing batch administrative work. When you run
`mongosh` on the server, connecting via the localhost
interface, the connection is fast with low latency.

## Disable Server-Side Execution of JavaScript

You can disable all server-side execution of JavaScript:

- For a `mongod` instance by passing the
  `--noscripting` option on the command
  line or setting `security.javascriptEnabled` to false in the
  configuration file.

- For a `mongos` instance by passing the 
  `--noscripting` option on the command 
  line or setting `security.javascriptEnabled` to false in the 
  configuration file. 

## Behavior

### Concurrency

Refer to the individual method or operator documentation for any
concurrency information. See also the concurrency table.

### Unsupported Array and String Functions

MongoDB 6.0 upgrades the internal JavaScript engine used for
server-side JavaScript,
`$accumulator`, `$function`, and `$where`
expressions and from MozJS-60 to MozJS-91. Several deprecated,
non-standard array and string functions that existed in MozJS-60 are
removed in MozJS-91.
