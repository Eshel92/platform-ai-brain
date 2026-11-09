<!-- Converted from reference/operator/aggregation/function.txt (reStructuredText). Includes are inlined. -->

# $function (aggregation)

## Definition

**`$function`**

Defines a custom aggregation function or expression in JavaScript.

You can use the `$function` operator to define custom
functions to implement behavior not supported by the MongoDB Query
Language. See also `$accumulator`.

**Important:**

Executing JavaScript inside an aggregation expression may
decrease performance. Only use the `$function`
operator if the provided pipeline operators cannot fulfill your
application's needs.

## Syntax

The `$function` operator has the following syntax:

```javascript
{ 
  $function: {
    body: <code>,
    args: <array expression>,
    lang: "js"
  }
}
```

| Field | Type | Description |
|---|---|---|
| body | String or Code | .. _function-body: The function definition. You can specify the function definition as either BSON type Code or String. See also lang. `function(arg1, arg2, ...) { ... }` or `"function(arg1, arg2, ...) { ... }"` |
| args | Array | .. _function-args: Arguments passed to the function body. If the body function does not take an argument, you can specify an empty array `[ ]`. The array elements can be any BSON type, including Code. See function-example-where-alternative. |
| lang | String | .. _function-lang: The language used in the body. You must specify `lang: "js"`. |

## Considerations

### Schema Validation Restriction

You cannot use `$function` as part of schema validation
query expression.

### Javascript Enablement

To use `$function`, you must have server-side scripting
enabled (default).

If you do not use `$function` (or `$accumulator`,
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

### Alternative to `$where`

The query operator `$where` can also be used to specify
JavaScript expression. However:
   
- The `$expr` operator allows the use of 
  aggregation expressions within the
  query language.

- The `$function` and `$accumulator` allows users to define 
  custom aggregation expressions in JavaScript if the provided pipeline 
  operators cannot fulfill your application's needs.
   
Given the available aggregation operators:

- The use of `$expr` with aggregation operators that do not use
  JavaScript (i.e. non-`$function` and
  non-`$accumulator` operators) is faster than `$where`
  because it does not execute JavaScript and should be preferred if
  possible.

- However, if you must create custom expressions,
  `$function` is preferred over `$where`.

### Unsupported Array and String Functions

MongoDB 6.0 upgrades the internal JavaScript engine used for
server-side JavaScript,
`$accumulator`, `$function`, and `$where`
expressions and from MozJS-60 to MozJS-91. Several deprecated,
non-standard array and string functions that existed in MozJS-60 are
removed in MozJS-91.

For the complete list of removed array and string functions, see the
6.0 compatibility notes.

## Examples

### Example 1: Usage Example

Create a sample collection named `players` with the following
documents:

```javascript
db.players.insertMany([
   { _id: 1, name: "Miss Cheevous",  scores: [ 10, 5, 10 ] },
   { _id: 2, name: "Miss Ann Thrope", scores: [ 10, 10, 10 ] },
   { _id: 3, name: "Mrs. Eppie Delta ", scores: [ 9, 8, 8 ] }
])
```

The following aggregation operation uses `$addFields` to
add new fields to each document:

- `isFound` whose value is determined by the custom
  `$function` expression that checks whether the MD5
  hash of the name is equal to a specified hash.

- `message` whose value is determined by the custom
  `$function` expression that format a string message
  using a template.

```javascript
db.players.aggregate( [
   { $addFields:
      {
        isFound:
            { $function:
               {
                  body: function(name) { 
                     return hex_md5(name) == "15b0a220baa16331e8d80e15367677ad"
                  },
                  args: [ "$name" ],
                  lang: "js"
               }
            },
         message: 
            { $function:
               {
                  body: function(name, scores) {
                     let total = Array.sum(scores);
                     return `Hello ${name}.  Your total score is ${total}.`
                  },
                  args: [ "$name", "$scores"],
                  lang: "js"
               }
            }
       }
    }
] )
```

The operation returns the following documents:

```javascript
{ "_id" : 1, "name" : "Miss Cheevous", "scores" : [ 10, 5, 10 ], "isFound" : false, "message" : "Hello Miss Cheevous.  Your total score is 25." }
{ "_id" : 2, "name" : "Miss Ann Thrope", "scores" : [ 10, 10, 10 ], "isFound" : true, "message" : "Hello Miss Ann Thrope.  Your total score is 30." }
{ "_id" : 3, "name" : "Mrs. Eppie Delta ", "scores" : [ 9, 8, 8 ], "isFound" : false, "message" : "Hello Mrs. Eppie Delta .  Your total score is 25." }
```

### Example 2: Alternative to `$where`

**Note:** Aggregation Alternatives Preferred over `$where`

The `$expr` operator allows the use of 
aggregation expressions within the
query language. The `$function` and `$accumulator` 
allows users to define custom aggregation expressions in JavaScript if the 
provided pipeline operators cannot fulfill your application's needs.

Given the available aggregation operators:

- The use of `$expr` with aggregation operators that do not
  use JavaScript (i.e. non-`$function` and
  non-`$accumulator` operators) is faster than
  `$where` because it does not execute JavaScript and should
  be preferred if possible.

- However, if you must create custom expressions,
  `$function` is preferred over `$where`.

As an alternative to a query that uses the `$where` operator,
you can use `$expr` and `$function`. For example,
consider the following `$where` example.

```javascript
db.players.find( { $where: function() { 
   return (hex_md5(this.name) == "15b0a220baa16331e8d80e15367677ad") 
} } );
```

The `db.collection.find()` operation returns the following document:

```javascript
{ "_id" : 2, "name" : "Miss Ann Thrope", "scores" : [ 10, 10, 10 ] }
```

The example can be expressed using `$expr` and `$function`:

```javascript
db.players.find( {$expr: { $function: {
      body: function(name) { return hex_md5(name) == "15b0a220baa16331e8d80e15367677ad"; },
      args: [ "$name" ],
      lang: "js"
} } } )
```
