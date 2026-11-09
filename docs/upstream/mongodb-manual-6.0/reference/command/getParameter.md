<!-- Converted from reference/command/getParameter.txt (reStructuredText). Includes are inlined. -->

# getParameter

## Definition

**`getParameter`**

`getParameter` is an administrative command for
retrieving the values of parameters. Use the `db.adminCommand(
{ command } )` method to run the
`getParameter` command in the `admin` database.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command has limited support in M0, M2, M5, and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The command has the following syntax:

```javascript
db.adminCommand(
   { 
     getParameter: <value>, 
     <parameter> : <value>,
     comment: <any>
   }
)
```

## Command Fields

The command takes the following fields:

* - Field
  - Type
  - Description

* - `getParameter`
  - int, string, document
  - Specify a value of:

    - `1` (or any integer value) to return the value for the 
      specified `<parameter>`.

    - `'*'` to return values for all parameters available to
      `getParameter`, ignoring the `<parameter>` field.

    - `{ showDetails: true }` to return a document containing:

      - `value`, the value that `<parameter>` is set to
      - `settableAtRuntime`, whether or not `<parameter>` can 
        be set at runtime
      - `settableAtStartup`, whether or not `<parameter>` can
        be set at startup  

    - `{ showDetails: true, allParameters: true }` to return a 
      document containing showDetails fields for **all** parameters.

* - `<parameter>`
  - string
  - String name of the parameter to retrieve.

    The value for `<value>` does not affect output.

* - `comment`
  - any
  - .. include:: /includes/extracts/comment-content.rst

## Behavior

`getParameter` runs on the `admin` database only, and returns 
an error if run on any other database. 

The possible value for `<parameter>` may vary depending on what version and 
storage engine in use. See getParameter-retrieve-all-params for an 
example of listing the available parameters.

## Examples

### Retrieve Single Parameter

The following operation runs `getParameter` on the `admin` 
database using a value of `saslHostName` to retrieve the value for 
that parameter:

```javascript
db.adminCommand( { getParameter : 1, "saslHostName" : 1 } )
```

  
The command returns the following output:

**Note:**

The output may vary depending on the version and specific
configuration of your MongoDB instance.

```javascript
{ "saslHostName" : "www.example.net:27018", "ok" : 1 }
```

### Retrieve All Parameters

The following operation runs `getParameter` with a value of
`'*'` to retrieve all parameters:

```javascript
db.adminCommand( { getParameter : '*' } )
```

**Note:**

The output may vary depending on the version of MongoDB and the 
specific configuration of the running MongoDB instance.

**See also:**

`setParameter` for more about these parameters.

### Report Details on a Single Parameter

The following example runs `getParameter` with 
`{showDetails: true}` to report details 
on `saslHostName`.

```javascript
db.adminCommand( { getParameter : { showDetails: true }, "saslHostName" : 1 } )
```

  
Example output:

```javascript
{
  saslHostName: {
    value: '<hostname>',
    settableAtRuntime: false,
    settableAtStartup: true
  },
  ok: 1
}
```

**Note:**

The output may vary depending on the version and specific
configuration of your MongoDB instance.

### Report Details for All Parameters

The following example runs `getParameter` with 
`{showDetails: true, allParameters: true}` to report 
details on **all** parameters.

```javascript
db.adminCommand( { getParameter : { showDetails: true, allParameters: true } } )
```
