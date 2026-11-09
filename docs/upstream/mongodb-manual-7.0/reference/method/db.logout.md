<!-- Converted from reference/method/db.logout.txt (reStructuredText). Includes are inlined. -->

# db.logout() (mongosh method)

**`db.logout()`**

**Deprecated since version:** 5.0

Attempting to use the `db.logout()` method will write an 
error message to the log once per logout attempt.

This method will be removed in a future release.

Ends the current authentication session. This function has no effect
if the current session is not authenticated.

**Note:**

If you're not logged in and using authentication, `db.logout()`
has no effect.

Because MongoDB allows users defined in one database to have
privileges on another database, you must call `db.logout()` while
using the same database context that you authenticated to.

If you authenticated to a database such as `users` or
`$external`, you must issue `db.logout()` against this
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
can use the `db.logout()` to log out of database as in the
following operation:

```javascript
db.logout()
```

`db.logout()` function provides a wrapper around the
database command `logout`.

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
