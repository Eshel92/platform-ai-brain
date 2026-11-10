<!-- Converted from tab-widgets/snapshot-repo-widget.asciidoc (AsciiDoc). Includes are inlined. -->

When you create a cluster, Elasticsearch Service automatically registers a default
{cloud}/ec-snapshot-restore.html[`found-snapshots`] repository. This repository
supports {search-snaps}.

The `found-snapshots` repository is specific to your cluster. To use another
cluster's default repository, refer to the Cloud
{cloud}/ec-snapshot-restore.html[Snapshot and restore] documentation.

You can also use any of the following custom repository types with {search-snaps}:

* {cloud}/ec-gcs-snapshotting.html[Google Cloud Storage (GCS)]
* {cloud}/ec-azure-snapshotting.html[Azure Blob Storage]
* {cloud}/ec-aws-custom-repository.html[Amazon Web Services (AWS)]

Use any of the following repository types with searchable snapshots:

* AWS S3
* Google Cloud Storage
* Azure Blob Storage
* {plugins}/repository-hdfs.html[Hadoop Distributed File Store (HDFS)]
* Shared filesystems such as NFS
* Read-only HTTP and HTTPS repositories

You can also use alternative implementations of these repository types, for
instance MinIO, as long as they are fully compatible.
Use the repo-analysis-api API to analyze your repository's suitability for
use with searchable snapshots.
