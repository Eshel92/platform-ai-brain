<!-- Converted from reference-architectures/multi-cluster-no-mesh/gke-clusters-no-mesh.txt (reStructuredText). Includes are inlined. -->

# Deploy GKE Clusters

Kubernetes is not vendor specific; however, for the sake of providing explicit 
and complete instructions for deploying all elements of a multi-cluster 
Kubernetes Operator implementation, this section walks you through the process 
of deploying multiple Kubernetes clusters on GCP (Google Cloud Platform) specifically. 

## Prerequisites

Before you begin, perform the following actions:

- Create a GCP (Google Cloud Platform) account.
- Prepare a GCP (Google Cloud Platform) project so that you can use it to create [GKE (Google Kubernetes Engine)](https://cloud.google.com/kubernetes-engine) clusters.
- Install the GCP (Google Cloud Platform) [CLI](https://cloud.google.com/sdk/docs/install). 
- [Authenticate](https://cloud.google.com/docs/authentication/gcloud) with the `gcloud auth login` command. 
- Update as needed and set the environment variables defined in the following  `env_variables.sh` file. 

```bash
# GCP project name - this is the only parameter that is mandatory to change here
export MDB_GKE_PROJECT="${MDB_GKE_PROJECT:="### Set your GKE project name here ###"}"

# Adjust the values for each Kubernetes cluster in your deployment.
# The deployment script references the following variables to get values for each cluster.
export K8S_CLUSTER_0="k8s-mdb-0${K8S_CLUSTER_SUFFIX:-""}"
export K8S_CLUSTER_0_ZONE="europe-central2-a"
export K8S_CLUSTER_0_NUMBER_OF_NODES=3
export K8S_CLUSTER_0_MACHINE_TYPE="e2-standard-4"
export K8S_CLUSTER_0_CONTEXT_NAME="gke_${MDB_GKE_PROJECT}_${K8S_CLUSTER_0_ZONE}_${K8S_CLUSTER_0}"

export K8S_CLUSTER_1="k8s-mdb-1${K8S_CLUSTER_SUFFIX:-""}"
export K8S_CLUSTER_1_ZONE="europe-central2-b"
export K8S_CLUSTER_1_NUMBER_OF_NODES=3
export K8S_CLUSTER_1_MACHINE_TYPE="e2-standard-4"
export K8S_CLUSTER_1_CONTEXT_NAME="gke_${MDB_GKE_PROJECT}_${K8S_CLUSTER_1_ZONE}_${K8S_CLUSTER_1}"

export K8S_CLUSTER_2="k8s-mdb-2${K8S_CLUSTER_SUFFIX:-""}"
export K8S_CLUSTER_2_ZONE="europe-central2-c"
export K8S_CLUSTER_2_NUMBER_OF_NODES=1
export K8S_CLUSTER_2_MACHINE_TYPE="e2-standard-4"
export K8S_CLUSTER_2_CONTEXT_NAME="gke_${MDB_GKE_PROJECT}_${K8S_CLUSTER_2_ZONE}_${K8S_CLUSTER_2}"

# Comment out the following line so that the script does not create preemptible nodes.
# DO NOT USE preemptible nodes in production.
export GKE_SPOT_INSTANCES_SWITCH="--preemptible"
```

## Source Code

You can find all included source code in the MongoDB Kubernetes Operator repository.

## Procedure

**Step 1: Set your default GCP (Google Cloud Platform) project:**

```bash
gcloud config set project "${MDB_GKE_PROJECT}"
```

**Step 2: Create Kubernetes clusters.**

Create three [GKE (Google Kubernetes Engine)](https://cloud.google.com/kubernetes-engine) clusters. The Kubernetes Operator is deployed to one of 
these clusters, and MongoDB custom resources are deployed across all 
clusters, and are managed by the Kubernetes Operator. 

```bash
gcloud container clusters create "${K8S_CLUSTER_0}" \
      --zone="${K8S_CLUSTER_0_ZONE}" \
      --num-nodes="${K8S_CLUSTER_0_NUMBER_OF_NODES}" \
      --machine-type "${K8S_CLUSTER_0_MACHINE_TYPE}" \
      --tags=mongodb \
      "${GKE_SPOT_INSTANCES_SWITCH:-""}"
```

```bash
gcloud container clusters create "${K8S_CLUSTER_1}" \
      --zone="${K8S_CLUSTER_1_ZONE}" \
      --num-nodes="${K8S_CLUSTER_1_NUMBER_OF_NODES}" \
      --machine-type "${K8S_CLUSTER_1_MACHINE_TYPE}" \
      --tags=mongodb \
      "${GKE_SPOT_INSTANCES_SWITCH:-""}"
```

```bash
gcloud container clusters create "${K8S_CLUSTER_2}" \
      --zone="${K8S_CLUSTER_2_ZONE}" \
      --num-nodes="${K8S_CLUSTER_2_NUMBER_OF_NODES}" \
      --machine-type "${K8S_CLUSTER_2_MACHINE_TYPE}" \
      --tags=mongodb \
      "${GKE_SPOT_INSTANCES_SWITCH:-""}"
```

**Step 3: Store credentials in your `kubeconfig` file.**

Obtain credentials and save contexts to the current `kubeconfig`
file. By default, this file is located in the `~/.kube/config` directory
and referenced by the `$KUBECONFIG` environment variable.

```bash
gcloud container clusters get-credentials "${K8S_CLUSTER_0}" --zone="${K8S_CLUSTER_0_ZONE}"
gcloud container clusters get-credentials "${K8S_CLUSTER_1}" --zone="${K8S_CLUSTER_1_ZONE}"
gcloud container clusters get-credentials "${K8S_CLUSTER_2}" --zone="${K8S_CLUSTER_2_ZONE}"
```

All `kubectl` commands reference these contexts using the following variables:

- `$K8S_CLUSTER_0_CONTEXT_NAME`
- `$K8S_CLUSTER_1_CONTEXT_NAME`
- `$K8S_CLUSTER_2_CONTEXT_NAME`

**Step 4: Verify that `kubectl` has access to Kubernetes clusters.**

```bash
```

Output:

```
```
