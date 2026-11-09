<!-- Converted from reference/method/rs.freeze.txt (reStructuredText). Includes are inlined. -->

# rs.freeze() (mongosh method)

## Description

**`rs.freeze(seconds)`**

Makes the current replica set member ineligible to become
primary for the period specified.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `replSetFreeze` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

The `rs.freeze()` method has the following parameter:

| Parameter | Type | Description |
|---|---|---|
| `seconds` | number | The duration the member is ineligible to become primary. |

          

## Compatibility

This method is available in deployments hosted in the following environments:

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB
