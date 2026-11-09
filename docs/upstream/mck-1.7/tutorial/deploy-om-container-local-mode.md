<!-- Converted from tutorial/deploy-om-container-local-mode.txt (reStructuredText). Includes are inlined. -->

:noprevnext:

# Configure an Ops Manager Resource to use Local Mode

**Important:**

Configuring Ops Manager to use Local Mode in Kubernetes is not recommended.
Consider configuring Ops Manager to use Remote Mode instead.

In a default configuration, the MongoDB Agent\'s and Backup Daemons
access MongoDB installation archives over the Internet from MongoDB, Inc.

You can configure Ops Manager to run in **Local Mode** with the 
Kubernetes Operator if the nodes in your Kubernetes cluster don't have access to
the Internet. The Backup Daemons and managed MongoDB resources download
installation archives only from a [Persistent Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) that you create for
the Ops Manager StatefulSet.

This procedure covers uploading installation archives to Ops Manager.

If Ops Manager has no Internet access, see 
`Configure Deployment to Have Limited Internet Access`.

For compatibility, see k8s-compatibility. To view all available 
versions for each image, see k8s-container-images.

## Prerequisites

- deploy-om-container. The following procedure shows you how to 
  update your Ops Manager Kubernetes [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) to enable Local Mode.

- To avoid downtime when you enable Local Mode, ensure that you set 
  `spec.replicas` to a value greater than `1` in your 
  Ops Manager resource definition.

  If you updated your Ops Manager resource definition to make Ops Manager 
  highly available, apply your changes before you begin this tutorial:

  ```sh
  kubectl apply -f <opsmgr-resource>.yaml -n <metadata.namespace>
  ```

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

**Step 2: Delete the [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) that manages your Ops Manager Pods.**

In this tutorial, you update the StatefulSet that manages the Ops Manager 
Pods in your Kubernetes cluster.

You must first delete the Ops Manager StatefulSet so that Kubernetes can apply
the updates that Local Mode requires.

a. Find the name of your Ops Manager StatefulSet:

   ```sh
   kubectl get statefulsets
   ```

   The entry in the response that matches the 
   `metadata.name` of your 

   Your Ops Manager StatefulSet is the entry in the response that matches
   the `metadata.name` in your Ops Manager resource 
   definition.

   ```sh
   kubectl get statefulsets -n mongodb
   NAME                       READY   AGE
   ops-manager-localmode      2/2     2m31s
   ops-manager-localmode-db   3/3     4m46s
   ```

#. Delete the Ops Manager StatefulSet:

   **Warning:**

   Ensure that you include the `--cascade=false` flag when you
   delete your Ops Manager StatefulSet. If you don't include this
   flag, Kubernetes also deletes your Ops Manager Pods.

   ```sh
   kubectl delete statefulset --cascade=false <ops-manager-statefulset>
   ```

**Step 3: Copy the fields of this Ops Manager resource.**

Copy Lines 9-31 of this example to:

- Use the Ops Manager configuration setting 
  `automation.versions.source: local` in 
  `spec.configuration` to enable Local Mode.

- Define a [Persistent Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) for the Ops Manager StatefulSet to store the 
  MongoDB installation archive. MongoDB Agent\'s running in MongoDB
  database resource containers that you create with the Kubernetes Operator
  download the installation archives from Ops Manager instead of from the
  Internet.

```yaml
apiVersion: mongodb.com/v1
kind: MongoDBOpsManager
metadata:
 name: ops-manager-localmode
spec:
 replicas: 2
 version: "8.0.0"
 adminCredentials: ops-manager-admin-secret
 configuration:
   # this enables local mode in Ops Manager
   automation.versions.source: local
 statefulSet:
   spec:
     # the Persistent Volume Claim will be created for each Ops Manager Pod
     volumeClaimTemplates:
      - metadata:
          name: mongodb-versions
        spec:
          accessModes: [ "ReadWriteOnce" ]
          resources:
            requests:
              storage: "20Gi"
     template:
       spec:
         containers:
           - name: mongodb-ops-manager
             volumeMounts:
             - name: mongodb-versions
               # this is the directory in each Pod where all MongoDB
               # archives must be put
               mountPath: /mongodb-ops-manager/mongodb-releases
 backup:
  enabled: false
 applicationDatabase:
  members: 3
```

**Step 4: Paste the copied example section into your existing Ops Manager resource.**

Open your preferred text editor and paste the [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/)
specification into the appropriate location in your resource file.

**Step 5: Save your Ops Manager config file.**

**Step 6: Apply changes to your Ops Manager deployment.**

a. Invoke the following `kubectl` command on the filename of the
   Ops Manager resource definition:

   ```sh
   kubectl apply -f <opsmgr-resource>.yaml
   ```

#. Kubernetes creates a new Ops Manager StatefulSet when you apply the changes
   to your Ops Manager resource definition. Before proceeding to the next 
   step, run the following command to ensure that the Ops Manager StatefulSet
   exists:

   ```sh
   kubectl get statefulsets
   ```

   The new Ops Manager StatefulSet should show 0 members ready:

   ```sh
   kubectl get statefulsets -n mongodb
   NAME                       READY   AGE         ops-manager-localmode      0/2     2m31s
   ops-manager-localmode-db   3/3     4m46s
   ```

**Step 7: In a rolling fashion, delete your old Ops Manager Pods.**

a. List the Ops Manager Pods in your Kubernetes cluster:

   ```sh
   kubectl get pods
   ```

#. Delete one Ops Manager Pod:

   ```sh
   kubectl delete pod <om-pod-0>
   ```

#. Kubernetes recreates the Ops Manager Pod you deleted. Continue to get the 
   status of the new Pod until it is ready:

   ```sh
   kubectl get pods
   ```

   When the new Pod is initializing, the output is similar to the
   following example:

   ```sh
   NAME                                          READY   STATUS    RESTARTS   AGE
   mongodb-kubernetes-operator-5648d4c86-k5brh   1/1     Running   0          5m24s
   ops-manager-localmode-0                       0/1     Running   0          0m55s
   ops-manager-localmode-1                       1/1     Running   0          5m45s
   ops-manager-localmode-db-0                    1/1     Running   0          5m19s
   ops-manager-localmode-db-1                    1/1     Running   0          4m54s
   ops-manager-localmode-db-2                    1/1     Running   0          4m12s
   ```

   When the new Pod is ready, the output is similar to the following example:

   ```sh
   NAME                                          READY   STATUS    RESTARTS   AGE
   mongodb-kubernetes-operator-5648d4c86-k5brh   1/1     Running   0          5m24s
   ops-manager-localmode-0                       1/1     Running   0          3m55s
   ops-manager-localmode-1                       1/1     Running   0          5m45s
   ops-manager-localmode-db-0                    1/1     Running   0          5m19s
   ops-manager-localmode-db-1                    1/1     Running   0          4m54s
   ops-manager-localmode-db-2                    1/1     Running   0          4m12s
   ```

#. Repeat Steps **b** and **c** until you've deleted all of your 
   Ops Manager Pods and confirmed that all of the new Pods are ready.

**Step 8: Track the status of your Ops Manager instance.**

To check the status of your Ops Manager resource, invoke the following
command:

```sh
kubectl get om -o yaml -w
```

See /reference/troubleshooting for information about the
resource deployment statuses.

After the Ops Manager resource completes the `Pending` phase, the 
command returns output similar to the following:

```yaml
status:
  applicationDatabase:
    lastTransition: "2020-05-15T16:20:22Z"
    members: 3
    phase: Running
    type: ReplicaSet
    version: "8.0.0-ubi8"
  backup:
    phase: ""
  opsManager:
    lastTransition: "2020-05-15T16:20:26Z"
    phase: Running
    replicas: 1
    url: http://ops-manager-localmode-svc.mongodb.svc.cluster.local:8080
    version: "8.0.0"
```

Copy the value of the `status.opsManager.url` field, which states 
the resource's connection URL (Uniform Resource Locator). You use this value when you create a
[ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) later in the procedure.

**Step 9: Download the MongoDB installation archive to your local machine.**

The installers that you download depend on the environment to which 
you deployed the operator:

**Note:**

The following example includes a link that allows you to download
the specified version of MongoDB Community Edition.
To download any other version of MongoDB Community Edition, visit the MongoDB Community Edition Download Center.
To download MongoDB Enterprise Edition, visit the MongoDB Enterprise Download Center.

Download the RHEL installation tarball for the MongoDB Server version 
you want the Kubernetes Operator to deploy. For example, to download the 
`8.0.0` release:

```sh
curl -OL https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-rhel80-8.0.0.tgz
```

**Step 10: Copy the MongoDB archive to the Ops Manager Persistent Volume.**

Copy the MongoDB archive for each MongoDB version you intend to deploy
to the Ops Manager Persistent Volume.

The commands that you use depend on the environment to which you
deployed the Kubernetes Operator:

**Note:**

If you deployed more than one Ops Manager
`replica`, copy only the MongoDB
installation `tarball` packages to `Replica 1` and
beyond.

**k8s:**

To copy the MongoDB installation archive to the 
Ops Manager PersistentVolume:

Copy the MongoDB Server installation tarball to the
Ops Manager PersistentVolume. For example, to copy the `8.0.0`
release:

| Replica 0:

```sh
kubectl cp mongodb-linux-x86_64-rhel80-8.0.0.tgz \ 
"ops-manager-localmode-0:/mongodb-ops-manager/mongodb-releases/mongodb-linux-x86_64-rhel80-8.0.0.tgz"
```

| Replica 1:

```sh
kubectl cp mongodb-linux-x86_64-rhel80-8.0.0.tgz \ 
"ops-manager-localmode-1:/mongodb-ops-manager/mongodb-releases/mongodb-linux-x86_64-rhel80-8.0.0.tgz"
```

**os:**

To copy the MongoDB installation archive to the 
Ops Manager PersistentVolume, copy the MongoDB Server installation `tarball` to the 
Ops Manager PersistentVolume. For example, to copy the `8.0.0`
release:

| Replica 0:

```sh
oc rsync  "ops-manager-localmode-0:/mongodb-ops-manager/mongodb-releases/mongodb-linux-x86_64-rhel80-8.0.0.tgz" \ 
mongodb-linux-x86_64-rhel80-8.0.0.tgz
```

| Replica 1:

```sh
oc rsync  "ops-manager-localmode-1:/mongodb-ops-manager/mongodb-releases/mongodb-linux-x86_64-rhel80-8.0.0.tgz" \ 
mongodb-linux-x86_64-rhel80-8.0.0.tgz
```

**Step 11: Deploy a MongoDB Database Resource.**

a. If you have not done so already, complete the following 
   prerequisites:

   - /tutorial/create-operator-credentials
   - /tutorial/create-project-using-configmap

#. Deploy a MongoDB database resource 
   in the same namespace to which you deployed Ops Manager.
   Ensure that you:

   i. Match the `spec.opsManager.configMapRef.name` of the resource 
      to the `metadata.name` of your ConfigMap.
   #. Match the `spec.credentials` of the resource to the name of 
      the secret you created that contains an Ops Manager programmatic 
      API key pair.

MongoDB Agent\'s run in MongoDB database resource containers that
you create with the Kubernetes Operator. Download the installation archives
from Ops Manager instead of downloading them from the Internet.
