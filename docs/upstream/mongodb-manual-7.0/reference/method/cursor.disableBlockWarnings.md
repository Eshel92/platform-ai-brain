<!-- Converted from reference/method/cursor.disableBlockWarnings.txt (reStructuredText). Includes are inlined. -->

# cursor.disableBlockWarnings() (mongosh method)

## Definition

**`cursor.disableBlockWarnings()`**

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

Use the `disableBlockWarnings()` cursor option to silence warnings
that `mongosh` prints when you run blocking calls on cursors, such
as `.next()` or `.hasNext()` on change streams and tailable
cursors.

## Syntax

```javascript
db.<collection>.find(<match document>).disableBlockWarnings()
```

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

## Example

The following example silences warnings on a tailable cursor that is
stored in a variable called `myTailableCursor`:

```javascript
myTailableCursor.disableBlockWarnings()
```
