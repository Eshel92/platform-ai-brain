<!-- Converted from reference/system-roles-collection.txt (reStructuredText). Includes are inlined. -->

# `system.roles` Collection in Self-Managed Deployments

The `system.roles` collection in the `admin` database stores the
user-defined roles. To create and manage these user-defined
roles, MongoDB provides role management commands.

## `system.roles` Schema

The documents in the `system.roles` collection have the following
schema:

```javascript
{
  _id: <system-defined id>,
  role: "<role name>",
  db: "<database>",
  privileges:
      [
          {
              resource: { <resource> },
              actions: [ "<action>", ... ]
          },
          ...
      ],
  roles:
      [
          { role: "<role name>", db: "<database>" },
          ...
      ]
}
```

A `system.roles` document has the following fields:

**`admin.system.roles.role`**

The `role` field is a string that
specifies the name of the role.

**`admin.system.roles.db`**

The `db` field is a string that specifies
the database to which the role belongs. MongoDB uniquely identifies
each role by the pairing of its name (i.e.
`role`) and its database.

**`admin.system.roles.privileges`**

The `privileges` array contains the
privilege documents that define the privileges for the role.

A privilege document has the following syntax:

```javascript
{
  resource: { <resource> },
  actions: [ "<action>", ... ]
}
```

Each privilege document has the following fields:

**`admin.system.roles.privileges[n].resource`**

A document that specifies the resources upon which the privilege
`actions` apply. The document
has one of the following form:

```javascript
{ db: <database>, collection: <collection> }
```

or

```javascript
{ cluster : true }
```

See resource-document for more details.

**`admin.system.roles.privileges[n].actions`**

An array of actions permitted on the resource. For a list of
actions, see security-user-actions.

**`admin.system.roles.roles`**

The `roles` array contains role documents
that specify the roles from which this role inherits privileges.

A role document has the following syntax:

```javascript
{ role: "<role name>", db: "<database>" }
```

A role document has the following fields:

**`admin.system.roles.roles[n].role`**

The name of the role. A role can be a built-in role provided by MongoDB or a user-defined
role.

**`admin.system.roles.roles[n].db`**

The name of the database where the role is defined.

## Examples

Consider the following sample documents found in `system.roles`
collection of the `admin` database.

### A User-Defined Role Specifies Privileges

The following is a sample document for a user-defined role `appUser`
defined for the `myApp` database:

```javascript
{
  _id: "myApp.appUser",
  role: "appUser",
  db: "myApp",
  privileges: [
       { resource: { db: "myApp" , collection: "" },
         actions: [ "find", "createCollection", "dbStats", "collStats" ] },
       { resource: { db: "myApp", collection: "logs" },
         actions: [ "insert" ] },
       { resource: { db: "myApp", collection: "data" },
         actions: [ "insert", "update", "remove", "compact" ] },
       { resource: { db: "myApp", collection: "system.js" },
         actions: [ "find" ] },
  ],
  roles: []
}
```

The `privileges` array lists the five privileges that the `appUser`
role specifies:

- The first privilege permits its actions ( `"find"`,
  `"createCollection"`, `"dbStats"`, `"collStats"`) on all the
  collections in the `myApp` database *excluding* its system
  collections. See resource-specific-db.

- The next two privileges permits *additional* actions on specific
  collections, `logs` and `data`, in the `myApp` database. See
  resource-specific-db-collection.

- The last privilege permits actions on one system
  collections in the `myApp`
  database. While the first privilege gives database-wide permission
  for the `find` action, the action does not apply to `myApp`'s
  system collections. To give access to a system collection, a
  privilege must explicitly specify the collection. See
  /reference/resource-document.

As indicated by the empty `roles` array, `appUser` inherits no
additional privileges from other roles.

### User-Defined Role Inherits from Other Roles

The following is a sample document for a user-defined role `appAdmin`
defined for the `myApp` database: The document shows that the
`appAdmin` role specifies privileges as well as inherits privileges
from other roles:

```javascript
{
  _id: "myApp.appAdmin",
  role: "appAdmin",
  db: "myApp",
  privileges: [
      {
         resource: { db: "myApp", collection: "" },
         actions: [ "insert", "dbStats", "collStats", "compact" ]
      }
  ],
  roles: [
      { role: "appUser", db: "myApp" }
  ]
}
```

The `privileges` array lists the privileges that the `appAdmin`
role specifies. This role has a single privilege that permits its
actions ( `"insert"`, `"dbStats"`, `"collStats"`, `"compact"`)
on all the collections in the `myApp` database *excluding* its system
collections. See resource-specific-db.

The `roles` array lists the roles, identified by the role names and
databases, from which the role `appAdmin` inherits privileges.
