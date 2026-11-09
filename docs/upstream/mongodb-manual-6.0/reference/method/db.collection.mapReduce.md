<!-- Converted from reference/method/db.collection.mapReduce.txt (reStructuredText). Includes are inlined. -->

# db.collection.mapReduce()

**Note:** Aggregation Pipeline as Alternative to Map-Reduce

Starting in MongoDB 5.0, map-reduce is
deprecated:

- Instead of map-reduce, you should use an
  aggregation pipeline. Aggregation
  pipelines provide better performance and usability than map-reduce.

- You can rewrite map-reduce operations using aggregation
  pipeline stages, such as
  `$group`, `$merge`, and others. 

- For map-reduce operations that require custom functionality, you can
  use the `$accumulator` and `$function` aggregation
  operators. You can use those
  operators to define custom aggregation expressions in JavaScript.

For examples of aggregation pipeline alternatives to map-reduce, see:

- /reference/map-reduce-to-aggregation-pipeline

- /tutorial/map-reduce-examples

**`db.collection.mapReduce(map,reduce, { <options> })`**

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `mapReduce` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

**Note:**

Views do not support map-reduce operations.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0, M2, M5, and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

**Note:**

MongoDB ignores the verbose option.

Starting in version 4.2, MongoDB deprecates:

- The map-reduce option to *create* a new sharded collection as well
  as the use of the sharded option for
  map-reduce. To output to a sharded collection, create the sharded
  collection first. MongoDB 4.2 also deprecates the replacement of
  an existing sharded collection.

`db.collection.mapReduce()` has the following syntax:

```javascript
db.collection.mapReduce(
                         <map>,
                         <reduce>,
                         {
                           out: <collection>,
                           query: <document>,
                           sort: <document>,
                           limit: <number>,
                           finalize: <function>,
                           scope: <document>,
                           jsMode: <boolean>,
                           verbose: <boolean>,
                           bypassDocumentValidation: <boolean>
                         }
                       )
```

`db.collection.mapReduce()` takes the following parameters:

| Parameter | Type | Description |
|---|---|---|
| `map` | JavaScript or String | A JavaScript function that associates or "maps" a `value` with a `key` and emits the `key` and value `pair`. You can specify the function as BSON type JavaScript (i.e. BSON type 13) or String (i.e. BSON type 2). See Requirements for the map Function for more information. |
| `reduce` | JavaScript or String | A JavaScript function that "reduces" to a single object all the `values` associated with a particular `key`. You can specify the function as BSON type JavaScript (i.e. BSON type 13) or String (i.e. BSON type 2). See Requirements for the reduce Function for more information. |
| `options` | document | A document that specifies additional parameters to `db.collection.mapReduce()`. |

       
       

The following table describes additional arguments that
`db.collection.mapReduce()` can accept.

* - Field

  - Type

  - Description

* - `out`

  - string or document

  - Specifies the location of the result of the map-reduce operation.
    You can output to a collection, output to a collection with an
    action, or output inline. You may output to a collection when
    performing map-reduce operations on the primary members of the set;
    on secondary members you may only use the `inline` output.

    See out Options for more information.

* - `query`

  - document

  - Specifies the selection criteria using query operators for determining the documents input to the
    `map` function.

* - `sort`

  - document

  - Sorts the *input* documents. This option is useful for
    optimization. For example, specify the sort key to be the same as
    the emit key so that there are fewer reduce operations. The sort key
    must be in an existing index for this collection.

* - `limit`

  - number

  - Specifies a maximum number of documents for the input into the
    `map` function.

* - `finalize`

  - Javascript or String

  - Optional. A JavaScript function that modifies the output after
    the `reduce` function. You can specify the function as BSON type
    JavaScript (i.e. BSON type 13)
    or String (i.e. BSON type 2).

    See Requirements for the finalize Function for more information.

* - `scope`

  - document

  - Specifies global variables that are accessible in the `map`,
    `reduce` and `finalize` functions.

* - `jsMode`

  - boolean

  - Specifies whether to convert intermediate data into BSON
    format between the execution of the `map` and `reduce`
    functions.

    Defaults to `false`.

    If `false`:

    - Internally, MongoDB converts the JavaScript objects emitted
      by the `map`
      function to BSON objects. These BSON
      objects are then converted back to JavaScript objects when
      calling the `reduce` function.

    - The map-reduce operation places the intermediate BSON objects
      in temporary, on-disk storage. This allows the map-reduce
      operation to execute over arbitrarily large data sets.

    If `true`:

    - Internally, the JavaScript objects emitted during `map`
      function remain as JavaScript objects. There is no need to
      convert the objects for the `reduce` function, which
      can result in faster execution.

    - You can only use `jsMode` for result sets with fewer than
      500,000 distinct `key` arguments to the mapper's `emit()`
      function.

* - `verbose`

  - boolean

  - Specifies whether to include the `timing` information in the
    result information. Set `verbose` to `true` to include
    the `timing` information.

    Defaults to `false`.

    This option is ignored. The result
    information always excludes the `timing` information.
    You can view timing information by running
    `db.collection.explain()` with
    `db.collection.mapReduce()` in the `"executionStats"`
    or `"allPlansExecution"` `verbosity` modes.

* - `collation`

  - document

  - Optional. 

    Specifies the collation  to use for the operation.

    Collation allows users to specify
    language-specific rules for string comparison, such as rules for
    lettercase and accent marks.

    The collation option has the following syntax:

    ```none
    collation: {
       locale: <string>,
       caseLevel: <boolean>,
       caseFirst: <string>,
       strength: <int>,
       numericOrdering: <boolean>,
       alternate: <string>,
       maxVariable: <string>,
       backwards: <boolean>
    }
    ```

    When specifying collation, the `locale` field is mandatory; all
    other collation fields are optional. For descriptions of the fields,
    see collation-document-fields.

    If the collation is unspecified but the collection has a
    default collation (see `db.createCollection()`), the
    operation uses the collation specified for the collection.

    If no collation is specified for the collection or for the
    operations, MongoDB uses the simple binary comparison used in prior
    versions for string comparisons.

    You cannot specify multiple collations for an operation. For
    example, you cannot specify different collations per field, or if
    performing a find with a sort, you cannot use one collation for the
    find and another for the sort.

* - `bypassDocumentValidation`

  - boolean

  - Optional. Enables `mapReduce` to bypass schema validation
    during the operation. This lets you insert documents that do not
    meet the validation requirements.

**Note:**

`map-reduce operations` and `$where`
operator expressions **cannot** access certain global functions or
properties, such as `db`, that are available in
`mongosh`.

The following JavaScript functions and properties **are available** to
`map-reduce operations` and `$where`
operator expressions:

| Available Properties | Available Functions |  |
|---|---|---|
| \| `args` \| `MaxKey` \| `MinKey` | \| `assert()` \| `BinData()` \| `DBPointer()` \| `DBRef()` \| `doassert()` \| `emit()` \| `gc()` \| `HexData()` \| `hex_md5()` \| `isNumber()` \| `isObject()` \| `ISODate()` \| `isString()` | \| `Map()` \| `MD5()` \| `NumberInt()` \| `NumberLong()` \| `ObjectId()` \| `print()` \| `printjson()` \| `printjsononeline()` \| `sleep()` \| `Timestamp()` \| `tojson()` \| `tojsononeline()` \| `tojsonObject()` \| `UUID()` \| `version()` |

## Requirements for the `map` Function

The `map` function is responsible for transforming each input document into
zero or more documents. It can access the variables defined in the `scope`
parameter, and has the following prototype:

```javascript
function() {
   ...
   emit(key, value);
}
```

The `map` function has the following requirements:

- In the `map` function, reference the current document as `this`
  within the function.

- The `map` function should *not* access the database for any reason.

- The `map` function should be pure, or have *no* impact outside of
  the function (i.e. side effects.)

- The `map` function may optionally call `emit(key,value)` any number of
  times to create an output document associating `key` with `value`.

The following `map` function will call `emit(key,value)` either
0 or 1 times depending on the value of the input document's
`status` field:

```javascript
function() {
    if (this.status == 'A')
        emit(this.cust_id, 1);
}
```

The following `map` function may call `emit(key,value)`
multiple times depending on the number of elements in the input
document's `items` field:

```javascript
function() {
    this.items.forEach(function(item){ emit(item.sku, 1); });
}
```

## Requirements for the `reduce` Function

The `reduce` function has the following prototype:

```javascript
function(key, values) {
   ...
   return result;
}
```

The `reduce` function exhibits the following behaviors:

- The `reduce` function should *not* access the database,
  even to perform read operations.

- The `reduce` function should *not* affect the outside
  system.

- MongoDB can invoke the `reduce` function more than once for the
  same key. In this case, the previous output from the `reduce`
  function for that key will become one of the input values to the next
  `reduce` function invocation for that key.

- The `reduce` function can access the variables defined
  in the `scope` parameter.

- The inputs to `reduce` must not be larger than half of MongoDB's
  maximum BSON document size. This
  requirement may be violated when large documents are returned and then
  joined together in subsequent `reduce` steps.

Because it is possible to invoke the `reduce` function
more than once for the same key, the following
properties need to be true:

- the *type* of the return object must be **identical**
  to the type of the `value` emitted by the `map`
  function.

- the `reduce` function must be *associative*. The following statement must be
  true:

  ```javascript
  reduce(key, [ C, reduce(key, [ A, B ]) ] ) == reduce( key, [ C, A, B ] )
  ```

- the `reduce` function must be *idempotent*. Ensure
  that the following statement is true:

  ```javascript
  reduce( key, [ reduce(key, valuesArray) ] ) == reduce( key, valuesArray )
  ```

- the `reduce` function should be *commutative*: that is, the order of the
  elements in the `valuesArray` should not affect the output of the
  `reduce` function, so that the following statement is true:

  ```javascript
  reduce( key, [ A, B ] ) == reduce( key, [ B, A ] )
  ```

## `out` Options

You can specify the following options for the `out` parameter:

### Output to a Collection

This option outputs to a new collection, and is not available on secondary
members of replica sets.

```javascript
out: <collectionName>
```

### Output to a Collection with an Action

**Note:**

Starting in version 4.2, MongoDB deprecates:

- The map-reduce option to *create* a new sharded collection as well
  as the use of the sharded option for
  map-reduce. To output to a sharded collection, create the sharded
  collection first. MongoDB 4.2 also deprecates the replacement of
  an existing sharded collection.

This option is only available when passing a collection that
already exists to `out`. It is not available 
on secondary members of replica sets.

```javascript
out: { <action>: <collectionName>
        [, db: <dbName>]
        [, sharded: <boolean> ] }
```

When you output to a collection with an action, the `out` has the
following parameters:

- `<action>`: Specify one of the following actions:

  - `replace`

    Replace the contents of the `<collectionName>` if the
    collection with the `<collectionName>` exists.

  - `merge`

    Merge the new result with the existing result if the
    output collection already exists. If an existing document
    has the same key as the new result, *overwrite* that
    existing document.

  - `reduce`

    Merge the new result with the existing result if the
    output collection already exists. If an existing document
    has the same key as the new result, apply the `reduce`
    function to both the new and the existing documents and
    overwrite the existing document with the result.

- `db`:

  Optional. The name of the database that you want the map-reduce
  operation to write its output. By default this will be the same
  database as the input collection.

### Output Inline

Perform the map-reduce operation in memory and return the result. This
option is the only available option for `out` on secondary members of
replica sets.

```javascript
out: { inline: 1 }
```

The result must fit within the maximum size of a BSON document.

## Requirements for the `finalize` Function

The `finalize` function has the following prototype:

```javascript
function(key, reducedValue) {
   ...
   return modifiedObject;
}
```

The `finalize` function receives as its arguments a `key`
value and the `reducedValue` from the `reduce` function. Be
aware that:

- The `finalize` function should *not* access the database for
  any reason.

- The `finalize` function should be pure, or have *no* impact
  outside of the function (i.e. side effects.)

- The `finalize` function can access the variables defined in
  the `scope` parameter.

## Requirements for the `map` Function

The `map` function is responsible for transforming each input document into
zero or more documents. It can access the variables defined in the `scope`
parameter, and has the following prototype:

```javascript
function() {
   ...
   emit(key, value);
}
```

The `map` function has the following requirements:

- In the `map` function, reference the current document as `this`
  within the function.

- The `map` function should *not* access the database for any reason.

- The `map` function should be pure, or have *no* impact outside of
  the function (i.e. side effects.)

- The `map` function may optionally call `emit(key,value)` any number of
  times to create an output document associating `key` with `value`.

The following `map` function will call `emit(key,value)` either
0 or 1 times depending on the value of the input document's
`status` field:

```javascript
function() {
    if (this.status == 'A')
        emit(this.cust_id, 1);
}
```

The following `map` function may call `emit(key,value)`
multiple times depending on the number of elements in the input
document's `items` field:

```javascript
function() {
    this.items.forEach(function(item){ emit(item.sku, 1); });
}
```

## Requirements for the `reduce` Function

The `reduce` function has the following prototype:

```javascript
function(key, values) {
   ...
   return result;
}
```

The `reduce` function exhibits the following behaviors:

- The `reduce` function should *not* access the database,
  even to perform read operations.

- The `reduce` function should *not* affect the outside
  system.

- MongoDB can invoke the `reduce` function more than once for the
  same key. In this case, the previous output from the `reduce`
  function for that key will become one of the input values to the next
  `reduce` function invocation for that key.

- The `reduce` function can access the variables defined
  in the `scope` parameter.

- The inputs to `reduce` must not be larger than half of MongoDB's
  maximum BSON document size. This
  requirement may be violated when large documents are returned and then
  joined together in subsequent `reduce` steps.

Because it is possible to invoke the `reduce` function
more than once for the same key, the following
properties need to be true:

- the *type* of the return object must be **identical**
  to the type of the `value` emitted by the `map`
  function.

- the `reduce` function must be *associative*. The following statement must be
  true:

  ```javascript
  reduce(key, [ C, reduce(key, [ A, B ]) ] ) == reduce( key, [ C, A, B ] )
  ```

- the `reduce` function must be *idempotent*. Ensure
  that the following statement is true:

  ```javascript
  reduce( key, [ reduce(key, valuesArray) ] ) == reduce( key, valuesArray )
  ```

- the `reduce` function should be *commutative*: that is, the order of the
  elements in the `valuesArray` should not affect the output of the
  `reduce` function, so that the following statement is true:

  ```javascript
  reduce( key, [ A, B ] ) == reduce( key, [ B, A ] )
  ```

## `out` Options

You can specify the following options for the `out` parameter:

### Output to a Collection

This option outputs to a new collection, and is not available on secondary
members of replica sets.

```javascript
out: <collectionName>
```

### Output to a Collection with an Action

**Note:**

Starting in version 4.2, MongoDB deprecates:

- The map-reduce option to *create* a new sharded collection as well
  as the use of the sharded option for
  map-reduce. To output to a sharded collection, create the sharded
  collection first. MongoDB 4.2 also deprecates the replacement of
  an existing sharded collection.

This option is only available when passing a collection that
already exists to `out`. It is not available 
on secondary members of replica sets.

```javascript
out: { <action>: <collectionName>
        [, db: <dbName>]
        [, sharded: <boolean> ] }
```

When you output to a collection with an action, the `out` has the
following parameters:

- `<action>`: Specify one of the following actions:

  - `replace`

    Replace the contents of the `<collectionName>` if the
    collection with the `<collectionName>` exists.

  - `merge`

    Merge the new result with the existing result if the
    output collection already exists. If an existing document
    has the same key as the new result, *overwrite* that
    existing document.

  - `reduce`

    Merge the new result with the existing result if the
    output collection already exists. If an existing document
    has the same key as the new result, apply the `reduce`
    function to both the new and the existing documents and
    overwrite the existing document with the result.

- `db`:

  Optional. The name of the database that you want the map-reduce
  operation to write its output. By default this will be the same
  database as the input collection.

### Output Inline

Perform the map-reduce operation in memory and return the result. This
option is the only available option for `out` on secondary members of
replica sets.

```javascript
out: { inline: 1 }
```

The result must fit within the maximum size of a BSON document.

## Requirements for the `finalize` Function

The `finalize` function has the following prototype:

```javascript
function(key, reducedValue) {
   ...
   return modifiedObject;
}
```

The `finalize` function receives as its arguments a `key`
value and the `reducedValue` from the `reduce` function. Be
aware that:

- The `finalize` function should *not* access the database for
  any reason.

- The `finalize` function should be pure, or have *no* impact
  outside of the function (i.e. side effects.)

- The `finalize` function can access the variables defined in
  the `scope` parameter.

## Requirements for the `map` Function

The `map` function is responsible for transforming each input document into
zero or more documents. It can access the variables defined in the `scope`
parameter, and has the following prototype:

```javascript
function() {
   ...
   emit(key, value);
}
```

The `map` function has the following requirements:

- In the `map` function, reference the current document as `this`
  within the function.

- The `map` function should *not* access the database for any reason.

- The `map` function should be pure, or have *no* impact outside of
  the function (i.e. side effects.)

- The `map` function may optionally call `emit(key,value)` any number of
  times to create an output document associating `key` with `value`.

The following `map` function will call `emit(key,value)` either
0 or 1 times depending on the value of the input document's
`status` field:

```javascript
function() {
    if (this.status == 'A')
        emit(this.cust_id, 1);
}
```

The following `map` function may call `emit(key,value)`
multiple times depending on the number of elements in the input
document's `items` field:

```javascript
function() {
    this.items.forEach(function(item){ emit(item.sku, 1); });
}
```

## Requirements for the `reduce` Function

The `reduce` function has the following prototype:

```javascript
function(key, values) {
   ...
   return result;
}
```

The `reduce` function exhibits the following behaviors:

- The `reduce` function should *not* access the database,
  even to perform read operations.

- The `reduce` function should *not* affect the outside
  system.

- MongoDB can invoke the `reduce` function more than once for the
  same key. In this case, the previous output from the `reduce`
  function for that key will become one of the input values to the next
  `reduce` function invocation for that key.

- The `reduce` function can access the variables defined
  in the `scope` parameter.

- The inputs to `reduce` must not be larger than half of MongoDB's
  maximum BSON document size. This
  requirement may be violated when large documents are returned and then
  joined together in subsequent `reduce` steps.

Because it is possible to invoke the `reduce` function
more than once for the same key, the following
properties need to be true:

- the *type* of the return object must be **identical**
  to the type of the `value` emitted by the `map`
  function.

- the `reduce` function must be *associative*. The following statement must be
  true:

  ```javascript
  reduce(key, [ C, reduce(key, [ A, B ]) ] ) == reduce( key, [ C, A, B ] )
  ```

- the `reduce` function must be *idempotent*. Ensure
  that the following statement is true:

  ```javascript
  reduce( key, [ reduce(key, valuesArray) ] ) == reduce( key, valuesArray )
  ```

- the `reduce` function should be *commutative*: that is, the order of the
  elements in the `valuesArray` should not affect the output of the
  `reduce` function, so that the following statement is true:

  ```javascript
  reduce( key, [ A, B ] ) == reduce( key, [ B, A ] )
  ```

## `out` Options

You can specify the following options for the `out` parameter:

### Output to a Collection

This option outputs to a new collection, and is not available on secondary
members of replica sets.

```javascript
out: <collectionName>
```

### Output to a Collection with an Action

**Note:**

Starting in version 4.2, MongoDB deprecates:

- The map-reduce option to *create* a new sharded collection as well
  as the use of the sharded option for
  map-reduce. To output to a sharded collection, create the sharded
  collection first. MongoDB 4.2 also deprecates the replacement of
  an existing sharded collection.

This option is only available when passing a collection that
already exists to `out`. It is not available 
on secondary members of replica sets.

```javascript
out: { <action>: <collectionName>
        [, db: <dbName>]
        [, sharded: <boolean> ] }
```

When you output to a collection with an action, the `out` has the
following parameters:

- `<action>`: Specify one of the following actions:

  - `replace`

    Replace the contents of the `<collectionName>` if the
    collection with the `<collectionName>` exists.

  - `merge`

    Merge the new result with the existing result if the
    output collection already exists. If an existing document
    has the same key as the new result, *overwrite* that
    existing document.

  - `reduce`

    Merge the new result with the existing result if the
    output collection already exists. If an existing document
    has the same key as the new result, apply the `reduce`
    function to both the new and the existing documents and
    overwrite the existing document with the result.

- `db`:

  Optional. The name of the database that you want the map-reduce
  operation to write its output. By default this will be the same
  database as the input collection.

### Output Inline

Perform the map-reduce operation in memory and return the result. This
option is the only available option for `out` on secondary members of
replica sets.

```javascript
out: { inline: 1 }
```

The result must fit within the maximum size of a BSON document.

## Requirements for the `finalize` Function

The `finalize` function has the following prototype:

```javascript
function(key, reducedValue) {
   ...
   return modifiedObject;
}
```

The `finalize` function receives as its arguments a `key`
value and the `reducedValue` from the `reduce` function. Be
aware that:

- The `finalize` function should *not* access the database for
  any reason.

- The `finalize` function should be pure, or have *no* impact
  outside of the function (i.e. side effects.)

- The `finalize` function can access the variables defined in
  the `scope` parameter.

## Requirements for the `map` Function

The `map` function is responsible for transforming each input document into
zero or more documents. It can access the variables defined in the `scope`
parameter, and has the following prototype:

```javascript
function() {
   ...
   emit(key, value);
}
```

The `map` function has the following requirements:

- In the `map` function, reference the current document as `this`
  within the function.

- The `map` function should *not* access the database for any reason.

- The `map` function should be pure, or have *no* impact outside of
  the function (i.e. side effects.)

- The `map` function may optionally call `emit(key,value)` any number of
  times to create an output document associating `key` with `value`.

The following `map` function will call `emit(key,value)` either
0 or 1 times depending on the value of the input document's
`status` field:

```javascript
function() {
    if (this.status == 'A')
        emit(this.cust_id, 1);
}
```

The following `map` function may call `emit(key,value)`
multiple times depending on the number of elements in the input
document's `items` field:

```javascript
function() {
    this.items.forEach(function(item){ emit(item.sku, 1); });
}
```

## Requirements for the `reduce` Function

The `reduce` function has the following prototype:

```javascript
function(key, values) {
   ...
   return result;
}
```

The `reduce` function exhibits the following behaviors:

- The `reduce` function should *not* access the database,
  even to perform read operations.

- The `reduce` function should *not* affect the outside
  system.

- MongoDB can invoke the `reduce` function more than once for the
  same key. In this case, the previous output from the `reduce`
  function for that key will become one of the input values to the next
  `reduce` function invocation for that key.

- The `reduce` function can access the variables defined
  in the `scope` parameter.

- The inputs to `reduce` must not be larger than half of MongoDB's
  maximum BSON document size. This
  requirement may be violated when large documents are returned and then
  joined together in subsequent `reduce` steps.

Because it is possible to invoke the `reduce` function
more than once for the same key, the following
properties need to be true:

- the *type* of the return object must be **identical**
  to the type of the `value` emitted by the `map`
  function.

- the `reduce` function must be *associative*. The following statement must be
  true:

  ```javascript
  reduce(key, [ C, reduce(key, [ A, B ]) ] ) == reduce( key, [ C, A, B ] )
  ```

- the `reduce` function must be *idempotent*. Ensure
  that the following statement is true:

  ```javascript
  reduce( key, [ reduce(key, valuesArray) ] ) == reduce( key, valuesArray )
  ```

- the `reduce` function should be *commutative*: that is, the order of the
  elements in the `valuesArray` should not affect the output of the
  `reduce` function, so that the following statement is true:

  ```javascript
  reduce( key, [ A, B ] ) == reduce( key, [ B, A ] )
  ```

## `out` Options

You can specify the following options for the `out` parameter:

### Output to a Collection

This option outputs to a new collection, and is not available on secondary
members of replica sets.

```javascript
out: <collectionName>
```

### Output to a Collection with an Action

**Note:**

Starting in version 4.2, MongoDB deprecates:

- The map-reduce option to *create* a new sharded collection as well
  as the use of the sharded option for
  map-reduce. To output to a sharded collection, create the sharded
  collection first. MongoDB 4.2 also deprecates the replacement of
  an existing sharded collection.

This option is only available when passing a collection that
already exists to `out`. It is not available 
on secondary members of replica sets.

```javascript
out: { <action>: <collectionName>
        [, db: <dbName>]
        [, sharded: <boolean> ] }
```

When you output to a collection with an action, the `out` has the
following parameters:

- `<action>`: Specify one of the following actions:

  - `replace`

    Replace the contents of the `<collectionName>` if the
    collection with the `<collectionName>` exists.

  - `merge`

    Merge the new result with the existing result if the
    output collection already exists. If an existing document
    has the same key as the new result, *overwrite* that
    existing document.

  - `reduce`

    Merge the new result with the existing result if the
    output collection already exists. If an existing document
    has the same key as the new result, apply the `reduce`
    function to both the new and the existing documents and
    overwrite the existing document with the result.

- `db`:

  Optional. The name of the database that you want the map-reduce
  operation to write its output. By default this will be the same
  database as the input collection.

### Output Inline

Perform the map-reduce operation in memory and return the result. This
option is the only available option for `out` on secondary members of
replica sets.

```javascript
out: { inline: 1 }
```

The result must fit within the maximum size of a BSON document.

## Requirements for the `finalize` Function

The `finalize` function has the following prototype:

```javascript
function(key, reducedValue) {
   ...
   return modifiedObject;
}
```

The `finalize` function receives as its arguments a `key`
value and the `reducedValue` from the `reduce` function. Be
aware that:

- The `finalize` function should *not* access the database for
  any reason.

- The `finalize` function should be pure, or have *no* impact
  outside of the function (i.e. side effects.)

- The `finalize` function can access the variables defined in
  the `scope` parameter.

## Map-Reduce Examples

The examples in this section include aggregation pipeline alternatives
without custom aggregation expressions. For alternatives that use custom
expressions, see Map-Reduce to Aggregation Pipeline Translation
Examples.

Create a sample collection `orders` with these documents:

```javascript
db.orders.insertMany([
   { _id: 1, cust_id: "Ant O. Knee", ord_date: new Date("2020-03-01"), price: 25, items: [ { sku: "oranges", qty: 5, price: 2.5 }, { sku: "apples", qty: 5, price: 2.5 } ], status: "A" },
   { _id: 2, cust_id: "Ant O. Knee", ord_date: new Date("2020-03-08"), price: 70, items: [ { sku: "oranges", qty: 8, price: 2.5 }, { sku: "chocolates", qty: 5, price: 10 } ], status: "A" },
   { _id: 3, cust_id: "Busby Bee", ord_date: new Date("2020-03-08"), price: 50, items: [ { sku: "oranges", qty: 10, price: 2.5 }, { sku: "pears", qty: 10, price: 2.5 } ], status: "A" },
   { _id: 4, cust_id: "Busby Bee", ord_date: new Date("2020-03-18"), price: 25, items: [ { sku: "oranges", qty: 10, price: 2.5 } ], status: "A" },
   { _id: 5, cust_id: "Busby Bee", ord_date: new Date("2020-03-19"), price: 50, items: [ { sku: "chocolates", qty: 5, price: 10 } ], status: "A"},
   { _id: 6, cust_id: "Cam Elot", ord_date: new Date("2020-03-19"), price: 35, items: [ { sku: "carrots", qty: 10, price: 1.0 }, { sku: "apples", qty: 10, price: 2.5 } ], status: "A" },
   { _id: 7, cust_id: "Cam Elot", ord_date: new Date("2020-03-20"), price: 25, items: [ { sku: "oranges", qty: 10, price: 2.5 } ], status: "A" },
   { _id: 8, cust_id: "Don Quis", ord_date: new Date("2020-03-20"), price: 75, items: [ { sku: "chocolates", qty: 5, price: 10 }, { sku: "apples", qty: 10, price: 2.5 } ], status: "A" },
   { _id: 9, cust_id: "Don Quis", ord_date: new Date("2020-03-20"), price: 55, items: [ { sku: "carrots", qty: 5, price: 1.0 }, { sku: "apples", qty: 10, price: 2.5 }, { sku: "oranges", qty: 10, price: 2.5 } ], status: "A" },
   { _id: 10, cust_id: "Don Quis", ord_date: new Date("2020-03-23"), price: 25, items: [ { sku: "oranges", qty: 10, price: 2.5 } ], status: "A" }
])
```

### Return the Total Price Per Customer

Perform the map-reduce operation on the `orders` collection to group
by the `cust_id`, and calculate the sum of the `price` for each
`cust_id`:

#. Define the map function to process each input document:

   - In the function, `this` refers to the document that the
     map-reduce operation is processing.

   - The function maps the `price` to the `cust_id` for each
     document and emits the `cust_id` and `price`.

   ```javascript
   var mapFunction1 = function() {
      emit(this.cust_id, this.price);
   };
   ```

#. Define the corresponding reduce function with two arguments
   `keyCustId` and `valuesPrices`:

   - The `valuesPrices` is an array whose elements are the `price`
     values emitted by the map function and grouped by `keyCustId`.

   - The function reduces the `valuesPrice` array to the
     sum of its elements.

   ```javascript
   var reduceFunction1 = function(keyCustId, valuesPrices) {
      return Array.sum(valuesPrices);
   };
   ```

#. Perform map-reduce on all documents in the `orders` collection
   using the `mapFunction1` map function and the `reduceFunction1`
   reduce function:

   ```javascript
   db.orders.mapReduce(
      mapFunction1,
      reduceFunction1,
      { out: "map_reduce_example" }
   )
   ```

   This operation outputs the results to a collection named
   `map_reduce_example`. If the `map_reduce_example` collection
   already exists, the operation will replace the contents with the
   results of this map-reduce operation.

#. Query the `map_reduce_example` collection to verify the results:

   ```javascript
   db.map_reduce_example.find().sort( { _id: 1 } )
   ```

   The operation returns these documents:

   ```javascript
   { "_id" : "Ant O. Knee", "value" : 95 }
   { "_id" : "Busby Bee", "value" : 125 }
   { "_id" : "Cam Elot", "value" : 60 }
   { "_id" : "Don Quis", "value" : 155 }
   ```

#### Aggregation Alternative

Using the available aggregation pipeline operators, you can rewrite
the map-reduce operation without defining custom functions:

```javascript
db.orders.aggregate([
   { $group: { _id: "$cust_id", value: { $sum: "$price" } } },
   { $out: "agg_alternative_1" }
])
```

#. The `$group` stage groups by the `cust_id` and
   calculates the `value` field (See also `$sum`). The
   `value` field contains the total `price` for each `cust_id`.

   The stage output the following documents to the next stage:

   ```javascript
   { "_id" : "Don Quis", "value" : 155 }
   { "_id" : "Ant O. Knee", "value" : 95 }
   { "_id" : "Cam Elot", "value" : 60 }
   { "_id" : "Busby Bee", "value" : 125 }
   ```

#. Then, the `$out` writes the output to the collection
   `agg_alternative_1`. Alternatively, you could use
   `$merge` instead of `$out`.

#. Query the `agg_alternative_1` collection to verify the results:

   ```javascript
   db.agg_alternative_1.find().sort( { _id: 1 } )
   ```

   The operation returns the following documents:

   ```javascript
   { "_id" : "Ant O. Knee", "value" : 95 }
   { "_id" : "Busby Bee", "value" : 125 }
   { "_id" : "Cam Elot", "value" : 60 }
   { "_id" : "Don Quis", "value" : 155 }
   ```

**See also:**

For an alternative that uses custom aggregation expressions, see
Map-Reduce to Aggregation Pipeline Translation Examples.

### Calculate Order and Total Quantity with Average Quantity Per Item

In the following example, you will see a map-reduce operation on the
`orders` collection for all documents that have an `ord_date` value
greater than or equal to `2020-03-01`.

The operation in the example:

#. Groups by the `item.sku` field, and calculates the number of orders
   and the total quantity ordered for each `sku`.

#. Calculates the average quantity per order for each `sku` value and
   merges the results into the output collection.

When merging results, if an existing document has the same key as the
new result, the operation overwrites the existing document. If there is
no existing document with the same key, the operation inserts the
document.

Example steps:

#. Define the map function to process each input document:

   - In the function, `this` refers to the document that the
     map-reduce operation is processing.

   - For each item, the function associates the `sku` with a new
     object `value` that contains the `count` of `1` and the item
     `qty` for the order and emits the `sku` (stored in the `key`)
     and the `value`.

   ```javascript
    var mapFunction2 = function() {
       for (var idx = 0; idx < this.items.length; idx++) {
          var key = this.items[idx].sku;
          var value = { count: 1, qty: this.items[idx].qty };

          emit(key, value);
       }
   };
   ```

#. Define the corresponding reduce function with two arguments
   `keySKU` and `countObjVals`:

   - `countObjVals` is an array whose elements are the objects
     mapped to the grouped `keySKU` values passed by map
     function to the reducer function.

   - The function reduces the `countObjVals` array to a single
     object `reducedValue` that contains the `count` and the
     `qty` fields.

   - In `reducedVal`, the `count` field contains the sum of the
     `count` fields from the individual array elements, and the
     `qty` field contains the sum of the `qty` fields from the
     individual array elements.

   ```javascript
   var reduceFunction2 = function(keySKU, countObjVals) {
      reducedVal = { count: 0, qty: 0 };

      for (var idx = 0; idx < countObjVals.length; idx++) {
          reducedVal.count += countObjVals[idx].count;
          reducedVal.qty += countObjVals[idx].qty;
      }

      return reducedVal;
   };
   ```

#. Define a finalize function with two arguments `key` and
   `reducedVal`. The function modifies the `reducedVal` object
   to add a computed field named `avg` and returns the modified
   object:

   ```javascript
   var finalizeFunction2 = function (key, reducedVal) {
     reducedVal.avg = reducedVal.qty/reducedVal.count;
     return reducedVal;
   };
   ```

#. Perform the map-reduce operation on the `orders` collection using
   the `mapFunction2`, `reduceFunction2`, and
   `finalizeFunction2` functions:

   ```javascript
   db.orders.mapReduce( 
      mapFunction2,
      reduceFunction2,
      {
        out: { merge: "map_reduce_example2" },
        query: { ord_date: { $gte: new Date("2020-03-01") } },
        finalize: finalizeFunction2
      }
    );
   ```

   This operation uses the `query` field to select only those
   documents with `ord_date` greater than or equal to ``new
   Date("2020-03-01")``. Then it outputs the results to a collection
   `map_reduce_example2`. 

   If the `map_reduce_example2` collection already exists, the
   operation will merge the existing contents with the results of this
   map-reduce operation. That is, if an existing document has the same
   key as the new result, the operation overwrites the existing
   document. If there is no existing document with the same key, the
   operation inserts the document.

#. Query the `map_reduce_example2` collection to verify the results:

   ```javascript
   db.map_reduce_example2.find().sort( { _id: 1 } )
   ```

   The operation returns these documents:

   ```javascript
   { "_id" : "apples", "value" : { "count" : 4, "qty" : 35, "avg" : 8.75 } }
   { "_id" : "carrots", "value" : { "count" : 2, "qty" : 15, "avg" : 7.5 } }
   { "_id" : "chocolates", "value" : { "count" : 3, "qty" : 15, "avg" : 5 } }
   { "_id" : "oranges", "value" : { "count" : 7, "qty" : 63, "avg" : 9 } }
   { "_id" : "pears", "value" : { "count" : 1, "qty" : 10, "avg" : 10 } }
   ```

#### Aggregation Alternative

Using the available aggregation pipeline operators, you can rewrite
the map-reduce operation without defining custom functions:

```javascript
db.orders.aggregate( [ 
   { $match: { ord_date: { $gte: new Date("2020-03-01") } } },
   { $unwind: "$items" }, 
   { $group: { _id: "$items.sku", qty: { $sum: "$items.qty" }, orders_ids: { $addToSet: "$_id" } }  },
   { $project: { value: { count: { $size: "$orders_ids" }, qty: "$qty", avg: { $divide: [ "$qty", { $size: "$orders_ids" } ] } } } },
   { $merge: { into: "agg_alternative_3", on: "_id", whenMatched: "replace",  whenNotMatched: "insert" } }
] )
```

#. The `$match` stage selects only those
   documents with `ord_date` greater than or equal to ``new
   Date("2020-03-01")``.

#. The `$unwind` stage breaks down the document by
   the `items` array field to output a document for each array
   element. For example:

   ```javascript
   { "_id" : 1, "cust_id" : "Ant O. Knee", "ord_date" : ISODate("2020-03-01T00:00:00Z"), "price" : 25, "items" : { "sku" : "oranges", "qty" : 5, "price" : 2.5 }, "status" : "A" }
   { "_id" : 1, "cust_id" : "Ant O. Knee", "ord_date" : ISODate("2020-03-01T00:00:00Z"), "price" : 25, "items" : { "sku" : "apples", "qty" : 5, "price" : 2.5 }, "status" : "A" }
   { "_id" : 2, "cust_id" : "Ant O. Knee", "ord_date" : ISODate("2020-03-08T00:00:00Z"), "price" : 70, "items" : { "sku" : "oranges", "qty" : 8, "price" : 2.5 }, "status" : "A" }
   { "_id" : 2, "cust_id" : "Ant O. Knee", "ord_date" : ISODate("2020-03-08T00:00:00Z"), "price" : 70, "items" : { "sku" : "chocolates", "qty" : 5, "price" : 10 }, "status" : "A" }
   { "_id" : 3, "cust_id" : "Busby Bee", "ord_date" : ISODate("2020-03-08T00:00:00Z"), "price" : 50, "items" : { "sku" : "oranges", "qty" : 10, "price" : 2.5 }, "status" : "A" }
   { "_id" : 3, "cust_id" : "Busby Bee", "ord_date" : ISODate("2020-03-08T00:00:00Z"), "price" : 50, "items" : { "sku" : "pears", "qty" : 10, "price" : 2.5 }, "status" : "A" }
   { "_id" : 4, "cust_id" : "Busby Bee", "ord_date" : ISODate("2020-03-18T00:00:00Z"), "price" : 25, "items" : { "sku" : "oranges", "qty" : 10, "price" : 2.5 }, "status" : "A" }
   { "_id" : 5, "cust_id" : "Busby Bee", "ord_date" : ISODate("2020-03-19T00:00:00Z"), "price" : 50, "items" : { "sku" : "chocolates", "qty" : 5, "price" : 10 }, "status" : "A" }
   ...
   ```

#. The `$group` stage groups by the `items.sku`, calculating for each sku:

   - The `qty` field. The `qty` field contains the
      total `qty` ordered per each `items.sku` (See `$sum`).

   - The `orders_ids` array. The `orders_ids` field contains an
      array of distinct order `_id`'s for the `items.sku` (See
      `$addToSet`).

   ```javascript
   { "_id" : "chocolates", "qty" : 15, "orders_ids" : [ 2, 5, 8 ] }
   { "_id" : "oranges", "qty" : 63, "orders_ids" : [ 4, 7, 3, 2, 9, 1, 10 ] }
   { "_id" : "carrots", "qty" : 15, "orders_ids" : [ 6, 9 ] }
   { "_id" : "apples", "qty" : 35, "orders_ids" : [ 9, 8, 1, 6 ] }
   { "_id" : "pears", "qty" : 10, "orders_ids" : [ 3 ] }
   ```

#. The `$project` stage reshapes the output document to
   mirror the map-reduce's output to have two fields `_id` and
   `value`. The `$project` sets:

#. The `$unwind` stage breaks down the document by
   the `items` array field to output a document for each array
   element. For example:

   ```javascript
   { "_id" : 1, "cust_id" : "Ant O. Knee", "ord_date" : ISODate("2020-03-01T00:00:00Z"), "price" : 25, "items" : { "sku" : "oranges", "qty" : 5, "price" : 2.5 }, "status" : "A" }
   { "_id" : 1, "cust_id" : "Ant O. Knee", "ord_date" : ISODate("2020-03-01T00:00:00Z"), "price" : 25, "items" : { "sku" : "apples", "qty" : 5, "price" : 2.5 }, "status" : "A" }
   { "_id" : 2, "cust_id" : "Ant O. Knee", "ord_date" : ISODate("2020-03-08T00:00:00Z"), "price" : 70, "items" : { "sku" : "oranges", "qty" : 8, "price" : 2.5 }, "status" : "A" }
   { "_id" : 2, "cust_id" : "Ant O. Knee", "ord_date" : ISODate("2020-03-08T00:00:00Z"), "price" : 70, "items" : { "sku" : "chocolates", "qty" : 5, "price" : 10 }, "status" : "A" }
   { "_id" : 3, "cust_id" : "Busby Bee", "ord_date" : ISODate("2020-03-08T00:00:00Z"), "price" : 50, "items" : { "sku" : "oranges", "qty" : 10, "price" : 2.5 }, "status" : "A" }
   { "_id" : 3, "cust_id" : "Busby Bee", "ord_date" : ISODate("2020-03-08T00:00:00Z"), "price" : 50, "items" : { "sku" : "pears", "qty" : 10, "price" : 2.5 }, "status" : "A" }
   { "_id" : 4, "cust_id" : "Busby Bee", "ord_date" : ISODate("2020-03-18T00:00:00Z"), "price" : 25, "items" : { "sku" : "oranges", "qty" : 10, "price" : 2.5 }, "status" : "A" }
   { "_id" : 5, "cust_id" : "Busby Bee", "ord_date" : ISODate("2020-03-19T00:00:00Z"), "price" : 50, "items" : { "sku" : "chocolates", "qty" : 5, "price" : 10 }, "status" : "A" }
   ...
   ```

#. The `$group` stage groups by the `items.sku`, calculating for each sku:

   - The `qty` field. The `qty` field contains the
     total `qty` ordered per each `items.sku` using
     `$sum`.

   - The `orders_ids` array. The `orders_ids` field contains an
     array of distinct order `_id`'s for the `items.sku` using
     `$addToSet`.

   ```javascript
   { "_id" : "chocolates", "qty" : 15, "orders_ids" : [ 2, 5, 8 ] }
   { "_id" : "oranges", "qty" : 63, "orders_ids" : [ 4, 7, 3, 2, 9, 1, 10 ] }
   { "_id" : "carrots", "qty" : 15, "orders_ids" : [ 6, 9 ] }
   { "_id" : "apples", "qty" : 35, "orders_ids" : [ 9, 8, 1, 6 ] }
   { "_id" : "pears", "qty" : 10, "orders_ids" : [ 3 ] }
   ```

#. The `$project` stage reshapes the output document to
   mirror the map-reduce's output to have two fields `_id` and
   `value`. The `$project` sets:

   - the `value.count` to the size of the `orders_ids` array
     using `$size`.

   - the `value.qty` to the `qty` field of input document.

   - the `value.avg` to the average number of qty per order
     using `$divide` and `$size`.

   ```javascript
   { "_id" : "apples", "value" : { "count" : 4, "qty" : 35, "avg" : 8.75 } }
   { "_id" : "pears", "value" : { "count" : 1, "qty" : 10, "avg" : 10 } }
   { "_id" : "chocolates", "value" : { "count" : 3, "qty" : 15, "avg" : 5 } }
   { "_id" : "oranges", "value" : { "count" : 7, "qty" : 63, "avg" : 9 } }
   { "_id" : "carrots", "value" : { "count" : 2, "qty" : 15, "avg" : 7.5 } }
   ```

#. Finally, the `$merge` writes the output to the
   collection `agg_alternative_3`. If an existing document has the same
   key `_id` as the new result, the operation overwrites the existing
   document. If there is no existing document with the same key, the
   operation inserts the document.

#. Query the `agg_alternative_3` collection to verify the results:

   ```javascript
   db.agg_alternative_3.find().sort( { _id: 1 } )
   ```

   The operation returns the following documents:

   ```javascript
   { "_id" : "apples", "value" : { "count" : 4, "qty" : 35, "avg" : 8.75 } }
   { "_id" : "carrots", "value" : { "count" : 2, "qty" : 15, "avg" : 7.5 } }
   { "_id" : "chocolates", "value" : { "count" : 3, "qty" : 15, "avg" : 5 } }
   { "_id" : "oranges", "value" : { "count" : 7, "qty" : 63, "avg" : 9 } }
   { "_id" : "pears", "value" : { "count" : 1, "qty" : 10, "avg" : 10 } }
   ```

**See also:**

For an alternative that uses custom aggregation expressions, see
Map-Reduce to Aggregation Pipeline Translation Examples.

## Output

The output of the `db.collection.mapReduce()` method is
identical to that of the `mapReduce` command. See the
Output section of the `mapReduce`
command for information on the `db.collection.mapReduce()`
output.

## Restrictions

`db.collection.mapReduce()` no longer supports
afterClusterTime. As such,
`db.collection.mapReduce()` cannot be associatd with
causally consistent sessions.

## Additional Information

- /tutorial/troubleshoot-map-function

- /tutorial/troubleshoot-reduce-function

- `mapReduce` command

- /aggregation

- Map-Reduce

- /tutorial/perform-incremental-map-reduce
