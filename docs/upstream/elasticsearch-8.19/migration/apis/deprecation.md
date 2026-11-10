<!-- Converted from migration/apis/deprecation.asciidoc (AsciiDoc). Includes are inlined. -->

### Deprecation info APIs

**New API reference**
For the most up-to-date API details, refer to [Migration APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-migration).

**Tip:** These APIs are designed for indirect use by Kibana's **Upgrade Assistant**.
We strongly recommend you use the **Upgrade Assistant** to upgrade from
{prev-major-last} to {version}. For upgrade instructions, refer to
{stack-ref}/upgrading-elastic-stack.html[Upgrading to Elastic {version}].
The deprecation API is to be used to retrieve information about different
cluster, node, and index level settings that use deprecated features that will
be removed or changed in a future version.

#### Request

`GET /_migration/deprecations` +

`GET /<target>/_migration/deprecations`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
cluster privilege to use this API.

#### Path parameters

`<target>`::
(Optional, string)
Comma-separate list of data streams or indices to check. Wildcard (`*`)
expressions are supported.
When you specify this parameter, only deprecations for the specified
data streams or indices are returned.

#### Settings

You can use the following settings to control the behavior of the deprecation info API:

**Note:** This setting is designed for indirect use by {ess-trial}[Elasticsearch Service], {ece-ref}[Elastic Cloud Enterprise], and {eck-ref}[Elastic Cloud on Kubernetes].
Direct use is not supported.

`deprecation.skip_deprecated_settings`
(Dynamic)
Defaults to an empty list. Set to a list of setting names to be ignored by the deprecation info API. Any
deprecations related to settings in this list will not be returned by the API. Simple wildcard matching is supported.

#### Examples

To see the list of offenders in your cluster, submit a GET request to the
`_migration/deprecations` endpoint:

```console
GET /_migration/deprecations
```

Example response:

```
{
  "cluster_settings" : [
    {
      "level" : "critical",
      "message" : "Cluster name cannot contain ':'",
      "url" : "{ref-70}/breaking-changes-7.0.html#_literal_literal_is_no_longer_allowed_in_cluster_name",
      "details" : "This cluster is named [mycompany:logging], which contains the illegal character ':'."
    }
  ],
  "node_settings" : [ ],
  "index_settings" : {
    "logs:apache" : [
      {
        "level" : "warning",
        "message" : "Index name cannot contain ':'",
        "url" : "{ref-70}/breaking-changes-7.0.html#_literal_literal_is_no_longer_allowed_in_index_name",
        "details" : "This index is named [logs:apache], which contains the illegal character ':'."
      }
    ]
  },
  "ml_settings" : [ ]
}
```

The response breaks down all the specific forward-incompatible settings that you
should resolve before upgrading your cluster. Any offending settings are
represented as a deprecation warning.

The following is an example deprecation warning:

```
{
  "level" : "warning",
  "message" : "This is the generic descriptive message of the breaking change",
  "url" : "{ref-60}/breaking_60_indices_changes.html",
  "details" : "more information, like which nodes, indices, or settings are to blame"
}
```

As is shown, there is a `level` property that describes the significance of the
issue.

|=======
|warning | You can upgrade directly, but you are using deprecated functionality
which will not be available or behave differently in a future version.
|critical | You cannot upgrade without fixing this problem.
|=======

The `message` property and the optional `details` property provide descriptive
information about the deprecation warning. The `url` property provides a link to
the Breaking Changes Documentation, where you can find more information about
this change.

Any cluster-level deprecation warnings can be found under the `cluster_settings`
key. Similarly, any node-level warnings are found under `node_settings`. Since
only a select subset of your nodes might incorporate these settings, it is
important to read the `details` section for more information about which nodes
are affected. Index warnings are sectioned off per index and can be filtered
using an index-pattern in the query. This section includes warnings for the
backing indices of data streams specified in the request path. Machine Learning
related deprecation warnings can be found under the `ml_settings` key.

The following example request shows only index-level deprecations of all
`logstash-*` indices:

```console
GET /logstash-*/_migration/deprecations
```
