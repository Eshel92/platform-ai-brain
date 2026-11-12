<!-- Part 168 of 193 of reference/crd/k8ssandra-operator-crds-latest/_index.md (split because the page is big). -->

### Medusa
<sup><sup>[↩ Parent](#medusak8ssandraiov1alpha1 )</sup></sup>








<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
      <td><b>apiVersion</b></td>
      <td>string</td>
      <td>medusa.k8ssandra.io/v1alpha1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>Medusa</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.20/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#medusaspec">spec</a></b></td>
        <td>object</td>
        <td>
          MedusaSpec defines the desired state of Medusa.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### Medusa.spec
<sup><sup>[↩ Parent](#medusa)</sup></sup>



MedusaSpec defines the desired state of Medusa.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>cassandraUserSecretRef</b></td>
        <td>string</td>
        <td>
          Defines the username and password that Medusa will use to authenticate CQL connections to Cassandra clusters. These credentials will be automatically turned into CQL roles by cass-operator when bootstrapping the datacenter, then passed to the Medusa instances, so that it can authenticate against nodes in the datacenter using CQL. The secret must be in the same namespace as Cassandra and must contain two keys: "username" and "password".<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#medusaspeccontainerimage">containerImage</a></b></td>
        <td>object</td>
        <td>
          MedusaContainerImage is the image characteristics to use for Medusa containers. Leave nil to use a default image.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#medusaspecsecuritycontext">securityContext</a></b></td>
        <td>object</td>
        <td>
          SecurityContext applied to the Medusa containers.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#medusaspecstorageproperties">storageProperties</a></b></td>
        <td>object</td>
        <td>
          Provides all storage backend related properties for backups.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### Medusa.spec.containerImage
<sup><sup>[↩ Parent](#medusaspec)</sup></sup>



MedusaContainerImage is the image characteristics to use for Medusa containers. Leave nil to use a default image.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>repository</b></td>
        <td>string</td>
        <td>
          <br/>
          <br/>
            <i>Default</i>: k8ssandra/medusa<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#medusaspeccontainerimageimagepullsecret">imagePullSecret</a></b></td>
        <td>object</td>
        <td>
          LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>pullPolicy</b></td>
        <td>string</td>
        <td>
          PullPolicy describes a policy for if/when to pull a container image<br/>
          <br/>
            <i>Default</i>: IfNotPresent<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>registry</b></td>
        <td>string</td>
        <td>
          <br/>
          <br/>
            <i>Default</i>: docker.io<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>tag</b></td>
        <td>string</td>
        <td>
          <br/>
          <br/>
            <i>Default</i>: latest<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### Medusa.spec.containerImage.imagePullSecret
<sup><sup>[↩ Parent](#medusaspeccontainerimage)</sup></sup>



LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### Medusa.spec.securityContext
<sup><sup>[↩ Parent](#medusaspec)</sup></sup>



SecurityContext applied to the Medusa containers.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>allowPrivilegeEscalation</b></td>
        <td>boolean</td>
        <td>
          AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no_new_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP_SYS_ADMIN<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#medusaspecsecuritycontextcapabilities">capabilities</a></b></td>
        <td>object</td>
        <td>
          The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>privileged</b></td>
        <td>boolean</td>
        <td>
          Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>procMount</b></td>
        <td>string</td>
        <td>
          procMount denotes the type of proc mount to use for the containers. The default is DefaultProcMount which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>readOnlyRootFilesystem</b></td>
        <td>boolean</td>
        <td>
          Whether this container has a read-only root filesystem. Default is false.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>runAsGroup</b></td>
        <td>integer</td>
        <td>
          The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.<br/>
          <br/>
            <i>Format</i>: int64<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>runAsNonRoot</b></td>
        <td>boolean</td>
        <td>
          Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>runAsUser</b></td>
        <td>integer</td>
        <td>
          The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.<br/>
          <br/>
            <i>Format</i>: int64<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#medusaspecsecuritycontextselinuxoptions">seLinuxOptions</a></b></td>
        <td>object</td>
        <td>
          The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#medusaspecsecuritycontextseccompprofile">seccompProfile</a></b></td>
        <td>object</td>
        <td>
          The seccomp options to use by this container. If seccomp options are provided at both the pod & container level, the container options override the pod options.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#medusaspecsecuritycontextwindowsoptions">windowsOptions</a></b></td>
        <td>object</td>
        <td>
          The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### Medusa.spec.securityContext.capabilities
<sup><sup>[↩ Parent](#medusaspecsecuritycontext)</sup></sup>



The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>add</b></td>
        <td>[]string</td>
        <td>
          Added capabilities<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>drop</b></td>
        <td>[]string</td>
        <td>
          Removed capabilities<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### Medusa.spec.securityContext.seLinuxOptions
<sup><sup>[↩ Parent](#medusaspecsecuritycontext)</sup></sup>



The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>level</b></td>
        <td>string</td>
        <td>
          Level is SELinux level label that applies to the container.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>role</b></td>
        <td>string</td>
        <td>
          Role is a SELinux role label that applies to the container.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>type</b></td>
        <td>string</td>
        <td>
          Type is a SELinux type label that applies to the container.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>user</b></td>
        <td>string</td>
        <td>
          User is a SELinux user label that applies to the container.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### Medusa.spec.securityContext.seccompProfile
<sup><sup>[↩ Parent](#medusaspecsecuritycontext)</sup></sup>



The seccomp options to use by this container. If seccomp options are provided at both the pod & container level, the container options override the pod options.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>type</b></td>
        <td>string</td>
        <td>
          type indicates which kind of seccomp profile will be applied. Valid options are: 
 Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>localhostProfile</b></td>
        <td>string</td>
        <td>
          localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet's configured seccomp profile location. Must only be set if type is "Localhost".<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### Medusa.spec.securityContext.windowsOptions
<sup><sup>[↩ Parent](#medusaspecsecuritycontext)</sup></sup>



The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>gmsaCredentialSpec</b></td>
        <td>string</td>
        <td>
          GMSACredentialSpec is where the GMSA admission webhook (https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>gmsaCredentialSpecName</b></td>
        <td>string</td>
        <td>
          GMSACredentialSpecName is the name of the GMSA credential spec to use.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>hostProcess</b></td>
        <td>boolean</td>
        <td>
          HostProcess determines if a container should be run as a 'Host Process' container. This field is alpha-level and will only be honored by components that enable the WindowsHostProcessContainers feature flag. Setting this field without the feature flag will result in errors when validating the Pod. All of a Pod's containers must have the same effective HostProcess value (it is not allowed to have a mix of HostProcess containers and non-HostProcess containers).  In addition, if HostProcess is true then HostNetwork must also be set to true.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>runAsUserName</b></td>
        <td>string</td>
        <td>
          The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### Medusa.spec.storageProperties
<sup><sup>[↩ Parent](#medusaspec)</sup></sup>



Provides all storage backend related properties for backups.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>apiProfile</b></td>
        <td>string</td>
        <td>
          AWS Profile to use for authentication.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>backupGracePeriodInDays</b></td>
        <td>integer</td>
        <td>
          Age after which orphan sstables can be deleted from the storage backend. Protects from race conditions between purge and ongoing backups. Defaults to 10 days.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>bucketName</b></td>
        <td>string</td>
        <td>
          The name of the bucket to use for the backups.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>concurrentTransfers</b></td>
        <td>integer</td>
        <td>
          Number of concurrent uploads. Helps maximizing the speed of uploads but puts more pressure on the network. Defaults to 1.<br/>
          <br/>
            <i>Default</i>: 1<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>host</b></td>
        <td>string</td>
        <td>
          Host to connect to for the storage backend.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>maxBackupAge</b></td>
        <td>integer</td>
        <td>
          Maximum backup age that the purge process should observe.<br/>
          <br/>
            <i>Default</i>: 0<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>maxBackupCount</b></td>
        <td>integer</td>
        <td>
          Maximum number of backups to keep (used by the purge process). Default is unlimited.<br/>
          <br/>
            <i>Default</i>: 0<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>multiPartUploadThreshold</b></td>
        <td>integer</td>
        <td>
          File size over which cloud specific cli tools are used for transfer. Defaults to 100 MB.<br/>
          <br/>
            <i>Default</i>: 104857600<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>port</b></td>
        <td>integer</td>
        <td>
          Port to connect to for the storage backend.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>prefix</b></td>
        <td>string</td>
        <td>
          Name of the top level folder in the backup bucket. If empty, the cluster name will be used.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>region</b></td>
        <td>string</td>
        <td>
          Region of the storage bucket. Defaults to "default".<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>secure</b></td>
        <td>boolean</td>
        <td>
          Whether to use SSL for the storage backend.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>storageProvider</b></td>
        <td>enum</td>
        <td>
          The storage backend to use for the backups.<br/>
          <br/>
            <i>Enum</i>: local, google_storage, azure_blobs, s3, s3_compatible, s3_rgw, ibm_storage<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>storageSecretRef</b></td>
        <td>string</td>
        <td>
          Kubernetes Secret that stores the key file for the storage provider's API. If using 'local' storage, this value is ignored.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>transferMaxBandwidth</b></td>
        <td>string</td>
        <td>
          Max upload bandwidth in MB/s. Defaults to 50 MB/s.<br/>
          <br/>
            <i>Default</i>: 50MB/s<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>
