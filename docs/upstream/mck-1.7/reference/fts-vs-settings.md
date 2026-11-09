<!-- Converted from reference/fts-vs-settings.txt (reStructuredText). Includes are inlined. -->

# MongoDB Search and Vector Search Settings

You can deploy MongoDB Search and Vector Search alongside MongoDB v8.0
or higher using MongoDB Controllers for Kubernetes Operator.

## Example Resource Specification

The following example shows the settings inside the `spec` object for
MongoDB Search and Vector Search deployment. To learn more about these
settings, see the k8s-fts-vs-required-settings and
k8s-fts-vs-optional-settings. 

**Example:**

```yaml
spec:
  source:
    mongodbResourceRef: 
      name: mdb
    external: 
      hostAndPorts:
        - mdb-rs-external-0.example.com:27017
        - mdb-rs-external-1.example.com:27017
        - mdb-rs-external-2.example.com:27017
      tls:
        ca:
          name: mdbc-rs-ca            
    username: search-sync-source
    passwordSecretRef:
      name: mdbc-rs-search-sync-source-password
      key: password
  security:
    tls:
      certificateKeySecretRef:
        name: mdbs-tls-secret        
  resourceRequirements:
    limits:
      cpu: "3"
      memory: 5Gi
    requests:
      cpu: "2"
      memory: 3Gi
  autoEmbedding:
    embeddingModelAPIKeySecret: 
      name: embedding-model-api-query-key
    providerEndpoint: https://ai.mongodb.com/v1/embeddings
  logLevel: INFO
  prometheus: {}
```

## Required Settings

This section describes the settings that are required for deploying 
the MongoDB Search and Vector Search resource. If you define only the
required settings in the Custom Resource Definition (CRD), the
MongoDB Controllers for Kubernetes Operator uses the defaults for all optional settings to configure MongoDBSearch.  

`apiVersion`
  *Type*: string

  Version of the MongoDB Kubernetes resource schema. Set the value to
  `mongodb.com/v1`. 

`kind`
  *Type*: string

  Kind of MongoDB Kubernetes resource to create. Set this to MongoDBSearch.

`metadata.namespace`
  *Type*: string

  Namespace where the MongoDBSearch resource should be created. To
  leverage automatic configuration of MongoDBSearch and `MongoDB`
  or `MongoDBCommunity` resources, the MongoDBSearch resource
  should be created in the same namespace as the `MongoDB` or
  `MongoDBCommunity` resource. 

`metadata.name`
  *Type*: string

  Unique identifier of the MongoDBSearch resource. The resource name can
  be a maximum of 44 characters in length. 

## Optional Settings

This section describes the optional settings for the MongoDB Search and
Vector Search resource. If you omit the optional settings and define
only the required settings in the CRD (Custom Resource Definition), the MongoDB Controllers for Kubernetes Operator uses the
defaults for all optional settings to configure MongoDBSearch. 

### Settings for Configuring the Data Source

`spec.source`
  *Type*: object 

  Setting that describes the MongoDB source replica set for `mongot`.
  This is required if: 

  - `MongoDB` is external
  - `MongoDB` has a different name from MongoDBSearch

  The MongoDBSearch resource must always be connected to the
  replica set. If you deployed the replica set using the Kubernetes Operator
  with `MongoDB` or `MongoDBCommunity` CRD (Custom Resource Definition), and if `spec.source`
  is empty, the Kubernetes Operator uses the following based on the
  `metadata.name` to look for the database in Kubernetes: 

  - Find `MongoDB` or `MongoDBCommunity` resources with the same name
    as set for `metadata.name` in MongoDBSearch, in the same
    namespace. 
  - Find the password secret for the `mongot` user from the
    `<MongoDBSearch.metadata.name>-search-sync-source-password` secret. 

`spec.source.mongodbResourceRef.name`
  *Type*: string 

  Name of the `MongoDB` or `MongoDBCommunity` resource to associate 
  with this MongoDB Search and Vector Search resource. You can't have
  more than one MongoDBSearch resource referencing the same
  `MongoDB` or `MongoDBCommunity` resource. If you specify a
  different name, you must explicitly point to the `MongoDB` or 
  `MongoDBCommunity` where you want to enable MongoDB Search and
  Vector Search.   

  Use this field only if your `MongoDB` or `MongoDBCommunity`
  resource is deployed in the same Kubernetes cluster and is in the same
  namespace as your MongoDBSearch resource. Setting this field
  allows the Kubernetes Operator to automatically:

  - Set proper connection strings to the database.
  - Reconfigure MongoDB database deployments by setting necessary parameters to
    enable search functionality and configure the addresses of the search
    pods.
  
  If your database is deployed outside of Kubernetes or is in a different
  namespace, use `spec.external` to configure connection to the
  database. This field is mutually exclusive with `spec.external`.

  If omitted, the Kubernetes Operator will look for `MongoDB` or
  `MongoDBCommunity` resource with the same name as this MongoDBSearch
  resource. 

### Setting for Configuring `mongot` User

`spec.source.username`
  *Type*: string 

  Username to use to authenticate `mongot` with `mongod`. The
  specified user must have the `searchCoordinator` role. If
  omitted, the Kubernetes Operator assumes the username is
  `search-sync-source`. 

`spec.source.passwordSecretRef.name`
  *Type*: string 

  Name of the secret that contains the password that `mongot` must use
  to authenticate with `mongod`. If omitted, defaults to 
  `<MongoDBSearch.metadata.name>-search-sync-source-password`. 

`spec.source.passwordSecretRef.key`
  *Type*: string 

  Key under which the password value is stored in the secret. If
  omitted, defaults to `password`.

### Settings for Connecting to External MongoDB

The following settings are only required for configuring a connection to
an external MongoDB replica set.

`spec.source.external`
  *Type*: object 

  Settings that describe the external data source. This object describes
  the settings for the MongoDB Search and Vector Search resource to
  connect to an external MongoDB. These settings should be specified
  only if you want to connect to an external MongoDB that wasn't
  deployed using the Kubernetes Operator. If specified, these settings
  override settings for `spec.source.mongodbResourceRef.name`. If you
  used the Kubernetes Operator to install MongoDB in the same cluster, these
  settings are optional.

`spec.source.external.hostAndPorts`
  *Type*: array of strings

  List of hostnames and ports of the external replica set. This is a
  host seed list to the MongoDB replica set. The `mongot` connects
  to the database in a replica set mode and gets the list of all other
  nodes using `db.hello()`.

  **Example:**

  ```shell
  hostAndPorts: 
    - mdbc-rs-0.my-external-domain.example.com:27017
    - mdbc-rs-1.my-external-domain.example.com:27017
    - mdbc-rs-2.my-external-domain.example.com:27017
  ```

`spec.source.external.tls`
  *Type*: object 

  TLS Settings that `mongot` must use when connecting to the external
  MongoDB database. 

`spec.source.external.tls.ca.name`
  *Type*: string 

  Name of the Secret containing the trusted chain of the certificate
  authorities that issued the TLS certificate used by the `mongod`
  nodes. 

  **Example:**

  ```yaml
  spec:
    source:
      external:
        tls:
          ca: 
            name: trusted-ca
  ```

  
  The certificate (or certificates if this is a chain of trusted
  CA certificates) must be specified under `ca.crt` key in this
  Secret. 

  **Example:**

  ```yaml
  name: Secret
  apiVersion: v1
  metadata:
    name: trusted-ca
  data:
    ca.crt: |
      -----BEGIN CERTIFICATE-----
      MIIDBTCCAe2gAwIBAgIIH3EOUAGAsx0wDQYJKoZIhvcNAQELBQAwFTETMBEGA1UE
      [...]
      U/4rN8Ias/FONYFRtGfs9uXHmo2MP04BF+9ED2dlbNDUbat+6XCozLJj98nI4VEi
      qaV3JrVFHTgN
      -----END CERTIFICATE-----
  ```

### Settings for Security

`spec.security`
  *Type*: object 

  Security settings for `mongot` listen server.

`spec.security.tls`
  *Type*: object 

  TLS (Transport Layer Security) settings for `mongot`. If
  omitted, `mongot` won't use TLS for incoming connections.

`spec.security.tls.certificateKeySecretRef.name`
  *Type*: string 

  Name of  a TLS secret in the same namespace containing private key
  (`tls.key`) and the certificate (`tls.crt`). The secret can be of
  type `kubernetes.io/tls` (that is issued by cert-manager) or can be
  created manually. This is required for enabling TLS (Transport Layer Security) in `mongot`.

### Settings for Provisioning Resources

`spec.resourceRequirements`
  *Type*: [core/v1/ResourceRequirements](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.34/#resourcerequirements-v1-core) 

  CPU and memory that the `mongodb-search` container can
  request and be limited to. We recommend using this field to customize
  resource allocations instead of overriding it with
  `spec.statefulSet`.

  If omitted, the Kubernetes Operator uses the following default
  values: 

  ```yaml
  requests: 
    cpu: 2
    memory: 2G
  ```

`spec.resourceRequirements.limits`
  *Type*: object 

  Upper cap on the resource, CPU and memory, that the `mongodb-search`
  container can consume. By default, there are no limits set. If
  omitted, the pod isn't restricted and so, might use all the resources
  on the node. We recommend setting limits based on your workload. 

`spec.resourceRequirements.requests`
  *Type*: object 

  Amount of CPU and memory requested for the `mongodb-search`
  container. If omitted, the Kubernetes Operator uses the following default 
  values: 

  ```yaml
  requests: 
    cpu: 2
    memory: 2G
  ```

`spec.persistence.single`
  *Type*: object 

  Storage configuration for MongoDB Search and Vector Search
  persistence volume where MongoDB Search and Vector Search indexes are
  stored. Each search instance (pod) has its own independent storage to
  maintain indexes, which isn't shared with the MongoDB database. Only
  index metadata (definitions) are stored in the database itself.

  | Scalar | Data Type | Description |
  |---|---|---|
  | `labelSelector` | string | [Tag](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#selector) used to bind mounted volumes to directories. |
  | `storage` | string | Minimum size of [Persistent Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) that should be mounted. This value is expressed as an integer followed by a unit of storage in JEDEC (Joint Electron Device Engineering Council Solid State Technology Association) notation. Default value is 16Gi. For example, if replica set requires 60 gigabytes of storage space, set this value to `60Gi`. |
  | `storageClass` | string | Type of storage specified in a [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims). You may create this storage type as a [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) object before using it in this [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification. Make sure to set the [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) `reclaimPolicy` to [Retain](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#retain). This ensures that data is retained when a [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) is removed. |

  MongoDBSearch supports only `single` persistence field. If omitted,
  the Kubernetes Operator sets `spec.persistence.single.storage` to `10GB`.

### Settings for Logging

`spec.logLevel`
  *Type*: string 

  Verbosity of the `mongot` logs. Value can be one of the following: 

  - `TRACE`
  - `DEBUG`
  - `INFO`
  - `WARN`
  - `ERROR`

  If omitted, defaults to `INFO`.

### Settings for Metrics

`spec.prometheus` 
  *Type*: object

  **This is available only in v1.6 and later.**
  
  Configuration to enable Prometheus metrics endpoint. If omitted, the
  metrics endpoint in `mongot` is disabled. To enable Prometheus
  metrics endpoint on the default port (`9946`), specify an empty
  `{}` object in the `spec.prometheus` field. To change the port,
  set it in `spec.prometheus.port` field. 

`spec.prometheus.port`
  *Type*: string

  Port on which to enable Prometheus metrics endpoint. By default,
  Prometheus metrics endpoint is enabled on port `9946`.

### Settings for Automated Embedding

**Important:**

Automated embedding is available as a Preview feature for only MongoDB 
Community Edition deployment. The feature and corresponding documentation 
might change at any time during the Preview period. To learn more, see 
[Preview Features](https://www.mongodb.com/docs/preview-features/). 

`spec.autoEmbedding`
  *Type*: Object 

  Configuration for Automated Embedding for 
  text data in your collection.

`spec.autoEmbedding.embeddingModelAPIKeySecret`
  *Type*: Object

  Configuration for the embedding model provider API (Application Programming Interface) keys. To enable 
  Automated Embedding, you must create two keys, one for generating 
  embeddings at index-time for data in your collection and another for 
  generating embeddings at query-time for the query text. If you don't 
  already have the keys, we recommend that you create keys from two Atlas 
  projects. To learn more about creating keys for the Atlas projects 
  from the Atlas UI, see Manage API Keys.

`spec.autoEmbedding.embeddingModelAPIKeySecret.name`
  *Type*: string

  Name of the secret that contains the embedding model API (Application Programming Interface) keys that 
  `mongot` must use to generate embeddings at index- and query-time.

`spec.autoEmbedding.providerEndpoint`
  *Type*: string

  Embedding model endpoint URL for generating embeddings. Value varies 
  based on whether you create the keys from the Atlas UI (recommended) 
  or directly from the embedding service (Voyage AI). For keys created 
  from: 

  - Atlas UI, value is `https://ai.mongodb.com/v1/embeddings` (default)
  - Voyage AI, value is `https://api.voyageai.com/v1/embeddings`

### Other Settings

`spec.version`
  *Type*: string 

  Version of `mongodb-search` docker image. If omitted, the
  Kubernetes Operator automatically chooses the newest version of
  MongoDBSearch. You can set it explicitly to prevent
  automatic upgrades when the Kubernetes Operator version is upgraded. 

`spec.statefulSet`
  *Type*: [apps/v1/StatefulSet](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.26/#statefulset-v1-apps)

  Specification for the [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/),
  created for deploying `mongot` pods, that overwrites the settings
  that the Kubernetes Operator applies. The overrides are always applied
  last. Supports both the `spec.statefulSet.spec` and
  `spec.statefulSet.metadata` fields. 

  **Note:**

  Don't set resource requirements or persistence settings using
  `spec.statefulSet`. Instead, use the `spec.resourceRequirements`
  and `spec.persistence` fields respectively.
