<!-- Converted from reference/command/logout.txt (reStructuredText). Includes are inlined. -->

# logout (database command)

## Definition

**`logout`**

**Deprecated since version:** 5.0

Attempting to use the `logout` command will write an 
error message to the log once per logout attempt.

This command will be removed in a future release.   

**Note:**

This command was used when you could log in as multiple users on a single physical connection.
Because this is no longer possible, running `logout` may cause connections to fail.
Going forward, you can achieve the same results by closing your connection.

## Compatibility

This command is available in deployments hosted in the following environments: 

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

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   { 
     logout: 1 
   }
)
```

## Example

**Note:**

If you're not logged in and using authentication, `logout`
has no effect.

Because MongoDB allows users defined in one database to have
privileges on another database, you must call `logout` while
using the same database context that you authenticated to.

If you authenticated to a database such as `users` or
`$external`, you must issue `logout` against this
database in order to successfully log out.

**Example:**

Use the `use <database-name>` helper in `mongosh`, or the
following `db.getSiblingDB()` method in an interactive
`mongosh` session or in `mongosh` shell
scripts to change the `db` object:

```javascript
db = db.getSiblingDB('<database-name>')
```

When you have set the database context and `db` object, you
can use the `logout` to log out of database as in the
following operation:

```javascript
db.runCommand( { logout: 1 } )
```
