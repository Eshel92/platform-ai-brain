<!-- Converted from tutorial/backup-sharded-cluster-metadata.txt (reStructuredText). Includes are inlined. -->

# Back Up Self-Managed Cluster Metadata

This procedure shuts down the `mongod` instance of a
config server in order to create a
backup of a :sharded cluster's
metadata. The cluster's config servers store all of the cluster's
metadata, most importantly the mapping from chunks to
shards.

When you perform this procedure, the cluster remains operational
[#read-only]_.

#. Disable the cluster balancer process temporarily. See
   sharding-balancing-disable-temporarily for more information.

#. Shut down one of the config databases.

#. Create a full copy of the data files (i.e. the path specified by
   the `dbPath` option for the config instance.)

#. Restart the original configuration server.

#. Re-enable the balancer to allow the cluster to resume normal
   balancing operations. See the
   sharding-balancing-disable-temporarily section for more
   information on managing the balancer process.

**See also:**

/core/backups
