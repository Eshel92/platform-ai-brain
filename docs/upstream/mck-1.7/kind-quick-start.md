<!-- Converted from kind-quick-start.txt (reStructuredText). Includes are inlined. -->

# Quick Start for the Kubernetes Operator

**Important:**

This section is for single Kubernetes cluster deployments only. For
multi-Kubernetes cluster MongoDB deployments, see multi-cluster-quick-start-ref.

The MongoDB Controllers for Kubernetes Operator uses the Kubernetes API and tools to manage MongoDB
clusters running within your Kubernetes cluster. Kubernetes Operator works together 
with MongoDB Cloud Manager or Ops Manager. This tutorial demonstrates how to deploy 
and connect to your first MongoDB replica set in MongoDB Cloud Manager with Kubernetes Operator. 
You can use Kind (Kubernetes in Docker) to quickly set up a cluster. 
To learn more, see [Kind](https://kind.sigs.k8s.io/).

## Prerequisites

This tutorial requires:

- A running MongoDB Cloud Manager cluster.
- A running Kubernetes cluster.
- Kubernetes nodes running on supported hardware architectures.
- The [MongoDB Shell](https://www.mongodb.com/docs/mongodb-shell/) installed on your local machine.

## Procedure

**Step 1: Add the [MongoDB Helm Charts for Kubernetes](https://mongodb.github.io/helm-charts) repository to Helm.**

```sh
helm repo add mongodb https://mongodb.github.io/helm-charts
```

**Step 2: Install the MongoDB Controllers for Kubernetes Operator**

To install the Kubernetes Operator with Helm, see the 
instructions in the repository.

**Example**

The following command installs the MongoDB Controllers for Kubernetes Operator in the `mongodb` 
namespace with the optional `--create-namespace` option. By 
default, Kubernetes Operator uses the `default` namespace. 

```sh
helm install kubernetes-operator mongodb/mongodb-kubernetes --namespace mongodb --create-namespace
```

**Step 3: Configure `kubectl` to default to your namespace.**

If you haven't already, run the following command to execute all 
`kubectl` commands in the namespace you created:

```sh
kubectl config set-context $(kubectl config current-context) --namespace=mongodb
```

**Step 4: Configure the Kubernetes Operator**

a. `Go to the Kubernetes Setup Page in the Cloud Manager UI`.

#. Click Create New API Keys or 
   Use Existing API Keys.

#. Complete the form. To learn more, see 
   `Programmatic Access to Cloud Manager`.

#. Click Generate Key and YAML.

**Step 5: Copy and save the ConfigMap.**

Copy and save the generated `config-map.yaml` file.

**Example:**

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-project
  namespace: mongodb
data:
  baseUrl: https://cloud.mongodb.com

  projectName: my-project # this is an optional parameter
  orgId: 5ecd252f8c1a75033c74106c # this is a required parameter
```

To learn more, see the parameter descriptions.

**Step 6: Copy and save the Secret.**

Copy and save the generated `secret.yaml` file.

**Example:**

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: organization-secret
  namespace: mongodb
stringData:
  publicKey: <public_key>
  privateKey: <private_key>
```

For security purposes, MongoDB Cloud Manager displays this file only once.

**Step 7: Apply the ConfigMap and Secret.**

Run the following command:

```sh
kubectl apply -f secret.yaml -f config-map.yaml
```

**Step 8: Deploy the MongoDB replica set resource.**

a. Copy and save the following YAML (Yet Another Markup Language) file:

   ```yaml
   apiVersion: mongodb.com/v1
   kind: MongoDB
   metadata:
     name: demo-mongodb-cluster-1
     namespace: mongodb
   spec:
     members: 3
     version: 8.0.0
     type: ReplicaSet
     security:
       authentication:
         enabled: true
         modes: ["SCRAM"]
     cloudManager:
       configMapRef:
         name: my-project
     credentials: organization-secret
     persistent: true
     podSpec:
       podTemplate:
         spec:
          containers:
           - name: mongodb-enterprise-database
             resources:
               limits:
                 cpu: 2
                 memory: 1.5G
               requests:
                 cpu: 1
                 memory: 1G 
               persistence:
                 single:
                   storage: 10Gi
   ```

#. Run the following command:

   ```sh
   kubectl apply -f <replica-set-conf>.yaml
   ```

**Step 9: Create a secret with your database user password**

You can choose to use a cleartext password or a Base64-encoded 
password. Plaintext passwords use `stringData.password` and 
Base64-encoded passwords use `data.password`.

**Note:**

Provide your values for the following parameters. To learn more, 
see the parameter descriptions.

For a cleartext password, create and save the following YAML (Yet Another Markup Language) file:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mms-user-1-password
  # corresponds to user.spec.passwordSecretKeyRef.name
type: Opaque
stringData:
  password: <my-plain-text-password>
  # corresponds to user.spec.passwordSecretKeyRef.key
```

For a Base64-encoded password, create and save the following YAML 
file:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mms-user-1-password
  # corresponds to user.spec.passwordSecretKeyRef.name
type: Opaque
data:
  password: <base-64-encoded-password>
  # corresponds to user.spec.passwordSecretKeyRef.key
```

**Step 10: Create a database user.**

a. Copy and save the following mongodbuser-specification file:

   ```yaml
   apiVersion: mongodb.com/v1
   kind: MongoDBUser
   metadata:
     name: mms-scram-user-1
   spec:
     passwordSecretKeyRef:
       name: mms-user-1-password
       # Match to metadata.name of the User Secret
       key: password
     username: "mms-scram-user-1"
     db: "admin" #
     mongodbResourceRef:
       name: "demo-mongodb-cluster-1"
       # Match to MongoDB resource using authentication
     roles:
     - db: "admin"
       name: "clusterAdmin"
     - db: "admin"
       name: "userAdminAnyDatabase"
     - db: "admin"
       name: "readWrite"
   ```

#. Run the following command:

   ```sh
   kubectl apply -f <database-user-conf>.yaml
   ```

**Step 11: View the newly created user in Cloud Manager or Ops Manager.**

You can view the newly-created user in Cloud Manager or Ops Manager:

a. From the Project's Deployment view, click
   the Security tab.

#. Click the MongoDB Users nested tab.

**Step 12: Connect to the MongoDB replica set.**

Perform the following steps in the `Cloud Manager` application:

a. Click Deployment in the left navigation.

#. Click `ellipsis` for the deployment to which you want
   to connect.

#. Click Connect to this instance.

#. Run the connection command in a terminal to connect to the
   deployment.
