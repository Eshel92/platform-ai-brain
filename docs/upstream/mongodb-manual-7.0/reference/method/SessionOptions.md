<!-- Converted from reference/method/SessionOptions.txt (reStructuredText). Includes are inlined. -->

# SessionOptions

## Definition

**`SessionOptions`**

The options for a `session` in
`mongosh`. To access the `SessionOptions`
object, use the `Session.getOptions()` method.

The session options available are:

* - Option
  - Description

* - `causalConsistency`

  - Boolean. Enables or disables causal consistency for the session.

    You can explicitly set the option when you start a session
    manually:

    - `Session = db.getMongo().startSession( { causalConsistency: true } )`

* - `readConcern`

  - Document. Specifies the read concern.

    In `mongosh`, you can set the option when
    you run `Mongo.startSession()`. You can also access
    the `readConcern` option via the following methods:

    - `Session.getOptions().getReadConcern()`

    - `Session.getOptions().setReadConcern(<document>)`

* - `readPreference`

  - Document. Specifies the read preference.

    In `mongosh`, you can set the option
    when you run `Mongo.startSession()`. You can also
    access the `readPreference` option via the following
    methods:

    - `Session.getOptions().getReadPreference()`

    - `Session.getOptions().setReadPreference({ mode: <string>, tags: <array>})`

* - `retryWrites`

  - Boolean. Enables or disables the ability to retry writes upon
    encountering transient network errors, such as during
    failovers.

    To enable retry writes, start `mongosh`
    with the `--retryWrites` option.

    You can view whether `retryWrites` is enabled for a session
    via the following method:

    - `Session.getOptions().shouldRetryWrites()`

* - `writeConcern`

  - Document. Specifies the write concern.

    In `mongosh`, you can set the options
    when you run `Mongo.startSession()`. You can also
    access the `writeConcern` option via the following methods:

    - `Session.getOptions().getWriteConcern()`

    - `Session.getOptions().setWriteConcern(<document>)`

Verify which options are enabled for the session by running
`Session.getOptions()`.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB
