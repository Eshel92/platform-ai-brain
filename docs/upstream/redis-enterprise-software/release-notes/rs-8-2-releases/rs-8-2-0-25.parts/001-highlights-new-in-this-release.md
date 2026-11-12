<!-- Part 1 of 3 of release-notes/rs-8-2-releases/rs-8-2-0-25.md (split because the page is big). -->

## Highlights

This version offers:

- Database-scoped management roles

- Data path command auditing

- FIPS 140-3 support


## New in this release

### Database-scoped management roles

You can now scope the `db_member` and `db_viewer` [management roles](/content/operate/rs/security/access-control/create-cluster-roles.md) to specific databases instead of granting access to every database in the cluster. This lets you give application or tenant teams management access to only their own databases in a shared cluster.

- To scope a role, specify the databases it applies to using the new `resources` field when you create or update a [role](/content/operate/rs/references/rest-api/objects/role.md). For example, `"resources": [{"type": "db", "uids": ["1", "2"]}]` scopes the role to databases `1` and `2`.

- Roles without a `resources` scope continue to apply to all databases, so existing roles are unaffected.

- Users assigned a database-scoped role see only their authorized databases in the Cluster Manager UI and REST API responses, including database lists, metrics, alerts, and event logs. Other databases are hidden.

### Data path command auditing

Redis Software now supports auditing of data path commands (CRUD operations), in addition to the existing connection auditing. This lets you record which commands run against a database, along with the connection and authentication context, and stream the audit records to an external audit destination for security monitoring and compliance.

- Enable auditing per database with the new `audit_settings` configuration, choosing to audit connection events only (`connection`) or both connection events and commands (`connection_and_crud`).

- Filter audited commands by username, source IP address, or both to control the volume of audit data.

- Monitor the auditing pipeline with new `audit_sink_*` metrics.

For more information, see [Audit events](/content/operate/rs/security/audit-events.md).

### FIPS 140-3 support

Redis Software supports deployments on RHEL 9 VMs and RHEL 9 containerized Redis on GKE using cryptographic libraries based on FIPS 140-3 validated modules, enabling the use of FIPS-approved cryptographic algorithms in supported environments.

- Install Redis Software on a RHEL 9 host that has FIPS mode enabled. See [Supported platforms](#supported-platforms) for the platforms that support FIPS mode.

- In FIPS mode, Redis Software uses only FIPS-approved cryptographic algorithms and cipher suites; non-approved ciphers and algorithms are blocked.

- Because FIPS mode fixes the allowed cipher suites, you cannot change the cluster's TLS cipher suites while FIPS mode is enabled. Requests to update them return a `tls_cipher_update_not_allowed` error.

For FIPS-mode limitations, see [Increased memory usage in FIPS mode](#increased-memory-usage-in-fips-mode) and [SFTP storage not supported in FIPS mode](#sftp-storage-not-supported-in-fips-mode).

### Enhancements

- **Disable Basic authentication for the REST API.** You can now disable Basic and Digest authentication for the cluster management REST API using the new `control_plane_basic_authentication` cluster setting. Basic authentication remains enabled by default; when you disable it, the cluster rejects Basic and Digest authentication on inbound REST API requests. Configure it with [`rladmin tune cluster`](/content/operate/rs/references/cli-utilities/rladmin/tune.md) or an [update cluster settings](/content/operate/rs/references/rest-api/requests/cluster/_index.md#put-cluster) REST API request. Cluster join and Active-Active (CRDB) management operations support certificate credentials when Basic and Digest authentication are disabled or unavailable. See [Disable basic authentication for the REST API](/content/operate/rs/security/access-control/disable-basic-authentication.md).

- **Expose database tags in metrics.** You can now expose selected [database tags](/content/operate/rs/databases/configure/db-tags.md) as labels in [v2 metrics](/content/operate/rs/monitoring/metrics_stream_engine/prometheus-metrics-v2.md) through a new `db_tags` metric, so you can group, filter, and alert on database metrics by your own tags. Enable it in the cluster's metrics configuration using the `expose_db_tags` and `metrics_tag_keys_exposed` settings.

- **Faster replica synchronization.** Redis Software now manages gradual (parallel) synchronization through a `gradual_sync_policy` that applies tuned defaults for common scenarios, such as migration, adding a replica, and Active-Active. This speeds up replica bootstrap in multi-node and multi-shard deployments, such as during upgrades and scaling events, while leaving small deployments unaffected. You can select a policy or set custom parameters with [`rladmin tune db`](/content/operate/rs/references/cli-utilities/rladmin/tune.md) or the REST API.

- **Certificate–cipher suite validation.** When you upload a cluster certificate, Redis Software now validates that the certificate is compatible with the configured cipher suites and rejects incompatible certificates at upload time, so mismatches are caught early instead of surfacing later. For example, uploading an ECDSA certificate while only RSA-authenticated cipher suites are configured now fails at upload. The check applies to the control-plane certificates (such as `api`, `cm`, and `metrics_exporter`) and to the proxy certificate against the data-path cipher suites. If an upload is rejected, update either the certificate or the configured cipher suites so they are compatible.

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

- RS200909: Fixed an issue where alert emails were not sent when the SMTP server was configured with STARTTLS and username/password authentication.

- RS199037: Fixed an issue where Active-Active (CRDB) shard creation could fail with an invalid CRDT key type error.

- RS199021: Fixed an issue where LDAP authentication could fail when a user's mapped group appeared beyond roughly the 100th entry in the group query results.

- RS199012: Fixed a memory leak in `dmcproxy` that could occur when a multi-key command received a local `MOVED` or `CROSSSLOT` response.

- RS198858: Added a readiness endpoint to the `envoy_control_plane` service to improve health reporting.

- RS197703: Fixed an issue where an exception during first-node bootstrap could leave a cluster partially created without its modules.

- RS196975: Fixed an issue where deleting and updating a user at the same time could corrupt the user record stored on the cluster, which was the underlying cause of cluster-wide ACL authentication failures.

- RS196954: Fixed an issue where a user configuration could become corrupted if it was deleted and updated concurrently, which broke ACL authentication for all databases on the cluster and prevented users from connecting.

- RS196903: Fixed an issue where upgrading a module could leave the shard manager stuck unless replica shards were stopped first.

- RS196225: Fixed an issue where LDAP filters that use an `OR` clause to match multiple attributes could fail to find a unique DN for some users after upgrading to Redis Software version 8.0.x.

- RS195811: Fixed an issue where the `search-workers-priority-bias-threshold` configuration could not be set at runtime.

- RS195106: Fixed a cluster upgrade issue where adding multiple nodes with a new version simultaneously to a cluster could cause node configuration data to be incorrectly deleted and lead to node addition failures.

- RS195089: Fixed an issue where a major reconfiguration of an Active-Active database could cause an unnecessary full synchronization across all participating clusters.

- RS194243: Fixed a memory leak in the Active-Active database syncer that could occur when a participating cluster became unavailable but was not removed from the CRDB configuration.

- RS193861: Fixed an issue where a cluster could become unresponsive after a node was redeployed.

- RS192993: Fixed an issue where creating a new user with just-in-time (JIT) provisioning could cause authentication to fail for all databases that use ACL-only authentication.

- RS192582: Fixed an issue where the creation of Redis 8.x Active-Active databases could fail when no modules were specified due to missing module semantic versions in requests.

- RS192405: Improved `dmcproxy` SSL handshake error messages to provide actionable context when a TLS version mismatch occurs.

- RS192048: Fixed an issue where a feature set incompatibility could cause a database upgrade to fail.

- RS191757: Fixed an issue where a replica shard could fail to replicate and block failover for an extended period.

- RS191347: Fixed an issue where an orphaned shard on a node could block maintenance mode and leave a database in an active-change-pending state.

- RS190875: Fixed an issue where ciphers that use SHA-1 could not be removed when FIPS mode was enabled. FIPS mode now excludes SHA and CHACHA20 from `control_cipher_suites`.

- RS188659: Fixed an issue where a valid IPv6 address could be misidentified as the localhost loopback address.

- RS181161: Fixed an issue where access control users in an error state could not be deleted.

- RS177787: Reduced the volume of message logs included in support packages.

- RS176225: Fixed an issue where a backup exported from a Memcached database could not be imported.

- RS148518: Fixed an issue where an SMTP server could not be configured to send email alerts.

- RS144017: Fixed an issue where synchronization could fail with a `-BUSYKEY Target key name already exists` error.
