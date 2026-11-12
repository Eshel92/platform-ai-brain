<!-- Part 1 of 3 of release-notes/rs-8-2-releases/rs-8-2-6-25.md (split because the page is big). -->

## Highlights

This version offers:

- Redis database version 8.8

- Redis Search on Flex databases, in preview

- Customer-provided encryption keys (SSE-C) for exports and imports with Amazon S3 and S3-compatible storage

- Internal fixes and improvements


## New in this release

### New features

#### Redis database version 8.8

Redis Software 8.2.6 adds Redis database version 8.8. See [What's new in Redis 8.8](/content/develop/whats-new/8-8.md) and the [Redis Open Source 8.8 release notes](/content/operate/oss_and_stack/stack-with-enterprise/release-notes/redisce/redisos-8.8-release-notes.md).

#### Redis Search on Flex (preview)

Flex databases can now store Redis Search indexes on flash, so large indexes don't need to fit in RAM. Redis Search on Flex requires Redis database version 8.8 or later.

See [Index and search data in Flex databases](/content/operate/rs/flex/search.md) for requirements, supported features, and limitations.

#### Customer-provided encryption keys for exports and imports

You can now encrypt data you export to Amazon S3 or S3-compatible storage with a customer-provided encryption key (SSE-C), and import data from a source encrypted with one. You provide the key in each export or import request.

See [Export data from a database](/content/operate/rs/databases/import-export/export-data.md) and [Import data into a database](/content/operate/rs/databases/import-export/import-data.md).

### Enhancements

- **Cluster FQDN in support package file names.** Add the `fqdn` option to [`rladmin cluster debug_info`](/content/operate/rs/references/cli-utilities/rladmin/cluster/debug_info.md) to include the cluster's fully qualified domain name (FQDN) in the support package file name, which helps you tell support packages from different clusters apart.

- **Selective fork termination under memory pressure.** When a node runs low on memory for fork operations, such as backups, AOF rewrites, and replica full syncs, Redis Software now stops only the most recently started forks needed to free enough memory, instead of stopping all of them. The older forks can finish and release their memory, which prevents repeated cycles of failed full syncs and backups.

- **Key size metrics for Active-Active databases on Redis 7.4.** [v2 metrics](/content/operate/rs/monitoring/metrics_stream_engine/prometheus-metrics-v2.md) that count keys by value size or number of elements, such as strings larger than 512 MB or sets, sorted sets, hashes, and lists with more than 8 million elements, are now available for Active-Active databases that use Redis database version 7.4.

- **SAML SSO role mappings apply at every sign-in.** Redis Software now checks the `redisRoleMapping` attribute each time a user created with just-in-time (JIT) provisioning signs in with SAML single sign-on (SSO), so role changes in the identity provider take effect at the user's next sign-in. If the attribute is missing or contains no valid role UIDs, the sign-in fails and the user's roles are removed. Users who existed in Redis Software before SSO was set up keep their existing roles. See [SAML single sign-on](/content/operate/rs/security/access-control/saml-sso.md). Before you upgrade, review [SAML SSO role mappings on upgrade](#saml-sso-role-mappings-on-upgrade).

### Redis database versions and feature sets

Redis Software version 8.2.6 includes the following Redis database versions: 8.8.0, 8.6.2, 8.4.0, 8.2.1, 8.0.2, 7.4.3, 7.2.7, and 6.2.13.

The [default Redis database version](/content/operate/rs/databases/configure/db-defaults.md#database-version) is 8.6.

Redis Software includes multiple feature sets, compatible with different Redis database versions.

{{< collapsible "Show feature set details" >}}

The following table shows which Redis modules are compatible with each Redis database version included in this release.

| Redis database version | Compatible Redis modules |
|------------------------|--------------------------|
| 8.8 | RediSearch 8.8<br />RedisJSON 8.8<br />RedisTimeSeries 8.8<br />RedisBloom 8.8<br />See [What's new in Redis 8.8](/content/develop/whats-new/8-8.md) and [Redis Open Source 8.8 release notes](/content/operate/oss_and_stack/stack-with-enterprise/release-notes/redisce/redisos-8.8-release-notes.md) |
| 8.6 | RediSearch 8.6<br />RedisJSON 8.6<br />RedisTimeSeries 8.6<br />RedisBloom 8.6<br />See [What's new in Redis 8.6](/content/develop/whats-new/8-6.md) and [Redis Open Source 8.6 release notes](/content/operate/oss_and_stack/stack-with-enterprise/release-notes/redisce/redisos-8.6-release-notes.md) |
| 8.4 | RediSearch 8.4<br />RedisJSON 8.4<br />RedisTimeSeries 8.4<br />RedisBloom 8.4<br />See [What's new in Redis 8.4](/content/develop/whats-new/8-4.md) and [Redis Open Source 8.4 release notes](/content/operate/oss_and_stack/stack-with-enterprise/release-notes/redisce/redisos-8.4-release-notes.md) |
| 8.2 | RediSearch 8.2<br />RedisJSON 8.2<br />RedisTimeSeries 8.2<br />RedisBloom 8.2<br />See [What's new in Redis 8.2](/content/develop/whats-new/8-2.md) and [Redis Open Source 8.2 release notes](/content/operate/oss_and_stack/stack-with-enterprise/release-notes/redisce/redisos-8.2-release-notes.md) |
| 8.0 | RediSearch 8.0<br />RedisJSON 8.0<br />RedisTimeSeries 8.0<br />RedisBloom 8.0<br />See [What's new in Redis 8.0](/content/develop/whats-new/8-0.md) and [Redis Open Source 8.0 release notes](/content/operate/oss_and_stack/stack-with-enterprise/release-notes/redisce/redisos-8.0-release-notes.md) |
| 7.4 | [RediSearch 2.10](/content/operate/oss_and_stack/stack-with-enterprise/release-notes/redisearch/redisearch-2.10-release-notes.md)<br />[RedisJSON 2.8](/content/operate/oss_and_stack/stack-with-enterprise/release-notes/redisjson/redisjson-2.8-release-notes.md)<br />[RedisTimeSeries 1.12](/content/operate/oss_and_stack/stack-with-enterprise/release-notes/redistimeseries/redistimeseries-1.12-release-notes.md)<br />[RedisBloom 2.8](/content/operate/oss_and_stack/stack-with-enterprise/release-notes/redisbloom/redisbloom-2.8-release-notes.md) |
| 7.2 | [RediSearch 2.8](/content/operate/oss_and_stack/stack-with-enterprise/release-notes/redisearch/redisearch-2.8-release-notes.md)<br />[RedisJSON 2.6](/content/operate/oss_and_stack/stack-with-enterprise/release-notes/redisjson/redisjson-2.6-release-notes.md)<br />[RedisTimeSeries 1.10](/content/operate/oss_and_stack/stack-with-enterprise/release-notes/redistimeseries/redistimeseries-1.10-release-notes.md)<br />[RedisBloom 2.6](/content/operate/oss_and_stack/stack-with-enterprise/release-notes/redisbloom/redisbloom-2.6-release-notes.md) |
| 6.2 | [RediSearch 2.6](/content/operate/oss_and_stack/stack-with-enterprise/release-notes/redisearch/redisearch-2.6-release-notes.md)<br />[RedisJSON 2.4](/content/operate/oss_and_stack/stack-with-enterprise/release-notes/redisjson/redisjson-2.4-release-notes.md)<br />[RedisTimeSeries 1.8](/content/operate/oss_and_stack/stack-with-enterprise/release-notes/redistimeseries/redistimeseries-1.8-release-notes.md)<br />[RedisBloom 2.4](/content/operate/oss_and_stack/stack-with-enterprise/release-notes/redisbloom/redisbloom-2.4-release-notes.md) |

{{< /collapsible >}}

### Resolved issues

- RS147347: Fixed an issue where a failover could get stuck when a long-running Lua script made the newly promoted primary shard unresponsive.

- RS152117: Fixed an issue where disabling connection auditing with `db_conns_auditing` did not stop the DMC proxy from connecting to the auditing server.

- RS163957: Fixed an issue where a failover could get stuck if the node with the primary shards went down while the cluster was moving primary shards off that node, for example during `rladmin node <ID> enslave` or `rladmin node <ID> maintenance_mode on`.

- RS176407: Fixed an issue where the discovery service did not retry loading the database list after node restarts, which caused client connection errors.

- RS182474: Fixed an issue where old AOF `.prev` folders were not deleted when the persistent storage path was changed from the default during node setup, which could fill the persistent storage disk.

- RS182713: Fixed an issue where `crdb-cli crdb create` did not fully validate `shard_key_regex` in `--default-db-config`. An invalid value could leave Active-Active database creation stuck and prevent you from deleting the database.

- RS182889: Fixed an issue where `rlcheck` reported success even when a service was in the `BACKOFF` state.

- RS186010: Fixed an issue where replica full syncs could fail repeatedly when several ran at the same time on a node with low free memory, which could leave failovers and node removal stuck.

- RS193680: Fixed an issue where, with the all-nodes endpoint policy, DNS continued to return the IP address of a node that was down for several minutes.

- RS196638: Fixed an issue where updating an Active-Active database to set an instance's `db_config` field to `null`, to fall back to `default_db_config`, failed validation for some fields, such as `data_persistence`, `tls_mode`, `proxy_policy`, and `eviction_policy`.

- RS196965: Fixed an issue where an Active-Active database went out of sync with an encryption error when `authentication_ssl_client_certs` included CA certificates.

- RS197093: Fixed an issue where planning shard placement to scale out a database could fail with `Cannot allocate nodes for slave shards, count bomb at -1` even when a valid placement existed.

- RS197570: Fixed an issue where users with the User Manager role could not edit other users' email addresses, passwords, or ACLs in the Cluster Manager UI.

- RS197670: Fixed an issue where several Active-Active databases stopped syncing and syncer logs filled up when one node hosted many Active-Active database endpoints.

- RS197961: Fixed an issue where a database's shards could use more combined memory than the database memory limit when the database grew very quickly.

- RS197962: Fixed an issue where upgrading deleted customer-created roles, which caused single sign-on (SSO) just-in-time provisioning to fail.

- RS198022: Fixed an issue where `rladmin node <ID> external_addr set` accepted duplicate addresses, which created duplicate DNS records.

- RS198370: Fixed an issue where replication for Redis Flex databases restarted from the beginning when the `max_slave_full_syncs` limit took effect after the checkpoint phase.

- RS198633: Fixed an issue where a failover could proceed during a cluster master election while the cluster master was isolated from the network, which could leave two primary shards and break replication.

- RS198733: Fixed an issue where the cluster could place shards on a node configured as quorum only.

- RS198984: Fixed an issue where LDAP users could not sign in to the Cluster Manager UI.

- RS199023: Fixed an issue where the Cluster Manager UI and the database health report REST API reported Active-Active replication as down when participating clusters ran different Redis Software versions.

- RS199700: Fixed an issue where a database that was not an Active-Active database but had `crdt_sync` enabled could not be upgraded to Redis database version 8.0 or later.

- RS199707: Fixed an issue where automatic AOF rewrites could stop on a node while the cluster kept running, which let AOF files and persistent disk usage keep growing.

- RS199842: Fixed an issue where ACL updates failed on some shards with the error `Could not parse None as a boolean`.

- RS200250: Changed the permissions of the diagnostic logging directory, `/var/opt/redislabs/log/diagnostics`, to 640.

- RS201408: Fixed an issue where the firewalld service definitions did not include all documented ports, so those ports stayed blocked after a default installation on RHEL.

- RS201488: Fixed an issue where `rladmin tune db <db> slave_buffer <value>` and the equivalent REST API request failed, and left only some shards updated, when a shard was unreachable. The new value is now stored and applied to each shard as it becomes reachable.

- RS202179: Fixed an issue where Redis Software services could restart repeatedly on a slow node because startup took longer than the operating system's default service startup timeout.

- RS202472: Fixed an issue where upgrades failed with the error `Background processes currently running` even when no tasks were running.

- RS202473: Fixed an issue where `upgrade_mode` stayed enabled after you upgraded the last node in the cluster.

- RS205562: Fixed an issue where a replica shard of a database with Redis Search indexes could restart repeatedly while loading data during a full sync.

- RS206359: Fixed an issue where increasing the memory limit of an Active-Active database did not clear its out-of-memory state.

- RS207736: Fixed an issue where a timeout while committing an Active-Active database configuration change to one participating cluster could leave the participating clusters on different configuration versions and stop synchronization.

- RS207864: Fixed an issue where the discovery service's memory usage grew continuously when clients rapidly opened and closed TLS connections.

- RS207995: Fixed an issue where `FT.SEARCH` and `FT.INFO` kept failing with `shards topology update is either transient or has failed` after node changes during an upgrade, even after the cluster was stable.

- RS208093: Fixed an issue where a database update that used a shards blueprint to change the number of shards could fail with `Cannot match group_ids for shards_blueprint`.

- RS208861: Fixed an issue where `HELLO 3` reported `mode cluster` when the OSS Cluster API was disabled.

- RS209365: Fixed an issue where a Replica Of full sync could fail repeatedly on a shard that contained a very large key.

- RS209426: Fixed an issue where the discovery service exited and restarted repeatedly after a node was removed from the cluster.

- RS209544: Fixed an issue where an Active-Active syncer did not restart after a connection error, which left synchronization stopped.

- RS209754: Fixed an issue where `crdb-cli crdb remove-instance` could hang with 504 errors and make Active-Active database management unavailable.

- RS209935: Fixed an issue where repeated failovers during a network disruption could cause data loss on an Active-Active database with a single participating cluster.

- RS210056: Fixed an issue where the DMC proxy crashed repeatedly while resharding a database with more than 200 primary shards under pipelined client traffic, which dropped client connections.

- RS210070: Fixed an issue where cluster setup could fail on RHEL 9 when the system OpenSSL default digest was set to SHA-1.

- RS210376: Fixed an issue where the DMC proxy could stop receiving configuration changes after its connection to the cluster master stalled, which caused database and endpoint operations to fail with `verification timed out` errors.

- RS210428: Fixed an issue where an Active-Active syncer kept trying to connect to a removed node after node replacement, which stalled synchronization.

- RS210779: Fixed an issue where certificate-based authentication failed when the client certificate subject included extra attributes, such as `emailAddress`.

- RS210787: Fixed an issue where adding a participating cluster to an Active-Active database failed after `shards_count` was increased on a database without sharding.

- RS210791: Fixed an issue where a large cluster could become unresponsive after a cluster master change, when many nodes reconnected to the new cluster master at the same time.

- RS210977: Fixed an issue where an upgrade could report a completed step as timed out and leave the cluster partly reconfigured, so the cluster could later stop responding after a node failed or was replaced.

- RS211018: Fixed an issue where resharding a database with sparse shard placement could place most primary shards on one node.

- RS211657: Fixed an issue where the Cluster Manager UI Overview page did not load after an upgrade from Redis Software 7.2.4 to 8.2.0 because the `GET /v2/actions` REST API request returned an error.

- RS212502: Fixed an issue where the discovery service went down on all nodes after you enabled TLS for a database.

- RS212623: Fixed an issue where a failed database operation could leave stale data that caused a later failover of the same database to fail, which left the database unavailable.

- RS212738: Fixed an issue where the DMC proxy could crash while processing a `SCAN` command during a rolling upgrade with Smart client handoffs (SCH) enabled.

- RS212887: Fixed an issue where very large multi-key `UNLINK` requests received no reply, and request metrics did not match traffic.

- RS213534: Fixed an issue where `rladmin cluster recover` failed when internode encryption used customer-provided certificates.

- RS213830: Fixed an issue where creating a database from persistence files with `POST /v2/bdbs` and a `recovery_plan` retried indefinitely when no persistence files were found, instead of failing with a `missing_recovery_files` error.

- RS213865: Fixed an issue where an ACL rule such as `-config|get` did not block `CONFIG GET`.

- RS214201: Fixed an issue where replica shards failed to sync after a node reboot, which left databases without replication.

- RS214244: Fixed an issue where database recovery failed when the append-only file (AOF) was empty.

- RS217882: Fixed an issue where resharding and other database operations could fail with `verification timed out: 1 notifications still pending` when the DMC proxy was slow to apply configuration changes on nodes with high CPU usage.

- RS218864: Fixed an issue where log files for Auto Tiering databases that use the Speedb storage engine used much more disk space than their file size showed after log rotation, which could fill the log disk on busy nodes.

- RS220480: Fixed an issue where upgrading a cluster from Redis Software versions 7.0 through 7.4 could lose the cluster configuration, including DNS records, if the cluster master changed while some nodes still ran the earlier version.
