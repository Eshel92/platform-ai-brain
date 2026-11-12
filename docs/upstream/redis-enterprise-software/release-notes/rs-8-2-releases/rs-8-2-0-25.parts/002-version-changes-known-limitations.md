<!-- Part 2 of 3 of release-notes/rs-8-2-releases/rs-8-2-0-25.md (split because the page is big). -->

## Version changes

### Breaking changes

Redis Software version 8.2.0 introduces the following breaking changes:

- **Local import from Redis Software system directories is no longer supported.** To improve security, database imports that use the `mount_point` source can no longer read files from Redis Software system directories, including `/opt/redislabs`, `/var/opt/redislabs`, `/etc/opt/redislabs`, and any of their subdirectories.

    - Import operations that reference files in these directories now fail.

    - Store import files in a non-system location accessible to Redis Software before you start the import.

- **`smtp_password` is now a write-only field in the Cluster API.** To improve security, the API no longer returns the SMTP password in responses to `GET /v1/cluster`, and the Cluster Manager UI no longer reads or displays the existing password.

    - Applications or scripts that previously expected `smtp_password` to be returned by the Cluster API no longer receive this field.

    - When you update SMTP settings, the existing password cannot be retrieved. To change the SMTP password, provide a new password as part of the update request.

- **Custom module upload is disabled by default.** To improve security, custom (user-defined) module uploads are now disabled by default. A new cluster setting, `allow_modules_upload`, controls access to the custom module upload APIs. When this setting is disabled (the default), requests to `POST /v2/modules/user-defined` and `POST /v2/local/modules/user-defined/artifacts` return `403 modules_upload_disabled`, regardless of user role.

    - To enable custom module uploads, set `allow_modules_upload` to `true` with a `PUT /v1/cluster` request.

    - Applications or automation that call the custom module upload APIs directly receive a `403 modules_upload_disabled` response until the setting is enabled.

    - Existing functionality for listing, deleting, and loading modules is unchanged.

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

### Deprecations

- The `db_conns_auditing` cluster policy and database configuration field is deprecated. Use the `audit_settings.audit_mode` field instead. Setting `db_conns_auditing` to `true` is equivalent to setting `audit_mode` to `connection`. See [Audit events](/content/operate/rs/security/audit-events.md) for the current auditing configuration.

- The `gradual_src_mode`, `gradual_sync_mode`, and `gradual_sync_max_shards_per_source` parameters are deprecated. Use `gradual_sync_policy` instead. You can set it with [`rladmin tune db`](/content/operate/rs/references/cli-utilities/rladmin/tune.md) or the REST API.

    > [!WARNING]
    > Upgrading to Redis Software version 8.2 can overwrite these settings. Contact Redis Support before you upgrade if any of them differ from these values:
    >
    > - `gradual_sync_mode`: `auto` or `enabled`
    > - `gradual_src_mode`: `disabled`
    > - `gradual_src_max_sources`: `1`
    > - `gradual_sync_max_shards_per_source`: `1`
    >
    > To check the current values, run [`rladmin info db`](/content/operate/rs/references/cli-utilities/rladmin/info.md#info-db).

- The `old_password` field in `POST /v1/users/password` and `PUT /v1/users/password` requests is deprecated and ignored. It was optional and had no effect when adding or resetting a password, so you can remove it from these requests. `old_password` is still required for `DELETE /v1/users/password`, which uses it to identify the password to delete.

- The following REST API fields, deprecated since Redis Software version 6.4.2, are removed in this release:

    - `use_ipv6` (cluster object) — use `use_external_ipv6` instead.

    - `redis_cleanup_job_settings` (job scheduler object) — use `persistence_cleanup_scan_interval` instead.

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

| Package | SHA256 checksum (8.2.0-25 July release) |
|---------|---------------------------------------|
| Ubuntu 20 | <span class="break-all">e68acba411779c2a1ea419305e42d31d007959ed7dfe31cc7624a0ed34cee9ed</span> |
| Ubuntu 22 (amd64) | <span class="break-all">9113dc664965aaff8844b212a6625eda350c935eb8b436cb233194f213bc0893</span> |
| Ubuntu 22 (arm64) | <span class="break-all">a0611bc21fb97742100e8529f2ff56c4986175dedfa674e6abfba4e30bc7fc9a</span> |
| Red Hat Enterprise Linux (RHEL) 8 | <span class="break-all">b0729139cf8cde0eb93e85b8e8fae82cf5b1e35d78eba972877148ee7f879186</span> |
| Red Hat Enterprise Linux (RHEL) 9 (amd64) | <span class="break-all">b4c540c9ed785a26af90e54e196d12c3ccb9e10ca8498fe9c17f2dcbbb2c6420</span> |
| Red Hat Enterprise Linux (RHEL) 9 (arm64) | <span class="break-all">62aff83e8ff44ebd0ae9b7b94bd6fa815d2274fe8143d980e290c5daca64c0c6</span> |
| Red Hat Enterprise Linux (RHEL) 9 FIPS (amd64) | <span class="break-all">1cb61db526cd1231b6cbbc79f1087c3c9afce7f0f578c5c5f55c9972b5b05462</span> |
| Amazon Linux 2023 (amd64) | <span class="break-all">17ba316aaa3a59ac217453b470e89b95ec639e53e09bd3be47326b6869080c44</span> |
| Amazon Linux 2023 (arm64) | <span class="break-all">f4a3e5ee809a17ed1bf3b4ef54b0799df65102ac1829eac48655767441ed6219</span> |


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
