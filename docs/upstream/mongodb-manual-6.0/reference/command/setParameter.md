<!-- Converted from reference/command/setParameter.txt (reStructuredText). Includes are inlined. -->

# setParameter

## Definition

   

**`setParameter`**

`setParameter` is an administrative command for
modifying options normally set on the command line. You must issue
the `setParameter` command against the admin 
database.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0, M2, M5, M10+, and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

```javascript
db.adminCommand( 
   { 
     setParameter: 1, 
     <parameter>: <value> 
   } 
)
```

For the available parameters, including examples, see
/reference/parameters.

## Behavior

### Persistence

Commands issued by the admin command `setParameter`
do not survive server restarts. For a persistent option use the
`--setParameter` command line option 
or the `setParameter` configuration file setting.

### Stable API

When using Stable API V1 with apiStrict set to `true`, you cannot use
`setParameter` to modify server parameters.
