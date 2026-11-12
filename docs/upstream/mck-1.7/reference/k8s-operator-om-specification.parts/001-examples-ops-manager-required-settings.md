<!-- Part 1 of 5 of reference/k8s-operator-om-specification.md (split because the page is big). -->

## Examples

The following examples show a resource specification for an Ops Manager
deployment:

**single-cluster:**

```yaml
apiVersion: mongodb.com/v1
kind: MongoDBOpsManager
metadata:
 name: om
spec:
 topology: SingleCluster # optional, SingleCluster by default
 opsManagerURL: https://link.to.configured.load-balancer.example.com # optional OM URL for the operator
replicas: 1
version: "8.0.0"
 adminCredentials: ops-manager-admin-secret
 configuration:
  mms.fromEmailAddr: admin@example.com
  mms.security.allowCORS: "false"
 security:
   tls:
     ca: issuer-ca
 backup:
  enabled: true
  encryption:
    kmip:
      server:
        url: kmip.corp.mongodb.com:5696
        ca: mongodb-kmip-certificate-authority-pem
  headDB:
   storage: "30Gi"
   labelSelector:
    matchLabels:
     app: my-app
  opLogStores:
   - name: oplog1
                       # Sets labels for the oplog store.
     assignmentLabels: ["test1", "test2"]
     mongodbResourceRef:
      name: my-oplog-db
     mongodbUserRef:
      name: my-oplog-user
  s3Stores:
   - name: s3store1
                       # Sets labels for the S3 store.
     assignmentLabels: ["test1", "test2"]

     mongodbResourceRef:
      name: my-s3-metadata-db
     mongodbUserRef:
      name: my-s3-store-user
     s3SecretRef:
       name: my-s3-credentials
     pathStyleAccessEnabled: true
     s3BucketEndpoint: s3.region.amazonaws.com
     s3BucketName: my-bucket
 applicationDatabase:
   passwordSecretKeyRef:
    name: om-db-user-secret
    key: password
   members: 3
   topology: SingleCluster
   version: "7.0.21-ubi8"
   featureCompatibilityVersion: "6.0" # During upgrade, set this FCV value to your currently deployed AppDB version.
   security:
     certsSecretPrefix: appdb
     tls:
       ca: issuer-ca
```

**multi-cluster:**

```yaml
apiVersion: mongodb.com/v1
kind: MongoDBOpsManager
metadata:
 name: om
spec:
 topology: MultiCluster # optional, SingleCluster by default
 opsManagerURL: https://link.to.configured.lb.example.com # optional OM URL for the operator
 clusterSpecList: # optional ClusterSpecOMItem list, the type is different than ClusterSpecItem for AppDB and MongoDB
   - clusterName: cluster-1 # required
     replicas: 1 # required, OM application replicas
     # optional parameters to override those defined at MongoDBOpsManager level
     clusterDomain: cluster-1.example.com # optional, default cluster.local
     jvmParameters: ["-Xmx4352m","-Xms4352m"]
     externalConnectivity: # optional to override
       type: LoadBalancer
       port: 9090
       annotations:
         key: value
     statefulSet: # StatefulSetSpecWrapper override
       spec: {}
       metadata: {}
     configuration:
       automation.versions.source: mongodb
       mms.adminEmailAddr: cloud-manager-support@mongodb.com
     backup: # MongoDBOpsManagerBackup, optional, we only support a subset of fields
       members: 1 # backup daemon replicas, optional, default=1
       assignmentLabels: [] # assignment labels to override
       jvmParameters: ["-Xmx4352m","-Xms4352m"] # optional
       statefulSet: # mdbc.StatefulSetConfiguration, optional to override for backup daemon
         spec: {}
         metadata: {}
   - clusterName: cluster-2
     replicas: 1

     ....

replicas: 1
 version: "8.0.0"
 adminCredentials: ops-manager-admin-secret
 configuration:
  mms.fromEmailAddr: admin@example.com
  mms.security.allowCORS: "false"
 backup:
  enabled: true
  encryption:
    kmip:
      server:
        url: kmip.corp.mongodb.com:5696
        ca: mongodb-kmip-certificate-authority-pem
  headDB:
   storage: "30Gi"
   labelSelector:
    matchLabels:
     app: my-app
  opLogStores:
   - name: oplog1
                       # Sets labels for the oplog store.
     assignmentLabels: ["test1", "test2"]
     mongodbResourceRef:
      name: my-oplog-db
     mongodbUserRef:
      name: my-oplog-user
  s3Stores:
   - name: s3store1
                       # Sets labels for the S3 store.
     assignmentLabels: ["test1", "test2"]

     mongodbResourceRef:
      name: my-s3-metadata-db
     mongodbUserRef:
      name: my-s3-store-user
     s3SecretRef:
       name: my-s3-credentials
     pathStyleAccessEnabled: true
     s3BucketEndpoint: s3.region.amazonaws.com
     s3BucketName: my-bucket
 security:
   tls:
     ca: issuer-ca
 applicationDatabase:
   passwordSecretKeyRef:
    name: om-db-user-secret
    key: password
   version: "8.0.0-ubi8"
   topology: MultiCluster
   clusterSpecList:
    - clusterName: cluster1.example.com
      members: 4
    - clusterName: cluster2.example.com
      members: 3
    - clusterName: cluster3.example.com
      members: 2
   security:
    certsSecretPrefix: appdb
    tls:
     ca: issuer-ca
```


## Ops Manager Required Settings

This section describes settings that you must use for all Ops Manager
resources.

**`apiVersion`**

*Type*: string

*Required*. Version of the MongoDB Kubernetes resource schema.

**`kind`**

*Type*: string

*Required*. Kind of MongoDB Kubernetes resource to create. Set this
to `MongoDBOpsManager`.

**`metadata.name`**

*Type*: string

*Required*. Name of the MongoDB Kubernetes resource you are creating.

Resource names must be 44 characters or less.

**`spec.version`**

*Type*: string

*Required*. Version of Ops Manager that you want to install
on this MongoDB Kubernetes resource. 

**`spec.adminCredentials`**

*Type*: string

*Required*. Name of the Kubernetes [secret](https://kubernetes.io/docs/concepts/configuration/secret/) you created for
the Ops Manager admin user. When you deploy the Ops Manager resource,
Kubernetes Operator creates a user with these credentials.

**Note:**

To avoid storing secrets in single-cluster Kubernetes deployments, you can
migrate all [secrets](https://kubernetes.io/docs/concepts/configuration/secret/) to a secret storage tool.
Deployments on multiple Kubernetes clusters don't support storing secrets
in secret storage tools, such as [HashiCorp Vault](https://www.vaultproject.io/).

The admin user is granted the
`Global Owner`
role.

**`spec.replicas`**

*Type*: integer

*Conditional*. Number of Ops Manager instances to run in parallel.
If you specify `SingleCluster` in `spec.topology`, this
parameter is required. The mimimum accepted value is `1`. 

If you specify `MultiCluster` in `spec.topology`, this
parameter is ignored.
