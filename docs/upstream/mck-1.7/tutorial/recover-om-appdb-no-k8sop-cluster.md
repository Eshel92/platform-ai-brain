<!-- Converted from tutorial/recover-om-appdb-no-k8sop-cluster.txt (reStructuredText). Includes are inlined. -->

# Recover Ops Manager if the Central Cluster Fails

If the Kubernetes cluster hosting the Kubernetes Operator and the Ops Manager Application
fails, you can manually recover the central cluster and the Ops Manager Application.

To restore the previous running state of Ops Manager, configure a periodic backup
mechanism for your Ops Manager and Application Database resources. The
Kubernetes Operator needs these resources to manage the Ops Manager Application deployment.

## Recover the Kubernetes Operator and Ops Manager

To recover the Kubernetes Operator and Ops Manager,
restore the Ops Manager resource on a new Kubernetes cluster:

**Step 1: Configure the Kubernetes Operator in a new cluster.**

Follow the instructions to install the Kubernetes Operator in a new Kubernetes cluster.

**Note:**

If you plan to re-use a member cluster, ensure that the 
appropriate service account and role exist. These values can overlap
and have different permissions between the central cluster and member
cluster.

To see the appropriate role required for the 
Kubernetes Operator, refer to the sample in the public repository.

**Step 2: Retrieve the backed-up resources from the failed Ops Manager resource.**

Copy the [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification for the failed Ops Manager resource and
retrieve the following resources, replacing the placeholder text with 
your specific Ops Manager resource name and namespace.

* - Resource Type
  - Values

* - Secrets
  - - `<om-name>-db-om-password`
    - `<om-name>-db-agent-password`
    - `<om-name>-db-keyfile`
    - `<om-name>-db-om-user-scram-credentials`
    - `<om-namespace>-<om-name>-admin-key`
    - `<om-name>-admin-secret`
    - `<om-name>-gen-key`
    - TLS (Transport Layer Security) certificate secrets (optional)

* - ConfigMaps
  - - `<om-name>-db-cluster-mapping`
    - `<om-name>-db-member-spec`
    - Custom CA for TLS (Transport Layer Security) certificates (optional)

* - OpsManager
  - - `<om-name>`

Then, paste the specification that you copied into a new file and 
configure the new resource by using the preceding values. To 
learn more, see deploy-om-container.

**Step 3: Re-apply the Ops Manager resource to the new cluster.**

Use the following command to apply the updated resource: 

```sh
kubectl apply \
  --context "$MDB_CENTRAL_CLUSTER_FULL_NAME" \
  --namespace "mongodb" 
   -f https://raw.githubusercontent.com/mongodb/mongodb-kubernetes/1.7.0/public/samples/ops-manager/ops-manager-external.yaml
```

To check the status of your Ops Manager resource, use the following command:

```sh
kubectl get om -o yaml -w
```

Once the central cluster reaches a `Running` state, you can 
re-scale the Application Database to your desired 
distribution of member clusters.

At this point, the newly restored Kubernetes Operator should pick up management of
the existing Application Database.

- The ConfigMap used to create the initial project.

- The secrets used in the previous Kubernetes Operator 
  instance.

- The `MongoDB` or `MongoDBMulticluster` [custom resource](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) at its last 
  available state on the source cluster, including any [annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/) 
  added by the Kubernetes Operator during its lifecycle.

**Note:**

If the Application Database replica set has lost some nodes and is
unable to form a voting majority, forcibly reconfigure the replica set.
This adds new replica set nodes that will form a voting majority allowing
the replica set to elect a primary.
