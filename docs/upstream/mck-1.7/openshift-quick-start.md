<!-- Converted from openshift-quick-start.txt (reStructuredText). Includes are inlined. -->

# OpenShift Quick Start

**Important:**

This section is for single Kubernetes cluster deployments only. For
multi-Kubernetes cluster MongoDB deployments, see multi-cluster-quick-start-ref.

MongoDB Controllers for Kubernetes Operator uses the Kubernetes API and tools to manage MongoDB
clusters. Kubernetes Operator works together with MongoDB Cloud Manager or Ops Manager. This 
tutorial demonstrates how to deploy and connect to your first replica 
set in Cloud Manager or Ops Manager from OpenShift with Kubernetes Operator.

## Prerequisites

This tutorial requires:

- A running Cloud Manager or Ops Manager cluster.

## Procedure

**Step 1: Clone the MongoDB Controllers for Kubernetes Operator repository and check out the tag for the current release.**

```sh
git clone https://github.com/mongodb/mongodb-kubernetes.git
cd mongodb-kubernetes
git checkout 1.7.0
```

**Step 2: Create a [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) for your Kubernetes deployment.**

By default, The Kubernetes Operator uses the `mongodb` namespace. To
simplify your installation, consider creating a namespace labeled
`mongodb` using the following [kubectl](https://kubernetes.io/docs/reference/kubectl/kubectl/) command:

```sh
kubectl create namespace mongodb
```

**Step 3: Configure `kubectl` to default to your namespace.**

If you have not already, run the following command to execute all 
`kubectl` commands in the namespace you created:

```sh
kubectl config set-context $(kubectl config current-context) --namespace=mongodb
```

**Step 4: Install the MongoDB Controllers for Kubernetes Operator**

a. Invoke the following [oc](https://docs.openshift.com/container-platform/4.12/cli_reference/index.html) command to install the [CustomResourceDefinitions](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/) for 
   MongoDB deployments:

   ```sh
   oc apply -f crds.yaml
   ```

#. Add your `<openshift-pull-secret>` to the `ServiceAccount`
   definitions in the MongoDB Controllers for Kubernetes Operator YAML (Yet Another Markup Language) file.

   ```yaml
   ---
   apiVersion: v1
   kind: ServiceAccount
   metadata:
     name: enterprise-operator

     namespace: mongodb

   imagePullSecrets:
    - name: <openshift-pull-secret>

   ---
   apiVersion: v1
   kind: ServiceAccount
   metadata:
     name: mongodb-kubernetes-appdb

     namespace: mongodb

   imagePullSecrets:
    - name: <openshift-pull-secret>

   ---
   apiVersion: v1
   kind: ServiceAccount
   metadata:
     name: mongodb-kubernetes-database-pods

     namespace: mongodb

   imagePullSecrets:
    - name: <openshift-pull-secret>
   ```

#. Invoke the following [oc](https://docs.openshift.com/container-platform/4.12/cli_reference/index.html) command to install Kubernetes Operator:

   ```sh
   oc apply -f mongodb-kubernetes-openshift.yaml
   ```

**Step 6: Create credentials and store them as a secret.**

Run the following command:

**Note:**

Provide your Public and Private Key values for the following 
parameters. To learn more, see create-k8s-credentials.

```sh
kubectl -n mongodb \
  create secret generic ops-manager-admin-key \
  --from-literal="publicKey=<publicKey>" \
  --from-literal="privateKey=<privateKey>"
```

**Step 7: Invoke the following command to create a ConfigMap.**

```sh
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-project
  namespace: mongodb
data:
  projectName: myProjectName # this is an optional parameter; when omitted, the Operator creates a project with the resource name
  orgId: 5b890e0feacf0b76ff3e7183 # this is a required parameter
  baseUrl: https://ops.example.com:8443

EOF
```

| Key | Type | Description | Example |
|---|---|---|---|
| `metadata.name` | string | Name of the Kubernetes [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/). Resource names must be 44 characters or less. This name must follow RFC1123 naming conventions, containing only lowercase alphanumeric characters or `-` , and starting and ending with an alphanumeric character. To learn more, see Kubernetes documentation on [names](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/). | `my-project` |
| `metadata.namespace` | string | Kubernetes [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) where the Kubernetes Operator creates this `MongoDB` resource and other [objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/). | `mongodb` |
| `data.projectName` | string | Label for your `Ops Manager` `Project`. The Kubernetes Operator creates the `Ops Manager` project if it does not exist. If you omit the `projectName`, the Kubernetes Operator creates a project with the same name as your Kubernetes resource. To use an existing project in a Cloud Manager or Ops Manager organization, locate the `projectName` by clicking the All Clusters link at the top left of the Cloud Manager or Ops Manager page, and searching by name in the Search box, or scrolling to find the name in the list. Each card in this list represents the combination of one Cloud Manager or Ops Manager **Organization** and **Project**. | `myProjectName` |
| `data.orgId` | string | *Required*. 24 character hex string that uniquely identifies your Cloud Manager or Ops Manager `Organization`. You can use the Kubernetes Operator to deploy MongoDB resources with Cloud Manager and with Ops Manager version 6.0.x or later. You can use the Atlas Operator to deploy MongoDB resources to Atlas. Specify an `existing Organization`: a. Find the organization's ID. Click Settings in the left navigation bar. #. Copy and paste the orgId into the URL. Select your organization, view the current URL (Uniform Resource Locator) in your browser and copy the value displayed in the `<orgId>` placeholder as follows: `https://ops.example.com:8443/` `v2#/org/<orgId>/projects` You must have the `Organization Project Creator` role to create a new project within an existing Cloud Manager or Ops Manager organization. If you provide an empty string as your `orgId`, Kubernetes Operator creates an organization with the same name as your project. | `5b890e0feacf0b76ff3e7183` |
| `data.baseUrl` | string | URL (Uniform Resource Locator) to your Ops Manager Application including the FQDN (fully qualified domain name) and port number. IMPORTANT: If you deploy Ops Manager with the Kubernetes Operator and Ops Manager will manage MongoDB database resources deployed **outside** of the Kubernetes cluster it's deployed to, you must set `data.baseUrl` to the same value of the `spec.configuration.mms.centralUrl` setting in the Ops Manager resource specification. To learn more, see mdb-resource-deployment-locations. If you're using Cloud Manager, set the `data.baseUrl` value to `https://cloud.mongodb.com`. | `https://ops.example.com:8443` |

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
