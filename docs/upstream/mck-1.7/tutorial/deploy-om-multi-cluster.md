<!-- Converted from tutorial/deploy-om-multi-cluster.txt (reStructuredText). Includes are inlined. -->

:noprevnext:

# Deploy Ops Manager Resources on Multiple Kubernetes Clusters

To make your multi-cluster Ops Manager and the Application Database deployment
resilient to entire data center or zone failures, deploy the Ops Manager Application
and the Application Database on multiple Kubernetes clusters.

To learn more about the architecture, networking, limitations, and performance
of multi-Kubernetes cluster deployments for Ops Manager resources, see:

- om-multi-k8s
- om-multi-k8s-limitations
- multi-vs-single-om-diffs
- Architecture Diagram
- Networking, Load Balancer, Service Mesh
- Performance

## Overview

**Note:**

The following procedure requires that you deploy a service mesh across all of 
your Kubernetes clusters. If you need to deploy Ops Manager across multiple Kubernetes 
clusters without a service mesh, please see Multi-Cluster Ops Manager Without a Service Mesh
to learn more.

When you deploy the Ops Manager Application and the Application Database using the
procedure in this section, you:

1. Use [GKE (Google Kubernetes Engine)](https://cloud.google.com/kubernetes-engine) and [Istio](https://istio.io/) service mesh as tools that help demonstrate the
   multi-Kubernetes cluster deployment.

2. Install the Kubernetes Operator on one of the member Kubernetes clusters,
   which serves as the central cluster. The central cluster acts as a Hub
   in the "Hub and Spoke" pattern used by the Kubernetes Operator to
   manage deployments on multiple Kubernetes clusters.

3. Deploy the central cluster in the `$OPERATOR_NAMESPACE` and
   configure this cluster to watch `$NAMESPACE` and manage all
   member Kubernetes clusters.

4. Deploy the Application Database and the Ops Manager Application on a single member
   Kubernetes cluster to demonstrate similarity of a multi-cluster deployment
   to a single cluster deployment. A single cluster deployment with
   `spec.topology` and `spec.applicationDatabase.topology`
   set to `MultiCluster` prepares the deployment for adding more Kubernetes clusters
   to it.

5. Deploy an additional Application Database replica set on the second member
   Kubernetes cluster to improve Application Database\'s resiliency. You also
   deploy an additional Ops Manager Application instance in the second member
   Kubernetes cluster.

6. Create valid certificates for TLS (Transport Layer Security) encryption, and establish
   TLS (Transport Layer Security)-encrypted connections to and from the Ops Manager Application and between
   the Application Database\'s replica set members.  When running over HTTPS (Hypertext Transfer Protocol Secure),
   Ops Manager runs on port `8443` by default.

7. Enable backup using S3 (Simple Storage Service)-compatible storage and deploy the Backup Daemon
   on the third member Kubernetes cluster. To simplify setting up S3 (Simple Storage Service)-compatible
   storage buckets, you deploy the [MinIO Operator](https://github.com/minio/operator). You enable the Backup Daemon only
   on one member cluster in your deployment. However, you can configure
   other member clusters to host the Backup Daemon resources as well.
   Only S3 (Simple Storage Service) backups are supported in multi-cluster Ops Manager deployments.

## Prerequisites

- install-tools-om-mc
- gcloud-cli-auth
- install-kubectl-mongodb-plugin-om-mc
- clone-k8sop-repo-om-mc
- set-env-vars-om-mc

### Install Tools

Before you can begin the deployment, install the following required tools:

- [Install Helm](https://helm.sh/docs/intro/install/). Installing [Helm](https://helm.sh/) is required for the installation of the Kubernetes Operator.
- [Install kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl).
- Prepare the GCP (Google Cloud Platform) project so that you can use it to create [GKE (Google Kubernetes Engine)](https://cloud.google.com/kubernetes-engine) clusters.
  In the following  procedure, you create three new GKE clusters, with a
  total of seven `e2-standard-4` low-cost [Spot VMs](https://cloud.google.com/kubernetes-engine/docs/concepts/spot-vms).
- [Install gcloud CLI](https://cloud.google.com/sdk/docs/install).

### Authorize into gcloud CLI

[Install gcloud CLI](https://cloud.google.com/sdk/docs/install) and authorize into it:

```sh
gcloud auth login
```

### Install the `kubectl mongodb` plugin

The kubectl mongodb plugin automates the
configuration of the Kubernetes clusters. This allows the Kubernetes Operator to
deploy resources, necessary roles, and services for accounts for the
Ops Manager Application, Application Database, and MongoDB resources on these clusters.

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

### Clone the MongoDB Controllers for Kubernetes Operator Repository

Clone the MongoDB Controllers for Kubernetes Operator repository, change into the `mongodb-kubernetes`
directory, and check out the current version.

```bash
git clone https://github.com/mongodb/mongodb-kubernetes.git
cd mongodb-kubernetes
git checkout 1.7.0
cd public/architectures
```

**Important:**

Some steps in this guide work only if you run them from
the `public/samples/ops-manager-multi-cluster` directory.

### Set up Environment Variables

All steps in this guide reference the environment variables defined in `env_variables.sh`.

```shell
export MDB_GKE_PROJECT="### Set your GKE project name here ###"

export NAMESPACE="mongodb"
export OPERATOR_NAMESPACE="mongodb-operator"

# comma-separated key=value pairs
# export OPERATOR_ADDITIONAL_HELM_VALUES=""

# Adjust the values for each Kubernetes cluster in your deployment.
# The deployment script references the following variables to get values for each cluster.
export K8S_CLUSTER_0="k8s-mdb-0"
export K8S_CLUSTER_0_ZONE="europe-central2-a"
export K8S_CLUSTER_0_NUMBER_OF_NODES=3
export K8S_CLUSTER_0_MACHINE_TYPE="e2-standard-4"
export K8S_CLUSTER_0_CONTEXT_NAME="gke_${MDB_GKE_PROJECT}_${K8S_CLUSTER_0_ZONE}_${K8S_CLUSTER_0}"

export K8S_CLUSTER_1="k8s-mdb-1"
export K8S_CLUSTER_1_ZONE="europe-central2-b"
export K8S_CLUSTER_1_NUMBER_OF_NODES=3
export K8S_CLUSTER_1_MACHINE_TYPE="e2-standard-4"
export K8S_CLUSTER_1_CONTEXT_NAME="gke_${MDB_GKE_PROJECT}_${K8S_CLUSTER_1_ZONE}_${K8S_CLUSTER_1}"

export K8S_CLUSTER_2="k8s-mdb-2"
export K8S_CLUSTER_2_ZONE="europe-central2-c"
export K8S_CLUSTER_2_NUMBER_OF_NODES=1
export K8S_CLUSTER_2_MACHINE_TYPE="e2-standard-4"
export K8S_CLUSTER_2_CONTEXT_NAME="gke_${MDB_GKE_PROJECT}_${K8S_CLUSTER_2_ZONE}_${K8S_CLUSTER_2}"

# Comment out the following line so that the script does not create preemptible nodes.
# DO NOT USE preemptible nodes in production.
export GKE_SPOT_INSTANCES_SWITCH="--preemptible"

export S3_OPLOG_BUCKET_NAME=s3-oplog-store
export S3_SNAPSHOT_BUCKET_NAME=s3-snapshot-store

# minio defaults
export S3_ENDPOINT="minio.tenant-tiny.svc.cluster.local"
export S3_ACCESS_KEY="console"
export S3_SECRET_KEY="console123"

export OFFICIAL_OPERATOR_HELM_CHART="mongodb/mongodb-kubernetes"
export OPERATOR_HELM_CHART="${OFFICIAL_OPERATOR_HELM_CHART}"

# (Optional) Change the following setting when using the external URL.
# This env variable is used in OpenSSL configuration to generate
# server certificates for Ops Manager Application.
export OPS_MANAGER_EXTERNAL_DOMAIN="om-svc.${NAMESPACE}.svc.cluster.local"

export OPS_MANAGER_VERSION="7.0.4"
export APPDB_VERSION="7.0.9-ubi8"
```

Adjust the settings in the previous example for your needs as instructed
in the comments and source them into your shell as follows:

```shell
source env_variables.sh
```

**Important:**

Each time after you update `env_variables.sh`, run `source env_variables.sh` 
to ensure that the scripts in this section use updated variables.

## Procedure

This procedure applies to deploying an Ops Manager instance on multiple
Kubernetes clusters.

**Step 1: Create Kubernetes clusters.**

You may skip this step if you already have installed and configured your
own Kubernetes clusters with a service mesh.

a. Create three [GKE (Google Kubernetes Engine)](https://cloud.google.com/kubernetes-engine) clusters:

   ```sh
   gcloud container clusters create "${K8S_CLUSTER_0}" \
         --zone="${K8S_CLUSTER_0_ZONE}" \
         --num-nodes="${K8S_CLUSTER_0_NUMBER_OF_NODES}" \
         --machine-type "${K8S_CLUSTER_0_MACHINE_TYPE}" \
         ${GKE_SPOT_INSTANCES_SWITCH:-""}
   ```

   ```sh
   gcloud container clusters create "${K8S_CLUSTER_1}" \
         --zone="${K8S_CLUSTER_1_ZONE}" \
         --num-nodes="${K8S_CLUSTER_1_NUMBER_OF_NODES}" \
         --machine-type "${K8S_CLUSTER_1_MACHINE_TYPE}" \
         ${GKE_SPOT_INSTANCES_SWITCH:-""}
   ```

   ```sh
   gcloud container clusters create "${K8S_CLUSTER_2}" \
         --zone="${K8S_CLUSTER_2_ZONE}" \
         --num-nodes="${K8S_CLUSTER_2_NUMBER_OF_NODES}" \
         --machine-type "${K8S_CLUSTER_2_MACHINE_TYPE}" \
         ${GKE_SPOT_INSTANCES_SWITCH:-""}
   ```

#. Set your default gcloud project:

   ```sh
   gcloud config set project "${MDB_GKE_PROJECT}"
   ```

#. Obtain credentials and save contexts to the current `kubeconfig`
   file. By default, this file is located in the `~/.kube/config` directory
   and referenced by the `$KUBECONFIG` environment variable.

   ```sh
   gcloud container clusters get-credentials "${K8S_CLUSTER_0}" --zone="${K8S_CLUSTER_0_ZONE}"
   gcloud container clusters get-credentials "${K8S_CLUSTER_1}" --zone="${K8S_CLUSTER_1_ZONE}"
   gcloud container clusters get-credentials "${K8S_CLUSTER_2}" --zone="${K8S_CLUSTER_2_ZONE}"
   ```

   All `kubectl` commands reference these contexts using the following variables:

   - `$K8S_CLUSTER_0_CONTEXT_NAME`
   - `$K8S_CLUSTER_1_CONTEXT_NAME`
   - `$K8S_CLUSTER_2_CONTEXT_NAME`

#. Verify that `kubectl` has access to Kubernetes clusters:

   ```sh
   ```

   Output:

   ```sh
   ```

#. Install [Istio](https://istio.io/) service mesh to allow cross-cluster DNS (Domain Name System) resolution
   and network connectivity between Kubernetes clusters:

   ```sh
   CTX_CLUSTER1=${K8S_CLUSTER_0_CONTEXT_NAME} \
   CTX_CLUSTER2=${K8S_CLUSTER_1_CONTEXT_NAME} \
   CTX_CLUSTER3=${K8S_CLUSTER_2_CONTEXT_NAME} \
   ISTIO_VERSION="1.20.2" \
   ../multi-cluster/install_istio_separate_network.sh
   ```

**Step 2: Create namespaces.**

**Note:**

To enable [sidecar injection](https://istio.io/latest/docs/setup/additional-setup/sidecar-injection/#automatic-sidecar-injection) in Istio, the following commands add
the `istio-injection=enabled` labels to the `$OPERATOR_NAMESPACE`
and the `mongodb` namespaces on each member cluster.
If you use another service mesh, configure it to handle network
traffic in the created namespaces.

- Create a separate namespace, `mongodb-operator`, referenced by the
  `$OPERATOR_NAMESPACE` environment variable
  for the Kubernetes Operator deployment.

- Create the same `$OPERATOR_NAMESPACE` on each member Kubernetes cluster.
  This is needed so that the kubectl mongodb plugin
  can create a service account for the Kubernetes Operator on each member cluster.
  The Kubernetes Operator uses these service accounts on the operator
  cluster to perform operations on each member cluster.

  ```sh
  kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" create namespace "${OPERATOR_NAMESPACE}"
  kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" label namespace "${OPERATOR_NAMESPACE}" istio-injection=enabled --overwrite

  kubectl --context "${K8S_CLUSTER_1_CONTEXT_NAME}" create namespace "${OPERATOR_NAMESPACE}"
  kubectl --context "${K8S_CLUSTER_1_CONTEXT_NAME}" label namespace "${OPERATOR_NAMESPACE}" istio-injection=enabled --overwrite

  kubectl --context "${K8S_CLUSTER_2_CONTEXT_NAME}" create namespace "${OPERATOR_NAMESPACE}"
  kubectl --context "${K8S_CLUSTER_2_CONTEXT_NAME}" label namespace "${OPERATOR_NAMESPACE}" istio-injection=enabled --overwrite
  ```

- On each member cluster, including the member cluster that serves
  as the central cluster, create another, separate namespace, `mongodb`.
  The Kubernetes Operator uses this namespace for Ops Manager resources and components.

  ```sh
  kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" create namespace "${NAMESPACE}"
  kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" label namespace "${NAMESPACE}" istio-injection=enabled --overwrite

  kubectl --context "${K8S_CLUSTER_1_CONTEXT_NAME}" create namespace "${NAMESPACE}"
  kubectl --context "${K8S_CLUSTER_1_CONTEXT_NAME}" label namespace "${NAMESPACE}" istio-injection=enabled --overwrite

  kubectl --context "${K8S_CLUSTER_2_CONTEXT_NAME}" create namespace "${NAMESPACE}"
  kubectl --context "${K8S_CLUSTER_2_CONTEXT_NAME}" label namespace "${NAMESPACE}" istio-injection=enabled --overwrite
  ```

**Step 3: Optional. Authorize clusters to pull secrets from private image registries.**

This step is optional if you use official Helm charts and images from the [Quay](https://quay.io/) registry.

```sh
kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${OPERATOR_NAMESPACE}" create secret generic "image-registries-secret" \
        --from-file=.dockerconfigjson="${HOME}/.docker/config.json" --type=kubernetes.io/dockerconfigjson
kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${NAMESPACE}" create secret generic "image-registries-secret" \
        --from-file=.dockerconfigjson="${HOME}/.docker/config.json" --type=kubernetes.io/dockerconfigjson
kubectl --context "${K8S_CLUSTER_1_CONTEXT_NAME}" -n "${NAMESPACE}" create secret generic "image-registries-secret" \
        --from-file=.dockerconfigjson="${HOME}/.docker/config.json" --type=kubernetes.io/dockerconfigjson
kubectl --context "${K8S_CLUSTER_2_CONTEXT_NAME}" -n "${NAMESPACE}" create secret generic "image-registries-secret" \
        --from-file=.dockerconfigjson="${HOME}/.docker/config.json" --type=kubernetes.io/dockerconfigjson
```

**Step 4: Optional. Check cluster connectivity.**

The following optional scripts verify whether the service mesh is
configured correctly for cross-cluster DNS resolution and connectivity.

a. Run this script on cluster 0:

   ```yaml
   kubectl apply --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${NAMESPACE}" -f - <<EOF
     apiVersion: apps/v1
     kind: StatefulSet
     metadata:
       name: echoserver0
     spec:
       replicas: 1
       selector:
         matchLabels:
           app: echoserver0
       template:
         metadata:
           labels:
             app: echoserver0
         spec:
           containers:
             - image: k8s.gcr.io/echoserver:1.10
               imagePullPolicy: Always
               name: echoserver0
               ports:
                 - containerPort: 8080
   EOF
   ```

b. Run this script on cluster 1:

   ```yaml
   kubectl apply --context "${K8S_CLUSTER_1_CONTEXT_NAME}" -n "${NAMESPACE}" -f - <<EOF
     apiVersion: apps/v1
     kind: StatefulSet
     metadata:
       name: echoserver1
     spec:
       replicas: 1
       selector:
         matchLabels:
           app: echoserver1
       template:
         metadata:
           labels:
             app: echoserver1
         spec:
           containers:
             - image: k8s.gcr.io/echoserver:1.10
               imagePullPolicy: Always
               name: echoserver1
               ports:
                 - containerPort: 8080
   EOF
   ```

c. Run this script on cluster 2:

   ```yaml
   kubectl apply --context "${K8S_CLUSTER_2_CONTEXT_NAME}" -n "${NAMESPACE}" -f - <<EOF
     apiVersion: apps/v1
     kind: StatefulSet
     metadata:
       name: echoserver2
     spec:
       replicas: 1
       selector:
         matchLabels:
           app: echoserver2
       template:
         metadata:
           labels:
             app: echoserver2
         spec:
           containers:
             - image: k8s.gcr.io/echoserver:1.10
               imagePullPolicy: Always
               name: echoserver2
               ports:
                 - containerPort: 8080
   EOF
   ```

d. Run this script to wait for the creation of StatefulSets:

   ```sh
   kubectl wait --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${NAMESPACE}" --for=condition=ready pod -l statefulset.kubernetes.io/pod-name=echoserver0-0 --timeout=60s
   kubectl wait --context "${K8S_CLUSTER_1_CONTEXT_NAME}" -n "${NAMESPACE}" --for=condition=ready pod -l statefulset.kubernetes.io/pod-name=echoserver1-0 --timeout=60s
   kubectl wait --context "${K8S_CLUSTER_2_CONTEXT_NAME}" -n "${NAMESPACE}" --for=condition=ready pod -l statefulset.kubernetes.io/pod-name=echoserver2-0 --timeout=60s
   ```

e. Create Pod service on cluster 0:

   ```yaml
   kubectl apply --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${NAMESPACE}" -f - <<EOF
   apiVersion: v1
   kind: Service
   metadata:
     name: echoserver0-0
   spec:
     ports:
       - port: 8080
         targetPort: 8080
         protocol: TCP
     selector:
       statefulset.kubernetes.io/pod-name: "echoserver0-0"
   EOF
   ```

f. Create Pod service on cluster 1:

   ```yaml
   kubectl apply --context "${K8S_CLUSTER_1_CONTEXT_NAME}" -n "${NAMESPACE}" -f - <<EOF
   apiVersion: v1
   kind: Service
   metadata:
     name: echoserver1-0
   spec:
     ports:
       - port: 8080
         targetPort: 8080
         protocol: TCP
     selector:
       statefulset.kubernetes.io/pod-name: "echoserver1-0"
   EOF
   ```

g. Create Pod service on cluster 2:

   ```yaml
   kubectl apply --context "${K8S_CLUSTER_2_CONTEXT_NAME}" -n "${NAMESPACE}" -f - <<EOF
   apiVersion: v1
   kind: Service
   metadata:
     name: echoserver2-0
   spec:
     ports:
       - port: 8080
         targetPort: 8080
         protocol: TCP
     selector:
       statefulset.kubernetes.io/pod-name: "echoserver2-0"
   EOF
   ```

h. Create round robin service on cluster 0:

   ```yaml
   kubectl apply --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${NAMESPACE}" -f - <<EOF
   apiVersion: v1
   kind: Service
   metadata:
     name: echoserver
   spec:
     ports:
       - port: 8080
         targetPort: 8080
         protocol: TCP
     selector:
       app: echoserver0
   EOF
   ```

i. Create round robin service on cluster 1:

   ```yaml
   kubectl apply --context "${K8S_CLUSTER_1_CONTEXT_NAME}" -n "${NAMESPACE}" -f - <<EOF
   apiVersion: v1
   kind: Service
   metadata:
     name: echoserver
   spec:
     ports:
       - port: 8080
         targetPort: 8080
         protocol: TCP
     selector:
       app: echoserver1
   EOF
   ```

j. Create round robin service on cluster 2:

   ```yaml
   kubectl apply --context "${K8S_CLUSTER_2_CONTEXT_NAME}" -n "${NAMESPACE}" -f - <<EOF
   apiVersion: v1
   kind: Service
   metadata:
     name: echoserver
   spec:
     ports:
       - port: 8080
         targetPort: 8080
         protocol: TCP
     selector:
       app: echoserver2
   EOF
   ```

k. Verify Pod 0 from cluster 1:

   ```sh
   ```

   Output:

   ```sh
   ```

l. Verify Pod 1 from cluster 0:

   ```sh
   ```

   Output:

   ```sh
   ```

m. Verify Pod 1 from cluster 2:

   ```sh
   ```

   Output:

   ```sh
   ```

o. Verify Pod 2 from cluster 0:

   ```sh
   ```

   Output:

   ```sh
   ```

p. Run the cleanup script:

   ```sh
   kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${NAMESPACE}" delete statefulset echoserver0
   kubectl --context "${K8S_CLUSTER_1_CONTEXT_NAME}" -n "${NAMESPACE}" delete statefulset echoserver1
   kubectl --context "${K8S_CLUSTER_2_CONTEXT_NAME}" -n "${NAMESPACE}" delete statefulset echoserver2
   kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${NAMESPACE}" delete service echoserver
   kubectl --context "${K8S_CLUSTER_1_CONTEXT_NAME}" -n "${NAMESPACE}" delete service echoserver
   kubectl --context "${K8S_CLUSTER_2_CONTEXT_NAME}" -n "${NAMESPACE}" delete service echoserver
   kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${NAMESPACE}" delete service echoserver0-0
   kubectl --context "${K8S_CLUSTER_1_CONTEXT_NAME}" -n "${NAMESPACE}" delete service echoserver1-0
   kubectl --context "${K8S_CLUSTER_2_CONTEXT_NAME}" -n "${NAMESPACE}" delete service echoserver2-0
   ```

**Step 5: Deploy a multi-cluster configuration.**

In this step, you use the `kubectl mongodb` plugin to automate the Kubernetes cluster
configuration that is necessary for the Kubernetes Operator to manage workloads
on multiple Kubernetes clusters.

Because you configure the Kubernetes clusters before you install the Kubernetes Operator,
when you deploy the Kubernetes Operator for the multi-Kubernetes cluster operation,
all the necessary multi-cluster configuration is already in place. 

As stated in the om-multi-procedure-overview, the Kubernetes Operator
has the configuration for three member clusters that you can use to deploy
Ops Manager MongoDB databases.
The first cluster is also used as the central cluster, where you
install the Kubernetes Operator and deploy the custom resources.

```sh
```

Output:

```sh
```

**Step 6: Install the Kubernetes Operator using the Helm chart.**

a. Add and update the MongoDB Helm repository. Verify that the local Helm cache refers to the correct Kubernetes Operator version:

   ```sh
   ```

   Output:

   ```sh
   ```

b. Install the Kubernetes Operator into the `$OPERATOR_NAMESPACE`, configured to watch
   `$NAMESPACE` and to manage three member Kubernetes clusters. At this point
   in the procedure, `ServiceAccounts`
   and `roles`
   are already deployed by the `kubectl mongodb` plugin. Therefore, the following
   scripts skip configuring them and set `operator.createOperatorServiceAccount=false`
   and `operator.createResourcesServiceAccountsAndRoles=false`.
   The scripts specify the `multiCluster.clusters` setting to instruct
   the Helm chart to deploy the Kubernetes Operator in multi-cluster mode.

   ```sh
   ```

   Output:

   ```sh
   ```

c. Check the Kubernetes Operator deployment:

   ```sh
   ```

   Output:

   ```sh
   ```

**Step 7: Prepare TLS certificates.**

In this step, you enable TLS (Transport Layer Security) for the Application Database and the Ops Manager Application.
If you don't want to use TLS, remove the following fields from the `MongoDBOpsManager`
resources:

- `spec.security.certsSecretPrefix`
- `spec.security.tls.ca`
- `spec.applicationDatabase.security.certsSecretPrefix`
- `spec.applicationDatabase.security.tls.ca`

a. Optional. Generate keys and certificates:

   Use the `openssl` command line tool to generate self-signed CAs and
   certificates for testing purposes.

   ```shell
   mkdir certs || true

   cat <<EOF >certs/ca.cnf
   [ req ]
   default_bits       = 2048
   prompt             = no
   default_md         = sha256
   distinguished_name = dn
   x509_extensions    = v3_ca

   [ dn ]
   C=US
   ST=New York
   L=New York
   O=Example Company
   OU=IT Department
   CN=exampleCA

   [ v3_ca ]
   basicConstraints = CA:TRUE
   keyUsage = critical, keyCertSign, cRLSign
   subjectKeyIdentifier = hash
   authorityKeyIdentifier = keyid:always,issuer
   EOF

   cat <<EOF >certs/om.cnf
   [ req ]
   default_bits       = 2048
   prompt             = no
   default_md         = sha256
   distinguished_name = dn
   req_extensions     = req_ext

   [ dn ]
   C=US
   ST=New York
   L=New York
   O=Example Company
   OU=IT Department
   CN=${OPS_MANAGER_EXTERNAL_DOMAIN}

   [ req_ext ]
   subjectAltName = @alt_names
   keyUsage = critical, digitalSignature, keyEncipherment
   extendedKeyUsage = serverAuth, clientAuth

   [ alt_names ]
   DNS.1 = ${OPS_MANAGER_EXTERNAL_DOMAIN}
   DNS.2 = om-svc.${NAMESPACE}.svc.cluster.local
   EOF

   cat <<EOF >certs/appdb.cnf
   [ req ]
   default_bits       = 2048
   prompt             = no
   default_md         = sha256
   distinguished_name = dn
   req_extensions     = req_ext

   [ dn ]
   C=US
   ST=New York
   L=New York
   O=Example Company
   OU=IT Department
   CN=AppDB

   [ req_ext ]
   subjectAltName = @alt_names
   keyUsage = critical, digitalSignature, keyEncipherment
   extendedKeyUsage = serverAuth, clientAuth

   [ alt_names ]
   # multi-cluster mongod hostnames from service for each pod
   DNS.1 = *.${NAMESPACE}.svc.cluster.local
   # single-cluster mongod hostnames from headless service
   DNS.2 = *.om-db-svc.${NAMESPACE}.svc.cluster.local
   EOF

   # generate CA keypair and certificate
   openssl genrsa -out certs/ca.key 2048
   openssl req -x509 -new -nodes -key certs/ca.key -days 1024 -out certs/ca.crt -config certs/ca.cnf

   # generate OpsManager's keypair and certificate
   openssl genrsa -out certs/om.key 2048
   openssl req -new -key certs/om.key -out certs/om.csr -config certs/om.cnf

   # generate AppDB's keypair and certificate
   openssl genrsa -out certs/appdb.key 2048
   openssl req -new -key certs/appdb.key -out certs/appdb.csr -config certs/appdb.cnf

   # generate certificates signed by CA for OpsManager and AppDB
   openssl x509 -req -in certs/om.csr -CA certs/ca.crt -CAkey certs/ca.key -CAcreateserial -out certs/om.crt -days 365 -sha256 -extfile certs/om.cnf -extensions req_ext
   openssl x509 -req -in certs/appdb.csr -CA certs/ca.crt -CAkey certs/ca.key -CAcreateserial -out certs/appdb.crt -days 365 -sha256 -extfile certs/appdb.cnf -extensions req_ext
   ```

b. Create secrets with TLS keys:

   If you prefer to use your own keys and certificates, skip the previous
   generation step and put the keys and certificates  into the following files:

   - `certs/ca.crt` - CA (Certificate Authority) certificates. These are not necessary when using trusted certificates.
   - `certs/appdb.key` - private key for the Application Database.
   - `certs/appdb.crt` - certificate for the Application Database.
   - `certs/om.key` - private key for Ops Manager.
   - `certs/om.crt` - certificate for Ops Manager.

   ```sh
   kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${NAMESPACE}" create secret tls cert-prefix-om-cert \
     --cert=certs/om.crt \
     --key=certs/om.key

   kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${NAMESPACE}" create secret tls cert-prefix-om-db-cert \
     --cert=certs/appdb.crt \
     --key=certs/appdb.key

   kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${NAMESPACE}" create configmap om-cert-ca --from-file="mms-ca.crt=certs/ca.crt"
   kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${NAMESPACE}" create configmap appdb-cert-ca --from-file="ca-pem=certs/ca.crt"
   ```

**Step 8: Install Ops Manager.**

At this point, you have prepared the environment and the Kubernetes Operator
to deploy the Ops Manager resource.

a. Create the necessary credentials for the Ops Manager admin user that the
   Kubernetes Operator will create after deploying the Ops Manager Application instance:

   ```sh
   kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" --namespace "${NAMESPACE}" create secret generic om-admin-user-credentials \
     --from-literal=Username="admin" \
     --from-literal=Password="Passw0rd@" \
     --from-literal=FirstName="Jane" \
     --from-literal=LastName="Doe"
   ```

b. Deploy the simplest `MongoDBOpsManager` custom resource possible
   (with TLS (Transport Layer Security) enabled) on a single member cluster, which is also known as
   the central cluster.

   This deployment is almost the same as for the single-cluster mode,
   but with `spec.topology` and `spec.applicationDatabase.topology`
   set to `MultiCluster`.

   Deploying this way shows that a single Kubernetes cluster deployment is
   a special case of a multi-Kubernetes cluster deployment on a single Kubernetes member cluster.
   You can start deploying the Ops Manager Application and the Application Database
   on as many Kubernetes clusters as necessary from the beginning, and don't
   have to start with the deployment with only a single member Kubernetes cluster.

   At this point, you have prepared the Ops Manager deployment to span more
   than one Kubernetes cluster, which you will do later in this procedure.

   ```yaml
   kubectl apply --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${NAMESPACE}" -f - <<EOF
   apiVersion: mongodb.com/v1
   kind: MongoDBOpsManager
   metadata:
     name: om
   spec:
     topology: MultiCluster
     version: "${OPS_MANAGER_VERSION}"
     adminCredentials: om-admin-user-credentials
     security:
       certsSecretPrefix: cert-prefix
       tls:
         ca: om-cert-ca
     clusterSpecList:
       - clusterName: "${K8S_CLUSTER_0_CONTEXT_NAME}"
         members: 1
     applicationDatabase:
       version: "${APPDB_VERSION}"
       topology: MultiCluster
       security:
         certsSecretPrefix: cert-prefix
         tls:
           ca: appdb-cert-ca
       clusterSpecList:
         - clusterName: "${K8S_CLUSTER_0_CONTEXT_NAME}"
           members: 3
     backup:
       enabled: false
   EOF
   ```

c. Wait for the Kubernetes Operator to pick up the work and reach the
   `status.applicationDatabase.phase=Pending` state. Wait for both the
   Application Database and Ops Manager deployments to complete.

   ```sh
   ```

   Output:

   ```sh
   ```

d. Deploy Ops Manager. The Kubernetes Operator deploys Ops Manager by performing
   the following steps. It:

   - Deploys the Application Database\'s replica set nodes and waits
     for the MongoDB processes in the replica set to start running.
   - Deploys the Ops Manager Application instance with the Application Database\'s
     connection string and waits for it to become ready.
   - Adds the Monitoring MongoDB Agent containers to each Application Database\'s Pod.
   - Waits for both the Ops Manager Application and the Application Database Pods to start running.

   ```sh
   ```

   Output:

   ```sh
   ```

   Now that you have deployed a single-member cluster in a multi-cluster mode,
   you can reconfigure this deployment to span more than one Kubernetes cluster.

e. On the second member cluster, deploy two additional Application Database
   replica set members and one additional instance of the Ops Manager Application:

   ```yaml
   kubectl apply --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${NAMESPACE}" -f - <<EOF
   apiVersion: mongodb.com/v1
   kind: MongoDBOpsManager
   metadata:
     name: om
   spec:
     topology: MultiCluster
     version: "${OPS_MANAGER_VERSION}"
     adminCredentials: om-admin-user-credentials
     security:
       certsSecretPrefix: cert-prefix
       tls:
         ca: om-cert-ca
     clusterSpecList:
       - clusterName: "${K8S_CLUSTER_0_CONTEXT_NAME}"
         members: 1
       - clusterName: "${K8S_CLUSTER_1_CONTEXT_NAME}"
         members: 1
     applicationDatabase:
       version: "${APPDB_VERSION}"
       topology: MultiCluster
       security:
         certsSecretPrefix: cert-prefix
         tls:
           ca: appdb-cert-ca
       clusterSpecList:
         - clusterName: "${K8S_CLUSTER_0_CONTEXT_NAME}"
           members: 3
         - clusterName: "${K8S_CLUSTER_1_CONTEXT_NAME}"
           members: 2
     backup:
       enabled: false
   EOF
   ```

f. Wait for the Kubernetes Operator to pick up the work (pending phase):

   ```sh
   ```

   Output:

   ```sh
   ```

g. Wait for the Kubernetes Operator to finish deploying all components:

   ```sh
   ```

   Output:

   ```sh
   ```

**Step 9: Enable backup.**

In a multi-Kubernetes cluster deployment of the Ops Manager Application, you can configure
only S3 (Simple Storage Service)-based backup storage. This procedure refers to `S3_*`
defined in env_variables.sh.

a. Optional. Install the [MinIO Operator](https://github.com/minio/operator).

   This procedure deploys S3 (Simple Storage Service)-compatible storage for your backups using the [MinIO Operator](https://github.com/minio/operator).
   You can skip this step if you have AWS (Amazon Web Services) S3 (Simple Storage Service) or other S3 (Simple Storage Service)-compatible
   buckets available. Adjust the `S3_*` variables accordingly in
   env_variables.sh in this case.

   ```sh
   kubectl kustomize "github.com/minio/operator/resources/?timeout=120&ref=v5.0.12" | \
     kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" apply -f -

   kubectl kustomize "github.com/minio/operator/examples/kustomization/tenant-tiny?timeout=120&ref=v5.0.12" | \
     kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" apply -f -

   # add two buckets to the tenant config
   kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "tenant-tiny" patch tenant/myminio \
     --type='json' \
     -p="[{\"op\": \"add\", \"path\": \"/spec/buckets\", \"value\": [{\"name\": \"${S3_OPLOG_BUCKET_NAME}\"}, {\"name\": \"${S3_SNAPSHOT_BUCKET_NAME}\"}]}]"
   ```

b. Before you configure and enable backup, create secrets:

   - `s3-access-secret` - contains S3 (Simple Storage Service) credentials.
   - `s3-ca-cert` - contains a CA (Certificate Authority) certificate that issued the bucket's
     server certificate. In the case of the sample MinIO deployment used
     in this procedure, the default Kubernetes Root CA (Certificate Authority) certificate
     is used to sign the certificate. Because it's not a publicly trusted
     CA (Certificate Authority) certificate, you must provide it so that Ops Manager can
     trust the connection.

   If you use publicly trusted certificates, you may skip this step and
   remove the values from the `spec.backup.s3Stores.customCertificateSecretRefs`
   and `spec.backup.s3OpLogStores.customCertificateSecretRefs` settings.

   ```sh
   kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${NAMESPACE}" create secret generic s3-access-secret \
     --from-literal=accessKey="${S3_ACCESS_KEY}" \
     --from-literal=secretKey="${S3_SECRET_KEY}"

   # minio TLS secrets are signed with the default k8s root CA
   kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${NAMESPACE}" create secret generic s3-ca-cert \
     --from-literal=ca.crt="$(kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n kube-system get configmap kube-root-ca.crt -o jsonpath="{.data.ca\.crt}")"
   ```

**Step 10: Re-deploy Ops Manager with backup enabled.**

a. The Kubernetes Operator can configure and deploy all components,
   the Ops Manager Application, the Backup Daemon instances, and the Application
   Database's replica set nodes in any combination on any member clusters
   for which you configure the Kubernetes Operator.

   To illustrate the flexibility of the multi-Kubernetes cluster deployment
   configuration, deploy only one Backup Daemon instance on the third
   member cluster and specify zero Backup Daemon members for the first
   and second clusters.

   ```yaml
   kubectl apply --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "${NAMESPACE}" -f - <<EOF
   apiVersion: mongodb.com/v1
   kind: MongoDBOpsManager
   metadata:
     name: om
   spec:
     topology: MultiCluster
     version: "${OPS_MANAGER_VERSION}"
     adminCredentials: om-admin-user-credentials
     security:
       certsSecretPrefix: cert-prefix
       tls:
         ca: om-cert-ca
     clusterSpecList:
       - clusterName: "${K8S_CLUSTER_0_CONTEXT_NAME}"
         members: 1
         backup:
           members: 0
       - clusterName: "${K8S_CLUSTER_1_CONTEXT_NAME}"
         members: 1
         backup:
           members: 0
       - clusterName: "${K8S_CLUSTER_2_CONTEXT_NAME}"
         members: 0
         backup:
           members: 1
     configuration: # to avoid configuration wizard on first login
         mms.adminEmailAddr: email@example.com
         mms.fromEmailAddr: email@example.com
         mms.ignoreInitialUiSetup: "true"
         mms.mail.hostname: smtp@example.com
         mms.mail.port: "465"
         mms.mail.ssl: "true"
         mms.mail.transport: smtp
         mms.minimumTLSVersion: TLSv1.2
         mms.replyToEmailAddr: email@example.com
     applicationDatabase:
       version: "${APPDB_VERSION}"
       topology: MultiCluster
       security:
         certsSecretPrefix: cert-prefix
         tls:
           ca: appdb-cert-ca
       clusterSpecList:
         - clusterName: "${K8S_CLUSTER_0_CONTEXT_NAME}"
           members: 3
         - clusterName: "${K8S_CLUSTER_1_CONTEXT_NAME}"
           members: 2
     backup:
       enabled: true
       s3Stores:
         - name: my-s3-block-store
           s3SecretRef:
             name: "s3-access-secret"
           pathStyleAccessEnabled: true
           s3BucketEndpoint: "${S3_ENDPOINT}"
           s3BucketName: "${S3_SNAPSHOT_BUCKET_NAME}"
           customCertificateSecretRefs:
             - name: s3-ca-cert
               key: ca.crt
       s3OpLogStores:
         - name: my-s3-oplog-store
           s3SecretRef:
             name: "s3-access-secret"
           s3BucketEndpoint: "${S3_ENDPOINT}"
           s3BucketName: "${S3_OPLOG_BUCKET_NAME}"
           pathStyleAccessEnabled: true
           customCertificateSecretRefs:
             - name: s3-ca-cert
               key: ca.crt
   EOF
   ```

b. Wait until the Kubernetes Operator finishes its configuration:

   ```sh
   ```

   Output:

   ```sh
   ```

**Step 11: Optional. Delete the [GKE (Google Kubernetes Engine)](https://cloud.google.com/kubernetes-engine) clusters and all their associated resources (VMs).**

Run the following script to delete the GKE clusters and clean up your environment.

**Important:**

The following commands are not reversible. They delete all clusters
referenced in `env_variables.sh`. Don't run these commands if you
wish to retain the GKE clusters, for example, if you didn't create
the GKE clusters as part of this procedure.

```sh
yes | gcloud container clusters delete "${K8S_CLUSTER_0}" --zone="${K8S_CLUSTER_0_ZONE}" &
yes | gcloud container clusters delete "${K8S_CLUSTER_1}" --zone="${K8S_CLUSTER_1_ZONE}" &
yes | gcloud container clusters delete "${K8S_CLUSTER_2}" --zone="${K8S_CLUSTER_2_ZONE}" &
wait
```
