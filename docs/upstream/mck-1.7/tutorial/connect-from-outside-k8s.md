<!-- Converted from tutorial/connect-from-outside-k8s.txt (reStructuredText). Includes are inlined. -->

# Connect to a MongoDB Database Resource from Outside Kubernetes

The following procedure describes how to connect to a MongoDB resource
deployed in Kubernetes from outside of the Kubernetes cluster. 

## Prerequisite

### Compatible MongoDB Versions

For your databases to be accessed outside of Kubernetes, they must run
MongoDB 4.2.3 or later.

## Considerations

### Configure Readiness Probe Overrides

If you create custom services that require external access to MongoDB custom
resources deployed by the Kubernetes Operator and use readiness probes
in Kubernetes, set the `publishNotReadyAddresses` setting in Kubernetes to `true`.

The `publishNotReadyAddresses` setting indicates that an agent that
interacts with endpoints for this service should disregard the service's
`ready`
state. Setting `publishNotReadyAddresses` to `true` overrides the
behavior of the readiness probe configured for the Pod hosting your service.

By default, the `publishNotReadyAddresses` setting is set to `false`.
In this case, when the Pods that host the MongoDB custom resources in the
Kubernetes Operator lose connectivity to Cloud Manager or Ops Manager, the
readiness probes configured for these Pods fail.
However, when you set the  `publishNotReadyAddresses` setting to `true`:

- Kubernetes does not shut down the service whose readiness probe fails.
- Kubernetes considers all endpoints as `ready`
  even if the probes for the Pods hosting the services for these endpoints
  indicate that they aren't ready.
- MongoDB custom resources are still available for read and write operations.

**See also:**

- [Kubernetes API Reference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/) and search for `publishNotReadyAddresses`
- `DNS for Services in Pods`
- `Configure Readiness Probes`

## Procedure

The following procedure walks you through the process of configuring external 
connectivity for your deployment by using the built-in configuration options in 
the Kubernetes Operator.

How you connect to a MongoDB resource that the Kubernetes Operator deployed
from outside of the Kubernetes cluster depends on the resource.

**standalone:**

To connect to your Kubernetes Operator-deployed MongoDB 
standalone resource from outside of the Kubernetes cluster:

**Step 1: Deploy a standalone resource with the Kubernetes Operator.**

If you haven't deployed a standalone resource, follow the instructions to
deploy one.

This procedure uses the following example:

```yaml
---
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: <my-standalone>
spec:
  version: "8.0.0"
  opsManager:
    configMapRef:
      name: <configMap.metadata.name>
            # Must match metadata.name in ConfigMap file
  credentials: <mycredentials>
  type: Standalone
...
```

**Step 2: Create an external service for the MongoDB Pod.**

To connect to your standalone resource from an external resource, configure the 
spec.externalAccess setting:

```yaml
externalAccess: {}
```

This setting instructs the Kubernetes Operator to create an external `LoadBalancer` service for the MongoDB Pod in your 
standalone resource. The external service provides an entry point for external connections.
Adding this setting with no values creates an external service with the following default
values:

| Field | Value | Description |
|---|---|---|
| `Name` | `<pod-name>-svc-external` | Name of the external service. You can't change this value. |
| `Type` | `LoadBalancer` | Creates an external `LoadBalancer` service. |
| `Port` | `<Port Number>` | A port for `mongod`. |
| `publishNotReadyAddress` | `true` | Specifies that `DNS records` are created even if the Pod isn't ready. Do not set to `false` for any database Pod. |

Optionally, if you need to add values to the service or override the default values,
specify:

- Annotations specific to your cloud provider, in `spec.externalAccess.externalService.annotations`

- Overrides for the service specification, in `spec.externalAccess.externalService.spec`.

For example, the following settings override the default values for the external service 
to configure your standalone resource to create `NodePort services` that expose the MongoDB Pod:

```yaml
externalAccess:
  externalService: 
    annotations:
      # cloud-specific annotations for the service
    spec:
      type: NodePort # default is LoadBalancer
      port: 27017
      # you can specify other spec overrides if necessary
```

**Tip:**

To learn more, see [annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/)
and `ServiceSpec` 
in the Kubernetes documentation.

**Step 3: Verify the external services.**

In your standalone resource, run the following command to verify that the 
Kubernetes Operator created the external service for your deployment.

```sh
$ kubectl get services
```

The command returns a list of services similar to the following output.
For each database Pod in the cluster, the Kubernetes Operator creates an external service 
named <pod-name>-0-svc-external. This service is configured according to the values 
and overrides you provide in the external service specification.

```sh
NAME                                  TYPE         CLUSTER-IP   EXTERNAL-IP       PORT(S)           AGE
<my-standalone>-0-svc-external   LoadBalancer   10.102.27.116    <lb-ip-or-fqdn>   27017:27017/TCP    8m30s
```

Depending on your cluster configuration or cloud provider, 
the IP address of the LoadBalancer service is an externally 
accessible IP address or FQDN (fully qualified domain name). You can use the IP address or FQDN (fully qualified domain name) 
to route traffic from your external domain. 

**Step 4: Test the connection to the standalone resource.**

To connect to your deployment from outside of the Kubernetes cluster, 
use the MongoDB Shell (`mongosh`) and specify the MongoDB Pod address 
that you've exposed through the external domain. 

**Example:**

If you have an external FQDN (fully qualified domain name) of `<my-standalone>.<external-domain>`, you can
connect to this sharded cluster instance from outside of the Kubernetes
cluster by using the following command:

```sh
mongosh "mongodb://<my-standalone>.<external-domain>"
```

**repl:**

**Important:**

This procedure explains the simplest way to 
enable external connectivity. You can use other
utilities in production.

To connect to your Kubernetes Operator-deployed MongoDB replica 
set resource from outside of the Kubernetes cluster:

**Step 1: Deploy a replica set with the Kubernetes Operator.**

If you haven't deployed a replica set, follow the instructions to
deploy one.

You must enable TLS (Transport Layer Security) for the replica set by providing a value for 
the `spec.security.certsSecretPrefix` setting. The replica 
set must use a custom CA (Certificate Authority) certificate stored with 
`spec.security.tls.ca`.

**Step 2: Create an external service for the MongoDB Pods.**

To connect to your replica set from an external resource, configure the 
spec.externalAccess setting:

```yaml
externalAccess: {}
```

This setting instructs the Kubernetes Operator to create an external `LoadBalancer` service for the MongoDB Pods in your 
replica set. The external service provides an entry point for external connections.
Adding this setting with no values creates an external service with the following default
values:

| Field | Value | Description |
|---|---|---|
| `Name` | `<pod-name>-svc-external` | Name of the external service. You can't change this value. |
| `Type` | `LoadBalancer` | Creates an external `LoadBalancer` service. |
| `Port` | `<Port Number>` | A port for `mongod`. |
| `publishNotReadyAddress` | `true` | Specifies that `DNS records` are created even if the Pod isn't ready. Do not set to `false` for any database Pod. |

Optionally, if you need to add values to the service or override the default values,
specify:

- Annotations specific to your cloud provider, in `spec.externalAccess.externalService.annotations`

- Overrides for the service specification, in `spec.externalAccess.externalService.spec`.

For example, the following settings override the default values for the external service 
to configure your replica set to create `NodePort services` that expose the MongoDB Pods:

```yaml
externalAccess:
  externalService: 
    annotations:
      # cloud-specific annotations for the service
    spec:
      type: NodePort # default is LoadBalancer
      port: 27017
      # you can specify other spec overrides if necessary
```

**Tip:**

To learn more, see [annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/)
and `ServiceSpec` 
in the Kubernetes documentation.

**Step 3: Add Subject Alternate Names to your TLS (Transport Layer Security) certificates.**

Add each external DNS (Domain Name System) name to the certificate SAN (Subject Alternative Name).

**Step 4: Verify the external services.**

In your replica set, run the following command to verify that the 
Kubernetes Operator created the external service for your deployment.

```sh
$ kubectl get services
```

The command returns a list of services similar to the following output.
For each database Pod in the cluster, the Kubernetes Operator creates an external service 
named <pod-name>-<pod-idx>-svc-external. This service is configured according to the values 
and overrides you provide in the external service specification.

```sh
NAME                                  TYPE         CLUSTER-IP   EXTERNAL-IP       PORT(S)           AGE
<my-replica-set>-0-svc-external   LoadBalancer   10.102.27.116    <lb-ip-or-fqdn>   27017:27017/TCP    8m30s
```

Depending on your cluster configuration or cloud provider, 
the IP address of the LoadBalancer service is an externally 
accessible IP address or FQDN (fully qualified domain name). You can use the IP address or FQDN (fully qualified domain name) 
to route traffic from your external domain. 

**Step 5: Open your replica set resource YAML (Yet Another Markup Language) file.**

**Step 6: Copy the sample replica set resource.**

Change the settings of this YAML (Yet Another Markup Language) file to match your
desired replica set configuration.

```yaml
---
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: <my-replica-set>
spec:
  members: 3
  version: "8.0.0"
  type: ReplicaSet
  opsManager:
    configMapRef:
      name: <configMap.metadata.name>
  credentials: <mycredentials>
  persistent: true
```

```yaml
  security:
    tls:
      enabled: true
  connectivity:
    replicaSetHorizons:
      - "example-website": "web1.example.com:30907"
      - "example-website": "web2.example.com:32350"
      - "example-website": "web3.example.com:31185"
...
```

**Step 7: Paste the copied example section into your existing replica set resource.**

Open your preferred text editor and paste the [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification
at the end of your resource file in the `spec` section.

**Step 8: Change the highlighted settings to your preferred values.**

* - Key
  - Type
  - Necessity
  - Description
  - Example

* - | `spec.connectivity`
    | `.replicaSetHorizons`
  - collection
  - Conditional
  - Add this parameter and values if you need your database to be
    accessed outside of Kubernetes. This setting allows you to provide
    different DNS (Domain Name System) settings within the Kubernetes cluster and to the
    Kubernetes cluster. The Kubernetes Operator uses split horizon DNS (Domain Name System) for
    replica set members. This feature allows communication both
    within the Kubernetes cluster and from outside Kubernetes.

    You may add multiple external mappings per host.

    Split Horizon Requirements

    - Make sure that each value in this array is unique.

    - Make sure that the number of entries in this array matches
      the value given in `spec.members`.

    - Provide a value for the
      `spec.security.certsSecretPrefix` setting to
      enable TLS (Transport Layer Security). This method to use split horizons requires the
      Server Name Indication extension of the TLS (Transport Layer Security) protocol.
  - `See Setting`

* - | `spec.security`
    | `certsSecretPrefix`
  - string
  - Required
  - Add the `<prefix>` of the secret 
    name that contains your MongoDB deployment's TLS (Transport Layer Security) certificates.
  - `devDb`

**Step 9: Confirm the external hostnames and external service values in your replica set resource.**

Confirm that the external hostnames in the
`spec.connectivity.replicaSetHorizons` setting are correct.

External hostnames should match the DNS (Domain Name System) names of Kubernetes worker nodes.
These can be *any* nodes in the Kubernetes cluster. Kubernetes nodes use internal
routing if the pod runs on another node.

Set the ports in `spec.connectivity.replicaSetHorizons` to
the external service values.

**Example:**

```yaml
  security:
    tls:
      enabled: true
  connectivity:
    replicaSetHorizons:
      - "example-website": "web1.example.com:30907"
      - "example-website": "web2.example.com:32350"
      - "example-website": "web3.example.com:31185"
...
```

**Step 10: Save your replica set config file.**

**Step 11: Update and restart your replica set deployment.**

In any directory, invoke the following Kubernetes command to update and 
restart your replica set:

```sh
kubectl apply -f <replica-set-conf>.yaml
```

**Step 12: Test the connection to the replica set.**

In the development environment, for each host in a replica set, run
the following command:

```sh
mongosh --host <my-replica-set>/web1.example.com \
      --port 30907
      --ssl \
      --sslAllowInvalidCertificates
```

**Note:**

Don't use the `--sslAllowInvalidCertificates` flag in production.

In production, for each host in a replica set, specify the TLS (Transport Layer Security)
certificate and the CA (Certificate Authority) to securely connect to client tools or
applications:

```sh
mongosh --host <my-replica-set>/web1.example.com \
  --port 30907 \
  --tls \
  --tlsCertificateKeyFile server.pem \
  --tlsCAFile ca-pem
```

If the connection succeeds, you should see:

```javascript
Enterprise <my-replica-set> [primary]
```

**shard:**

To connect to your Kubernetes Operator-deployed MongoDB sharded
cluster resource from outside of the Kubernetes cluster:

**Step 1: Deploy a sharded cluster with the Kubernetes Operator.**

If you haven't deployed a sharded cluster, follow the instructions to
deploy one.

You must enable TLS (Transport Layer Security) for the sharded cluster by configuring the 
following settings:

| Key | Type | Necessity | Description | Example |
|---|---|---|---|---|
| \| `spec.security` \| `.certsSecretPrefix` | string | Required | Add the `<prefix>` of the secret name that contains your MongoDB deployment's TLS (Transport Layer Security) certificates. | `devDb` |
| \| `spec.security.tls` \| `.additionalCertificateDomains` | collection | Optional | List of every domain that should be added to TLS (Transport Layer Security) certificates to each pod in this deployment. When you set this parameter, every CSR (Certificate Signing Request) that the Kubernetes Operator transforms into a TLS (Transport Layer Security) certificate includes a SAN (Subject Alternative Name) in the form `<pod name>.<additional cert domain>`. | `example.com` |

**Step 2: Create an external service for the `mongos` Pods.**

To connect to your sharded cluster from an external resource, configure the 
spec.externalAccess setting:

```yaml
externalAccess: {}
```

This setting instructs the Kubernetes Operator to create an external `LoadBalancer` service for the `mongos` Pods in your 
sharded cluster. The external service provides an entry point for external connections.
Adding this setting with no values creates an external service with the following default
values:

| Field | Value | Description |
|---|---|---|
| `Name` | `<pod-name>-svc-external` | Name of the external service. You can't change this value. |
| `Type` | `LoadBalancer` | Creates an external `LoadBalancer` service. |
| `Port` | `<Port Number>` | A port for `mongod`. |
| `publishNotReadyAddress` | `true` | Specifies that `DNS records` are created even if the Pod isn't ready. Do not set to `false` for any database Pod. |

Optionally, if you need to add values to the service or override the default values,
specify:

- Annotations specific to your cloud provider, in `spec.externalAccess.externalService.annotations`

- Overrides for the service specification, in `spec.externalAccess.externalService.spec`.

For example, the following settings override the default values for the external service 
to configure your sharded cluster to create `NodePort services` that expose the `mongos` Pods:

```yaml
externalAccess:
  externalService: 
    annotations:
      # cloud-specific annotations for the service
    spec:
      type: NodePort # default is LoadBalancer
      port: 27017
      # you can specify other spec overrides if necessary
```

**Tip:**

To learn more, see [annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/)
and `ServiceSpec` 
in the Kubernetes documentation.

**Step 3: Add Subject Alternate Names to your TLS (Transport Layer Security) certificates.**

Add each external DNS (Domain Name System) name to the certificate SAN (Subject Alternative Name).

Each MongoDB host uses the following SAN (Subject Alternative Name)\s:

```sh
<my-sharded-cluster>-<shard>-<pod-index>.<external-domain>
<my-sharded-cluster>-config-<pod-index>.<external-domain>
<my-sharded-cluster>-mongos-<pod-index>.<external-domain>
```

The `mongos` instance uses the following SAN (Subject Alternative Name):

```sh
<my-sharded-cluster>-mongos-<pod-index>-svc-external.<external-domain>
```

Configure the `spec.security.tls.additionalCertificateDomains` setting similar
to the following example. Each TLS (Transport Layer Security) certificate that you use must include the 
corresponding SAN (Subject Alternative Name) for the shard, config server, or `mongos` instance.  
The Kubernetes Operator validates your configuration. 

```yaml
---
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: <my-sharded-cluster>
spec:
  version: "8.0.0"
  opsManager:
    configMapRef:
      name: <configMap.metadata.name>
            # Must match metadata.name in ConfigMap file
  shardCount: 2
  mongodsPerShardCount: 3
  mongosCount: 2
  configServerCount: 3
  credentials: my-secret
  type: ShardedCluster
  externalAccess: {}
  security:
    tls:
      certsSecretPrefix: <prefix>
      additionalCertificateDomains:
         - "<external-domain>"
...
```

**Step 4: Verify the external services.**

In your sharded cluster, run the following command to verify that 
the Kubernetes Operator created the external services for your deployment.

```sh
$ kubectl get services
```

The command returns a list of services similar to the following output.
For each `mongos` instance in the cluster, the Kubernetes Operator creates an external service 
named `<pod-name>-<pod-idx>-svc-external`. This service is configured according to the values 
and overrides you provide in the external service specification.

```sh
NAME                                              TYPE         CLUSTER-IP     EXTERNAL-IP       PORT(S)           AGE
<my-sharded-cluster>-mongos-0-svc-external    LoadBalancer   10.102.27.116  <lb-ip-or-fqdn>   27017:27017/TCP    8m30s
<my-sharded-cluster>-mongos-1-svc-external    LoadBalancer   10.102.27.116  <lb-ip-or-fqdn>   27017:27017/TCP    8m30s
```

Depending on your cluster configuration or cloud provider, the IP address of the 
LoadBalancer service is an externally accessible IP address or FQDN (fully qualified domain name). You can use 
the IP address or FQDN (fully qualified domain name) to route traffic from your external domain. This example 
has two `mongos` instances, therefore the Kubernetes Operator creates two external services.

**Step 5: Test the connection to the sharded cluster.**

To connect to your deployment from outside of the Kubernetes cluster, 
use the MongoDB Shell (`mongosh`) and specify the addresses for the `mongos` instances 
that you've exposed through the external domain. 

**Example:**

If you have external FQDN (fully qualified domain name) of `<my-sharded-cluster>-mongos-0-svc-external.<external-domain>` and `<my-sharded-cluster>-mongos-1-svc-external.<external-domain>` addressCommand: mongodb://<my-sharded-cluster>-mongos-0-svc-external.<external-domain>,<my-sharded-cluster>-mongos-1-svc-external.<external-domain>, you can
connect to this sharded cluster instance from outside of the Kubernetes
cluster by using the following command:

```sh
mongosh ""
```
