<!-- Converted from rest-api/root.asciidoc (AsciiDoc). Includes are inlined. -->

## Root API

**New API reference**
For the most up-to-date API details, refer to [Info APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-info).

The Elasticsearch API's base url returns its basic build, 
version, and cluster information. 

```console
GET /
```

### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
`monitor`, `manage`, or `all`
cluster privilege to use this API.

### Response body

`name` ::
The responding Node's `name`.

`cluster_name` ::
The responding Cluster's `name`.

`cluster_uuid` ::
The responding Cluster's `uuid` as confirmed by 
Cluster State.

`version` ::
(object) 
Contains information about the running version of Elasticsearch.
+ properties of `version`
`number` ::
Version number of responding 
[Elasticsearch release](https://www.elastic.co/downloads/past-releases#elasticsearch).

`build_flavor` ::
Build flavor, e.g. `default`.

`build_type` ::
Build type corresponding to how 
<<install-elasticsearch,Elasticsearch was installed>, 
e.g. `docker`, `rpm`, `tar`.

`build_hash` ::
Elasticsearch's Git commit's SHA hash.

`build_date` ::
Elasticsearch's Git commit's date.

`build_snapshot` ::
If Elasticsearch's build was from a snapshot.

`lucene_version` ::
Version number of Elasticsearch's 
underlying Lucene software.

`minimum_wire_compatibility_version` ::
Minimum node version with which the responding node can 
communicate. Also minimum  version from which you can perform 
a Rolling Upgrade.

`minimum_index_compatibility_version` ::
Minimum index version with which the responding node can read 
from disk.

### Examples

The API returns the following response: 

```console-result
{
  "name": "instance-0000000000",
  "cluster_name": "my_test_cluster",
  "cluster_uuid": "5QaxoN0pRZuOmWSxstBBwQ",
  "version": {
    "build_date": "2024-02-01T13:07:13.727175297Z",
    "minimum_wire_compatibility_version": "7.17.0",
    "build_hash": "6185ba65d27469afabc9bc951cded6c17c21e3f3",
    "number": "8.12.1",
    "lucene_version": "9.9.2",
    "minimum_index_compatibility_version": "7.0.0",
    "build_flavor": "default",
    "build_snapshot": false,
    "build_type": "docker"
  },
  "tagline": "You Know, for Search"
}
```
