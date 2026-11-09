<!-- Converted from tutorial/create-x509-client-certs.txt (reStructuredText). Includes are inlined. -->

# Generate X.509 Client Certificates

The MongoDB Controllers for Kubernetes Operator can deploy MongoDB instances with 
X.509 authentication
enabled. If X.509 authentication has been enabled for the deployment,
you must generate and use an X.509 certificate to connect to the
deployment. This new client certificate must be signed by the
same CA (Certificate Authority) that signs the server certificates for the MongoDB
deployment to accept it.

Use the procedure outlined in this document to use an X.509 certificate
to connect to your X.509-enabled MongoDB deployment.

If you're using [HashiCorp Vault](https://www.vaultproject.io/) as your secret storage tool, 
you can Create a Vault Secret instead.

**Note:**

To automate certificate renewal for Ops Manager deployments, consider setting up the cert-manager integration.

## Prerequisites

**Note:**

A full description of Transport Layer Security (TLS), Public Key Infrastructure (PKI)
certificates, and Certificate Authorities is beyond the scope of this
document. This page assumes prior knowledge of TLS (Transport Layer Security) and
X.509 authentication.

- To complete this tutorial, you must have the MongoDB Controllers for Kubernetes Operator
  installed. For instructions on installing the Kubernetes Operator, 
  see install-k8s.

- This tutorial assumes you have a MongoDB deployment which
  requires X.509 authentication. For instructions on deploying
  MongoDB resources, see k8s-deploy-mdb-resources.

## Procedure

First create the client certificate. Then create a MongoDB user
and connect to the X.509-enabled deployment.

**Step 1: Generate an X.509 client certificate.**

For production use, your MongoDB deployment should use valid
certificates generated and signed by a CA (Certificate Authority). You or your
organization can generate and maintain an independent CA (Certificate Authority) using
Kubernetes\-native tools such as 
[cert-manager](https://cert-manager.io/docs/).

Obtaining and managing certificates is beyond the scope of this
documentation.

**Important:**

You must concatenate your client's TLS (Transport Layer Security) certificate and the
certificate's key in a `.pem` file. You must present this
`.pem` file when you connect to your X.509-enabled MongoDB
deployment.

To learn about the properties that your client certificates must have,
see Client Certificate Requirements
in the MongoDB Manual.

**Step 2: Configure `kubectl` to default to your namespace.**

If you have not already, run the following command to execute all 
`kubectl` commands in the namespace you created.

**Note:**

If you are deploying an Ops Manager resource in a multi-Kubernetes cluster MongoDB deployment:

- Set the `context` to the name of the central cluster, such as:
  `kubectl config set context "$MDB_CENTRAL_CLUSTER_FULL_NAME"`.

- Set the `--namespace` to the same scope
  that you used for your multi-Kubernetes cluster MongoDB deployment, such as: `kubectl config --namespace "mongodb"`.

```sh
kubectl config set-context $(kubectl config current-context) --namespace=<metadata.namespace>
```

**Step 3: Copy and save the following example [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/).**

Save the following ConfigMap as `x509-mongodb-user.yaml`:

```none
---
apiVersion: mongodb.com/v1
kind: MongoDBUser
metadata:
  name: new-x509-user
spec:
  username: "CN=my-x509-authenticated-user,OU=organizationalunit,O=organization"
  db: "$external"
  mongodbResourceRef:
    name: '<name of the MongoDB resource>'
  roles:
    - db: "admin"
      name: "readWriteAnyDatabase"
```

This ConfigMap `.yaml` file describes a `MongoDBUser` custom object. You
can use these custom objects to create MongoDB users. To learn more, see mongodbuser-specification.

In this example, the ConfigMap describes the user as an X.509
user that the client can use to connect to MongoDB with the
corresponding X.509 certificate.

**Step 4: Create the X.509 MongoDB user.**

Run the following command to apply the ConfigMap and create the
X.509 MongoDB user:

```sh
kubectl apply -f x509-mongodb-user.yaml
```

You should see an output similar to the following:

```sh
mongodbuser.mongodb.com/new-x509-user created
```

**Step 5: Verify your newly created user**

Run the following command to check the state of the `new-x509-user`:

```sh
kubectl get mdbu/new-x509-user -o yaml
```

You should see an output similar to the following:

```sh
NAME            CREATED AT
new-x509-user   8m
```

**Step 6: Find the mount location of the CA (Certificate Authority).**

Run the following command to find where in each pod the Kubernetes Operator
mounted the CA (Certificate Authority) secret:

```sh
kubectl get statefulset <metadata.name> -o yaml
```

In the output, find the `secret-ca` mount:

```yaml
volumeMounts:
  - mountPath: /opt/scripts
    name: database-scripts
    readOnly: true
  - mountPath: /var/lib/mongodb-automation/secrets/ca
    name: secret-ca
    readOnly: true
  - mountPath: /var/lib/mongodb-automation/secrets/certs
    name: secret-certs
    readOnly: true
```

In the following step when you connect to your database deployment,
append `secret-ca` to the `mountPath`, which forms the full path:

```sh
/var/lib/mongodb-automation/secrets/ca/secret-ca
```

**Step 7: Use your X.509 user to connect to the MongoDB deployment**

Once you have created your X.509 user, try to connect to the
deployment using the MongoDB Shell (`mongosh`):

```sh
mongosh --host {host} --port {port} --tls \
  --tlsCAFile </path/to/secret-ca> \
  --tlsCertificateKeyFile <your-cert>.pem \
  --authenticationMechanism MONGODB-X509  \
  --authenticationDatabase '$external'
```
