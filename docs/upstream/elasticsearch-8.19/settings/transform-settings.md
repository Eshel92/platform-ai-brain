<!-- Converted from settings/transform-settings.asciidoc (AsciiDoc). Includes are inlined. -->

### Transforms  settings in Elasticsearch

You do not need to configure any settings to use transforms. It is enabled by
default.

#### General transforms settings

`node.roles: [ transform ]`::
(Static) Set `node.roles` to contain `transform` to
identify the node as a _transform node_. If you want to run transforms, there
must be at least one transform node in your cluster.
If you set `node.roles`, you must explicitly specify all the required roles for
the node. To learn more, refer to modules-node.
**Important:** It is strongly recommended that dedicated transform nodes also have
the `remote_cluster_client` role; otherwise, cross-cluster search fails when used in
transforms. See remote-node.

`xpack.transform.enabled`::
deprecated:[7.8.0,Basic License features should always be enabled]
(Static) This deprecated setting no longer has any
effect.

`xpack.transform.num_transform_failure_retries`::
(Dynamic) The number of times that a transform
retries when it experiences a non-fatal error. Once the number of retries is
exhausted, the transform task is marked as `failed`. The default value is `10`
with a valid minimum of `0` and maximum of `100`. If a transform is already
running, it has to be restarted to use the changed setting.
The `num_failure_retries` setting can also be specified on an individual transform level.
Specifying this setting for each transform individually is recommended.
