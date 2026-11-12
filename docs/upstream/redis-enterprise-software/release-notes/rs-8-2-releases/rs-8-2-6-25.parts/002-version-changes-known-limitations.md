<!-- Part 2 of 3 of release-notes/rs-8-2-releases/rs-8-2-6-25.md (split because the page is big). -->

## Version changes

### JWT token invalidation on upgrade

To improve system security, the JWT signing secret has changed in version 8.0.22 and later. As a result, upgrading invalidates all previously issued JWT tokens, which must be regenerated. Tokens used programmatically within the cluster are regenerated automatically. Cluster Manager users must sign out and sign in again, or wait for their session or token to expire.

### SAML SSO role mappings on upgrade

Redis Software versions earlier than 8.2.6 read `redisRoleMapping` only when they created a user with JIT provisioning, so the attribute might have been removed since. After the upgrade, JIT-provisioned users without a valid mapping can't sign in, and their roles are removed. Roles you changed in Redis Software for these users are replaced at their next sign-in.

Before you upgrade, make sure:

- Your identity provider sends `redisRoleMapping` with valid role UIDs for every user created with JIT provisioning.

- The cluster has at least one admin user that you created in Redis Software instead of through JIT provisioning. Redis Software removes a JIT-provisioned user's roles even if that user is the cluster's only admin.

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

### Deprecations

- The `max_redis_forks` cluster and node setting is deprecated and no longer limits concurrent `redis-server` fork operations on a node, such as BGSAVE, AOF rewrite, full sync, and backup or export. The setting could previously cause database backups to fail indefinitely.

    Existing automation that sets `max_redis_forks` with [`rladmin tune`](/content/operate/rs/references/cli-utilities/rladmin/tune.md) or the REST API keeps running without errors, but the setting has no effect. To limit full-sync concurrency, use `max_slave_full_syncs` instead.

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

| Package | SHA256 checksum (8.2.6-25 October release) |
|---------|---------------------------------------|
| Ubuntu 20 | <span class="break-all">28ace57b01bac0de4f3847ba29e4e0710c0e1b6d9464254b398ad76738b80734</span> |
| Ubuntu 22 (amd64) | <span class="break-all">27dad5afff38d98da3db869023394ba74f746a127eaf20cf50910949a4903118</span> |
| Ubuntu 22 (arm64) | <span class="break-all">7be4617206cb2ad9865c833ab88b48f31c5bf6097aac5c9888a52508ea96ed27</span> |
| Red Hat Enterprise Linux (RHEL) 8 | <span class="break-all">bdbd7eafd22e58b83027ac97ecf3ae4fcdea99eeeaa762af2da3fbdc39226735</span> |
| Red Hat Enterprise Linux (RHEL) 9 (amd64) | <span class="break-all">51bc922cda44c389b02202e40d099a893ac506e5fa4686f3544ebdb3b56d1428</span> |
| Red Hat Enterprise Linux (RHEL) 9 (arm64) | <span class="break-all">d13f2441510be19721737ec4676a0e6eff7584edc7b2f6824c1c9c96cef31f07</span> |
| Red Hat Enterprise Linux (RHEL) 9 FIPS (amd64) | <span class="break-all">eea84da171493780dfb4286e80053b3ed41114d998954c879331d4d918a097e0</span> |
| Amazon Linux 2023 (amd64) | <span class="break-all">abf699f8f57a52cf37ce4acd7b14dee58f724c364dddaa08e841a3f9b08d6d21</span> |
| Amazon Linux 2023 (arm64) | <span class="break-all">9119619374adf2921074766c9d0807c166c2125e3d9285fa09b7184b3851ceba</span> |


## Known issues

- RS155734: Endpoint availability metrics do not work as expected due to a calculation error.


## Known limitations

#### Active-Active database updates rejected after upgrading to 8.2.6

On clusters running versions earlier than 8.2.6, a cluster master failover (for example, during a Kubernetes operator upgrade) can interrupt a change to an Active-Active database while the change is in progress. After the upgrade to 8.2.6, updates to that database can still be rejected with 409 – Another operation is already in progress. This only happens if the configuration change started within seconds of the failover.

Workaround: Before you upgrade, wait until all pending Active-Active database changes have finished.

#### TimeSeries and Search command failures during online module upgrades

During an online module upgrade, Redis Software can temporarily reject TimeSeries and Search commands across the database, including commands for healthy shards. Rejected commands return the error `ERR could not perform command '<command>' because shards topology update is either transient or has failed`. Rejected writes are not applied and are not retried automatically. Commands succeed again after the topology update reaches all primary shards.

Schedule module upgrades during a maintenance window. Make sure applications handle this error, retry eligible operations, and do not treat a rejected write as successful.

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
