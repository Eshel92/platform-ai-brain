<!-- Converted from reference/cluster-configuration.txt (reStructuredText). Includes are inlined. -->

# Automation Configuration

## Overview

The Automation uses an automation configuration to determine the
desired state of a MongoDB deployment and to effect changes as needed.
If you modify the deployment through the Ops Manager web interface, you never
need manipulate this configuration.

If you are using the Automation without Ops Manager, you can construct and
distribute the configuration manually.

Optional fields are marked as such.

A field that takes a `<number>` as its value can take integers and
floating point numbers.

**Warning:**

Ops Manager automation doesn't support or validate the following settings. Using them
could cause deployment failure or downtime.

- net.unixDomainSocket options such as
  `net.unixDomainSocket.enabled`, `net.unixDomainSocket.pathPrefix`,
  and `net.unixDomainSocket.filePermissions`.

- Ops Manager automation rejects deployments that contain internal settings such as
  `__exec` and `__rest`.

If you require these settings, you must manage the deployment manually without Ops Manager.

## Configuration Version

This lists the version of the automation configuration.

```json
"version" : "<integer>"
```

| Name | Type | Necessity | Description |
|---|---|---|---|
| version | integer | Required | Revision of this automation configuration file. |

## Download Base

Ops Manager downloads automatic versions and runs starting scripts in the directory set in **options.downloadBase**.

```json
"options" : {
  "downloadBase" : "<string>",
}
```

| Name | Type | Necessity | Description |
|---|---|---|---|
| options | object | Required | Path for automatic downloads of new versions. |
| options.downloadBase | string | Required | Directory on Linux and UNIX platforms for automatic version downloads and startup scripts. |

## MongoDB Versions Specifications

The `mongoDbVersions[n]` array defines specification objects for
the MongoDB instances found in the `processes` array. Each
MongoDB instance in the `processes` array must have a
specification object in this array.

```json
"mongoDbVersions[n]" : [
  {
   "name" : "<string>",
    "builds" : [
      {
       "platform" : "<string>",
        "url" : "<string>",
        "gitVersion" : "<string>",
        "modules" : [ "<string>", ... ],
        "architecture" : "<string>",
        "bits" : "<integer>",
        "win2008plus" : "<Boolean>",
        "winVCRedistUrl" : "<string>",
        "winVCRedistOptions" : [ "<string>", ... ],
        "winVCRedistDll" : "<string>",
        "winVCRedistVersion" : "<string>"
      },
      ...
    ],
  },
  ...
]
```

| Name | Type | Necessity | Description |
|---|---|---|---|
| mongoDbVersions[n] | array of objects | Required | Specification objects for the MongoDB instances found in the **processes** array. Each MongoDB instance in **processes** must have a specification object in **mongoDbVersions[n]**. |
| mongoDbVersions[n].name | string | Required | Name of the specification object. The specification object is attached to a MongoDB instance through the instance's **processes.version** parameter in this configuration. |
| mongoDbVersions[n].builds[k] | array of objects | Required | Builds available for this MongoDB instance. |
| mongoDbVersions[n].builds[k].platform | string | Required | Platform for this MongoDB instance. |
| mongoDbVersions[n].builds[k].url | string | Required | URL (Uniform Resource Locator) from which to download MongoDB for this instance. |
| mongoDbVersions[n].builds[k].gitVersion | string | Required | Commit identifier that identifies the state of the code used to build the MongoDB process. The MongoDB buildInfo command returns the gitVersion identifier. |
| mongoDbVersions[n].builds[k].modules | array | Required | List of modules for this version. Corresponds to the **modules** parameter that the **buildInfo** command returns. |
| mongoDbVersions[n].builds[k].architecture | string | Required | Processor's architecture. Ops Manager accepts **amd64** or **ppc64le**. |
| mongoDbVersions[n].builds[k].bits | integer | Deprecated | Processor's bus width. Don't remove or make modifications to this parameter. |
| mongoDbVersions[n].builds[k].win2008plus | Boolean | Optional | Set to **true** if this is a Windows build that requires either Windows 7 later or Windows Server 2008 R2 or later. |
| mongoDbVersions[n].builds[k].winVCRedistUrl | string | Optional | URL (Uniform Resource Locator) from which the required version of the Microsoft Visual C++ redistributable can be downloaded. |
| mongoDbVersions[n].builds[k].winVCRedistOptions | array of strings | Optional | String values that list the command-line options to be specified when running the Microsoft Visual C++ redistributable installer. Each command-line option is a separate string in the array. |
| mongoDbVersions[n].builds[k].winVCRedistDll | string | Optional | Name of the Microsoft Visual C++ runtime DLL file that the agent checks to determine if a new version of the Microsoft Visual C++ redistributable is needed. |
| mongoDbVersions[n].builds[k].winVCRedistVersion | string | Optional | Minimum version of the Microsoft Visual C++ runtime DLL that must be present to skip over the installation of the Microsoft Visual C++ redistributable. |

## Automation

**agentVersion** specifies the version of the MongoDB Agent.

**Note:**

While you can update the MongoDB Agent version through this
configuration property, you should use the
Update Agent Versions
endpoint to ensure your versions are up to date.

```json
"agentVersion" : {
  "name" : "<string>",
  "directoryUrl" : "<string>"
}
```

| Name | Type | Necessity | Description |
|---|---|---|---|
| agentVersion | object | Optional | Version of the MongoDB Agent to run. If the running version does not match this setting, the MongoDB Agent downloads the specified version, shuts itself down, and starts the new version. |
| agentVersion.name | string | Optional | Desired version of the MongoDB Agent. |
| agentVersion.directoryUrl | string | Optional | URL (Uniform Resource Locator) from which to download the MongoDB Agent. |

## Monitoring

The **monitoringVersions** array specifies the version of the
Monitoring Agent. Ops Manager has made this parameter obsolete. To update the
monitoring log settings, use the update-monitoring-logs
endpoint.

```json
"monitoringVersions" : [
  {
    "name" : "<string>",
    "hostname" : "<string>",
    "urls" : {
      "<platform1>" : {
        "<build1>" : "<string>",
        ...,
        "default" : "<string>"
      },
      ...
    },
    "baseUrl" : "<string>",
    "logPath" : "<string>",
    "logRotate" : {
      "sizeThresholdMB" : <number>,
      "timeThresholdHrs" : <integer>,
      "numUncompressed": <integer>,
      "percentOfDiskspace" : <number>,
      "numTotal" : <integer>
    }
  },
  ...
]
```

* - Name
  - Type
  - Necessity
  - Description

* - monitoringVersions
  - array of objects
  - Optional
  - Objects that define version information for each Monitoring
    Agent.

* - monitoringVersions.name
  - string
  - Required
  - Version of the Monitoring Agent.

    To learn more, see /reference/mongodb-compatibility.

    **Important:**

    This property is read-only. Any modifications made to this
    property are not reflected when updating the Monitoring Agent
    through the API (Application Programming Interface).

    To update the Monitoring Agent version, use this endpoint.

* - monitoringVersions.hostname
  - string
  - Required
  - FQDN (fully qualified domain name) of the host that runs the Monitoring Agent. If the
    Monitoring Agent is not running on the host, Ops Manager installs the
    agent from the location specified in
    **monitoringVersions.urls**.

* - monitoringVersions.urls
  - object
  - Required
  - Platform- and build-specific URL (Uniform Resource Locator)\s from which to download
    the Monitoring Agent.

* - monitoringVersions.urls.<platform>
  - object
  - Required
  - Label that identifies an operating system and its version. The
    field contains an object with key-value pairs, where each key is
    either the name of a build or **default** and each value is a
    URL (Uniform Resource Locator) for downloading the Monitoring Agent. The object must
    include the **default** key set to the default download URL (Uniform Resource Locator)
    for the platform.

* - monitoringVersions.baseUrl
  - string
  - Required
  - Base URL (Uniform Resource Locator) used for the mmsbaseurl setting.

* - monitoringVersions.logPath
  - string
  - Optional
  - Directory where the agent stores its logs. The
    default is to store logs in **/dev/null**.

* - monitoringVersions.logRotate
  - object
  - Optional
  - Enables log rotation for the MongoDB logs for a
    process.

* - monitoringVersions.logRotate.sizeThresholdMB
  - number
  - Required
  - Maximum size in MB for an individual log file before rotation.

* - monitoringVersions.logRotate.timeThresholdHrs
  - integer
  - Required
  - Maximum time in hours for an individual log file before
    rotation.

* - monitoringVersions.logRotate.numUncompressed
  - integer
  - Optional
  - Maximum number of total log files to leave uncompressed,
    including the current log file. The default is **5**. In earlier
    versions of Ops Manager, this field was named **maxUncompressed**. The
    earlier name is still recognized, though the new version is
    preferred.

* - monitoringVersions.logRotate.percentOfDiskspace
  - number
  - Optional
  - Maximum percentage of total disk space all log
    files should take up before deletion. The default is **.02**.

* - monitoringVersions.logRotate.numTotal
  - integer
  - Optional
  - Total number of log files. If a number is not
    specified, the total number of log files defaults to **0** and
    is determined by other **monitoringVersions.logRotate**
    settings.

## Backup

The **backupVersions** array specifies the version of the Backup Agent.
Ops Manager has made this parameter obsolete. To update the backup log
settings, use the update-backup-logs endpoint.

```json
"backupVersions[n]" : [
  {
   "name" : "<string>",
    "hostname" : "<string>",
    "urls" : {
     "<platform1>" : {
       "<build1>" : "<string>",
        ...,
        "default" : "<string>"
      },
      ...
    },
    "baseUrl" : "<string>",
    "logPath" : "<string>",
    "logRotate" : {
     "sizeThresholdMB" : "<number>",
      "timeThresholdHrs" : "<integer>",
      "numUncompressed": "<integer>",
      "percentOfDiskspace" : "<number>",
      "numTotal" : "<integer>"
    }
  },
  ...
]
```

* - Name
  - Type
  - Necessity
  - Description

* - backupVersions[n]
  - array of objects
  - Optional
  - Objects that define version information for each
    Backup Agent.

* - backupVersions[n].name
  - string
  - Required
  - Version of the Backup Agent.

    To learn more, see /reference/mongodb-compatibility.

    **Important:**

    This property is read-only. Any modifications made to this
    property are not reflected when updating the Backup Agent
    through the API (Application Programming Interface). To update the Backup Agent version, see
    this endpoint.

* - backupVersions[n].hostname
  - string
  - Required
  - FQDN (fully qualified domain name) of the host that runs the Backup Agent. If the Backup
    Agent is not running on the host, Ops Manager installs the agent from
    the location specified in **backupVersions[n].urls**.

* - backupVersions[n].urls
  - object
  - Required
  - Platform- and build-specific URL (Uniform Resource Locator)\s from which to download the
    Backup Agent.

* - backupVersions[n].urls.<platform>
  - object
  - Required
  - Label that identifies an operating system and its version. The
    field contains an object with key-value pairs, where each key is
    either the name of a build or **default** and each value is a
    URL (Uniform Resource Locator) for downloading the Backup Agent. The object must include
    the **default** key set to the default download URL (Uniform Resource Locator) for the
    platform.

* - backupVersions[n].baseUrl
  - string
  - Required
  - Base URL (Uniform Resource Locator) used for the **mothership** and **https** settings
    in the Custom Settings. For example, for
    **"baseUrl"=https://cloud.mongodb.com**, the backup
    configuration fields would have these values:
    **mothership=api-backup.mongodb.com** and **https"=true**.

* - backupVersions[n].logPath
  - string
  - Optional
  - Directory where the agent stores its logs. The default is to
    store logs in **/dev/null**.

* - backupVersions[n].logRotate
  - object
  - Optional
  - Enables log rotation for the MongoDB logs for a process.

* - backupVersions[n].logRotate.sizeThresholdMB
  - number
  - Required
  - Maximum size in MB for an individual log file before
    rotation.

* - backupVersions[n].logRotate.timeThresholdHrs
  - integer
  - Required
  - Maximum time in hours for an individual log file before
    rotation.

* - backupVersions[n].logRotate.numUncompressed
  - integer
  - Optional
  - Maximum number of total log files to leave uncompressed,
    including the current log file. The default is **5**.

* - backupVersions[n].logRotate.percentOfDiskspace
  - number
  - Optional
  - Maximum percentage of total disk space all log files should
    take up before deletion. The default is **.02**.

* - backupVersions[n].logRotate.numTotal
  - integer
  - Optional
  - If a number is not specified, the total number of log files
    defaults to **0** and is determined by other
    **backupVersion.logRotate** settings.

## MongoDB Instances

The **processes** array determines the configuration of your MongoDB
instances. Using this array, you can:

- Restore an instance.
- Start an initial sync
  process on one or more MongoDB instances.

```yaml
"processes": [{
  "<args>": {},
  "alias": "<string>",
  "authSchemaVersion": "<integer>",
  "backupRestoreUrl": "<string>",
  "cluster": "<string>",
  "defaultRWConcern": {
    "defaultReadConcern": {
      "level": "<string>"
    },
    "defaultWriteConcern": {
      "j": "<boolean>",
      "w": "<string>",
      "wtimeout": "<integer>"
    }
  }
  "disabled": "<Boolean>",
  "featureCompatibilityVersion": "<string>",
  "hostname": "<string>",
  "lastCompact" : "<dateInIso8601Format>",
  "lastRestart" : "<dateInIso8601Format>",
  "lastResync" : "<dateInIso8601Format>",
  "lastKmipMasterKeyRotation" : "<dateInIso8601Format>",
  "logRotate": {
    "sizeThresholdMB": "<number>",
    "timeThresholdHrs": "<integer>",
    "numUncompressed": "<integer>",
    "percentOfDiskspace": "<number>",
    "numTotal": "<integer>"
  },
  "manualMode": "<Boolean>",
  "name": "<string>",
  "numCores": "<integer>",
  "processType": "<string>",
  "version": "<string>"
}]
```

* - Name
  - Type
  - Necessity
  - Description

* - processes
  - array
  - Required
  - Contains objects that define the `mongos` and `mongod` instances
    that Ops Manager monitors. Each object defines a different instance.

* - processes[n].args2_6
  - object
  - Required
  - MongoDB configuration object for MongoDB versions 2.6 and later.

    The `processes.args2_6` object accepts most MongoDB 
    settings and parameters for MongoDB versions 2.6 and later. 
    To learn more, see om-unsupported-mdb-settings.

* - processes[n].alias
  - string
  - Optional
  - Hostname alias (often a DNS (Domain Name System) CNAME) for the host on which the
    process runs. If an alias is specified, the MongoDB Agent prefers
    this alias over the hostname specified in **processes.hostname**
    when connecting to the host. You can also specify this alias in
    **replicaSets.host** and **sharding.configServer**.

* - processes[n].authSchemaVersion
  - integer
  - Required
  - Schema version of the user credentials for MongoDB database
    users. This should match all other elements of the **processes**
    array that belong to the same cluster.

    - Ops Manager accepts **3** and **5** for this parameter.
    - MongoDB 3.x and 4.x clusters default to **5**.
    - MongoDB 2.6 clusters default to  **3**.

    To learn more, see Upgrade to SCRAM-SHA-1 in the MongoDB 3.0 release notes.

* - processes[n].backupRestoreUrl
  - string
  - Optional
  - Delivery URL (Uniform Resource Locator) for the restore. Ops Manager sets this when creating a
    restore. To cancel an in-progress restore operation, set this
    option to `CANCEL`.

    To learn more, see /tutorial/automate-backup-restoration-with-api.

* - processes[n].cluster
  - string
  - Conditional
  - Name of the sharded cluster. Set this value to the same value in
    the **sharding.name** parameter in the **sharding** array for
    the `mongos`.

    - *Required* for a `mongos`.
    - *Not needed* for a `mongod`.

* - defaultRWConcern.defaultReadConcern.level
  - string
  - Optional
  - Consistency and isolation properties set for the data read from
    replica sets and replica set shards. MongoDB Atlas accepts the following values:

    - "available"
    - "local"
    - "majority"

* - defaultRWConcern.defaultWriteConcern.j
  - boolean
  - Optional
  - Flag that indicates whether the write acknowledgement must be
    written to the
    on-disk journal.

* - defaultRWConcern.defaultWriteConcern.w
  - string
  - Optional
  - Desired number of mongod instances that must acknowledge a write
    operation in a replica sets and replica set shards. MongoDB Atlas accepts the
    following values:

    - Any number 0 or greater
    - "majority"

* - defaultRWConcern.defaultWriteConcern.wtimeout
  - number
  - Optional
  - Desired time limit for the write concern
    expressed in milliseconds. Set this value when you set
    **defaultRWConcern.defaultWriteConcern.w** to a value greater
    than **1**.

* - processes[n].disabled
  - Boolean
  - Optional
  - Flag that indicates if this process should be shut down. Set to
    **true** to shut down the process.

* - processes[n].featureCompatibilityVersion
  - string
  - Required
  - Version of MongoDB with which this process has feature
    compatibility. Changing this value can enable or disable certain
    features that persist data incompatible with MongoDB versions
    earlier or later than the **featureCompatibilityVersion** you
    choose.

    - Ops Manager accepts **5.0**, **6.0**, and **7.0** as parameter values. If you have an
      existing deployment, Ops Manager only accepts a
      **featureCompatibilityVersion** equal to or one release older
      than the MongoDB version you deployed. To learn which of
      these parameter values is supported for each MongoDB version,
      and which features each of these values enable or disable,
      see setFeatureCompatibilityVersion in the
      MongoDB Manual.
    - Ops Manager sets this parameter to match the MongoDB version for new
      deployments.
    - Ops Manager doesn't automatically increment this parameter when you
      upgrade a host from one MongoDB version to the next.

    To learn more, see setFeatureCompatibilityVersion.

* - processes[n].hostname
  - string
  - Required
  - Name of the host that serves this process. This defaults to
    **localhost**.

* - processes[n].lastCompact
  - string
  - Optional
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when Ops Manager last reclaimed free space on a
    cluster's disks. During certain operations, MongoDB might move
    or delete data but it doesn't free the currently unused space. Ops Manager
    reclaims the disk space in a rolling fashion across members of
    the replica set or shards.

    To reclaim this space:

    - Immediately, set this value to the current time as an
      ISO 8601 timestamp.
    - Later, set this value to a future ISO 8601 timestamp. Ops Manager
      reclaims the space after the current time passes the provided
      timestamp.

    To remove any ambiguity as to when you intend to reclaim the
    space on the cluster's disks, specify a time zone with your
    ISO 8601 timestamp. For example, to set
    **processes.lastCompact**
    to 28 January 2021 at  2:43:52 PM US Central Standard Time, use
    `"processes.lastCompact" : "2021-01-28T14:43:52-06:00"`

* - processes[n].lastRestart
  - string
  - Optional
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when Ops Manager last restarted this process. If you
    set this parameter to the current timestamp, Ops Manager forces a
    restart of this process after you upload this configuration.
    If you set this parameter for multiple processes in the same
    cluster, the Ops Manager restarts the selected processes in a rolling
    fashion across members of the replica set or shards.

* - processes[n].lastResync
  - string
  - Optional
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) of the last
    initial sync
    process that Ops Manager performed on the node.

    To trigger the init sync process on the node immediately, set
    this value to the current time as an ISO 8601 timestamp.

    WARNING: Use this parameter with caution. During
    initial sync, Automation removes the entire
    contents of the node's `dbPath` directory.

    If you set this parameter:

    - On the secondary node, the MongoDB Agent checks whether the
      specified timestamp is later than the time of the last resync,
      and if confirmed, starts init sync on this node.

      For example, to set `processes.lastResync` on the secondary node to 28
      May 2021 at 2:43:52 PM US CentralStandard Time, use:

      `"processes.lastResync" : "2021-05-28T14:43:52-06:00"`

      If the MongoDB Agent confirms that this timestamp is later
      than the recorded time of the last resync, it starts init
      sync on the node.

    - On the primary node, the MongoDB Agent waits until you ask the
      primary node to become the secondary with the
      `rs.stepDown` method, and then starts init sync on
      this node.

    - On all of the nodes in the same cluster, including the
      primary, the MongoDB Agent checks whether the specified
      timestamp is later than the time of the last resync, and if
      confirmed, starts init sync on the secondary nodes in a
      rolling fashion. The MongoDB Agent waits until you ask the
      primary node to become the secondary with the
      `rs.stepDown` method, and then starts init sync on
      this node.

    To learn more, see Initial Sync.

* - processes[n].lastKmipMasterKeyRotation
  - string
  - Optional
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when Ops Manager last rotated the master KMIP (Key Management Interoperability) key. If
    you set this parameter to the current timestamp, Ops Manager rotate the key after you upload this configuration.

* - processes[n].logRotate
  - object
  - Optional
  - MongoDB configuration object for rotating the MongoDB logs of a
    process.

* - processes[n].logRotate.
    numTotal
  - integer
  - Optional
  - Total number of log files that Ops Manager retains. If you don't set
    this value, the total number of log files defaults to **0**.
    Ops Manager bases rotation on your other **processes.logRotate**
    settings.

* - processes[n].logRotate.
    numUncompressed
  - integer
  - Optional
  - Maximum number of total log files to leave uncompressed,
    including the current log file. The default is **5**.

* - processes[n].logRotate.
    percentOfDiskspace
  - number
  - Optional
  - Maximum percentage of total disk space that Ops Manager can use to
    store the log files expressed as decimal. If this limit is
    exceeded, Ops Manager deletes compressed log files until it meets this
    limit. Ops Manager deletes the oldest log files first.

    The default is **0.02**.

* - processes[n].logRotate.
    sizeThresholdMB
  - number
  - Required
  - Maximum size in MB for an individual log file before Ops Manager
    rotates it. Ops Manager rotates the log file immediately if it meets
    the value given in either this **sizeThresholdMB** or the
    **processes.logRotate.timeThresholdHrs** limit.

* - processes[n].logRotate.
    timeThresholdHrs
  - integer
  - Required
  - Maximum duration in hours for an individual log file before the
    next rotation. The time is since the last rotation.

    Ops Manager rotates the log file once the file meets either this
    **timeThresholdHrs** or the
    **processes.logRotate.sizeThresholdMB** limit.

* - processes[n].manualMode
  - Boolean
  - Optional
  - Flag that indicates if MongoDB Agent automates this process.

    - This defaults to **false**.
    - Set to **true** to suspend Automation on this process. The
      MongoDB Agent takes no further actions on this process until
      Automation is resumed.
    - Set to **false** to enable Automation on this process. The
      MongoDB Agent automates actions on this process.

* - processes[n].name
  - string
  - Required
  - Unique name to identify the instance.

* - processes[n].numCores
  - integer
  - Optional
  - Number of cores that Ops Manager should bind to this process. The
    MongoDB Agent distributes processes across the cores as evenly as
    possible.

* - processes[n].processType
  - string
  - Required
  - Type of MongoDB process being run. Ops Manager accepts `mongod` or
    `mongos` for this parameter.

* - processes[n].version
  - string
  - Required
  - Name of the **mongoDbVersions** specification used with this
    instance.

## Cluster Wide

**clusterWideConfigurations** specifies the parameters to set across a
replica set or sharded cluster without requiring a `rolling restart`.

```json
"clusterWideConfigurations" : { 
  "<replicaSetID/clusterName>": {
    "changeStreamOptions": {
      "preAndPostImages": {
        "expireAfterSeconds": <integer>
      }
    }
  }
}
```

| Name | Type | Necessity | Description |
|---|---|---|---|
| replicaSetID/clusterName | object | Optional | The change stream options to apply to the replica set or sharded cluster. MongoDB Agent only checks if this configuration is in a valid JSON (Javascript Object Notation) format but doesn't check the values for correctness. |
| changeStreamOptions.preAndPostImages.expireAfterSeconds | number | Required | Retention policy of change stream pre- and post-images in seconds. If you omit the value, the cluster retains the pre- and post-images until it removes the corresponding change stream events from the oplog. If you remove this value, MongoDB Agent only removes this parameter from its automation configuration, but not from the server. To learn more, see changeStreamOptions. |

## Replica Sets

The **replicaSets** array defines each replica set's configuration.
This field is required for deployments with replica sets.

```json
"replicaSets":
[
  {
    "_id": "<string>",
    "protocolVersion": "<string>",
    "members":
    [
      {
        "_id": "<integer>",
        "host": "<string>",
        "arbiterOnly": "<boolean>",
        "buildIndexes": "<boolean>",
        "hidden": "<boolean>",
        "priority": "<number>",
        "tags": "<object>",
        "secondaryDelaySecs": "<integer>",
        "votes": "<number>"
      },{
        "_id": "<integer>",
        "host": "<string>",
        "arbiterOnly": "<boolean>",
        "buildIndexes": "<boolean>",
        "hidden": "<boolean>",
        "priority": "<number>",
        "tags": "<object>",
        "secondaryDelaySecs": "<integer>",
        "votes": "<number>"
      },{
        "_id": "<integer>",
        "host": "<string>",
        "arbiterOnly": "<boolean>",
        "buildIndexes": "<boolean>",
        "hidden": "<boolean>",
        "priority": "<number>",
        "tags": "<object>",
        "secondaryDelaySecs": "<integer>",
        "votes": "<number>"
      }
    ],
    "force":
    {
      "currentVersion": "<integer>"
    }
  }
]
```

| Name | Type | Necessity | Description |
|---|---|---|---|
| replicaSets | array | Optional | Configuration of each replica set. The MongoDB Agent uses the values in this array to create valid replica set configuration documents. The agent regularly checks that replica sets are configured correctly. If a problem occurs, the agent reconfigures the replica set according to its configuration document. The array can contain the following top-level fields from a replica set configuration document: **_id**; **version**; and **members**. To learn more, see replSetGetConfig. |
| replicaSets[n]._id | string | Required | The name of the replica set. |
| replicaSets[n].protocolVersion | string | Optional | Protocol version of the replica set. |
| replicaSets[n].members | array | Optional | Objects that define each member of the replica set. The **members.host** field must specify the host's name as listed in **processes.name**. The MongoDB Agent expands the **host** field to create a valid replica set configuration. To learn more, see replSetGetConfig. |
| replicaSets[n].members[m]._id | integer | Required | Any positive integer that indicates the member of the replica set. |
| replicaSets[n].members[m].host | string | Optional | Hostname, and port number when applicable, that serves this replica set member. |
| replicaSets[n].members[m].arbiterOnly | boolean | Optional | Flag that indicates whether this replica set member acts as an arbiter. |
| replicaSets[n].members[m].buildIndexes | boolean | Optional | Flag that indicates whether the `mongod` process builds indexes on this replica set member. |
| replicaSets[n].members[m].hidden | boolean | Optional | Flag that indicates whether the replica set allows this member to accept read operations. |
| replicaSets[n].members[m].priority | number | Optional | Relative eligibility for Ops Manager to select this replica set member as a primary. Larger number increase eligibility. This value can be between 0 and 1000, inclusive for data-bearing nodes. Arbiters can have values of 0 or 1. |
| replicaSets[n].members[m].tags | object | Optional | List of user-defined labels and their values applied to this replica set member. |
| replicaSets[n].members[m].secondaryDelaySecs | integer | Optional | Amount of time in seconds that this replica set memberr should lag behind the primary. |
| replicaSets[n].members[m].votes | number | Optional | Quantity of votes this replica set member can cast for a replica set election. All data bearing nodes can have 0 or 1 votes. Arbiters always have 1 vote. |
| replicaSets[n].force | object | Optional | Instructions to the MongoDB Agent to force a replica set to use the automation-config-api-config-version specified in **replicaSets.force.CurrentVersion**. With this object, the MongoDB Agent can force a replica set to accept a new configuration to recover from a state in which a minority of its members are available. |
| replicaSets[n].force.currentVersion | integer | Optional | automation-config-api-config-version that the MongoDB Agent forces the replica set to use. Set to **-1** to force a replica set to accept a new configuration. WARNING: Forcing a replica set reconfiguration might lead to a rollback of majority-committed writes. Proceed with caution. Contact [MongoDB Support](https://support.mongodb.com) if you have questions about the potential impacts of this operation. |

## Sharded Clusters

The **sharding** array defines the configuration of each sharded
cluster. This parameter is required for deployments with sharded
clusters.

```json
"sharding" : [
  {
    "managedSharding" : false,
    "name" : "<string>",
    "configServerReplica" : "<string>",
    "shards" : [
      {
        "_id" : "<string>",
        "rs" : "<string>",
        "tags" : [ "<string>", ... ]
      },
      ...
    ],
  },
  ...
]
```

* - Name
  - Type
  - Necessity
  - Description

* - sharding
  - array of objects
  - Optional
  - Objects that define the configuration of each
    sharded cluster. Each object in the array contains the
    specifications for one cluster. The MongoDB Agent regularly
    checks each cluster's state against the specifications. If the
    specification and cluster don't match, the agent will change the
    configuration of the cluster, which might cause the balancer to
    migrate chunks.

* - sharding.managedSharding
  - boolean
  - Optional
  - Flag that indicates whether Ops Manager Automation manages all
    sharded collections
    and tags in the deployment.
    Starting in Ops Manager version 7.0, this can be set only to `false`.

* - sharding.name
  - string
  - Conditional
  - Name of the cluster. This must correspond with the value in
    **processes.cluster** for a `mongos`.

* - sharding.configServerReplica
  - string
  - Conditional
  - Name of the config server replica set.

    You can add this array parameter if your config server runs as a replica set.

    If you run legacy mirrored config servers that
    don't run as a replica set, use **sharding.configServer**.

* - sharding.configServer
  - array of strings
  - Conditional
  - Names of the config server hosts. The host names match the names
    used in each host's **processes.name** parameter.

    If your sharded cluster runs MongoDB 3.4 or later, use
    **sharding.configServerReplica**.

    **Important:** MongoDB 3.4 removes support for mirrored config servers.

* - sharding.shards
  - array of objects
  - Conditional
  - Cluster's shards.

* - sharding.shards._id
  - string
  - Conditional
  - Name of the shard.

* - sharding.shards.rs
  - string
  - Conditional
  - Name of the shard's replica set. This is specified in the
    **replicaSets._id** parameter.

* - sharding.shards.tags
  - array of strings
  - Conditional
  - Zones assigned to this shard.

    You can add this array parameter if you use
    zoned sharding.

## Cluster Balancer

The **balancer** object is optional and defines balancer settings for each cluster.

```json
"balancer": {
  "<clusterName1>": {},
  "<clusterName2>": {},
  ...
}
```

| Name | Type | Necessity | Description |
|---|---|---|---|
| balancer | object | Optional | Parameters named according to clusters, each parameter containing an object with the desired balancer settings for the cluster. The object uses the **stopped** and **activeWindow** parameters, as described in the procedure to schedule the balancing window in this tutorial in the MongoDB manual. |

## Authentication

To enable authentication, configure the `auth` object. This object is
optional and defines authentication-related settings.

```json
{
  "auth": {
    "authoritativeSet": "<boolean>",
    "autoUser": "<string>",
    "autoPwd": "<string>",
    "disabled": "<boolean>",
    "deploymentAuthMechanisms": ["<string>", "<string>"],
    "autoAuthMechanisms": ["<string>"],
    "key": "<string>",
    "keyfile": "<string>",
    "newAutoPwd": "<string>",
    "newKey": "<string>",
    "usersDeleted": [{
      "user": "<string>",
      "dbs": ["<string>", "<string>"]
    }],
    "usersWanted": [{
      "authenticationRestrictions": [{
        "clientSource": ["(IP | CIDR range)", "(IP | CIDR range)"],
        "serverAddress": ["(IP | CIDR range)", "(IP | CIDR range)"]
      }],
      "db": "<string>",
      "initPwd": "<string>",
      "otherDBRoles": {
        "<string>": ["<string>", "<string>"]
      },
      "roles": [{
        "db": "<string>",
        "role": "<string>"
      }],
      "pwd": "<string>",
      "user": "<string>"
    }]
  }
}
```

* - Name
  - Type
  - Necessity
  - Description

* - auth
  - object
  - Optional
  - Defines authentication-related
    settings.

    If you omit this parameter, skip the rest of this section.

* - auth.authoritativeSet
  - boolean
  - Conditional
  - Sets whether or not Ops Manager enforces a consistent set of managed
    MongoDB users and roles in all managed deployments in the
    project.

    - If **"auth.authoritativeSet" : true**, then Ops Manager
      enforces consistent users and roles.

    - If **"auth.authoritativeSet" : false**, then Ops Manager
      doesn't enforce consistent users and roles.

    **auth.authoritativeSet** defaults to **false**.

    **Required if you enable authentication.**

* - auth.autoUser
  - string
  - Conditional
  - Username that the Automation uses when connecting to an
    instance.

    **Required if you enable authentication.**

* - auth.autoPwd
  - string
  - Conditional
  - Password that the Automation uses when connecting to an
    instance.

    **Required if you enable authentication.**

* - auth.disabled
  - boolean
  - Optional
  - Flag indicating if auth is disabled. If not specified,
    **disabled** defaults to **false**.

* - auth.deploymentAuthMechanisms
  - array of strings
  - Conditional
  - Lists the supported authentication mechanisms for the processes
    in the deployment.

    **Required if you enable authentication.**

    Specify:

    | Value | Authentication Mechanism |
    |---|---|
    | MONGODB-CR | SCRAM-SHA-1 |
    | SCRAM-SHA-256 | SCRAM-SHA-256 |
    | MONGODB-X509 | x.509 Client Certificate |
    | PLAIN | LDAP |
    | GSSAPI | Kerberos |

* - auth.autoAuthMechanisms
  - array of strings
  - Conditional
  - Sets the authentication mechanism used by the Automation. 
    If not specified, **disabled** defaults to **false**.

    **Required if you enable authentication.**

    This parameter contains more than one element only when 
    it's configured for both SCRAM-SHA-1 and SCRAM-SHA-256.

    Specify:

    | Value | Authentication Mechanism |
    |---|---|
    | MONGODB-CR | SCRAM-SHA-1 |
    | SCRAM-SHA-256 | SCRAM-SHA-256 |
    | MONGODB-X509 | x.509 Client Certificate |
    | PLAIN | LDAP |
    | GSSAPI | Kerberos |

* - auth.key
  - string
  - Conditional
  - Contents of the key file that Ops Manager uses to authenticate to the
    MongoDB processes.

    Required if **you enable authentication** and **"auth.disabled" : false**.

    If you change the **auth.key** value, you must change the
    **auth.keyfile** value.

* - auth.keyfile
  - string
  - Conditional
  - Path and name of the key file that Ops Manager uses to authenticate to
    the MongoDB processes.

    Required if **you enable authentication** and **"auth.disabled" : false**.

    If you change the **auth.keyfile** value, you must change the
    **auth.key** value.

* - | auth
    | .newAutoPwd
  - string
  - Optional
  - New password that the Automation uses when connecting to an
    instance. To rotate passwords without losing the connection:

    1. Set **auth.newAutoPwd** and leave **auth.autoPwd** with its 
       current password.

    #. Wait for the goal state.

    #. **auth.newAutoPwd** copies over the **auth.autoPwd**
       password automatically.

    You can set this option only when you include SCRAM-SHA-1 
    or SCRAM-SHA-256 as one of the authentication 
    mechanisms for the Automation in **auth.autoAuthMechanisms**.

* - auth.newKey
  - string
  - Optional
  - Contents of a new key file that you want Ops Manager to use to 
    authenticate to the MongoDB processes. 

    When you set this option, Ops Manager rotates the key that the
    application uses to authenticate to the MongoDB processes in 
    your deployment. When all MongoDB Agents use the new key, Ops Manager 
    replaces the value of **auth.key** with the new key that you 
    provided in **auth.newKey** and removes **auth.newKey** from the
    automation configuration.

* - auth.usersDeleted
  - array of objects
  - Optional
  - Objects that define the authenticated users to be deleted from
    specified databases or from all databases. This array must
    contain **auth.usersDeleted.user** and
    **auth.usersDeleted.dbs**.

* - auth.usersDeleted[n].user
  - string
  - Optional
  - Username of user that Ops Manager should delete.

* - auth.usersDeleted[n].dbs
  - array of strings
  - Optional
  - List the names of the databases from which Ops Manager should delete
    the authenticated user.

* - auth.usersWanted
  - array of objects
  - Optional
  - Contains objects that define authenticated users to
    add to specified databases. Each object must have the
    **auth.usersWanted[n].db**, **auth.usersWanted[n].user**, and
    **auth.usersWanted[n].roles** parameters, and then have exactly one
    of the following parameters: **auth.usersWanted[n].pwd**,
    **auth.usersWanted[n].initPwd**, or
    **auth.usersWanted[n].userSource**.

* - auth.usersWanted[n].db
  - string
  - Conditional
  - Database to which to add the user.

* - auth.usersWanted[n].user
  - string
  - Conditional
  - Name of the user that Ops Manager should add.

* - auth.usersWanted[n].roles
  - array
  - Conditional
  - List of the roles to be assigned to the user
    from the user's database, which is specified in
    **auth.usersWanted[n].db**.

* - auth.usersWanted[n].pwd
  - string
  - Conditional
  - 32-character hex **SCRAM-SHA-1** hash of the password
    currently assigned to the user.

    Ops Manager doesn't use this parameter to set or change a password.

    Required if:

    - You enable authentication
    - **"auth.deploymentAuthMechanisms" : "MONGODB-CR"**
    - **"auth.usersWanted[n].initPwd"** is unset

* - auth.usersWanted[n].initPwd
  - string
  - Conditional
  - Cleartext password that you want to assign to the user.

    Required if:

    - You enable authentication
    - **"auth.deploymentAuthMechanisms" : "MONGODB-CR"**
    - **"auth.usersWanted[n].initPwd"** is unset

* - auth.usersWanted[n].userSource
  - string
  - Deprecated
  - No longer supported.

* - auth.usersWanted[n].otherDBRoles
  - object
  - Optional
  - If you assign the user's database **"auth.usersWanted[n].db" :
    "admin"**, then you can use this object to assign the user roles
    from other databases as well. The object contains key-value
    pairs where the key is the name of the database and the value is
    an array of string values that list the roles be assigned from
    that database.

* - auth.usersWanted[n].authenticationRestrictions
  - array of documents
  - Optional
  - Authentication restrictions that the host enforces on the
    user.

    WARNING: If a user inherits multiple roles with incompatible authentications restrictions, that user becomes unusable. For example, if a user inherits one role in which the `clientSource` field is `[198.51.100.0]` and another role in which the `clientSource` field is `[203.0.113.0]`, the server is unable to authenticate the user.
    For more information about authentication in MongoDB, see [Authentication](https://www.mongodb.com/docs/manual/core/authentication/).

* - auth.usersWanted[n].authenticationRestrictions[k].clientSource
  - array of strings
  - Conditional
  - If present when authenticating a user, the host verifies that
    the given list contains the client's IP address CIDR (Classless Inter-Domain Routing) range. If
    the client's IP address is not present, the host does not
    authenticate the user.

* - auth.usersWanted[n].authenticationRestrictions[k].serverAddress
  - array of strings
  - Conditional
  - Comma-separated array of IP addresses to which the client can
    connect. If present, the host verifies that Ops Manager accepted the
    client's connection from an IP address in the given array. If
    the connection was accepted from an unrecognized IP address, the
    host doesn't authenticate the user.

## LDAP

The `ldap` object enables LDAP (Lightweight Directory Access Protocol) authorization. This
object is optional. To learn more, see enable-ldap-auth.

```json
   "ldap": {
     "servers": "<host>:<port>, <host>:<port>",
     "timeoutMS": "<time>",
     "bindMethod": "<sasl/simple>",
     "bindSaslMechanisms": "<sasl-mechanism>, <sasl-mechanism>",
     "bindQueryUser": <ldap-dn>",
     "bindQueryPassword": "<password>",
     "userCacheInvalidationPeriod": "<interval>",
     "authzQueryTemplate": "<rfc-4516-url>",
     "userToDNMapping": [
		{
  			"match": "<ECMAScript-regex>",
  			"<substition/ldapQuery>": "<DN-string/RFC4516-encoded-LDAP-query>"
		}
     ]
  }
```

| Name | Type | Necessity | Description |
|---|---|---|---|
| ldap | object | Optional | Object that contains the settings to enable and configure LDAP (Lightweight Directory Access Protocol) authorization. |
| ldap.servers | string | Conditional | Comma-separated string that contains one or more LDAP (Lightweight Directory Access Protocol) servers in `<host>:<port>` format to execute queries against. You can use `setParameter` to configure this setting on a running system. For LDAP (Lightweight Directory Access Protocol) authorization, you must specify this setting. |
| ldap.timeoutMS | long | Optional | Amount of time in milliseconds that MongoDB waits for an LDAP (Lightweight Directory Access Protocol) server to respond to a request before timing out. You can use `setParameter` to configure this setting on a running system. By default, MongoDB times out after ten seconds. |
| ldap.bindMethod | string | Optional | Human-readable string that indicates whether to use simple authentication or an SASL (Simple Authentication and Security Layer) protocol to authenticate itself. You can specify `simple` or `sasl`. By default, MongoDB uses simple authentication. |
| ldap.bindSaslMechanisms | string | Optional | String that contains a comma-separated list of SASL (Simple Authentication and Security Layer) mechanisms for MongoDB to attempt authentication against the LDAP (Lightweight Directory Access Protocol) server while binding. By default, MongoDB uses `DIGEST-MD5` to bind. |
| ldap.bindQueryUser | string | Conditional | LDAP (Lightweight Directory Access Protocol) entity domain name that MongoDB binds as when it connects to an LDAP (Lightweight Directory Access Protocol) server. You can use `setParameter` to configure this setting on a running system. For MongoDB to bind with authentication credentials, you must specify this setting. |
| ldap.bindQueryPassword | string | Conditional | Password that MongoDB binds with when it connects to an LDAP (Lightweight Directory Access Protocol) server. You can use `setParameter` to configure this setting on a running system. For MongoDB to bind with a password, you must specify this setting. |
| ldap.userCacheInvalidationPeriod | integer | Optional | Interval that MongoDB waits between user cache flushes. When the external user cache is flushed, the next operation that an LDAP (Lightweight Directory Access Protocol) authorized user makes requires a reaquisition of roles. If you specify a high value, you might decrease the load on your LDAP (Lightweight Directory Access Protocol) servers and increase the amount of time needed to synchronize MongoDB roles with LDAP (Lightweight Directory Access Protocol) group membership. By default, MongoDB waits 30 seconds between cache flushes. |
| ldap.authzQueryTemplate | string | Conditional | RFC 4516 formatted URL (Uniform Resource Locator) of the LDAP (Lightweight Directory Access Protocol) query to execute to obtain LDAP (Lightweight Directory Access Protocol) groups relative to the `ldap.server` setting. In this URL (Uniform Resource Locator), the placeholder token string `{USER}` is replaced with the acquired user domain name. You can use `setParameter` to configure this setting on a running system. For LDAP (Lightweight Directory Access Protocol) authorization, you must specify this setting. |
| ldap.userToDNMapping | array | Optional | JSON (Javascript Object Notation)-formatted array that contains the ordered transformations that MongoDB applies to authenticate MongoDB user names to match their domain names. You can specify this setting if you use an alternate authentication method, or if the user name passed to MongoDB for authentication doesn't match the LDAP (Lightweight Directory Access Protocol) domain name. You can use `setParameter` to configure this setting on a running system. By default, MongoDB uses user names as the domain names for automatic LDAP (Lightweight Directory Access Protocol) authorization. |

## SSL

The **ssl** object enables TLS (Transport Layer Security) for encrypting connections. This
object is optional.

```json
"ssl" : {
  "CAFilePath" : "<string>"
}
```

* - Name
  - Type
  - Necessity
  - Description

* - ssl
  - object
  - Optional
  - Enables TLS (Transport Layer Security) for encrypting connections. To use TLS (Transport Layer Security), choose a
    package that supports TLS (Transport Layer Security).

    All platforms that support
    `MongoDB Enterprise` also support
    TLS (Transport Layer Security).

* - ssl.clientCertificateMode
  - string
  - Conditional
  - Indicates whether connections to Ops Manager require a TLS (Transport Layer Security)
    certificate. The values are **OPTIONAL** and **REQUIRE**.

* - ssl.CAFilePath
  - string
  - Conditional
  - Absolute file path to the certificate used to authenticate
    through TLS (Transport Layer Security) on a Linux or UNIX host. 

    Ops Manager requires either **ssl.CAFilePath** or **ssl.CAFilePathWindows** if:

    - You're using TLS (Transport Layer Security) or X.509 authentication, and
    - The CA file is not in your operating system's root certificates.

* - ssl.CAFilePathWindows
  - string
  - Conditional
  - Absolute file path to the certificate used to authenticate
    through TLS (Transport Layer Security) on a Windows host.

    Ops Manager requires either **ssl.CAFilePath** or **ssl.CAFilePathWindows** if:

    - You're using TLS (Transport Layer Security) or X.509 authentication, and
    - The CA file is not in your operating system's root certificates.

* - ssl.autoPEMKeyFilePath
  - string
  - Conditional
  - Absolute file path to the client private key (PEM) file that
    authenticates the TLS (Transport Layer Security) connection on a Linux or UNIX
    host. 

    Ops Manager requires either **ssl.autoPEMKeyFilePath** or **ssl.autoPEMKeyFilePathWindows**
    if you're using TLS (Transport Layer Security) or X.509 authentication.

* - ssl.autoPEMKeyFilePathWindows
  - string
  - Conditional
  - Absolute file path to the client private key (PEM) file that
    authenticates the TLS (Transport Layer Security) connection on a Windows host.

    Ops Manager requires either **ssl.autoPEMKeyFilePath** or **ssl.autoPEMKeyFilePathWindows**
    if you're using TLS (Transport Layer Security) or X.509 authentication.

* - ssl.autoPEMKeyFilePwd
  - string
  - Conditional
  - Password for the private key (PEM) file specified in
    **ssl.autoPEMKeyFilePath** or **ssl.autoPEMKeyFilePathWindows**. Ops Manager
    requires this password if the PEM file is encrypted.

## MongoDB Roles

The `roles` array is optional and describes user-defined roles.

```json
"roles" : [
  {
    "role" : "<string>",
    "db" : "<string>",
    "privileges" : [
      {
        "resource" : { ... },
        "actions" : [ "<string>", ... ]
      },
      ...
    ],
    "roles" : [
      {
        "role" : "<string>",
        "db" : "<string>"
      }
    ]
    "authenticationRestrictions" : [
     {
      "clientSource": [("<IP>" | "<CIDR range>"), ...],
      "serverAddress": [("<IP>" | "<CIDR range>"), ...]
    }, ...
  ]
  },
  ...
]
```

| Name | Type | Necessity | Description |
|---|---|---|---|
| roles | array of objects | Optional | Roles and privileges that MongoDB has assigned to a cluster's user-defined roles. Each object describes a different user-defined role. Objects in this array contain the same fields as documents in the system roles collection, except for the **_id** field. |
| roles[n].role | string | Conditional | Name of the user-defined role. |
| roles[n].db | string | Conditional | Database to which the user-defined role belongs. |
| roles[n].privileges | array of documents | Conditional | Privileges this role can perform. |
| roles[n].privileges[k].resource | string | Conditional | Specifies the resources upon which the privilege **actions** apply. |
| roles[n].privileges[k].actions | string | Conditional | Actions permitted on the resource. To learn more, see Privilege Actions. |
| roles[n].roles | array of documents | Conditional | Roles from which this role inherits privileges. |
| roles[n].authenticationRestrictions | array of documents | Optional | Authentication restrictions that the MongoDB server enforces on this role. WARNING: If a user inherits multiple roles with incompatible authentications restrictions, that user becomes unusable. For example, if a user inherits one role in which the `clientSource` field is `[198.51.100.0]` and another role in which the `clientSource` field is `[203.0.113.0]`, the server is unable to authenticate the user. For more information about authentication in MongoDB, see [Authentication](https://www.mongodb.com/docs/manual/core/authentication/). |
| roles[n].authenticationRestrictions[k].clientSource | array of strings | Conditional | If present, when authenticating a user, the MongoDB server verifies that the client's IP address is either in the given list or belongs to a CIDR (Classless Inter-Domain Routing) range in the list. If the client's IP address is not present, the MongoDB server does not authenticate the user. |
| roles[n].authenticationRestrictions[k].serverAddress | array of strings | Conditional | Comma-separated array of IP addresses to which the client can connect. If present, the MongoDB server verifies that it accepted the client's connection from an IP address in the given array. If the MongoDB server accepts a connection from an unrecognized IP address, the MongoDB server does not authenticate the user. |

## Kerberos

The **kerberos** object is optional and defines a kerberos service name used in authentication.

```json
"kerberos": {
  "serviceName": "<string>"
}
```

* - Name
  - Type
  - Necessity
  - Description

* - kerberos
  - object
  - Optional
  - Key-value pair that defines the kerberos service name
    agents use to authenticate via kerberos.

* - kerberos.serviceName
  - string
  - Required
  - Label that sets:

    - The service name that the agents use to authenticate to a
      `mongod` or `mongos` via Kerberos.
    - The **saslServiceName** option in the
      MongoDB Server Parameters.

## Indexes

The **indexConfigs** array is optional and defines indexes to be built for specific replica sets.

```json
"indexConfigs": [{
  "key": [
    ["<string>", "<value>"]
  ],
  "rsName": "<string>",
  "dbName": "<string>",
  "collectionName": "<string>",
  "collation": {
    "locale": "<string>",
    "caseLevel": <boolean>,
    "caseFirst": "<string>",
    "strength": <number>,
    "numericOrdering": <boolean>,
    "alternate": "<string>",
    "maxVariable": "<string>",
    "normalization": <boolean>,
    "backwards": <boolean>
  },
  "options": {
    "<key>": "<value>"
  }
}]
```

* - Name
  - Type
  - Necessity
  - Description

* - indexConfigs
  - array of objects
  - Optional
  - Specific indexes to be built for specific replica sets.

* - indexConfigs.key
  - array of arrays
  - Required
  - Keys in the index. This "array of arrays" contains a single
    array if the index has just one key.

* - indexConfigs.rsName
  - string
  - Required
  - Replica set on which MongoDB builds the index.

* - indexConfigs.dbName
  - string
  - Required
  - Database that MongoDB indexes.

* - indexConfigs.collectionName
  - string
  - Required
  - Collection that MongoDB indexes.

* - indexConfigs.collation
  - object
  - Optional
  - Language-specific rules to use when sorting and matching
    strings if the index uses
    collation.

    If you include the **indexConfigs.collation** object, you must
    include the **indexConfigs.collation.locale** parameter. All
    other parameters are optional.

    If you don't include the **indexConfigs.collation** object, the
    index can't include collation.

* - indexConfigs.collation.locale
  - string
  - Required
  - Locale that the [ICU](http://site.icu-project.org/) defines.

    The MongoDB Server Manual lists the supported locales in its
    Collation Locales and Default Parameters section.

    To specify simple binary comparison, set this value to
    **simple**.

* - indexConfigs.collation.caseLevel
  - boolean
  - Optional
  - Flag that indicates how the index uses case comparison.

    If you set this parameter to **true**, the index uses case
    comparison.

    This parameter applies only if you set
    **indexConfigs.collation.strength** to **1** or **2**.

    To learn more, see Collation.

* - indexConfigs.collation.caseFirst
  - string
  - Optional
  - Sort order of case differences during tertiary level
    comparisons.

    The MongoDB Server Manual lists the possible values in its
    Collation section.

* - indexConfigs.collation.strength
  - number
  - Optional
  - Level of comparison to perform. Corresponds to
    [ICU Comparison Levels](http://userguide.icu-project.org/collation/concepts#TOC-Comparison-Levels).

    The MongoDB Server Manual lists the possible values in its
    Collation section.

* - indexConfigs.collation.numericOrdering
  - boolean
  - Optional
  - Flag that indicates how to compare numeric strings.

    | Value | Collation Method | Example |
    |---|---|---|
    | true | numeric strings compared as numbers | **10** > **2**. |
    | false | numeric strings compared as strings | **10** < **2**. |

    The default is **false**.

    To learn more, see Collation.

* - indexConfigs.collation.alternate
  - string
  - Optional
  - Setting that determines how collation should consider whitespace
    and punctuation as base characters during comparisons.

    The MongoDB Server Manual lists the possible values in its
    Collation section.

* - indexConfigs.collation.maxVariable
  - string
  - Optional
  - Characters the index can ignore. This parameter applies only if
    **indexConfigs.collation.alternate** is set to **shifted**.

    The MongoDB Server Manual lists the possible values in its
    Collation section.

* - indexConfigs.collation.normalization
  - boolean
  - Optional
  - Flag that indicates if the text should be normalized.

    If you set this parameter to **true**, collation:

    - Checks if text requires [normalization](http://userguide.icu-project.org/collation/concepts#TOC-Normalization).
    - Performs normalization to compare text.

    The default is **false**.

    To learn more, see Collation.

* - indexConfigs.collation.backwards
  - boolean
  - Optional
  - Flag that indicates how the index should handle diacritic
    strings.

    If you set this parameter to **true**, strings with diacritics
    sort from the back to the front of the string.

    The default is **false**.

    To learn more, see Collation.

* - indexConfigs.options
  - document
  - Required
  - Index options that the `MongoDB Go Driver`
    supports.
