<!-- Converted from reference/method/cursor.explain.txt (reStructuredText). Includes are inlined. -->

# cursor.explain()

## Definition

**`cursor.explain(verbosity)`**

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

Provides information on the query plan for the
`db.collection.find()` method.

The `explain()` method has the following form:

```javascript
db.collection.find().explain()
```

The `explain()` method has the following parameter:

* - Parameter
  - Necessity
  - Type
  - Description

* - `verbose`
  - Optional
  - String
  - Determines the amount of information to include in the explain
    output. The possible verbosity modes are:

    - `allPlansExecution`
    - `executionStats`
    - `queryPlanner` (*Default*)

    For backwards compatibility with earlier versions of
    `explain()`, MongoDB interprets `true` as
    `allPlansExecution` and `false` as `queryPlanner`.

    For more information on the modes, see
    explain-cursor-method-verbosity.

The `explain()` method returns a document with the
query plan and, optionally, the execution statistics.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Required Access

To use `explain`, you must have permission to run the underlying
command.

## Behavior

(Include not available offline: includes/explain-ignores-cache-plan.rst)

### Verbosity Modes

The behavior of `cursor.explain()` and the amount of
information returned depend on the `verbosity` mode.

#### `queryPlanner` Mode

By default, `cursor.explain()` runs in `queryPlanner`
verbosity mode.

MongoDB runs the query optimizer to choose
the winning plan for the operation under evaluation. `cursor.explain()` returns
the `queryPlanner` information for the evaluated
method.

#### `executionStats` Mode

MongoDB runs the query optimizer to choose
the winning plan, executes the winning plan to completion, and returns
statistics describing the execution of the winning plan.

For write operations, `cursor.explain()` returns information about
the update or delete operations that *would* be performed, but does
*not* apply the modifications to the database.

`cursor.explain()` returns the `queryPlanner` and
`executionStats` information for the evaluated
method. However, `executionStats` does not
provide query execution information for the rejected plans.

MongoDB runs the query optimizer to choose
the winning plan, executes the winning plan to completion, and returns
statistics describing the execution of the winning plan.

For write operations, `cursor.explain()` returns information about
the update or delete operations that *would* be performed, but does
*not* apply the modifications to the database.

`cursor.explain()` returns the `queryPlanner` and
`executionStats` information for the evaluated
method. However, `executionStats` does not
provide query execution information for the rejected plans.

#### `allPlansExecution` Mode

MongoDB runs the query optimizer to choose the winning plan and executes the
winning plan to completion. In `"allPlansExecution"` mode, MongoDB
returns statistics describing the execution of the winning plan as well
as statistics for the other candidate plans captured during plan
selection.

For write operations, `cursor.explain()` returns information about
the update or delete operations that *would* be performed, but does
*not* apply the modifications to the database.

`cursor.explain()` returns the `queryPlanner` and
`executionStats` information for the evaluated
method. The `executionStats` includes the
*completed* query execution information for the *winning plan*.

If the query optimizer considered more than one plan,
`executionStats` information also includes the *partial*
execution information captured during the plan selection phase for both the winning and rejected
candidate plans.

MongoDB runs the query optimizer to choose the winning plan and executes the
winning plan to completion. In `"allPlansExecution"` mode, MongoDB
returns statistics describing the execution of the winning plan as well
as statistics for the other candidate plans captured during plan
selection.

For write operations, `cursor.explain()` returns information about
the update or delete operations that *would* be performed, but does
*not* apply the modifications to the database.

`cursor.explain()` returns the `queryPlanner` and
`executionStats` information for the evaluated
method. The `executionStats` includes the
*completed* query execution information for the *winning plan*.

If the query optimizer considered more than one plan,
`executionStats` information also includes the *partial*
execution information captured during the plan selection phase for both the winning and rejected
candidate plans.

### `db.collection.explain().find()`

`db.collection.explain().find()` is similar to
`db.collection.find().explain()` with the
following key differences:

- The `db.collection.explain().find()` construct allows for the
  additional chaining of query modifiers. For list of query modifiers,
  see db.collection.explain().find().help().

- The `db.collection.find().explain()` returns a cursor, which
  requires a call to `.next()`, or its alias `.finish()`, to return
  the `explain()` results.
  If run interactively in `mongosh`,
  `mongosh` automatically calls `.finish()` to return
  the results. For scripts, however, you must explicitly call
  `.next()`, or `.finish()`, to return the results. For list of
  cursor-related methods, see
  db.collection.explain().find().help().

See `db.collection.explain()` for more information.

## Output

`cursor.explain()` operations can return information regarding:

- `explainVersion`, the output format version (for example, `"1"`);

- `command`, which details the command being explained;

- queryPlanner, which details the plan selected by the
  query optimizer and lists the rejected
  plans;

- executionStats, which details the execution of the winning
  plan and the rejected plans;

- serverInfo, which provides information on the
  MongoDB instance; and

- `serverParameters`, which details internal parameters.

The verbosity mode (i.e. `queryPlanner`, `executionStats`,
`allPlansExecution`) determines whether the results include
executionStats and whether executionStats includes data
captured during plan selection.

Explain output is limited by the maximum `Nested Depth for BSON
Documents`, which is 100 levels of nesting. Explain output that exceeds
the limit is truncated.

For details on the output, see /reference/explain-results.

## Example

The following example runs `cursor.explain()` in
"executionStats" verbosity mode
to return the query planning and execution information for the
specified `db.collection.find()` operation:

```javascript
db.products.find(
   { quantity: { $gt: 50 }, category: "apparel" }
).explain("executionStats")
```
