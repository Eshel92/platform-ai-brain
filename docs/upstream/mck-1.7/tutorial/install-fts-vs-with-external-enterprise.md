<!-- Converted from tutorial/install-fts-vs-with-external-enterprise.txt (reStructuredText). Includes are inlined. -->

:noprevnext:

# Install and Use MongoDB Search and Vector Search With External MongoDB Enterprise Edition

You can use the Kubernetes Operator to deploy MongoDB Search and
Vector Search on a Kubernetes cluster to run with an external
MongoDB Enterprise Edition v8.2.0 or higher server. This procedure
demonstrates how to deploy and configure the `mongot` process in your
Kubernetes cluster to use a new or existing external replica set deployment.
This tutorial demonstrates how to configure a secure deployment with
TLS (Transport Layer Security) enabled. You must provide the TLS (Transport Layer Security) certificates: 

- The server certificate and key for the MongoDBSearch service.
- The public CA certificate for the external MongoDB database.

## Prerequisites

To deploy MongoDB Search and Vector Search, you must have the
following:

- A running Kubernetes cluster with `kubeconfig` available locally.
- Kubernetes command-line tool, `kubectl`, configured to communicate with
  your cluster.
- [Helm](https://helm.sh/), the package manager for Kubernetes, to install the Kubernetes Operator.
- Bash v5.1 or higher for running the commands in this tutorial.
- A MongoDB Enterprise Edition replica set running version 8.2 or
  higher for storing data.

  **Important:**

  The version format for the Enterprise edition would be
  `X.Y.Z-ent`. Ensure that you choose `v8.2.0` or higher. To learn
  more about MongoDB versioning, see release-version-numbers
  in the MongoDB Manual. 

  To learn more about deploying MongoDB Enterprise, see
  mdb-resources.

- A running MongoDB Cloud Manager or Ops Manager for managing MongoDB tasks.

- External DB TLS (Transport Layer Security) 
 
  Your external MongoDB Enterprise deployment must be configured to use
  and require TLS (Transport Layer Security) connections.
  
- External DB CA file
  
  You must have the public Certificate Authority (CA) certificate file
  (for example, `external-ca.crt`) that was used to sign your external
  MongoDB deployment's server certificates. You will need this file
  locally.

- Search Service certificate files
 
  You must have a valid TLS (Transport Layer Security) server certificate and private key (for
  example, `search-service.crt`, `search-service.key`) for the
  MongoDBSearch service. This certificate must be valid for the hostname
  you will use to access the service (for example,
  `mdbs-search.example.com`). 

## Before You Begin

Before you install MongoDB Search and Vector Search using the
Kubernetes Operator, you must do the following:

- k8s-search-set-parameters
- k8s-search-create-role-user
- k8s-search-set-env-for-external_mdb

### Configure Cloud Manager or Ops Manager Parameters for MongoDB Search and Vector Search

Log in to the Cloud Manager or Ops Manager UI and perform the following steps to configure
Cloud Manager or Ops Manager for MongoDB Search and Vector Search.

**Step 1: Go to your Cloud Manager or Ops Manager Deployment page.**

a. Log in to MongoDB Cloud Manager or Ops Manager.
#. Click the Deployment tab.
#. Select the cluster that you want to modify.

**Step 2: Modify your Cloud Manager or Ops Manager deployment configuration.**

a. Click the Modify button to open the deployment
   configuration editor.
#. Click Advanced Configuration Options under the
   Process Configuration section.
#. Click the Add Option button and select
   setParameter Startup Option from the dropdown.
#. Add the following parameters in the fields, one by one, by
   clicking Add after adding the name and value:

   | Parameter | Value |
   |---|---|
   | `mongotHost` | Your search hostname and port. For example: `search-node1.example.com:27017`. |
   | `searchIndexManagementHostAndPort` | Your search hostname and port. For example: `search-node1.example.com:27017`. |
   | `skipAuthenticationToSearchIndexManagementServer` | `false` |
   | `searchTLSMode` | Your configured TLS mode. For example, `preferTLS`, if the `mongot` process is configured to accept TLS connections. |
   | `useGrpcForSearch` | `true` |

**Step 3: Review and deploy your changes.**

a. Click the Review & Deploy button.
#. Review and confirm to apply the changes.

   Cloud Manager or Ops Manager performs a rolling restart of your replica set to
   apply the new configuration.

### Configure a Cloud Manager or Ops Manager User for MongoDB Search and Vector Search

You must create a user with the `searchCoordinator` role. In MongoDB
versions 8.2 and later, the `searchCoordinator` is a built-in role. You must
create a user and assign the role to the user. 

To create the user and assign the user the built-in
`searchCoordinator` role, complete the following steps by using either
the Cloud Manager or Ops Manager UI or the `mongosh`:

**ui:**

**Step 1: Go to the Users page.**

a. Log in to Cloud Manager or Ops Manager UI.
#. Go to the Security tab and click on
   Users.

**Step 2: Click Add New User.**

**Step 3: Set the credentials for the user.**

|  |  |
|---|---|
| Username | Enter `search-sync-source`. |
| Password | Set a strong, secure password. |
| Authentication Database | Choose the `admin` database. |

**Step 4: Assign the `searchCoordinator` role to the user.**

In the Assign Roles section, select the built-in
`searchCoordinator` role from the dropdown for the
`admin` database.

**Step 5: Click Add User to create the user with the `searchCoordinator` role.**

**mongosh:**

In `mongosh`, run the following commands:

**Step 1: Switch to the `admin` database.**

```javascript
use admin;
```

**Step 2: Run the following command after replacing the password with a secure password to create the user.**

```javascript
db.createUser({
   user: "search-sync-source",
   pwd: "<PASSWORD>", // Replace with your actual password
   roles: [
      { role: "searchCoordinator", db: "admin" }
   ]
});
```

### Setup Your Environment

Prepare your environment for running the sample code in this tutorial in
a terminal.

**Step 1: Required. Set the environment variables.**

To set the environment variables for use in the subsequent steps
in this procedure, copy the following, set the values for the
environment variables, and then run the commands in your terminal:

```yaml
export K8S_CTX="<your kubernetes context here>"

export MDB_NS="mongodb"

export MDB_VERSION="8.2.0"

export MDB_ADMIN_USER_PASSWORD="admin-user-password-CHANGE-ME"
export MDB_USER_PASSWORD="mdb-user-password-CHANGE-ME"
export MDB_SEARCH_SYNC_USER_PASSWORD="search-sync-user-password-CHANGE-ME"

export MDB_TLS_CA_SECRET_NAME="ca"
export MDB_SEARCH_TLS_SECRET_NAME="mdbs-search-tls"

export MDB_SEARCH_SERVICE_NAME="mdbs-search"
export MDB_SEARCH_HOSTNAME="mdbs-search.example.com"

# External MongoDB replica set members - REPLACE THESE VALUES with your actual external MongoDB hosts
# In production, replace with your actual external MongoDB replica set members
export MDB_EXTERNAL_HOST_0="mdbc-rs-0.mdbc-rs-svc.${MDB_NS}.svc.cluster.local:27017"
export MDB_EXTERNAL_HOST_1="mdbc-rs-1.mdbc-rs-svc.${MDB_NS}.svc.cluster.local:27017"
export MDB_EXTERNAL_HOST_2="mdbc-rs-2.mdbc-rs-svc.${MDB_NS}.svc.cluster.local:27017"

# REPLACE with your actual external MongoDB replica set name
export MDB_EXTERNAL_REPLICA_SET_NAME="mdbc-rs"

export OPERATOR_HELM_CHART="mongodb/mongodb-kubernetes"
export OPERATOR_ADDITIONAL_HELM_VALUES=""

export MDB_CONNECTION_STRING="mongodb://mdb-user:${MDB_USER_PASSWORD}@${MDB_EXTERNAL_HOST_0}/?replicaSet=${MDB_EXTERNAL_REPLICA_SET_NAME}&tls=true&tlsCAFile=/tls/ca.crt"
```

Note that these environment variables are only available in
the current terminal session and will need to be set again in any
new terminal sessions.

**Step 2: Conditional. Add the MongoDB [Helm](https://helm.sh/) repository.**

[Helm](https://helm.sh/) automates the deployment and management of MongoDB
instances on Kubernetes. If you have already added the [Helm](https://helm.sh/)
repository that contains the [Helm](https://helm.sh/) chart for installing the
Kubernetes Operator operator, skip this step. Otherwise, add the
[Helm](https://helm.sh/) repository.

To add, copy, paste, and run the following command:

```shell
```

Output:

```shell
```

**Step 3: Conditional. Install the MongoDB Controllers for Kubernetes Operator.**

The Kubernetes Operator watches `MongoDB`, `MongoDBOpsManager`, and
MongoDBSearch custom resources and manages the lifecycle of
your MongoDB deployments. If you already installed the MongoDB Controllers for Kubernetes Operator,
skip this step. Otherwise, install the MongoDB Controllers for Kubernetes Operator from the [Helm](https://helm.sh/)
repository you added in the previous step.

To install the MongoDB Controllers for Kubernetes Operator in the `mongodb` namespace, copy, paste,
and run the following:

```shell
```

Output:

```shell
```

The preceding command installs Kubernetes Operator in the `mongodb`
namespace, which it creates if it doesn't already exist. After
installation, the Kubernetes Operator watches for MongoDBSearch
custom resources and manage the lifecycle of your MongoDB Search and
Vector Search deployments.

## Install MongoDB Search and Vector Search

**Step 1: Required. Create and load the MongoDB user secrets.**

The `mongot` process requires authentication credentials to
connect to your external MongoDB deployment for creating search
indexes and running search queries. This step creates the
following Kubernetes secrets:

- `mdb-admin-user-password` - credentials for the MongoDB administrator.
- `mdb-user-password` - credentials for the user authorized to perform search queries.
- `mdbc-rs-search-sync-source-password` - credentials for a
  dedicated search user used internally by the `mongot` process
  to synchronize data and manage indexes.

Kubernetes Operator mounts these secrets into the MongoDB pods.

To create the secrets, copy, paste, and run the following in the
namespace where you plan to deploy MongoDB Search and
Vector Search:

```shell
```

Output:

```
secret/mdb-admin-user-password created
secret/mdbc-rs-search-sync-source-password created
secret/mdb-user-password created
```

**Step 2: Required. Create and deploy the resource for MongoDB Search and Vector Search.**

You can deploy one instance of the search node without any load
balancing. To deploy, complete the following steps:

a. Create a MongoDBSearch custom resource named `mdbs`.

   This resource contains the following:

   |  |  |
   |---|---|
   | `spec.source.external.hostAndPorts` | List of external MongoDB replica set members. |
   | `spec.source.username` | Search synchronization user username. |
   | `spec.source.passwordSecretRef` | Search synchronization user password. |
   | `spec.source.external.tls.ca.name` | Configures MongoDBSearch pods to trust the external database. It points to the Kubernetes secret that contains the public CA certificate for your external MongoDB. |
   | `spec.security.tls.certificateKeySecretRef.name` | Secures the MongoDBSearch service. It points to the Kubernetes secret containing the TLS (Transport Layer Security) server certificate and private key that the MongoDBSearch pods will present to incoming clients. |
   | `spec.resourceRequirements` | CPU and memory resource requirements for the search container. |

   To learn more about the settings in this custom resource, see
   k8s-fts-vs-settings.

   ```shell
   kubectl apply --context "${K8S_CTX}" -n "${MDB_NS}" -f - <<EOF
   apiVersion: mongodb.com/v1
   kind: MongoDBSearch
   metadata:
     name: ${MDB_SEARCH_RESOURCE_NAME:-mdbs}
   spec:
     source:
       external:
         hostAndPorts:
           - ${MDB_EXTERNAL_HOST_0}
           - ${MDB_EXTERNAL_HOST_1}
           - ${MDB_EXTERNAL_HOST_2}
         tls:
           ca:
             name: ${MDB_TLS_CA_SECRET_NAME}
       username: search-sync-source
       passwordSecretRef:
         name: ${MDB_RESOURCE_NAME}-search-sync-source-password
         key: password
     security:
       tls:
         certificateKeySecretRef:
           name: ${MDB_SEARCH_TLS_SECRET_NAME}
     resourceRequirements:
       limits:
         cpu: "3"
         memory: 5Gi
       requests:
         cpu: "2"
         memory: 3Gi
   EOF
   ```

#. Wait for the MongoDBSearch resource deployment to
   complete.

   When you apply the MongoDBSearch custom resource, the
   Kubernetes operator begins deploying the search nodes (pods). This
   step pauses the execution until the `mdbs` resource's
   status phase is `Running`, which indicates that the
   MongoDB Search StatefulSet is operational.

   ```shell
   echo "Waiting for MongoDBSearch resource to reach Running phase..."

   kubectl --context "${K8S_CTX}" -n "${MDB_NS}" wait --for=jsonpath='{.status.phase}'=Running mdbs/"${MDB_SEARCH_RESOURCE_NAME:-mdbs}" --timeout=300s
   ```

**Step 3: Required. Configure external access for MongoDB Search and Vector Search.**

To enable your external MongoDB instances to connect to the search
service, you must configure external access for MongoDB Search and
Vector Search. You can create a LoadBalancer Service that
exposes the search pods outside the Kubernetes cluster. 

This following service exposes the MongoDBSearch service on
port 27028 with an external IP address or hostname that can be
accessed from outside the Kubernetes cluster.

```javascript
kubectl apply --context "${K8S_CTX}" -n "${MDB_NS}" -f - <<YAML
apiVersion: v1
kind: Service
metadata:
  name: ${MDB_SEARCH_SERVICE_NAME}
spec:
  type: LoadBalancer
  selector:
    app: ${MDB_SEARCH_RESOURCE_NAME:-mdbs}-search-svc
  ports:
    - name: mongot
      port: 27028
      targetPort: 27028
YAML

echo "Waiting for external IP to be assigned to service ${MDB_SEARCH_SERVICE_NAME}..."
TIMEOUT=120  # 2 minutes timeout
ELAPSED=0
while [ ${ELAPSED} -lt ${TIMEOUT} ]; do
  EXTERNAL_IP=$(kubectl get service "${MDB_SEARCH_SERVICE_NAME}" --context "${K8S_CTX}" -n "${MDB_NS}" -o jsonpath='{.status.loadBalancer.ingress[0].ip}' 2>/dev/null)
  if [ -n "${EXTERNAL_IP}" ] && [ "${EXTERNAL_IP}" != "null" ]; then
    echo "External IP assigned: ${EXTERNAL_IP}"
    break
  fi
  echo "Still waiting for external IP assignment... (${ELAPSED}s/${TIMEOUT}s)"
  sleep 5
  ELAPSED=$((ELAPSED + 5))
done

if [ ${ELAPSED} -ge ${TIMEOUT} ]; then
  echo "ERROR: Timeout reached (${TIMEOUT}s) while waiting for external IP assignment"
  echo "LoadBalancer service may take longer to provision or there may be an issue"
  exit 1
fi
```

**Step 4: Optional. View all the running pods in your namespace.**

View all the running pods in your namespace pods for the MongoDB
replica set members, the MongoDB Controllers for Kubernetes Operator, and the Search nodes.

```shell
```

Output:

```shell
```

## Next Steps

Now that you've successfully deployed MongoDB Search and Vector Search
to use with external MongoDB Enterprise Edition, you can add data into
your MongoDB cluster, create MongoDB Search and Vector Search indexes,
and run queries against your data. To learn more, see
k8s-fts-vs-settings.
