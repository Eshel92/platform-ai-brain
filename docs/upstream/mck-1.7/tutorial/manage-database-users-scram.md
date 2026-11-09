<!-- Converted from tutorial/manage-database-users-scram.txt (reStructuredText). Includes are inlined. -->

:noprevnext:

# Manage Database Users Using SCRAM Authentication

The Kubernetes Operator supports managing database users using SCRAM
authentication on MongoDB deployments.

## Considerations

### Supported SCRAM Implementations

When you specify `SCRAM` as the authentication mechanism, the
implementation of SCRAM used depends upon:

- The version of MongoDB and
- If the database is the Application Database or another database.

| MongoDB Version | Database | SCRAM Implementation |
|---|---|---|
| 7.0 or later | Any except Application Database | `SCRAM-SHA-256` |
| Any | Application Database | `SCRAM-SHA-1` |

### Supported Authentication Mechanisms

The Kubernetes Operator supports SCRAM, LDAP, OpenID Connect, and X.509 authentication
mechanisms in deployments it creates. In an Kubernetes Operator-created
deployment, you cannot use `Ops Manager` to:

- Configure other authentication mechanisms for deployments.
- Manage users *not* using SCRAM, LDAP, or X.509 authentication.

After enabling SCRAM authentication, you can add SCRAM users using the
`Ops Manager` interface or by configuring the users in the [CustomResourceDefinition](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/) based on the mongodbuser-specification.

## Prerequisites

Before managing database users, you must deploy a
standalone,
replica set, or
sharded cluster.

For multi-Kubernetes cluster MongoDB deployments, you must deploy replica sets.
See Deploy Multiple Clusters.

## Add a Database User

**Important:**

You cannot assign the same database user 
to more than one MongoDB
standalone,
replica set, or
sharded cluster.
This includes database users with 
admin roles.

### Create User Secret

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

**Step 2: Copy the following example [secret](https://kubernetes.io/docs/concepts/configuration/secret/).**

You can choose to use a cleartext password:

```yaml
---
apiVersion: v1
kind: Secret
metadata:
  name: <mms-user-1-password>
  # corresponds to user.spec.passwordSecretKeyRef.name
type: Opaque
stringData:
  password: <my-plain-text-password>
  # corresponds to user.spec.passwordSecretKeyRef.key
...
```

or you can choose to use a Base64-encoded password:

```yaml
---
apiVersion: v1
kind: Secret
metadata:
  name: <mms-user-1-password>
  # corresponds to user.spec.passwordSecretKeyRef.name
type: Opaque
data:
  password: <base-64-encoded-password>
  # corresponds to user.spec.passwordSecretKeyRef.key
...
```

**Note:**

Make sure to copy the desired password configuration. Plaintext
passwords use `stringData.password` and Base64-encoded
passwords use `data.password`

**Step 3: Create a new User Secret YAML file.**

a. Open your preferred text editor.
b. Paste this User Secret into a new text file.

If you're using [HashiCorp Vault](https://www.vaultproject.io/) as your secret storage tool, 
you can Create a Vault Secret instead.

To learn about your options for secret
storage, see Configure Secret Storage.

**Step 4: Change the highlighted lines.**

Use the following table to guide you through changing the highlighted
lines in the Secret:

| Key | Type | Description | Example |
|---|---|---|---|
| `metadata.name` | string | Name of the database password secret. Resource names must be 44 characters or less. | `mms-scram-user-1-password` |
| `stringData.password` | string | Plaintext password for the desired user. Use this option and value *or* `data.password`. You can't use both. | `<my-plain-text-password>` |
| `data.password` | string | Base64-encoded password for the desired user. Use this option and value *or* `stringData.password`. You can't use both. You must encode your password into Base64 yourself then paste the resulting value with this option. There are tools for most every platform and multiple web-based tools as well. | `<my-base64-encoded-password>` |

**Step 5: Save the User Secret file with a `.yaml` extension.**

### Create MongoDBUser

**Step 1: Copy the following MongoDBUser example.**

```yaml
---
apiVersion: mongodb.com/v1
kind: MongoDBUser
metadata:
  name: <mms-scram-user-1>
spec:
  passwordSecretKeyRef:
    name: <mms-user-1-password>
    # Match to metadata.name of the User Secret
    key: password
  username: "<mms-scram-user-1>"
  db: "admin" #
  mongodbResourceRef:
    name: "<my-replica-set>"
    # Match to MongoDB resource using authentication
  roles:
    - db: "admin"
      name: "clusterAdmin"
    - db: "admin"
      name: "userAdminAnyDatabase"
    - db: "admin"
      name: "readWrite"

...
```

**Step 2: Create a new MongoDBUser file.**

a. Open your preferred text editor.
b. Paste this MongoDBUser into a new YAML file.

**Step 3: Change the highlighted lines.**

Use the following table to guide you through changing the highlighted
lines in the mongodbuser-specification:

| Key | Type | Description | Example |
|---|---|---|---|
| `metadata.name` | string | Name of the database user resource. Resource names must be 44 characters or less. | `mms-scram-user-1` |
| `spec.username` | string | Name of the database user. | `mms-scram-user-1` |
| `spec.passwordSecretKeyRef.name` | string | `metadata.name` value of the secret that stores the user's password. | `my-resource` |
| `spec.mongodbResourceRef.name` | string | Name of the MongoDB resource this user is associated with. | `my-resource` |
| `spec.roles.db` | string | Database on which the role can act. | `admin` |
| `spec.roles.name` | string | Name of the role to grant the database user. The role name can be any built-in MongoDB role or `custom role` that exists in Cloud Manager or Ops Manager. | `readWriteAnyDatabase` |

**Step 3: Add any additional roles for the user to the MongoDBUser.**

You may grant additional roles to this user.

**Step 4: Save the MongoDBUser file with a `.yaml` extension.**

**Step 5: Create the user.**

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

You can use these credentials to 
Connect to a MongoDB Database Resource from Inside Kubernetes.

**Step 6: View the newly created user in Cloud Manager or Ops Manager.**

You can view the newly-created user in Cloud Manager or Ops Manager:

a. From the Project's Deployment view, click
   the Security tab.

#. Click the MongoDB Users nested tab.

## Delete a Database User

To delete a database user, pass the `metadata.name` from the user
MongoDBUser to the following command:

```sh
kubectl delete mdbu <metadata.name>
```

## Change Authentication Mechanism

To change your user authenication mechanism to SCRAM:

1. Disable authentication.

   Under `spec.security.authentication`, change `enabled` to
   `false`.

   ```yaml
   spec:
     security:
       authentication:
         enabled : false
   ```

2. Reapply the user's resource definition.

3. Wait for the MongoDBResource to reach the `running` state.

4. Enable SCRAM authentication.

   Under `spec.security.authentication`, change `enabled` to
   `true` and set `spec.security.authentication.modes` to ``
   ["SCRAM"]``.

   ```yaml
   spec:
     security:
       authentication:
         enabled : true
         modes: ["SCRAM"]
   ```

5. Reapply the MongoDBUser resource.

6. Wait for the MongoDBResource to reach the `running` state.
