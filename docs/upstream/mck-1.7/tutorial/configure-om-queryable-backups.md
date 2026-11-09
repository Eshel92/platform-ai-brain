<!-- Converted from tutorial/configure-om-queryable-backups.txt (reStructuredText). Includes are inlined. -->

:noprevnext:

# Configure Queryable Backups for Ops Manager Resources

You can configure `queryable backups`
for Ops Manager resources that you deploy in the Kubernetes Operator.

**Note:** In the Ops Manager documentation, queryable backups are also

referred to as queryable snapshots, or queryable restores.

Queryable backups allow you to `run queries`
on specific backup snapsnots from your Ops Manager resources. Querying Ops Manager
backups helps you compare data from different snapshots and identify the
best snapshot to use for `restoring data`.

In the following procedure you:

- Create the `queryable.pem`
  file that holds the certificates for accessing the backup snapshots that you intend to query.
- Create the secret containing the `queryable.pem` file.
- Configure an Ops Manager custom resource to use the secret for queryable backups.
- Save the Ops Manager custom resource configuration and apply it.

Once the Kubernetes Operator deploys the updated configuration for its custom
resource, Ops Manager can read the secret from the `spec.backup.queryableBackupSecretRef.name`
parameter. You can now access the backup snapshots and run queries on them.

## Prerequisites

Before you configure queryable backups, complete the following tasks:

- Install the Kubernetes Operator.

- Deploy the Ops Manager application.

- Configure Backup Settings for the Ops Manager Resource.
  In the linked procedures, see the steps for configuring backups.

## Procedure

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

**Step 2: Create the PEM file for backups.**

Create the `Ops Manager queryable.pem`
file that you will use for accessing and querying backups based on
your deployment's TLS (Transport Layer Security) requirements. The PEM file contains a public
key certificate and its associated private key that are needed to
access and run queries on backup snapshots in Ops Manager.

To learn more about the PEM file's requirements, see
`Authorization and Authentication Requirements in Ops Manager`.

**Step 3: Create a secret containing the PEM file.**

Run the following command to create a secret with the
`queryable.pem`
file that you created in the previous step:

```sh
kubectl create secret generic queryable-pem --from-file=./queryable.pem
```

If you're using [HashiCorp Vault](https://www.vaultproject.io/) as your secret storage tool, 
you can Create a Vault Secret instead.

To learn about your options for secret
storage, see Configure Secret Storage.

**Step 4: Configure Ops Manager custom resource to use the secret.**

Configure `spec.backup.queryableBackupSecretRef.name` to
reference the `queryable.pem`
secret.

```yaml
  apiVersion: mongodb.com/v1
  kind: MongoDBOpsManager
  metadata:
    name: ops-manager
  spec:
    replicas: 1
    version: 8.0.0
    adminCredentials: ops-manager-admin-secret
    backup:
      enabled: true
      queryableBackupSecretRef:
        name: om-queryable-pem
```

**Step 5: Save your Ops Manager config file.**

**Step 6: Apply changes to your Ops Manager deployment.**

Invoke the following `kubectl` command on the filename of the
Ops Manager resource definition:

```sh
kubectl apply -f <opsmgr-resource>.yaml
```

When you apply the changes to your Ops Manager resource
definition, Kubernetes updates the Ops Manager StatefulSet,
creates the volumes, and mounts the Secrets.

**Step 7: Track the status of the mounted volumes and Secrets.**

a. Obtain the list of persistent volume claims:

   ```sh
   kubectl get pvc
   ```

#. Obtain the Secrets:

   ```sh
   kubectl get secrets
   ```

#. Check the status of your Ops Manager resources:

   ```sh
   kubectl get om <resource-name> -o yaml -w
   ```

   The `-w` flag means "watch". With the "watch" flag set, the
   output refreshes immediately when the configuration changes until
   the status phase achieves the `Running` state.

   To learn more about the resource deployment statuses, see
   /reference/troubleshooting.

After you configure queryable backups, you can `query them`
to select the best backup snapshot to use for `restoring data`.

## Disable Queryable Backups

If you require all containers in your MongoDB deployment to be fully static, disable queryable backups as a best practice. This is so the backup-daemon doesn't attempt to download the MongoDB binaries 
from Ops Manager. Downloading binaries undermines the immutable nature of static containers and is only 
possible with non-static containers. 
To learn more, see static-containers.

To disable queryable backups:

**Step 1: Update the Ops Manager custom resource.**

In the MongoDBOpsManager custom resource,
set `spec.configuration.mms.featureFlag.backup.queryable`
and `spec.configuration.mms.featureFlag.backup.wt.queryable`
to `disabled`.

```yaml
apiVersion: mongodb.com/v1
kind: MongoDBOpsManager
metadata:
  name: opsmgr-resource
spec:
  configuration:
    mms.featureFlag.backup.wt.queryable: "disabled"
    mms.featureFlag.backup.queryable: "disabled"
```

**Step 2: Save your Ops Manager custom resource.**

**Step 3: Apply the changes to your Ops Manager custom resource.**

Invoke the following `kubectl` command on the filename of the
Ops Manager resource definition:

```sh
kubectl apply -f <opsmgr-resource>.yaml
```

**Step 4: Navigate to the Ops Manager backup settings.**

In the Ops Manager UI, click Admin in the upper-right hand corner. From
the Admin screen, click General
arrow-right Ops Manager Config
arrow-right Backup.

**Step 5: Delete the PEM file**

Navigate to the Queryable Snapshot Configuration section and
delete the `Proxy Server PEM File`.

**Step 6: Restart the Web Server for the change to take effect.**
