<!-- Converted from setup/important-settings/snapshot.asciidoc (AsciiDoc). Includes are inlined. -->

#### Cluster backups

In a disaster, snapshots can prevent permanent data loss.
Snapshot lifecycle management is the easiest way to take regular
backups of your cluster. For more information, see snapshots-take-snapshot.

**Warning:**
**Taking a snapshot is the only reliable and supported way to back up a
cluster.** You cannot back up an Elasticsearch cluster by making copies of the data
directories of its nodes. There are no supported methods to restore any data
from a filesystem-level backup. If you try to restore a cluster from such a
backup, it may fail with reports of corruption or missing files or other data
inconsistencies, or it may appear to have succeeded having silently lost some of
your data.
