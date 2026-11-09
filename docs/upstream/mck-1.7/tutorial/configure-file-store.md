<!-- Converted from tutorial/configure-file-store.txt (reStructuredText). Includes are inlined. -->

# Configure File System Backup Store with Kubernetes Operator

Kubernetes Operator supports storage of filesystem snapshots.

## Prerequisites

To configure file system snapshot storage, your Kubernetes Operator 
deployment must have a 
`storage class`
configured with the `ReadWriteMany` method.

## Procedure

To configure file system snapshot storage:

**Step 1: Create a PersistentVolumeClaim object.**

Create a `PersistentVolumeClaim` 
object, and allocate storage as needed. Set 
`accessModes` 
to `ReadWriteMany`:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: snapshot-store-ops-manager
spec:
  storageClassName: managed-nfs-storage #SC that supports(RWX)
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 10G
    ...
```

**Step 2: Create and apply an Ops Manager Custom Resource Definition specifying your PersistentVolumeClaim.**

Create an Ops Manager [CustomResourceDefinition](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/) that specifies your 
`PersistentVolumeClaim` object and the
`spec.backup.fileSystemStores` field, which is the name of 
your file system snapshot store.

The following example creates a [CustomResourceDefinition](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/) file named 
`ops-manager-fs.yaml`, for the MongoDB 
oplog store with a `kube-user`.

```yaml
apiVersion: mongodb.com/v1
  kind: MongoDBOpsManager
  metadata:
    name: ops-manager
  spec:
    replicas: 1
    version: 8.0.0
    adminCredentials: ops-manager-admin-secret
    statefulSet:
      spec:
        template:
          spec:
            volumes:
              - name: snapshot-store
                persistentVolumeClaim:
                  claimName: snapshot-store-ops-manager
            containers:
              - name: mongodb-ops-manager
                volumeMounts:
                  - name: snapshot-store
                    mountPath: /snapshot_store  
    backup:
      enabled: true
      fileSystemStores:
        - name: filesystem1
      headDB:
        storage: "30Gi"
      assignmentLabels: ["test1", "test2"]
      opLogStores:
        assignmentLabels: ["test1", "test2"]
        - name: oplog1
          mongodbResourceRef:
            name: oplog-db
          # mongodbUserRef:
          #   name: kube-user
      statefulSet:
        spec:
          template:
            spec:
              volumes:
                - name: snapshot-store
                  persistentVolumeClaim:
                    claimName: snapshot-store-ops-manager
              containers:
                - name: mongodb-backup-daemon
                  volumeMounts:
                    - name: snapshot-store
                      mountPath: /snapshot_store  
    applicationDatabase:
      members: 3
      version: 8.0.0
```

**Step 3: Apply changes to your Ops Manager deployment.**

Invoke the following `kubectl` command on the filename of your
Ops Manager resource definition:

```sh
kubectl apply -f <opsmgr-resource>.yaml
```

**Step 4: Configure your oplog store.**

Wait for your Ops Manager object to report its state as `Running`, then 
configure your oplog store as described in the 
**Configure Backup Settings** step of the 
Deploy an Ops Manager Resource procedure.

**Step 5: Create a File System Snapshot Store in Ops Manager.**

Log into your Ops Manager instance and navigate to: Admin
arrow-right Backup arrow-right
Snapshot Store arrow-right
Create New File System Store.

Set the name to the value you set for `backup.fileSystemStores`
in your [CustomResourceDefinition](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/). Set the other values as appropriate, then click
Create.

Your Ops Manager object will report a `BACKUP` state of `Pending`
after you create the new file system store.
