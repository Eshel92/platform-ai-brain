<!-- Converted from core/tls/configure-server-tls-tutorial.txt (reStructuredText). Includes are inlined. -->

# Configure TLS on Self-Managed Deployments

This tutorial shows you how to configure TLS (Transport Layer Security) on a
self-managed replica set. Select an approach based on whether
you want to use intra-cluster mTLS (Mutual TLS), which is
required to enable X.509 authentication between nodes.

**Important:**

These steps apply to self-managed MongoDB deployments.
MongoDB Atlas clusters use TLS (Transport Layer Security) by default. If you use Cloud Manager or Ops Manager,
configure TLS through your deployment management tool.

## Before You Begin

Before you start, verify that you have the following:

- A self-managed replica set in which each node has a hostname, such as
  `localhost` or `mongo0.example.com`. TLS is not currently
  configured on any node in the replica set.

- TLS server certificates for each node that you obtained by following the
  Obtain Server Certificates tutorial, such
  as `mongo0.pem`.

- A CA certificate to sign the server certificates, such as `ca.pem`.

- Access to the `mongod` configuration file on each node.

- Access to `mongosh`.

## Steps

**server-tls-without-mtls:**

Follow this procedure if you do not need intra-cluster mTLS or X.509 
authentication between server nodes.

**Step 1: Create a keyfile**

Each node uses the contents of a keyfile to authenticate other
members of the deployment. Create a keyfile using the following command:

```shell
openssl rand -base64 756 > /etc/ssl/mongodb/keyfile
chmod 400 /etc/ssl/mongodb/keyfile
```

Copy the keyfile to each node in your deployment. Ensure that you
restrict permissions on the keyfile so that only the `mongod` process
can read the file.

**Step 2: Edit the configuration file on each node**

On **each node,** locate and open your `mongod`
configuration file. If the file does not exist, create it.
Add the following TLS options. 
Use absolute paths to
the certificate files.

For example, the configuration file for your primary node 
looks like the following:

```yaml
net:
  tls:
    mode: allowTLS
    certificateKeyFile: /etc/ssl/mongodb/mongo0.pem
    CAFile: /etc/ssl/mongodb/ca.pem
    allowConnectionsWithoutCertificates: true

security:
  clusterAuthMode: keyFile
  keyFile: /etc/ssl/mongodb/keyfile

setParameter:
  tlsWithholdClientCertificate: true
```

- `mode` set to `allowTLS` accepts TLS
  connections but does not require them, so nodes can
  complete a rolling restart without interrupting replication.
- .. include:: /includes/tls/configure-server-deployment/info-cert-and-ca-file.rst
- `allowConnectionsWithoutCertificates`
  allows clients to connect without providing a TLS
  certificate.
- `clusterAuthMode` set to `keyFile` enables
  nodes to authenticate using a keyfile. `keyFile`
  specifies the keyfile that nodes use to authenticate to
  each other.
- `tlsWithholdClientCertificate` prevents the node
  from presenting its server certificate when making outbound
  connections to other nodes in the cluster. This is necessary
  because it prevents nodes from using server-authentication certificates
  for client authentication, especially if your certificates do not 
  include the `clientAuth` EKU. 

**Step 3: Restart the replica set members**

Restart the `mongod` process to apply the new TLS configuration.
To apply the configuration without downtime, restart nodes in a rolling fashion.

On each host for your deployment, starting with the secondary nodes
and finishing with the primary node, run the following: 

```sh
sudo systemctl restart mongod
```

To verify that the rolling restart completed successfully, run the following 
command on each host: 

```sh
sudo systemctl status mongod
```

**Step 4: Update the configuration to enforce TLS**

After all nodes restart successfully with TLS enabled, update
the configuration file on each node. Change
`net.tls.mode` from `allowTLS` to `requireTLS` to
enforce encrypted connections for all clients and members:

```yaml
net:
  tls:
    mode: requireTLS
```

**Step 5: Restart the replica set members**

Restart the `mongod` process to apply the new TLS configuration.
To apply the configuration without downtime, restart nodes in a rolling fashion.

On each host for your deployment, starting with the secondary nodes
and finishing with the primary node, run the following: 

```sh
sudo systemctl restart mongod
```

To verify that the rolling restart completed successfully, run the following 
command on each host: 

```sh
sudo systemctl status mongod
```

**server-tls-with-mtls:**

Follow this procedure to configure your replica set to use intra-cluster
mTLS and X.509 authentication between nodes.

**Step 1: Edit the configuration file on each node**

**Important:**

Your node certificates must include both `serverAuth` and
`clientAuth` EKU for intra-cluster mTLS. 
If your certificates do not include `clientAuth`, see the [Public Certificate Authority Policy Changes Affecting mTLS](https://www.mongodb.com/resources/products/alerts/public-certificate-authority-policy-changes-affecting-mtls/)
Technical Advisory for alternative configuration options.

On **each node,** locate and open your `mongod`
configuration file. If the file does not exist, create it.
Add the following TLS options. 
Use absolute paths to
the certificate files.

For example, the configuration file for your primary node 
looks like the following:

```yaml
net:
  tls:
    mode: allowTLS
    certificateKeyFile: /etc/ssl/mongodb/mongo0.pem
    CAFile: /etc/ssl/mongodb/ca.pem
    allowConnectionsWithoutCertificates: true
    clusterAuthX509:
      attributes: O=MongoDB

security:
  clusterAuthMode: x509
```

- `mode` set to `allowTLS` accepts TLS
  connections but does not require them, so nodes can
  complete a rolling restart without interrupting replication.
- .. include:: /includes/tls/configure-server-deployment/info-cert-and-ca-file.rst
- `allowConnectionsWithoutCertificates`
  allows clients to connect without providing a TLS
  certificate.
- `net.tls.clusterAuthX509.attributes` specifies the
  X.509 certificate attributes that identify a node as a
  cluster member, rather than a regular client. For required
  certificate attributes, see x509-member-certificate.
- `clusterAuthMode` set to `x509` enables
  nodes to authenticate using X.509 certificates.

**Step 2: Restart the replica set members**

Restart the `mongod` process to apply the new TLS configuration.
To apply the configuration without downtime, restart nodes in a rolling fashion.

On each host for your deployment, starting with the secondary nodes
and finishing with the primary node, run the following: 

```sh
sudo systemctl restart mongod
```

To verify that the rolling restart completed successfully, run the following 
command on each host: 

```sh
sudo systemctl status mongod
```

**Step 3: Update the configuration to enforce TLS**

After all nodes restart successfully with TLS enabled, update
the configuration file on each node. Change
`net.tls.mode` from `allowTLS` to `requireTLS` to
enforce encrypted connections for all clients and members:

```yaml
net:
  tls:
    mode: requireTLS
```

**Step 4: Restart the replica set members**

Restart the `mongod` process to apply the new TLS configuration.
To apply the configuration without downtime, restart nodes in a rolling fashion.

On each host for your deployment, starting with the secondary nodes
and finishing with the primary node, run the following: 

```sh
sudo systemctl restart mongod
```

To verify that the rolling restart completed successfully, run the following 
command on each host: 

```sh
sudo systemctl status mongod
```

**Step 5: Inspect logs to verify your TLS configuration**

After the rolling restart completes, inspect the logs on each
node to verify that TLS is configured correctly. Your logs
must include the following content to verify that mTLS and
X.509 authentication are correctly configured:

```json
"msg":"Successfully authenticated",
"attr": {
  "isClusterMember":true,
  "mechanism":"MONGODB-X509",
  "user":"CN=mongo1.example.com,O=MongoDB,L=New York City,ST=New-York,C=US"
}
```

You should see a similar log message for each of the other
two nodes in your replica set. For example, if you look at
the logs on `mongo0`, you should see messages similar to
the above for `mongo1` and `mongo2`.

## Next Steps

To learn how to connect to your deployment 
with a client application, continue to configure-client-tls-tutorial.
