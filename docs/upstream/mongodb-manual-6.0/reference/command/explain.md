<!-- Converted from reference/command/explain.txt (reStructuredText). Includes are inlined. -->

# explain

## Definition

**`explain`**

The `explain` command provides information on the
execution of the following commands: `aggregate`,
`count`, `distinct`, `find`,
`findAndModify`, `delete`,
`mapReduce`, and `update`.

   `cursor.explain()` helper methods

**Tip:**

In `mongosh`, this command can also be run through the `db.collection.explain()` and.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

(Include not available offline: includes/explain-ignores-cache-plan.rst)

## Compatibility

This command is available in deployments hosted in the following environments: 

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

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   {
     explain: <command>,
     verbosity: <string>,
     comment: <any>
   }
)
```

## Command Fields

The command takes the following fields:

* - Field
  - Type
  - Description

* - `explain`
  - document
  - A document specifying the command for which to return the execution
    information. For details on the specific command document, see `aggregate`, `count`,
    `distinct`, `find`,
    `findAndModify`, `delete`, `mapReduce`, and `update`.

* - `verbosity`
  - string
  - Optional. A string specifying the mode in which to run `explain`.
    The mode affects the behavior of `explain` and determines
    the amount of information to return.

    The possible modes are: 

    - `"queryPlanner"`
    - `"executionStats"`
    - `"allPlansExecution"` (Default)

    For more information on the modes, see explain behavior.

* - `comment`
  - any
  - .. include:: /includes/extracts/comment-content.rst

    If you specify `explain` without a `comment`, it inherits
    any `comment` in the command specified to `explain`.

## Behavior

### Verbosity Modes

The behavior of `explain` and the amount of information
returned depend on the `verbosity` mode.

tabs:

  - id: queryplanner
    name: "queryPlanner Mode"
    content: |

      MongoDB runs the query optimizer to choose
      the winning plan for the operation under evaluation. `explain` returns
      the `queryPlanner` information for the evaluated
      `<command>`.

  - id: executionstats
    name: "executionStats Mode"
    content: |

       MongoDB runs the query optimizer to choose
       the winning plan, executes the winning plan to completion, and returns
       statistics describing the execution of the winning plan.

       For write operations, `explain` returns information about
       the update or delete operations that *would* be performed, but does
       *not* apply the modifications to the database.

       `explain` returns the `queryPlanner` and
       `executionStats` information for the evaluated
       `<command>`. However, `executionStats` does not
       provide query execution information for the rejected plans.

  - id: allplans
    name: "allPlansExecution Mode (Default)"
    content: |

       By default, `explain` runs in
       `"allPlansExecution"` verbosity mode.

       MongoDB runs the query optimizer to choose the winning plan and executes the
       winning plan to completion. In `"allPlansExecution"` mode, MongoDB
       returns statistics describing the execution of the winning plan as well
       as statistics for the other candidate plans captured during plan
       selection.

       For write operations, `explain` returns information about
       the update or delete operations that *would* be performed, but does
       *not* apply the modifications to the database.

       `explain` returns the `queryPlanner` and
       `executionStats` information for the evaluated
       `<command>`. The `executionStats` includes the
       *completed* query execution information for the *winning plan*.

       If the query optimizer considered more than one plan,
       `executionStats` information also includes the *partial*
       execution information captured during the plan selection phase for both the winning and rejected
       candidate plans.

### Explain and Write Operations

For write operations, the `explain` command returns
information about the write operation that would be performed but does
not actually modify the database.

### Stable API

The Stable API V1 supports the following
verbosity modes for the `explain` command:

- allPlansExecution
- executionStats
- queryPlanner

**Warning:**

MongoDB does not guarantee any specific output format from the 
`explain` command, even when using the Stable API.

### Restrictions

You cannot run the `explain`
command/`db.collection.explain()` in `executionStats` mode
or `allPlansExecution` mode for an `aggregation pipeline` that contains the `$out` stage.
Instead, you can either:

- run the explain in `queryPlanner` mode or 

- run the explain in `executionStats` mode or `allPlansExecution`
  mode but without the `$out` stage to return information
  for the stages that precede the `$out` stage.

## Output

`explain` operations can return information regarding:

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

## Examples

### `queryPlanner` Mode

The following `explain` command runs in `"queryPlanner"`
verbosity mode to return the query planning information for a
`count` command:

```javascript
db.runCommand(
   {
     explain: { count: "products", query: { quantity: { $gt: 50 } } },
     verbosity: "queryPlanner"
   }
)
```

### `executionStats` Mode

The following `explain` operation runs in `"executionStats"`
verbosity mode to return the query planning and execution information
for a `count` command:

```javascript
db.runCommand(
   {
      explain: { count: "products", query: { quantity: { $gt: 50 } } },
      verbosity: "executionStats"
   }
)
```

### `allPlansExecution` Mode

By default, `explain` runs in `"allPlansExecution"` verbosity
mode. The following `explain` command returns the
`queryPlanner` and `executionStats` for
all considered plans for an `update` command:

**Note:**

The execution of this explain will *not* modify data but runs the
query predicate of the update operation. For candidate plans,
MongoDB returns the execution information captured during the
plan selection phase.

```javascript
db.runCommand(
   {
     explain: {
        update: "products",
        updates: [
           {
               q: { quantity: 1057, category: "apparel" },
               u: { $set: { reorder: true } }
           }
        ]
     }
   }
)
```
