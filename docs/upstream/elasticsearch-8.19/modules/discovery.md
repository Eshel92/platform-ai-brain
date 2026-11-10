<!-- Converted from modules/discovery.asciidoc (AsciiDoc). Includes are inlined. -->

## Discovery and cluster formation

The discovery and cluster formation processes are responsible for discovering
nodes, electing a master, forming a cluster, and publishing the cluster state
each time it changes.

The following processes and settings are part of discovery and cluster
formation:

discovery-hosts-providers::

    Discovery is the process where nodes find each other when the master is
    unknown, such as when a node has just started up or when the previous
    master has failed.

modules-discovery-quorums::

    How Elasticsearch uses a quorum-based voting mechanism to
    make decisions even if some nodes are unavailable.

modules-discovery-voting::

    How Elasticsearch automatically updates voting configurations as nodes leave and join
    a cluster.

modules-discovery-bootstrap-cluster::

    Bootstrapping a cluster is required when an Elasticsearch cluster starts up
    for the very first time. In development mode, with no
    discovery settings configured, this is automatically performed by the nodes
    themselves. As this auto-bootstrapping is
    inherently unsafe, running a node in
    production mode requires bootstrapping to be
    explicitly configured.

Adding and removing master-eligible nodes::

    It is recommended to have a small and fixed number of master-eligible nodes
    in a cluster, and to scale the cluster up and down by adding and removing
    master-ineligible nodes only. However there are situations in which it may
    be desirable to add or remove some master-eligible nodes to or from a
    cluster. This section describes the process for adding or removing
    master-eligible nodes, including the extra steps that need to be performed
    when removing more than half of the master-eligible nodes at the same time.

cluster-state-publishing::

    Cluster state publishing is the process by which the elected master node
    updates the cluster state on all the other nodes in the cluster.

cluster-fault-detection::

    Elasticsearch performs health checks to detect and remove faulty nodes.

Settings::

    There are settings that enable users to influence the discovery, cluster
    formation, master election and fault detection processes.

(See `modules/discovery/discovery.md`)
(See `modules/discovery/quorums.md`)
(See `modules/discovery/voting.md`)
(See `modules/discovery/bootstrapping.md`)
(See `modules/discovery/publishing.md`)
(See `modules/discovery/fault-detection.md`)
