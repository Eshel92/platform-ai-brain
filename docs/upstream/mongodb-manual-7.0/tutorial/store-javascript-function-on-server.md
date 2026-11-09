<!-- Converted from tutorial/store-javascript-function-on-server.txt (reStructuredText). Includes are inlined. -->

:orphan:

# Store a JavaScript Function on the Server

There is a special system collection named `system.js` that can 
store JavaScript functions for reuse.

## Before you Begin

This task uses the legacy `mongo` shell to load server side 
functions from the `system.js` collection. This version of the shell
is no longer supported. For an alternative solution in the MongoDB 
Shell, see mdb-shell-write-scripts.

## About this Task

Consider the follow recommendations when using `system.js`:

- Do not store application logic in the database.
- There are performance limitations to running JavaScript inside of 
  MongoDB. 
- Application code is most effective when it shares version 
  control with the application.

## Steps

To store a function, insert the function into the `system.js` 
collection, as in these examples:

**Step 1: Create a test collection**

```javascript
db.test_numbers.insertMany([
   { value: 1 },
   { value: 2 },
   { value: 3 },
   { value: 4 },
   { value: 5 },
   { value: 6 }
])
```

**Step 2: Store JavaScript functions in the database**

To store JavaScript functions in the database, insert a document
with these fields:

- The `_id` field holds the name of the function and is unique 
  per database.

- The `value` field holds the function definition.

The following example creates an `echo` 
function in the `system.js` collection:

```javascript
db.system.js.insertOne(
   {
      _id: "echo",
      value : function(x) { return x; }
   }
)
```

The following example creates an `isEven` function 
in the `system.js` collection:

```javascript
db.system.js.insertOne(
   {
      _id: "isEven",
      value: function (num) {
         return num % 2 === 0;
      }
   }
)
```

These functions, saved as BSON type, are available 
for use from any JavaScript context, such as `mapReduce` and 
`$where`.

**Note:**

Functions saved as the deprecated BSON type JavaScript (with
scope), cannot be used by
`mapReduce` and `$where`.

**Step 3: Load the stored JavaScript functions into the shell**

```javascript
db.loadServerScripts()
```

**Step 4: Run the stored JavaScript functions**

a. The following code example runs the `echo` function
   stored in `system.js`:

   ```javascript
   echo("test")
   ```

   Output:

   ```javascript
   test
   ```

#. The following code example runs the `isEven`
   function stored in `system.js` in the `$where` 
   operator on the `test_numbers` collection:

   ```javascript
   db.test_numbers.find({
      $where: function () {
         return isEven(this.value);
      }
   })
   ```

   Output:

   ```javascript
   { "_id" : ObjectId("668d7be41b55bec1bf191499"), "value" : 2 }
   { "_id" : ObjectId("668d7be41b55bec1bf19149b"), "value" : 4 }
   { "_id" : ObjectId("668d7be41b55bec1bf19149d"), "value" : 6 }  
   ```
