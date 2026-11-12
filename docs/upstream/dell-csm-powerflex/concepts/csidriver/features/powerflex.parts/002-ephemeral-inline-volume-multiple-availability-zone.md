<!-- Part 2 of 4 of concepts/csidriver/features/powerflex.md (split because the page is big). -->

## Ephemeral Inline Volume

Starting from version 1.4, CSI PowerFlex driver supports ephemeral inline CSI volumes. This feature allows CSI volumes to be specified directly in the pod specification.

At runtime, nested inline volumes follow the ephemeral lifecycle of their associated pods where the driver handles all phases of volume operations as pods are created and destroyed.

The following is a sample manifest (found in csi-vxflexos/test/helm/ephemeral) for creating ephemeral volume in pod manifest with CSI PowerFlex driver.

```yaml
kind: Pod
apiVersion: v1
metadata:
  name: my-csi-app-inline-volumes
spec:
  containers:
    - name: my-frontend
      image: busybox
      command: [ "sleep", "100000" ]
      volumeMounts:
      - mountPath: "/data0"
        name: my-csi-volume
      - mountPath: "/data1"
        name: my-csi-volume-xfs
  volumes:
  - name: my-csi-volume
    csi:
      driver: csi-vxflexos.dellemc.com
      fsType: "ext4"
      volumeAttributes:
        volumeName: "my-csi-volume"
        size: "8Gi"
        storagepool: sample
        systemID: sample
  - name: my-csi-volume-xfs
    csi:
      driver: csi-vxflexos.dellemc.com
      fsType: "xfs"
      volumeAttributes:
        volumeName: "my-csi-volume-xfs"
        size: "10Gi"
        storagepool: sample
        systemID: sample

```

This manifest creates a pod and attach two newly created ephemeral inline csi volumes to it, one ext4 and the other xfs.
To run the corresponding helm test, go to csi-vxflexos/test/helm/ephemeral and fill in the values for storagepool and systemID in sample.yaml.
Then run:
```bash
./testEphemeral.sh
```
this test deploys the pod with two ephemeral volumes, and write some data to them before deleting the pod.
When creating ephemeral volumes, it is important to specify the following within the volumeAttributes section: volumeName, size, storagepool, and if you want to use a non-default array, systemID.


## Consuming Existing Volumes with Static Provisioning

To use existing volumes from PowerFlex array as Persistent volumes in your Kubernetes environment, perform these steps:
1. Log into one of the MDMs of the PowerFlex cluster.
2. Execute these commands to retrieve the `systemID` and `volumeID`.
    1. ```bash
        scli --mdm_ip <IPs, comma separated> --login --username <username> --password <password>
       ```
    - **Output:** `Logged in. User role is SuperUser. System ID is <systemID>`
    2. ```bash
        scli --query_volume --volume_name <volume name>
       ```
    - **Output:** `Volume ID: <volumeID> Name: <volume name>`
3. Create PersistentVolume and use this volume ID in the volumeHandle with the format `systemID`-`volumeID` in the manifest. Modify other parameters according to your needs.
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: existingVol
spec:
  capacity:
    storage: 8Gi
  csi:
    driver: csi-vxflexos.dellemc.com
    volumeHandle: <systemID>-<volumeID>
  volumeMode: Filesystem
  accessModes:
  - ReadWriteOnce
  storageClassName: vxflexos
```
4. Create PersistentVolumeClaim to use this PersistentVolume.
```yaml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: pvol
spec:
  accessModes:
  - ReadWriteOnce
  volumeMode: Filesystem
  resources:
    requests:
      storage: 8Gi
  storageClassName: vxflexos
```
5. Then use this PVC as a volume in a pod.
```yaml
apiVersion: v1
kind: Pod
metadata:
    name: static-prov-pod
spec:
    containers:
      - name: test
        image: busybox
        command: [ "sleep", "3600" ]
        volumeMounts:
          - mountPath: "/data0"
            name: pvol
    volumes:
      - name: pvol
        persistentVolumeClaim:
            claimName: pvol
```
6. After the pod is `Ready` and `Running`, you can start to use this pod and volume.

**Note:** Retrieval of the volume ID is possible through the UI. You must select the volume, navigate to `Details` section and click the volume in the graph. This selection will set the filter to the desired volume. At this point the volume ID can be found in the URL.


## Dynamic Logging Configuration

The dynamic logging configuration that was introduced in v1.5 of the driver was revamped for v2.0; v1.5 logging configuration is not compatible with v2.0.
Two fields in values.yaml (located at helm/csi-vxflexos/values.yaml) are used to configure the dynamic logging: logLevel and logFormat.

```yaml
# CSI driver log level
# Allowed values: "error", "warn"/"warning", "info", "debug"
# Default value: "debug"
logLevel: "debug"

# CSI driver log format
# Allowed values: "TEXT" or "JSON"
# Default value: "TEXT"
logFormat: "TEXT"
```

To change the logging fields after the driver is deployed, you can use this command to edit the configmap:
```bash
 kubectl edit configmap -n vxflexos vxflexos-config-params
```
and then make the necessary adjustments for CSI_LOG_LEVEL and CSI_LOG_FORMAT.

If either option is set to a value outside of what is supported, the driver will use the default values of "debug" and "text" .


## Volume Health Monitoring

> *NOTE*: Alpha feature gate `CSIVolumeHealth` needs to be enabled for the node side monitoring to take effect. For more information, please refer to the [Kubernetes GitHub repository](https://github.com/kubernetes-csi/external-health-monitor/blob/master/README.md). If the feature gate is on, and you want to use this feature,
> ensure the proper values are enabled in your values file. See the values table in the installation doc for more details.

Starting in version 2.1, CSI Driver for PowerFlex now supports volume health monitoring. This allows Kubernetes to report on the condition of the underlying volumes via events when a volume condition is abnormal. For example, if a volume were to be deleted from the array, or unmounted outside of Kubernetes, Kubernetes will now report these abnormal conditions as events.

To accomplish this, the driver utilizes the external-health-monitor sidecar. When driver detects a volume condition is abnormal, the sidecar will report an event to the corresponding PVC. For example, in this event from `kubectl describe pvc -n <ns>` we can see that the underlying volume was deleted from the PowerFlex array:

```text
Events:
  Type     Reason                     Age                 From                                                         Message
  ----     ------                     ----                ----                                                         ------
  Warning  VolumeConditionAbnormal    32s                 csi-pv-monitor-controller-csi-vxflexos.dellemc.com           Volume is not found at 2021-11-03 20:31:04
```

Events will also be reported to pods that have abnormal volumes. In these two events from `kubectl describe pods -n <ns>`, we can see that this pod has two abnormal volumes: one volume was unmounted outside of Kubernetes, while another was deleted from PowerFlex array.

```text
Events:
  Type     Reason                     Age                 From         Message
  ----     ------                     ----                ----         ------
Warning  VolumeConditionAbnormal      35s (x9 over 12m)  kubelet       Volume vol4: volPath: /var/.../rhel-705f0dcbf1/mount is not mounted: <nil>
Warning  VolumeConditionAbnormal      5s                 kubelet       Volume vol2: Volume is not found by node driver at 2021-11-11 02:04:49
```


## Set QoS Limits
Starting in version 2.5, CSI Driver for PowerFlex now supports setting the limits for the bandwidth and IOPS that one SDC generates for the specified volume. This enables the CSI driver to control the quality of service (QoS).
In this release this is supported at the StorageClass level, so once a volume is created QoS Settings can't be adjusted later.
To accomplish this, two new parameters are introduced in the storage class: bandwidthLimitInKbps and iopsLimit.
> Ensure that the proper values are enabled in your storage class yaml files. Refer to the [sample storage class yamls](https://github.com/dell/csi-powerflex/tree/main/samples/storageclass) for more details.

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
    storagepool: "pool2" # Insert Storage pool
    systemID: <SYSTEM_ID> # Insert System ID
    bandwidthLimitInKbps: "10240" # Insert bandwidth limit in Kbps
    iopsLimit: "11" # Insert iops limit
    csi.storage.k8s.io/fstype: ext4
volumeBindingMode: WaitForFirstConsumer
allowedTopologies:
  - matchLabelExpressions:
      - key: csi-vxflexos.dellemc.com/<SYSTEM_ID> # Insert System ID
        values:
          - csi-vxflexos.dellemc.com
```
Once the volume gets created, the ControllerPublishVolume will set the QoS limits for the volumes mapped to SDC.


## Rename SDC

Starting with version 2.6, the CSI driver for PowerFlex will support renaming of SDCs. To use this feature, the node section of values.yaml should have renameSDC keys enabled with a prefix value.

To enable renaming of SDC, make the following edits to [values.yaml](https://github.com/dell/helm-charts/blob/main/charts/csi-vxflexos/values.yaml) file:
```yaml
# "node" allows to configure node specific parameters
node:
   ...
   ...

  # "renameSDC" defines the rename operation for SDC
  # Default value: None
  renameSDC:
    # enabled: Enable/Disable rename of SDC
    # Allowed values:
    #   true: enable renaming
    #   false: disable renaming
    # Default value: "false"
    enabled: false
    # "prefix" defines a string for the new name of the SDC.
    # "prefix" + "worker_node_hostname" should not exceed 31 chars.
    # Default value: none
    # Examples: "rhel-sdc", "sdc-test"
    prefix: "sdc-test"
```
The renameSDC section is going to be used by the Node Service, it has two keys enabled and prefix:
* `enabled`: Boolean variable that specifies if the renaming for SDC is to be carried out or not. If true then the driver will perform the rename operation. By default, its value will be false.
* `prefix`: string variable that is used to set the prefix for SDC name.

Based on these two keys, there are certain scenarios on which the driver is going to perform the rename SDC operation:
* If enabled and prefix given then set the prefix+worker_node_name for SDC name.
* If enabled and prefix not given then set worker_node_name for SDC name.

> ℹ️ **NOTE:** : name of the SDC cannot be more than 31 characters, hence the prefix given and the worker node hostname name taken should be such that the total length does not exceed 31 character limit.


## Pre-approving SDC

Starting with version 2.15, the CSI Driver for PowerFlex will support pre-approving SDC by either GUID or IP address.
CSI PowerFlex driver will detect the SDC mode set on the PowerFlex array and will request SDC approval from the array prior to publishing a volume. This is specific to each SDC.

To request SDC approval either by GUID or IP address, make the following edits to [values.yaml](https://github.com/dell/helm-charts/blob/main/charts/csi-vxflexos/values.yaml) file:
```yaml
# "node" allows to configure node specific parameters
node:
  ...
  ...

  # "approveSDC" defines the approve operation for SDC
  # Default value: None
  approveSDC:
    # enabled: Enable/Disable SDC approval
    #Allowed values:
    #  true: Driver will enable SDC approval based on either GUID or IP address, depending on the restricted SDC mode configured in PowerFlex system
    #  false: Driver will disable SDC approval based on either GUID or IP address, depending on the restricted SDC mode configured in PowerFlex system
    # Default value: false
    enabled: false
```
> ℹ️ **NOTE:** : Currently, the CSI-PowerFlex driver only supports GUID for the restricted SDC mode.

If SDC approval is denied, then provisioning of the volume will not be attempted and an appropriate error message is reported in the logs/events so the user is informed.


## Volume Limit

The CSI Driver for Dell PowerFlex allows users to specify the maximum number of PowerFlex volumes that can be used in a node.

The user can set the volume limit for a node by creating a node label `max-vxflexos-volumes-per-node` and specifying the volume limit for that node.
<br/> `kubectl label node <node_name> max-vxflexos-volumes-per-node=<volume_limit>`

The user can also set the volume limit for all the nodes in the cluster by specifying the same to `maxVxflexosVolumesPerNode` attribute in values.yaml file.

>**NOTE:** <br>To reflect the changes after setting the value either via node label or in values.yaml file, user has to bounce the driver controller and node pods using the command `kubectl get pods -n vxflexos --no-headers=true | awk '/vxflexos-/{print $1}'| xargs kubectl delete -n vxflexos pod`. <br><br> If the value is set both by node label and values.yaml file then node label value will get the precedence and user has to remove the node label in order to reflect the values.yaml value. <br><br>The default value of `maxVxflexosVolumesPerNode` is 0. <br><br>If `maxVxflexosVolumesPerNode` is set to zero, then Container Orchestration decides how many volumes of this type can be published by the controller to the node.<br><br>The volume limit specified to `maxVxflexosVolumesPerNode` attribute is applicable to all the nodes in the cluster for which node label `max-vxflexos-volumes-per-node` is not set.


## Volume Size and Rounding Rules

For Block Volumes, the minimum supported size is 8 Gi. Any size request below 8 Gi will result in a volume of 8 Gi being created. Additionally, if the requested size is not a multiple of 8, the system will round it up to the next multiple of 8 when provisioning the volume.

For example:
A requested size of 9 Gi or 8.1 Gi will result in a 16 Gi volume being created on the backend array.
Similarly, a size of 20 Gi will be rounded up to 24 Gi.
This behavior ensures that the allocated volume sizes comply with the backend array's alignment requirements.


## Storage Capacity Tracking
CSI-PowerFlex driver version 2.8.0 and above supports Storage Capacity Tracking.

This feature helps the scheduler to make more informed choices about where to schedule pods which depend on unbound volumes with late binding (aka "wait for first consumer"). Pods will be scheduled on a node (satisfying the topology constraints) only if the requested capacity is available on the storage array.
If such a node is not available, the pods stay in Pending state. This means pods are not scheduled.

Without storage capacity tracking, pods get scheduled on a node satisfying the topology constraints. If the required capacity is not available, volume attachment to the pods fails, and pods remain in ContainerCreating state. Storage capacity tracking eliminates unnecessary scheduling of pods when there is insufficient capacity.

The attribute `storageCapacity.enabled` in `values.yaml` can be used to enable/disable the feature during driver installation using helm. This is by default set to true. To configure how often the driver checks for changed capacity set `storageCapacity.pollInterval` attribute. In case of driver installed via operator, this interval can be configured in the sample file provided [here](https://github.com/dell/csm-operator/blob/release/{{< version-docs key="csm-operator_latest_version">}}/samples/{{< version-docs key="csm-operator_latest_samples_dir" >}}/storage_csm_powerflex_{{< version-docs key="Det_sample_operator_pflex" >}}.yaml) by editing the `--capacity-poll-interval` argument present in the provisioner sidecar.


## Multiple Availability Zones
PowerFlex CSI driver version 2.13.0 and above supports multiple Availability Zones for Block. NFS is not supported at this time.

This feature supports the use of a StorageClass that is not associated with any specific PowerFlex system or storage pool. Each cluster node must be labeled with a zone and each PowerFlex system must be assigned to a single zone. When a Pod is scheduled on a node, the volume will be provisioned on the PowerFlex system associated with the cluster node's zone.

Requirements:
- Every cluster worker node must be labeled with a zone label.
- Every PowerFlex system in the driver Secret must be assigned to their own zone.
- The StorageClass does not contain any reference to the SystemID or storagepool.
- Use the CSM Operator to install the PowerFlex CSI driver. The CSM Operator will detect if multiple Availability Zones are enabled in the driver Secret and ensure the correct MDMs are configured on each worker node during the SDC installation.

> Note: Helm deployment currently doesn’t support multiple Availability Zones.

The example manifests below illustrate how to configure two PowerFlex systems, with each system assigned to its own zone. Zone labels can have any custom key, but it must be consistent across the StorageClass, Secret, and Node labels.

#### Labeling Worker Nodes
```bash
# Label each worker node in the cluster
kubectl label nodes worker-1 topology.kubernetes.io/zone=zone1
kubectl label nodes worker-2 topology.kubernetes.io/zone=zone1
...
kubectl label nodes worker-3 topology.kubernetes.io/zone=zone2
kubectl label nodes worker-4 topology.kubernetes.io/zone=zone2
```

#### StorageClass
For multiple Availability Zones support, the StorageClass does not require details about the PowerFlex system. Optionally, the `allowedTopologies` can be used to specify topology labels used when provisioning volumes with this StorageClass.

> Note: The StorageClass must use `volumeBindingMode: WaitForFirstConsumer`. Using `volumeBindingMode: Immediate` **will not guarantee** that the volume is provisioned in the same zone as the scheduled Pod.

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
allowVolumeExpansion: true
allowedTopologies:
- matchLabelExpressions:
  - key: topology.kubernetes.io/zone
    values:
    - zone1
    - zone2
metadata:
  name: powerflex-multiaz
parameters:
  csi.storage.k8s.io/fstype: ext4
provisioner: csi-vxflexos.dellemc.com
reclaimPolicy: Delete
volumeBindingMode: WaitForFirstConsumer
```

#### Secret
The Secret specifies the zone associated with each PowerFlex system along with additional details such as the protection domain and storage pool name.

> Note: The protection domain name is required if storage pool names are not unique across protection domains.

```yaml
- username: "user"
  password: "password"
  systemID: "2000000000000001"
  endpoint: "https://10.0.0.1"
  skipCertificateValidation: true
  mdm: "10.0.0.2,10.0.0.3"
  zone:
    name: "zone1"
    labelKey: "topology.kubernetes.io/zone"
    protectionDomains:
      - name: "domain1"
        pools:
          - "pool1"

- username: "user"
  password: "password"
  systemID: "2000000000000002"
  endpoint: "https://10.0.0.4"
  skipCertificateValidation: true
  mdm: "10.0.0.5,10.0.0.6"
  zone:
    name: "zone2"
    labelKey: "topology.kubernetes.io/zone"
    protectionDomains:
      - name: "domain2"
        pools:
          - "pool2"
```
