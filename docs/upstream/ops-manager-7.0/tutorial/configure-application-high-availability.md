<!-- Converted from tutorial/configure-application-high-availability.txt (reStructuredText). Includes are inlined. -->

# Configure a Highly Available Ops Manager Application

The Ops Manager Application provides high availability through use of multiple
Ops Manager Application servers behind a load balancer and through use of a
replica set to host the mms-application-database.

## Considerations

### Load Balancer

The Ops Manager Application's components are
stateless between requests. Any Ops Manager Application server can handle
requests as long as all the servers read from the same Ops Manager Application
Database. If one Ops Manager Application becomes unavailable, another
fills requests.

To take advantage of this for high availability, configure a load
balancer of your choice to balance between the pool of Ops Manager Application
hosts. To do this in Ops Manager, perform the following actions:

- Set the `URL to Access Ops Manager` property to the load
  balancer URL (Uniform Resource Locator).
  
- Set the `Load Balancer Remote IP Header` property to
  `X-Forwarded-For`,
  which is the HTTP (Hypertext Transfer Protocol) header field the load balancer uses to 
  identify the originating client's IP address. 

  **Note:**

  If you are using a Layer-4 load balancer that does not support
  `X-Forwarded-For` by default, either enable `X-Forwarded-For`,
  or use [Proxy Protocol](https://www.haproxy.com/blog/haproxy/proxy-protocol/).

The Ops Manager Application uses the client's IP address for auditing, logging,
and setting an access list for
the API (Application Programming Interface).

After the load balancer is configured and started, you should not log 
in to the Ops Manager Application from its individual host URL (Uniform Resource Locator)\s. 

**Note:**

To disallow access to each Ops Manager Application server, configure your 
firewall rules accordingly.

**Example:**

If you have two Ops Manager hosts serving the following URL (Uniform Resource Locator)\s:

- `ops1.example.com`
- `ops2.example.com`

and put them behind a load balancer at the following URL (Uniform Resource Locator):

- `opsmanager.example.com`

After you configure and start that load balancer, you should not log 
in to `ops1.example.com`. Log in to `opsmanager.example.com` 
instead.

**Note:**

If you set these parameters using the configuration file, change
`mms.remoteIp.header` to the URL (Uniform Resource Locator) for the load balancer
and `mms.centralUrl` to the URL (Uniform Resource Locator) for the Ops Manager host
and port.

#### File System Snapshots Require Shared File System

If you configure Ops Manager to use multiple Ops Manager application 
servers behind an HTTP (Hypertext Transfer Protocol) or HTTPS (Hypertext Transfer Protocol Secure) load balancer and use 
file system snapshots, 
FCV 4.2 or 
later backup snapshot jobs run in parallel on one or more servers. 
Ensure that you have a shared file system mounted on each Ops Manager 
server. The Ops Manager application server might open and write 
different offsets of the same files. Ensure that the shared file 
system allows this. Otherwise, you will encounter access errors.

#### Diagnostic Archive

To give your Ops Manager diagnostic archive time to generate, set the
HTTP idle timeout parameter for the load balancer to 180
seconds.

#### Appliance Network Layer Support

Any load balancing appliance must support
Layer 7 (the Application Layer) of
the OSI (Open Systems Interconnection) model.

### Replica Set for the Ops Manager Application Database

Deploy a replica set rather than a standalone to host the
mms-application-database. Replica sets have automatic
failover if the
primary becomes unavailable.

If the replica set has members in multiple facilities, ensure that a
single facility has enough votes to elect a primary if needed.
Choose the facility that hosts the core application systems. Place a
majority of voting members and all the members that can become primary
in this facility. Otherwise, network partitions could prevent the set
from being able to form a majority. For details on how replica sets
elect primaries, see
Replica Set Elections.

You can back up the replica set using
file system snapshots.
File system snapshots use system-level tools to create copies of the
device that holds replica set's data files.

To deploy the replica set that hosts the Ops Manager Application Database, see
backing MongoDB instance.

### The `gen.key` File

`gen.key` file is a 24-byte binary file used to encrypt and decrypt
Ops Manager\'s backing databases and user credentials. An identical
`gen.key` file must be stored on every server that is part of a
highly available Ops Manager deployment.

The `gen.key` file can be generated automatically or manually.

To have Ops Manager generate the file:
   Start *one* Ops Manager server. Ops Manager will create a `gen.key` file
   if none exists.

To create the file manually:
   Generate a 24-byte binary file.

   **Example:**

   The following creates the `gen.key` file using `openssl`:

   ```sh
   openssl rand 24 > /<keyPath>/gen.key
   ```

   Protect the `gen.key` file like any sensitive file. Change the
   owner to the user running Ops Manager and set the file permission to
   read and write for the owner only.

Once you have the `gen.key` file (either created automatically or
manually), *before* starting the other Ops Manager servers, copy the file
to the appropriate directory on the current server and to the
appropriate directory on the other Ops Manager servers:

* `/etc/mongodb-mms/` for RPM or Ubuntu installations

* `${HOME}/.mongodb-mms/` for archive (`.tar`) file
  installations

**Important:**

* Any shared storage resource that stores the `gen.key` file
  should be configured for high availability so as not to introduce
  a potential single point of failure.

* Any Ops Manager server that does not have the `gen.key` file
  installed cannot connect to the backing databases and become part
  of an HA Ops Manager instance.

* Once you have generated the `gen.key` for your Ops Manager instance
  on the first Ops Manager server, back up the `gen.key` file to a
  secure location.

### Upgrade Mode

If you have an Ops Manager installation with more than one Ops Manager host
pointing to the same Application Database, you can upgrade Ops Manager to
a newer version with only a brief monitoring downtime. After you
complete the upgrade of one Ops Manager host of a highly available
Ops Manager deployment, that deployment enters a state known as **Upgrade
Mode**. In this state, Ops Manager is available during an upgrade. The
benefits of this mode are that throughout the upgrade process:

- Alerts and monitoring operate
- Ops Manager instances remain live
- Ops Manager Application may be accessed in read-only mode
- Ops Manager API (Application Programming Interface)\s that write or delete data are disabled

Your Ops Manager instance stays in **Upgrade Mode** until all Ops Manager
hosts have been upgraded and restarted. You should not upgrade more
than one Ops Manager host at a time.

### Performance in Multi-Region Deployments

The geographical distribution of the Application Database and Ops Manager
instances might impact the performance of the Ops Manager Application.

#### Multi-region Application Database Performance

If you plan to replicate the Application Database across multiple regions,
consider that many of the Ops Manager write workload operations use
`w:2` write concern, which requires
acknowledgement from the primary member and one secondary member of the
replica set for each write operation.

Therefore, having a secondary replica member of the Application Database in
the **same** region as the primary member can lead to better read and write
performance.

For example, deploying three Application Database replica set members in
three regions in a 1-1-1 fashion might result in worse performance
compared with deploying three Application Database replica members in
two regions in a 2-1 fashion, where one region hosts two Application Database
replica set members and another region hosts the third replica set member.

#### Performance of the Ops Manager UI

The Ops Manager UI is more performant if you connect to the Ops Manager Application instance
deployed it in the same region as the Application Database primary member
of the Application Database replica set.

In other words, you may achieve a better user experience connecting to
the Ops Manager Application instance hosted in the same region as the
Application Database primary member of the replica set, rather than
connecting to a closer Ops Manager Application instance where the instance itself
must connect to a primary Application Database replica set member hosted in
a different, distant region with a high latency.

## Prerequisites

Deploy the replica set that serves the mms-application-database.
To deploy a replica set, see
Deploy a Replica Set in the
MongoDB manual.

## Procedure

The following procedure assumes you generated the first `gen.key` 
using one of the Ops Manager Application hosts. If you instead create your
own `gen.key`, distribute it to the Ops Manager hosts before starting
any of the Ops Manager Application\s.

**Important:**

The load balancer placed in front of the Ops Manager Application servers must
not return cached content. The load balancer must have caching
disabled.

To configure multiple Ops Manager Application \s with load balancing:

**Step 1: Configure a load balancer with the pool of Ops Manager Application hosts.**

Configure the load balancer to perform a health check on each 
Ops Manager health API endpoint:

```sh
http://<OpsManagerHost>:<OpsManagerPort>/monitor/health
```

Ops Manager responds with one of two HTTP (Hypertext Transfer Protocol) codes:

| HTTP Status Code | Health Status |
|---|---|
| 200 | Ops Manager host and application database appear healthy. |
| 500 | Ops Manager host or application database appear unhealthy. If this endpoint returns `HTTP 500` often, review the /troubleshooting section. |

The load balancer must not return cached content.

**Step 2: Configure Ops Manager to use the load balancer.**

a. In Ops Manager, click Admin, then the General
   tab, and then Ops Manager Config.

b. Set the `URL to Access Ops Manager` property to
   point to the load balancer URL.

c. Set the `Load Balancer Remote IP Header` property to the
   name of the HTTP (Hypertext Transfer Protocol) header field the load balancer uses to
   identify the client's IP address.

   Once `Load Balancer Remote IP Header` is set, Ops Manager
   enables the following HTTP (Hypertext Transfer Protocol) headers:

   | HTTP (Hypertext Transfer Protocol) Header | Forwards to Ops Manager |
   |---|---|
   | X-Forwarded-Host | Original host that the client requested in the Host HTTP (Hypertext Transfer Protocol) request header. |
   | X-Forwarded-Proto | Protocol used to make the HTTP (Hypertext Transfer Protocol) request. |
   | [X-Forwarded-Server](https://www.eclipse.org/jetty/javadoc/current/org/eclipse/jetty/server/ForwardedRequestCustomizer.html) | Hostname of the proxy server. |
   | [X-Proxied-Https](https://www.eclipse.org/jetty/javadoc/current/org/eclipse/jetty/server/ForwardedRequestCustomizer.html) | HTTPS (Hypertext Transfer Protocol Secure) status of a request. |

**Step 3: Update each Ops Manager Application host with the replication hosts information.**

On each host, edit the `conf-mms.properties` file to
set the `mongo.mongoUri` property to the
connection string of the
mms-application-database. You *must* specify at least **3**
hosts in the `mongo.mongoUri` connection string.

```ini
mongo.mongoUri=mongodb://<mms0.example.net>:<27017>,<mms1.example.net>:<27017>,<mms2.example.net>:<27017>/?maxPoolSize=100
```

**Step 4: Change the Ops Manager URL (Uniform Resource Locator) to the Load Balancer URL (Uniform Resource Locator) in the MongoDB Agent configuration file.**

Complete the following steps on each MongoDB Agent's host.

a. Open the MongoDB Agent configuration file.

   ```sh
   vi /path/to/configurationFile.config
   ```

   The location of the Automation configuration file depends on
   your platform:

   tabs:

     - id: macos
       content: |

         ```sh
         /path/to/install/local.config
         ```

     - id: linux
       content: |

         ```sh
         /path/to/install/local.config
         ```

     - id: rhel
       content: |

         ```sh
         /etc/mongodb-mms/automation-agent.config
         ```

     - id: debian
       content: |

         ```sh
         /etc/mongodb-mms/automation-agent.config
         ```

#. Edit the `mmsBaseUrl` property to point
   to the load balancer and save the changes.

   ```ini
   mmsBaseUrl=<LOAD-BALANCER-URL>:<PORT>
   ```

#. Restart the MongoDB Agent.

**Step 5: Start one of the Ops Manager Applications.**

**Example:**

If you installed the Ops Manager Application with an `rpm` or `deb`
package, issue the following:

```sh
service mongodb-mms start
```

**Step 6: Copy the `gen.key` file to each Ops Manager host.**

The `gen.key` file is located in `/etc/mongodb-mms/` for
installations from a package manager and in `${HOME}/.mongodb-mms/`
for installations from an archive.

Copy the `gen.key` file from the running Ops Manager Application's host to
the appropriate directory on the other Ops Manager Application hosts.

**Step 9: Start the remaining Ops Manager Applications.**

## Additional Information

For information on making Ops Manager Backup highly available, see
/tutorial/configure-backup-high-availability.
