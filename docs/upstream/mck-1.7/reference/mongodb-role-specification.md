<!-- Converted from reference/mongodb-role-specification.txt (reStructuredText). Includes are inlined. -->

# ClusterMongoDBRole Resource Specification

The `ClusterMongoDBRole` custom resource lets you configure the 
[role](https://www.mongodb.com/docs/atlas/security-add-mongodb-users/) 
required for a user to access a MongoDB database.

## Example

The following example shows a resource specification for a  `ClusterMongoDBRole` 
custom resource:

```yaml
---
apiVersion: mongodb.com/v1
kind: ClusterMongoDBRole
metadata:
  name: ldap-user-1
spec:
  role: "customRole"
  db: admin    
  privileges:
  - actions:
    - insert
    resource:
      collection: cats
      db: pets
  - actions:
    - insert
    - find
    resource:
      collection: dogs
      db: pets
...
```

## Required `ClusterMongoDBRole` Resource Settings

**`spec.role`**

*Type*: string

Name of the user-defined role.

**`spec.roles`**

*Type*: array

Array that lists the roles assigned to this user.

**`spec.roles.db`**

*Type*: string

The databases to which this role has access.

**`spec.roles.role`**

*Type*: string

The name of the inherited role.

**`spec.authenticationRestrictions`**

*Type*: array

Array that defines the IP address from which and to which users
assigned this `spec.security.roles.role` can
connect.

**`spec.db`**

*Type*: string

Database for which the privilege
`spec.privileges.actions`
apply.

If you provide a value for this setting, you must also provide a value
for
`spec.privileges.resource`.

**`spec.privileges`**

*Type*: array

Array that describes the privileges that users granted this role
possess.

**`spec.privileges.actions`**

*Type*: array

List of actions that users granted this role can perform. For a list
of accepted values, see Privilege Actions in the
MongoDB Server documentation for the MongoDB versions you deploy with the
Kubernetes Operator.

**`spec.privileges.resource`**

*Type*: collection

Resources for which the privilege
`spec.privileges.actions`
apply.

This collection must include either:

- The
  `spec.security.roles.privileges.resource.database`
  and
  `spec.security.roles.privileges.resource.collection`
  settings, or
- The
  `spec.security.roles.privileges.resource.cluster`
  setting with a value of `true`.

**`spec.privileges.resource.db`**

*Type*: string

Database for which the privilege
`spec.privileges.actions`
apply.

If you provide a value for this setting, you must also provide a value
for
`spec.privileges.resource.collection`.

**`spec.privileges.resource.collection`**

*Type*: string

Collection in the
`spec.privileges.resource.db`
for which the privilege
`spec.privileges.actions`
apply.

If you provide a value for this setting, you must also provide a value
for
`spec.privileges.resource.db`.
