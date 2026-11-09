<!-- Converted from multi-cluster-prerequisites.txt (reStructuredText). Includes are inlined. -->

# Multi-Cluster Deployment Prerequisites

Before you create a multi-Kubernetes cluster MongoDB deployment using either the quick start or a
deployment procedure, complete the following tasks.

To learn more about prerequisites specific to the quick start, see 
Quick Start Prerequisites.

## Review Supported Hardware Architectures

See supported hardware architectures.

## Clone the MongoDB Controllers for Kubernetes Operator Repository

Clone the MongoDB Controllers for Kubernetes Operator repository
and check out the tag for the current release:

```sh
git clone https://github.com/mongodb/mongodb-kubernetes.git
cd mongodb-kubernetes
git checkout 1.7.0
```

## Set Environment Variables

Set the environment variables with cluster names
where you deploy the clusters, as in this example:

```sh
export MDB_CENTRAL_CLUSTER_FULL_NAME="mdb-central"
export MDB_CLUSTER_1_FULL_NAME="mdb-1"
export MDB_CLUSTER_2_FULL_NAME="mdb-2"
export MDB_CLUSTER_3_FULL_NAME="mdb-3"
```

## Install Go and Helm

Install the following tools:

1. Install [Go](https://golang.org/dl/) v1.17 or later.

2. Install [Helm](https://helm.sh/).

## Understand Kubernetes Roles and Role Bindings

To use a multi-Kubernetes cluster MongoDB deployment, you must have a specific set of 
Kubernetes `Roles, ClusterRoles`, 
`RoleBindings, ClusterRoleBindings`, 
and `ServiceAccounts`, which you can configure in any of the following ways:

- Follow the multi-cluster-quick-start-ref, which tells you how to use the
  MongoDB Plugin to automatically create the required objects
  and apply them to the appropriate clusters within your multi-Kubernetes cluster MongoDB deployment.

- Use [Helm](https://helm.sh/) to configure the required Kubernetes Roles and service accounts
  for each member cluster:

  ```sh
  helm template --show-only \
    templates/database-roles.yaml \
    mongodb/mongodb-kubernetes \
    --set namespace=mongodb | \
  kubectl apply -f - \
    --context=$MDB_CLUSTER_1_FULL_NAME \
    --namespace mongodb
  ```

  ```sh
  helm template --show-only \
    templates/database-roles.yaml \
    mongodb/mongodb-kubernetes \
    --set namespace=mongodb | \
  kubectl apply -f - \
    --context=$MDB_CLUSTER_2_FULL_NAME \
    --namespace mongodb
  ```

  ```sh
  helm template --show-only \
    templates/database-roles.yaml \
    mongodb/mongodb-kubernetes \
    --set namespace=mongodb | \
  kubectl apply -f - \
    --context=$MDB_CLUSTER_3_FULL_NAME \
    --namespace mongodb 
  ```

- Manually create Kubernetes object `.yaml` files and add the required Kubernetes Roles and
  service accounts to your multi-Kubernetes cluster MongoDB deployment with the `kubectl apply` command. This may be
  necessary for certain highly automated workflows. MongoDB provides sample configuration files.

  For custom resources scoped to a subset of namespaces:

  - [Roles, Role Bindings, and Service Accounts for your Central Cluster](https://raw.githubusercontent.com/mongodb/mongodb-kubernetes/1.7.0/public/samples/multi-cluster-cli-gitops/resources/rbac/namespace_scoped_central_cluster.yaml)

  - [Roles, Role Bindings, and Service Accounts for your Member Clusters](https://raw.githubusercontent.com/mongodb/mongodb-kubernetes/1.7.0/public/samples/multi-cluster-cli-gitops/resources/rbac/namespace_scoped_member_cluster.yaml)

  For custom resources scoped to a cluster-wide namespace:

  - [ClusterRoles, ClusterRoleBindings, and ServiceAccounts for your Central Cluster](https://raw.githubusercontent.com/mongodb/mongodb-kubernetes/1.7.0/public/samples/multi-cluster-cli-gitops/resources/rbac/cluster_scoped_central_cluster.yaml)

  - [ClusterRoles, ClusterRoleBindings, and ServiceAccounts for your Member Cluster](https://raw.githubusercontent.com/mongodb/mongodb-kubernetes/1.7.0/public/samples/multi-cluster-cli-gitops/resources/rbac/cluster_scoped_member_cluster.yaml)

  Each file defines multiple resources. To support your deployment, you
  must replace the placeholder values in the following fields:

  - `subjects.namespace` in each `RoleBinding` or `ClusterRoleBinding` resource

  - `metadata.namespace` in each `ServiceAccount` resource

  After modifying the definitions, apply them by running the following 
  command for each file:

  ```sh
  kubectl apply -f <fileName>
  ```

## Set the Deployment's Scope

By default, the multi-cluster Kubernetes Operator is scoped to the [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)
in which you install it. The Kubernetes Operator reconciles the `MongoDBMultiCluster` resource
deployed in the same namespace as the Kubernetes Operator.

When you run the MongoDB kubectl plugin
as part of the multi-cluster quick start, and don't modify the `kubectl mongodb` plugin
settings, the plugin:

- Creates a default ConfigMap named `mongodb-kubernetes-operator-member-list`
  that contains all the member clusters of the multi-Kubernetes cluster MongoDB deployment. This name is
  hard-coded and you can't change it. See Known Issues.
- Creates `ServiceAccounts`,
  `Roles, ClusterRoles`,
  `RoleBindings and ClusterRoleBindings`
  in the central cluster and
  each member cluster.
- Applies the correct permissions for service accounts.
- Uses the preceding settings to create your multi-Kubernetes cluster MongoDB deployment.

Once the Kubernetes Operator creates the multi-Kubernetes cluster MongoDB deployment, the Kubernetes Operator
starts watching `MongoDB` resources in the `mongodb` [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/).

To configure the Kubernetes Operator with the correct permissions to deploy
in a subset or all namespaces, run the following command and specify the
namespaces that you would like the Kubernetes Operator to watch.

```sh
kubectl mongodb multicluster setup \
  --central-cluster="${MDB_CENTRAL_CLUSTER_FULL_NAME}" \
  --member-clusters="${MDB_CLUSTER_1_FULL_NAME},${MDB_CLUSTER_2_FULL_NAME},${MDB_CLUSTER_3_FULL_NAME}" \
  --member-cluster-namespace="mongodb2" \
  --central-cluster-namespace="mongodb2" \
  --create-service-account-secrets \
  --cluster-scoped="true"
```

When you install the multi-Kubernetes cluster MongoDB deployment to multiple or all [namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/), you
can configure the Kubernetes Operator to:

- Watch Resources in Multiple Namespaces
- Watch Resources in All Namespaces

**Note:**

Install and set up a single Kubernetes Operator instance and configure it
to watch one, many, or all custom resources in different, non-overlapping
subsets of namespaces. See also faq-many-operators

### Watch Resources in Multiple Namespaces

If you set the scope for the multi-Kubernetes cluster MongoDB deployment to many [namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/), you can
configure the Kubernetes Operator to watch `MongoDB` resources in these namespaces
in the multi-Kubernetes cluster MongoDB deployment.

**mc-kubectl:**

Set the `spec.template.spec.containers.name.env.name:WATCH_NAMESPACE`
in the mongodb-kubernetes.yaml
file from the MongoDB Controllers for Kubernetes Operator GitHub Repository to the comma-separated list
of namespaces that you would like the Kubernetes Operator to watch:

```sh
WATCH_NAMESPACE: "$namespace1,$namespace2,$namespace3"
```

**mc-with-helm:**

Run the following command and replace the values in the last line
with the namespaces that you would like the Kubernetes Operator to
watch.

```sh
helm upgrade \
  --install \
  mongodb-kubernetes-operator-multi-cluster \
  mongodb/mongodb-kubernetes \
  --namespace mongodb \
  --set namespace=mongodb \
  --version <mongodb-kubernetes-operator-version>\
  --set operator.name=mongodb-kubernetes-operator-multi-cluster \
  --set operator.createOperatorServiceAccount=false \
  --set operator.createResourcesServiceAccountsAndRoles=false \
  --set "multiCluster.clusters={$MDB_CLUSTER_1_FULL_NAME,$MDB_CLUSTER_2_FULL_NAME,$MDB_CLUSTER_3_FULL_NAME}" \
  --set operator.watchNamespace="$namespace1,$namespace2,$namespace3"
```

### Watch Resources in All Namespaces

If you set the scope for the multi-Kubernetes cluster MongoDB deployment to all [namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) instead 
of the default `mongodb` namespace, you can configure the Kubernetes Operator
to watch `MongoDB` resources in all namespaces in the multi-Kubernetes cluster MongoDB deployment.

**mc-kubectl:**

Set the `spec.template.spec.containers.name.env.name:WATCH_NAMESPACE`
in mongodb-kubernetes.yaml
to `"*"`. You must include the double quotation marks (`"`)
around the asterisk (`*`) in the YAML file.

```sh
WATCH_NAMESPACE: "*"
```

**mc-with-helm:**

Run the following command:

```sh
helm upgrade \
  --install \
  mongodb-kubernetes-operator-multi-cluster \
  mongodb/mongodb-kubernetes \
  --namespace mongodb \
  --set namespace=mongodb \
  --version <mongodb-kubernetes-operator-version>\
  --set operator.name=mongodb-kubernetes-operator-multi-cluster \
  --set operator.createOperatorServiceAccount=false \
  --set operator.createResourcesServiceAccountsAndRoles=false \
  --set "multiCluster.clusters={$MDB_CLUSTER_1_FULL_NAME,$MDB_CLUSTER_2_FULL_NAME,$MDB_CLUSTER_3_FULL_NAME}" \
  --set operator.watchNamespace="*"
```

## Plan for External Connectivity: Should You Use a Service Mesh?

A service mesh enables inter-cluster communication between the replica set
members deployed in different Kubernetes clusters. Using a service mesh greatly
simplifies creating multi-Kubernetes cluster MongoDB deployments and is the recommended way of deploying
MongoDB across multiple Kubernetes clusters. However, if your IT organization doesn't
use a service mesh, you can deploy a replica set in a multi-Kubernetes cluster MongoDB deployment without it.

Depending on your environment, do the following:

- If you can use a service mesh, install Istio.
- If you can't use a service mesh:

  1. Review the section external_connectivity_how
  2. Enable external connectivity through external domains and DNS zones.
  3. Deploy a multi-Kubernetes cluster without a service mesh.

### How Does the Kubernetes Operator Establish Connectivity?

Regardless of the deployment type, a MongoDB deployment in Kubernetes must
establish the following connections:

- From the Ops Manager MongoDB Agent in the Pod to its `mongod` process,
  to enable MongoDB deployment's lifecycle management and monitoring.
- From the Ops Manager MongoDB  Agent in the Pod to the Ops Manager instance,
  to enable automation.
- Between all `mongod` processes, to allow replication.

When the Kubernetes Operator deploys the MongoDB resources, it treats these
connectivity requirements in the following ways, depending on the type of deployment:

- In a single Kubernetes cluster deployment, the Kubernetes Operator configures hostnames
  in the replica set as FQDN (fully qualified domain name)\s of a [Headless Service](https://kubernetes.io/docs/concepts/services-networking/service/#headless-services). This is a single
  service that resolves the DNS (Domain Name System) of a direct IP address of each Pod hosting
  a MongoDB instance by the Pod's FQDN (fully qualified domain name), as follows:
  `<pod-name>.<replica-set-name>-svc.<namespace>.svc.cluster.local`.

- In a multi-Kubernetes cluster MongoDB deployment that uses a service mesh, the Kubernetes Operator creates
  a separate StatefulSet for each MongoDB replica set member in the Kubernetes
  cluster. A service mesh allows communication between `mongod` processes
  across distinct Kubernetes clusters.

  Using a service mesh allows the multi-Kubernetes cluster MongoDB deployment to:

  - Achieve global DNS (Domain Name System) hostname resolution across Kubernetes clusters and
    establish connectivity between them. For each MongoDB deployment Pod
    in each Kubernetes cluster, the Kubernetes Operator creates a ClusterIP service
    through the `spec.duplicateServiceObjects: true` configuration in
    the `MongoDBMultiCluster` resource. Each process has a hostname defined to this
    service's FQDN (fully qualified domain name): `<pod-name>-svc.<namespace>.svc.cluster.local`.
    These hostnames resolve from DNS to a service's ClusterIP in each member cluster.

  - Establish communication between Pods in different Kubernetes clusters.
    As a result, replica set members hosted on different clusters form a
    single replica set across these clusters.

- In a multi-Kubernetes cluster MongoDB deployment without a service mesh, the Kubernetes Operator uses the
  following `MongoDBMultiCluster` resource settings to expose all its `mongod` processes
  externally. This enables DNS resolution of hostnames between distinct
  Kubernetes clusters, and establishes connectivity between Pods routed through
  the networks that connect these clusters.

  - spec.clusterSpecList.externalAccess.externalService
  - spec.externalAccess
  - spec.clusterSpecList.externalAccess.externalService.annotations
  - spec.clusterSpecList.externalAccess.externalDomain

### Optional: Install Istio

Install [Istio](https://istio.io/) in a [multi-primary mode on different networks](https://istio.io/latest/docs/setup/install/multicluster/multi-primary_multi-network/), using the Istio documentation.
Istio is a service mesh that simplifies DNS (Domain Name System) resolution and helps establish
inter-cluster communication between the member Kubernetes clusters in a multi-Kubernetes cluster MongoDB deployment.
If you choose to use a service mesh, you need to install it. If you can't
utilize a service mesh, skip this section and use external domains
and configure DNS to enable external connectivity.

In addition, we offer the install_istio_separate_network example script. This script is based on Istio documentation and provides an example installation
that uses the [multi-primary mode on different networks](https://istio.io/latest/docs/setup/install/multicluster/multi-primary_multi-network/). We don't guarantee the script's maintenance with future Istio releases. If you choose to use the script, review the latest Istio documentation for
[installing a multicluster](https://istio.io/latest/docs/setup/install/multicluster/),
and, if necessary, adjust the script to match the documentation and your deployment.
If you use another service mesh solution, create your own script for
configuring separate networks to facilitate DNS resolution.

### Enable External Connectivity through External Domains and DNS Zones

If you don't use a service mesh, do the following to enable external
connectivity to and between `mongod` processes and the
Ops Manager MongoDB Agent:

- When you create a multi-Kubernetes cluster MongoDB deployment, use
  the spec.clusterSpecList.externalAccess.externalDomain
  setting to specify an external domain and instruct the Kubernetes Operator to
  configure hostnames for `mongod` processes in the following pattern:
  

  ```sh
  <pod-name>.<externalDomain>
  ```

  **Note:**

  You can specify external domains **only** for new deployments. You
  can't change external domains after you configure a multi-Kubernetes cluster MongoDB deployment.

  After you configure an external domain in this way, the Ops Manager
  MongoDB Agents and `mongod` processes use this domain to connect
  to each other.

- Customize external services that the Kubernetes Operator creates for each Pod
  in the Kubernetes cluster. Use the global configuration in the spec.externalAccess
  settings and Kubernetes cluster-specific overrides in the spec.clusterSpecList.externalAccess.externalService settings.

- Configure Pod hostnames in a DNS (Domain Name System) zone to ensure that each Kubernetes Pod
  hosting a `mongod` process allows establishing an external connection
  to the other `mongod` processes in a multi-Kubernetes cluster MongoDB deployment. A Pod is considered
  "exposed externally" when you can connect to a `mongod` process by
  using the `<pod-name>.<externalDomain>` hostname on ports 27017
  (this is the default database port) and 27018 (this is the database port + 1).
  You may also need to configure firewall rules to allow TCP traffic on
  ports 27017 and 27018.

..
  Feature for unknown future release - ER 7/13/23
  - When you create a Kubernetes cluster for your multi-Kubernetes cluster MongoDB deployment, use the
    spec.clusterDomain setting to specify
    an externally-available custom domain instead of the default domain.
    With the default cluster domain, `mongod` processes use `*.cluster.local`
    hostnames. However, if you specify an externally-available custom domain
    for each Kubernetes cluster in a multi-Kubernetes cluster MongoDB deployment, `mongod` processes use
    hostnames in the following pattern:

    ```sh
    <pod-name>.<replica-set-name>-svc.<namespace>.svc.<externally-available-cluster-domain>
    ```

    **Note:**

    You can set a custom cluster domain **only**  when creating a Kubernetes cluster
    for a multi-Kubernetes cluster MongoDB deployment.

After you complete these prerequisites, you can
deploy a multi-Kubernetes cluster without a service mesh.

## Check Connectivity Across Clusters

Follow the steps in this procedure to verify that service FQDN (fully qualified domain name)\s are
reachable across Kubernetes clusters.

In this example, you deploy a sample application defined in
sample-service.yaml
across two Kubernetes clusters.

**Step 1: Create a namespace in each cluster.**

Create a namespace in each of the Kubernetes clusters to deploy the `sample-service.yaml`.

```sh
kubectl create --context="${CTX_CLUSTER_1}" namespace sample
kubectl create --context="${CTX_CLUSTER_2}" namespace sample
```

**Note:**

In certain service mesh solutions, you might need to annotate
or label the namespace.

**Step 2: Deploy the `sample-service.yaml` in both Kubernetes clusters.**

```sh
kubectl apply --context="${CTX_CLUSTER_1}" \
   -f sample-service.yaml \
   -l service=helloworld1 \
   -n sample

kubectl apply --context="${CTX_CLUSTER_2}" \
   -f sample-service.yaml \
   -l service=helloworld2 \
   -n sample
```

**Step 3: Deploy the sample application on `CLUSTER_1`.**

```sh
kubectl apply --context="${CTX_CLUSTER_1}" \
   -f sample-service.yaml \
   -l version=v1 \
   -n sample
```

**Step 4: Ensure `CLUSTER_1` is running.**

Check that the `CLUSTER_1` hosting Pod is in the `Running` state.

```sh
kubectl get pod --context="${CTX_CLUSTER_1}" \
   -n sample \
   -l app=helloworld
```

**Step 5: Deploy the sample application on `CLUSTER_2`.**

```sh
kubectl apply --context="${CTX_CLUSTER_2}" \
   -f sample-service.yaml \
   -l version=v2 \
   -n sample
```

**Step 6: Ensure `CLUSTER_2` is running.**

Check that the `CLUSTER_2` hosting Pod is in the `Running` state.

```sh
kubectl get pod --context="${CTX_CLUSTER_2}" \
   -n sample \
   -l app=helloworld
```

**Step 7: Verify `CLUSTER_1` can connect to `CLUSTER_2`.**

Deploy the Pod in `CLUSTER_1` and check that you can reach the sample application in `CLUSTER_2`.

```sh
kubectl run  --context="${CTX_CLUSTER_1}" \
   -n sample \
   curl --image=radial/busyboxplus:curl \
   -i --tty \
   curl -sS helloworld2.sample:5000/hello
```

You should see output similar to this example:

```sh
Hello version: v2, instance: helloworld-v2-758dd55874-6x4t8
```

**Step 8: Verify `CLUSTER_2` can connect to `CLUSTER_1`.**

Deploy the Pod in `CLUSTER_2` and check that you can reach the sample application in `CLUSTER_1`.

```sh
kubectl run --context="${CTX_CLUSTER_2}" \
   -n sample \
   curl --image=radial/busyboxplus:curl \
   -i --tty \
   curl -sS helloworld1.sample:5000/hello
```

You should see output similar to this example:

```sh
Hello version: v1, instance: helloworld-v1-758dd55874-6x4t8
```

## Review the Requirements for Deploying Ops Manager

As part of the Quick Start, you deploy an Ops Manager resource on the central
cluster.

## Prepare for TLS-Encrypted Connections

If you plan to secure your multi-Kubernetes cluster MongoDB deployment using TLS (Transport Layer Security) encryption,
complete the following tasks to enable internal cluster authentication and generate TLS (Transport Layer Security)
certificates for member clusters and the MongoDB Agent:

**Note:**

You must possess the CA (Certificate Authority) certificate and the key that you used to
sign your TLS (Transport Layer Security) certificates.

**with-sm:**

**Step 1: Generate a TLS certificate for Kubernetes services.**

Use one of the following options:

- Generate a wildcard TLS (Transport Layer Security) certificate that covers hostnames
  of the services that the Kubernetes Operator creates for each Pod
  in the deployment.

  If you generate wildcard certificates, you can continue using
  the same certificates when you scale up or rebalance nodes in
  the Kubernetes member clusters, for example for disaster recovery.

  For example, add the hostname similar to the following format
  to the SAN (Subject Alternative Name):

  ```sh
  *.<namespace>.svc.cluster.local
  ```

- For each Kubernetes service that the Kubernetes Operator generates corresponding
  to each Pod in each member cluster, add SAN (Subject Alternative Name)\s to the certificate.
  In your TLS (Transport Layer Security) certificate, the SAN (Subject Alternative Name) for each Kubernetes service must
  use the following format:

  ```none
  <metadata.name>-<member_cluster_index>-<n>-svc.<namespace>.svc.cluster.local
  ```

  where `n` ranges from `0` to `clusterSpecList[member_cluster_index].members - 1`.

**Step 2: Generate one TLS certificate for your project's MongoDB Agents.**

For the MongoDB Agent TLS (Transport Layer Security) certificate:

- The Common Name in the TLS (Transport Layer Security) certificate must not be empty.

- The combined Organization and Organizational Unit in each TLS (Transport Layer Security)
  certificate must differ from the Organization and Organizational
  Unit in the TLS (Transport Layer Security) certificate for your replica set members. 

**via-script:**

To speed up creating TLS (Transport Layer Security) certificates for member Kubernetes clusters,
we offer the setup_tls script. We don't guarantee the script's maintenance. If you choose to use the script,
test it and adjust it to your needs. The script does the following:

- Creates the `cert-manager` namespace in the connected cluster and installs [cert-manager](https://cert-manager.io/docs/) using [Helm](https://helm.sh/) in the `cert-manager` namespace.

- Installs a local CA (Certificate Authority) using [mkcert](https://github.com/FiloSottile/mkcert).

- Downloads TLS (Transport Layer Security) certificates from `downloads.mongodb.com` and concatenates them with the CA (Certificate Authority) file name and `ca-chain`.

- Creates a ConfigMap that includes the `ca-chain` files.

- Creates an `Issuer` resource, which cert-manager uses to generate certificates.

- Creates a `Certificate` resource, which cert-manager uses to create a key object for the certificates.

To use the script:

**Step 1: Install `mkcert`.**

Install [mkcert](https://github.com/FiloSottile/mkcert) on the machine you plan to run this script.

**Step 2: Set the context to the central cluster.**

```sh
kubectl --context $MDB_CENTRAL_CLUSTER_FULL_NAME \
--namespace=<metadata.namespace> \
```

**Step 3: Run the `setup_tls` script.**

```sh
curl https://raw.githubusercontent.com/mongodb/mongodb-kubernetes/1.7.0/scripts/release/kubectl_mongodb/setup_tls.sh  -o  setup_tls.sh
```

The output includes:

- A secret containing the CA (Certificate Authority) named `ca-key-pair`.

- A secret containing the server certificates on the central n  `clustercert-${resource}-cert`.

- A ConfigMap containing the CA (Certificate Authority) certificates named `issuer-ca`.

**Step 4: Generate one TLS certificate for your project's MongoDB Agents.**

For the MongoDB Agent TLS (Transport Layer Security) certificate:

- The Common Name in the TLS (Transport Layer Security) certificate must not be empty.

- The combined Organization and Organizational Unit in each TLS (Transport Layer Security)
  certificate must differ from the Organization and Organizational
  Unit in the TLS (Transport Layer Security) certificate for your replica set members. 

**without-sm:**

**Step 1: Generate a TLS certificate for SAN hostnames.**

Use one of the following options:

- Generate a wildcard TLS (Transport Layer Security) certificate that contains all
  externalDomains
  that you created in the SAN (Subject Alternative Name). For example, add the hostnames
  similar to the following format to the SAN (Subject Alternative Name):

  ```sh
  *.cluster-0.example.com, *.cluster-1.example.com
  ```

  If you generate wildcard certificates, you can continue using
  them when you scale up or rebalance nodes in the Kubernetes member
  clusters, for example for disaster recovery.

- Generate a TLS (Transport Layer Security) certificate for each MongoDB replica set member
  hostname in the SAN (Subject Alternative Name). For example, add the hostnames similar
  to the following to the SAN (Subject Alternative Name):

  ```sh
  my-replica-set-0-0.cluster-0.example.com,
  my-replica-set-0-1.cluster-0.example.com, 
  my-replica-set-1-0.cluster-1.example.com,
  my-replica-set-1-1.cluster-1.example.com
  ```

  If you generate an individual TLS (Transport Layer Security) certificate that contains
  all the specific hostnames, you must create a new certificate
  each time you scale up or rebalance nodes in the Kubernetes member
  clusters, for example for disaster recovery.

**Step 2: Generate one TLS certificate for your project's MongoDB Agents.**

For the MongoDB Agent TLS (Transport Layer Security) certificate:

- The Common Name in the TLS (Transport Layer Security) certificate must not be empty.

- The combined Organization and Organizational Unit in each TLS (Transport Layer Security)
  certificate must differ from the Organization and Organizational
  Unit in the TLS (Transport Layer Security) certificate for your replica set members. 

**Important:**

The Kubernetes Operator uses `kubernetes.io/tls` secrets
to store TLS (Transport Layer Security) certificates and private keys for Ops Manager and MongoDB
resources. Starting in Kubernetes Operator version 1.17.0, the 
Kubernetes Operator doesn't support concatenated PEM (Privacy-Enhanced Mail) files stored as
`Opaque secrets`.

## Choose GitOps or the kubectl MongoDB Plugin

You can choose to create and maintain the resource files needed for the `MongoDBMultiCluster` resources deployment in a GitOps environment. 

If you use a GitOps workflow, you can't use the kubectl mongodb plugin, which automatically configures `role-based access control (RBAC)` and creates the kubeconfig file that allows the central cluster to communicate with its member clusters. Instead, you must manually configure or build your own automation for configuring the RBAC and `kubeconfig` files based on the procedure and examples in multi-cluster-gitops.

The following prerequisite sections describe how to install the kubectl MongoDB plugin if you don't use GitOps or configure resources for GitOps if you do.

## Install the kubectl MongoDB Plugin

Use the `kubectl mongodb` plugin to:

- Set up multi-Kubernetes-cluster Deployments
- Run automatic and manual disaster recovery

**Note:**

If you use GitOps, you can't use the `kubectl mongodb` plugin. Instead, follow the procedure in multi-cluster-gitops.

To install the `kubectl mongodb` plugin:

**Step 1: Download your desired Kubernetes Operator package version.**

Download your desired Kubernetes Operator package version from the
Release Page of the MongoDB Controllers for Kubernetes Operator Repository.

The package's name uses this pattern:
`kubectl-mongodb_{{ .Version }}_{{ .Os }}_{{ .Arch }}.tar.gz`.

Use one of the following packages:

- `kubectl-mongodb_{{ .Version }}_darwin_amd64.tar.gz`
- `kubectl-mongodb_{{ .Version }}_darwin_arm64.tar.gz`
- `kubectl-mongodb_{{ .Version }}_linux_amd64.tar.gz`
- `kubectl-mongodb_{{ .Version }}_linux_arm64.tar.gz`

**Step 2: Unpack the Kubernetes Operator package.**

Unpack the package, as in the following example:

```sh
tar -zxvf kubectl-mongodb_<version>_darwin_amd64.tar.gz
```

**Step 3: Locate the `kubectl mongodb` plugin binary and copy it to its desired destination.**

Find the `kubectl-mongodb` binary in the unpacked directory and move it
to its desired destination, inside the PATH for the Kubernetes Operator user,
as shown in the following example:

```sh
mv kubectl-mongodb /usr/local/bin/kubectl-mongodb
```

Now you can run the `kubectl mongodb` plugin using the following commands:

```sh
kubectl mongodb multicluster setup
kubectl mongodb multicluster recover
```

To learn more about the supported flags,
see the MongoDB kubectl plugin Reference.

## Configure Resources for GitOps

If you use a GitOps workflow, you won't be able to use the kubectl mongodb plugin to automatically configure `role-based access control (RBAC)` or the kubeconfig file that allows the central cluster to communicate with its member clusters. Instead, you must manually configure and apply the following resource files or build your own automation based on the information below.

**Note:**

To learn how the `kubectl mongodb` plugin automates the following steps, 
view the code in GitHub.

To configure RBAC and the `kubeconfig` for GitOps:

**Step 1: Create and apply RBAC resources to each cluster.**

Use these RBAC resource examples to create your own. To learn more about these 
RBAC resources, see multi-cluster-rbac-manual.

To apply them to your central and member clusters with GitOps, you can use a tool like [Argo CD](https://argoproj.github.io/cd).

**Step 2: Create and apply the ConfigMap file.**

The Kubernetes Operator keeps track of its member clusters using a [ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/) file. Copy, modify, and apply the following example ConfigMap:

```yaml
apiVersion: v1
kind: ConfigMap
data:
  cluster1: ""
  cluster2: ""
metadata:
  namespace: <namespace>
  name: mongodb-kubernetes-operator-member-list
  labels:
    multi-cluster: "true"
```

**Step 3: Configure the `kubeconfig` secret for the Kubernetes Operator.**

The Kubernetes Operator, which runs in the central cluster, communicates with the Pods in 
the member clusters through the Kubernetes API. For this to work, the Kubernetes Operator 
needs a `kubeconfig` 
file that contains the service account tokens of the member clusters. Create this 
`kubeconfig` file by following these steps: 

1. Obtain a list of [service accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) configured in the Kubernetes Operator's namespace.  For example, if you chose to use the default `mongodb` namespace, then you can obtain the service accounts using the following command:

   ```sh
   kubectl get serviceaccounts -n mongodb
   ```

#. Get the secret for each service account that belongs to a member cluster.

   ```sh
   kubectl get secret <service-account-name> -n mongodb -o yaml
   ```

#. In each service account secret, copy the CA (Certificate Authority) certificate and token. For example, copy `<ca_certificate>` and `<token>` from the secret, as shown in the following example:  

   ```yaml
   apiVersion: v1
   kind: Secret
   metadata:
     name: my-service-account
     namespace: mongodb
   data:
     ca.crt: <ca_certificate>
     token: <token>
   ```

#. Copy the following `kubeconfig` example for the central cluster and replace 
   the placeholders with the `<ca_certificate>` and `<token>` you copied from 
   the service account secrets by running the commands listed below.

   ```yaml
   apiVersion: v1
   clusters:
   - cluster:
       certificate-authority:
       server: https://
     name: kind-e2e-cluster-1
   - cluster:
       certificate-authority:
       server: https://
     name: kind-e2e-cluster-2
   contexts:
   - context:
       cluster: kind-e2e-cluster-1
       namespace: mongodb
       user: kind-e2e-cluster-1
     name: kind-e2e-cluster-1
   - context:
       cluster: kind-e2e-cluster-2
       namespace: mongodb
       user: kind-e2e-cluster-2
     name: kind-e2e-cluster-2
   kind: Config
   users:
   - name: kind-e2e-cluster-1
     user:
       token:
   - name: kind-e2e-cluster-2
     user:
       token:
   ```

   Populate the following `kubectl` commands with the correct values and run 
   them to update your example `kubeconfig` file.

   ```sh
   kubectl config --kubeconfig=kubeconfig set-cluster kind-e2e-cluster-1 --certificate-authority=<cluster-1-ca.crt>
   kubectl config --kubeconfig=kubeconfig set-cluster kind-e2e-cluster-2 --certificate-authority=<cluster-2-ca.crt>

   kubectl config --kubeconfig=kubeconfig set-credentials kind-e2e-cluster-1 --token=<cluster-1-token>
   kubectl config --kubeconfig=kubeconfig set-credentials kind-e2e-cluster-2 --token=<cluster-2-token>
   ```

#. Create a secret in the central cluster that you mount in the Kubernetes Operator as illustrated in the reference Helm chart. For example:

   ```sh
   kubectl --context="${CTX_CENTRAL_CLUSTER}" -n <operator-namespace> create secret --from-file=kubeconfig=<path-to-kubeconfig-file> <kubeconfig-secret-name>
   ```
