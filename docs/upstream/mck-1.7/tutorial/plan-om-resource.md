<!-- Converted from tutorial/plan-om-resource.txt (reStructuredText). Includes are inlined. -->

# Plan Your Ops Manager Resource

MongoDB `Ops Manager` is an enterprise application that manages, backs
up, and monitors MongoDB deployments. With Ops Manager, you can scale and
upgrade MongoDB, optimize queries, perform point-in-time restores, receive
performance alerts, and monitor your deployments. To manage and maintain
Ops Manager and its underlying database, you can use the MongoDB Controllers for Kubernetes Operator to run
Ops Manager as a resource deployed in a container on Kubernetes.

You can deploy Ops Manager resources in one of the following ways:

- **Single Kubernetes cluster mode**. You can deploy a single Ops Manager
  instance to support your single Kubernetes cluster deployment of MongoDB resources.

- **Multiple Kubernetes cluster mode**. You can deploy multiple Ops Manager
  and Application Database instances in multiple Kubernetes clusters. In this
  mode, the multi-cluster of `Ops Manager` resources supports
  a deployment of the Ops Manager Application and the Application Database on
  multiple Kubernetes clusters.

Before you deploy an Ops Manager resource in either a single or multiple
Kubernetes clusters, review meko-om-arch and considerations,
and complete the prerequisites.

## Architecture

For Ops Manager resource architecture details, see:

- Single Kubernetes cluster deployments of Ops Manager resources: meko-om-arch.
- Multiple Kubernetes cluster deployments of Ops Manager resources: om-multi-k8s.

## Considerations

### Encryption Key

The Kubernetes Operator generates an encryption key to protect sensitive
information in the mms-application-database. The Kubernetes Operator
saves this key in a [secret](https://kubernetes.io/docs/concepts/configuration/secret/) in the same namespace as the Ops Manager
resource. The Kubernetes Operator names the secret
`<om-resource-name>-gen-key`.

**Note:**

To avoid storing secrets in single-cluster Kubernetes deployments, you can
migrate all [secrets](https://kubernetes.io/docs/concepts/configuration/secret/) to a secret storage tool.
Deployments on multiple Kubernetes clusters don't support storing secrets
in secret storage tools, such as [HashiCorp Vault](https://www.vaultproject.io/).

If you remove the Ops Manager resource, the key remains stored in the
secret on the Kubernetes cluster. If you stored the Application Database in
a [Persistent Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) and you create another Ops Manager resource with the same name,
the Kubernetes Operator reuses the secret. If you create an Ops Manager
resource with a different name, then Kubernetes Operator creates a new
secret and Application Database, and the old secret isn't reused.

### Application Database

#### Topology

- When you create an instance of Ops Manager through the Kubernetes Operator in
  a single Kubernetes cluster, the mms-application-database
  is deployed as a replica set. You can't configure the Application Database
  as a standalone database or sharded cluster. If you have
  concerns about performance or size requirements for the Application Database,
  contact [MongoDB Support](https://support.mongodb.com/welcome).

- When you create an instance of Ops Manager through
  the Kubernetes Operator in a multi-cluster mode, the Kubernetes Operator can configure
  the mms-application-database on multiple member clusters. To learn more,
  see om-multi-k8s.

#### Monitoring

The Kubernetes Operator automatically configures Ops Manager to monitor the
Application Database that backs the Ops Manager Application. The Kubernetes Operator
creates a project named `<ops-manager-deployment-name>-db` for you to
monitor the Application Database deployment.

Ops Manager monitors the Application Database deployment, but Ops Manager doesn't
manage it. You can't change the Application Database\'s configuration in
the Ops Manager Application.

**Important:**

The Ops Manager UI might display warnings in the
`<ops-manager-deployment-name>-db` project stating that the
agents for the Application Database are out of date. You can safely
ignore these warnings.

#### Authentication

The Kubernetes Operator enforces `SCRAM-SHA-256`
authentication on
the Application Database.

The Kubernetes Operator creates the database user which Ops Manager uses to
connect to the Application Database. This database user has the
following attributes:

* - Username
  - `mongodb-ops-manager`

* - Authentication Database
  - `admin`

* - Roles
  -
    - `readWriteAnyDatabase`
    - `dbAdminAnyDatabase`
    - `clusterMonitor`

You can't modify the Ops Manager database user's name and roles. You
create a secret to set the database user's
password. You edit the secret to update the password. If you don't
create a secret or delete an existing secret, the Kubernetes Operator
generates a password and stores it.

To learn about other options for secret
storage, see Configure Secret Storage.
Multi-cluster deployments don't support storing secrets in [HashiCorp Vault](https://www.vaultproject.io/).

#### Offline Deployments

The Kubernetes Operator requires that you specify the MongoDB Enterprise version
for the `Application Database` image to enable any
deployments of Ops Manager resources, including offline deployments.

### Streamlined Configuration

After you deploy Ops Manager, you need to configure it. The regular
procedure involves setting up Ops Manager through the
`configuration wizard`. If you
set some essential settings in your object specification before you
deploy, you can bypass the configuration wizard.

In the `spec.configuration` block of your Ops Manager object
specification, you need to:

- Add mms.ignoreInitialUiSetup and set to
  `true`.

- Add the minimum configuration settings to
  allow the Ops Manager instance to start without errors.

**Example:**

To disable the Ops Manager configuration wizard, configure the
following settings in your `spec.configuration` block:

```yaml
spec:
  configuration:
    mms.ignoreInitialUiSetup: "true"
    automation.versions.source: "remote"
    mms.adminEmailAddr: cloud-manager-support@mongodb.com
    mms.fromEmailAddr: cloud-manager-support@mongodb.com
    mms.mail.hostname: email-smtp.us-east-1.amazonaws.com
    mms.mail.port: "465"
    mms.mail.ssl: "true"
    mms.mail.transport: smtp
    mms.minimumTLSVersion: TLSv1.2
    mms.replyToEmailAddr: cloud-manager-support@mongodb.com
```

Replace the example values with the values you want your Ops Manager to
use.

### Backup

Kubernetes Operator enables mms-backup-functional-overview by
default. The Kubernetes Operator deploys a [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) comprised of
one Pod to host the backup-daemon and then creates a [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims)
and [Persistent Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) for the Backup Daemon's head database. The
Kubernetes Operator uses the `Ops Manager API` to
enable the Backup Daemon and configure the head database.

**Important:**

To configure Backup, you must create the `MongoDB` resources or `MongoDBMultiCluster` resources
for the oplog store and for one of the
following:

- oplog store or S3 (Simple Storage Service) oplog store.
  If you deploy both the oplog store and the S3 (Simple Storage Service)  oplog store, Ops Manager
  chooses one to use for Backup at random.
- S3 (Simple Storage Service) snapshot store or blockstore.
  If you deploy both an S3 (Simple Storage Service) snapshot store and a
  blockstore, Ops Manager chooses one
  to use for Backup at random.

The Ops Manager resource remains in a `Pending` state until you configure these Backup resources.

You can also encrypt backup jobs, but 
limitations apply to deployments where the same 
Kubernetes Operator instance is not managing both the 
MongoDBOpsManager and MongoDB 
custom resources.

#### Oplog Store

You must deploy a three-member replica set to store your
oplog slices.

The Oplog database only supports the `SCRAM` authentication mechanism.
You cannot enable other authentication mechanisms.

If you enable `SCRAM` authentication on the oplog database, you
must: 

- Create a MongoDB user resource to connect Ops Manager to the oplog 
  database.
- Specify the `name`
  of the user in the Ops Manager resource definition.

#### S3 Oplog Store

To configure an S3 (Simple Storage Service) oplog store, you must create an AWS (Amazon Web Services) S3 (Simple Storage Service) or
S3 (Simple Storage Service)-compatible bucket to store your database Backup Oplog.

You can configure the oplog store for both `MongoDB` resource and `MongoDBMultiCluster` resource,
using the `spec.backup.s3OpLogStores.mongodbResourceRef.name` setting
in the Ops Manager resource definition.

#### Blockstore

To configure a blockstore, you
must deploy a replica set to store snapshots.

#### S3 Snapshot Store

To configure an S3 (Simple Storage Service) snapshot store, you
must create an AWS (Amazon Web Services) S3 (Simple Storage Service) or S3 (Simple Storage Service)-compatible bucket to store your
database Backup `snapshots`.

The default configuration stores snapshot metadata in the Application
Database. You can also deploy a replica set to store snapshot metadata,
then configure it using the
`spec.backup.s3Stores.mongodbResourceRef.name` settings in
the Ops Manager resource definition.

You can configure the S3 (Simple Storage Service) snapshot store for both `MongoDB` resource and `MongoDBMultiCluster` resource.

You can update any additional S3 (Simple Storage Service)
`configuration settings`
that Kubernetes Operator doesn't manage through the Ops Manager Application.

#### Disable Backup

To disable backup after you enabled it:

1. Set the Ops Manager Kubernetes [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) `spec.backup.enabled`
   setting to `false`.

#. `Disable backups` in the
   Ops Manager Application.

#. Delete the backup-daemon [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/):

   ```sh
   kubectl delete statefulset <metadata.name> -backup-daemon \
    -n <metadata.namespace>
   ```

**Important:**

The [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) and [Persistent Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) for the Backup Daemon's head
database are not deleted when you delete the backup-daemon
[StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/). You can retrieve stored data before you delete
these Kubernetes resources.

To learn about reclaiming [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/), see the
`Kubernetes documentation`.

#### Manually Configure KMIP Backup Encryption

For deployments where the same Kubernetes Operator instance is *not* managing both the
MongoDBOpsManager and 
MongoDB custom resources, 
you must manually configure KMIP (Key Management Interoperability Protocol) backup encryption client settings in Ops Manager 
using the following procedure. If the Kubernetes Operator *is* managing both resources, 
see configure-kmip-backup-encryption instead.

##### Prerequisites

- A running KMIP (Key Management Interoperability Protocol) server.
- A running Ops Manager instance, configured to use KMIP.
- A TLS (Transport Layer Security) secret that concatenates the private key and the KMIP
  client certificate in PEM format.

##### Procedure

1. Mount the TLS (Transport Layer Security) secret to the MongoDBOpsManager custom resource. For example:

   ```yaml
   apiVersion: mongodb.com/v1
   kind: MongoDBOpsManager
   metadata:
     name: ops-manager-pod-spec
   spec:
     < ... omitted ... >
     statefulSet:
       spec:
         template:
           spec:
             volumes:
             - name: kmip-client-test-prefix-mdb-latest-kmip-client
               secretName: test-prefix-mdb-latest-kmip-client
             containers:
               - name: mongodb-ops-manager
                 volumeMounts:
                 - mountPath: /mongodb-ops-manager/kmip/client/test-prefix-mdb-latest-kmip-client
                   name: kmip-client-test-prefix-mdb-latest-kmip-client
                   readOnly: true
     ...
   ```

   
2. Configure the KMIP (Key Management Interoperability Protocol) settings for your project in Ops Manager following the procedure 
   in configure-group-kmip.

### Configure Ops Manager to Run over HTTPS

You can configure your Ops Manager instance created through the Kubernetes Operator
to run over HTTPS (Hypertext Transfer Protocol Secure) instead of HTTP (Hypertext Transfer Protocol). 

To configure your Ops Manager instance to run over HTTPS (Hypertext Transfer Protocol Secure): 

1. Create a secret that contains the TLS (Transport Layer Security) certificate and private key.
2. Add this secret to the Ops Manager configuration object. 

For detailed instructions, see deploy-om-container.

**Important:**

If you have existing deployments, you must restart them manually 
after enabling HTTPS (Hypertext Transfer Protocol Secure). To avoid restarting your deployments, 
configure HTTPS (Hypertext Transfer Protocol Secure) before deploying your managed resources.

To learn more, see https-enablement-issues.

### Ops Manager Application Access

By default, the Kubernetes Operator doesn't create a Kubernetes service to route
traffic originating from outside of the Kubernetes cluster to the Ops Manager
application.

To access the Ops Manager application, you can:

- Configure the Kubernetes Operator to create a Kubernetes service.
- Create a Kubernetes service manually. MongoDB recommends using a
  `LoadBalancer` Kubernetes service if your cloud provider supports it.
- If you're using OpenShift, use
  [routes](https://docs.openshift.com/enterprise/3.0/architecture/core_concepts/routes.html).
- Use a third-party service, such as Istio.

The simplest method is configuring the Kubernetes Operator to create a Kubernetes
service that routes external traffic to the Ops Manager application. The
Ops Manager deployment procedure instructs you to add the following
settings to the [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification that configures the
Kubernetes Operator to create a service:

- `spec.``externalConnectivity`
- `spec.externalConnectivity.``type`

In addition, for deployments on multiple Kubernetes clusters, see om-nw-lb-mesh.

### Deploying Ops Manager in Remote or Local Mode

You can use the Kubernetes Operator to configure a single Ops Manager cluster to operate in 
**Local** or **Remote** mode if your environment prevents granting hosts
in your Kubernetes cluster access to the Internet. In these modes, the Backup
Daemons and managed MongoDB resources download installation archives
from Ops Manager instead of from the Internet:

- deploy-om-container-remote-mode: Ops Manager reads the
  installation archives from HTTP endpoints on a web server
  or S3-compatible file store deployed to your Kubernetes cluster.
  
- deploy-om-container-local-mode: Ops Manager reads the instalation
  archives from a [Persistent Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) that you create for the Ops Manager StatefulSet.

### Managing External MongoDB Deployments

When you deploy Ops Manager with the Kubernetes Operator, Ops Manager can manage
MongoDB database resources deployed:

- To the same Kubernetes cluster as Ops Manager.
- Outside of Kubernetes clusters.

If Ops Manager manages MongoDB database resources deployed to different
Kubernetes clusters than Ops Manager or outside of Kubernetes clusters, you must:

1. Add the `mms.centralUrl` setting to `spec.configuration` in the
   Ops Manager resource specification.

   Set the value to the URL by which Ops Manager is exposed outside of the
   Kubernetes cluster:

   ```yaml
   spec:
     configuration:
       mms.centralUrl: https://a9a8f8566e0094380b5c257746627b82-1037623671.us-east-1.elb.example.com:8080/
   ```

#. Update the ConfigMaps referenced by
   all MongoDB database resources inside the Kubernetes cluster that you
   deployed with the Kubernetes Operator.

   Set `data.baseUrl` to the same value of the
   `spec.configuration.mms.centralUrl`
   setting in the Ops Manager resource specification.

   **Important:**

   This includes the ConfigMaps `referenced by the MongoDB database resources
   for the oplog and snapshot stores`.

### Deploying Ops Manager in Multi-Clusters

See om-multi-k8s.

## Secret Storage

To avoid storing secrets in Kubernetes, migrate all Kubernetes [secrets](https://kubernetes.io/docs/concepts/configuration/secret/) that
the Kubernetes Operator creates to a secret storage tool.
Multi-cluster deployments don't support storing secrets in secret storage
tools such as [HashiCorp Vault](https://www.vaultproject.io/).

## Prerequisites

1. If you have not already, run the following command to run all
   `kubectl` commands in the namespace you created:

   ```sh
   kubectl config set-context $(kubectl config current-context) \
     -n <metadata.namespace>
   ```

   **Note:**

   If you are deploying an Ops Manager resource in a multi-Kubernetes cluster MongoDB deployment:

   - Set the `context` to the name of the central cluster, such as:
     `kubectl config set context "$MDB_CENTRAL_CLUSTER_FULL_NAME"`.

   - Set the `--namespace` to the same scope
     that you used for your multi-Kubernetes cluster MongoDB deployment, such as: `kubectl config --namespace "mongodb"`.

#. Install the MongoDB Controllers for Kubernetes Operator.

#. Ensure that the host on which you want to deploy Ops Manager has a
   minimum of five gigabytes of memory.

4. Create a Kubernetes [secret](https://kubernetes.io/docs/concepts/configuration/secret/) for an admin user in the same [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)
   as the Ops Manager resource. If you are deploying Ops Manager in a multi-Kubernetes cluster MongoDB deployment,
   use the same [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) that you set for your multi-Kubernetes cluster MongoDB deployment scope.

   If you're using [HashiCorp Vault](https://www.vaultproject.io/) as your secret storage tool, 
   you can Create a Vault Secret instead.

   To learn about your options for secret
   storage, see Configure Secret Storage.

   When you deploy the Ops Manager resource, Ops Manager creates a user with
   these credentials and grants it the `Global Owner` role.
   Use these credentials to log in to Ops Manager for the first time. Once
   you deploy Ops Manager, change the password or remove this secret.

   **Note:**

   The admin user's password must adhere to the Ops Manager
   `password complexity requirements`. 

   ```sh
   kubectl create secret generic <adminusercredentials> \
     --from-literal=Username="<username>" \
     --from-literal=Password="<password>" \
     --from-literal=FirstName="<firstname>" \
     --from-literal=LastName="<lastname>"
   ```

1. (*Optional*) To set the password for the Ops Manager database user,
   create a [secret](https://kubernetes.io/docs/concepts/configuration/secret/) in the same [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) as the Ops Manager resource.

   If you're using [HashiCorp Vault](https://www.vaultproject.io/) as your secret storage tool, 
   you can Create a Vault Secret instead.

   The Kubernetes Operator creates the database user that Ops Manager uses to
   connect to the mms-application-database. You can set the
   password for this database user by invoking the following command to
   create a secret:

   ```sh
   kubectl create secret generic <om-db-user-secret-name> \
     --from-literal=password="<om-db-user-password>"
   ```

   **Note:**

   If you choose to create a secret for the Ops Manager database user,
   you must specify the secret's
   `name`
   in the Ops Manager resource definition. By default, the
   Kubernetes Operator looks for the password value in the `password`
   key. If you stored the password value in a different key, you
   must also specify that
   `key`
   name in the Ops Manager resource definition.

   If you don't create a secret, then the Kubernetes Operator automatically
   generates a password and stores it internally. To learn more,
   see app-db-auth.

#. (*Optional*). To configure Backup to an S3 (Simple Storage Service) snapshot store, create
   a [secret](https://kubernetes.io/docs/concepts/configuration/secret/) in the same namespace as the Ops Manager resource.

   If you're using [HashiCorp Vault](https://www.vaultproject.io/) as your secret storage tool, 
   you can Create a Vault Secret instead.

   This secret stores your S3 (Simple Storage Service) credentials so that the Kubernetes Operator
   can connect Ops Manager to your AWS (Amazon Web Services) S3 (Simple Storage Service) or S3 (Simple Storage Service)-compatible bucket.
   The secret must contain the following key-value pairs:

   |  |  |
   |---|---|
   | Key | Value |
   | `accessKey` | Unique identifer of the AWS (Amazon Web Services) user who owns the S3 (Simple Storage Service) or S3 (Simple Storage Service)-compatible bucket. |
   | `secretKey` | Secret key of the AWS (Amazon Web Services) user who owns the S3 (Simple Storage Service) or S3 (Simple Storage Service)-compatible bucket. |

   To create the secret, invoke the following command:

   ```sh
   kubectl create secret generic <my-aws-s3-credentials> \
     --from-literal=accessKey="<AKIAIOSFODNN7EXAMPLE>" \
     --from-literal=secretKey="<wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY>"
   ```

   To learn more about managing S3 (Simple Storage Service) snapshot storage, see the
   `Prerequisites`.
