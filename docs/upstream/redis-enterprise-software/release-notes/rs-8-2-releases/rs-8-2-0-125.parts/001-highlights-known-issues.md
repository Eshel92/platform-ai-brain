<!-- Part 1 of 3 of release-notes/rs-8-2-releases/rs-8-2-0-125.md (split because the page is big). -->

## Highlights

This version offers:

- Bug fix for upgrades from Redis Software 7.2.x and 7.4.x

- Bug fixes for cluster management after a primary node change

- Bug fix for node removal during rolling upgrades

- Bug fixes for DMC proxy stability and Active-Active proxy recovery

- Bug fixes for scaling, resharding, and cluster recovery

- Bug fix for ACL rule validation

- Bug fix for Google Cloud Storage backup configuration

- Bug fix for signing in with passwords that contain a colon

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

- RS196137: Fixed an issue where the Cluster Manager did not send the required `private_key` field when configuring Google Cloud Storage (GCS) backups.

- RS201541: Fixed an issue where removing a node could get stuck in a decommissioning state during a rolling upgrade of a cluster with AOF persistence on RHEL and Amazon Linux.

- RS202231: Fixed an issue where the DMC proxy could crash while resharding a database during a scale-out.

- RS202483: Fixed an issue where ACL rule validation did not apply the cluster's `acl_pubsub_default` setting, which caused validation to reject valid ACL rules or accept invalid rules that then left the database change pending.

- RS209436: Fixed an issue where a proxy that started during a database failover did not resume forwarding traffic and closed client connections while the database appeared active.

- RS210971: Fixed an issue where endpoint request metrics did not count requests to Memcached databases.

- RS211091: Fixed an issue where the cluster could become unresponsive after a newly joined node became the primary node while scaling the cluster.

- RS212081: Fixed an issue where changing the primary node could time out and leave the cluster without a working primary node.

- RS212205: Fixed an issue where users with a password that contains a colon (`:`) could not sign in to the Cluster Manager UI or authenticate REST API requests.

- RS212633: Fixed an issue where recovering a cluster after a full cluster restart could use outdated persistence files, which prevented the database from being recovered.

- RS213016: Fixed an issue where a node that was frozen and then resumed could stop responding to cluster management requests, which caused cluster health checks to fail and left the database in an `active-change-pending` state.

- RS213801: Fixed an issue where a shard could remain in the wrong role after resharding or scaling.

- RS215390: Fixed an issue where a database with the `all-nodes` proxy policy could stay in an `active-change-pending` state after a node was added to the cluster.

- RS215608: Fixed an issue where running `dmc-cli list bdb` or `dmc-cli list server` could corrupt memory and cause the DMC proxy to crash.

- RS215676: Fixed an issue where adding a participating cluster to an Active-Active database could cause the new participating cluster's shards to crash repeatedly during the full sync, which also disrupted synchronization between the other participating clusters.

- RS216045: Fixed an issue where the DMC proxy could crash repeatedly when a client sent a command without key arguments, such as `PUBSUB SHARDNUMSUB` with no channels, in a pipeline with another command.

- RS219531: Fixed an issue where upgrading a cluster from Redis Software version 7.2.x or 7.4.x to version 8.2.0 could fail because a node that still ran the earlier version lost its replication link to the cluster configuration store.


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

See [Ports and port ranges used by Redis Software](/content/operate/rs/networking/port-configurations.md#ports-and-port-ranges-used-by-redis-software) for a complete list.

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

| Package | SHA256 checksum (8.2.0-125 October release) |
|---------|---------------------------------------|
| Ubuntu 20 | <span class="break-all">edeb44f10ac5db8648c3a1ecd4266ec4a7e73035ea2e6415468ee6596c22da00</span> |
| Ubuntu 22 (amd64) | <span class="break-all">841feb35520a76b3ee51d7635f8fd2ed511b45c43a72d212c57af10394241527</span> |
| Ubuntu 22 (arm64) | <span class="break-all">9c527e55411fafca18353db49613381c669a1189e784e87010d92b8d2556bf17</span> |
| Red Hat Enterprise Linux (RHEL) 8 | <span class="break-all">c23106b4801c07e18adc660317b6b93aa7161f5ffb4b15f74893db91c761ffe6</span> |
| Red Hat Enterprise Linux (RHEL) 9 (amd64) | <span class="break-all">8bbd7fd39ac073a7b52e1545800d66c3995719b4766a58f762b5bc66c59ab5f0</span> |
| Red Hat Enterprise Linux (RHEL) 9 (arm64) | <span class="break-all">d908c2f20579e4e6c8e1d41c91cfb5bc48403306f4741d46f81b5afa784dcb6e</span> |
| Red Hat Enterprise Linux (RHEL) 9 FIPS (amd64) | <span class="break-all">896bb24fd57bfd3aaa269ebb9a31e42337c57f3afb2cae9ee45339e21b5ecfb2</span> |
| Amazon Linux 2023 (amd64) | <span class="break-all">06ac73b6788a38f1144288db2bccab9656deaad9523de1e0b508eb26c1129e21</span> |
| Amazon Linux 2023 (arm64) | <span class="break-all">b801de92c1c1633bacd2c2ac06ffbc8586de24fe689486b8c2a04a0084e6a362</span> |


## Known issues

- RS155734: Endpoint availability metrics do not work as expected due to a calculation error.

- For databases that use RedisTimeSeries with Redis database version 8.2, 8.4, or 8.6, after a shard restarts and recovers from its append-only file (AOF), requests routed to that shard can receive replies that belong to other commands or no reply at all. The issue does not resolve on its own.
