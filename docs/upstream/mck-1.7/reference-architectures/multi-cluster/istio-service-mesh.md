<!-- Converted from reference-architectures/multi-cluster/istio-service-mesh.txt (reStructuredText). Includes are inlined. -->

# Istio Service Mesh

While it is possible to deploy Multi-Cluster Ops Manager, Multi-Cluster 
Sharded Cluster, and Multi-Cluster Replica Set configurations 
without a service mesh, 
the recommended approach (presented here) is to leverage a service mesh to 
handle the networking across multiple Kubernetes clusters. To learn more, 
see How Does the Kubernetes Operator Establish Connectivity.

This page walks you through the process of deploying and validating an [Istio](https://istio.io/) 
service mesh across multiple Kubernetes clusters. Istio is only one of many options 
for deploying a service mesh, and it is not supported by MongoDB.

**Note:** Istio is not supported by MongoDB

Istio is not supported by MongoDB and is only one of many tools you can use 
to deploy a service mesh across your Kubernetes clusters.

## Prerequisites

Before you begin, perform the following tasks:

- Install `kubectl`.
- Set the `K8S_CLUSTER_*_CONTEXT_NAME` environment variables as 
  explained in the GKE Clusters guide.

## Source Code

You can find all included source code in the [MongoDB Kubernetes Operator repository](https://github.com/mongodb/mongodb-kubernetes/tree/1.7.0/public/architectures/setup-multi-cluster/ra-03-setup-istio).

## Procedure

**Step 1: Clone the Kubernetes Operator repository.**

Run the following command to clone the repository.

```bash
git clone https://github.com/mongodb/mongodb-kubernetes.git
cd mongodb-kubernetes
git checkout 1.7.0
cd public/architectures
```

**Step 2: Install Istio service mesh.**

Install [Istio](https://istio.io/) service mesh to allow cross-cluster DNS (Domain Name System) resolution
and network connectivity between Kubernetes clusters.

```bash
CTX_CLUSTER1=${K8S_CLUSTER_0_CONTEXT_NAME} \
CTX_CLUSTER2=${K8S_CLUSTER_1_CONTEXT_NAME} \
CTX_CLUSTER3=${K8S_CLUSTER_2_CONTEXT_NAME} \
ISTIO_VERSION="1.20.2" \
./install_istio_separate_network.sh
```

**Step 3: Label the Kubernetes namespaces.**

Label the Kubernetes namespaces in each cluster to enable Istio sidecar injection.

```
kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" label namespace "${OPERATOR_NAMESPACE}" istio-injection=enabled --overwrite
kubectl --context "${K8S_CLUSTER_1_CONTEXT_NAME}" label namespace "${OPERATOR_NAMESPACE}" istio-injection=enabled --overwrite
kubectl --context "${K8S_CLUSTER_2_CONTEXT_NAME}" label namespace "${OPERATOR_NAMESPACE}" istio-injection=enabled --overwrite

kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" label namespace "${OM_NAMESPACE}" istio-injection=enabled --overwrite
kubectl --context "${K8S_CLUSTER_1_CONTEXT_NAME}" label namespace "${OM_NAMESPACE}" istio-injection=enabled --overwrite
kubectl --context "${K8S_CLUSTER_2_CONTEXT_NAME}" label namespace "${OM_NAMESPACE}" istio-injection=enabled --overwrite

kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" label namespace "${MDB_NAMESPACE}" istio-injection=enabled --overwrite
kubectl --context "${K8S_CLUSTER_1_CONTEXT_NAME}" label namespace "${MDB_NAMESPACE}" istio-injection=enabled --overwrite
kubectl --context "${K8S_CLUSTER_2_CONTEXT_NAME}" label namespace "${MDB_NAMESPACE}" istio-injection=enabled --overwrite
```

**Step 4: Optional. Check cluster connectivity.**

The following optional scripts verify whether the service mesh is
configured correctly for cross-cluster DNS resolution and connectivity.

a. Create a Kubernetes namespace for the connectivity test.

   ```bash
   kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" create namespace "connectivity-test"
   kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" label namespace "connectivity-test" istio-injection=enabled --overwrite

   kubectl --context "${K8S_CLUSTER_1_CONTEXT_NAME}" create namespace "connectivity-test"
   kubectl --context "${K8S_CLUSTER_1_CONTEXT_NAME}" label namespace "connectivity-test" istio-injection=enabled --overwrite

   kubectl --context "${K8S_CLUSTER_2_CONTEXT_NAME}" create namespace "connectivity-test"
   kubectl --context "${K8S_CLUSTER_2_CONTEXT_NAME}" label namespace "connectivity-test" istio-injection=enabled --overwrite
   ```

b. Run this script on cluster 0:

   ```bash
   kubectl apply --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "connectivity-test" -f - <<EOF
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

c. Run this script on cluster 1:

   ```bash
   kubectl apply --context "${K8S_CLUSTER_1_CONTEXT_NAME}" -n "connectivity-test" -f - <<EOF
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

d. Run this script on cluster 2:

   ```bash
   kubectl apply --context "${K8S_CLUSTER_2_CONTEXT_NAME}" -n "connectivity-test" -f - <<EOF
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

e. Run this script to wait for the creation of StatefulSets:

   ```bash
   kubectl wait --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "connectivity-test" --for=condition=ready pod -l statefulset.kubernetes.io/pod-name=echoserver0-0 --timeout=60s
   kubectl wait --context "${K8S_CLUSTER_1_CONTEXT_NAME}" -n "connectivity-test" --for=condition=ready pod -l statefulset.kubernetes.io/pod-name=echoserver1-0 --timeout=60s
   kubectl wait --context "${K8S_CLUSTER_2_CONTEXT_NAME}" -n "connectivity-test" --for=condition=ready pod -l statefulset.kubernetes.io/pod-name=echoserver2-0 --timeout=60s
   ```

f. Create Pod service on cluster 0:

   ```bash
   kubectl apply --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "connectivity-test" -f - <<EOF
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

g. Create Pod service on cluster 1:

   ```bash
   kubectl apply --context "${K8S_CLUSTER_1_CONTEXT_NAME}" -n "connectivity-test" -f - <<EOF
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

h. Create Pod service on cluster 2:

   ```bash
   kubectl apply --context "${K8S_CLUSTER_2_CONTEXT_NAME}" -n "connectivity-test" -f - <<EOF
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

i. Create round robin service on cluster 0:

   ```bash
   kubectl apply --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "connectivity-test" -f - <<EOF
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

j. Create round robin service on cluster 1:

   ```bash
   kubectl apply --context "${K8S_CLUSTER_1_CONTEXT_NAME}" -n "connectivity-test" -f - <<EOF
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

k. Create round robin service on cluster 2:

   ```bash
   kubectl apply --context "${K8S_CLUSTER_2_CONTEXT_NAME}" -n "connectivity-test" -f - <<EOF
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

l. Verify Pod 0 from cluster 1:

   ```bash
   ```

   Output:

   ```bash
   ```

m. Verify Pod 1 from cluster 0:

   ```bash
   ```

   Output:

   ```bash
   ```

n. Verify Pod 1 from cluster 2:

   ```bash
   ```

   Output:

   ```bash
   ```

o. Verify Pod 2 from cluster 0:

   ```bash
   ```

   Output:

   ```bash
   ```

p. Run the cleanup script:

   ```bash
   kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "connectivity-test" delete statefulset echoserver0
   kubectl --context "${K8S_CLUSTER_1_CONTEXT_NAME}" -n "connectivity-test" delete statefulset echoserver1
   kubectl --context "${K8S_CLUSTER_2_CONTEXT_NAME}" -n "connectivity-test" delete statefulset echoserver2
   kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "connectivity-test" delete service echoserver
   kubectl --context "${K8S_CLUSTER_1_CONTEXT_NAME}" -n "connectivity-test" delete service echoserver
   kubectl --context "${K8S_CLUSTER_2_CONTEXT_NAME}" -n "connectivity-test" delete service echoserver
   kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -n "connectivity-test" delete service echoserver0-0
   kubectl --context "${K8S_CLUSTER_1_CONTEXT_NAME}" -n "connectivity-test" delete service echoserver1-0
   kubectl --context "${K8S_CLUSTER_2_CONTEXT_NAME}" -n "connectivity-test" delete service echoserver2-0
   kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" delete ns "connectivity-test"
   kubectl --context "${K8S_CLUSTER_1_CONTEXT_NAME}" delete ns "connectivity-test"
   kubectl --context "${K8S_CLUSTER_2_CONTEXT_NAME}" delete ns "connectivity-test"
   ```
