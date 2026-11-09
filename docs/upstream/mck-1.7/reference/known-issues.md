<!-- Converted from reference/known-issues.txt (reStructuredText). Includes are inlined. -->

# Known Issues in the MongoDB Controllers for Kubernetes Operator

## Underprovisioned EBS Volume Causes Long IOPS Wait Times

If you used [kops](https://kops.sigs.k8s.io/) to provision a Kubernetes cluster in AWS (Amazon Web Services) and
are experiencing poor performance and high IOPS (Input/Output Operations per Second) wait times, your Elastic Block Store
(EBS) volume may be underprovisioned. 

To improve performance, increase the storage-to-IOPS ratio for your EBS volume. For
example, if your database is 500 GB, increase IOPS to 1500, a 3:1 ratio per GB. To learn 
more about increasing IOPS, see the
`AWS documentation`.

## ConfigMap Name `mongodb-kubernetes-operator-member-list` is Hard-Coded

When you run the `kubectl mongodb` plugin, such as during the
multi-Kubernetes-cluster quick start procedure,
the plugin creates a default ConfigMap named `mongodb-kubernetes-operator-member-list`.
This ConfigMap contains all the members of the multi-Kubernetes cluster MongoDB deployment. You can't change
the ConfigMap's name. To learn more about plugin's flags and actions,
see kubectl-plugin-ref.

## `mongos` Instances Fail to Reach Ready State After Disabling Authentication

**Note:**

This issue applies only to sharded clusters
that meet the following criteria: 

- Deployed using the Kubernetes Operator 1.13.0
- Use X.509 authentication 
- Use `kubernetes.io/tls` secrets for TLS (Transport Layer Security)
  certificates for the MongoDB Agent

If you disable authentication by setting 
`spec.security.auth.enabled` to  `false`, the `mongos` Pods 
never reach a `ready` state.

As a workaround, delete each `mongos` Pod in your deployment. 

Run the following command to list all of your Pods:

```sh
kubectl get pods
```

For each Pod with a name that contains `mongos`, delete it with the
following command:

```sh
kubectl delete pod <podname>
```

When you delete a Pod, Kubernetes recreates it. Each Pod that Kubernetes
recreates receives the updated configuration and can reach a `READY` 
state. To confirm that all of your `mongos` Pods are `READY`, run the
following command:

```sh
kubectl get pods -n <metadata.namespace>
```

A response like the following indicates that all of your `mongos` Pods
are `READY`:

```sh
NAME                                           READY   STATUS    RESTARTS   AGE
mongodb-kubernetes-operator-6495bdd947-ttwqf   1/1     Running   0          50m
my-sharded-cluster-0-0                         1/1     Running   0          12m
my-sharded-cluster-1-0                         1/1     Running   0          12m
my-sharded-cluster-config-0                    1/1     Running   0          12m
my-sharded-cluster-config-1                    1/1     Running   0          12m
my-sharded-cluster-mongos-0                    1/1     Running   0          11m
my-sharded-cluster-mongos-1                    1/1     Running   0          11m
om-0                                           1/1     Running   0          42m
om-db-0                                        2/2     Running   0          44m
om-db-1                                        2/2     Running   0          43m
om-db-2                                        2/2     Running   0          43m
```

## Update Google Firewall Rules to Fix WebHook Issues

When you deploy Kubernetes Operator to [GKE (Google Kubernetes Engine)](https://cloud.google.com/kubernetes-engine) private clusters, the
`MongoDB` resources or MongoDBOpsManager resource creation could time out.
The following message might appear in the logs: ``Error setting state
to reconciling: Timeout: request did not complete within requested
timeout 30s``.

Google configures its firewalls to restrict access to your Kubernetes
[Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/). To use the webhook service,
`add a new firewall rule`
to grant [GKE (Google Kubernetes Engine)](https://cloud.google.com/kubernetes-engine) control plane access to your webhook service.

The Kubernetes Operator webhook service runs on port 443.

## Configure Persistent Storage Correctly

If there are no
`persistent volumes`
available when you create a resource, the resulting [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/) stays in
transient state and the Operator fails  (after 20 retries) with the
following error:

```sh
Failed to update Ops Manager automation config: Some agents failed to register
```

To prevent this error, either:

- Provide [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) or
- Set `persistent : false` for the resource

For testing only, you may also set `persistent : false`. This
*must not be used in production*, as data is not preserved between
restarts.

## Remove Resources before Removing Kubernetes

Sometimes Ops Manager can diverge from Kubernetes. This mostly occurs when
Kubernetes resources are removed manually. Ops Manager can keep displaying an
Automation Agent which has been shut down.

If you want to remove deployments of MongoDB on Kubernetes, use the
resource specification to delete resources first so no dead Automation
Agents remain.

To troubleshoot any issues that might occur, see:

- remove-k8s-resource
- k8s-disable-feature-controls
- k8s-delete-om

## Create Separate Namespaces for Kubernetes Operator and MongoDB Resources

The best strategy is to create Kubernetes Operator and its resources in
different namespaces so that the following operations would work
correctly:

```sh
kubectl delete pods --all
```

or

```sh
kubectl delete namespace mongodb
```

If the Kubernetes Operator and resources sit in the same `mongodb`
[namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/), then operator would also be removed in the same operation.
This would mean that it could not clean the configurations, which
would have to be done in the Ops Manager Application.

## HTTPS Enabled After Deployment

We recommend that you enable HTTPS (Hypertext Transfer Protocol Secure) *before* deploying your Ops Manager resources.
However, if you enable HTTPS (Hypertext Transfer Protocol Secure) after deployment,
your managed resources can no longer communicate with Ops Manager and 
the Kubernetes Operator reports your resources' status as `Failed`.

To resolve this issue, you must delete your [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/) by
running the following command for each Pod:

```sh
kubectl delete pod <replicaset-pod-name>
```

      
After deletion, Kubernetes automatically restarts the deleted Pods. 
During this period, the resource is unreachable and incurs 
downtime.

**See also:**

- config-https
- k8s-troubleshooting

## Unable to Update the MongoDB Agent on Application Database Pods

You can't use Ops Manager to upgrade the MongoDB Agent\'s that run on the
Application Database Pods. The MongoDB Agent version that runs on these
Pods is embedded in the Application Database Docker image.

You can use the Kubernetes Operator to upgrade the MongoDB Agent version on
Application Database Pods as MongoDB publishes new images.

**See also:**

- meko-appdb-agent-version
- registry-appdb-version

## Unable to Pull Enterprise Kubernetes Operator Images from IBM Cloud Paks

If you pull the Kubernetes Operator images from a container registry hosted in 
[IBM Cloud Paks](https://www.ibm.com/cloud/paks), the IBM Cloud Paks
changes the names of the images by adding a digest SHA to the official image 
names. This action results in error messages from the Kubernetes Operator similar 
to the following:

```sh
Failed to apply default image tag "cp.icr.io/cp/cpd/ibm-cpd-mongodb-agent@
sha256:10.14.24.6505-1": couldn't parse image reference "cp.icr.io/cp/cpd/
ibm-cpd-mongodb-agent@sha256:10.14.24.6505-1": invalid reference format
```

As a workaround, update the Ops Manager Application Database resource definition 
in `spec.applicationDatabase.podSpec.``podTemplate` to 
specify the new names for the Kubernetes Operator images that contain the digest SHAs, 
similar to the following example.

```sh
applicationDatabase:
  # The version specified must match the one in the image provided in the `mongod` field
  version: 4.4.11-ubi8
  members: 3
  podSpec:
    podTemplate:
      spec:
        containers:
          - name: mongodb-agent
            image: 'cp.icr.io/cp/cpd/ibm-cpd-mongodb-agent@sha256:689df23cc35a435f5147d9cd8a697474f8451ad67a1e8a8c803d95f12fea0b59'
```

## Machine Memory vs. Container Memory

The Automation Agent in Cloud Manager and Ops Manager reports
host memory (RAM) usage instead of the Kubernetes container memory usage.

## On MacOS, hosts using Docker Desktop OpsManager fail to download database images

If you see errors in OpsManager logs like:

```sh
['desiredState.FullVersion' is not a member of 'currentState.VersionsOnDisk' ('desiredState.FullVersion'={"trueName":"8.0.4","gitVersion":"bc35ab4305d9920d9d0491c1c9ef9b72383d31f9","modules":null,"major":8,"minor":0,"patch":4}, 'currentState.VersionsOnDisk'=[])] (err=<nil>). Outcome=Failure
```

The following combination of Docker Desktop settings may resolve the issue:

- [Enable Apple Virtualization framework](https://github.com/docker/enable-macos-virtualization-framework)
- [Disable "Use Rosetta for x86_64/amd64 emulation on Apple Silicon"](https://docs.docker.com/desktop/settings-and-maintenance/settings/)
- [Enable gRPC FUSE](http://docs.docker.com/desktop/settings-and-maintenance/settings/)
