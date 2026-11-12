<!-- Part 2 of 3 of release-notes/rs-8-2-releases/rs-8-2-0-78.md (split because the page is big). -->

## Known limitations

#### Increased memory usage in FIPS mode

FIPS-enabled builds use more memory than non-FIPS builds. Each Go-based control-plane service uses roughly 34 MB more when running in FIPS mode, which adds up to approximately 210 MB of additional memory per node. Account for this overhead when sizing FIPS-enabled deployments. This limitation affects FIPS-enabled builds only.

#### SFTP storage not supported in FIPS mode

FIPS-enabled builds do not support SFTP as a storage location for backups, imports, or exports, because the SFTP library is not FIPS-compliant. In FIPS mode, use a different storage location. This limitation affects FIPS-enabled builds only.

#### Redis Search query failures during rolling upgrades across the 8.4 version boundary

Redis Search queries can fail during a rolling upgrade when a cluster contains shards running Redis versions earlier than 8.4 and shards running Redis version 8.4 or later, due to an internal protocol change introduced in version 8.4. This issue affects only clusters where `parallel_shards_upgrade` has been changed from its default value of `0`. If both conditions apply, expect Redis Search downtime until all nodes are upgraded.

#### Trim ACKED not supported for Active-Active 8.4 databases

For Active-Active databases running Redis database version 8.4, the `ACKED` option is not supported for trimming commands.

#### Rolling upgrade limitation for clusters with custom or deprecated modules

Due to module handling changes introduced in Redis Software version 8.0, upgrading a cluster that contains custom or deprecated modules, such as RedisGraph and RedisGears v2, can become stuck when adding a new node to the cluster during a rolling upgrade.

#### Cluster Manager sign-outs and false "down" status during an Active-Active upgrade

While an Active-Active database has participating clusters running different Redis Software versions, the Cluster Manager UI on an upgraded cluster can sign users out intermittently and show a participating cluster as down, even though replication is active and the syncers are connected.

This affects the Cluster Manager UI only. It's caused by a JWT signing-key mismatch between nodes running different versions during the upgrade window (see [JWT token invalidation on upgrade](#jwt-token-invalidation-on-upgrade)). The data path and replication are not affected.

To resolve it, upgrade the remaining participating clusters. The issue clears after every participating cluster runs the same version. If you're signed out, sign in again.

#### Module commands limitation during Active-Active database upgrades to Redis 8.0

When upgrading an Active-Active database to Redis version 8.0, you cannot use module commands until all Active-Active database instances have been upgraded. Currently, these commands are not blocked automatically.

#### Redis 8.0 database cannot be created with flash

You cannot create a Redis 8.0 database with flash storage enabled. Create a Redis 8.0 database with RAM-only storage instead, or use Redis 8.2 for flash-enabled (Redis Flex) databases.

#### Cluster Manager UI limitations

The following legacy UI features are not yet available in the new Cluster Manager UI:

- Purge an Active-Active instance.

    Use [`crdb-cli crdb purge-instance`](/content/operate/rs/references/cli-utilities/crdb-cli/crdb/purge-instance.md) instead.
