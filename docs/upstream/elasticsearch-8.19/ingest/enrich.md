<!-- Converted from ingest/enrich.asciidoc (AsciiDoc). Includes are inlined. -->

## Enrich your data

You can use the enrich processor to add data from your
existing indices to incoming documents during ingest.

For example, you can use the enrich processor to:

* Identify web services or vendors based on known IP addresses
* Add product information to retail orders based on product IDs
* Supplement contact information based on an email address
* Add postal codes based on user coordinates

### How the enrich processor works

Most processors are self-contained and only change _existing_ data in incoming
documents.

(Figure: images/ingest/ingest-process.svg)

The enrich processor adds _new_ data to incoming documents and requires a few
special components:

(Figure: images/ingest/enrich/enrich-process.svg)

enrich policy::
A set of configuration options used to add the right enrich data to the right
incoming documents.

An enrich policy contains:

* A list of one or more _source indices_ which store enrich data as documents
* The _policy type_ which determines how the processor matches the enrich data
  to incoming documents
* A _match field_ from the source indices used to match incoming documents
* _Enrich fields_ containing enrich data from the source indices you want to add
  to incoming documents

Before it can be used with an enrich processor, an enrich policy must be
executed. When executed, an enrich policy uses
enrich data from the policy's source indices to create a streamlined system
index called the _enrich index_. The processor uses this index to match and
enrich incoming documents.

source index::
An index which stores enrich data you'd like to add to incoming documents. You
can create and manage these indices just like a regular Elasticsearch index. You can use
multiple source indices in an enrich policy. You also can use the same source
index in multiple enrich policies.

enrich index::
A special system index tied to a specific enrich policy.

Directly matching incoming documents to documents in source indices could be
slow and resource intensive. To speed things up, the enrich processor uses an
enrich index.

Enrich indices contain enrich data from source indices but have a few special
properties to help streamline them:

* They are system indices, meaning they're managed internally by Elasticsearch and only
  intended for use with enrich processors and the ES|QL `ENRICH` command.
* They always begin with `.enrich-*`.
* They are read-only, meaning you can't directly change them.
* They are force merged for fast retrieval.

### Set up an enrich processor

To set up an enrich processor, follow these steps:

. Check the prerequisites.
. create-enrich-source-index.
. create-enrich-policy.
. execute-enrich-policy.
. add-enrich-processor.
. ingest-enrich-docs.

Once you have an enrich processor set up,
you can update your enrich data
and update your enrich policies.

**Important:**
The enrich processor performs several operations and may impact the speed of
your ingest pipeline.

We strongly recommend testing and benchmarking your enrich processors
before deploying them in production.

We do not recommend using the enrich processor to append real-time data.
The enrich processor works best with reference data
that doesn't change frequently.

#### Prerequisites

To use enrich policies, you must have:

* `read` index privileges for any indices used
* The `enrich_user` built-in role

#### Add enrich data

To begin, add documents to one or more source indices. These documents should
contain the enrich data you eventually want to add to incoming data.

You can manage source indices just like regular Elasticsearch indices using the
document and index APIs.

You also can set up {beats-ref}/getting-started.html[Beats], such as a
{filebeat-ref}/filebeat-installation-configuration.html[{filebeat}], to
automatically send and index documents to your source indices. See
{beats-ref}/getting-started.html[Getting started with Beats].

#### Create an enrich policy

After adding enrich data to your source indices, use the
create enrich policy API or
Index Management in Kibana to create an enrich policy.

**Warning:**
Once created, you can't update or change an enrich policy.
See update-enrich-policies.

#### Execute the enrich policy

Once the enrich policy is created, you need to execute it using the
execute enrich policy API or
Index Management in Kibana to create an
enrich index.

(Figure: images/ingest/enrich/enrich-policy-index.svg)

The _enrich index_ contains documents from the policy's source indices.
Enrich indices always begin with `.enrich-*`,
are read-only,
and are force merged.

**Warning:**
Enrich indices should only be used by the enrich processor
or the ES|QL `ENRICH` command. Avoid using enrich indices for
other purposes.

#### Add an enrich processor to an ingest pipeline

Once you have source indices, an enrich policy, and the related enrich index in
place, you can set up an ingest pipeline that includes an enrich processor for
your policy.

(Figure: images/ingest/enrich/enrich-processor.svg)

Define an enrich processor and add it to an ingest
pipeline using the create or update pipeline API.

When defining the enrich processor, you must include at least the following:

* The enrich policy to use.
* The field used to match incoming documents to the documents in your enrich index.
* The target field to add to incoming documents. This target field contains the
match and enrich fields specified in your enrich policy.

You also can use the `max_matches` option to set the number of enrich documents
an incoming document can match. If set to the default of `1`, data is added to
an incoming document's target field as a JSON object. Otherwise, the data is
added as an array.

See enrich-processor for a full list of configuration options.

You also can add other processors to your ingest pipeline.

#### Ingest and enrich documents

You can now use your ingest pipeline to enrich and index documents.

(Figure: images/ingest/enrich/enrich-process.svg)

Before implementing the pipeline in production, we recommend indexing a few test
documents first and verifying enrich data was added correctly using the
get API.

#### Update an enrich index

Once created, you cannot update 
or index documents to an enrich index.
Instead, update your source indices
and execute the enrich policy again.
This creates a new enrich index from your updated source indices. 
The previous enrich index will deleted with a delayed maintenance job. 
By default this is done every 15 minutes. 
If wanted, you can reindex
or update any already ingested documents
using your ingest pipeline.

#### Update an enrich policy

Once created, you can't update or change an enrich policy.
Instead, you can:

. Create and execute a new enrich policy.

. Replace the previous enrich policy
    with the new enrich policy
    in any in-use enrich processors or ES|QL queries.

. Use the delete enrich policy API or
Index Management in Kibana
    to delete the previous enrich policy.

#### Enrich components

The enrich coordinator is a component that manages and performs the searches
required to enrich documents on each ingest node. It combines searches from all enrich
processors in all pipelines into bulk multi-searches.

The enrich policy executor is a component that manages the executions of all
enrich policies. When an enrich policy is executed, this component creates
a new enrich index and removes the previous enrich index. The enrich policy
executions are managed from the elected master node. The execution of these
policies occurs on a different node.

#### Node Settings

The `enrich` processor has node settings for enrich coordinator and
enrich policy executor.

The enrich coordinator supports the following node settings:

`enrich.cache_size`::
Maximum size of the cache that caches searches for enriching documents.
The size can be specified in three units: the raw number of
cached searches (e.g. `1000`), an absolute size in bytes (e.g. `100Mb`),
or a percentage of the max heap space of the node (e.g. `1%`).
Both for the absolute byte size and the percentage of heap space,
Elasticsearch does not guarantee that the enrich cache size will adhere exactly to that maximum,
as Elasticsearch uses the byte size of the serialized search response
which is is a good representation of the used space on the heap, but not an exact match.
Defaults to `1%`. There is a single cache for all enrich processors in the cluster.

`enrich.coordinator_proxy.max_concurrent_requests`::
Maximum number of concurrent multi-search requests to
run when enriching documents. Defaults to `8`.

`enrich.coordinator_proxy.max_lookups_per_request`::
Maximum number of searches to include in a <<search-multi-search,multi-search
request>> when enriching documents. Defaults to `128`.

The enrich policy executor supports the following node settings:

`enrich.fetch_size`::
Maximum batch size when reindexing a source index into an enrich index. Defaults
to `10000`.

`enrich.max_force_merge_attempts`::
Maximum number of force merge attempts allowed on an
enrich index. Defaults to `3`.

`enrich.cleanup_period`::
How often Elasticsearch checks whether unused enrich indices can be deleted. Defaults to
`15m`.

`enrich.max_concurrent_policy_executions`::
Maximum number of enrich policies to execute concurrently. Defaults to `50`.

(See `ingest/geo-match-enrich-policy-type-ex.md`)
(See `ingest/match-enrich-policy-type-ex.md`)
(See `ingest/range-enrich-policy-type-ex.md`)
