<!-- Converted from tutorial/resize-pv-storage.txt (reStructuredText). Includes are inlined. -->

# Increase Storage for Persistent Volumes

The `Ops Manager`, MongoDB Database, AppDB and Backup Daemon custom resources that 
comprise a standard Kubernetes Operator deployment are each deployed as Kubernetes 
`statefulSets`. The Kubernetes Operator supports increasing the storage associated with 
these specific resources by increasing the capacity of their respective Kubernetes 
`persistentVolumeClaims` when the underlying Kubernetes `storageClass` supports Kubernetes 
`persistentVolume` expansion.

Depending on the specific resource type, you can increase storage in one of two ways. 
You can either manually increase storage, or you can leverage the Kubernetes Operator 
easy storage expansion feature. The following table illustrates which of these two 
procedures is supported for a given custom resource type. 

| Custom Resource Type | Manual Storage Expansion | Easy Storage Expansion |
|---|---|---|
| AppDB | check-square | check-square |
| Backup Daemon | check-square |  |
| MongoDB Database | check-square | check-square |
| MongoDB Multi-Cluster | check-square | check-square |
| Ops Manager | check-square |  |

## Prerequisites

### Storage Class Must Support Resizing

Make sure the [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) and volume plugin provider that the [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
use supports resize:

```sh
kubectl patch storageclass/<my-storageclass> --type='json' \
        -p='[{"op": "add", "path": "/allowVolumeExpansion", "value": true }]'
```

If you don't have a `storageClass` that supports resizing, ask your Kubernetes
administrator to help.

## Easy Expand Storage

**Note:**

The easy expansion mechanism requires the default RBAC included with the Kubernetes Operator. 
Specifically, it requires `get`, `list`, `watch`, `patch` and `update` 
permissions for `persistantVolumeClaims`. If you have customized any of 
the Kubernetes Operator RBAC resources, you might need to adjust permissions to 
allow the Kubernetes Operator to resize storage resources in your Kubernetes cluster.

This process results in a rolling restart of the MongoDB custom resource 
in your Kubernetes cluster.

      
**Step 1: Create or identify a persistent [custom resource](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/).**

Use an existing database resource or create a new one with persistent
storage. Wait until the persistent volume enters the `Running`
state.

**Example:**

A database resource with persistent storage would include:

```yaml
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: <my-replica-set>
spec:
  members: 3
  version: "8.0.0"
  project: my-project
  credentials: my-credentials
  type: ReplicaSet
  podSpec:
    persistence:
      single:
        storage: "1Gi"
```

**Step 2: Insert data into the database that the resource serves.**

a. Start `mongo` in the Kubernetes cluster.

   ```sh
   $kubectl exec -it <my-replica-set>-0 \
            /var/lib/mongodb-mms-automation/mongodb-linux-x86_64-8.0.0/bin/mongo
   ```

b. Insert data into the `test` database.

   ```javascript
   <my-replica-set>:PRIMARY> use test

   switched to db test

   <my-replica-set>:PRIMARY> db.tmp.insertOne({"foo":"bar"})

   {
     "acknowledged" : true,
     "insertedId" : ObjectId("61128cb4a783c3c57ae5142d")
   }
   ```

**Step 3: Update the database resource with a new storage value.**

**Important:**

You can only increase disk size for existing storage resources, not decrease. 
Decreasing the storage size causes an error in the reconcile stage. 

a. Update the disk size. Open your preferred text editor and make
   changes similar to this example:

   **Example:**

   To update the disk size of the replica set to 2 GB, change the
   `storage` value in the database resource specification:

   ```yaml
   apiVersion: mongodb.com/v1
   kind: MongoDB
   metadata:
     name: <my-replica-set>
   spec:
     members: 3
     version: "8.0.0"
     project: my-project
     credentials: my-credentials
     type: ReplicaSet
     podSpec:
       persistence:
         single:
           storage: "2Gi"
   ```

b. Update the MongoDB custom resource with the new volume size.

   ```sh
   kubectl apply -f my-updated-replica-set-vol.yaml
   ```

c. Wait until this StatefulSet achieves the `Running` state.

**Step 4: Validate that the [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) has been resized.**

If you reuse [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/), you can find the data that you inserted in **Step
2** on the databases stored in [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/):

```sh
$ kubectl describe mongodb/<my-replica-set> -n mongodb
```

The following output indicates that your PVC resize request is being processed.

```sh
status:
  clusterStatusList: {}
  lastTransition: "2024-08-21T11:03:52+02:00"
  message: StatefulSet not ready
  observedGeneration: 2
  phase: Pending
  pvc:
    - phase: PVC Resize - STS has been orphaned
      statefulsetName: multi-replica-set-pvc-resize-0
  resourcesNotReady:
    - kind: StatefulSet
      message: 'Not all the Pods are ready (wanted: 2, updated: 1, ready: 1, current:2)'
      name: multi-replica-set-pvc-resize-0
  version: ""
```

**Step 5: Validate data exists on the updated [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims).**

If you reuse [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/), you can find the data that you inserted in **Step
2** on the databases stored in [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/):

```sh
$ kubectl exec -it <my-replica-set>-1 \
          /var/lib/mongodb-mms-automation/mongodb-linux-x86_64-8.0.0/bin/mongo
```

```javascript
<my-replica-set>:PRIMARY> use test
switched to db test

<my-replica-set>:PRIMARY> db.tmp.count()
1
```

## Manually Expand Storage

      
**Step 1: Create or identify a persistent [custom resource](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/).**

Use an existing database resource or create a new one with persistent
storage. Wait until the persistent volume gets to the `Running`
state.

**Example:**

A database resource with persistent storage would include:

```yaml
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: <my-replica-set>
spec:
  members: 3
  version: "8.0.0"
  project: my-project
  credentials: my-credentials
  type: ReplicaSet
  podSpec:
    persistence:
      single:
        storage: "1Gi"
```

**Step 2: Insert data to the database that the resource serves.**

a. Start `mongo` in the Kubernetes cluster.

   ```sh
   $kubectl exec -it <my-replica-set>-0 \
            /var/lib/mongodb-mms-automation/mongodb-linux-x86_64-8.0.0/bin/mongo
   ```

b. Insert data into the `test` database.

   ```javascript
   <my-replica-set>:PRIMARY> use test

   switched to db test

   <my-replica-set>:PRIMARY> db.tmp.insertOne({"foo":"bar"})

   {
     "acknowledged" : true,
     "insertedId" : ObjectId("61128cb4a783c3c57ae5142d")
   }
   ```

**Step 3: Patch each persistence volume.**

Invoke the following commands for the entire replica set:

```sh
kubectl patch pvc/"data-<my-replica-set>-0" -p='{"spec": {"resources": {"requests": {"storage": "2Gi"}}}}'
kubectl patch pvc/"data-<my-replica-set>-1" -p='{"spec": {"resources": {"requests": {"storage": "2Gi"}}}}'
kubectl patch pvc/"data-<my-replica-set>-2" -p='{"spec": {"resources": {"requests": {"storage": "2Gi"}}}}'
```

Wait until each [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) gets to the following condition:

```yaml
- lastProbeTime: null
  lastTransitionTime: "2019-08-01T12:11:39Z"
  message: Waiting for user to (re-)start a pod to finish file
           system resize of volume on node.
  status: "True"
  type: FileSystemResizePending
```

**Step 4: Stop the Operator.**

Update the Kubernetes Operator deployment definition and apply the change to your 
Kubernetes cluster in order to scale the Kubernetes Operator down to `0` replicas. 
Scaling the Kubernetes Operator down to `0` replicas allows you to avoid a race 
condition in which the Kubernetes Operator tries to restore the state of the 
manually updated resource to align with the resource's original definition. 

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mongodb-kubernetes-operator
  namespace: mongodb
spec:
  replicas: 0
```

**Step 5: Remove the StatefulSets.**

**Note:**

This step removes the [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) only. The pods remain
unchanged and running.

Delete a [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) resource.

```sh
kubectl delete sts --cascade=false <my-replica-set>
```

**Step 6: Update the database resource with a new storage value.**

a. Update the disk size. Open your preferred text editor and make
   changes similar to this example:

   **Example:**

   To update the disk size of the replica set to 2 GB, change the
   `storage` value in the database resource specification:

   ```yaml
   apiVersion: mongodb.com/v1
   kind: MongoDB
   metadata:
     name: <my-replica-set>
   spec:
     members: 3
     version: "8.0.0"
     project: my-project
     credentials: my-credentials
     type: ReplicaSet
     podSpec:
       persistence:
         single:
           storage: "2Gi"
   ```

b. Recreate a [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) resource with the new volume size.

   ```sh
   kubectl apply -f my-replica-set-vol.yaml
   ```

c. Wait until the MongoDB custom resource is in a `Running` state.

**Step 7: Update the pods in a rolling fashion.**

Invoke the following command:

```sh
kubectl rollout restart sts <my-replica-set>
```

The new pods mount the resized volume.

**Step 8: Validate data exists on the updated [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims).**

If the [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) were reused, the data that you inserted in **Step
2** can be found on the databases stored in [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/):

```sh
$ kubectl exec -it <my-replica-set>-1 \
          /var/lib/mongodb-mms-automation/mongodb-linux-x86_64-8.0.0/bin/mongo
```

```javascript
<my-replica-set>:PRIMARY> use test
switched to db test

<my-replica-set>:PRIMARY> db.tmp.count()
1
```
