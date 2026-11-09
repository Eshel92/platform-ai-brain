<!-- Converted from reference/method/db.collection.explain.txt (reStructuredText). Includes are inlined. -->

# db.collection.explain()

This page documents a `mongosh` method. To see the equivalent
method in a MongoDB driver, see the corresponding page for your
programming language:

**`https://www.mongodb.com/docs/drivers/java/sync/current/fundamentals/aggregation/#explain-aggregation-example`**

**`https://www.mongodb.com/docs/languages/java/reactive-streams-driver/current/tutorials/aggregation/#explain-an-aggregation`**

**`https://mongodb.github.io/mongo-csharp-driver/2.29.0/api/MongoDB.Driver/MongoDB.Driver.Core.Operations.ExplainOperation.-ctor.html`**

**`https://mongoc.org/libmongoc/current/mongoc_collection_find.html#the-explain-command`**

**`https://www.mongodb.com/docs/languages/cpp/cpp-driver/upcoming/aggregation/#explain-an-aggregation`**

**`https://www.mongodb.com/docs/languages/python/pymongo-driver/current/aggregation/#explain-an-aggregation`**

**`https://mongodb.github.io/node-mongodb-native/6.9/classes/FindCursor.html#explain`**

**`https://www.mongodb.com/docs/drivers/go/current/fundamentals/run-command/#example`**

**`https://www.mongodb.com/docs/php-library/current/reference/method/MongoDBCollection-explain/`**

**`https://www.mongodb.com/docs/languages/scala/scala-driver/current/tutorials/aggregation/#explain-an-aggregation`**

**`https://mongodb.github.io/mongo-java-driver/5.2/apidocs/mongodb-driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-aggregate-flow/explain.html?query=suspend%20fun%20%3CR%20:%20Any%3E%20explain(resultClass:%20Class%3CR%3E,%20verbosity:%20ExplainVerbosity?%20=%20null):%20R`**

**`https://mongodb.github.io/mongo-java-driver/5.2/apidocs/mongodb-driver-kotlin-sync/mongodb-driver-kotlin-sync/com.mongodb.kotlin.client/-aggregate-iterable/explain.html?query=fun%20%3CR%20:%20Any%3E%20explain(resultClass:%20Class%3CR%3E,%20verbosity:%20ExplainVerbosity?%20=%20null):%20R`**

**`https://www.rubydoc.info/github/mongoid/mongoid/Mongoid%2FContextual%2FMongo:explain`**

**`https://www.mongodb.com/docs/drivers/rust/current/fundamentals/run-command/#command-example`**

## Description

**`db.collection.explain()`**

Returns information on the query plan for the following methods:

- `aggregate()`
- `count()`
- `find()`
- `remove()`
- `distinct()` 
- `findAndModify()`

Returns information on `mapReduce()`.

To use `db.collection.explain()`, append one of the
aforementioned methods to `db.collection.explain()`:

```none
db.collection.explain().<method(...)>
```

For example,

```javascript
db.products.explain().remove( { category: "apparel" }, { justOne: true } )
```

For more examples, see explain-method-examples. See also
db.collection.explain().help().

The `db.collection.explain()` method has the following
parameter:

* - Parameter

  - Type

  - Description

* - `verbosity`

  - string

  - Optional. Specifies the verbosity mode for the explain output. The mode affects
    the behavior of `explain()` and determines the amount of information
    to return. The possible modes are: 

    - `"queryPlanner"` (Default)
    - `"executionStats"`
    - `"allPlansExecution"`

    For backwards compatibility with earlier versions of
    `cursor.explain()`, MongoDB interprets `true` as
    `"allPlansExecution"` and `false` as `"queryPlanner"`.

    For more information on the modes, see
    explain-method-verbosity.
          
          
   

## Required Access

To use `explain`, you must have permission to run the underlying
command.

## Behavior

(Include not available offline: includes/explain-ignores-cache-plan.rst)

### Verbosity Modes

The behavior of `db.collection.explain()` and the amount of
information returned depend on the `verbosity` mode.

tabs:

  - id: queryplanner
    name: "queryPlanner Mode (Default)"
    content: |

      By default, `db.collection.explain()` runs in
      `queryPlanner` verbosity mode.

      MongoDB runs the query optimizer to choose
      the winning plan for the operation under evaluation. `db.collection.explain()` returns
      the `queryPlanner` information for the evaluated
      method.

  - id: executionstats
    name: "executionStats Mode"
    content: |

      MongoDB runs the query optimizer to choose
      the winning plan, executes the winning plan to completion, and returns
      statistics describing the execution of the winning plan.

      For write operations, `db.collection.explain()` returns information about
      the update or delete operations that *would* be performed, but does
      *not* apply the modifications to the database.

      `db.collection.explain()` returns the `queryPlanner` and
      `executionStats` information for the evaluated
      method. However, `executionStats` does not
      provide query execution information for the rejected plans.

  - id: allplans
    name: "allPlansExecution Mode"
    content: |

      MongoDB runs the query optimizer to choose the winning plan and executes the
      winning plan to completion. In `"allPlansExecution"` mode, MongoDB
      returns statistics describing the execution of the winning plan as well
      as statistics for the other candidate plans captured during plan
      selection.

      For write operations, `db.collection.explain()` returns information about
      the update or delete operations that *would* be performed, but does
      *not* apply the modifications to the database.

      `db.collection.explain()` returns the `queryPlanner` and
      `executionStats` information for the evaluated
      method. The `executionStats` includes the
      *completed* query execution information for the *winning plan*.

      If the query optimizer considered more than one plan,
      `executionStats` information also includes the *partial*
      execution information captured during the plan selection phase for both the winning and rejected
      candidate plans.

### Explain and Write Operations

For write operations, `db.collection.explain()` returns
information about the write operation that would be performed but does
not actually modify the database.

### Restrictions

You cannot run the `explain`
command/`db.collection.explain()` in `executionStats` mode
or `allPlansExecution` mode for an `aggregation pipeline` that contains the `$out` stage.
Instead, you can either:

- run the explain in `queryPlanner` mode or 

- run the explain in `executionStats` mode or `allPlansExecution`
  mode but without the `$out` stage to return information
  for the stages that precede the `$out` stage.

### `explain()` Mechanics

The `db.collection.explain()` method wraps the
`explain` command and is the preferred way to run
`explain`.

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

`db.collection.explain().aggregate()`
is equivalent to passing the 
explain option to
the `db.collection.aggregate()` method.

### `help()`

To see the list of operations supported by
`db.collection.explain()`, run:

```javascript
db.collection.explain().help()
```

`db.collection.explain().find()` 
returns a cursor, which allows for the chaining of query modifiers. 
To see the list of query modifiers supported by 
`db.collection.explain().find()` as 
well as cursor-related methods, run:

```javascript
db.collection.explain().find().help()
```

You can chain multiple modifiers to `db.collection.explain().find()`.
For an example, see explain-find-modifiers.

## Output

`db.collection.explain()` operations can return information regarding:

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

By default, `db.collection.explain()` runs in
`"queryPlanner"` verbosity mode.

The following example runs `db.collection.explain()` in
`"queryPlanner"` verbosity mode to return the query planning information
for the specified `count()` operation:

```javascript
db.products.explain().count( { quantity: { $gt: 50 } } )
```

### `executionStats`  Mode

The following example runs `db.collection.explain()` in
`"executionStats"` verbosity mode
to return the query planning and execution information for the
specified `find()` operation:

```javascript
db.products.explain("executionStats").find(
   { quantity: { $gt: 50 }, category: "apparel" }
)
```

### `allPlansExecution` Mode

The following example runs `db.collection.explain()` in
`"allPlansExecution"` verbosity mode.
`db.collection.explain()` returns the
`queryPlanner` and `executionStats` for
all considered plans for the specified
`findAndModify()` operation:

**Note:**

The execution of this explain will *not* modify data but runs the
query predicate of the update operation. For candidate plans,
MongoDB returns the execution information captured during the
plan selection phase.

```javascript
db.products.explain( "allPlansExecution" ).findAndModify( {
   query: { name: "Tom", state: "active", rating: { $gt: 10 } },
   sort: { rating: 1 },
   update: { $inc: { score: 1 } }
} )
```

### Explain `find()` with Modifiers

`db.collection.explain().find()` 
construct allows for the chaining of query modifiers. For example, the 
following operation provides information on the 
`find()` method with
`sort()` and `hint()` query modifiers.

```javascript
db.products.explain("executionStats").find(
   { quantity: { $gt: 50 }, category: "apparel" }
).sort( { quantity: -1 } ).hint( { category: 1, quantity: -1 } )
```

For a list of query modifiers available, run the following in
`mongosh`:

```javascript
db.collection.explain().find().help()
```

### Iterate the `explain().find()` Return Cursor

`db.collection.explain().find()` 
returns a cursor to the explain results. If run interactively in
`mongosh`, `mongosh` automatically 
iterates the cursor using the `.next()` method. For scripts, however, 
you must explicitly call `.next()` (or its alias `.finish()`) to 
return the results:

```javascript
var explainResult = db.products.explain().find( { category: "apparel" } ).next();
```
