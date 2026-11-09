<!-- Converted from tutorial/rotate-x509-to-extensionValue.txt (reStructuredText). Includes are inlined. -->

# Rotate X.509 Certificates to Use Extension Values

**New in version:** 7.0

Cluster members can use X.509 certificates 
for membership authentication to identify other servers in the same deployment. 
This tutorial describes how to perform a rolling update to migrate from using 
certificate Distinguished Name (DN) attributes to using extension values to identify 
members of a cluster. 

When a server configured with the `net.tls.clusterAuthX509.extensionValue` setting
receives a connection request, it compares the the extension value string 
of the presented certificates to the configured values of the 
`extensionValue` setting and
`tlsClusterAuthX509Override` parameter.
If the values match, it treats the connection as a cluster member. 

Clusters adopting new certificates can use the 
`tlsClusterAuthX509Override` parameter to accept X.509 certificates
with different DN attributes during the certificate rotation procedure. Once
all members use certificates with the new value, remove the override to begin
rejecting the now out of date certificates.

## About This Task

Consider a replica set where member certificates,
set using the `clusterFile` and 
`certificateKeyFile` settings, 
have Distinguished Name (DN) attributes that use the `MongoDB` organization
and `MongoDB Server` organizational unit. These DN attributes are set using the
`net.tls.clusterAuthX509.attributes` setting.

```yaml
security:
  clusterAuthMode:      x509
net:
  tls:
    mode:               requireTLS
    certificateKeyFile: /etc/mycerts/10gen-server1.pem
    CAFile:             /etc/mycerts/ca.pem
    clusterFile:        /etc/mycerts/10gen-cluster1.pem
    clusterCAFile:      /etc/mycerts/ca.pem
    clusterAuthX509:
       attributes:      O=MongoDB, OU=MongoDB Server
```

**Note:**

The following procedure assumes that the new X.509 certificates meet
membership certificate and all other requirements and that the cluster configuration 
identifies peer certificates using Distinguished Name (DN) values.
For more information, see x509-member-certificate-requirements.

## Steps

These steps update member certificates to use new X.509 certificates 
on a cluster configured with the 
`attributes` setting.

Initially, the clusters identify members using DN values. 
With the new certificates, the servers instead identify members
using the `mongodb://example.mongodb.net` extension value and ignore certificate attributes.

**Step 1: Update the TLS Cluster Membership Configuration**

Update the configuration file of each server:

* Change the `clusterAuthX509` setting to match 
  the new certificate by replacing the  
  `attributes` setting with the 
  the `extensionValue` setting.

* Set the `tlsClusterAuthX509Override` parameter to use the
  DN attributes of the old certificate.

For example: 

```yaml
net:
  tls:
    mode:               requireTLS
    certificateKeyFile: /etc/mycerts/mongodb-server1.pem
    CAFile:             /etc/mycerts/ca.pem
    clusterFile:        /etc/mycerts/mongodb-cluster1.pem
    clusterCAFile:      /etc/mycerts/ca.pem
    clusterAuthX509:
       extensionValue:  mongodb://example.mongodb.net
security:
  clusterAuthMode: x509
setParameter:
   tlsClusterAuthX509Override: "{ attributes: 'O=MongoDB, OU=MongoDB Server' }"
```

**Step 2: Restart Secondary Cluster Members**

Restart each secondary cluster member:

#. Use `mongosh` to connect to each secondary cluster member,
   then use the `db.shutdownServer` method to stop the server:

   ```javascript
   use admin
   db.shutdownServer()
   ```

#. Restart the server.

#. Use the `rs.status` method to determine the member state:

   ```javascript
   rs.status().members
   ```

#. Wait for the `stateStr` field for this member to show a value of
   `SECONDARY`, then restart the next secondary.

Secondary servers in the replica set now accept peer connections from
members using certificates with the new extension values as well as 
the old DN attributes.

**Step 3: Restart Primary Cluster Member**

Restart the primary member:

#. Connect to the primary using `mongosh`, then use the
   `rs.stepDown` method to step the member down as the
   primary:

   ```javascript
   rs.stepDown()    
   ```

   The cluster promotes a secondary with the new certificate to serve
   as the new primary.

#. Use the `db.shutdownServer` method to shut the server down:

   ```javascript
   use admin
   db.shutdownServer()
   ```

#. Restart the server. 

The primary server in the replica set steps down and restarts as a
secondary that now accepts peer connections from members using
certificates with the new extension value as well as the old DN
attributes.

**Step 4: Update the TLS Certificates**

Update the configuration file of each server:

* Change the `net.tls.certificateKeyFile` setting to use the 
  new certificate.

* Change the `net.tls.clusterFile` setting to use the 
  new certificate.

For example:

```yaml
net:
  tls:
    mode:               requireTLS
    certificateKeyFile: /etc/mycerts/mongodb-server2.pem
    CAFile:             /etc/mycerts/ca.pem
    clusterFile:        /etc/mycerts/mongodb-cluster2.pem
    clusterCAFile:      /etc/mycerts/ca.pem
    clusterAuthX509:
       extensionValue:  mongodb://example.mongodb.net
security:
  clusterAuthMode: x509
setParameter:
   tlsClusterAuthX509Override: "{ attributes: 'O=MongoDB, OU=MongoDB Server' }"
```

**Step 5: Restart Secondary Cluster Members**

Restart each secondary cluster member:

#. Use `mongosh` to connect to each secondary cluster member,
   then use the `db.shutdownServer` method to stop the server:

   ```javascript
   use admin
   db.shutdownServer()
   ```

#. Restart the server.

#. Use the `rs.status` method to determine the member state:

   ```javascript
   rs.status().members
   ```

#. Wait for the `stateStr` field for this member to show a value of
   `SECONDARY`, then restart the next secondary.

Secondary servers in the replica set now use the new X.509 certificates.

**Step 6: Restart Primary Cluster Member**

Restart the primary member:

#. Connect to the primary using `mongosh`, then use the
   `rs.stepDown` method to step the member down as the
   primary:

   ```javascript
   rs.stepDown()    
   ```

   The cluster promotes a secondary with the new certificate to serve
   as the new primary.

#. Use the `db.shutdownServer` method to shut the server down:

   ```javascript
   use admin
   db.shutdownServer()
   ```

#. Restart the server. 

The primary server in the replica set steps down and restarts as a 
secondary that uses the new X.509 certificate. 

**Step 7: Remove the DN Certification Override Configuration**

With all members of the cluster now using the new X.509 certificate, 
update the configuration file to remove the `setParameter` 
settings for the `tlsClusterAuthX509Override` parameter.

For example:

```yaml
net:
  tls:
    mode:               requireTLS
    certificateKeyFile: /etc/mycerts/mongodb-server1.pem
    CAFile:             /etc/mycerts/ca.pem
    clusterFile:        /etc/mycerts/mongodb-cluster1.pem
    clusterCAFile:      /etc/mycerts/ca.pem
    clusterAuthX509:
       extensionValue:  mongodb://example.mongodb.net
security:
  clusterAuthMode: x509
```

This ensures that the server doesn't configure the old certificate
settings on startup.

**Step 8: Restart Secondary Cluster Members**

Restart each secondary cluster member:

#. Use `mongosh` to connect to each secondary cluster member,
   then use the `db.shutdownServer` method to stop the server:

   ```javascript
   use admin
   db.shutdownServer()
   ```

#. Restart the server.

#. Use the `rs.status` method to determine the member state:

   ```javascript
   rs.status().members
   ```

#. Wait for the `stateStr` field for this member to show a value of
   `SECONDARY`, then restart the next secondary.

Secondary servers in the replica set restart and no longer accept
connections from the old X.509 certificates.

**Step 9: Restart Primary Cluster Member**

Restart the primary member:

#. Connect to the primary using `mongosh`, then use the
   `rs.stepDown` method to step the member down as the
   primary:

   ```javascript
   rs.stepDown()    
   ```

   The cluster promotes a secondary with the new certificate to serve
   as the new primary.

#. Use the `db.shutdownServer` method to shut the server down:

   ```javascript
   use admin
   db.shutdownServer()
   ```

#. Restart the server. 

The primary server steps down and restarts as a secondary that no longer
accepts connections from the old X.509 certificates.

## Learn More

* security-auth-x509
* x509-internal-authentication
* upgrade-to-x509-internal-authentication
* x509-rotate-member-certs
