<!-- Converted from reference/operator/aggregation/accumulator.txt (reStructuredText). Includes are inlined. -->

# $accumulator (accumulator operator)

## Definition

**`$accumulator`**

Defines a custom accumulator operator. Accumulators are operators that
maintain their state (e.g. totals, maximums, minimums, and related
data) as documents progress through the pipeline. Use the
`$accumulator` operator to execute your own JavaScript
functions to implement behavior not supported by the MongoDB Query
Language. See also `$function`.

`$accumulator` is available in these stages:

- `$bucket`

- `$bucketAuto`

- `$group`

**Important:**

Executing JavaScript inside of an aggregation operator may
decrease performance. Only use the `$accumulator` operator
if the provided pipeline operators cannot fulfill your
application's needs.

## Syntax

The `$accumulator` operator has this syntax:

```javascript
{ 
  $accumulator: {
    init: <code>,
    initArgs: <array expression>,        // Optional
    accumulate: <code>,
    accumulateArgs: <array expression>,
    merge: <code>,
    finalize: <code>,                    // Optional
    lang: <string>
  }
}
```

* - Field
  - Type
  - Description

* - init

  - String or Code

  - .. _accumulator-init:

    Function used to initialize the state. The `init` function
    receives its arguments from the initArgs array expression. You can specify the
    function definition as either BSON type Code or String.

    The `init` function has the following form:

    ```javascript
    function (<initArg1>, <initArg2>, ...) {
      ...
      return <initialState>
    }
    ```

    Spilling to disk or running a query on a sharded cluster can cause the 
    accumulator to be computed as a merge of multiple sub-accumulations, each 
    of which begins by calling `init()`. Ensure that your `init()`, 
    `accumulate()`, and `merge()` functions are compatible with this 
    execution model.

* - initArgs

  - Array

  - .. _accumulator-initArgs:

    Optional. Arguments passed to the `init` function.

    `initArgs` has the following form:

    ```javascript
    [ <initArg1>, <initArg2>, ... ]
    ```

    IMPORTANT: When used in a `$bucketAuto` stage, 
    `initArgs` cannot refer to the group key (i.e., you cannot use the 
    `$<fieldName>` syntax). Instead, in a `$bucketAuto` stage, 
    you can only specify constant values in `initArgs`.

* - accumulate

  - String or Code

  - .. _accumulator-accumulate:

    Function used to accumulate documents. The `accumulate`
    function receives its arguments from the current state and
    accumulateArgs array
    expression. The result of the `accumulate` function becomes
    the new state. You can specify the function definition as
    either BSON type Code or String.

    The `accumulate` function has the following form:

    ```javascript
    function(state, <accumArg1>, <accumArg2>, ...) {
      ... 
      return <newState>
    }
    ```

* - accumulateArgs

  - Array

  - .. _accumulator-accumulateArgs:

    Arguments passed to the `accumulate` function. You can use
    `accumulateArgs` to specify what field values to pass to
    the `accumulate` function.

    `accumulateArgs` has the following form:

    ```javascript
    [ <accumArg1>, <accumArg2>, ... ]
    ```

* - merge

  - String or Code

  - .. _accumulator-merge:

    Function used to merge two internal states. `merge` must be
    either a String or Code BSON type. `merge` returns the
    combined result of the two merged states. For information on
    when the merge function is called, see
    merge-multiple-states.

    The `merge` function has the following form:

    ```javascript
    function (<state1>, <state2>) {
      <logic to merge state1 and state2>
      return <newState>
    }
    ```

* - finalize

  - String or Code

  - .. _accumulator-finalize:

    Optional. Function used to update the result of the accumulation.

    The `finalize` function has the following form:

    ```javascript
    function (state) {
      ...
      return <finalState>
    }
    ```

* - lang

  - String

  - .. _accumulator-lang:

    The language used in the `$accumulator` code.

    IMPORTANT: Currently, the only supported value for `lang` is 
    `js`.

## Behavior

The following steps outline how the `$accumulator` operator
processes documents:

1. The operator begins at an initial state, defined by the
   init function. 
   
#. For each document, the operator updates
   the state based on the accumulate
   function. The accumulate function's
   first argument is the current state, and additional arguments are be
   specified in the accumulateArgs
   array.

#. When the operator needs to merge multiple intermediate states, it
   executes the merge function. For more
   information on when the merge function is
   called, see merge-multiple-states.
   
#. If a finalize function has been
   defined, once all documents have been processed and the state has
   been updated accordingly, finalize
   converts the state to a final output.

### Merge Two States with `$merge`

As part of its internal operations, the `$accumulator` operator
may need to merge two separate, intermediate states. The merge function specifies how the operator should merge
two states.

The merge function always merges two
states at a time. If more than two states must be merged,
the resulting merge of two states is merged with a single state. This
process repeats until all states are merged.

For example, `$accumulator` may need to combine two states in the
following scenarios:

- `$accumulator` is run on a sharded cluster. The operator
  needs to merge the results from each shard to obtain the final
  result.

- A single `$accumulator` operation exceeds its specified
  memory limit. If you specify the `allowDiskUse` option, the operator stores the
  in-progress operation on disk and finishes the operation in memory.
  Once the operation finishes, the results from disk and memory are
  merged together using the merge function.

### Document Processing Order

The order that MongoDB processes documents for the `init()`,
`accumulate()`, and `merge()` functions can vary, and might differ
from the order that those documents are specified to the
`$accumulator` function.

For example, consider a series of documents where the `_id` fields are
the letters of the alphabet:

```javascript
 :copyable: false

{ _id: 'a' },
{ _id: 'b' },
{ _id: 'c' }
...
{ _id: 'z' }
```

Next, consider an aggregation pipeline that sorts the documents by the
`_id` field and then uses an `$accumulator` function to concatenate
the `_id` field values:

```javascript
[
   {
      $sort: { _id: 1 }
   },
   {
      $group: {
         _id: null,
         alphabet: {
            $accumulator: {
               init: function() {
                  return ""
               },
               accumulate: function(state, letter) {
                  return(state + letter)
               },
               accumulateArgs: [ "$_id" ],
               merge: function(state1, state2) {         
                  return(state1 + state2)
               },
               lang: "js"
            }
         }
      }
   }
]
```

MongoDB does not guarantee that the documents are processed in the
sorted order, meaning the `alphabet` field does not necessarily get
set to `abc...z`.

Due to this behavior, ensure that your `$accumulator` function does
not need to process and return documents in a specific order.

### Javascript Enabled

To use `$accumulator`, you must have server-side scripting
enabled.

If you do not use `$accumulator` (or `$function`,
`$where`, or `mapReduce`), disable server-side
scripting: 

- For a `mongod` instance, see
  `security.javascriptEnabled` configuration option or
  `--noscripting` command-line option.

- For a `mongos` instance, see
  `security.javascriptEnabled` configuration option or the
  `--noscripting` command-line option.
  
  | In earlier versions, MongoDB does not allow JavaScript execution on
    `mongos` instances.

See also security-checklist-javascript.

### Unsupported Array and String Functions

MongoDB 6.0 upgrades the internal JavaScript engine used for
server-side JavaScript,
`$accumulator`, `$function`, and `$where`
expressions and from MozJS-60 to MozJS-91. Several deprecated,
non-standard array and string functions that existed in MozJS-60 are
removed in MozJS-91.

## Examples

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

### Use `$accumulator` to Implement the `$avg` Operator

**Note:**

This example walks through using the `$accumulator` operator
to implement the `$avg` operator, which is already supported
by MongoDB. The goal of this example is not to implement new
functionality, but to illustrate the behavior and syntax of the
`$accumulator` operator with familiar logic.

The following operation `groups` the documents by
`rated`, and uses `$accumulator` to compute the average
`imdb.rating` for each content rating. The `$match` stage
restricts the input to the `G`, `PG`, `PG-13`, and `R`
content ratings, and excludes documents where `imdb.rating` is
not a double, such as an empty string:

```javascript
```

Output:

```javascript
```

#### Behavior

The `$accumulator` defines an initial state where `count`
and `sum` are both set to `0`. For each document that the
`$accumulator` processes, it updates the state by:

- Incrementing the `count` by 1 and

- Adding the values of the document's `imdb.rating` field to the
  `sum`. The accumulate function can
  access the `imdb.rating` field because it is passed in the
  accumulateArgs field.

With each document that is processed, the
accumulate function returns the updated
state.

Once all documents have been processed, the
finalize function divides the `sum` of
the ratings by the `count` of documents to obtain the average. This
removes the need to keep a running computed average, since the
finalize function receives the cumulative
`sum` and `count` of all documents.

#### Comparison with `$avg`

This operation is equivalent to the following pipeline, which uses the
`$avg` operator:

```javascript
```

Output:

```javascript
```

### Use `initArgs` to Vary the Initial State by Group

You can use the initArgs option
to vary the initial state of `$accumulator`. This can be
useful if you want to, for example:

- Use the value of a field which is not in your state to affect your
  state, or

- Set the initial state to a different value based on the group being
  processed.

Suppose an application allows users to query this data to find movies.
It may be useful to show more results for the content rating that the
user prefers. For this example, the user's preferred content rating is
`PG-13`, which is passed to the `init` function as
`userProfileRated`.

The following aggregation pipeline `groups` the
documents by `rated`. The operation uses the `$accumulator`
to display a different number of movies from each content rating
depending on whether the movie's rating matches the rating in the
user's profile:

**Note:**

To run this example with a different preferred content rating,
replace `"PG-13"` in the initArgs
array with another value, such as `"R"`.

```javascript
```

Output:

```javascript
```

#### Behavior

The init function defines an initial state
containing `max` and `movies` fields. The `max` field sets the
maximum number of movies for that particular group. If the document's
`rated` field matches `userProfileRated`, that group contains a
maximum of 3 movies. Otherwise, if the document's `rated` field does
not match `userProfileRated`, the group contains at most a single
movie. The init function receives both the
`rated` and `userProfileRated` arguments from the initArgs array.

For each document that the `$accumulator` processes, it pushes
the `title` of the movie to the `movies` array, if that title would
not put the length of `movies` over the `max` value. With each
document that is processed, the accumulate function returns the updated state.

The merge function defines how to merge two
states. The function concatenates the `movies` arrays from each state
together, and the length of the resulting array is limited using the
[slice()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice)
method to ensure that it does not exceed the `max` value.

Once all documents have been processed, the finalize function modifies the resulting state to only
return the titles of the movies. Without this function, the `max`
field would also be included in the output, which does not fulfill any
needs for the application.
