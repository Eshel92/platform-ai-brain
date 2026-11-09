<!-- Converted from reference/operator/aggregation/ifNull.txt (reStructuredText). Includes are inlined. -->

# $ifNull (expression operator)

## Definition

**`$ifNull`**

The `$ifNull` expression evaluates input expressions for
null values and returns:
   
- The first non-null input expression
  value found.
   
- A replacement expression value if all
  input expressions evaluate to null.
     
`$ifNull` treats undefined values and missing fields as
null.
   

## Compatibility

You can use `$ifNull` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

```none
{
   $ifNull: [
      <input-expression-1>,
      ...
      <input-expression-n>,
      <replacement-expression-if-null>
   ]
}
```

## Examples

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

### Single Input Expression

The following example uses `$ifNull` to return:

- `rated` if the `rated` field is non-null.

- `"Not Rated"` string if `rated` is null or missing.

```javascript
```

Output:

```javascript
```

### Multiple Input Expressions

**New in version:** 5.0

The following example uses `$ifNull` to return:

- `tomatoes.critic.rating` if it's non-null.

- `tomatoes.viewer.rating` if `tomatoes.critic.rating` is null
  or missing and `tomatoes.viewer.rating` is non-null.

- `0` if both `tomatoes.critic.rating` and
  `tomatoes.viewer.rating` are null or missing.

```javascript
```

Output:

```javascript
```
