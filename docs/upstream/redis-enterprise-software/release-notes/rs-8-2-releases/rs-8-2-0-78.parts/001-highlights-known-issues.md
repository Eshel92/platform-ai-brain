<!-- Part 1 of 3 of release-notes/rs-8-2-releases/rs-8-2-0-78.md (split because the page is big). -->

## Highlights

This version offers:

- FIPS 140-3 support for AWS EKS with Bottlerocket FIPS worker nodes

- Bug fixes for minor version upgrades and shard placement

- Bug fix for LDAP client authentication

- Bug fixes for database connectivity and DMC proxy connection cleanup

- Bug fix for applying custom internode encryption certificates

- Bug fix for resizing a database with Auto Tiering enabled

- Bug fix for `crdb-cli` certificate-based authentication

- Bug fixes for metrics export and Prometheus ingestion

- Bug fixes for module configuration and support package collection

- Internal fixes and improvements


## New in this release

### FIPS 140-3 support for AWS EKS

Redis Software now supports FIPS 140-3 for RHEL 9 containerized Redis on AWS EKS with Bottlerocket FIPS worker nodes, using cryptographic libraries based on FIPS 140-3 validated modules, enabling the use of FIPS-approved cryptographic algorithms in supported environments.

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

- RS149489: Fixed an issue where Redis Software exported metrics samples that shared a timestamp but carried different values, which caused Prometheus to reject them with an ingestion error.

- RS192976: Fixed an issue where a master shard could not be reached while the shard placement blueprint was applied through migrations and failovers.

- RS197092: Fixed an issue where databases became unreachable after a quorum node went down.

- RS197402: Fixed an issue where LDAP client authentication failed after a period of time.

- RS205561: Fixed an issue where v2 metrics were exported with a duplicate cluster label, which caused Grafana dashboards based on v2 metrics to show no data.

- RS206926: Fixed an issue where the DMC proxy could fail an assertion while cleaning up an SSL client disconnection over IPv6.

- RS208996: Fixed an issue where applying a custom internode encryption certificate restarted the heartbeat daemon and made the cluster configuration store and the management API on port 9443 unavailable cluster-wide.

- RS210365: Fixed an issue where removing module arguments from a database configuration did not update the `redis.conf` file on the shards.

- RS212043: Fixed an issue where `crdb-cli` did not use the configured client key when certificate-based authentication was enabled.

- RS212448: Fixed an issue where resizing a database with Auto Tiering enabled did not complete after a cluster upgrade, which left the database in a pending state and caused subsequent requests to return a busy error.

- RS213492: Fixed an issue where shards loaded slowly from persistence during a minor version upgrade of a non-replicated database, which extended the time the database spent in a loading state.

- RS215377: Fixed an issue where `rladmin cluster debug_info` silently omitted nodes whose collection failed, which produced a support package that appeared complete.


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

| Package | SHA256 checksum (8.2.0-78 September release) |
|---------|---------------------------------------|
| Ubuntu 20 | <span class="break-all">9b6e72f4a6e33edfc1fcfecb8c3e2d9fa3eaa7046671769b9ef4577232bcc752</span> |
| Ubuntu 22 (amd64) | <span class="break-all">c8db7bdd96d62477ba63b0cd6394cdb8f9b9324a42d75b7555184cd5af9c8ac7</span> |
| Ubuntu 22 (arm64) | <span class="break-all">49df72b4dc94d8d1e82c93b8e7d6ceb619a54c1de39635c0fe181be35a02d496</span> |
| Red Hat Enterprise Linux (RHEL) 8 | <span class="break-all">3f2e2982de2635c3dd95cf9c6e61cc3017cdecaf6882443f78a8ac0ef3b4b35e</span> |
| Red Hat Enterprise Linux (RHEL) 9 (amd64) | <span class="break-all">90f6d4b0384309a8a0cd56483c2792ba70431c97e901beec3619eadfbb453767</span> |
| Red Hat Enterprise Linux (RHEL) 9 (arm64) | <span class="break-all">47d8a20b7400f888ea6eb91fcdf4e5a4a8f0907466cd2e939f862c0a92853b0f</span> |
| Red Hat Enterprise Linux (RHEL) 9 FIPS (amd64) | <span class="break-all">f6dfd1a5ff272c83ca58c596636ddfd579fcc8d29ae725e9f1db8001831b7e6a</span> |
| Amazon Linux 2023 (amd64) | <span class="break-all">bd9e235ad9e5691bd28c2f044e5cb82487855c5936400b3e6e32dc3c4ed0c36a</span> |
| Amazon Linux 2023 (arm64) | <span class="break-all">19edcb85236007f1dcd6b62aeea0828f439a20b76247c75303a1f4592d1fb748</span> |


## Known issues

- RS155734: Endpoint availability metrics do not work as expected due to a calculation error.

- RS219531: Upgrading a cluster from Redis Software version 7.2.x or 7.4.x to version 8.2.0 can fail. After the first node is upgraded, a node that still runs the earlier version can lose its replication link to the cluster configuration store. `rladmin` then reports `CCS ERROR: REPLICATION LINK DOWN`, and the upgrade of the next node fails with `Failed to sync with master ccs`.

    To upgrade a Redis Software 7.2.x or 7.4.x cluster, first upgrade it to Redis Software version 8.0.x, and then upgrade to version 8.2.0.
