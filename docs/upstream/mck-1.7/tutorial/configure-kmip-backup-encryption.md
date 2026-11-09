<!-- Converted from tutorial/configure-kmip-backup-encryption.txt (reStructuredText). Includes are inlined. -->

# Configure KMIP Backup Encryption for Ops Manager

`Ops Manager` can encrypt backup jobs. You can use the Kubernetes Operator to 
configure KMIP (Key Management Interoperability Protocol) backup encryption for `Ops Manager`. To learn more, see 
`Encrypted Backup Snapshots`.

## Limitations

For deployments where the same Kubernetes Operator instance is not managing both the
MongoDBOpsManager and 
MongoDB custom resources, 
you must manually configure KMIP (Key Management Interoperability Protocol) 
backup encryption client settings in the 
MongoDBOpsManager custom resource.
This requirement involves including client certificates for each MongoDB database, 
which you can achieve by overriding the Ops Manager Pod's StatefulSet to mount 
the certificates. To learn more, see kmip-manual-procedure.

## Procedure

**Step 1: Create the ConfigMap of the CA (Certificate Authority).**

Run the following command:

```sh
kubectl -n mongodb create configmap mongodb-kmip-certificate-authority-pem --from-file=ca-pem
```

**Step 2: Configure the Ops Manager custom resource to use KMIP (Key Management Interoperability Protocol) backup encryption.**

Configure the `spec.backup.encryption.kmip` settings.

```yaml
  apiVersion: mongodb.com/v1
  kind: MongoDBOpsManager
  metadata:
    name: om-backup-kmip
  spec:
    replicas: 1
    version: 8.0.0
    adminCredentials: ops-manager-admin-secret
    backup:
      encryption: 
        kmip:
          server:
            url: kmip.corp.mongodb.com:5696
            ca: mongodb-kmip-certificate-authority-pem
```

**Step 3: Save your Ops Manager config file.**

**Step 4: Apply changes to your Ops Manager deployment.**

Invoke the following `kubectl` command on the filename of the
Ops Manager resource definition:

```sh
kubectl apply -f <opsmgr-resource>.yaml
```

**Step 5: Check the status of your Ops Manager resources.**

Run the following command:

```sh
kubectl get om <resource-name> -o yaml -w
```

**Step 6: Create the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) of the client certificate and private key.**

Run the following command:

```sh
kubectl -n mongodb create secret tls mongodb-kmip-client-pem-my-replica-set-kmip-client \ 
--cert=<path-to-cert-file> \
--key=<path-to-key-file>
```

The client certificate [secret](https://kubernetes.io/docs/concepts/configuration/secret/) name has the following naming 
convention inferred from the `MongoDB` [CustomResourceDefinition](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/):

```sh
<clientCertificatePrefix>-<objectMeta.name>-kmip-client
```

|  |  |
|---|---|
| `clientCertificatePrefix` | Human-readable label specified in the `spec.backup.encryption.kmip.client.clientCertificatePrefix` field of the `MongoDB` [CustomResourceDefinition](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/). |
| `objectMeta.name` | Human-readable label specified in the `metadata.name` field of the `MongoDB` [CustomResourceDefinition](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/). |
| `kmip-client` | Fixed suffix that the Kubernetes Operator assumes. |

To learn more, see `kubernetes.io/tls`.

**Step 7: Configure your MongoDB database deployment.**

Configure the `spec.backup.encryption.kmip` settings.

```yaml
  apiVersion: mongodb.com/v1
  kind: MongoDB
  metadata:
    name: my-replica-set
  spec:
    members: 3
    version: 8.0.0
    type: ReplicaSet
    backup:
      encryption: 
        kmip:
          client:
            clientCertificatePrefix: mongodb-kmip-client-pem
```

To learn more, see deploy a replica set 
or deploy a sharded cluster.

**Step 8: Save your MongoDB database deployment config file.**

**Step 9: Apply changes to your MongoDB database deployment.**

Invoke the following `kubectl` command on the filename of the
Ops Manager resource definition:

```sh
kubectl apply -f <mdb-database-deployment>.yaml
```

**Step 10: Check the status of your MongoDB database deployment.**

Run the following command:

```sh
kubectl get mdb <resource-name> -o yaml -w
```
