<!-- Converted from tutorial/cert-manager-integration.txt (reStructuredText). Includes are inlined. -->

# Set Up a cert-manager Integration

[cert-manager](https://cert-manager.io/) simplifies and automates
the management of security certificates for Kubernetes. The following 
procedure describes how to configure `cert-manager` to generate
certificates for MongoDB Kubernetes Operator resources.

## Prerequisites

**encrypted:**

To deploy a replica set using an [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/), you must:

- Have or create an `Ops Manager instance` or a `Cloud Manager organization`.

- Have or install the MongoDB Controllers for Kubernetes Operator.

- Create or generate a Kubernetes Operator ConfigMap.

- Create credentials for the Kubernetes Operator or 
  configure a different secret storage tool.

**Note:**

To avoid storing secrets in single-cluster Kubernetes deployments, you can
migrate all [secrets](https://kubernetes.io/docs/concepts/configuration/secret/) to a secret storage tool.
Deployments on multiple Kubernetes clusters don't support storing secrets
in secret storage tools, such as [HashiCorp Vault](https://www.vaultproject.io/).

- Generate one TLS (Transport Layer Security) certificate for each of the following components:

  - Your replica set. Ensure that you add SAN (Subject Alternative Name)\s for each Kubernetes pod 
    that hosts a member of your replica set to the certificate. 

    In your TLS (Transport Layer Security) certificate, the SAN (Subject Alternative Name) for each pod must use the 
    following format:

    ```none
    <pod-name>.<metadata.name>-svc.<namespace>.svc.cluster.local
    ```

    **Important:**

    If you're using an ACME (Automatic Certificate Management Environment) based service provider such as [Let's Encrypt](https://letsencrypt.org) to issue TLS (Transport Layer Security) certificates, the provider 
    might prohibit you from adding the Pod's default FQDN (fully qualified domain name)\s (`*.svc.cluster.local`)
    to SAN (Subject Alternative Name)\s in the certificate.

    To use an ACME (Automatic Certificate Management Environment) based certificate, you must configure 
    the certificate for your replica set resource. 
    To learn more, see the step about ACME (Automatic Certificate Management Environment) based TLS (Transport Layer Security) 
    certificates in the procedure.

  - Your project's MongoDB Agent. For the MongoDB Agent certificate, 
    ensure that you meet the following requirements:

    - The Common Name in the TLS (Transport Layer Security) certificate is not empty.
    - The combined Organization and Organizational Unit in each TLS (Transport Layer Security)
      certificate differs from the Organization and
      Organizational Unit in the TLS (Transport Layer Security) certificate for your
      replica set members.

- You must have the CA (Certificate Authority) certificate file and name it `ca-pem`.
- You must have the key that you used to sign your TLS (Transport Layer Security) certificates.

**Important:**

The Kubernetes Operator uses `kubernetes.io/tls` secrets
to store TLS (Transport Layer Security) certificates and private keys for Ops Manager and MongoDB
resources. Starting in Kubernetes Operator version 1.17.0, the 
Kubernetes Operator doesn't support concatenated PEM (Privacy-Enhanced Mail) files stored as
`Opaque secrets`.

**non-encrypted:**

To deploy a replica set using an [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/), you must:

- Have or create an `Ops Manager instance` or a `Cloud Manager organization`.

- Have or install the MongoDB Controllers for Kubernetes Operator.

- Create or generate a Kubernetes Operator ConfigMap.

- Create credentials for the Kubernetes Operator or 
  configure a different secret storage tool.

**Note:**

To avoid storing secrets in single-cluster Kubernetes deployments, you can
migrate all [secrets](https://kubernetes.io/docs/concepts/configuration/secret/) to a secret storage tool.
Deployments on multiple Kubernetes clusters don't support storing secrets
in secret storage tools, such as [HashiCorp Vault](https://www.vaultproject.io/).

## Procedure

**Step 1: Create a CA (Certificate Authority) secret.**

**Note:**

The following steps assume that you have already created a custom
CA (Certificate Authority) along with the corresponding `tls.key` private key 
and `tls.crt` signed certificate.

Create a secret to store your CA (Certificate Authority) data:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: ca-key-pair
  namespace: <namespace>
data:
  tls.crt: <your-CA-certificate>
  tls.key: <your-CA-private-key>
```

**Step 2: Add additional certificates to custom CA (Certificate Authority) certificates.**

If your Ops Manager TLS (Transport Layer Security) certificate is signed by a custom CA (Certificate Authority), 
the CA (Certificate Authority) certificate must also contain
additional certificates that allow Ops Manager Backup Daemon to download
MongoDB binaries from the Internet. To create the TLS (Transport Layer Security)
certificate(s), create a [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) to hold the CA (Certificate Authority)
certificate: 

**Important:**

The Kubernetes Operator requires that your Ops Manager certificate is named
`mms-ca.crt` in the ConfigMap. 

a. Obtain the entire TLS (Transport Layer Security) certificate chain for Ops Manager from
   `downloads.mongodb.com`. The following `openssl` command
   outputs the certificate in the chain to your current working
   directory, in `.crt` format:

   ```sh
   openssl s_client -showcerts -verify 2 \
   -connect downloads.mongodb.com:443 -servername downloads.mongodb.com < /dev/null \
   | awk '/BEGIN/,/END/{ if(/BEGIN/){a++}; out="cert"a".crt"; print >out}'
   ```

#. Concatenate your CA (Certificate Authority)\'s certificate file for Ops Manager
   with the entire TLS (Transport Layer Security) certificate chain from 
   `downloads.mongodb.com` that
   you obtained in the previous step:

   ```sh
   cat <custom_ca_cert.pem> cert2.crt cert3.crt cert4.crt  >> mms-ca.crt
   ```

   **Note:**

   - Replace the placeholder `<custom_ca_cert.pem>` with your custom CA certificate PEM file. 
   - Don't include your `cert1.crt` file, as it is your server certificate from 
     MongoDB that shouldn't be included.

#. Create the [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) for Ops Manager:

   ```sh
   kubectl create configmap om-http-cert-ca --from-file="mms-ca.crt"
   ```

**Step 3: Configure a cert-manager CA (Certificate Authority) issuer**

a. Create a CA (Certificate Authority) issuer that references your CA (Certificate Authority) secret:

   ```yaml
   apiVersion: cert-manager.io/v1
   kind: Issuer
   metadata: 
     name: ca-issuer
     namespace: <namespace>
   spec:
     ca:
       secretName: ca-key-pair
   ```

#. Verify that the issuer is ready:

   ```sh
   kubectl get issuer ca-issuer
   ```

   The `READY` field in the output should have a value of `True`.

**Step 4: Create a CA (Certificate Authority) ConfigMap**

Create a ConfigMap containing your CA (Certificate Authority). It must have two 
fields, `ca-pem` and `mms-ca.crt`, both pointing to your
CA (Certificate Authority) certificate. Replace `<CA-certificate>` with the path to your 
CA (Certificate Authority) certificate.

```sh
kubectl create cm ca-issuer --from-file=ca-pem=<CA-certificate> \
--from-file=mms-ca.crt=<CA-certificate>
```

**Step 5: Create certificates for your MongoDB resources**

To secure a MongoDB resource with your generated certification, you
must create certificates for both the resource itself and the MongoDB
agent. 

a. Create the MongoDB resource certificate. The following example 
   assumes a replica set named `my-replica-set` with three members:

   **Note:**

   The `spec.issuerRef.name` parameter references the previously 
   created CA (Certificate Authority) ConfigMap.

   ```yaml
   apiVersion: cert-manager.io/v1
   kind: Certificate
   metadata:
     name: my-replica-set-certificate
     namespace: mongodb
   spec:
     dnsNames:
     - my-replica-set-0
     - my-replica-set-0.my-replica-set-svc.mongodb.svc.cluster.local
     - my-replica-set-1
     - my-replica-set-1.my-replica-set-svc.mongodb.svc.cluster.local
     - my-replica-set-2
     - my-replica-set-2.my-replica-set-svc.mongodb.svc.cluster.local
     duration: 240h0m0s
     issuerRef:
       name: ca-issuer
     renewBefore: 120h0m0s
     secretName: mdb-my-replica-set-cert
     usages:
     - server auth
     - client auth
   ```

   For sharded clusters, you must create one certificate for each
   [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/). To learn more about sharded cluster 
   configuration, see deploy-sharded-cluster.

#. Create the MongoDB agent certificate:

   **Note:**

   The `spec.issuerRef.name` parameter references the previously 
   created CA (Certificate Authority) ConfigMap.

   ```yaml
   apiVersion: cert-manager.io/v1
   kind: Certificate
   metadata:
     name: agent-certs
     namespace: mongodb
   spec:
     commonName: automation
     dnsNames:
     - automation
     duration: 240h0m0s
     issuerRef:
       name: ca-issuer
     renewBefore: 120h0m0s
     secretName: mdb-my-replica-set-agent-certs
     usages:
     - digital signature
     - key encipherment
     - client auth          
     subject:
       countries:
       - US
       localities:
       - NY
       organizationalUnits:
       - a-1635241837-m5yb81lfnrz
       organizations:
       - cluster.local-agent
       provinces:
       - NY
   ```

#. Create the MongoDB resource:

   **Note:**

   If you leave the `spec.security.tls.ca` 
   parameter unspecified, it defaults to `{replica-set}-ca`.

   ```yaml
   apiVersion: mongodb.com/v1
   kind: MongoDB
   metadata:
     name: my-replica-set
     namespace: mongodb
   spec:
     type: ReplicaSet

     members: 3
     version: 8.0.0

     opsManager:
       configMapRef:
         name: my-project
     credentials: my-credentials

     security:
       certsSecretPrefix: mdb
       authentication:
         enabled: true
         modes:
         - X509
       tls:
         ca: ca-issuer
         enabled: true
   ```

**Step 6: Create certificates for Ops Manager and AppDB with TLS**

To secure an Ops Manager resource, you must first create certificates
for Ops Manager and AppDB, then create the Ops Manager resource.

a. Create the Ops Manager certificate:

   **Note:**

   The `spec.issuerRef.name` parameter references the previously 
   created CA (Certificate Authority) ConfigMap.

   ```yaml
   apiVersion: cert-manager.io/v1
   kind: Certificate
   metadata:
     name: cert-for-ops-manager
     namespace: mongodb
   spec:
     dnsNames:
     - om-with-https-svc.mongodb.svc.cluster.local
     duration: 240h0m0s
     issuerRef:
       name: ca-issuer
     renewBefore: 120h0m0s
     secretName: mdb-om-with-https-cert
     usages:
     - server auth
     - client auth
   ```

#. Create the AppDB certificate:

   **Note:**

   The `spec.issuerRef.name` parameter references the previously 
   created CA (Certificate Authority) ConfigMap.

   ```yaml
   apiVersion: cert-manager.io/v1
   kind: Certificate
   metadata:
     name: appdb-om-with-https-db-cert
     namespace: mongodb
   spec:
     dnsNames:
     - om-with-https-db-0
     - om-with-https-db-0.om-with-https-db-svc.mongodb.svc.cluster.local
     - om-with-https-db-1
     - om-with-https-db-1.om-with-https-db-svc.mongodb.svc.cluster.local
     - om-with-https-db-2
     - om-with-https-db-2.om-with-https-db-svc.mongodb.svc.cluster.local
     duration: 240h0m0s
     issuerRef:
       name: ca-issuer
     renewBefore: 120h0m0s
     secretName: appdb-om-with-https-db-cert
     usages:
     - server auth
     - client auth
   ```

#. Create the Ops Manager resource:

   ```yaml
   apiVersion: mongodb.com/v1
   kind: MongoDBOpsManager
   metadata:
     name: om-with-https
     namespace: mongodb
   spec:
     adminCredentials: ops-manager-admin-secret
     version: "8.0.0"
     applicationDatabase:
       members: 3
       security:
         certsSecretPrefix: appdb
         tls:
           ca: ca-issuer
       version: 8.0.0-ubi8
     replicas: 1
     security:
       certsSecretPrefix: mdb
       tls:
         ca: ca-issuer
   ```

## Renewing Certificates

cert-manager will renew certificates under the following circumstances:

- The certificate expires according to its `spec.duration` and 
  `spec.renewBefore` fields.
- You delete the secret holding a certificate. In this case, 
  cert-manager recreates the secret according to the configuration 
  in your certificate custom resource.
- You alter the configuration of the certificate custom resource.
  In this case, cert-manager recreates the secret that contains the 
  certificate when it detects the changes to its configuration.
