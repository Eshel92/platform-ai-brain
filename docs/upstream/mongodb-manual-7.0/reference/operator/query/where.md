<!-- Converted from reference/operator/query/where.txt (reStructuredText). Includes are inlined. -->

# $where (query predicate operator)

## Definition

**`$where`**

Use the `$where` operator to pass either a string
containing a JavaScript expression or a full JavaScript function to
the query system. The `$where` provides greater
flexibility, but requires that the database processes the
JavaScript expression or function for *each* document in the
collection. Reference the document in the JavaScript expression or
function using either `this` or `obj` .

## Compatibility

You can use `$where` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The `$where` operator has the following form:

```javascript
{ $where: <string|JavaScript Code> }
```

**Note:**

`$where` no longer supports the deprecated 
BSON type JavaScript code with scope (BSON Type 15). 
The `$where` operator only supports BSON type String (BSON Type 2) or 
BSON type JavaScript (BSON Type 13). The use of BSON type JavaScript with 
scope for `$where` has been deprecated since MongoDB 4.2.1.

**Note:** Aggregation Alternatives Preferred

The `$expr` operator allows the use of 
aggregation expressions within
the query language. The `$function` and 
`$accumulator` allows users to define custom aggregation expressions 
in JavaScript if the provided
pipeline operators 
cannot fulfill your application's needs.

Given the available aggregation operators:

- The use of `$expr` with aggregation operators that do not
  use JavaScript (i.e. non-`$function` and
  non-`$accumulator` operators) is faster than
  `$where` because it does not execute JavaScript and should
  be preferred if possible.

- However, if you must create custom expressions,
  `$function` is preferred over `$where`.

## Behavior

### Available JavaScript Properties and Functions

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

### `elemMatch`

Only apply the `$where` query operator to top-level
documents. The `$where` query operator will not work inside a
nested document, for instance, in an `$elemMatch` query.

### Considerations

- Do not use global variables.

- `$where` evaluates JavaScript and cannot take
  advantage of indexes. Therefore, query performance improves
  when you express your query using the standard MongoDB
  operators (e.g., `$gt`, `$in`).

- In general, you should use `$where` only when you
  cannot express your query using another operator. If you must
  use `$where`, try to include at least one other
  standard query operator to filter the result set. Using
  `$where` alone requires a collection scan.

Using normal non\-`$where` query statements provides the
following performance advantages:

- MongoDB will evaluate non\-`$where` components of query
  before `$where` statements. If the
  non\-`$where` statements match no documents, MongoDB
  will not perform any query evaluation using `$where`.

- The non\-`$where` query statements may use an
  index.

### JavaScript Enablement

To use `$where` (or `$function`,
`$accumulator`, or `mapReduce`), you must have
server-side scripting enabled (default).

However, if you do not use these operations, disable server-side
scripting: 

- For a `mongod` instance, see
  `security.javascriptEnabled` configuration option or
  `--noscripting` command-line option.

- For a `mongos` instance, see
  `security.javascriptEnabled` configuration option or the
  `--noscripting` command-line option.

See also security-checklist-javascript.

### Unsupported Array and String Functions

MongoDB 6.0 upgrades the internal JavaScript engine used for
server-side JavaScript,
`$accumulator`, `$function`, and `$where`
expressions and from MozJS-60 to MozJS-91. Several deprecated,
non-standard array and string functions that existed in MozJS-60 are
removed in MozJS-91.

## Example

Consider the following documents in the `players` collection:

```javascript
db.players.insertMany([
   { _id: 12378, name: "Steve", username: "steveisawesome", first_login: "2017-01-01" },
   { _id: 2, name: "Anya", username: "anya", first_login: "2001-02-02" }
])
```

The following example uses `$where` and the `hex_md5()`
JavaScript function to compare the value of the `name` field to an
MD5 hash and returns any matching document.

```bash
db.players.find( { $where: function() { 
   return (hex_md5(this.name) == "9b53e667f30cd329dca1ec9e6a83e994") 
} } );
```

The operation returns the following result:

```bash
{
   "_id" : 2,
   "name" : "Anya",
   "username" : "anya",
   "first_login" : "2001-02-02"
}
```

As an alternative, the previous example can be rewritten using
`$expr` and `$function`. You can define custom aggregation 
expression in JavaScript with the aggregation operator `$function`. 
To access `$function` and other aggregation operators in
`db.collection.find()`, use with `$expr`:

```javascript
db.players.find( {$expr: { $function: {
      body: function(name) { return hex_md5(name) == "9b53e667f30cd329dca1ec9e6a83e994"; },
      args: [ "$name" ],
      lang: "js"
} } } )
```

If you must create custom expressions, `$function` is
preferred over `$where`.
