<!-- Converted from ccr/apis/ccr-apis.asciidoc (AsciiDoc). Includes are inlined. -->

## Cross-cluster replication APIs

**New API reference**
For the most up-to-date API details, refer to [Cross-cluster replication APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ccr).

You can use the following APIs to perform cross-cluster replication operations.

### Top-Level

* Get cross-cluster replication stats

### Follow

* Create follower index
* Pause follower
* Resume follower
* Convert follower index to a regular index
* Remove follower retention leases from the leader
* Get stats about follower indices
* Get info about follower indices

### Auto-follow

* Create auto-follow pattern
* Delete auto-follow pattern
* Get auto-follow patterns
* Pause auto-follow pattern
* Resume auto-follow pattern

(See `ccr/apis/get-ccr-stats.md`)
(See `ccr/apis/follow/put-follow.md`)
(See `ccr/apis/follow/post-pause-follow.md`)
(See `ccr/apis/follow/post-resume-follow.md`)
(See `ccr/apis/follow/post-unfollow.md`)
(See `ccr/apis/follow/post-forget-follower.md`)
(See `ccr/apis/follow/get-follow-stats.md`)
(See `ccr/apis/follow/get-follow-info.md`)
(See `ccr/apis/auto-follow/put-auto-follow-pattern.md`)
(See `ccr/apis/auto-follow/delete-auto-follow-pattern.md`)
(See `ccr/apis/auto-follow/get-auto-follow-pattern.md`)
(See `ccr/apis/auto-follow/pause-auto-follow-pattern.md`)
(See `ccr/apis/auto-follow/resume-auto-follow-pattern.md`)
