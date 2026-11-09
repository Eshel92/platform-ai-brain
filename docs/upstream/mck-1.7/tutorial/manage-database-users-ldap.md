<!-- Converted from tutorial/manage-database-users-ldap.txt (reStructuredText). Includes are inlined. -->

:noprevnext:

# Manage Database Users Using LDAP Authentication

The Kubernetes Operator supports managing database users for deployments
running with TLS (Transport Layer Security) and LDAP cluster authentication enabled.

## Considerations

The configuration for users authenticated through LDAP (Lightweight Directory Access Protocol) relies on the
LDAP Query Templates and the mappings that MongoDB establishes.

To learn more, see the following sections in the MongoDB Server
documentation:

- LDAP Authorization
- LDAP Query Templates
- security.ldap.userToDNMapping

### Supported Authentication Mechanisms

The Kubernetes Operator supports SCRAM, LDAP, OpenID Connect, and X.509 authentication
mechanisms in deployments it creates. In an Kubernetes Operator-created
deployment, you cannot use `Ops Manager` to:

- Configure other authentication mechanisms for deployments.
- Manage users *not* using SCRAM, LDAP, or X.509 authentication.

## Prerequisites

Before managing database users, you must deploy a
replica set or
sharded cluster with LDAP (Lightweight Directory Access Protocol) enabled.
enabled. Optionally, you can enable TLS (Transport Layer Security). To learn more, see
Secure a Database Resource.

## Add a Database User

**Step 1: Configure `kubectl` to default to your namespace.**

If you have not already, run the following command to execute all 
`kubectl` commands in the namespace you created.

**Note:**

If you are deploying an Ops Manager resource in a multi-Kubernetes cluster MongoDB deployment:

- Set the `context` to the name of the central cluster, such as:
  `kubectl config set context "$MDB_CENTRAL_CLUSTER_FULL_NAME"`.

- Set the `--namespace` to the same scope
  that you used for your multi-Kubernetes cluster MongoDB deployment, such as: `kubectl config --namespace "mongodb"`.

```sh
kubectl config set-context $(kubectl config current-context) --namespace=<metadata.namespace>
```

**Step 2: Copy the following example [CustomResourceDefinition](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/).**

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

**Step 3: Open your preferred text editor and paste the example [CustomResourceDefinition](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/) into a new text file.**

**Step 4: Change the lines for the following parameters, as needed.**

Use the following table to guide you through changing the relevant
lines in the mongodbuser-specification. For a full list of LDAP user settings, see
security settings in the Kubernetes Operator
MongoDB resource specification.

| Key | Type | Description | Example |
|---|---|---|---|
| `metadata.name` | string | The name of the resource for the MongoDB database user. Resource names must be 44 characters or less. | `ldap-user-1` |
| `spec.db` | string | The name of the MongoDB database where users will be added. This value must be `$external`. | `$external` |
| `spec.mongodbResourceRef.name` | string | The name of the MongoDB resource to which this user is associated. | `my-resource` |
| `spec.opsManager.configMapRef.name` | string | The name of the project containing the MongoDB database where the user will be added. The `spec.cloudManager.configMapRef.name` setting is an alias for this setting and can be used in its place. | `my-project` |
| `spec.roles.db` | string | The database the role can act on. | `admin` |
| `spec.roles.name` | string | The name of the role to grant the database user. The role name can be any built-in MongoDB role or `custom role` that exists in Cloud Manager or Ops Manager. | `readWriteAnyDatabase` |
| `spec.username` | string | The authenticated username that is mapped to an LDAP Distinguished Name (DN) according to `spec.security.authentication.ldap.userToDNMapping`. The DN must already exist in your LDAP deployment. This username must comply with the [RFC 2253](https://tools.ietf.org/html/rfc2253) LDAPv3 Distinguished Name standard. `transformed` To learn more, see LDAP Query Templates in the MongoDB Manual. | `uid=mdb0,dc=example,dc=org` |

**Step 5: Add any additional roles for the user to the [CustomResourceDefinition](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/).**

You may grant additional roles to this user using the format defined
in the following example:

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

**Step 6: Create the user.**

Invoke the following Kubernetes command to create your database user:

```sh
kubectl apply -f <database-user-conf>.yaml
```

The following examples illustrate the connection string formats that you
can use when enabling authentication with LDAP in Kubernetes Operator MongoDB
deployments. These examples use the `mongodb` namespace and a replica
set deployment named `replica-set-ldap`. The examples are similar for
sharded clusters.

- `connectionString.standard`:Standard connection string
  that can connect you to the database as this database user.

  ```sh
  mongodb://replica-set-ldap-0-0-svc.mongodb.svc.cluster.local/?connectTimeoutMS=20000&replicaSet=replica-set-ldap&serverSelectionTimeoutMS=20000&ssl=true&authSource=$external
  ```

- `connectionString.standardSrv`: DNS seed list connection string that
  can connect you to the database as this database user.

  ```sh
  mongodb+srv://replica-set-ldap-svc.mongodb.svc.cluster.local/?connectTimeoutMS=20000&replicaSet=replica-set-ldap&serverSelectionTimeoutMS=20000&ssl=true&authSource=$external
  ```

Using the previously-shown formats, you can connect to the MongoDB
database with the MongoDB Shell (`mongosh`), as in the following
example:

```sh
mongosh <connection-string> \
  --host <my-replica-set>/web1.example.com \
  --port 30907 \
  --authenticationMechanism PLAIN \
  --username cn=rob,cn=Users,dc=ldaps-01,dc=myteam,dc=com
```

You can use these credentials to
connect to a MongoDB Database Resource from Inside Kubernetes.

**Step 7: View the newly created user in Cloud Manager or Ops Manager.**

You can view the newly-created user in Cloud Manager or Ops Manager:

1. From the Project's Deployment view, click
   the Security tab.

#. Click the MongoDB Users nested tab.

## Delete a Database User

To delete a database user, pass the `metadata.name` from the user
[ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) to the following command:

```sh
kubectl delete mdbu <metadata.name>
```
