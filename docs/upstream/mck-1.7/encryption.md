<!-- Converted from encryption.txt (reStructuredText). Includes are inlined. -->

# Configure Encryption

## Enable HTTPS

The Kubernetes Operator supports configuring Ops Manager to run over 
HTTPS.

Enable HTTPS (Hypertext Transfer Protocol Secure) before deploying your Ops Manager resources to avoid a situation 
where the Kubernetes Operator reports your resources' status as `Failed`.

**See also:**

- https-enablement-issues

## Enable TLS

The Kubernetes Operator supports TLS (Transport Layer Security) encryption.
Use TLS (Transport Layer Security) with your MongoDB deployment to encrypt your data over
the network.

The configuration in the following example enables TLS (Transport Layer Security) for the replica
set. When TLS (Transport Layer Security) is enabled, all traffic between members of the replica
set and clients is encrypted using TLS (Transport Layer Security) certificates.

To learn more about securing your MongoDB deployments using TLS (Transport Layer Security), see 
secure-tls.

The default TLS (Transport Layer Security) mode is `requireTLS`. You can customize it using the
`spec.additionalMongodConfig.net.ssl.mode` configuration
parameter, as shown in the following abbreviated example.

```yaml
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
name: my-tls-enabled-rs
spec:
  type: ReplicaSet
  members: 3
  version: 8.0.0

 opsManager:
   configMapRef:
     name: my-project
 credentials: my-credentials

 security:
   tls:
     enabled: true
     ca: <custom-ca>

 ...
 additionalMongodConfig:
   net:
     ssl:
      mode: "preferSSL"
```

See the full TLS (Transport Layer Security) configuration example in
replica-set.yaml
in the TLS
samples directory. This directory also contains sample TLS (Transport Layer Security) configurations for
sharded clusters and standalone deployments.
