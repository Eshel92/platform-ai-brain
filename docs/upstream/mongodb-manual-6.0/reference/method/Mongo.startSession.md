<!-- Converted from reference/method/Mongo.startSession.txt (reStructuredText). Includes are inlined. -->

# Mongo.startSession()

## Definition

**`Mongo.startSession(<options>)`**

Starts a session for the connection.
`mongosh` assigns the session ID to commands associated
with the session.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `startSession` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

A session can only be used with the `MongoClient` object that created
the session. A single session cannot be used concurrently. Operations
that use a single session must be run sequentially.

The `startSession()` method can take a document with
session options. The options available are:

* - Field
  - Description

* - causalConsistency

  - Boolean. Enables or disables causal consistency for the session.
    `Mongo.startSession()` enables `causalConsistency`
    by default.

    After starting a session, you cannot modify its
    `causalConsistency` setting.

    The session may have causal consistency enabled even
    though the `Mongo` connection object may have
    causal consistency disabled or vice versa. To set causal
    consistency on the connection object, see
    `Mongo.setCausalConsistency()`.

* - readConcern

  - Document. Specifies the read concern.

    To modify the setting after starting a session, see
    `Session.getOptions().setReadConcern()`.

* - readPreference

  - Document. Specifies the read preference.

    The readPreference document contains the `mode` field and
    the optional `tags` field:

    ```javascript
    { mode: <string>, tags: <array> }
    ```

    To modify the setting after starting a session, see
    `Session.getOptions().setReadPreference()`.

* - retryWrites

  - Boolean. Enables or disables the ability to retry writes upon
    encountering transient network errors.

    If you start `mongosh` with the
    `--retryWrites` option, `retryWrites` is enabled by
    default for `Mongo.startSession()`.

    After starting a session, you cannot modify its
    `retryWrites` setting.

* - writeConcern

  - Document. Specifies the write concern.

    To modify the setting after starting a session, see
    `Session.getOptions().setWriteConcern()`.

## Examples

The following starts a session with causal consistency and retryable
writes enabled on the `Mongo` connection object associated with
`mongosh`'s global `db` variable:

```javascript
db = db.getMongo().startSession({retryWrites: true, causalConsistency: true}).getDatabase(db.getName());
```
