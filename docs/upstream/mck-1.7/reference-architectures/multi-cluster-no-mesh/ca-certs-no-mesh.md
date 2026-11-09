<!-- Converted from reference-architectures/multi-cluster-no-mesh/ca-certs-no-mesh.txt (reStructuredText). Includes are inlined. -->

# Manage TLS Certificates (No Service Mesh)

This section provides guidance on the creation of TLS certificates for each 
component of MongoDB, and the creation of Kubernetes Secrets in each of your Kubernetes 
clusters to mount the TLS certificates securely into the appropriate Kubernetes Pods. 

The process outlined below utilizes [Cert Manager](https://cert-manager.io/) 
for creating the TLS certificates. However, note that this is an 
opinionated guide, and CertManager is not supported by MongoDB. Moreover, CertManager 
is only one of many ways in which you can add TLS certificates to your Kubernetes clusters.
Additionally, self-signed certificates may not be suitable for production deployments, 
depending on the security requirements of your organization. If you require 
publicly trusted certificates configure your [Issuer](https://cert-manager.io/docs/configuration/issuers/) accordingly 
or provide the TLS certificate directly. To learn more, see cert-manager-integration.

## Prerequisites

Before you begin, perform the following tasks:

- Install `kubectl`.
- [Install Helm](https://helm.sh/docs/intro/install/).
- Set the `K8S_CLUSTER_*_CONTEXT_NAME` environment variables as 
  explained in the GKE Clusters guide.

## Source Code

You can find all included source code in the MongoDB Kubernetes Operator repository.

## Procedure

**Step 1: Add the Helm charts repo.**

```bash
helm repo add jetstack https://charts.jetstack.io --force-update
```

**Step 2: Use Helm to install cert-manager.**

```bash
```

Output:

```
```

**Step 3: Create a certificate issuer.**

```bash
kubectl apply --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -f - <<EOF
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: selfsigned-cluster-issuer
spec:
  selfSigned: {}
EOF

kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" wait --for=condition=Ready clusterissuer selfsigned-cluster-issuer

kubectl apply --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -f - <<EOF
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: my-selfsigned-ca
  namespace: cert-manager
spec:
  isCA: true
  commonName: my-selfsigned-ca
  secretName: root-secret
  privateKey:
    algorithm: ECDSA
    size: 256
  issuerRef:
    name: selfsigned-cluster-issuer
    kind: ClusterIssuer
EOF

kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" wait --for=condition=Ready -n cert-manager certificate my-selfsigned-ca

kubectl apply --context "${K8S_CLUSTER_0_CONTEXT_NAME}" -f - <<EOF
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: my-ca-issuer
spec:
  ca:
    secretName: root-secret
EOF

kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" wait --for=condition=Ready clusterissuer my-ca-issuer
```

**Step 4: Verify creation of the issuer.**

```bash
```

Output:

```
```

**Step 5: Create CA configMap.**

If your Ops Manager TLS certificate is signed by a custom CA, the CA 
certificate must also contain additional certificates that allows the 
agents to download MongoDB binaries from the Internet. To create the TLS 
certificate(s), create a ConfigMap to hold the CA certificate:

```bash
mkdir -p certs

openssl s_client -showcerts -verify 2 \
-connect downloads.mongodb.com:443 -servername downloads.mongodb.com < /dev/null \
| awk '/BEGIN/,/END/{ if(/BEGIN/){a++}; out="certs/cert"a".crt"; print >out}'

kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" get secret root-secret -n cert-manager -o jsonpath="{.data['ca\.crt']}" | base64 --decode > certs/ca.crt
cat certs/ca.crt certs/cert2.crt certs/cert3.crt  >> certs/mms-ca.crt

kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" create cm ca-issuer -n "${MDB_NAMESPACE}" --from-file=ca-pem=certs/mms-ca.crt --from-file=mms-ca.crt=certs/mms-ca.crt
kubectl --context "${K8S_CLUSTER_0_CONTEXT_NAME}" create cm ca-issuer -n "${OM_NAMESPACE}" --from-file=ca-pem=certs/mms-ca.crt --from-file=mms-ca.crt=certs/mms-ca.crt
```
