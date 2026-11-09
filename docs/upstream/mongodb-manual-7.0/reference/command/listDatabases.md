<!-- Converted from reference/command/listDatabases.txt (reStructuredText). Includes are inlined. -->

# listDatabases (database command)

## Definition

**`listDatabases`**

The `listDatabases` command returns an unsorted list of all existing 
databases and basic statistics about each database. You must
run the `listDatabases` command against the `admin` database.

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

```javascript
db.adminCommand( 
   { 
     listDatabases: 1 
   } 
)
```

The value (e.g. `1`) does not affect the output of the
command.

## Command Fields

The command can take the following optional fields:

* - Field
  - Type
  - Description

* - `filter`
  - document
  - Optional. A query predicate that determines which databases are listed.

    You can specify a condition on any of the fields in the output of
    `listDatabases`:

    - `name`

    - `sizeOnDisk`

    - `empty`

    - `shards`

* - `nameOnly`
  - boolean
  - Optional. A flag to indicate whether the command should return just the
    database names, or return both database names and size information.

    The default value is `false`, so `listDatabases` returns
    the name and size information of each database.

* - `authorizedDatabases`
  - boolean
  - Optional. A flag that determines which databases are returned based on the
    user privileges when access control is enabled.

    - If `authorizedDatabases` is unspecified, and

      - If the user has `listDatabases` action on the
        cluster resource, `listDatabases` command returns all
        databases.

      - If the user does not have `listDatabases` action on
        the cluster, `listDatabases` returns only the databases for 
        which the user has privileges (including databases for which the user 
        has privileges on specific collections).

    - If `authorizedDatabases` is `true`, `listDatabases` returns
      only the databases for which the user has privileges (including databases 
      for which the user has privileges on specific collections).

    - If `authorizedDatabases` is `false`, and

      - If the user has `listDatabases` action on the
        cluster, `listDatabases` command returns all databases

      - If the user does not have `listDatabases` action on
        the cluster, `listDatabases` command errors with
        insufficient permissions.

    For more information, see listDatabases-behavior.

* - `comment`
  - any
  - .. include:: /includes/extracts/comment-content.rst

## Behavior

When authentication is enabled,
the `listDatabases` command returns different values based on 
the privileges assigned to the user who executes the command and the
`authorizedDatabases` command option:

- If `authorizedDatabases` is unspecified, and

  - If the user has `listDatabases` action on the
    cluster resource, `listDatabases` command returns all
    databases.

  - If the user does not have `listDatabases` action on
    the cluster, `listDatabases` command returns only the
    databases for which the user has privileges (including databases
    for which the user has privileges on specific collections).

- If `authorizedDatabases` is `true`, `listDatabases`
  command returns only the databases for which the user has
  privileges (including databases for which the user has privileges
  on specific collections).

- If `authorizedDatabases` is `false`, and

  - If the user has `listDatabases` action on the
    cluster, `listDatabases` command returns all databases

  - If the user does not have `listDatabases` action on
    the cluster, `listDatabases` command errors with
    insufficient permissions.

### Client Disconnection

If the client that issued `listDatabases` disconnects before the operation 
completes, MongoDB marks `listDatabases` for termination using 
`killOp`.

### Replica Set Member State Restriction

To run on a replica set member, `listDatabases` operations require the member 
to be in `PRIMARY` or `SECONDARY` state. If the member
is in another state, such as `STARTUP2`, the
operation errors.

## Examples

### List Database Names and Sizes

Run `listDatabases` against the `admin` database:

```javascript
db.adminCommand( { listDatabases: 1 } )
```

The following is an example of a `listDatabases` result:

```json
{
   "databases" : [
      {
         "name" : "admin",
         "sizeOnDisk" : 83886080,
         "empty" : false
      },
      {
         "name" : "local",
         "sizeOnDisk" : 83886080,
         "empty" : false
      },
      {
         "name" : "test",
         "sizeOnDisk" : 83886080,
         "empty" : false
      }
   ],
   "totalSize" : 251658240,
   "totalSizeMb" : 251,
   "ok" : 1
}
```

### List Database Names Only

Run `listDatabases` against the `admin` database. Specify
the `nameOnly: true` option:

```javascript
db.adminCommand( { listDatabases: 1, nameOnly: true} )
```

Example output:

```javascript
{
   "databases" : [
      {
         "name" : "admin"
      },
      {
         "name" : "local"
      },
      {
         "name" : "test"
      }
   ],
   "ok" : 1
}
```

### List Databases That Match the Filter

Run `listDatabases` against the `admin` database. Specify
the `filter` option to only list databases that match the specified filter criteria.

For example, the following specifies a filter such that
`listDatabases` only returns information on databases whose
name matches the specified `regular expression`:

```javascript
db.adminCommand( { listDatabases: 1, filter: { "name": /^rep/ } } )
```

### Sharded Clusters

When executed against a `mongos` instance,
`listDatabases`:

- adds a `shards` embedded document to each database's summary
  document if `nameOnly: false`, and
- excludes the `local` database.

Each element in the `shards` embedded document consists of a field
whose key gives the name of a collection on that shard, and whose value
represents the collection's size in bytes.

The `sizeOnDisk` field represents the total size of all
listed collections and indexes.

For example:

```javascript
{
  "databases" : [
    {
      "name" : "admin",
      "sizeOnDisk" : 16384,
      "empty" : false,
      "shards" : {
        "config" : 16384
      }
    },
    {
      "name" : "config",
      "sizeOnDisk" : 176128,
      "empty" : false,
      "shards" : {
        "clients" : 28672,
        "patients" : 8192,
        "config" : 139264
      }
    },
    {
      "name" : "test",
      "sizeOnDisk" : 12288,
      "empty" : false,
      "shards" : {
        "clients" : 12288
      }
    }
  ],
  "totalSize" : 204800,
  "totalSizeMb" : 0,
  "ok" : 1
}
```

**See also:**

/tutorial/use-database-commands.

## Output

**`listDatabases.databases`**

*Type: Array*

Array of documents, each containing information on a single
database.
   

**`listDatabases.databases.name`**

*Type: String*

Name of the database.

**`listDatabases.databases.sizeOnDisk`**

*Type: Integer*

Total size of the database files on disk, expressed in bytes.

**`listDatabases.databases.empty`**

*Type: Boolean*

Specifies whether the database is empty.
   

**`listDatabases.databases.shards`**

*Type: Document*

Each element in the `shards` document consists of a field whose key 
gives the name of a collection on that shard, and whose value 
represents the collection's size in bytes.

`shards` only appears in the output if `nameOnly: false`.

See Sharded Clusters
for details.

**`listDatabases.totalSize`**

*Type: Integer*

Sum of all the `sizeOnDisk` fields in bytes.

**`listDatabases.totalSizeMb`**

*Type: Integer*

Sum of all the `sizeOnDisk` fields, expressed in megabytes.

**`listDatabases.ok`**

*Type: Integer*

Return value for the command. A value of `1` indicates
success.
