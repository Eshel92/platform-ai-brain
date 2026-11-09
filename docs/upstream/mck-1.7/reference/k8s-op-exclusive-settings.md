<!-- Converted from reference/k8s-op-exclusive-settings.txt (reStructuredText). Includes are inlined. -->

# MongoDB Kubernetes Operator Exclusive Settings

**Note:**

At any place on this page that says *Ops Manager*, you can substitute *Cloud Manager*.

## Kubernetes Operator Overrides Some Ops Manager Settings

Some settings that you configure using Kubernetes Operator cannot be set or
overridden in the Ops Manager Application. Settings that the Kubernetes Operator does
not manage are accepted.

The following list of settings are exclusive to Kubernetes. This list may
change at a later date.

These settings can be found on the
`automation configuration`
page:

- `auth.autoAuthMechanisms`
- `auth.authoritativeSet`
- `auth.autoPwd`
- `auth.autoUser`
- `auth.deploymentAuthMechanisms`
- `auth.disabled`
- `auth.key`
- `auth.keyfile`
- `auth.keyfileWindows`
- `auth.usersWanted`
- `auth.usersWanted[n].mechanisms`
- `auth.usersWanted[n].roles`
- `auth.usersWanted[n].roles[m].role`
- `auth.usersWanted[n].roles[m].db`
- `auth.usersWanted[n].user`
- `auth.usersWanted[n].authenticationRestrictions`
- `processes.args2_6.net.port`
- `processes.args2_6.net.tls.certificateKeyFile`
- `processes.args2_6.net.tls.clusterFile`
- `processes.args2_6.replication.replSetName`
- `processes.args2_6.sharding.clusterRole`
- `processes.args2_6.security.clusterAuthMode`
- `processes.args2_6.storage.dbPath`
- `processes.args2_6.systemLog.destination`
- `processes.args2_6.systemLog.path`
- `processes.authSchemaVersion`
- `processes.cluster` (mongos processes)
- `processes.featureCompatibilityVersion`
- `processes.hostname`
- `processes.name`
- `processes.version`
- `replicaSets._id`
- `replicaSets.members._id`
- `replicaSets.members.host`
- `replicaSets.members`
- `replicaSets.version`
- `sharding.clusterRole` (config server)
- `sharding.configServerReplica`
- `sharding.name`
- `sharding.shards._id`
- `sharding.shards.rs`
- `ssl.CAFilePath`
- `ssl.autoPEMKeyFilePath`
- `ssl.clientCertificateMode`

In addition to the list of Automation settings, the Kubernetes Operator uses attributes
outside of the deployment from the Monitoring and Backup Agent configurations.

- `backupAgentTemplate.username`
- `backupAgentTemplate.sslPEMKeyFile`
- `monitoringAgentTemplate.username`
- `monitoringAgentTemplate.sslPEMKeyFile`

**Example:**

- Kubernetes Operator creates a replica set of 3 members.

- You changed `storage.wiredTiger.engineConfig.cacheSizeGB`
  to `40`.

  **Note:**

  This setting is not in the Kubernetes Operator exclusive settings
  list.

- You then use the Kubernetes Operator to scale the replica set to
  5 members.

- The `storage.wiredTiger.engineConfig.cacheSizeGB` on the
  new members should still be `40`.
