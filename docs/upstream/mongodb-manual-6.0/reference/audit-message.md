<!-- Converted from reference/audit-message.txt (reStructuredText). Includes are inlined. -->

# System Event Audit Messages

**Note:**

System Event Audit Messages are available in 
MongoDB Enterprise
and MongoDB Atlas.

To learn more about this feature in MongoDB Atlas, see 
the Atlas documentation for set-up-database-auditing
and mongodb-logs.

## Audit Message

The event auditing feature can record events in
JSON format. To configure auditing output, see
/tutorial/configure-auditing.

**Changed in version:** 5.0

The recorded JSON messages have the following syntax:

```none
{
  atype: <string>,
  ts : { $date: <timestamp> },
  uuid : { $binary: <string>, $type: <string> },
  local: { ip: <string>, port: <int> || isSystemUser: <boolean> || unix: <string> },
  remote: { ip: <string>, port: <int> || isSystemUser: <boolean> || unix: <string> },
  users : [ { user: <string>, db: <string> }, ... ],
  roles: [ { role: <string>, db: <string> }, ... ],
  param: <document>,
  result: <int>
}
```

* - Field

  - Type

  - Description

* - `atype`

  - string

  - Action type. See audit-action-details-results.

* - `ts`

  - document

  - Document that contains the date and UTC time of the event, in ISO
    8601 format.

* - .. _audit-message-uuid:

    `uuid`

  - document

  - A document that contains a message identifier.

    The UUID (Universally unique identifier) identifies a 
    client connection. Use the UUID to track audit events connected
    to that client. 

    The value of the `$type` field is BSON type
    `04` which indicates that the `$binary` field contains a
    UUID.

    **New in version:** 5.0

* - .. _audit-message-local:

    `local`

  - document

  - A document that contains the `ip` address and the `port`
    number of the running instance.

    Starting in MongoDB 5.0, can alternatively be a document with one of
    these fields:

    - `isSystemUser` that indicates whether the user who
      caused the event was a system user. Logged for self-referential jobs
      initiated by a background process that runs on the same server
      instance.

    - `unix` that contains the MongoDB socket file path if the client
      connects through a Unix domain socket.

    **Note:**

    Starting in MongoDB 5.0, the `local` field is deprecated.
    Use the `localEndpoint` field in the clientMetadata audit message instead.

    **Changed in version:** 5.0

* - `remote`

  - document

  - A document that contains the `ip` address and the `port`
    number of the incoming connection associated with the event.

    Starting in MongoDB 5.0, can alternatively be a document with one of
    these fields:

    - `isSystemUser` that indicates whether the user who
      caused the event was a system user. Logged for self-referential jobs
      initiated by a background process that runs on the same server
      instance.

    - `unix` that contains the MongoDB socket file path if the client
      connects through a Unix domain socket.

    **Changed in version:** 5.0

* - `users`

  - array

  - Array of user identification documents. Because MongoDB allows a
    session to log in with different user per database, this array can
    have more than one user. Each document contains a `user` field for
    the username and a `db` field for the authentication database for
    that user.

* - `roles`

  - array

  - Array of documents that specify the roles granted to the user. Each document contains a
    `role` field for the name of the role and a `db` field for the
    database associated with the role.

* - `param`

  - document

  - Specific details for the event. See audit-action-details-results.

* - `result`

  - integer

  - Error code. See audit-action-details-results.
       
       

## Audit Event Actions, Details, and Results

The following table lists for each `atype` or action type, the
associated `param` details and the `result` values, if any.

* - `atype`

  - `param`

  - `result`

* - .. _audit-message-authenticate:

    `authenticate`

  - .. code-block:: none
       :copyable: false

       {
         user: <user name>,
         db: <database>,
         mechanism: <mechanism>
       }

    Starting in MongoDB 5.0, `authenticate`:

    - Is logged for incomplete authentication attempts.

    - Includes the principle name and identifier in
      `mechanism` for external authentication mechanisms such as
      x.509 and Amazon Web Services
      Identity and Access Management (AWS-IAM) (see
      `authMechanism`).

    **Changed in version:** 5.0

  - | `0` - Success
    | `18` - Authentication Failed
    | `334` - Mechanism Unavailable

* - .. _audit-message-authCheck:

    `authCheck`

  - .. code-block:: none
       :copyable: false

       {
         command: <name>,
         ns: <database>.<collection>,
         args: <command object>
       }

    | `ns` field is optional.
    | `args` field may be redacted.

    By default, the auditing system logs only the authorization
    failures. To enable the system to log authorization successes,
    use the `auditAuthorizationSuccess` parameter.

    Enabling `auditAuthorizationSuccess` degrades performance
    more than logging only the authorization failures.

    Starting in MongoDB 5.0, `authCheck` is not logged for actions
    that are generated internally.

    **Changed in version:** 5.0

  - | `0` - Success
    | `13` - Unauthorized to perform the operation.

* - .. _audit-message-clientMetadata:

    `clientMetadata`

  - .. code-block:: none
       :copyable: false

       {
          localEndpoint : {
             ip : <IP address of running instance>,
             port : <port of running instance>
          } || {
             unix : <MongoDB socket file path if connecting through
                     a Unix domain socket>
          },
          clientMetadata : {
             driver : {
                name : <client driver name>,
                version : <client driver version>
             },
             os : {
                type : <client operating system type>,
                name : <client operating system name>,
                architecture : <client operating system architecture>,
                version : <client operating system version>
             },
             platform : <client platform name>,
             application : {
                name : <client application name>
             }
          }
       }

    Contains the client metadata. Logged when the client runs the
    `hello` command.

    **See also:**

    log-messages-client-data

    **New in version:** 5.0

  - `0` - Success

* - .. _audit-message-createCollection:

    `createCollection`

  - .. code-block:: none
       :copyable: false

       {
          ns: <database>.<collection || view>,
          viewOn: <database>.<collection>,
          pipeline: [ <pipeline definition> ]
       }

    Logged when a:

    - Collection is created.

    - View is created, with the view
      name logged in the `ns` field.

    Starting in MongoDB 5.0, this additional information is logged for a
    view:

    - `viewOn` field with the database and collection for the view.

    - `pipeline` field with the
      aggregation pipeline definition
      for the view.

    **Changed in version:** 5.0

  - `0` - Success

* - `createDatabase`

  - .. code-block:: none
       :copyable: false

       { ns: <database> }

  - `0` - Success

* - .. _audit-message-createIndex:

    `createIndex`

  - .. code-block:: none
       :copyable: false

       {
         ns: <database>.<collection>,
         indexName: <index name>,
         indexSpec: <index specification>,
         indexBuildState: <index build state>
       }

    Possible values for `indexBuildState` are:

    - `IndexBuildStarted`
    - `IndexBuildSucceeded`
    - `IndexBuildAborted`

    Starting in MongoDB 5.0, `createIndex` audit events
    are:

    - Logged at the start and end of index creation, and includes a
      message indicating if the index was successfully created or
      not.

    - Attributed to the originating user for the action that
      caused the `createIndex` audit event.

    - Logged for a `createCollection` event if the
      collection has an index.

    **Changed in version:** 5.0

  - | `0` - Success
    | `276` - Index build aborted.

    The audit message contains result code `276` for
    `createIndex` audit events with `IndexBuildState`
    set to `IndexBuildAborted`. The audit message contains result
    code `0` for `createIndex` audit events with
    `IndexBuildState` set to `IndexBuildStarted` or
    `IndexBuildSucceeded`.

* - .. _audit-message-directAuthMutation:

    `directAuthMutation`

  - .. code-block:: none
       :copyable: false

       {
          document: {
             <collection modifications>
          },
          ns: <database>.<collection>,
          operation: <database operation>
       }

    Logged when a database operation directly modifies the contents
    of the `admin.system.users` or `admin.system.roles`
    collections.

    **New in version:** 5.0

  - `0` - Success

* - `renameCollection`

  - .. code-block:: none
       :copyable: false

       {
         old: <database>.<collection>,
         new: <database>.<collection>
       }

  - `0` - Success

* - .. _audit-message-dropCollection:

    `dropCollection`

  - .. code-block:: none
       :copyable: false

       {
          ns: <database>.<collection || view>,
          viewOn: <database>.<collection>,
          pipeline: [ <pipeline definition> ]
       }

    Logged when a:

    - Collection is dropped.

    - View is dropped, with the view
      name logged in the `ns` field.

    Starting in MongoDB 5.0, this additional information is logged for a
    view:

    - `viewOn` field with the database and collection for the view.

    - `pipeline` field with the
      aggregation pipeline definition
      for the view.

    In addition, starting in MongoDB 5.0, a
    `dropCollection` audit event is logged when a
    `dropDatabase` event occurs.

    **Changed in version:** 5.0

  - | `0` - Success
    | `26` - `NamespaceNotFound`

    If the collection or view does not exist, the audit message shows
    the return code as `result: 26`. 

* - `dropDatabase`

  - .. code-block:: none
       :copyable: false

       { ns: <database> }

  - `0` - Success

* - `dropIndex`

  - .. code-block:: none
       :copyable: false

       {
         ns: <database>.<collection>,
         indexName: <index name>
       }

  - `0` - Success

* - `createUser`

  - .. code-block:: none
       :copyable: false

       {
         user: <user name>,
         db: <database>,
         customData: <document>,
         roles: [
            {
              role: <role name>,
              db: <database>
            },
            ...
         ]
       }

    The `customData` field is optional.

  - `0` - Success

* - `dropUser`

  - .. code-block:: none
       :copyable: false

       {
         user: <user name>,
         db: <database>
       }

  - `0` - Success

* - `dropAllUsersFromDatabase`

  - .. code-block:: none
       :copyable: false

       { db: <database> }

  - `0` - Success

* - `updateUser`

  - .. code-block:: none
       :copyable: false

       {
         user: <user name>,
         db: <database>,
         passwordChanged: <boolean>,
         customData: <document>,
         roles: [
            {
              role: <role name>,
              db: <database>
            },
            ...
         ]
       }

    The `customData` field is optional.

  - `0` - Success

* - `grantRolesToUser`

  - .. code-block:: none
       :copyable: false

       {
         user: <user name>,
         db: <database>,
         roles: [
            {
              role: <role name>,
              db: <database>
            },
            ...
         ]
       }

  - `0` - Success

* - `revokeRolesFromUser`

  - .. code-block:: none
       :copyable: false

       {
         user: <user name>,
         db: <database>,
         roles: [
            {
              role: <role name>,
              db: <database>
            },
            ...
         ]
       }

  - `0` - Success

* - `createRole`

  - .. code-block:: none
       :copyable: false

       {
         role: <role name>,
         db: <database>,
         roles: [
            {
              role: <role name>,
              db: <database>
            },
            ...
         ],
         privileges: [
           {
             resource: <resource document>,
             actions: [ <action>, ... ]
           },
           ...
         ]
       }

    The `roles` and the `privileges` fields are optional.

    For details on the resource document, see resource-document.
    For a list of actions, see security-user-actions.

  - `0` - Success

* - `updateRole`

  - .. code-block:: none
       :copyable: false

       {
         role: <role name>,
         db: <database>,
         roles: [
            {
              role: <role name>,
              db: <database>
            },
            ...
         ],
         privileges: [
           {
             resource: <resource document>,
             actions: [ <action>, ... ]
           },
           ...
         ]
       }

    The `roles` and the `privileges` fields are optional.

    For details on the resource document, see resource-document.
    For a list of actions, see security-user-actions.

  - `0` - Success

* - `dropRole`

  - .. code-block:: none
       :copyable: false

       {
         role: <role name>,
         db: <database>
       }

  - `0` - Success

* - `dropAllRolesFromDatabase`

  - .. code-block:: none
       :copyable: false

       { db: <database> }

  - `0` - Success

* - `grantRolesToRole`

  - .. code-block:: none
       :copyable: false

       {
         role: <role name>,
         db: <database>,
         roles: [
            {
              role: <role name>,
              db: <database>
            },
            ...
         ]
       }

  - `0` - Success

* - `revokeRolesFromRole`

  - .. code-block:: none
       :copyable: false

       {
         role: <role name>,
         db: <database>,
         roles: [
            {
              role: <role name>,
              db: <database>
            },
            ...
         ]
       }

  - `0` - Success

* - `grantPrivilegesToRole`

  - .. code-block:: none
       :copyable: false

       {
         role: <role name>,
         db: <database>,
         privileges: [
           {
             resource: <resource document>,
             actions: [ <action>, ... ]
           },
           ...
         ]
       }

    For details on the resource document, see resource-document.
    For a list of actions, see security-user-actions.

  - `0` - Success

* -  `revokePrivilegesFromRole`

  - .. code-block:: none
       :copyable: false

       {
         role: <role name>,
         db: <database name>,
         privileges: [
           {
             resource: <resource document>,
             actions: [ <action>, ... ]
           },
           ...
         ]
       }

    For details on the resource document, see resource-document.
    For a list of actions, see security-user-actions.

  - `0` - Success

* - `replSetReconfig`

  - .. code-block:: none
       :copyable: false

       {
         old: {
          _id: <replicaSetName>,
          version: <number>,
          ...
          members: [ ... ],
          settings: { ... }
         },
         new: {
          _id: <replicaSetName>,
          version: <number>,
          ...
          members: [ ... ],
          settings: { ... }
         }
       }

    For details on the replica set configuration document, see
    /reference/replica-configuration.

  - `0` - Success

* - `enableSharding`

  - .. code-block:: none
       :copyable: false

       { ns: <database> }

  - `0` - Success

* - `shardCollection`

  - .. code-block:: none
       :copyable: false

       {
         ns: <database>.<collection>,
         key: <shard key pattern>,
         options: { unique: <boolean> }
       }

  - `0` - Success

* - `addShard`

  - .. code-block:: none
       :copyable: false

       {
         shard: <shard name>,
         connectionString: <hostname>:<port>,
         maxSize: <maxSize>
       }

    When a shard is a replica set, the `connectionString` includes the
    replica set name and can include other members of the replica set.

  - `0` - Success

* - `refineCollectionShardKey`

  - .. code-block:: none
       :copyable: false

       {
         ns: <database>.<collection>,
         key: <shard key pattern>
       }

  - `0` - Success

* - `removeShard`

  - .. code-block:: none
       :copyable: false

       { shard: <shard name> }

  - `0` - Success

* - `shutdown`

  - .. code-block:: none
       :copyable: false

       { }

    Indicates commencement of database shutdown.

  - `0` - Success

* - `applicationMessage`

  - .. code-block:: none
       :copyable: false

       { msg: <custom message string> }

    See `logApplicationMessage`.

  - `0` - Success

* - .. _audit-message-logout:

    `logout`

  - .. code-block:: none
       :copyable: false

       {
         reason: <string>,
         initialUsers: [ <document>, ... ],
         updatedUsers: [ <document>, ... ], 
       }

    `reason` will be either:
      - "Explicit logout from <database>"
      - "Implicit logout due to client connection closure"

    `initialUsers` is an array of documents containing users 
    authenticated on the current client prior to logout.

    `updatedUsers` is an array of documents containing users 
    expected to be authenticated on the current client after the 
    logout event. 

    Each document in `initialUsers` and `updatedUsers` contains:
      - `user`: the username
      - `db`: the database `user` is authenticated to

    **New in version:** 5.0

  - `0` - Success

* - .. _audit-message-startup:

    `startup`

  - .. code-block:: none
       :copyable: false

       { options: <document> }

    The `options` document contains the options the instance was 
    started with.

    **New in version:** 5.0

  - `0` - Success
