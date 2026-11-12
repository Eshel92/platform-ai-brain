<!-- Part 1 of 2 of release-notes/rs-8-2-releases/rs-8-2-0-46.md (split because the page is big). -->

## Highlights

This version offers:

- Bug fixes for internal certificate rotation and rolling upgrades

- Bug fix for the Cluster Manager UI Overview page not loading

- Bug fixes for shard rebalancing and cluster configuration store growth

- Bug fixes for Active-Active synchronization

- Internal fixes and improvements


## New in this release

### Redis database versions and feature sets

Redis Software version 8.2.0 includes the following Redis database versions: 8.6.2, 8.4.0, 8.2.1, 8.0.2, 7.4.3, 7.2.7, and 6.2.13.

The [default Redis database version](/content/operate/rs/databases/configure/db-defaults.md#database-version) is 8.6.

Redis Software includes multiple feature sets, compatible with different Redis database versions.

{{< collapsible "Show feature set details" >}}

The following table shows which Redis modules are compatible with each Redis database version included in this release.

| Redis database version | Compatible Redis modules |
|------------------------|--------------------------|
| 8.6 | RediSearch 8.6<br />RedisJSON 8.6<br />RedisTimeSeries 8.6<br />RedisBloom 8.6<br />See [What's new in Redis 8.6](/content/develop/whats-new/8-6.md) and [Redis Open Source 8.6 release notes](/content/operate/oss_and_stack/stack-with-enterprise/release-notes/redisce/redisos-8.6-release-notes.md) |
| 8.4 | RediSearch 8.4<br />RedisJSON 8.4<br />RedisTimeSeries 8.4<br />RedisBloom 8.4<br />See [What's new in Redis 8.4](/content/develop/whats-new/8-4.md) and [Redis Open Source 8.4 release notes](/content/operate/oss_and_stack/stack-with-enterprise/release-notes/redisce/redisos-8.4-release-notes.md) |
| 8.2 | RediSearch 8.2<br />RedisJSON 8.2<br />RedisTimeSeries 8.2<br />RedisBloom 8.2<br />See [What's new in Redis 8.2](/content/develop/whats-new/8-2.md) and [Redis Open Source 8.2 release notes](/content/operate/oss_and_stack/stack-with-enterprise/release-notes/redisce/redisos-8.2-release-notes.md) |
| 8.0 | RediSearch 8.0<br />RedisJSON 8.0<br />RedisTimeSeries 8.0<br />RedisBloom 8.0<br />See [What's new in Redis 8.0](/content/develop/whats-new/8-0.md) and [Redis Open Source 8.0 release notes](/content/operate/oss_and_stack/stack-with-enterprise/release-notes/redisce/redisos-8.0-release-notes.md) |
| 7.4 | [RediSearch 2.10](/content/operate/oss_and_stack/stack-with-enterprise/release-notes/redisearch/redisearch-2.10-release-notes.md)<br />[RedisJSON 2.8](/content/operate/oss_and_stack/stack-with-enterprise/release-notes/redisjson/redisjson-2.8-release-notes.md)<br />[RedisTimeSeries 1.12](/content/operate/oss_and_stack/stack-with-enterprise/release-notes/redistimeseries/redistimeseries-1.12-release-notes.md)<br />[RedisBloom 2.8](/content/operate/oss_and_stack/stack-with-enterprise/release-notes/redisbloom/redisbloom-2.8-release-notes.md) |
| 7.2 | [RediSearch 2.8](/content/operate/oss_and_stack/stack-with-enterprise/release-notes/redisearch/redisearch-2.8-release-notes.md)<br />[RedisJSON 2.6](/content/operate/oss_and_stack/stack-with-enterprise/release-notes/redisjson/redisjson-2.6-release-notes.md)<br />[RedisTimeSeries 1.10](/content/operate/oss_and_stack/stack-with-enterprise/release-notes/redistimeseries/redistimeseries-1.10-release-notes.md)<br />[RedisBloom 2.6](/content/operate/oss_and_stack/stack-with-enterprise/release-notes/redisbloom/redisbloom-2.6-release-notes.md) |
| 6.2 | [RediSearch 2.6](/content/operate/oss_and_stack/stack-with-enterprise/release-notes/redisearch/redisearch-2.6-release-notes.md)<br />[RedisJSON 2.4](/content/operate/oss_and_stack/stack-with-enterprise/release-notes/redisjson/redisjson-2.4-release-notes.md)<br />[RedisTimeSeries 1.8](/content/operate/oss_and_stack/stack-with-enterprise/release-notes/redistimeseries/redistimeseries-1.8-release-notes.md)<br />[RedisBloom 2.4](/content/operate/oss_and_stack/stack-with-enterprise/release-notes/redisbloom/redisbloom-2.4-release-notes.md) |

{{< /collapsible >}}

### Resolved issues

- RS200137: Fixed an issue where internal certificate rotation skipped nodes that were down when rotation started and never retried them, which left those nodes with outdated certificates after they came back online.

- RS200495: Fixed an issue where `rladmin master set` could time out during a rolling upgrade when a node still running the earlier build rejected a master shard candidate running the new build while database configuration updates were in progress.

- RS200753: Fixed an issue where the Cluster Manager UI Overview page did not load and returned `invalid_schema` errors for `v2/actions` requests.

- RS202176: Fixed an issue where rebalancing shards while adding a node to a cluster could overflow the connection tracking (conntrack) table on multiple nodes and cause master shards to go down.

- RS202429: Fixed an issue where the `sm_fixer:all` key in the cluster configuration store grew without bound.

- RS209759: Fixed an issue where an unrecognized configuration change in the Active-Active (CRDB) syncer triggered a full synchronization instead of being ignored.

- RS209889: Fixed an issue where an Active-Active database resent the full dataset instead of only changes during a full state sync when an internal version clock exceeded 32 bits.


## Version changes

### JWT token invalidation on upgrade

To improve system security, the JWT signing secret has changed in version 8.0.22 and later. As a result, upgrading invalidates all previously issued JWT tokens, which must be regenerated. Tokens used programmatically within the cluster are regenerated automatically. Cluster Manager users must sign out and sign in again, or wait for their session or token to expire.

### Reserved ports

Make sure the following ports are open before upgrading Redis Software.

The following port was added as a reserved port in Redis Software version 8.0.18; however, it is optional instead of reserved in Redis Software version 8.0.20-44:

| Port | Process name | Usage |
|------|--------------|-------|
| 3357 | reconciliation_tree_grpc | Internal communication |

Ports reserved as of Redis Software version 7.22.0:

| Port | Process name | Usage |
|------|--------------|-------|
| 3346 | cluster_api_internal | Cluster API internal port |
| 3351 | cluster_watchdog_grpc_api | Cluster watchdog now supports gRPC |
| 3352 | grpc_service_mesh | gRPC communication between nodes |
| 3353 | local_grpc_service_mesh | Local gRPC services |
| 3354 | grpc_gossip_envoy | gRPC gossip protocol communication between nodes |
| 3355 | authentication_service | Authentication service internal port |

Ports reserved as of Redis Software version 7.8.2:

| Port | Process name | Usage |
|------|--------------|-------|
| 3347 | cert_exporter | Reports cluster certificate metrics |
| 3348 | process_exporter | Reports process metrics for DMC and Redis processes |
| 3349 | cluster_wd_exporter | Reports cluster watchdog metrics |
| 3350 | db_controller | Internode communication |
| 9091 | node_exporter | Reports host node metrics related to CPU, memory, disk, and more |
| 9125 | statsd_exporter | Reports push metrics related to the DMC and syncer, and some cluster and node metrics |

See [Ports and port ranges used by Redis Software](/content/operate/rs/networking/port-configurations.md#ports-and-port-ranges-used-by-redis-enterprise-software) for a complete list.

### Supported platforms

The following table provides a snapshot of supported platforms as of this Redis Software release. See the [supported platforms reference](/content/operate/rs/references/supported-platforms.md) for more details about operating system compatibility.

**Amazon Linux 2 is no longer supported.** Starting with Redis Software version 8.0.22, Redis Software no longer builds or publishes Amazon Linux 2 (`amzn2`) packages. Use Amazon Linux 2023 instead.

{{< collapsible "Show supported platforms" >}}

<span title="Check mark icon">&#x2705;</span> Supported – The platform is supported for this version of Redis Software and Redis Stack modules.

<span title="Warning icon" class="font-serif">:warning:</span> Deprecation warning – The platform is still supported for this version of Redis Software, but support will be removed in a future release.

| Redis Software<br />major versions | 8.2 | 8.0 | 7.22 | 7.8 | 7.4 | 7.2 | 6.4 | 6.2 |
|---------------------------------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| **Release date** | Jul 2026 | Oct 2025 | May 2025 | Nov 2024 | Feb 2024 | Aug 2023 | Feb 2023 | Aug 2021 |
| [**End-of-life date**](/content/operate/rs/installing-upgrading/product-lifecycle.md#endoflife-schedule) | Determined after<br />next major release | Jul 2028 | Oct 2027 | May 2027 | Nov 2026 | Feb 2026 | Aug 2025 | Feb 2025 |
| **Platforms** | | | | | | | | |
| RHEL 9 &<br />compatible distros<sup>[1](#table-note-1)</sup> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | – | – | – |
| RHEL 9<br />FIPS mode<sup>[5](#table-note-5)</sup> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | – | – | – | – |
| RHEL 8 &<br />compatible distros<sup>[1](#table-note-1)</sup> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| RHEL 7 &<br />compatible distros<sup>[1](#table-note-1)</sup> | – | – | – | – | – | <span title="Deprecated" class="font-serif">:warning:</span> | <span title="Deprecated" class="font-serif">:warning:</span> | <span title="Deprecated" class="font-serif">:warning:</span> |
| Ubuntu 22.04<sup>[2](#table-note-2)</sup> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | – | – | – | – |
| Ubuntu 20.04<sup>[2](#table-note-2)</sup> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | – |
| Ubuntu 18.04<sup>[2](#table-note-2)</sup> | – | – | – | – | <span title="Deprecated" class="font-serif">:warning:</span> | <span title="Deprecated" class="font-serif">:warning:</span> | <span title="Deprecated" class="font-serif">:warning:</span> | <span title="Deprecated" class="font-serif">:warning:</span> |
| Ubuntu 16.04<sup>[2](#table-note-2)</sup> | – | – | – | – | – | <span title="Deprecated" class="font-serif">:warning:</span> | <span title="Deprecated" class="font-serif">:warning:</span> | <span title="Deprecated" class="font-serif">:warning:</span> |
| Amazon Linux 2023<sup>[6](#table-note-6)</sup> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | – | – | – | – | – | – |
| Amazon Linux 2 | – | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | – |
| Amazon Linux 1 | – | – | – | – | – | <span title="Deprecated" class="font-serif">:warning:</span> | <span title="Deprecated" class="font-serif">:warning:</span> | <span title="Deprecated" class="font-serif">:warning:</span> |
| Kubernetes<sup>[3](#table-note-3)</sup> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| Docker<sup>[4](#table-note-4)</sup> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |

1. <a name="table-note-1"></a>The RHEL-compatible distributions CentOS, CentOS Stream, Alma, and Rocky are supported if they have full RHEL compatibility. Oracle Linux running the Red Hat Compatible Kernel (RHCK) is supported, but the Unbreakable Enterprise Kernel (UEK) is not supported.

2. <a name="table-note-2"></a>The server version of Ubuntu is recommended for production installations. The desktop version is only recommended for development deployments.

3. <a name="table-note-3"></a>See the [Redis Enterprise for Kubernetes documentation](/content/operate/kubernetes/reference/supported_k8s_distributions.md) for details about support per version and Kubernetes distribution.

4. <a name="table-note-4"></a>[Docker images](/content/operate/rs/installing-upgrading/quickstarts/docker-quickstart.md) of Redis Software are certified for development and testing only.

5. <a name="table-note-5"></a>Supported only if [FIPS was enabled during RHEL installation](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/switching-rhel-to-fips-mode_security-hardening#proc_installing-the-system-with-fips-mode-enabled_switching-rhel-to-fips-mode) to ensure FIPS compliance.

6. <a name="table-note-6"></a>Amazon Linux 2023 support was added in Redis Software version 8.0.20.

{{< /collapsible >}}


## Downloads

The following table shows the SHA256 checksums for the available packages:

| Package | SHA256 checksum (8.2.0-46 August release) |
|---------|---------------------------------------|
| Ubuntu 20 | <span class="break-all">f403c0a0029e477552d23892f4822e6709a84e9c664e16c6ba881f83002cb7a0</span> |
| Ubuntu 22 (amd64) | <span class="break-all">dc78326342dac6b20d80a4d7eaf4ca581ec59f60a1639385395f09f4dfb0aca0</span> |
| Ubuntu 22 (arm64) | <span class="break-all">1fef79f41f681a11df1ca3075491ac387348781f0e8d7d333fdf0ac26cf6674b</span> |
| Red Hat Enterprise Linux (RHEL) 8 | <span class="break-all">44d91105a41ab9aba51eb2d2b44bfb45360f1e28fa9bb5f824e0705f93d71864</span> |
| Red Hat Enterprise Linux (RHEL) 9 (amd64) | <span class="break-all">ea6c5983d902571d59f63263cc636cc811438367b40da6230cc7dce03145b07d</span> |
| Red Hat Enterprise Linux (RHEL) 9 (arm64) | <span class="break-all">a99719de0779cafa591ec614e5e8b0bfcde5617bed889e14feea71b77b01d6ef</span> |
| Red Hat Enterprise Linux (RHEL) 9 FIPS (amd64) | <span class="break-all">341c9198f349cc65e8d212fcff1055af3ae44c6125b8363024da57cc244426bf</span> |
| Amazon Linux 2023 (amd64) | <span class="break-all">d810b015198c118546b99ffca3528936029fc832f393c1cc727e93f0035e6218</span> |
| Amazon Linux 2023 (arm64) | <span class="break-all">9929eee00837ef1d7f8e333a29ec72133e090071954c65e66613ff51bd6b71f6</span> |


## Known issues

- RS155734: Endpoint availability metrics do not work as expected due to a calculation error.

- RS219531: Upgrading a cluster from Redis Software version 7.2.x or 7.4.x to version 8.2.0 can fail. After the first node is upgraded, a node that still runs the earlier version can lose its replication link to the cluster configuration store. `rladmin` then reports `CCS ERROR: REPLICATION LINK DOWN`, and the upgrade of the next node fails with `Failed to sync with master ccs`.

    To upgrade a Redis Software 7.2.x or 7.4.x cluster, first upgrade it to Redis Software version 8.0.x, and then upgrade to version 8.2.0.


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
