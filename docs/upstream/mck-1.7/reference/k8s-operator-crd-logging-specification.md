<!-- Converted from reference/k8s-operator-crd-logging-specification.txt (reStructuredText). Includes are inlined. -->

# MongoDB CRD Log Rotation Settings

You can configure log rotation settings for [CustomResourceDefinitions](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/)
in the MongoDB and 
Ops Manager CRD (Custom Resource Definition) manifests.

The following table outlines logging configuration fields 
that you can define in the MongoDB CRD (Custom Resource Definition) manifests, 
and where they can be defined or accessed elsewhere if you choose not 
to configure them directly from the CRD (Custom Resource Definition) manifests.

| Component | Log type | CRD manifest configuration | Default configuration location |
|---|---|---|---|
| MongoDB | Automation agent logs | `MongoDB CRD` | `spec.agent.startupOptions` |
| MongoDB | Monitoring Agent logs | `MongoDB CRD` | Ops Manager API or UI |
| MongoDB | Backup logs | `MongoDB CRD` | Ops Manager API or UI |
| MongoDB | MongoDB logs | Ops Manager 7.0.4, 6.0.24, or later: `MongoDB CRD` | Ops Manager UI |
| MongoDB | Audit logs | `MongoDB CRD` | Ops Manager UI |
| MongoDB | Readiness Probe | `MongoDB CRD` | Container Environment Variables |
| Application Database | MongoDB Logs | `MongoDBOpsManager CRD <spec.applicationDatabase.agent.` | `spec.applicationDatabase.agent.mongod.logRotate <spec.applicationDatabase.agent.` |
| Application Database | Automation Agent Logs | `MongoDBOpsManager CRD` | `spec.applicationDatabase.agent.startupOptions` |
| Application Database | Monitoring Agent logs | `MongoDBOpsManager CRD <spec.applicationDatabase.agent.` | Forwarded to `stdout` only (kubectl logs). Managed and stored in the Kubernetes control plane. |
| Application Database | Audit logs | `MongoDBOpsManager CRD` | `spec.applicationDatabase.agent.mongod.auditlogRotate` |
| Ops Manager | Ops Manager logs | MongoDBOpsManager CRD | logback.xml configuration file |

## MongoDB Log Rotation

**Note:**

For Ops Manager 6, you can only configure `mongod` logs with this setting starting with version 6.0.2.
For Ops Manager 7, you can only configure `mongod` logs with this setting starting with version 7.0.4.
For previous Ops Manager versions, you must use the Ops Manager UI to configure `mongod` logs.

You can configure a log's rotation 
in the MongoDB CRD (Custom Resource Definition), as shown in the following example manifest. 

See the preceding comparison table for more 
information about configuring the rotation of other MongoDB-specific logs. 

### Automation Agent Logs

You can configure the MongoDB automation agent logs in the MongoDB CRD (Custom Resource Definition) manifest 
under `spec.agent.startupOptions`.

### Example Manifest

**Note:**

For sharded clusters, you can only configure log rotation at the `spec.agent` level. 
Configuring log rotation on sub-spec levels such as `spec.configsrv.agent` or 
`spec.shardsvr.agent` is not supported. 

```yaml
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: log-rotate
  namespace: mongodb
spec:
  podSpec:
    podTemplate:
      spec:
        containers:
        - name: mongodb-enterprise-database
          env:
          - name: READINESS_PROBE_LOGGER_MAX_SIZE
            value: "50"
  version: 8.0.0
  opsManager:
    configMapRef:
      name: my-project
  credentials: my-credentials
  type: Standalone
  persistent: false
  # https://docs.opsmanager.mongodb.com/current/reference/mongodb-agent-settings/
  agent:
    startupOptions:
      maxLogFiles: 10
      maxLogFileSize: 2
    readinessProbe:
      environmentVariables:
        READINESS_PROBE_LOGGER_MAX_SIZE: 10
        READINESS_PROBE_LOGGER_BACKUPS: 1
        READINESS_PROBE_LOGGER_MAX_AGE: 3
        READINESS_PROBE_LOGGER_COMPRESS: true
        MDB_WITH_AGENT_FILE_LOGGING: false
        LOG_FILE_PATH: /var/log/mongodb-mms-automation/readiness.log
    backupAgent:
      logRotate:
        sizeThresholdMB: "10"
        timeThresholdHrs: 10
    monitoringAgent:
      logRotate:
        sizeThresholdMB: "10"
        timeThresholdHrs: 10
    # For Ops Manager 6, you can only configure mongod logs with this setting starting with version 6.0.2.
    # For Ops Manager 7, you can only configure mongod logs with this setting starting with version 7.0.4.
    # For previous Ops Manager versions, you must configure mongod logs using the Ops Manager UI.
    mongod:
      logRotate:
        sizeThresholdMB: "10"
        timeThresholdHrs: 10
        numUncompressed: 10
        numTotal: 10
        percentOfDiskspace: 10
      auditlogRotate:
        sizeThresholdMB: "10"
        timeThresholdHrs: 10
        numUncompressed: 10
        numTotal: 10
        percentOfDiskspace: 10
```

## Application Database Log Rotation

You can configure the following log's rotation in the `MongoDBOpsManager` CRD (Custom Resource Definition), 
as shown in the following example manifest. See the preceding table for more 
information about configuring the rotation of other Application Database-specific logs. 

### MongoDB Logs

You can configure the Application Database MongoDB log rotation in the 
`MongoDBOpsManager` manifest under `spec.applicationDatabase.agent.<component>.logRotate`.  
MongoDB compresses log files beyond the two most recent logs by default.

Logs:
   - `/var/log/mongodb-mms-automation/mongodb.log`

### Automation Agent Logs

You can configure the Application Database Automation Agent log rotation in the 
`MongoDBOpsManager` manifest under 
`spec.applicationDatabase.agent.startupOptions`.  

Logs:
   - `/var/log/mongodb-mms-automation/automation-agent-verbose.log`
   - `/var/log/mongodb-mms-automation/automation-agent.log`

### Audit Logs

You can configure the Application Database Audit log rotation in the `MongoDBOpsManager` 
manifest under 
`spec.applicationDatabase.agent.mongod.auditlogRotate`. 

**Note:**

The `auditLogRotate` setting depends on the `logRotate` setting. 
In order for `auditLogRotate` to take effect, you must also configure `logRotate`.

Logs:
   - `/var/log/mongodb-mms-automation/mongodb-audit.log`

### Example Manifest

```yaml
apiVersion: mongodb.com/v1
kind: MongoDBOpsManager
metadata:
  name: ops-manager
  namespace: mongodb
spec:
  replicas: 1
  version: 8.0.0
  adminCredentials: ops-manager-admin-secret
  applicationDatabase:
    version: "8.0.0"
    members: 3
    agent:
    #agent.logRotate is deprecated and overwritten by agent.mongod.logRotate.
      logRotate:
      #Automation Agent log rotation
      startupOptions:
        maxLogFiles: 10
        maxLogFileSize: 2
      #Readiness probe log rotation
      readinessProbe:
        environmentVariables:
          READINESS_PROBE_LOGGER_MAX_SIZE: 10
          READINESS_PROBE_LOGGER_BACKUPS: 1
          READINESS_PROBE_LOGGER_MAX_AGE: 3
          READINESS_PROBE_LOGGER_COMPRESS: true
          MDB_WITH_AGENT_FILE_LOGGING: false
          LOG_FILE_PATH: /var/log/mongodb-mms-automation/readiness.log
      #AppDB backup log rotation
      backupAgent:
        logRotate:
          sizeThresholdMB: "10"
          timeThresholdHrs: 10
      #AppDB Monitoring Agent log rotation
      monitoringAgent:
        logRotate:
          sizeThresholdMB: "10"
          timeThresholdHrs: 10
      #AppDB (mongod) log rotation
      mongod:
        logRotate:
          sizeThresholdMB: "10"
          timeThresholdHrs: 10
          numUncompressed: 10
          numTotal: 10
          percentOfDiskspace: 10
        auditlogRotate:
          sizeThresholdMB: "10"
          timeThresholdHrs: 10
          numUncompressed: 10
          numTotal: 10
          percentOfDiskspace: 10
```

## Ops Manager Log Rotation

To manage and rotate Ops Manager, you can either 
manually override the StatefulSet or  
use CRD settings.

### Configure Ops Manager Logs with the StatefulSet

To manage and rotate Ops Manager logs, you can manually override the default logging 
configuration using a ConfigMap and StatefulSet override. This process involves 
creating a custom `logback.xml` configuration file and applying it to your 
Ops Manager Pods.

**Step 1: Create the custom `logback.xml` configuration file.**

You can retrieve the existing `logback.xml` to use as a template by running 
the following command:

```sh
kubectl cp om-pod-spec-0:/mongodb-ops-manager/conf/logback.xml ~/Downloads/logback-confs/logback.xml
```

To learn more about creating a custom `logback.xml`, see change-onprem-log-rotation.

**Step 2: Create a ConfigMap from the custom `logback.xml`.**

Ensure that the key in the ConfigMap is exactly the name of the file you want
to replace so that the mount path and subpath only overwrite one file and 
not the entire directory. In this example, the file name is `logback.xml`:

```sh
kubectl create configmap logback-config --from-file=logback.xml=path/to/your/custom_logback.xml
```

**Step 3: Override the StatefulSet configuration.**

Use the StatefulSet override feature to mount the custom `logback.xml` in your 
Ops Manager Pods. Add the following to your StatefulSet configuration:

**Note:**

The `key` in the following ConfigMap is `logback.xml` by default to ensure 
it correctly replaces the default file with the same name.

```yaml
spec:
  template:
    spec:
      volumes:
        - name: logback-volume
          configMap:
            name: logback-config
            items:
              - key: logback.xml
                path: logback.xml
      containers:
        - name: mongodb-ops-manager
          volumeMounts:
            - name: logback-volume
            mountPath: /mongodb-ops-manager/conf-template/logback.xml
            subPath: logback.xml
```

**Step 4: Replicate the ConfigMap for multi-cluster Ops Manager deployments.**

If you are using a multi-cluster Ops Manager deployment, ensure you replicate the `logback-config` 
ConfigMap to all
member clusters.

### Configure Ops Manager Logs with the CRD

You can also manage Ops Manager log rotation by using CRD (Custom Resource Definition) settings, which simplifies
the log rotation process by linking to the ConfigMap directly in the CRD (Custom Resource Definition).

**Step 1: Create the custom `logback.xml` configuration file.**

You can retrieve the existing `logback.xml` to use as a template by running 
the following command:

```sh
kubectl cp om-pod-spec-0:/mongodb-ops-manager/conf/logback.xml ~/Downloads/logback-confs/logback.xml
```

To learn more about creating a custom `logback.xml`, see change-onprem-log-rotation.

**Step 2: (Optional) Create a custom `logback-access.xml` configuration file.**

Use the `logback-access.xml` file to configure logging for HTTP access requests, 
such as those handled by a web server. If you want to customize how these access 
logs are managed, you can create a custom `logback-access.xml` file similar 
to the `logback.xml`. 

Retrieve the existing `logback-access.xml` to use as a template by running 
the following command:

```sh
kubectl cp om-pod-spec-0:/mongodb-ops-manager/conf/logback-access.xml ~/Downloads/logback-confs/logback-access.xml
```

Modify this file according to your logging requirements.

**Step 3: Create a ConfigMap from the custom `logback.xml` and `logback-access.xml`.**

Ensure that the key in the ConfigMap is exactly the name of the file you want
to replace so that the mount path and subpath only overwrite one file and 
not the entire directory. The following examples use default file names, 
`logback.xml` and `logback-access.xml`:

```sh
kubectl create configmap logback-config --from-file=logback.xml=path/to/your/custom_logback.xml
```

```sh
kubectl create configmap logback-access-config --from-file=logback-access.xml=path/to/your/custom_access_logback.xml
```

**Step 4: Set the CRD (Custom Resource Definition) logging properties.**

Add the following settings to your Ops Manager CRD (Custom Resource Definition):

* `spec.logging.LogBackAccessRef`
* `spec.logging.LogBackRef`
* `spec.backup.logging.LogBackAccessRef`
* `spec.backup.logging.LogBackRef`

**Note:**

The file names `logback.xml` and `logback-access.xml` are the default file 
names and must be the keys 
in the ConfigMap for the Kubernetes Operator to recognize them.

For example:

```yaml
apiVersion: mongodb.com/v1
kind: MongoDBOpsManager
metadata:
  name: ops-manager
  namespace: mongodb
spec:
  replicas: 1
  version: 8.0.0
  adminCredentials: ops-manager-admin-secret
  logging:
    LogBackAccessRef: 
      name: logback-access-config
    LogBackRef:
      name: logback-config
  backup:
    enabled: true
    logging:
      LogBackAccessRef:
        name: my-logback-access-cm-backup
      LogBackRef:
        name: my-logback-cm-backup
```

The Kubernetes Operator automatically generates the volume mounts similar to 
the preceding example and links the ConfigMap files to the correct locations in 
the Ops Manager Pods.
