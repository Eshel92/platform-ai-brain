<!-- Converted from encryption-at-rest.txt (reStructuredText). Includes are inlined. -->

# Configure KMIP (Key Management Interoperability Protocol) Encryption at Rest

   

You can configure encryption at rest 
for a MongoDB deployment managed by the Kubernetes Operator
by using a KMIP (Key Management Interoperability Protocol) server.

## Considerations

Before configuring encryption at rest, consider the following:

- You must have a running KMIP (Key Management Interoperability Protocol) server.
- You can't transition your deployment that uses keyfile-based encryption 
  at rest to KMIP (Key Management Interoperability Protocol)-based encryption at rest.
- If you want to enable KMIP (Key Management Interoperability Protocol) encryption at rest for an already deployed MongoDB 
  resource, contact [MongoDB Support](https://support.mongodb.com/welcome).

## Procedure

The following procedure describes how to configure
a sample KMIP (Key Management Interoperability Protocol) configuration for a MongoDB replica set.
Adjust the file names and paths, Kubernetes namespace, resource names,
and MongoDB version as necessary for your deployment.

**Step 1: Create the ConfigMap of the CA (Certificate Authority).**

Run the following command to create a [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/)
to hold the CA (Certificate Authority) that signed the KMIP (Key Management Interoperability Protocol) server's certificate:

```
kubectl -n mongodb create configmap mongodb-kmip-certificate-authority-pem --from-file=ca.pem
```

**Step 2: Create the Secret for the Client Certificate and Private Key PEM.**

Run the following command to create a [secret](https://kubernetes.io/docs/concepts/configuration/secret/) to hold the 
concatenated client certificate and private key for checking out 
the master key from the KMIP (Key Management Interoperability Protocol) server:

```
kubectl -n mongodb create secret generic mongodb-kmip-client-pem --from-file=cert.pem
```

**Step 3: Configure the deployment to use the KMIP (Key Management Interoperability Protocol) server.**

Configure the `additionalMongodConfig` settings
in your [custom resource](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) specification to use the KMIP (Key Management Interoperability Protocol) 
server. For example:

```yaml
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: kmip
  namespace: mongodb
spec:
  type: ReplicaSet
  members: 3
  backup:
    encryption:
      kmip:
        client:
          clientCertificatePrefix: "mdb"
  additionalMongodConfig:
    security:
      enableEncryption: true
      kmip:
        clientCertificateFile: /kmip/cert/cert.pem
        serverCAFile: /kmip/ca/ca.pem
        serverName: pykmip-server.pymongo
        port: 5696
  featureCompatibilityVersion: '8.0'
  version: 8.0.0
  opsManager:
    configMapRef:
      name: my-project
  credentials: my-credentials
  podSpec:
    podTemplate:
      spec:
        containers:
          - name: mongodb-enterprise-database
            volumeMounts:
              - name: mongodb-kmip-client-pem
                mountPath: /kmip/cert
              - name: mongodb-kmip-certificate-authority-pem
                mountPath: /kmip/ca
        volumes:
          - name: mongodb-kmip-client-pem
            secret:
              secretName: mongodb-kmip-client-pem
          - name: mongodb-kmip-certificate-authority-pem
            configMap:
              name: mongodb-kmip-certificate-authority-pem
              items:
                - key: ca.pem
                  path: ca.pem
```

**Important:**

If you set the `spec.backup.encryption.kmip` setting
in your resource, the API (Application Programming Interface) keys linked with 
the value of `spec.credentials` must have the `Global Owner` role.
