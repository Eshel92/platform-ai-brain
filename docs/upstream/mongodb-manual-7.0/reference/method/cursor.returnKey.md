<!-- Converted from reference/method/cursor.returnKey.txt (reStructuredText). Includes are inlined. -->

# cursor.returnKey() (mongosh method)

## Definition

**`cursor.returnKey()`**

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

**Tip:**

`$meta` supports the keyword `"indexKey"` to return index 
key metadata if an index is used. The use of 
`{ $meta: "indexKey" }` is preferred over 
`cursor.returnKey()`.

Modifies the cursor to return index keys rather than the documents.

The `cursor.returnKey()` has the following form:

```javascript
cursor.returnKey()
```

:returns:

   The cursor that `returnKey()` is attached to 
   with a modified result set. This allows for additional cursor modifiers 
   to be chained.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Behavior

If the query does not use an index to perform the read operation, the 
cursor returns empty documents.

## Example

The `restaurants` collection contains documents with the following schema:

```javascript
db.restaurants.insertOne( 
   {
      _id: ObjectId("564f3a35b385149fc7e3fab9"),
      address: {
         building: "2780",
         coord: [
            -73.98241999999999,
            40.579505
         ],
         street: "Stillwell Avenue",
         zipcode: "11224"
      },
      borough: "Brooklyn",
      cuisine: "American ",
      grades: [
         {
            date: ISODate("2014-06-10T00:00:00Z"),
            grade: "A",
            score: 5
         },
         {
            date: ISODate("2013-06-05T00:00:00Z"),
            grade: "A",
            score: 7
         }
      ],
      name: "Riviera Caterer",
      restaurant_id: "40356018"
   }
)
```

   
The collection has two indexes in addition to the default `_id` index:

```javascript
{
   "v" : 1,
   "key" : {
      "_id" : 1
   },
   "name" : "_id_",
   "ns" : "guidebook.restaurant"
},
{
   "v" : 1,
   "key" : {
      "cuisine" : 1
   },
   "name" : "cuisine_1",
   "ns" : "guidebook.restaurant"
},
{
   "v" : 1,
   "key" : {
      "_fts" : "text",
      "_ftsx" : 1
   },
   "name" : "name_text",
   "ns" : "guidebook.restaurant",
   "weights" : {
      "name" : 1
   },
   "default_language" : "english",
   "language_override" : "language",
   "textIndexVersion" : 3
}
```

      
The following code uses the `cursor.returnKey()` method to return 
only the indexed fields used for executing the query:

```javascript
var csr = db.restaurant.find( { "cuisine" : "Japanese" } )
csr.returnKey()
```

   
This returns the following:

```javascript
{ "cuisine" : "Japanese" }
{ "cuisine" : "Japanese" }
{ "cuisine" : "Japanese" }
{ "cuisine" : "Japanese" }
...
```
