<!-- Converted from tutorial/connection-pool-performance-tuning.txt (reStructuredText). Includes are inlined. -->

# Tuning Your Connection Pool Settings

| Problem | Solution |
|---|---|
| Slow application-side operation times that are not reflected in the database server logs or the real time panel. | Use `connectTimeoutMS` to ensure the driver does not wait indefinitely during the connection phase. Set `connectTimeoutMS` to a value greater than the longest network latency you have to a member of the set. For example: if a member has a latency of 10000 milliseconds, setting `connectTimeoutMS` to `5000` (milliseconds) prevents the driver from connecting to that member. |
| A misconfigured firewall closes a socket connection incorrectly and the driver cannot detect that the connection closed improperly. | Use `socketTimeoutMS` to ensure that sockets are always closed. Set `socketTimeoutMS` to two or three times the length of the slowest operation that the driver runs. |
| The server logs or real time panel show that the application spends too much time creating new connections. | Not enough connections are available at startup. Allocate connections in the pool by setting `minPoolSize`. Set minPoolSize to the number of connections you want to be available at startup. The `MongoClient` instance ensures that number of connections exists at all times. |
| The load on the database is low and there's a small number of active connections at any time. Application performs fewer operations at any one time than expected. | Increase maxPoolSize, or increase the number of active threads in your application or the framework you are using. |
| Database CPU usage is higher than expected. The server logs or real time panel show more connection attempts than expected. | Decrease the maxPoolSize or reduce the number of threads in your application. This can reduce load and response times. |

**Warning:**

Do not use `socketTimeoutMS` to prevent long-running 
server operations. Instead, use `maxTimeMS` with 
queries so that the server can cancel long-running operations.

       

## Calculate Maximum Number of Connections

Calculate usage to find the number of operations running for each
connection.

Consider four application servers connecting to a replica set with three
members. In this scenario, each of the four application servers
creates a connection pool for each replica set member.

Calculate the maximum number of connections that are opened by 
each application server by multiplying `maxPoolSize` by the 
number of members.  

Calculate outgoing connections from an application to a three-member 
replica set:

**100** (`maxPoolSize` default `100`) x **3** (replica set members) = **300** (outgoing connections from the application).

Calculate incoming connections from four application servers to a 
replica set:

**100** (`maxPoolSize` default `100`) x **4** (application servers) = **400** (incoming connections to each mongod).
