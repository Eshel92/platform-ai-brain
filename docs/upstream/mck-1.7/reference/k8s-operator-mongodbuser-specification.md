<!-- Converted from reference/k8s-operator-mongodbuser-specification.txt (reStructuredText). Includes are inlined. -->

# MongoDB User Resource Specification

The `MongoDBUser` custom resource lets you configure the authentication and [roles](https://www.mongodb.com/docs/atlas/security-add-mongodb-users/) required for a user to access a MongoDB database.

## Example

The following example shows a resource specification for a  `MongoDBUser` custom resource:

```yaml
---
apiVersion: mongodb.com/v1
kind: MongoDBUser
metadata:
  name: ldap-user-1
spec:
  username: "uid=mdb0,dc=example,dc=org"
  db: "$external" 
  mongodbResourceRef:
    name: ldap-replica-set
  roles:
  - db: "admin"
    name: "clusterAdmin"
  - db: "admin"
    name: "readWriteAnyDatabase"
  - db: "admin"
    name: "dbAdminAnyDatabase"

...
```

## Required `MongoDBUser` Resource Settings

This section describes settings that you must use for all `MongoDBUser` resources.

`apiVersion`
  *Type*: string

  Version of the MongoDB Kubernetes resource schema.

`kind`
  *Type*: string

  Kind of MongoDB Kubernetes resource to create. Set this to `MongoDBUser`.

`metadata.name`
  *Type*: string

  Human-readable name so you can identify this particular `MongoDBUser` resource.

  Resource names must be 44 characters or less.

`spec.db`
  *Type*: string

  Name of the MongoDB database that these users will access. The default is `admin`.

`spec.username`
  *Type*: string

  Human-readable label that identifies the user needed to authenticate to the MongoDB database or collection.

## Optional `MongoDBUser` Resource Settings

The `MongoDBUser` custom resource can use the following settings:

`spec.connectionStringSecretName`
  *Type*: string

  Name of the connection string secret that the Kubernetes Operator creates.

  When you create a new MongoDB database user, Kubernetes Operator automatically
  creates a new Kubernetes [secret](https://kubernetes.io/docs/concepts/configuration/secret/). The Kubernetes [secret](https://kubernetes.io/docs/concepts/configuration/secret/)
  contains the following information about the new database user:

  - `username`: Username for the database user
  - `password`: Password for the database user
  - `connectionString.standard`: Standard connection string
    that can connect you to the database as this database user.
  - `connectionString.standardSrv`: DNS seed list connection string that can
    connect you to the database as this database user.

`spec.mongodbResourceRef.name`
  *Type*: string

  Name of the MongoDB resource to which this user is associated. For example, `my-resource`.
  
`spec.mongodbResourceRef.namespace`
  *Type*: string

  The [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) that contains the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) for this user. 
  If unspecified, the Kubernetes Operator keeps connection secrets in the same [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) as the `MongoDBUser` custom resource.

`spec.passwordSecretKeyRef.name`
  *Type*: string
  
  `metadata.name` value of the secret that stores the user's password.
  For example, `my-secret-name`.

`spec.passwordSecretKeyRef.key`
  *Type*: string

  Name of the field in the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that
  contains the password for this MongoDB database user.

  To learn more, see the `Kubernetes documentation`.

`spec.roles.db`
  *Type*: string

  MongoDB database on which the [role](https://www.mongodb.com/docs/atlas/security-add-mongodb-users/) can act. For example, `admin`.

`spec.roles.name`
  *Type*: string

  Name of the [role](https://www.mongodb.com/docs/atlas/security-add-mongodb-users/) to grant the database user.
