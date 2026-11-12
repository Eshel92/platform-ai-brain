<!-- Part 1 of 4 of concepts/csidriver/features/powerflex.md (split because the page is big). -->

## Volume Snapshot Feature

The CSI PowerFlex driver versions 2.0 and higher support v1 snapshots.

In order to use Volume Snapshots, ensure the following components are deployed to your cluster:
- Kubernetes Volume Snapshot CRDs
- Volume Snapshot Controller

### Volume Snapshot Class

Installation of PowerFlex driver v1.5 and later does not create VolumeSnapshotClass. You can find a sample of a default v1
VolumeSnapshotClass instance in `samples/volumesnapshotclass` directory. If needed, you can install the default sample. Following is the default sample for v1:

```yaml
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshotClass
metadata:
  name: vxflexos-snapclass
driver: csi-vxflexos.dellemc.com
# Configure what happens to a VolumeSnapshotContent when the VolumeSnapshot object
# it is bound to is to be deleted
# Allowed values:
#   Delete: the underlying storage snapshot will be deleted along with the VolumeSnapshotContent object.
#   Retain: both the underlying snapshot and VolumeSnapshotContent remain.
deletionPolicy: Delete
```

### Create Volume Snapshot

The following is a sample manifest for creating a Volume Snapshot using the v1 snapshot APIs:

```yaml
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshot
metadata:
  name: pvol0-snap1
  namespace: helmtest-vxflexos
spec:
  volumeSnapshotClassName: vxflexos-snapclass
  source:
    persistentVolumeClaimName: pvol0
```

Once the VolumeSnapshot is successfully created by the CSI PowerFlex driver, a VolumeSnapshotContent object is automatically created. Once the status of the VolumeSnapshot object has the _readyToUse_ field set to _true_, it is available for use.

Following is the relevant section of VolumeSnapshot object status:
```yaml
status:
  boundVolumeSnapshotContentName: snapcontent-5a8334d2-eb40-4917-83a2-98f238c4bda
  creationTime: "2020-07-16T08:42:12Z"
  readyToUse: true
```

### Creating PVCs with Volume Snapshots as Source

The following is a sample manifest for creating a PVC with a VolumeSnapshot as a source:
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: restorepvc
  namespace: helmtest-vxflexos
spec:
  storageClassName: vxflexos
  dataSource:
    name: pvol0-snap
    kind: VolumeSnapshot
    apiGroup: snapshot.storage.k8s.io
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 8Gi
```


## Volume Expansion Feature

The CSI PowerFlex driver version 1.2 and later support expansion of Persistent Volumes. This expansion is done online, which is when PVC is attached to a node.

To use this feature, the storage class used to create the PVC must have the attribute _allowVolumeExpansion_ set to _true_.

Following is a sample manifest for a storage class that allows for Volume Expansion:
```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: vxflexos-expand
  annotations:
provisioner: csi-vxflexos.dellemc.com
reclaimPolicy: Delete
allowVolumeExpansion: true
parameters:
  storagepool: pool
volumeBindingMode: WaitForFirstConsumer
allowedTopologies:
- matchLabelExpressions:
  - key: csi-vxflexos.dellemc.com/sample
    values:
    - csi-vxflexos.dellemc.com
```
To resize a PVC, edit the existing PVC spec and set _spec.resources.requests.storage_ to the intended size.

For example, if you have a PVC - pvol0 of size 8Gi, then you can resize it to 16 Gi by updating the PVC:
```yaml
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 16Gi #update from 8Gi
  storageClassName: vxflexos
  volumeMode: Filesystem
  volumeName: k8s-0e50dada
status:
  accessModes:
  - ReadWriteOnce
  capacity:
    storage: 8Gi
  phase: Bound
```
> *NOTE:* Kubernetes Volume Expansion feature cannot be used to shrink a volume and volumes cannot be expanded to a value that is not a multiple of 8. If attempted, the driver will round up. For example, if the above PVC was edited to have a size of 20 Gb, the size would actually be expanded to 24 Gb, the next highest multiple of 8.


## Volume Cloning Feature

The CSI PowerFlex driver version 1.3 and later support volume cloning. This feature allows specifying existing PVCs in the _dataSource_ field to indicate a user would like to clone a Volume.

The source PVC must be bound and available (not in use). Source and destination PVC must be in the same namespace and have the same Storage Class.

To clone a volume, you must first have an existing pvc, for example, pvol0:

```yaml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: pvol0
  namespace: helmtest-vxflexos
spec:
  storageClassName: vxflexos
  accessModes:
  - ReadWriteOnce
  volumeMode: Filesystem
  resources:
    requests:
      storage: 8Gi
```

The following is a sample manifest for cloning pvol0:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: clonedpvc
  namespace: helmtest-vxflexos
spec:
  storageClassName: vxflexos
  dataSource:
    name: pvol0
    kind: PersistentVolumeClaim
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 8Gi
```


## Raw Block Support

The CSI PowerFlex driver version 1.2 and later support Raw Block volumes, which are created using the _volumeDevices_ list in the pod template spec with each entry accessing a volumeClaimTemplate specifying a _volumeMode: Block_.

Following is an example configuration of **Raw Block Outline**:

```yaml
kind: StatefulSet
apiVersion: apps/v1
metadata:
    name: powerflextest
    namespace: helmtest-vxflexos
spec:
    ...
    spec:
      ...
      containers:
        - name: test
        ...
        volumeDevices:
          - devicePath: "/dev/data0"
            name: pvol
    volumeClaimTemplates:
    - metadata:
        name: pvol
      spec:
        accessModes:
        - ReadWriteOnce
        volumeMode: Block
        storageClassName: vxflexos
        resources:
          requests:
          storage: 8Gi
```

Allowable access modes are _ReadWriteOnce_, _ReadWriteMany_, and for block devices that have been previously initialized, _ReadOnlyMany_.

Raw Block volumes are presented as a block device to the pod by using a bind mount to a block device in the node's file system. The driver does not format or check the format of any file system on the block device. Raw Block volumes do support online Volume Expansion, but it is up to the application to manage to reconfigure the file system (if any) to the new size.

For additional information, see the [Kubernetes Raw Block Volume Support documentation](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#volume-mode).


## Custom File System Format Options

The CSI PowerFlex driver version 1.5 and later support additional mkfs format options. A user is able to specify additional format options as needed for the driver. Format options are specified in storageclass yaml under _mkfsFormatOption_ as in the following example:

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: vxflexos
  annotations:
    storageclass.kubernetes.io/is-default-class: "true"
provisioner: csi-vxflexos.dellemc.com
reclaimPolicy: Delete
allowVolumeExpansion: true
parameters:
  storagepool: <STORAGE_POOL> # Insert Storage pool
  systemID: <SYSTEM_ID> # Insert System ID
  mkfsFormatOption: "<mkfs_format_option>" # Insert file system format option
volumeBindingMode: WaitForFirstConsumer
allowedTopologies:
- matchLabelExpressions:
  - key: csi-vxflexos.dellemc.com/<SYSTEM_ID> # Insert System ID
    values:
    - csi-vxflexos.dellemc.com

```

- *WARNING*: Before utilizing format options, you must first be fully aware of the potential impact and understand your environment's requirements for the specified option.


## Topology Support

The CSI PowerFlex driver version 1.2 and later supports Topology which forces volumes to be placed on worker nodes that have connectivity to the backend storage. This covers use cases where:

- The PowerFlex SDC may not be installed or running on some nodes.
- Users have chosen to restrict the nodes on which the CSI driver is deployed.

This Topology support does not include customer-defined topology, users cannot create their own labels for nodes and storage classes and expect the labels to be honored by the driver.

### Topology Usage

To utilize the Topology feature, the storage classes are modified to specify the _volumeBindingMode_ as _WaitForFirstConsumer_ and to specify the desired topology labels within _allowedTopologies_. This ensures that the pod schedule takes advantage of the topology and be guaranteed that the node selected has access to provisioned volumes.

Storage Class Example with Topology Support:

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  annotations:
    meta.helm.sh/release-name: vxflexos
    meta.helm.sh/release-namespace: vxflexos
    storageclass.kubernetes.io/is-default-class: "true"
  creationTimestamp: "2020-05-27T13:24:55Z"
  labels:
    app.kubernetes.io/managed-by: Helm
  name: vxflexos
  resourceVersion: "170198"
  selfLink: /apis/storage.k8s.io/v1/storageclasses/vxflexos
  uid: abb094e6-2c25-42c1-b82e-bd80372e78b
parameters:
  storagepool: pool
provisioner: csi-vxflexos.dellemc.com
reclaimPolicy: Delete
volumeBindingMode: WaitForFirstConsumer
allowedTopologies:
- matchLabelExpressions:
  - key: csi-vxflexos.dellemc.com/6c29fd07674c
    values:
    - csi-vxflexos.dellemc.com
```

For additional information, see the [Kubernetes Topology documentation](https://kubernetes-csi.github.io/docs/topology.html).

> *NOTE*: In the manifest file of the Container Storage Modules operator, topology can be enabled by specifying the system name or _systemid_ in the allowed topologies field. _Volumebindingmode_ is also set to _WaitForFirstConsumer_ by default.


## Controller HA

The CSI PowerFlex driver version 1.3 and later support multiple controller pods. A Controller pod can be assigned to a worker node or a master node, as long as no other controller pod is currently assigned to the node. To control the number of controller pods, edit:

```yaml
controllerCount: 2
```

in your values file to the desired number of controller pods. By default, the driver will deploy with two controller pods, each assigned to a different worker node.

> *NOTE:* If the controller count is greater than the number of available nodes, excess controller pods will be stuck in a pending state.

If you are using the Container Storage Modules Operator, the value to adjust is:

```yaml
replicas: 1
```

in your driver yaml in `config/samples/`

If you want to specify where controller pods get assigned, make the following edits to your values file at `csi-vxflexos/helm/csi-vxflexos/values.yaml`:

To assign controller pods to worker nodes only (Default):

```yaml
# "controller" allows to configure controller specific parameters
controller:

  #"controller.nodeSelector" defines what nodes would be selected for pods of controller deployment
  # Leave as blank to use all nodes
  # Allowed values: map of key-value pairs
  # Default value: None
  # Examples:
  #   node-role.kubernetes.io/master: ""
  nodeSelector:
  #   node-role.kubernetes.io/master: ""

  # "controller.tolerations" defines tolerations that would be applied to controller deployment
  # Leave as blank to install controller on worker nodes
  # Default value: None
  tolerations:
  # - key: "node-role.kubernetes.io/master"
  #   operator: "Exists"
  #   effect: "NoSchedule"

```

To assign controller pods to master and worker nodes:

```yaml
# "controller" allows to configure controller specific parameters
controller:

  #"controller.nodeSelector" defines what nodes would be selected for pods of controller deployment
  # Leave as blank to use all nodes
  # Allowed values: map of key-value pairs
  # Default value: None
  # Examples:
  #   node-role.kubernetes.io/master: ""
  nodeSelector:
  #   node-role.kubernetes.io/master: ""

  # "controller.tolerations" defines tolerations that would be applied to controller deployment
  # Leave as blank to install controller on worker nodes
  # Default value: None
  tolerations:
   - key: "node-role.kubernetes.io/master"
     operator: "Exists"
     effect: "NoSchedule"
```

To assign controller pods to master nodes only:

```yaml
# "controller" allows to configure controller specific parameters
controller:

  #"controller.nodeSelector" defines what nodes would be selected for pods of controller deployment
  # Leave as blank to use all nodes
  # Allowed values: map of key-value pairs
  # Default value: None
  # Examples:
  #   node-role.kubernetes.io/master: ""
  nodeSelector:
     node-role.kubernetes.io/master: ""

  # "controller.tolerations" defines tolerations that would be applied to controller deployment
  # Leave as blank to install controller on worker nodes
  # Default value: None
  tolerations:
   - key: "node-role.kubernetes.io/master"
     operator: "Exists"
     effect: "NoSchedule"
```

> *NOTE:* Tolerations/selectors work the same way for node pods.

For configuring Controller HA on the Container Storage Modules Operator, please refer to the [Container Storage Modules Operator documentation](../../../getting-started/installation/operator/#custom-resource-definitions).


## SDC Deployment

The CSI PowerFlex driver version 1.3 and later support the automatic deployment of the PowerFlex SDC on Kubernetes nodes which run the node portion of the CSI driver. The deployment of the SDC kernel module occurs on these nodes with OS platforms which support automatic SDC deployment: currently Red Hat CoreOS (RHCOS), RHEL8.x,RHEL 7.9 are the only supported OS platforms. On Kubernetes nodes with OS version not supported by automatic install, you must perform the Manual SDC Deployment steps below. Refer to https://quay.io/repository/dell/storage/powerflex/sdc for supported OS versions.

- On Kubernetes nodes which run the node portion of the CSI driver, the SDC init container runs prior to the driver being installed. It installs the SDC kernel module on the nodes with OS version which supports automatic SDC deployment. If there is an SDC kernel module installed then the version is checked and updated.
- Optionally, if the SDC monitor is enabled, another container is started and runs as the monitor. Follow PowerFlex SDC documentation to get monitor metrics.
- On nodes that do not support automatic SDC deployment by SDC init container, manual installation steps must be followed. The SDC init container skips installing and you can see this mentioned in the logs by running kubectl logs on the node for SDC.
Refer to https://quay.io/repository/dell/storage/powerflex/sdc for supported OS versions.
- There is no automated uninstallation of the SDC kernel module. Follow PowerFlex SDC documentation to manually uninstall the SDC driver from the node.

From Container Storage Modules **1.12.0**, you can disable automatic SDC deployment.

By default, SDC deployment is enabled. If you do not want to deploy `sdc` with PowerFlex, it can be disabled by setting the `sdc.enabled` field to `false`.

```yaml
node:
  ...
  sdc:
    # enabled: Enable/Disable SDC
    enabled: true
```


## Multiarray Support

The CSI PowerFlex driver version 1.4 added support for managing multiple PowerFlex arrays from the single driver instance. This feature is enabled by default and integrated to even single instance installations.When configuring the driver with multiple PowerFlex arrays, the blockProtocol value must be the same for all arrays.

To manage multiple arrays you need to create an array connection configuration that lists multiple arrays.

### Creating array configuration

There is a sample yaml file in the samples folder called `secret.yaml` with the following content:
 ```yaml
  # Username for accessing PowerFlex system.
  # If authorization is enabled, username will be ignored.
  - username: "admin"
  # Password for accessing PowerFlex system.
  # If authorization is enabled, password will be ignored.
  password: "password"
  # PowerFlex system name or ID.
  # Required: true
  systemID: "1a99aa999999aa9a"
  # Required: false
  # Previous names used in secret of PowerFlex system. Only needed if PowerFlex System Name has been changed by user
  # and old resources are still based on the old name.
  allSystemNames: "pflex-1,pflex-2"
  # REST API gateway HTTPS endpoint for PowerFlex system.
  # If authorization is enabled, endpoint should be the HTTPS localhost endpoint that
  # the authorization sidecar will listen on
  endpoint: "https://127.0.0.1"
    # Determines if the driver is going to validate certs while connecting to PowerFlex REST API interface.
    # Allowed values: true or false
    # Default value: true
  skipCertificateValidation: true
  # indicates if this array is the default array
  # needed for backwards compatibility
  # only one array is allowed to have this set to true
  # Default value: false
  isDefault: true
  # defines the MDM(s) that SDC should register with on start.
  # Allowed values:  a list of IP addresses or hostnames separated by comma.
  # Default value: none
  mdm: "10.0.0.1,10.0.0.2"
  # Defines all system names used to create powerflex volumes
  # Required: false
  # Default value: none
  AllSystemNames: "name1,name2"
- username: "admin"
  password: "Password123"
  systemID: "2b11bb111111bb1b"
  endpoint: "https://127.0.0.2"
  skipCertificateValidation: true
  mdm: "10.0.0.3,10.0.0.4"
  AllSystemNames: "name1,name2"
 ```
The systemID can be found by displaying system level information, which is outlined [here](https://infohub.delltechnologies.com/l/powerflex-rest-api-introduction/system-information)

Here we specify that we want the CSI driver to manage two arrays: one with an IP `127.0.0.1` and the other with an IP `127.0.0.2`.

To use this config we need to create a Kubernetes secret from it. To do so, run the following command:

```bash
kubectl create secret generic vxflexos-config -n vxflexos --from-file=config=secret.yaml
```


## Dynamic Array Configuration

To update or change any array configuration property, edit the secret. The driver will detect the change automatically and use the new values based on the Kubernetes watcher file change detection time.  You can use kubectl command to delete the current secret and create a new secret with changes. For example, refer yaml above and change only the password.
```yaml
 - username: "admin"
   password: "Password123"
```
to
```yaml
 - username: "admin"
   password: "Password456"
```
Below are sample command lines to delete a secret and create modified properties from file `secret.yaml`.
```bash
kubectl delete secret vxflexos-config  -n vxflexos
kubectl create secret generic vxflexos-config -n vxflexos --from-file=config=./secret.yaml
```
Dynamic array configuration change detection is only used for properties of an existing array, like username or password.
To add a new array to the secret, or to alter an array's mdm field, you must run `csi-install.sh` with `--upgrade` option to update the MDM key in secret and restart the node pods.
```bash
cd <DRIVER-HOME>/dell-csi-helm-installer
./csi-install.sh --namespace vxflexos --values ./myvalues.yaml --upgrade
 kubectl delete  pods --all -n vxflexos
```

### Creating storage classes

To be able to provision Kubernetes volumes using a specific array, we need to create corresponding storage classes.

Find the sample yaml files under `samples/storageclass`. Edit `storageclass.yaml` if you want `ext4` filesystem, and use `storageclass-xfs.yaml` if you want `xfs` filesystem. Replace `<STORAGE_POOL>` with the storage pool you have, and replace `<SYSTEM_ID>` with the system ID or system name for the array you'd like to use.

Then we need to apply storage classes to Kubernetes using `kubectl`:

```bash
kubectl apply -f storageclass.yaml
```

After that, you can use the storage class for the corresponding array.
