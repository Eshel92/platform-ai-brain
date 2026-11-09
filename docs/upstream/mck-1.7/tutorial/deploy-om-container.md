<!-- Converted from tutorial/deploy-om-container.txt (reStructuredText). Includes are inlined. -->

:noprevnext:

# Deploy an Ops Manager Resource

You can deploy Ops Manager as a resource in a Kubernetes container using the Kubernetes Operator.

## Considerations

The following considerations apply:

### Encrypting Connections

When you configure your Ops Manager deployment, you must choose whether to run connections over HTTPS (Hypertext Transfer Protocol Secure) or HTTP (Hypertext Transfer Protocol).

The following HTTPS (Hypertext Transfer Protocol Secure) procedure:
 
- Establishes TLS (Transport Layer Security)-encrypted connections to/from the Ops Manager
  application.
- Establishes TLS (Transport Layer Security)-encrypted connections between the application
  database's replica set members.
- Requires valid certificates for TLS (Transport Layer Security) encryption.

The following HTTP (Hypertext Transfer Protocol) procedure: 

- Doesn't encrypt connections to or from the Ops Manager application.
- Doesn't encrypt connections between the
  application database's replica set members.
- Has fewer setup requirements.

When running over HTTPS (Hypertext Transfer Protocol Secure), Ops Manager runs on port `8443` by
default.

Select the appropriate tab based on whether you want to encrypt
your Ops Manager and application database connections with TLS (Transport Layer Security).

#### Prerequisites

**https:**

- Complete the Prerequisites.
- Read the Considerations.
- Create one TLS (Transport Layer Security) certificate for the Application
  Database's replica set.

  This TLS (Transport Layer Security) certificate requires the following attributes:

  * - DNS Names
    - Ensure that you add SAN (Subject Alternative Name)\s or Subject Names
      for each [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/) that hosts a member of the 
      Application Database replica set. The SAN (Subject Alternative Name) for each pod
      must use the following format:

      ```sh
      <opsmgr-metadata.name>-db-<index>.<opsmgr-metadata.name>-db-svc.<namespace>.svc.cluster.local
      ```

  * - Key Usages
    - Ensure that the TLS (Transport Layer Security) certificates include the following
      key-usages (5280):

      - "server auth"
      - "client auth"

**Important:**

The Kubernetes Operator uses `kubernetes.io/tls` secrets
to store TLS (Transport Layer Security) certificates and private keys for Ops Manager and MongoDB
resources. Starting in Kubernetes Operator version 1.17.0, the 
Kubernetes Operator doesn't support concatenated PEM (Privacy-Enhanced Mail) files stored as
`Opaque secrets`.

**http:**

Before you deploy an Ops Manager resource, make sure you plan for
your Ops Manager resource:

- Complete the Prerequisites
- Read the Considerations.

## Procedure

This procedure applies to deploying an Ops Manager instance in a single
Kubernetes cluster, and to deploying Ops Manager on a central cluster in a multi-cluster
deployment.
If you want to deploy multiple instances of Ops Manager on multiple Kubernetes clusters,
see deploy-om-multi-cluster.

**https:**

Follow these steps to deploy the Ops Manager resource to run over 
HTTPS (Hypertext Transfer Protocol Secure) and secure the application database using TLS (Transport Layer Security).

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

**Step 2: Create secrets for your certificates.**

If you're using [HashiCorp Vault](https://www.vaultproject.io/) as your secret storage tool, 
you can Create a Vault Secret instead.
To learn about your options for secret
storage, see Configure Secret Storage.

a. Once you have your TLS (Transport Layer Security) certificates and private keys, run the 
   following command to create a [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that stores Ops Manager\'s
   TLS (Transport Layer Security) certificate:

   ```sh
   kubectl create secret tls <prefix>-<metadata.name>-cert \
     --cert=<om-tls-cert> \
     --key=<om-tls-key>
   ```

b. Run the following command to create a new [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that stores
   the application database's TLS (Transport Layer Security) certificate:

   ```sh
   kubectl create secret tls <prefix>-<metadata.name>-db-cert \
     --cert=<appdb-tls-cert> \
     --key=<appdb-tls-key>
   ```

**Step 3: Add additional certificates to custom CA (Certificate Authority) certificates.**

If your Ops Manager TLS (Transport Layer Security) certificate is signed by a custom CA (Certificate Authority), 
the CA (Certificate Authority) certificate must also contain
additional certificates that allow Ops Manager Backup Daemon to download
MongoDB binaries from the Internet. To create the TLS (Transport Layer Security)
certificate(s), create a [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) to hold the CA (Certificate Authority)
certificate: 

**Important:**

The Kubernetes Operator requires that your Ops Manager certificate is named
`mms-ca.crt` in the ConfigMap. 

a. Obtain the entire TLS (Transport Layer Security) certificate chain for Ops Manager from
   `downloads.mongodb.com`. The following `openssl` command
   outputs the certificate in the chain to your current working
   directory, in `.crt` format:

   ```sh
   openssl s_client -showcerts -verify 2 \
   -connect downloads.mongodb.com:443 -servername downloads.mongodb.com < /dev/null \
   | awk '/BEGIN/,/END/{ if(/BEGIN/){a++}; out="cert"a".crt"; print >out}'
   ```

#. Concatenate your CA (Certificate Authority)\'s certificate file for Ops Manager
   with the entire TLS (Transport Layer Security) certificate chain from 
   `downloads.mongodb.com` that
   you obtained in the previous step:

   ```sh
   cat <custom_ca_cert.pem> cert2.crt cert3.crt cert4.crt  >> mms-ca.crt
   ```

   **Note:**

   - Replace the placeholder `<custom_ca_cert.pem>` with your custom CA certificate PEM file. 
   - Don't include your `cert1.crt` file, as it is your server certificate from 
     MongoDB that shouldn't be included.

#. Create the [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) for Ops Manager:

   ```sh
   kubectl create configmap om-http-cert-ca --from-file="mms-ca.crt"
   ```

**Step 4: Copy one of the following Ops Manager Kubernetes [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) examples.**

Change the settings to match your Ops Manager and application database configuration.

**Single Kubernetes Cluster:**

```yaml
---
apiVersion: mongodb.com/v1
kind: MongoDBOpsManager
metadata:
  name: <myopsmanager>
spec:
  replicas: 1
  version: <opsmanagerversion>
  adminCredentials: <adminusercredentials> # Should match metadata.name
                                           # in the Kubernetes secret
                                           # for the admin user

  externalConnectivity:
    type: LoadBalancer
  security:
      certsSecretPrefix: <prefix> # Required. Text to prefix 
                                  # the name of the secret that contains
                                  # Ops Manager's TLS certificate.
      tls:
        ca: "om-http-cert-ca"  # Optional. Name of the ConfigMap file
                               # containing the certificate authority that
                               # signs the certificates used by the Ops
                               # Manager custom resource.

  applicationDatabase:
    topology: SingleCluster
    members: 3
    version: "8.0.0-ubi8"
    security:
      certsSecretPrefix: <prefix> # Required. Text to prefix to the 
                                  # name of the secret that contains the Application
                                  # Database's TLS certificate. Name the secret 
                                  # <prefix>-<metadata.name>-db-cert.
      tls:
        ca: "appdb-ca" # Optional, unless enabling TLS for :opsmgr:`Ops Manager </>`. 
                       # Name of the ConfigMap file
                       # containing the certicate authority that
                       # signs the certificates used by the
                       # application database.

...
```

**Multi-Kubernetes Cluster:**

```yaml
---
apiVersion: mongodb.com/v1
kind: MongoDBOpsManager
metadata:
  name: <myopsmanager>
spec:
  replicas: 1
  version: <opsmanagerversion>
  adminCredentials: <adminusercredentials> # Should match metadata.name
                                           # in the Kubernetes secret
                                           # for the admin user

  externalConnectivity:
    type: LoadBalancer
  security:
      certsSecretPrefix: <prefix> # Required. Text to prefix 
                                  # the name of the secret that contains
                                  # Ops Manager's TLS certificate.
      tls:
        ca: "om-http-cert-ca"  # Optional. Name of the ConfigMap file
                               # containing the certificate authority that
                               # signs the certificates used by the Ops
                               # Manager custom resource.

  applicationDatabase:
    topology: MultiCluster
    clusterSpecList:
    - clusterName: cluster1.example.com
      members: 4
    - clusterName: cluster2.example.com
      members: 3
    - clusterName: cluster3.example.com
      members: 2
    version: "8.0.0-ubi8"
    security:
      certsSecretPrefix: <prefix> # Required. Text to prefix to the 
                                  # name of the secret that contains the Application
                                  # Database's TLS certificate. Name the secret 
                                  # <prefix>-<metadata.name>-db-cert.
      tls:
        ca: "appdb-ca" # Optional, unless enabling TLS for :opsmgr:`Ops Manager </>`. 
                       # Name of the ConfigMap file
                       # containing the certicate authority that
                       # signs the certificates used by the
                       # application database.

...
```

**Step 5: Open your preferred text editor and paste the [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification into a new text file.**

**Step 6: Configure the settings specific to your deployment.**

| Key | Type | Description | Example |
|---|---|---|---|
| `metadata.name` | string | Name for this Kubernetes Ops Manager [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/). Resource names must be 44 characters or less. See also `metadata.name` and Kubernetes documentation on `names`. | `om` |
| `spec.replicas` | number | Number of Ops Manager instances to run in parallel. The minimum valid value is `1`. This field is ignored if you specify `MultiCluster` in the `spec.topology` setting. | `1` |
| `spec.version` | string | Version of Ops Manager to be installed. The format should be X.Y.Z. To view available Ops Manager versions, view the [container registry](https://quay.io/repository/mongodb/mongodb-enterprise-ops-manager?tag=latest&tab=tags). | `8.0.0` |
| `spec.adminCredentials` | string | Name of the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) you created for the Ops Manager admin user. Configure the secret to use the same [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) as the Ops Manager resource. | `om-admin-secret` |
| \| `spec` \| `.security` \| `.``certsSecretPrefix` | string | *Required*. Text to prefix to the name of the secret that contains Ops Manager\s TLS (Transport Layer Security) certificates. | `om-prod` |
| \| `spec` \| `.security` \| `.tls` \| `.``ca` | string | Name of the [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) you created to verify your Ops Manager TLS (Transport Layer Security) certificates signed using a custom CA (Certificate Authority). This field is required if you signed your Ops Manager TLS (Transport Layer Security) certificates using a custom CA (Certificate Authority). | `om-http-cert-ca` |
| \| `spec` \| `.externalConnectivity` \| `.``type` | string | The Kubernetes service `ServiceType` that exposes Ops Manager outside of Kubernetes. Exclude the `spec.``externalConnectivity` setting and its children if you don't want the Kubernetes Operator to create a Kubernetes service to route external traffic to the Ops Manager application. | `LoadBalancer` |
| \| `spec` \| `.applicationDatabase` \| `.``members` | integer | Number of members of the mms-application-database replica set. | `3` |
| \| `spec` \| `.applicationDatabase` \| `.``version` | string | *Required*. Version of MongoDB that the mms-application-database should run. The format should be `X.Y.Z-ubi8` for the `Enterprise edition` and `X.Y.Z` for the Community edition. Do not add the `-ubi8` tag suffix to the Community edition image because the Kubernetes Operator adds the tag suffix automatically. IMPORTANT: Ensure that you choose a compatible MongoDB Server version. Compatible versions differ depending on the base image that the MongoDB database resource uses. To learn more about MongoDB versioning, see release-version-numbers in the MongoDB Manual. | .. include:: /includes/facts/fact-which-appdb-version.rst |
| \| `spec` \| `.applicationDatabase` \| `.``topology` | string | *Optional*. The type of the Kubernetes deployment for the Application Database. If omitted, the default is `SingleCluster`. If you specify `MultiCluster`, the Kubernetes Operator ignores values that you set for the `spec.applicationDatabase.members` field, if specified. Instead, you must specify the `clusterSpecList` and include in it the `clusterName` of each selected Kubernetes member cluster on which you want to deploy the Application Database, and the number of `members` (MongoDB nodes) in each Kubernetes cluster. You can't convert a single cluster Ops Manager instance to a multi-Kubernetes cluster MongoDB deployment instance by modifying the `topology` and the `clusterSpecList` settings in the CRD. See also the example of the resource specification. | `MultiCluster` |
| \| `spec` \| `.applicationDatabase` \| `.security` \| `.``certsSecretPrefix` | string | *Required*. Text to prefix to the name of the secret that contains the application database's TLS (Transport Layer Security) certificates. | `appdb-prod` |
| \| `spec` \| `.applicationDatabase` \| `.security` \| `.tls` \| `.``ca` | string | Name of the [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) you created to verify your application database TLS (Transport Layer Security) certificates signed using a custom CA (Certificate Authority). This field is required if you signed your application database TLS (Transport Layer Security) certificates using a custom CA (Certificate Authority). | `ca` The Kubernetes Operator mounts the CA (Certificate Authority) you add using the `spec.applicationDatabase.security.tls.ca` setting to both the Ops Manager and the Application Database Pods. |

**Step 7: Configure Backup settings.**

To configure backup, you must enable it, and then:

- Choose to configure an S3 snapshot store
  or a blockstore. If you deploy
  both an S3 (Simple Storage Service) snapshot store and a
  blockstore, Ops Manager 
  randomly choses one to use for backup.

- Choose to configure an oplog store or an S3 (Simple Storage Service) oplog store.
  If you deploy both an oplog store and an S3 (Simple Storage Service) oplog store, Ops Manager
  randomly choses one of them to use for the oplog backup.

| Key | Type | Description | Example |
|---|---|---|---|
| \| `spec` \| `.backup` \| `.``enabled` | boolean | Flag that indicates that Backup is enabled. You must specify `spec.backup.enabled: true` to configure settings for the head database, oplog store, and snapshot store. | `true` |
| \| `spec` \| `.backup` \| `.headDB` | collection | A collection of configuration settings for the head database. For descriptions of the individual settings in the collection, see `spec.backup.headDB`. |  |
| \| `spec` \| `.backup` \| `.opLogStores` \| `.``name` | string | Name of the oplog store. | `oplog1` |
| \| `spec` \| `.backup` \| `.s3OpLogStores` \| `.``name` | string | Name of the S3 (Simple Storage Service) oplog store. | `my-s3-oplog-store` |
| \| `spec` \| `.backup` \| `.opLogStores` \| `.mongodbResourceRef` \| `.``name` | string | Name of the `MongoDB` resource or `MongoDBMultiCluster` resource for the oplog store. The resource's `metadata.name` must match this name. | `my-oplog-db` |
| \| `spec` \| `.backup` \| `.s3OpLogStores` \| `.mongodbResourceRef` \| `.``name` | string | Name of the `MongoDB` resource or `MongoDBMultiCluster` resource for the S3 (Simple Storage Service) oplog store. The resource's `metadata.name` must match this name. | `my-s3-oplog-db` |

You must also configure an S3 snapshot store
or a blockstore.

If you deploy both an S3 snapshot store
and a blockstore, Ops Manager
randomly choses one to use for Backup.

To configure a snapshot store, configure the following settings:

| Key | Type | Description | Example |
|---|---|---|---|
| \| `spec` \| `.backup` \| `.s3Stores` \| `.``name` | string | Name of the S3 (Simple Storage Service) snapshot store. | `s3store1` |
| \| `spec` \| `.backup` \| `.s3Stores` \| `.s3SecretRef` \| `.``name` | string | Name of the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that contains the `accessKey` and `secretKey` fields. The backup-daemon uses the values of these fields as credentials to access the S3 (Simple Storage Service) or S3 (Simple Storage Service)-compatible bucket. | `my-s3-credentials` |
| \| `spec` \| `.backup` \| `.s3Stores` \| `.``s3BucketEndpoint` | string | URL (Uniform Resource Locator) of the S3 (Simple Storage Service) or S3 (Simple Storage Service)-compatible bucket that `stores` the database Backup snapshots. | `s3.us-east-1.amazonaws.com` |
| \| `spec` \| `.backup` \| `.s3Stores` \| `.``s3BucketName` | string | Name of the S3 (Simple Storage Service) or S3 (Simple Storage Service)-compatible bucket that stores the database Backup snapshots. | `my-bucket` |

To configure a blockstore, configure the following settings:

| Key | Type | Description | Example |
|---|---|---|---|
| \| `spec` \| `.backup` \| `.blockStores` \| `.``name` | string | Name of the blockstore. | `blockStore1` |
| \| `spec` \| `.backup` \| `.blockStores` \| `.mongodbResourceRef` \| `.``name` | string | Name of the `MongoDB` resource that you create for the blockstore. You must deploy this database resource in the same namespace as the Ops Manager resource. | `my-mongodb-blockstore` |

**Step 8: Configure any additional settings for an Ops Manager backup.**

Add any optional settings for backups
that you want to apply to your deployment to the [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification
file. For example, for each type of backup store, and for Ops Manager backup
daemon processes, you can assign labels to associate particular backup
stores or backup daemon processes with specific projects.
Use `spec.backup.[*].assignmentLabels` elements of the OpsManager
resources.

**Step 9: Configure any additional settings for an Ops Manager deployment.**

Add any optional settings that you
want to apply to your deployment to the [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification file.

**Step 10: Save this file with a `.yaml` file extension.**

**Step 11: Create your Ops Manager instance.**

Run the following `kubectl` command on the filename of the
Ops Manager resource definition:

```sh
kubectl apply -f <opsmgr-resource>.yaml
```

**Note:**

If you are deploying an Ops Manager resource on a multi-Kubernetes cluster MongoDB deployment, run:

```sh
kubectl apply \
  --context "$MDB_CENTRAL_CLUSTER_FULL_NAME" \
  --namespace "mongodb" 
   -f https://raw.githubusercontent.com/mongodb/mongodb-kubernetes/1.7.0/public/samples/ops-manager/ops-manager-external.yaml
```

**Step 12: Track the status of your Ops Manager instance.**

To check the status of your Ops Manager resource, invoke the following
command:

```sh
kubectl get om -o yaml -w
```

The command returns the output similar to the following under the `status`
field while the resource deploys:

```yaml
status:
 applicationDatabase:
  lastTransition: "2022-04-01T09:49:22Z"
  message: AppDB Statefulset is not ready yet
  phase: Pending
  type: ""
  version: ""
 backup:
  phase: ""
 opsManager:
  phase: ""
```

The Kubernetes Operator reconciles the resources in the following order:

1. Application Database.
#. Ops Manager.
#. Backup.

The Kubernetes Operator doesn't reconcile a resource until the preceding
one enters the `Running` phase.

After the Ops Manager resource completes the `Pending` phase, the
command returns output similar to the following under the `status`
field if you enabled Backup:

```yaml
status:
 applicationDatabase:
     lastTransition: "2022-04-01T09:50:20Z"
     members: 3
     phase: Running
     type: ReplicaSet
     version: "8.0.0-ubi8"
  backup:
   lastTransition: "2022-04-01T09:57:42Z"
   message: The MongoDB object <namespace>/<oplogresourcename>
     doesn't exist
   phase: Pending
   opsManager:
     lastTransition: "2023-04-01T09:57:40Z"
     phase: Running
     replicas: 1
     url: https://om-svc.cloudqa.svc.cluster.local:8443
     version: "8.0.0"
```

Backup remains in a `Pending` state until you configure the Backup
databases.

**Tip:**

The `status.opsManager.url` field states the resource's
connection URL (Uniform Resource Locator). Using this URL (Uniform Resource Locator), you can reach Ops Manager from
inside the Kubernetes cluster or create a project using a
ConfigMap.

After the resource completes the `Pending` phase, the command
returns output similar to the following under the `status` field:

```yaml
status:
  applicationDatabase:
     lastTransition: "2022-12-06T18:23:22Z"
     members: 3
     phase: Running
     type: ReplicaSet
     version: "8.0.0-ubi8"
   opsManager:
     lastTransition: "2022-12-06T18:23:26Z"
     message: The MongoDB object namespace/oplogdbname doesn't exist
     phase: Pending
     url: https://om-svc.dev.svc.cluster.local:8443
     version: ""
```

Backup remains in a `Pending` state until you configure the Backup
databases.

**Tip:**

The `status.opsManager.url` field states the resource's
connection URL (Uniform Resource Locator). Using this URL (Uniform Resource Locator), you can reach Ops Manager from
inside the Kubernetes cluster or create a project using a
ConfigMap.

**Step 13: Access the Ops Manager application.**

The steps you take differ based on how you are routing traffic to the
Ops Manager application in Kubernetes. If you configured the Kubernetes Operator to
create a Kubernetes service for you, or you created a Kubernetes service
manually, use one of the following methods to access the Ops Manager
application:

**LoadBalancer Service:**

a. Query your cloud provider to get the FQDN (fully qualified domain name) of the load
   balancer service. See your cloud provider's documentation
   for details.

#. Open a browser window and navigate to the Ops Manager
   application using the FQDN (fully qualified domain name) and port number of your load
   balancer service.

   ```sh
   https://ops.example.com:8443
   ```

#. Log in to Ops Manager using the admin user credentials.

**NodePort Service:**

a. Set your firewall rules to allow access from the Internet to
   the `spec.externalConnectivity.``port`
   on the host on which your Kubernetes cluster is running.

#. Open a browser window and navigate to the Ops Manager
   application using the FQDN (fully qualified domain name) and the
   `spec.externalConnectivity.``port`.

   ```sh
   https://ops.example.com:30036
   ```

#. Log in to Ops Manager using the admin user credentials.

To learn how to access the Ops Manager application using a third-party
service, refer to the documentation for your solution.

**Step 14: Create credentials for the Kubernetes Operator.**

To configure credentials, you must create an Ops Manager organization,
generate programmatic API keys, and create a [secret](https://kubernetes.io/docs/concepts/configuration/secret/). These
activities follow the prerequisites and procedure on the
create-k8s-credentials page.

**Step 15: Create a project using a [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/).**

To create a project, follow the prerequisites and procedure on the
create-k8s-project page.

Set the following fields in your project ConfigMap:

- Set `data.baseUrl` in the ConfigMap to the Ops Manager Application\'s URL (Uniform Resource Locator).
  To find this URL (Uniform Resource Locator), invoke the following command:

  ```sh
  kubectl get om -o yaml -w
  ```

  The command returns the URL of the Ops Manager Application in the
  `status.opsManager.url` field, similar to the following example:

  ```yaml
  status:
     applicationDatabase:
       lastTransition: "2022-12-06T18:23:22Z"
       members: 3
       phase: Running
       type: ReplicaSet
       version: "8.0.0-ubi8"
     opsManager:
       lastTransition: "2022-12-06T18:23:26Z"
       message: The MongoDB object namespace/oplogdbname doesn't exist
       phase: Pending
       url: https://om-svc.dev.svc.cluster.local:8443
       version: ""
  ```

  **Important:**

  If you deploy Ops Manager with the Kubernetes Operator and Ops Manager will 
  manage MongoDB database resources deployed **outside** of the Kubernetes 
  cluster it's deployed to, you must set `data.baseUrl` to the same 
  value of the 
  `spec.configuration.mms.centralUrl`
  setting in the Ops Manager resource specification.

  To learn more, see mdb-resource-deployment-locations.

- Set `data.sslMMSCAConfigMap` to the name of your
  [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) containing the root
  CA (Certificate Authority) certificate used to sign the
  Ops Manager host's certificate. The Kubernetes Operator requires that you name
  this Ops Manager resource's certificate `mms-ca.crt` in the ConfigMap.

**Step 16: Deploy MongoDB database resources to complete the backup configuration.**

By default, Ops Manager enables mms-backup-functional-overview.
Create a MongoDB database resource for the oplog and snapshot stores
to complete the configuration.

a. Deploy a MongoDB database resource for the oplog store in the same
   namespace as the Ops Manager resource.

   **Note:**

   Create this database as a three-member replica set.

   Match the `metadata.name` of the resource with the
   `spec.backup.opLogStores.mongodbResourceRef.name`
   that you specified in your Ops Manager resource definition.

#. Deploy a MongoDB database resource for the S3 (Simple Storage Service) snapshot store in the
   same namespace as the Ops Manager resource.

   **Note:**

   Create the S3 (Simple Storage Service) snapshot store as a replica set.

   Match the `metadata.name` of the resource to the
   `spec.backup.s3Stores.mongodbResourceRef.name`
   that you specified in your Ops Manager resource definition.

**Step 17: Confirm that the Ops Manager resource is running.**

To check the status of your Ops Manager resource, invoke the following
command:

```sh
kubectl get om -o yaml -w
```

When Ops Manager is running, the command returns the output similar to the
following, under the `status` field:

```yaml
status:
  applicationDatabase:
    lastTransition: "2022-12-06T17:46:15Z"
    members: 3
    phase: Running
    type: ReplicaSet
    version: "8.0.0-ubi8"
  opsManager:
    lastTransition: "2022-12-06T17:46:32Z"
    phase: Running
    replicas: 1
    url: https://om-backup-svc.dev.svc.cluster.local:8443
    version: "8.0.0"
```

See /reference/troubleshooting for information about the
resource deployment statuses.

**http:**

Follow these steps to deploy the Ops Manager resource to run over
HTTP (Hypertext Transfer Protocol):

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

**Step 2: Copy one of the following Ops Manager Kubernetes [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) examples.**

Change the settings to match your Ops Manager configuration.

**Single Kubernetes Cluster:**

```yaml
---
apiVersion: mongodb.com/v1
kind: MongoDBOpsManager
metadata:
  name: <myopsmanager>
spec:
  replicas: 1
  version: <opsmanagerversion>
  adminCredentials: <adminusercredentials> # Should match metadata.name
                                           # in the secret
                                           # for the admin user
  externalConnectivity:
    type: LoadBalancer

  applicationDatabase:
    topology: SingleCluster
    members: 3
    version: <mongodbversion>
...
```

**Multi-Kubernetes Cluster:**

```yaml
---
apiVersion: mongodb.com/v1
kind: MongoDBOpsManager
metadata:
  name: <myopsmanager>
spec:
  replicas: 1
  version: <opsmanagerversion>
  adminCredentials: <adminusercredentials> # Should match metadata.name
                                           # in the Kubernetes secret
                                           # for the admin user

  externalConnectivity:
    type: LoadBalancer

  applicationDatabase:
    topology: MultiCluster
    clusterSpecList:
    - clusterName: cluster1.example.com
      members: 4
    - clusterName: cluster2.example.com
      members: 3
    - clusterName: cluster3.example.com
      members: 2
    version: "8.0.0-ubi8"

...
```

**Step 3: Open your preferred text editor and paste the [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification into a new text file.**

**Step 4: Configure the settings included in the previous example.**

| Key | Type | Description | Example |
|---|---|---|---|
| `metadata.name` | string | Name for this Kubernetes Ops Manager [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/). Resource names must be 44 characters or less. To learn more, see `metadata.name`, and Kubernetes documentation on `names`. | `om` |
| `spec.replicas` | number | Number of Ops Manager instances to run in parallel. The minimum valid value is `1`. This field is ignored if you specify `MultiCluster` in the `spec.topology` setting. | `1` |
| `spec.version` | string | Version of Ops Manager to be installed. The format should be X.Y.Z. For the list of available Ops Manager versions, view the [container registry](https://quay.io/repository/mongodb/mongodb-enterprise-ops-manager?tag=latest&tab=tags). | `8.0.0` |
| `spec.adminCredentials` | string | Name of the secret you created for the Ops Manager admin user. Configure the secret to use the same [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) as the Ops Manager resource. | `om-admin-secret` |
| \| `spec` \| `.externalConnectivity` \| `.``type` | string | *Optional*. The Kubernetes service `ServiceType` that exposes Ops Manager outside of Kubernetes. Exclude the `spec.``externalConnectivity` setting and its children if you don't want the Kubernetes Operator to create a Kubernetes service to route external traffic to the Ops Manager application. | `LoadBalancer` |
| \| `spec` \| `.applicationDatabase` \| `.``members` | integer | Number of members of the mms-application-database replica set. | `3` |
| \| `spec` \| `.applicationDatabase` \| `.``version` | string | *Required*. Version of MongoDB that the mms-application-database should run. The format should be `X.Y.Z` for the Community edition and `X.Y.Z-ubi8` for the `Enterprise edition`. IMPORTANT: Ensure that you choose a compatible MongoDB Server version. Compatible versions differ depending on the base image that the MongoDB database resource uses. To learn more about MongoDB versioning, see release-version-numbers in the MongoDB Manual. | .. include:: /includes/facts/fact-which-appdb-version.rst |
| \| `spec` \| `.applicationDatabase` \| `.``topology` | string | *Optional*. The type of the Kubernetes deployment for the Application Database. If omitted, the default is `SingleCluster`. If you specify `MultiCluster`, the Kubernetes Operator ignores values that you set for the `spec.applicationDatabase.members` field, if specified. Instead, you must specify the `clusterSpecList` and include in it the `clusterName` of each selected Kubernetes member cluster on which you want to deploy the Application Database, and the number of `members` (MongoDB nodes) in each Kubernetes cluster. You can't convert a single cluster Ops Manager instance to a multi-Kubernetes cluster MongoDB deployment instance by modifying the `topology` and the `clusterSpecList` settings in the CRD. See also the example of the resource specification. | `MultiCluster` |

**Step 5: Configure backup settings.**

To configure backup, you must enable it, and then:

- Choose to configure an S3 snapshot store 
  or a blockstore. If you deploy
  both an S3 (Simple Storage Service) snapshot store and a
  blockstore, Ops Manager 
  randomly choses one to use for backup.

- Choose to configure an oplog store or an S3 (Simple Storage Service) oplog store.
  If you deploy both an oplog store and an S3 (Simple Storage Service) oplog store, Ops Manager
  randomly choses one of them to use for the oplog backup.

| Key | Type | Description | Example |
|---|---|---|---|
| \| `spec` \| `.backup` \| `.``enabled` | boolean | Flag that indicates that backup is enabled. You must specify `spec.backup.enabled: true` to configure settings for the head database, oplog store, S3 (Simple Storage Service) oplog store, and snapshot store. | `true` |
| \| `spec` \| `.backup` \| `.headDB` | collection | A collection of configuration settings for the head database. For descriptions of the individual settings in the collection, see `spec.backup.headDB`. |  |
| \| `spec` \| `.backup` \| `.opLogStores` \| `.``name` | string | Name of the oplog store. | `oplog1` |
| \| `spec` \| `.backup` \| `.s3OpLogStores` \| `.``name` | string | Name of the S3 (Simple Storage Service) oplog store. | `my-s3-oplog-store` |
| \| `spec` \| `.backup` \| `.opLogStores` \| `.mongodbResourceRef` \| `.``name` | string | Name of the `MongoDB` resource or `MongoDBMultiCluster` resource for the oplog store. The resource's `metadata.name` must match this name. | `my-oplog-db` |
| \| `spec` \| `.backup` \| `.s3OpLogStores` \| `.mongodbResourceRef` \| `.``name` | string | Name of the MongoDB database resource for the S3 (Simple Storage Service) oplog store. | `my-s3-oplog-db` |

You must also configure an S3 snapshot store
or a blockstore. If you deploy both
an S3 (Simple Storage Service) snapshot store and a
blockstore, Ops Manager randomly
choses one to use for backup.

To configure an S3 (Simple Storage Service) snapshot store, configure the following settings:

| Key | Type | Description | Example |
|---|---|---|---|
| \| `spec` \| `.backup` \| `.s3Stores` \| `.``name` | string | Name of the S3 (Simple Storage Service) snapshot store. | `s3store1` |
| \| `spec` \| `.backup` \| `.s3Stores` \| `.s3SecretRef` \| `.``name` | string | Name of the secret that contains the `accessKey` and `secretKey` fields. The backup-daemon uses the values of these fields as credentials to access the S3 (Simple Storage Service) or S3 (Simple Storage Service)-compatible bucket. | `my-s3-credentials` |
| \| `spec` \| `.backup` \| `.s3Stores` \| `.``s3BucketEndpoint` | string | URL (Uniform Resource Locator) of the S3 (Simple Storage Service) or S3 (Simple Storage Service)-compatible bucket that `stores` the database backup snapshots. | `s3.us-east-1.amazonaws.com` |
| \| `spec` \| `.backup` \| `.s3Stores` \| `.``s3BucketName` | string | Name of the S3 (Simple Storage Service) or S3 (Simple Storage Service)-compatible bucket that stores the database backup snapshots. | `my-bucket` |
| \| `spec` \| `.backup` \| `.s3Stores` \| `.``s3RegionOverride` | string | Region where your S3 (Simple Storage Service)-compatible bucket resides. Use this field only if your S3 (Simple Storage Service) store's `s3BucketEndpoint` doesn't include a region in its URL (Uniform Resource Locator). Don't use this field with AWS (Amazon Web Services) S3 (Simple Storage Service) buckets. | `us-east-1` |

To configure a blockstore, configure the following settings:

| Key | Type | Description | Example |
|---|---|---|---|
| \| `spec` \| `.backup` \| `.blockStores` \| `.``name` | string | Name of the blockstore. | `blockStore1` |
| \| `spec` \| `.backup` \| `.blockStores` \| `.mongodbResourceRef` \| `.``name` | string | Name of the `MongoDB` resource  that you create for the blockstore. You must deploy this database resource in the same namespace as the Ops Manager resource. The resource's `metadata.name` must match this name. | `my-mongodb-blockstore` |

**Step 6: Configure any additional settings for an Ops Manager backup.**

Add any optional settings for backups
that you want to apply to your deployment to the [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification
file. For example, for each type of backup store, and for Ops Manager backup
daemon processes, you can assign labels to associate particular backup
backup stores or backup daemon processes with specific projects.
Use `spec.backup.[*].assignmentLabels` elements of the OpsManager
resources.

**Step 7: Configure any additional settings for an Ops Manager deployment.**

Add any optional settings that you 
want to apply to your deployment to the [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification file.

**Step 8: Save this file with a `.yaml` file extension.**

**Step 9: Create your Ops Manager instance.**

Run the following `kubectl` command on the filename of the Ops Manager resource definition:

```sh
kubectl apply -f <opsmgr-resource>.yaml
```

**Note:**

If you are deploying an Ops Manager resource on a multi-Kubernetes cluster MongoDB deployment, run:

```sh
kubectl apply \
  --context "$MDB_CENTRAL_CLUSTER_FULL_NAME" \
  --namespace "mongodb" 
   -f https://raw.githubusercontent.com/mongodb/mongodb-kubernetes/1.7.0/public/samples/ops-manager/ops-manager-external.yaml
```

**Step 10: Track the status of your Ops Manager instance.**

To check the status of your Ops Manager resource, invoke the following command:

```sh
kubectl get om -o yaml -w
```

The command returns output similar to the following, under the `status` field
while the resource deploys:

```yaml
status:
 applicationDatabase:
  lastTransition: "2023-04-01T09:49:22Z"
  message: AppDB Statefulset is not ready yet
  phase: Pending
  type: ""
  version: ""
 backup:
  phase: ""
 opsManager:
  phase: ""
```

The Kubernetes Operator reconciles the resources in the following order:

1. Application Database.
#. Ops Manager.
#. Backup.

The Kubernetes Operator doesn't reconcile a resource until the preceding 
one enters the `Running` phase.

After the Ops Manager resource completes the `Pending` phase, the 
command returns the output similar to the following under the `status`
field if you enabled backup:

```yaml
 status:
   applicationDatabase:
     lastTransition: "2023-04-01T09:50:20Z"
     members: 3
     phase: Running
     type: ReplicaSet
     version: "8.0.0-ubi8"
  backup:
   lastTransition: "2022-04-01T09:57:42Z"
   message: The MongoDB object <namespace>/<oplogresourcename> 
     doesn't exist
   phase: Pending
   opsManager:
     lastTransition: "2022-04-01T09:57:40Z"
     phase: Running
     replicas: 1
     url: http://om-svc.cloudqa.svc.cluster.local:8080
     version: "8.0.0"
```

Backup remains in a `Pending` state until you configure the backup 
databases.

**Tip:**

The `status.opsManager.url` field states the resource's
connection URL (Uniform Resource Locator). Using this URL (Uniform Resource Locator), you can reach Ops Manager from
inside the Kubernetes cluster or create a project using a
ConfigMap.

**Step 11: Access the Ops Manager application.**

The steps you take differ based on how you are routing traffic to the
Ops Manager application in Kubernetes. If you configured the Kubernetes Operator to
create a Kubernetes service for you, or you created a Kubernetes service
manually, use one of the following methods to access the Ops Manager
application:

**LoadBalancer Service:**

a. Query your cloud provider to get the FQDN (fully qualified domain name) of the load
   balancer service. See your cloud provider's documentation
   for details.

#. Open a browser window and navigate to the Ops Manager
   application using the FQDN (fully qualified domain name) and port number of your load
   balancer service.

   ```sh
   http://ops.example.com:8080
   ```

#. Log in to Ops Manager using the admin user credentials.

**NodePort Service:**

a. Set your firewall rules to allow access from the Internet to
   the `spec.externalConnectivity.``port`
   on the host on which your Kubernetes cluster is running.

#. Open a browser window and navigate to the Ops Manager
   application using the FQDN (fully qualified domain name) and the
   `spec.externalConnectivity.``port`.

   ```sh
   http://ops.example.com:30036
   ```

#. Log in to Ops Manager using the admin user credentials.

To learn how to access the Ops Manager application using a third-party
service, refer to the documentation for your solution.

**Step 12: Create credentials for the Kubernetes Operator.**

If you enabled backup, you must create an Ops Manager organization,
generate programmatic API keys, and create a secret in your secret-storage-tool. 
These activities follow the prerequisites and procedure on the
create-k8s-credentials page.

**Step 13: Create a project using a [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/).**

If you enabled backup, create a project by following the prerequisites 
and procedure on the create-k8s-project page.

You must set `data.baseUrl` in the ConfigMap to the Ops Manager Application\'s URL (Uniform Resource Locator). To find this URL (Uniform Resource Locator), invoke the following command:

```sh
kubectl get om -o yaml -w
```

The command returns the URL of the Ops Manager Application in the
`status.opsManager.url` field, similar to the following example:

```yaml
 status:
   applicationDatabase:
     lastTransition: "2022-04-01T10:00:32Z"
     members: 3
     phase: Running
     type: ReplicaSet
     version: "8.0.0-ubi8"
  backup:
   lastTransition: "2022-04-01T09:57:42Z"
   message: The MongoDB object <namespace>/<oplogresourcename> 
     doesn't exist
   phase: Pending
   opsManager:
     lastTransition: "2022-04-01T09:57:40Z"
     phase: Running
     replicas: 1
     url: http://om-svc.cloudqa.svc.cluster.local:8080
     version: "8.0.0"
```

**Important:**

If you deploy Ops Manager with the Kubernetes Operator and Ops Manager will 
manage MongoDB database resources deployed **outside** of the Kubernetes 
cluster it's deployed to, you must set `data.baseUrl` to the same 
value of the 
`spec.configuration.mms.centralUrl`
setting in the Ops Manager resource specification.

To learn more, see mdb-resource-deployment-locations.

**Step 14: Deploy MongoDB database resources to complete the backup configuration.**

If you enabled mms-backup-functional-overview,
create a MongoDB database resource for the oplog and snapshot stores
to complete the configuration.

a. Deploy a MongoDB database resource for the oplog store in the same
   namespace as the Ops Manager resource.

   **Note:**

   Create this database as a replica set.

   Match the `metadata.name` of the resource with the
   `spec.backup.opLogStores.mongodbResourceRef.name`
   that you specified in your Ops Manager resource definition.

#. Choose one of the following:

   i. Deploy a MongoDB database resource for the blockstore in the
      same namespace as the Ops Manager resource.

      Match the `metadata.name` of the resource to the
      `spec.backup.blockStores.mongodbResourceRef.name`
      that you specified in your Ops Manager resource definition.

   #. Configure an S3 (Simple Storage Service) bucket to use as the S3 (Simple Storage Service) snapshot store. 

      Ensure that you can access the S3 (Simple Storage Service) bucket using the details
      that you specified in your Ops Manager resource definition.

**Step 15: Confirm that the Ops Manager resource is running.**

If you enabled backup, check the status of your Ops Manager resource by 
invoking the following command:

```sh
kubectl get om -o yaml -w
```

When Ops Manager is running, the command returns the following
output under the `status` field:

```yaml
status:
  applicationDatabase:
    lastTransition: "2022-04-01T10:00:32Z"
    members: 3
    phase: Running
    type: ReplicaSet
    version: "8.0.0-ubi8"
  backup:
    lastTransition: "2022-04-01T10:00:53Z"
    phase: Running
    version: "8.0.0-ubi8"
  opsManager:
    lastTransition: "2022-04-01T10:00:34Z"
    phase: Running
    replicas: 1
    url: http://om-svc.cloudqa.svc.cluster.local:8080
    version: "8.0.0"
```

See /reference/troubleshooting for information about the
resource deployment statuses.
