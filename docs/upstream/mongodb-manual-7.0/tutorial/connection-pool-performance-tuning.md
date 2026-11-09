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

Consider an application server connecting to a replica set with three
members. In this scenario, the application server creates a connection pool for 
each replica set member. You also need to consider 
the connections each client, on each node, creates for monitoring. 

The maximum number of connections that are opened by 
the application server is based on the `maxPoolSize`, the number of 
members, and each member's monitoring and RTT connections. 

For example, you can calculate the outgoing connections from an application to a 
three-member replica set with the following formula:

```sh
(
   **100** {:urioption:`maxPoolSize`}
  + **1** monitoring connection 
  + **1** RTT connection
) 
* 3 replica set members  

= **306** outgoing connections from the application.
```
