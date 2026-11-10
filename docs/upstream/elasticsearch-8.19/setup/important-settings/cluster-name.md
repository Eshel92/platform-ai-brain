<!-- Converted from setup/important-settings/cluster-name.asciidoc (AsciiDoc). Includes are inlined. -->

#### Cluster name setting

A node can only join a cluster when it shares its `cluster.name` with all the
other nodes in the cluster. The default name is `elasticsearch`, but you should
change it to an appropriate name that describes the purpose of the cluster.

```yaml
cluster.name: logging-prod
```

**Important:** Do not reuse the same cluster names in different environments.
Otherwise, nodes might join the wrong cluster.

**Note:** Changing the name of a cluster requires a <<restart-cluster-full,full
cluster restart>>.
