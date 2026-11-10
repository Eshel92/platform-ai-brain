<!-- Converted from modules/cluster/remote-clusters-migration.asciidoc (AsciiDoc). Includes are inlined. -->

### Migrate remote clusters from certificate to API key authentication

The API key based security model for remote clusters offers administrators more
fine-grained access controls compared to the TLS certificate based security
model. For that reason, you may want to migrate from the certificate based
security model to the API key based model.

While it is possible to migrate by defining a new remote cluster connection,
using a new alias, this has several downsides:

- For cross-cluster replication, it's not possible to change the leader cluster alias for existing
tasks. As a result, with a new remote cluster, follower indices would need to be
re-created from scratch.
- For cross-cluster search, transform and anomaly detection jobs do allow updating the remote
cluster alias. However, if the job was created with wildcards, for example
`*:source_index`, and `superuser`, adding a new remote cluster will cause the
job to do double the amount of work and potentially skew results with
duplications.

For these reasons, you may prefer to migrate a remote cluster in-place, by
following these steps:

. Review the prerequisites
. remote-clusters-migration-remote-cluster
. remote-clusters-migration-stop
. remote-clusters-migration-reconnect
. remote-clusters-migration-resume
. remote-clusters-migration-disable-cert

If you run into any issues, refer to remote-clusters-troubleshooting.

#### Prerequisites

* The nodes of the local and remote clusters must be on version 8.10 or later.
* The local and remote clusters must have an appropriate license. For more
information, refer to https://www.elastic.co/subscriptions.

#### Reconfigure the remote cluster and generate a cross-cluster API key

On the remote cluster:

. Enable the remote cluster server on every node of the remote cluster. In
`elasticsearch.yml`:
.. Set `remote_cluster_server.enabled` to
`true`.
.. Configure the bind and publish address for remote cluster server traffic, for
example using `remote_cluster.host`. Without
configuring the address, remote cluster traffic may be bound to the local
interface, and remote clusters running on other machines can't connect.
.. Optionally, configure the remote server port using
`remote_cluster.port` (defaults to `9443`).
. Next, generate a certificate authority (CA) and a server certificate/key pair.
On one of the nodes of the remote cluster, from the directory where Elasticsearch has
been installed:

.. Create a CA, if you don't have a CA already:
```sh
./bin/elasticsearch-certutil ca --pem --out=cross-cluster-ca.zip --pass CA_PASSWORD
```
Replace `CA_PASSWORD` with the password you want to use for the CA. You can
remove the `--pass` option and its argument if you are not deploying to a
production environment.

.. Unzip the generated `cross-cluster-ca.zip` file. This compressed file
contains the following content:
```txt
/ca
|_ ca.crt
|_ ca.key
```

.. Generate a certificate and private key pair for the nodes in the remote
cluster:
```sh
./bin/elasticsearch-certutil cert --out=cross-cluster.p12 --pass=CERT_PASSWORD --ca-cert=ca/ca.crt --ca-key=ca/ca.key --ca-pass=CA_PASSWORD --dns=example.com --ip=127.0.0.1
```
* Replace `CA_PASSWORD` with the CA password from the previous step.
* Replace `CERT_PASSWORD` with the password you want to use for the generated
private key.
* Use the `--dns` option to specify the relevant DNS name for the certificate.
You can specify it multiple times for multiple DNS.
* Use the `--ip` option to specify the relevant IP address for the certificate.
You can specify it multiple times for multiple IP addresses.

.. If the remote cluster has multiple nodes, you can either:
* create a single wildcard certificate for all nodes;
* or, create separate certificates for each node either manually or in batch
with the silent mode.

. On every node of the remote cluster:
.. Copy the `cross-cluster.p12` file from the earlier step to the `config`
directory. If you didn't create a wildcard certificate, make sure you copy the
correct node-specific p12 file.
.. Add following configuration to `elasticsearch.yml`:
```yaml
xpack.security.remote_cluster_server.ssl.enabled: true
xpack.security.remote_cluster_server.ssl.keystore.path: cross-cluster.p12
```

.. Add the SSL keystore password to the Elasticsearch keystore:
```sh
./bin/elasticsearch-keystore add xpack.security.remote_cluster_server.ssl.keystore.secure_password
```
When prompted, enter the `CERT_PASSWORD` from the earlier step.

. Restart the remote cluster.

. On the remote cluster, generate a cross-cluster API key that provides access
to the indices you want to use for cross-cluster search or cross-cluster replication. You can use the
security-api-create-cross-cluster-api-key API or
[Kibana](https://www.elastic.co/guide/en/kibana/8.19/api-keys.html).

. Copy the encoded key (`encoded` in the response) to a safe location. You will
need it to connect to the remote cluster later.

#### Stop cross-cluster operations

On the local cluster, stop any persistent tasks that refer to the remote
cluster:

* Use the stop-transform API to stop any transforms.
* Use the ml-close-job API to close any anomaly detection jobs.
* Use the ccr-pause-auto-follow-pattern API to pause any auto-follow cross-cluster replication.
* Use the ccr-post-pause-follow API to pause any manual cross-cluster replication or existing
indices that were created from the auto-follow pattern.

#### Reconnect to the remote cluster

On the local cluster:

. Enhance any roles used by local cluster users with the required
remote indices privileges or 
remote cluster privileges for cross-cluster replication and cross-cluster search.
Refer to remote-clusters-privileges-api-key. Note:

** You only need to assign additional `remote_indices` or `remote_cluster` privileges to existing
roles used for cross-cluster operations. You should be able to copy these
privileges from the original roles on the remote cluster, where they are defined
under the certification based security model.
** The roles on the local cluster can't exceed the `access` privilege granted by
the cross-cluster API key. Any extra local privileges will be suppressed by the
cross-cluster API key's privileges.
** No update is needed if the cross-cluster replication or cross-cluster search tasks have been configured with a
`superuser` role. The `superuser` role is automatically updated to allow access
to all remote indices.
** Tasks that are run as regular users with named roles are immediately updated
with the new privileges. A task will load a new definition the next time it
runs.
** You need to restart tasks that are run using an API key (done in a later
step).

. If you've dynamically configured the remote cluster (via the cluster settings
API):

.. Retrieve the current remote cluster configuration, and store it in a safe
place. You may need it later in case you need to
roll back. Use the cluster settings API:
```console
GET /_cluster/settings?filter_path=persistent.cluster.remote
```

.. Remove the existing remote cluster definition by setting the remote cluster
settings to `null`.

. If you've statically configured the remote cluster (via `elasticsearch.yml`),
copy the `cluster.remote` settings from `elasticsearch.yml`, and store them
in a safe place. You may need them later in case you need to
roll back.

. On every node of the local cluster:

.. Copy the `ca.crt` file generated on the remote cluster earlier into the
`config` directory, renaming the file `remote-cluster-ca.crt`.

.. Add following configuration to `elasticsearch.yml`:
```yaml
xpack.security.remote_cluster_client.ssl.enabled: true
xpack.security.remote_cluster_client.ssl.certificate_authorities: [ "remote-cluster-ca.crt" ]
```
.. Add the cross-cluster API key, created on the remote cluster earlier, to the
keystore:
```sh
./bin/elasticsearch-keystore add cluster.remote.ALIAS.credentials
```
Replace `ALIAS` with the same alias that was used for cross-cluster operations
before the migration. When prompted, enter the encoded cross-cluster API key
created on the remote cluster earlier.

. If you've dynamically configured the remote cluster (via the cluster settings
API):

.. Restart the local cluster to load changes to the keystore and settings.

.. Re-add the remote cluster. Use the same remote cluster alias, and change the
transport port into the remote cluster port. For example:
```console
PUT /_cluster/settings
{
  "persistent" : {
    "cluster" : {
      "remote" : {
        "my_remote" : { <1>
          "mode": "proxy",
          "proxy_address": "my.remote.cluster.com:9443" <2>
        }
      }
    }
  }
}
```
<1> The remote cluster alias. Use the same alias that was used before the
migration.
<2> The remote cluster address with the remote cluster port, which defaults to
`9443`.

. If you've statically configured the remote cluster (via `elasticsearch.yml`):

.. Update the `cluster.remote` settings in `elasticsearch.yml` on each node of
the local cluster. Change the port into the remote cluster port, which defaults
to `9443`.

.. Restart the local cluster to load changes to the keystore and settings.

. Use the remote cluster info API to verify that the
local cluster has successfully connected to the remote cluster:
```console
GET /_remote/info
```
The API response should indicate that the local cluster has connected to the
remote cluster:
```console-result
{
  "my_remote": {
    "connected": true, <1>
    "mode": "proxy",
    "proxy_address": "my.remote.cluster.com:9443",
    "server_name": "",
    "num_proxy_sockets_connected": 0,
    "max_proxy_socket_connections": 18,
    "initial_connect_timeout": "30s",
    "skip_unavailable": false,
    "cluster_credentials": "::es_redacted::" <2>
  }
}
```
<1> The remote cluster is connected.
<2> If present, indicates the remote cluster has connected using API key
authentication.

#### Resume cross-cluster operations

Resume any persistent tasks that you stopped earlier. Tasks should be restarted
by the same user or API key that created the task before the migration. Ensure
the roles of this user or API key have been updated with the required
`remote_indices` or `remote_cluster` privileges. For users, tasks capture the caller's credentials
when started and run in that user's security context. For API keys, restarting a
task will update the task with the updated API key.

* Use the start-transform API to start any transforms.
* Use the ml-open-job API to open any anomaly detection jobs.
* Use the ccr-post-resume-follow API to resume any auto-follow cross-cluster replication.
* Use the ccr-resume-auto-follow-pattern API to resume any manual cross-cluster replication or
existing indices that were created from the auto-follow pattern.

#### Disable certificate based authentication and authorization

**Note:** Only proceed with this step if the migration has been proved successful on
the local cluster. If the migration is unsuccessful, either
<<remote-clusters-troubleshooting,find out what the problem is and attempt to
fix it>> or roll back.

Next, disable the certification based connection. Optionally, you can also
revoke the authorization.

. There is no particular setting to enable or disable a certificate based cross
cluster connection, because it shares the same transport protocol with the
intra-cluster node-to-node communication.
One way a remote cluster administrator can stop an existing local cluster from
connecting, is by changing TLS trust. The exact steps vary, depending on how the
clusters have been configured. A generic solution is to
<<encrypt-internode-communication,recreate the CA and certificate/key used by
the remote transport interface>> so that any existing certificate/key, locally
or distributed, is no longer trusted.
Another solution is to apply IP filters to the transport interface, blocking
traffic from outside the cluster.

. Optionally, delete any roles on the remote cluster that were only used for
cross-cluster operations. These roles are no longer used under the API key based
security model.

#### Rollback

If you need to roll back, follow these steps on the local cluster:

. Stop any persistent tasks that refer to the remote cluster.

. Remove the remote cluster definition by setting the remote cluster settings to
`null`.

. Remove the `remote_indices` or 'remote_cluster' privileges from any roles that were updated during
the migration.

. On each node, remove the `remote_cluster_client.ssl.*` settings from
`elasticsearch.yml`.

. Restart the local cluster to apply changes to the keystore and
`elasticsearch.yml`.

. On the local cluster, apply the original remote cluster settings. If the
remote cluster connection has been configured statically (using the
`elasticsearch.yml` file), restart the cluster.

. Use the remote cluster info API to verify that the
local cluster has connected to the remote cluster. The response should have
`"connected": true` and not have `"cluster_credentials": "::es_redacted::"`.

. Restart any persistent tasks that you've stopped earlier.
