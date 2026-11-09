<!-- Converted from modules/cassandra/pages/getting-started/querying.adoc (AsciiDoc). Includes are inlined. -->

# Inserting and querying

The API for Cassandra is `CQL`, the Cassandra Query Language. To
use CQL, you will need to connect to the cluster, using either:

* `cqlsh`, a shell for CQL
* a client driver for Cassandra
* for the adventurous, check out [Apache Zeppelin](https://zeppelin.apache.org/docs/0.7.0/interpreter/cassandra.html), a notebook-style tool

## CQLSH

`cqlsh` is a command-line shell for interacting with Cassandra using
CQL. It is shipped with every Cassandra package, and can be found in the
`bin` directory alongside the `cassandra` executable. It connects to the
single node specified on the command line. For example:

```shell
$ bin/cqlsh localhost

```
```cql
Connected to Test Cluster at localhost:9042.
[cqlsh 5.0.1 | Cassandra 3.8 | CQL spec 3.4.2 | Native protocol v4]
Use HELP for help.
cqlsh> SELECT cluster_name, listen_address FROM system.local;

 cluster_name | listen_address
--------------+----------------
 Test Cluster |      127.0.0.1

(1 rows)
cqlsh>

```
If the command is used without specifying a node, `localhost` is the default. See the `cqlsh` section for full documentation.

## Client drivers

A lot of client drivers are provided by the Community and a list of
known drivers is provided. You should refer to the documentation of each driver
for more information.
