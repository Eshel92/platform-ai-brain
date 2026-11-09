<!-- Converted from tutorial/multi-cluster-connect-from-outside-k8s.txt (reStructuredText). Includes are inlined. -->

# Connect to Multi-Cluster Resource from Outside Kubernetes

The following procedure describes how to connect to a `MongoDBMultiCluster` resource
deployed in Kubernetes from outside of the Kubernetes cluster.

## Prerequisite

### Compatible MongoDB Versions

Databases that run MongoDB 4.2.3 or later allow you to access them outside
of the Kubernetes cluster.

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

To connect to your Kubernetes Operator-deployed replica set with a `MongoDBMultiCluster` resource
from outside of the Kubernetes cluster:

**Step 1: Deploy a Multi-Kubernetes Cluster Replica Set.**

**Step 2: Secure the Multi-Kubernetes Cluster with TLS.**

Provide values for:

- The TLS (Transport Layer Security) secret in `spec.security.certsSecretPrefix`.
- The custom CA (Certificate Authority) certificate in `spec.security.tls.ca`.

**Step 3: Create an external service for the MongoDB Pods.**

To connect to your multi-Kubernetes-cluster deployment from an external resource, configure the 
spec.externalAccess setting:

```yaml
externalAccess: {}
```

This setting instructs the Kubernetes Operator to create an external `LoadBalancer` service for the MongoDB Pods in your 
multi-Kubernetes-cluster deployment. The external service provides an entry point for external connections.
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

- Annotations specific to your cloud provider, in spec.externalAccess.externalService.annotations

- Overrides for the service specification, in spec.externalAccess.externalService.spec.

For example, the following settings override the default values for the external service 
to configure your multi-Kubernetes-cluster deployment to create `NodePort services` that expose the MongoDB Pods:

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

**Step 4: Configure an external service for cluster members.**

If you need to configure settings for a specific cluster member, 
such as when you're hosting members on different cloud providers, 
you can override the global spec.externalAccess 
settings for a specific member by using the spec.clusterSpecList.externalAccess.externalService setting. 

To add values to the service or override the default values for a 
cluster member, specify:

- Annotations specific to the cloud provider for the cluster member, in 
  spec.clusterSpecList.externalAccess.externalService.annotations.

- Overrides specific to the cluster member, in spec.clusterSpecList.externalAccess.externalService.spec.

For example, the following file configures your multi-Kubernetes cluster MongoDB deployment to 
create load balancer services that expose the multi-Kubernetes cluster MongoDB deployment for 
cluster members deployed in [GKE (Google Kubernetes Engine)](https://cloud.google.com/kubernetes-engine) and AWS (Amazon Web Services) `EKS`.

**Note:**

The following example doesn't configure overrides, so the external services 
use the default values from the spec.externalAccess 
setting.

```yaml
clusterSpecList:
  - clusterName: gke-cluster-0.mongokubernetes.com
    members: 2
    externalAccess: 
      externalService: 
        annotations:
          "cloud.google.com/l4-rbs": "enabled"  
  - clusterName: eks-cluster-1.mongokubernetes.com
    members: 2
    externalAccess: 
      externalService: 
        annotations:
          "service.beta.kubernetes.io/aws-load-balancer-type": "external",
          "service.beta.kubernetes.io/aws-load-balancer-nlb-target-type": "instance",
          "service.beta.kubernetes.io/aws-load-balancer-scheme": "internet-facing"
```

**Step 5: Add Subject Alternate Names to your TLS (Transport Layer Security) certificate.**

Add each external DNS (Domain Name System) name to the certificate SAN (Subject Alternative Name).

**Step 6: Verify the external services.**

In each cluster, run the following command to verify that the 
Kubernetes Operator created the external service for your deployment.

```sh
$ kubectl get services
```

The command returns a list of services similar to the following output.
For each database Pod in the cluster, the Kubernetes Operator creates an external service 
named <pod-name>-<cluster-idx>-<pod-idx>-svc-external. This service is configured according to the values 
and overrides you provide in the external service specification.

```sh
NAME                                  TYPE         CLUSTER-IP   EXTERNAL-IP       PORT(S)           AGE
<my-replica-set>-0-0-svc-external   LoadBalancer   10.102.27.116    <lb-ip-or-fqdn>   27017:27017/TCP    8m30s
```

Depending on your cluster configuration or cloud provider, 
the IP address of the LoadBalancer service is an externally 
accessible IP address or FQDN (fully qualified domain name). You can use the IP address or FQDN (fully qualified domain name) 
to route traffic from your external domain. 

**Step 7: Update your replica set resource YAML (Yet Another Markup Language) file.**

Set the hostnames and ports in `spec.connectivity.replicaSetHorizons`
to the external service values that you created in the previous step.

Confirm that you specified the correct external hostnames. External
hostnames should match the DNS (Domain Name System) names of Kubernetes worker nodes.
These can be *any* nodes in the Kubernetes cluster. If the Pod runs on another
node, Kubernetes nodes use internal routing.

```sh
apiVersion: mongodb.com/v1
 kind: MongoDBMultiCluster
 metadata:
  name: multi-cluster-replica-set
  namespace: mongodb
 spec:
  clusterSpecList:
   - clusterName: e2e.cluster1.example.com
     members: 1
   - clusterName: e2e.cluster2.example.com
     members: 1
   - clusterName: e2e.cluster3.example.com
     members: 1
  connectivity:
   replicaSetHorizons:
   - sample-horizon: web1.example.com:30907
   - sample-horizon: web2.example.com:30907
   - sample-horizon: web3.example.com:30907
  credentials: my-credentials
  duplicateServiceObjects: false
  opsManager:
   configMapRef:
    name: my-project
  persistent: true
  security:
   certsSecretPrefix: clustercert
   tls:
     ca: ca-issuer
  type: ReplicaSet
  version: 8.0.0"
```

**Step 8: Apply the updated replica set file.**

In each cluster, run this command to apply the updated replica set file:

```sh
$ Kubectl apply -f <file_name.yaml>
```

**Step 9: Test the connection to the replica set.**

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
