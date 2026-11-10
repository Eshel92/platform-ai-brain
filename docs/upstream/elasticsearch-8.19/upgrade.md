<!-- Converted from upgrade.asciidoc (AsciiDoc). Includes are inlined. -->

# Upgrade Elasticsearch

**Important:** This documentation is for Elasticsearch {version}, which is not yet released.
You can upgrade from a previously released version to a pre-release build, if
following a supported upgrade path. Upgrading from a pre-release build to any
other build is not supported, and can result in errors or silent data loss. If
you run a pre-release build for testing, discard the contents of the cluster
before upgrading to another build of Elasticsearch.

Elasticsearch clusters can usually be upgraded one node at a time so upgrading does not
interrupt service. For upgrade instructions, refer to
{stack-ref}/upgrading-elastic-stack.html[Upgrading to Elastic {version}].

**Upgrade from 7.x**
**Important:** To upgrade to {version} from 7.16 or an earlier version, **you must
first upgrade to {prev-major-last}**, even if you opt to do a full-cluster
restart instead of a rolling upgrade. This enables you to use the **Upgrade
Assistant** to identify and resolve issues, reindex indices created before 7.0,
and then perform a rolling upgrade. You must resolve all critical issues before
proceeding with the upgrade. For instructions, refer to
{stack-ref}/upgrading-elastic-stack.html#prepare-to-upgrade[Prepare to upgrade
from 7.x].

### Out-of-order releases

Elastic maintains several minor versions of Elasticsearch at once. This means releases
do not always happen in order of their version numbers. You can only upgrade to
{version} if the version you are currently running meets both of these
conditions:

* Has an older version number than {version}.
* Has an earlier release date than {version}.

If you are currently running a version with an older version number but a later
release date than {version}, wait for a newer release before upgrading.

### Index compatibility

Elasticsearch has full query and write support for indices created in the previous major
version. If you have indices created in 6.x or earlier, you might use the
archive functionality to import them into newer Elasticsearch
versions, or you must reindex or delete them before upgrading to {version}.
Elasticsearch nodes will fail to start if incompatible indices are present.
Snapshots of 6.x or earlier indices can only restored using the
archive functionality to a 8.x cluster even if they
were created by a 7.x cluster.
The **Upgrade Assistant** in {prev-major-last} identifies any indices
that need to be reindexed or removed.

### REST API compatibility

REST API compatibility is a per-request opt-in
feature that can help REST clients mitigate non-compatible (breaking) changes to
the REST API.

### FIPS Compliance and Java 17

Elasticsearch 8.0 requires Java 17 or later. Elasticsearch 8.13 has been tested with [Bouncy Castle](https://www.bouncycastle.org/java.html)'s Java 17
[certified](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4616) FIPS implementation and is the
recommended Java security provider when running Elasticsearch in FIPS 140-2 mode.
Note - Elasticsearch does not ship with a FIPS certified security provider and requires explicit installation and configuration.

Alternatively, consider using Elasticsearch Service in the
[FedRAMP-certified GovCloud region](https://www.elastic.co/industries/public-sector/fedramp).

(See `upgrade/archived-settings.md`)
(See `upgrade/archive-indices.md`)
