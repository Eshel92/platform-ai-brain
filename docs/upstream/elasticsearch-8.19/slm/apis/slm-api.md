<!-- Converted from slm/apis/slm-api.asciidoc (AsciiDoc). Includes are inlined. -->

## Snapshot lifecycle management APIs

**New API reference**
For the most up-to-date API details, refer to [Snapshot lifecycle management APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-slm).

You use the following APIs to set up policies to automatically take snapshots and 
control how long they are retained.

For more information about snapshot lifecycle management (SLM), see automate-snapshots-slm.

### Policy management APIs

* Create lifecycle policy
* Get lifecycle policy
* Delete lifecycle policy

### Snapshot management APIs

* Execute snapshot lifecycle policy (take snapshots)
* Execute snapshot retention policy (delete expired snapshots)

### Operation management APIs

* Get SLM status
* Get global and policy-level action statistics
* Start SLM
* Stop SLM

(See `slm/apis/slm-put.md`)
(See `slm/apis/slm-get.md`)
(See `slm/apis/slm-delete.md`)
(See `slm/apis/slm-execute.md`)
(See `slm/apis/slm-execute-retention.md`)
(See `slm/apis/slm-get-status.md`)
(See `slm/apis/slm-stats.md`)
(See `slm/apis/slm-start.md`)
(See `slm/apis/slm-stop.md`)
