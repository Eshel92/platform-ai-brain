<!-- Converted from tutorial/manage-database-users-x509.txt (reStructuredText). Includes are inlined. -->

:noprevnext:

# Manage Database Users Using X.509 Authentication

The Kubernetes Operator supports managing database users for deployments
running with TLS (Transport Layer Security) and X.509 internal cluster authentication enabled.

## Supported Authentication Mechanisms

The Kubernetes Operator supports SCRAM, LDAP, OpenID Connect, and X.509 authentication
mechanisms in deployments it creates. In an Kubernetes Operator-created
deployment, you cannot use `Ops Manager` to:

- Configure other authentication mechanisms for deployments.
- Manage users *not* using SCRAM, LDAP, or X.509 authentication.

After enabling X.509 authentication, you can add X.509 users using the `Ops Manager` interface or the [CustomResourceDefinition](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/).

## Prerequisites

Before managing database users, you must deploy a
replica set or
sharded cluster with TLS (Transport Layer Security) and X.509
enabled.

If you need to generate X.509 certificates for your MongoDB users,
see create-x509-certs.

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
  name: <resource-name>
spec:
  username: <rfc2253-subject>
  db: "$external"
  mongodbResourceRef:
    name: '<MongoDB-Resource-name>'
  roles:
    - db: <database-name>
      name: <role-name>
...
```

**Step 3: Open your preferred text editor and paste the example [CustomResourceDefinition](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/) into a new text file.**

**Step 4: Change the lines for the following parameters, as needed.**

Use the following table to guide you through changing the relevant
lines in the mongodbuser-specification:

* - Key
  - Type
  - Description
  - Example

* - `metadata.name`
  - string
  - The name of the database user resource.

    Resource names must be 44 characters or less.

  - `mms-user-1`

* - `spec.username`
  - string
  - The subject line of the x509 client certificate signed
    by the Kubernetes CA (Certificate Authority) (Kube CA).

    IMPORTANT: The username must comply with the
    [RFC 2253](https://tools.ietf.org/html/rfc2253)
    LDAPv3 Distinguished Name standard.

    To get the subject line of the X.509 certificate, run the
    following command:

    ```sh
    openssl x509 -noout \
      -subject -in <my-cert.pem> \
      -nameopt RFC2253
    ```

  - `CN=mms-user,U=My Organizational Unit,O=My Org,L=New York,ST=New York,C=US`

* - `spec.opsManager.configMapRef.name`
  - string
  - The name of the project containing the MongoDB database
    where user will be added. The
    `spec.cloudManager.configMapRef.name` setting is an
    alias for this setting and can be used in its place.
  - `my-project`

* - `spec.roles.db`
  - string
  - The database the role can act on.
  - `admin`

* - `spec.mongodbResourceRef.name`
  - string
  - The name of the MongoDB resource to
    which this user is associated.
  - `my-resource`

* - `spec.roles.name`
  - string
  - The name of the role to grant the database
    user. The role name can be any
    built-in MongoDB role or
    `custom role` that exists
    in Cloud Manager or Ops Manager.
  - `readWriteAnyDatabase`

**Step 5: Add any additional roles for the user to the [CustomResourceDefinition](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/).**

You may grant additional roles to this user using the format defined
in the following example:

```yaml
---
apiVersion: mongodb.com/v1
kind: MongoDBUser
metadata:
  name: mms-user-1
spec:
  username: CN=mms-user,U=My Organizational Unit,O=My Org,L=New York,ST=New York,C=US
  project: my-project
  db: "$external"
  roles:
    - db: admin
      name: backup
    - db: admin
      name: restore
...
```

**Step 6: Create the user.**

Invoke the following Kubernetes command to create your database user:

```sh
kubectl apply -f <database-user-conf>.yaml
```

When you create a new MongoDB database user, Kubernetes Operator automatically
creates a new Kubernetes [secret](https://kubernetes.io/docs/concepts/configuration/secret/). The Kubernetes [secret](https://kubernetes.io/docs/concepts/configuration/secret/)
contains the following information about the new database user:

- `username`: Username for the database user
- `password`: Password for the database user
- `connectionString.standard`: Standard connection string
  that can connect you to the database as this database user.
- `connectionString.standardSrv`: DNS seed list connection string that can
  connect you to the database as this database user.

**Note:**

Alternatively, you can specify an optional 
`spec.connectionStringSecretName` field in the 
mongodbuser-specification to specify 
the name of the connection string secret that the 
Kubernetes Operator creates.

You can use these credentials to Connect to a MongoDB Database Resource from Inside Kubernetes.

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
