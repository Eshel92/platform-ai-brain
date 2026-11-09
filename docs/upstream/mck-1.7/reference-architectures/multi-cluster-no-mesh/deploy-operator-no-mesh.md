<!-- Converted from reference-architectures/multi-cluster-no-mesh/deploy-operator-no-mesh.txt (reStructuredText). Includes are inlined. -->

# Deploy the MongoDB Controllers for Kubernetes Operator Without a Service Mesh

To deploy multiple instances of MongoDB resources across multiple 
Kubernetes clusters, you first need to deploy the Kubernetes Operator to one of your 
Kubernetes clusters. Once the Kubernetes Operator is deployed to your central cluster, 
you can then create and manage all of your MongoDB resources across all of your 
Kubernetes clusters by applying updates to your central cluster. 

**Note:**

The procedure to deploy the Kubernetes Operator is the same with or
without a service mesh. The operator installation does not configure
cluster-to-cluster networking. When you deploy your MongoDB
resources, the operator exposes each member through an external
Kubernetes Service and sets its hostname to an externally reachable
FQDN (fully qualified domain name). In this reference architecture, External DNS creates the DNS
records that map these FQDN (fully qualified domain name) to the external Services.

## Prerequisites

Before you begin the following procedure, perform the following actions:

- Install `kubectl`. 
- [Install Helm](https://helm.sh/docs/intro/install/).
- Complete the GKE Clusters procedure or the equivalent.
- Complete the Configure External DNS procedure or the equivalent.
- Install the `kubectl mongodb` plugin.
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

- Update as needed and set the environment variables defined in the following  `env_variables.sh` file.

  ```bash
  # Namespace in which Ops Manager and AppDB will be deployed
  export OM_NAMESPACE="mongodb-om"
  # Namespace in which the operator will be installed
  export OPERATOR_NAMESPACE="mongodb-operator"
  # Namespace in which MongoDB resources will be deployed
  export MDB_NAMESPACE="mongodb"

  # comma-separated key=value pairs for additional parameters passed to the helm-chart installing the operator
  export OPERATOR_ADDITIONAL_HELM_VALUES="${OPERATOR_ADDITIONAL_HELM_VALUES:-""}"

  export OFFICIAL_OPERATOR_HELM_CHART="mongodb/mongodb-kubernetes"
  export OPERATOR_HELM_CHART="${OPERATOR_HELM_CHART:-${OFFICIAL_OPERATOR_HELM_CHART}}"
  ```

## Source Code

You can find all included source code in the MongoDB Kubernetes Operator repository.

## Procedure

**Step 1: Create namespaces for the Kubernetes Operator, MongoDB and Ops Manager in each of your Kubernetes clusters.**

```bash
kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" create namespace "${OPERATOR_NAMESPACE}"
kubectl --context "${K8S_CLUSTER_1_CONTEXT_NAME}" create namespace "${OPERATOR_NAMESPACE}"
kubectl --context "${K8S_CLUSTER_2_CONTEXT_NAME}" create namespace "${OPERATOR_NAMESPACE}"

kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" create namespace "${OM_NAMESPACE}"
kubectl --context "${K8S_CLUSTER_1_CONTEXT_NAME}" create namespace "${OM_NAMESPACE}"
kubectl --context "${K8S_CLUSTER_2_CONTEXT_NAME}" create namespace "${OM_NAMESPACE}"

kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" create namespace "${MDB_NAMESPACE}"
kubectl --context "${K8S_CLUSTER_1_CONTEXT_NAME}" create namespace "${MDB_NAMESPACE}"
kubectl --context "${K8S_CLUSTER_2_CONTEXT_NAME}" create namespace "${MDB_NAMESPACE}"
```

**Step 2: Create image pull secrets.**

```bash
mkdir -p secrets

kubectl create secret generic "image-registries-secret" \
        --from-file=.dockerconfigjson="${HOME}/.docker/config.json" --type=kubernetes.io/dockerconfigjson \
        --dry-run=client -o yaml > secrets/image-registries-secret.yaml

kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${OPERATOR_NAMESPACE}" apply -f secrets/image-registries-secret.yaml

kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${OM_NAMESPACE}" apply -f secrets/image-registries-secret.yaml
kubectl --context "${K8S_CLUSTER_1_CONTEXT_NAME}" -n "${OM_NAMESPACE}" apply -f secrets/image-registries-secret.yaml
kubectl --context "${K8S_CLUSTER_2_CONTEXT_NAME}" -n "${OM_NAMESPACE}" apply -f secrets/image-registries-secret.yaml

kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${MDB_NAMESPACE}" apply -f secrets/image-registries-secret.yaml
kubectl --context "${K8S_CLUSTER_1_CONTEXT_NAME}" -n "${MDB_NAMESPACE}" apply -f secrets/image-registries-secret.yaml
kubectl --context "${K8S_CLUSTER_2_CONTEXT_NAME}" -n "${MDB_NAMESPACE}" apply -f secrets/image-registries-secret.yaml
```

**Step 3: Configure your Kubernetes clusters.**

Run the following command to configure your Kubernetes clusters.

```bash
```

Output:

```
```

**Step 4: Add the MongoDB Helm Charts for Kubernetes.**

Add the [MongoDB Helm Charts for Kubernetes](https://mongodb.github.io/helm-charts) repository to Helm.

```bash
```

Output:

```
```

**Step 5: Deploy the Kubernetes Operator.**

Use the [MongoDB Helm Charts for Kubernetes](https://mongodb.github.io/helm-charts) to deploy the Kubernetes Operator.

```bash
```

Output:

```
```

**Step 6: Check the status of your MongoDB Controllers for Kubernetes Operator.**

```bash
```

Output:

```
```
