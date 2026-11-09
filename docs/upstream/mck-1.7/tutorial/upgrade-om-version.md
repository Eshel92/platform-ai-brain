<!-- Converted from tutorial/upgrade-om-version.txt (reStructuredText). Includes are inlined. -->

# Upgrade Ops Manager and Backing Database Versions

Update the major and minor versions of your Ops Manager instance and backing databases
in the k8s-om-specification that the Kubernetes Operator uses to manage your deployment.

## Prerequisites

**Warning:**

To maintain existing settings and availability, back up the following in your current Ops Manager instance: 

- Your `conf-mms.properties` to a secure location. The `conf-mms.properties`
  stores settings for the Ops Manager instance.
- Your `gen.key` files to a secure location. The gen.key
  provides details to encrypt and decrypt Ops Manager\'s backing databases
  and user credentials. Ops Manager might delete these files as part of the upgrade process.

As an extra precaution, you may use `mongodump` to create a binary export of the 
`Application Database`. No officially 
supported backup method exists for the Application Database. If the 
upgrade fails, contact [MongoDB Support](https://support.mongodb.com/welcome) for help fixing the 
issue with the Ops Manager version.

1. Upgrade Ops Manager by following the considerations, prerequisites, and procedure in upgrade-om.

   **Important:**

   Don't skip major Ops Manager versions when you upgrade. Upgrade to
   the latest available patch release of your current major version,
   then upgrade to the next major version. Repeat this process until
   you reach your target version. For example, to upgrade from 7.0.x
   to 8.0, first upgrade to the latest available 7.0 patch release.
   To find the upgrade path for your current version, see
   upgrade-om.

2. Reference compatible-mdb-versions to ensure your backing databases
   use a MongoDB version that is compatible with the new Ops Manager version.

3. If you need to upgrade your backing databases to a compatible MongoDB version,
   see meko-upgrade-mdb-version.

## Procedure

To upgrade Ops Manager and the application database versions, complete the
following steps: 

**Step 1: In your k8s-om-specification, the settings as shown in the following example:**

a. Set `spec.version` to the new Ops Manager version. 

#. If you upgraded your application database, set 
   `spec.applicationDatabase.version` to the compatible MongoDB 
   version. 

**Important:**

Ensure that you choose a compatible MongoDB Server version.

Compatible versions differ depending on the base image that the
MongoDB database resource uses.

**Warning:**

As shown in the example below, because the Application Database resources associated 
with your current Ops Manager deployment are upgraded in a rolling fashion, you 
must explicitly set the `featureCompatibilityVersion` to the current version 
of MongoDB that Application Database is running before starting the upgrade process.  

This prevents potential data misalignment issues between Ops Manager and 
Application Database during the upgrade process. 

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

**Step 2: Reapply the configuration to Kubernetes.**

```none
kubectl apply -f <om-resource-specification>.yaml
```

Kubernetes automatically reconfigures your deployment with the new 
specifications. You can see these changes reflected in your `Ops Manager` or 
`Cloud Manager` application.
