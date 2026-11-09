<!-- Converted from authentication.txt (reStructuredText). Includes are inlined. -->

# Enable Authentication

The Kubernetes Operator supports X.509, LDAP,
and SCRAM user authentication.

**Note:**

For LDAP configuration, see the
`spec.security.authentication.agents.automationLdapGroupDN`
setting.

   
You must create an additional [CustomResourceDefinition](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/) for your
MongoDB users and the MongoDB Agent instances.
The Kubernetes Operator generates and distributes the certificate.

See the full X.509 certificates configuration examples in the
x509 Authentication directory in
the Authentication
samples directory. This directory also contains sample LDAP and SCRAM configurations.

## Example Deployment CRD

```yaml
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: my-tls-enabled-rs
spec:
  type: ReplicaSet
  members: 3
  version: "8.0.0"
  opsManager:
    configMapRef:
      name: my-configmap-name
  credentials: my-credentials
  security:
    tls:
      enabled: true
    authentication:
      enabled: true
      modes: ["X509"]
      internalCluster: "X509"
```

## Example User CRD

```yaml
apiVersion: mongodb.com/v1
kind: MongoDBUser
metadata:
  name: user-with-roles
spec:
  username: "CN=mms-user-1,OU=cloud,O=MongoDB,L=New York,ST=New York,C=US"
  db: "$external"
  mongodbResourceRef:
    name: my-resource
  roles:
    - db: "admin"
      name: "clusterAdmin"
```

**See also:**

- mongodbuser-specification
- `spec.security.authentication.agents.automationLdapGroupDN`
- Manage Database Users Using X.509 Authentication
- Manage Database Users Using SCRAM Authentication
