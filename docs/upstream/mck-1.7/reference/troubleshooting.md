<!-- Converted from reference/troubleshooting.txt (reStructuredText). Includes are inlined. -->

# Troubleshoot the Kubernetes Operator

**Important:**

This section is for single Kubernetes cluster deployments only. For
multi-Kubernetes cluster MongoDB deployments, see multi-cluster-troubleshooting.

   

## Get Status of a Deployed Resource

To find the status of a resource deployed with the Kubernetes Operator,
invoke one of the following commands:

- For Ops Manager resource deployments:

  ```sh
  kubectl get <resource-name> -n <metadata.namespace> -o yaml
  ```

  - The `status.applicationDatabase.phase` field displays the
    Application Database resource deployment status.
  - The `status.backup.phase` displays the backup daemon resource
    deployment status.
  - The `status.opsManager.phase` field displays the Ops Manager resource
    deployment status.

  **Note:**

  The Cloud Manager or Ops Manager controller watches the database resources
  defined in the following settings:

  - `spec.backup.opLogStores`
  - `spec.backup.s3Stores`
  - `spec.backup.blockStores`

- For MongoDB resource deployments:

  ```sh
  kubectl get mdb <resource-name> -n <metadata.namespace> -o yaml
  ```

  The `status.phase` field displays the MongoDB resource deployment
  status.

The following key-value pairs describe the resource deployment statuses:

* - Key
  - Value

* - `message`
  - Message explaining why the resource is in a `Pending` or
    `Failed` state.
* - `phase`
  - - `Pending`: The Kubernetes Operator is unable to reconcile the
      resource deployment state. This happens when a
      reconciliation times out or if the Kubernetes Operator requires
      you to take action for the resource to enter a running
      state.

      If a resource is pending because a reconciliation timed
      out, the Kubernetes Operator attempts to reconcile the resource
      state in 10 seconds.

    - `Pending`: The Kubernetes Operator is reconciling the resource
      state.

      Resources enter this state after you create or update them
      or if the Kubernetes Operator is attempting to reconcile a
      resource previously in a `Failed` state.

      The Kubernetes Operator attempts to reconcile the resource state
      in 10 seconds.

    - `Running`: The resource is running properly.

    - `Failed`: The resource is not running properly. The
      `message` field provides additional details.

      The Kubernetes Operator attempts to reconcile the resource state
      in 10 seconds.

* - `lastTransition`
  - Timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601?oldid=793821205) date and time format in UTC (Coordinated Universal Time) when the last reconciliation happened.

* - `link`
  - Deployment URL (Uniform Resource Locator) in `Ops Manager`.

* - `backup.statusName`
  - If you enabled continuous backups with `spec.backup.mode`
    in Kubernetes for your MongoDB resource, this field indicates
    the status of the backup, such as `backup.statusName:"STARTED"`.
    Possible values are `STARTED`, `STOPPED`, and `TERMINATED`.

* - Resource specific fields
  - For descriptions of these fields, see
    k8s-specification.

**Example:**

To see the status of a replica set named `my-replica-set` in
the `developer` namespace, run:

```sh
kubectl get mdb my-replica-set -n developer -o yaml
```

If `my-replica-set` is running, you should see:

```yaml
status:
    lastTransition: "2019-01-30T10:51:40Z"
    link: http://ec2-3-84-128-187.compute-1.amazonaws.com:9080/v2/5c503a8a1b90141cbdc60a77
    members: 1
    phase: Running
    version: 8.0.0
```

If `my-replica-set` is not running, you should see:

```yaml
status:
  lastTransition: 2019-02-01T13:00:24Z
  link: http://ec2-34-204-36-217.compute-1.amazonaws.com:9080/v2/5c51c040d6853d1f50a51678
  members: 1
  message: 'Failed to create/update replica set in Ops Manager: Status: 400 (Bad Request),
    Detail: Something went wrong validating your Automation Config. Sorry!'
  phase: Failed
  version: 8.0.0
```

## Review the Logs

Keep and review adequate logs to help debug issues and monitor cluster 
activity. Use the recommended [logging architecture](https://kubernetes.io/docs/concepts/cluster-administration/logging/) 
to retain [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/) logs even after a Pod is deleted.

### Logging Process

The Kubernetes Operator writes to the Pod logs by using 
a wrapper that converts logs from the MongoDB Agent and `mongod` 
components on the database deployment Pod into a 
structured logging entry in the following JSON (Javascript Object Notation) format:

```json
{ "logType": "<log-type>", "contents": "<log line from a log file>" }
```

The Kubernetes Operator supports the following log types:

- `automation-agent-verbose`
- `automation-agent-stderr`
- `mongodb`
- `mongodb-audit`
- `agent-launcher-script`
- `automation-agent`
- `monitoring-agent`
- `backup-agent`

When you read logs from a database container,
the Kubernetes Operator returns the structured JSON (Javascript Object Notation) entry 
that contains logs from different sources.

### Review Logs from the Kubernetes Operator

To review the Kubernetes Operator logs, invoke this command:

```sh
kubectl logs -f deployment/mongodb-kubernetes-operator -n <metadata.namespace>
```

You could check the `Ops Manager Logs` as
well to see if any issues were reported to Ops Manager.

### Find a Specific Pod

To find which pods are available, invoke this command first:

```sh
kubectl get pods -n <metadata.namespace>
```

**See also:**

Kubernetes documentation on [kubectl get](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get).

### Review Logs from a Specific Pod

If you want to narrow your review to a specific [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/), you can
invoke this command:

```sh
kubectl logs <podName> -n <metadata.namespace>
```

**Example:**

If your replica set is labeled `myrs`, run:

```sh
kubectl logs myrs-0 -n <metadata.namespace>
```

This returns the Automation Agent Log for this
replica set.

### Review a Specific Log

You can narrow your review to a specific log type. For example,
the following command returns audit logs from the Kubernetes logs 
of the specified Pod by specifying the `mongodb-audit` log type:

```sh
kubectl logs -c mongodb-enterprise-database replica-set-0 | jq -r 'select(.logType == "mongodb-audit") | .contents'
```

The command returns an entry similar to the following output:

```json
{{{ "atype":"startup","ts":{"$date":"2023-08-30T20:43:54.649+00:00"},"uuid":{"$binary":"oDcPEY69R1yiUtpMupaXOQ==","$type":"04"},"local":{"isSystemUser":true},"remote":{"isSystemUser":true},"users":[],"roles":[],"param":{"options":{"auditLog":{"destination":"file","format":"JSON","path":"/var/log/mongodb-mms-automation/mongodb-audit.log"},"config":"/data/automation-mongod.conf","net":{"bindIp":"0.0.0.0","port":27017,"tls":{"mode":"disabled"}},"processManagement":{"fork":true},"replication":{"replSetName":"replica-set"},"storage":{"dbPath":"/data","engine":"wiredTiger"},"systemLog":{"destination":"file","path":"/var/log/mongodb-mms-automation/mongodb.log"}}},"result":0}
{"atype":"startup","ts":{"$date":"2023-08-30T20:44:05.466+00:00"},"uuid":{"$binary":"OUbUWC1DQM6k/Ih4hKZq4g==","$type":"04"},"local":{"isSystemUser":true},"remote":{"isSystemUser":true},"users":[],"roles":[],"param":{"options":{"auditLog":{"destination":"file","format":"JSON","path":"/var/log/mongodb-mms-automation/mongodb-audit.log"},"config":"/data/automation-mongod.conf","net":{"bindIp":"0.0.0.0","port":27017,"tls":{"mode":"disabled"}},"processManagement":{"fork":true},"replication":{"replSetName":"replica-set"},"storage":{"dbPath":"/data","engine":"wiredTiger"},"systemLog":{"destination":"file","path":"/var/log/mongodb-mms-automation/mongodb.log"}}},"result":0}}}
```

### Audit Logs

To include audit logs in the Kubernetes Pod's logs,
add the following `additionalMongodConfig.auditLog` configuration 
to your resource definition. You can update the provided file name as needed. 

```yaml
spec:
   additionalMongodConfig:
      auditLog:
         destination: file
            format: JSON
            path: /var/log/mongodb-mms-automation/mongodb-audit.log
```

## Check Messages from the Validation Webhook

The Kubernetes Operator uses a validation [Webhook](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#what-are-admission-webhooks) to prevent users
from applying invalid resource definitions. The webhook rejects invalid
requests.

The [ClusterRole](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#role-and-clusterrole) and [ClusterRoleBinding](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#rolebinding-and-clusterrolebinding) for the webhook are included in the default
configuration files that you apply during the installation. To create
the role and binding, you must have `cluster-admin privileges`.

If you create an invalid resource definition, the webhook returns
a message similar to the following that describes the error to the shell:

```sh
error when creating "my-ops-manager.yaml":
admission webhook "ompolicy.mongodb.com" denied the request:
shardPodSpec field is not configurable for application databases as
it is for sharded clusters and appdb replica sets
```

When the Kubernetes Operator reconciles each resource, it also validates that
resource. The Kubernetes Operator doesn't require the validation webhook to
create or update resources.

If you omit the validation webhook, or if you remove the webhook's role
and binding from the default configuration, or have insufficient
privileges to run the configuration, the Kubernetes Operator issues warnings,
as these are not critical errors. If the Kubernetes Operator encounters a
critical error, it marks the resource as `Failed`.

**Note:** [GKE (Google Kubernetes Engine)](https://cloud.google.com/kubernetes-engine) deployments

[GKE (Google Kubernetes Engine)](https://cloud.google.com/kubernetes-engine) has a known issue with the webhook when deploying to private
clusters. To learn more, see k8s-private-cluster-on-gke.

## View All `MongoDB` resource Specifications

To view all `MongoDB` resource specifications in the provided
[namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/):

```shell
kubectl get mdb -n <metadata.namespace>
```

**Example:**

To read details about the `dublin` standalone resource, run
this command:

```shell
kubectl get mdb dublin -n <metadata.namespace> -o yaml
```

This returns the following response:

```yaml
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"mongodb.com/v1","kind":"MongoDB","metadata":{"annotations":{},"name":"dublin","namespace":"mongodb"},"spec":{"credentials":"credentials","persistent":false,"podSpec":{"memory":"1Gi"},"project":"my-om-config","type":"Standalone","version":"4.0.0"}}
  clusterDomain: ""
  creationTimestamp: 2018-09-12T17:15:32Z
  generation: 1
  name: dublin
  namespace: mongodb
  resourceVersion: "337269"
  selfLink: /apis/mongodb.com/v1/namespaces/mongodb/mongodbstandalones/dublin
  uid: 7442095b-b6af-11e8-87df-0800271b001d
spec:
  credentials: my-credentials
  type: Standalone
  persistent: false
  project: my-om-config
  version: 8.0.0
```

## Restore StatefulSet that Failed to Deploy

A StatefulSet [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/) may hang with a status of `Pending` if it
encounters an error during deployment.

`Pending` [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/) do not automatically terminate, even if you
make *and apply* configuration changes to resolve the error.

To return the StatefulSet to a healthy state, apply the configuration
changes to the MongoDB resource in the `Pending` state, then delete
those pods.

**Example:**

A host system has a number of running [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/):

```sh
kubectl get pods

my-replica-set-0     1/1 Running 2 2h
my-replica-set-1     1/1 Running 2 2h
my-replica-set-2     0/1 Pending 0 2h
```

`my-replica-set-2` is stuck in the `Pending` stage. To gather
more data on the error, run:

```sh
kubectl describe pod my-replica-set-2

<describe output omitted>

Warning FailedScheduling 15s (x3691 over 3h) default-scheduler
0/3 nodes are available: 1 node(s) had taints that the pod
didn't tolerate, 2 Insufficient memory.
```

The output indicates an error in memory allocation.

Updating the memory allocations in the MongoDB resource is
insufficient, as the pod does not terminate automatically after
applying configuration updates.

To remedy this issue, update the configuration, apply the
configuration, then delete the hung pod:

```sh
vi <my-replica-set>.yaml

kubectl apply -f <my-replica-set>.yaml

kubectl delete pod my-replica-set-2
```

Once this hung pod is deleted, the other pods restart with your new
configuration as part of rolling upgrade of the Statefulset.

**Note:**

To learn more about this issue, see
[Kubernetes Issue 67250](https://github.com/kubernetes/kubernetes/issues/67250).

## Replace a ConfigMap to Reflect Changes

If you cannot modify or redeploy an already-deployed resource
`ConfigMap` file using the *kubectl apply* command, run:

```shell
kubectl replace -f <my-config-map>.yaml
```

This deletes and re-creates the `ConfigMap` resource file.

Use this command when you want to make an immediate
recursive change, or when you need to update resource files that cannot
be updated once initialized.

## Remove Kubernetes Components

**Important:**

To remove any component, you need the following permissions:

* - `Cluster Roles`
  -
    - `mongodb-kubernetes-operator-mongodb-webhook`
    - `mongodb-kubernetes-operator-mongodb-certs`

* - `Cluster Role Bindings`
  -
    - `mongodb-kubernetes-operator-mongodb-webhook-binding`
    - `mongodb-kubernetes-operator-mongodb-certs`

### Remove a `MongoDB` resource

To remove any instance that Kubernetes deployed, you must use Kubernetes.

**Important:**

- You can use only the Kubernetes Operator to remove Kubernetes\-deployed
  instances. If you use `Ops Manager` to remove the instance, `Ops Manager` throws an
  error.

- Deleting a MongoDB resource doesn't remove it from the Ops Manager UI. 
  You must remove the resource from Ops Manager manually. To learn more, see 
  `Remove a Process from Monitoring`.

- Deleting a MongoDB resource for which you enabled backup doesn't
  delete the resource's snapshots. You must `delete snapshots 
  in Ops Manager`.

**Example:**

To remove a single MongoDB instance you created using Kubernetes:

```shell
kubectl delete mdb <name> -n <metadata.namespace>
```

To remove all MongoDB instances you created using Kubernetes:

```shell
kubectl delete mdb --all -n <metadata.namespace>
```

### Remove the Kubernetes Operator

To remove the Kubernetes Operator:

1. Remove all Kubernetes resources:

   ```shell
   kubectl delete mdb --all -n <metadata.namespace>
   ```

2. Remove the Kubernetes Operator:

   ```shell
   kubectl delete deployment mongodb-kubernetes-operator -n <metadata.namespace>
   ```

### Remove the [CustomResourceDefinitions](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/)

To remove the [CustomResourceDefinitions](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/):

1. Remove all Kubernetes resources:

   ```shell
   kubectl delete mdb --all -n <metadata.namespace>
   ```

2. Remove the [CustomResourceDefinitions](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/):

   ```shell
   kubectl delete crd mongodb.mongodb.com
   kubectl delete crd mongodbusers.mongodb.com
   kubectl delete crd opsmanagers.mongodb.com
   ```

### Remove the [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)

To remove the [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/):

1. Remove all Kubernetes resources:

   ```shell
   kubectl delete mdb --all -n <metadata.namespace>
   ```

2. Remove the [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/):

   ```shell
   kubectl delete namespace <metadata.namespace>
   ```

## Create a New [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) after Deleting a Pod

If you accidentally delete the MongoDB replica set Pod and its [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims),
the Kubernetes Operator fails to reschedule the MongoDB Pod and issues
the following error message:

```sh
scheduler error: pvc not found to schedule the pod
```

To recover from this error, you must `manually create a new PVC`
with the PVC object's name that corresponds to this replica set Pod,
such as `data-<replicaset-pod-name>`.

## Disable Ops Manager Feature Controls

When you manage an Ops Manager project through the Kubernetes Operator, the
Kubernetes Operator places the `EXTERNALLY_MANAGED_LOCK`
`feature control policy`
on the project. This policy disables certain features in the Ops Manager
application that might compromise your Kubernetes Operator configuration. If
you need to use these blocked features, you can remove the policy
through the `feature controls API`,
make changes in the Ops Manager application, and then restore the original
policy through the `API`.

**Warning:**

The following procedure enables you to use features in the Ops Manager
application that are otherwise blocked by the Kubernetes Operator.

1. `Retrieve the feature control policies`
   for your Ops Manager project.

   ```sh
   curl --user "{USERNAME}:{APIKEY}" --digest \
        --header "Accept: application/json" \
        --header "Content-Type: application/json" \
        --include \
        --request GET "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/controlledFeature?pretty=true"
   ```

   Save the response that the API returns. After you make changes in
   the Ops Manager application, you must add these policies back to
   the project.

   **Important:**

   Note the highlighted fields and values in the following sample
   response. You must send these same fields and values in later
   steps when you remove and add feature control policies.

   The `externalManagementSystem.version` field corresponds to the 
   Kubernetes Operator version. You must send the exact same field value
   in your requests later in this task.

   Your response resembles the following:
 

   ```json
   {
    "created": "2020-02-25T04:09:42Z",
    "externalManagementSystem": {
      "name": "mongodb-kubernetes-operator",
      "systemId": null,
      "version": "1.4.2"
    },
    "policies": [
      {
        "disabledParams": [],
        "policy": "EXTERNALLY_MANAGED_LOCK"
      },
      {
        "disabledParams": [],
        "policy": "DISABLE_AUTHENTICATION_MECHANISMS"
      }
    ],
    "updated": "2020-02-25T04:10:12Z"
   }
   ```

#. `Update`
   the `policies` array with an empty list:

   **Note:**

   The values you provide for the `externalManagementSystem`
   object, like the `externalManagementSystem.version` field, must
   match values that you received in the response in Step 1.

   ```sh
   curl --user "{USERNAME}:{APIKEY}" --digest \
        --header "Accept: application/json" \
        --header "Content-Type: application/json" \
        --include \
        --request PUT "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/controlledFeature?pretty=true" \
        --data '{
            "externalManagementSystem": {
              "name": "mongodb-kubernetes-operator",
              "systemId": null,
              "version": "1.4.2"
            },
            "policies": []
          }'
   ```

   The previously blocked features are now available in the
   Ops Manager application.

#. Make your changes in the Ops Manager application.

#. `Update`
   the `policies` array with the original feature control policies:

   **Note:**

   The values you provide for the `externalManagementSystem`
   object, like the `externalManagementSystem.version` field, must
   match values that you received in the response in Step 1.

   ```sh
   curl --user "{USERNAME}:{APIKEY}" --digest \
        --header "Accept: application/json" \
        --header "Content-Type: application/json" \
        --include \
        --request PUT "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/controlledFeature?pretty=true" \
        --data '{
            "externalManagementSystem": {
              "name": "mongodb-kubernetes-operator",
              "systemId": null,
              "version": "1.4.2"
            },
            "policies": [
              {
                "disabledParams": [],
                "policy": "EXTERNALLY_MANAGED_LOCK"
              },
              {
                "disabledParams": [],
                "policy": "DISABLE_AUTHENTICATION_MECHANISMS"
              }
            ]
          }'
   ```

   The features are now blocked again, preventing you from making
   further changes through the Ops Manager application. However, the
   Kubernetes Operator retains any changes you made in the Ops Manager
   application while features were available.

## Remove Resources when the Kubernetes Operator Fails

When you delete a MongoDB custom resource through the Kubernetes Operator, the
Kubernetes Operator handles the removal of the deployment in Cloud Manager or Ops Manager.
To learn more, see remove-k8s-resource.

However, the removal of resources might fail
in Kubernetes. For example, if the Kubernetes Operator fails before you delete the MongoDB
resource, you must manually remove the deployments and delete their projects in
Cloud Manager or Ops Manager.

To remove Ops Manager or Cloud Manager resources manually:

1. Disable Ops Manager feature controls.

#. Remove a deployment from Ops Manager or Cloud Manager in the project by using the UI
   or the API.

   Remove a deployment in the Ops Manager or Cloud Manager UI.
   In Ops Manager, `remove a deployment from Automation`
   and `remove a deployment from Monitoring`.

   In Cloud Manager, `remove a deployment from Automation`
   and `remove a deployment from Monitoring`.

   Alternatively, remove a deployment by using the API for updating the Automation
   configuration in Ops Manager or Cloud Manager with an empty configuration using
   the `Ops Manager API` request,
   or the `Cloud Manager API` request.

   Run the command similar to the following Ops Manager example:

   ```sh
   curl --user "{USERNAME}:{APIKEY}" --digest \
        --header "Content-Type: application/json" \
        --include \
        --request PUT "https://{OPSMANAGER-HOST}/api/public/v1.0/groups/{PROJECT-ID}/automationConfig" \
        --data '{}'
   ```

   **Note:**

   Deleting a MongoDB resource for which you enabled backup doesn't
   delete the resource's snapshots. You must `delete snapshots 
   in Ops Manager`, or `delete snapshots 
   in Cloud Manager`.

#. Delete a project from Ops Manager or Cloud Manager by using the UI or the API.
   `Delete a project in Ops Manager`, or
   `delete a project in the Cloud Manager`.

   Alternatively, delete a project by using the `Ops Manager API` request,
   or the `Cloud Manager API` request.

   Run the command similar to the following Ops Manager example:

   ```sh
   curl --user "{USERNAME}:{APIKEY}" --digest \
        --request DELETE "{OPSMANAGER-HOST}/api/public/v1.0/groups/${PROJECT-ID}"
   ```

## Debug a Failing Container

A container might fail with an error that results in Kubernetes restarting
that container in a loop.

You may need to interact with that container to inspect files or run
commands. This requires you to prevent the container from restarting.

1. In your preferred text editor, open the MongoDB resource you need to
   repair.

#. To this resource, add a `podSpec` collection that resembles the
   following.

   ```yaml
   podSpec:
     podTemplate:
       spec:
         containers:
         - name: mongodb-enterprise-database
           command: ['sh', '-c', 'echo "Hello!" && sleep 3600' ]
   ```

   The sleep command in the
   `spec.podSpec.podTemplate.spec` instructs the container to
   wait for the number of seconds you specify. In this example, the
   container waits for 1 hour.

#. Apply this change to the resource.

   ```sh
   kubectl apply -f <resource>.yaml
   ```

#. Invoke the shell inside the container.

   ```sh
   kubectl exec -it <pod-name> bash
   ```

## Verify Correctness of Domain Names in TLS Certificates

A MongoDB replica set or sharded cluster may fail to reach
the `READY` state if the TLS (Transport Layer Security) certificate is invalid.

When you configure TLS for MongoDB replica sets or sharded clusters, verify
that you specify a valid certificate.

If you don't specify the correct Domain Name for each TLS (Transport Layer Security) certificate,
the Kubernetes Operator logs may contain an error
message similar to the following, where `foo.svc.local` is the
incorrectly-specified Domain Name for the cluster member's Pod:

```sh
TLS attempt failed : x509: certificate is valid for foo.svc.local,
not mongo-0-0.mongo-0.mongodb.svc.cluster.local
```

Each certificate should include a valid Domain Name.

For each replica set or sharded cluster member, the Common Name, also
known as the Domain Name, for that member's certificate must match
the FQDN (fully qualified domain name) of the pod this cluster member is deployed on.

The FQDN (fully qualified domain name) name in each certificate has the following syntax:
`pod-name.service-name.namespace.svc.cluster.local`. This name is
different for each Pod hosting a member of the replica set or a
sharded cluster.

For example, for a member of a replica set deployed on a Pod with
the name `rs-mongos-0-0`, in the Kubernetes Operator service
named `mongo-0` that is created in the default `mongodb`
namespace, the FQDN (fully qualified domain name) is:

```sh
rs-mongos-0-0.mongo-0.mongodb.svc.cluster.local
```

To check whether you have correctly configured TLS (Transport Layer Security) certificates:

1. Run:

   ```sh
   kubectl logs -f <pod_name>
   ```

2. Check for TLS (Transport Layer Security)-related messages in the Kubernetes Operator log files.

To learn more about TLS (Transport Layer Security) certificate requirements, see the
prerequisites on the TLS-Encrypted Connections tab in
deploy-replica-set or in deploy-sharded-cluster.

## Verify the MongoDB Version when Running in Local Mode

MongoDB `CustomResource` may fail to reach a `Running` state
if Ops Manager is running in Local Mode and you specify either a version of MongoDB
that doesn't exist, or a valid version of MongoDB for which
Ops Manager deployed in local mode did not download a corresponding MongoDB archive.

If you specify a MongoDB version that doesn't exist, or a valid MongoDB
version for which Ops Manager could not download a MongoDB archive, then
even though the Pods can reach the `READY` state,
the Kubernetes Operator logs contain an
error message similar to the following:

```sh
Failed to create/update (Ops Manager reconciliation phase):
Status: 400 (Bad Request), Detail:
Invalid config: MongoDB <version> is not available.
```

This may mean that the MongoDB Agent could not successfully download a
corresponding MongoDB binary to the `/var/lib/mongodb-mms-automation`
directory. In cases when the MongoDB Agent can download the MongoDB
binary for the specified MongoDB version successfully, this directory
contains a MongoDB binary folder, such as `mongodb-linux-x86_64-8.0.0`.

To check whether a MongoDB binary folder is present:

1. Specify the Pod's name to this command:

   ```sh
   kubectl exec --stdin --tty $<pod_name> /bin/sh
   ```

2. Check whether a MongoDB binary folder is present in the
   `/var/lib/mongodb-mms-automation` directory.

3. If you cannot locate a MongoDB binary folder,
   copy the MongoDB archive
   into the Ops Manager Persistent Volume for each deployed Ops Manager replica set.

## Upgrade Fails Using `kubectl` or `oc`

You might receive the following error when you upgrade the
Kubernetes Operator:

```sh
Forbidden: updates to statefulset spec for fields other than
'replicas', 'template', and 'updateStrategy' are forbidden
```

To resolve this error:

a. Remove the old Kubernetes Operator deployment.

   ```sh
   kubectl delete deployment/mongodb-kubernetes-operator -n <metadata.namespace>
   ```

   **Note:**

   Removing the Kubernetes Operator deployment doesn’t affect the lifecycle
   of your MongoDB resources.

b. Repeat the `kubectl apply` command to upgrade to the new 
   version of the Kubernetes Operator.

## Upgrade Fails Using Helm Charts

You might receive the following error when you upgrade the
Kubernetes Operator:

```sh
Error: UPGRADE FAILED: cannot patch "mongodb-kubernetes-operator"
with kind Deployment: Deployment.apps "mongodb-kubernetes-operator"
is invalid: ... field is immutable
```

To resolve this error:

a. Remove the old Kubernetes Operator deployment.

   ```sh
   kubectl delete deployment/mongodb-kubernetes-operator -n <metadata.namespace>
   ```

   **Note:**

   Removing the Kubernetes Operator deployment doesn’t affect the lifecycle
   of your MongoDB resources.

b. Repeat the `helm` command to upgrade to the new version of the
   Kubernetes Operator.

## Recover Resource Due to Broken Automation Configuration

If a custom resource remains in a `Pending` or `Failed` state
for a longer period of time, Kubernetes Operator automatically recovers 
your `MongoDB` resources by pushing the `automation configuration` to Ops Manager. This prevents a deadlock 
when the MongoDB Agent can't push an updated automation configuration change 
because the StatefulSet is stuck in a `Pending` state due to a previous 
push of an invalid automation configuration.

To configure automatic recovery, define the following environmental variables
in your mongodb-kubernetes.yaml
file:

- MDB_AUTOMATIC_RECOVERY_ENABLE
  to enable or disable automatic recovery for `MongoDB` resources per Pod. 

- MDB_AUTOMATIC_RECOVERY_BACKOFF_TIME_S 
  to set the number of seconds that a custom resource can remain in a `Pending` or 
  `Failed` state before the Kubernetes Operator automatically recovers your 
  `MongoDB` resources.

**Example:**

```yaml
spec:
  template:
     spec:
        serviceAccountName: mongodb-kubernetes-operator
        containers:
          - name: mongodb-kubernetes-operator
            image: <operatorVersionUrl>
            imagePullPolicy: <policyChoice>
            env:
             - name: MDB_AUTOMATIC_RECOVERY_ENABLE
               value: true
             - name: MDB_AUTOMATIC_RECOVERY_BACKOFF_TIME_S
               value: 1200
```

To learn how to define environment variables, see 
`Define Environment Variables for a Container`.

## Handle Ops Manager Agent API Key Updates

If the MongoDB `Agent API key` is
deleted or updated from the Ops Manager dashboard, the agents deployed with your MongoDB
resources can no longer authenticate to Ops Manager. As a result, Ops Manager might report the
replica set as down. Use the following procedure to manually ensure agents restart with
the updated API key:

**Step 1: Delete the project secret**

Delete the secret named `<project-id>-group-secret` in your MongoDB
deployment namespace.

**Step 2: Recreate the secret**

Wait for the secret to automatically recreate or create it manually with
the following command:

```sh
kubectl create secret generic <project-id>-group-secret \
   --from-literal=agentApiKey=<new-agent-key> \
   -n <mongodb-namespace>
```

**Step 3: Verify the secret**

Verify that the new `<project-id>-group-secret` exists and has the
correct data.

**Step 4: Restart the MongoDB Pods**

Restart the MongoDB StatefulSet Pods to ensure agents start with the
updated API key:

```sh
kubectl rollout restart statefulset <mongodb-sts> -n <mongodb-namespace>
```

**Step 5: Confirm health in Ops Manager**

Verify that Ops Manager reports the health of replica set members correctly.
