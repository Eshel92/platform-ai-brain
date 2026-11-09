<!-- Converted from reference/resource-document.txt (reStructuredText). Includes are inlined. -->

# Resource Document on Self-Managed Deployments

The resource document specifies the resources upon which a
privilege permits `actions`.

## Database and/or Collection Resource

To specify databases and/or collections, use the following syntax:

```javascript
{ db: <database>, collection: <collection> }
```

### Specify a Collection of a Database as Resource

If the resource document specifies both the `db` and `collection`
fields as non-empty strings, the resource is the specified
collection in the specified database. For example, the following
document specifies a resource of the `inventory` collection in the
`products` database:

```javascript
{ db: "products", collection: "inventory" }
```

For a user-defined role scoped for a non-`admin` database, the
resource specification for its privileges must specify the same
database as the role. User-defined roles scoped for the
`admin` database can specify other databases.

For user-defined roles, only roles scoped for the `admin` database
can have this resource specification for their privileges.

### Specify a Database as Resource

If only the `collection` field is an empty string (`""`), the
resource is the specified database, excluding the system
collections. For example, the
following resource document specifies the resource of the `test`
database, excluding the system collections:

```javascript
{ db: "test", collection: "" }
```

For a user-defined role scoped for a non-`admin` database, the
resource specification for its privileges must specify the same
database as the role. User-defined roles scoped for the
`admin` database can specify other databases.

For user-defined roles, only roles scoped for the `admin` database
can have this resource specification for their privileges.

**Note:** When you specify a database as the resource, system

collections are excluded, unless you name them explicitly, as in the
following:

```javascript
{ db: "test", collection: "system.js" }
```

System collections include but are not limited to the following:

- `<database>.system.profile`
- `<database>.system.js`
- /reference/system-users-collection in the `admin` database
- /reference/system-roles-collection in the `admin` database

### Specify Collections Across Databases as Resource

If only the `db` field is an empty string (`""`), the resource is
all collections with the specified name across all databases. For
example, the following document specifies the resource of all
the `accounts` collections across all the databases:

```javascript
{ db: "", collection: "accounts" }
```

For a user-defined role scoped for a non-`admin` database, the
resource specification for its privileges must specify the same
database as the role. User-defined roles scoped for the
`admin` database can specify other databases.

For user-defined roles, only roles scoped for the `admin` database
can have this resource specification for their privileges.

### Specify All Non-System Collections in All Databases

If both the `db` and `collection` fields are empty strings
(`""`), the resource is all collections, excluding the system
collections, in all the databases:

```javascript
{ db: "", collection: "" }
```

For a user-defined role scoped for a non-`admin` database, the
resource specification for its privileges must specify the same
database as the role. User-defined roles scoped for the
`admin` database can specify other databases.

For user-defined roles, only roles scoped for the `admin` database
can have this resource specification for their privileges.

## Cluster Resource

To specify the cluster as the resource, use the following syntax:

```javascript
{ cluster : true }
```

Use the `cluster` resource for actions that affect the state of the
system rather than act on specific set of databases or collections.
Examples of such actions are `shutdown`, `replSetReconfig`, and
`addShard`. For example, the following document grants the action
`shutdown` on the `cluster`.

```javascript
{ resource: { cluster : true }, actions: [ "shutdown" ] }
```

For a user-defined role scoped for a non-`admin` database, the
resource specification for its privileges must specify the same
database as the role. User-defined roles scoped for the
`admin` database can specify other databases.

For user-defined roles, only roles scoped for the `admin` database
can have this resource specification for their privileges.

## `anyResource`

The internal resource `anyResource` gives access to every resource in
the system and is intended for internal use. **Do not** use this resource,
other than in exceptional circumstances. The syntax for this resource is
`{ anyResource: true }`.
