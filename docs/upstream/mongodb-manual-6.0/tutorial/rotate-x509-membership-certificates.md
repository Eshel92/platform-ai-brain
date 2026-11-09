<!-- Converted from tutorial/rotate-x509-membership-certificates.txt (reStructuredText). Includes are inlined. -->

# Rolling Update of X.509 Certificates that Contain New DN on Self-Managed Clusters

Members of a replica set or a sharded cluster can use X.509
certificates for membership authentication to
identify other servers in the same deployment.
   
When a server node receives a connection request, it compares the Distinguished Name (DN)
attributes in the `subject` field of the presented certificates to the subject DN attributes of its own certificates. 
The certificates match if their subjects contain the same values for the Organization (`O`), Organizational Unit (`OU`), 
and Domain Component (`DC`) attributes. 
A server's configuration file can also specify alternative DN attributes to use for matching in the 
`tlsX509ClusterAuthDNOverride` parameter.
If the server's subject DN attributes or configured `tlsX509ClusterAuthDNOverride` value 
match the subject DN attributes of the presented certificate, the server node treats the 
connection as a cluster member.  

In some situations, you may need to update the member certificates to
new certificates with new subject Distinguished Name (DN) attributes, such as if
an organization changes its name. 
In a rolling update, member certificates are updated one at a time, and
your deployment does not incur any downtime. 

Clusters adopting new certificates can use the `tlsX509ClusterAuthDNOverride` parameter to accept x.509 
certificates with different subject DN attributes during the certificate rotation procedure.
Once all members use certificates with the new value, remove the override to begin rejecting the now out of date certificates.

## About This Task

Consider a replica set where each member's X.509 certificates, 
set using the `clusterFile` and `certificateKeyFile` settings,  
have subject DN attributes of `"OU=10gen Server,O=10gen"`. 

A member of this replica set has the following configuration file: 

```yaml
net.tls.mode: requireTLS
net.tls.certificateKeyFile: "./mycerts/10gen-server1.pem"
net.tls.CAFile: "./mycerts/ca.pem"

security.clusterAuthMode: x509
net.tls.clusterFile:  "./mycerts/10gen-cluster1.pem"
net.tls.clusterCAFile: "./mycerts/ca.pem"
```

The following procedure updates each member's certificates to new certificates that have
subject DN attributes of `"OU=MongoDB Server, O=MongoDB"`.

**Note:**

The following procedure assumes that the new X.509 certificates meet
membership certificate and all other requirements and that the cluster configuration 
identifies peer certificates using Distinguished Name (DN) values.
For more information, see x509-member-certificate-requirements.

## Steps

**Step 1: Set override parameter on all members.**

During a rolling update, members are restarted one at a time with a new configuration. 
To allow server nodes with the the old subject DN attributes to identify nodes with the new 
subject DN attributes as cluster members, set the override parameter to the new subject DN attributes on all running members. 

To do this, modify the configuration file of each server to set the `tlsX509ClusterAuthDNOverride` parameter 
to use the subject DN attributes of the new certificate:

```yaml
net.tls.mode: requireTLS
net.tls.certificateKeyFile: "./mycerts/10gen-server1.pem"
net.tls.CAFile: "./mycerts/ca.pem"

security.clusterAuthMode: x509
net.tls.clusterFile:  "./mycerts/10gen-cluster1.pem"
net.tls.clusterCAFile: "./mycerts/ca.pem"

setParameter:
   tlsX509ClusterAuthDNOverride: "OU=MongoDB Server,O=MongoDB"
```

This configuration will not be taken into consideration until you restart each member.

**Step 2: Restart all members.**

To perform a rolling restart of all members, 
restart each secondary and then the primary. 

**For each secondary member**, connect `mongosh` to the
member, then: 

a. Use the `db.shutdownServer()` method to shut down the member:

   ```javascript
   use admin
   db.shutdownServer()
   ```

#. Restart the member. 

   Before restarting the next secondary, ensure this member has 
   reached `SECONDARY` state. To determine the member state, 
   run `rs.status()` and read the value of the `stateStr` field. 

   ```sh
   rs.status().members 
   ```

**For the primary member**, connect `mongosh` to the member, then: 

a. Use `rs.stepDown()` to step down the member:

   ```javascript
   rs.stepDown()
   ```

#. Use the `db.shutdownServer()` method to shut down the member:

   ```javascript
   use admin
   db.shutdownServer()
   ```

#. Restart the member.

All servers in the replica set can now use the override parameter to accept peer connections 
from members using certificates with the new subject DN attributes.

**Step 3: Modify configuration of all members.**

Update the configuration file of each server:

- Change the `net.tls.certificateKeyFile` setting to the new certificate.

- Change the `net.tls.clusterFile` setting to the new certificate. 

- Set the `tlsX509ClusterAuthDNOverride` parameter to use the
  DN attributes of the old certificate.

For example:

```yaml
net.tls.mode: requireTLS
net.tls.certificateKeyFile: "./mycerts/mongodb-server1.pem"
net.tls.CAFile: "./mycerts/ca.pem"

security.clusterAuthMode: x509
net.tls.clusterFile:  "./mycerts/mongodb-cluster1.pem"
net.tls.clusterCAFile: "./mycerts/ca.pem"

setParameter:
   tlsX509ClusterAuthDNOverride: "OU=10Gen Server,O=10Gen"
```

This configuration will not be taken into consideration until you restart each
member.

**Step 4: Restart all members.**

To apply the updated configuration to each member, perform a rolling 
restart of the server nodes by repeating the procedure from step 2. 

During this process, nodes that have been restarted with new certificates will use the 
old DN attributes stored in `tlsX509ClusterAuthDNOverride` to identify nodes 
presenting old certificates. Nodes that still have old certificates will use the new DN 
stored in `tlsX509ClusterAuthDNOverride` to identify nodes presenting new certificates. 

**Step 5: Remove override parameter from all members.**

To prevent the updated server nodes from treating clients presenting the
old certificate as peers, remove the `tlsX509ClusterAuthDNOverride`
parameter from all server node configuration files. 

For example: 

```yaml
net.tls.mode: requireTLS
net.tls.certificateKeyFile: "./mycerts/mongodb-server1.pem"
net.tls.CAFile: "./mycerts/ca.pem"

security.clusterAuthMode: x509

net.tls.clusterFile:  "./mycerts/mongodb-cluster1.pem"
net.tls.clusterCAFile: "./mycerts/ca.pem"
```

This configuration will not be taken into consideration until you restart each
member.

**Step 6: Restart all members.**

To apply the updated configuration to each member, perform a rolling 
restart of the server nodes by repeating the procedure from step 2. 

All servers in the replica set now accept peer connections only from members
using certificates that have the new subject DN attributes.
