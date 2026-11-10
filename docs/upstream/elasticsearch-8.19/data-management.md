<!-- Converted from data-management.asciidoc (AsciiDoc). Includes are inlined. -->

# Data management

The data you store in Elasticsearch generally falls into one of two categories:

* *Content*: a collection of items you want to search, such as a catalog of products
* *Time series data*: a stream of continuously-generated timestamped data, such as log entries
*Content* might be frequently updated,
but the value of the content remains relatively constant over time.
You want to be able to retrieve items quickly regardless of how old they are.

*Time series data* keeps accumulating over time, so you need strategies for
balancing the value of the data against the cost of storing it.
As it ages, it tends to become less important and less-frequently accessed,
so you can move it to less expensive, less performant hardware.
For your oldest data, what matters is that you have access to the data.
It's ok if queries take longer to complete.

To help you manage your data, Elasticsearch offers you the following options:

* Index lifecycle management
* Data stream lifecycle
* {curator-ref-current}/about.html[Elastic Curator]

**ILM** can be used to manage both indices and data streams. It allows you to do the following:

* Define the retention period of your data. The retention period is the minimum time your data will be stored in Elasticsearch.
Data older than this period can be deleted by Elasticsearch.
* Define multiple tiers of data nodes with different performance characteristics.
* Automatically transition indices through the data tiers according to your performance needs and retention policies.
* Leverage searchable snapshots stored in a remote repository to provide resiliency
for your older indices while reducing operating costs and maintaining search performance.
* Perform asynchronous searches of data stored on less-performant hardware.

**Data stream lifecycle** is less feature rich but is focused on simplicity. It allows you to do the following:

* Define the retention period of your data. The retention period is the minimum time your data will be stored in Elasticsearch.
Data older than this period can be deleted by Elasticsearch at a later time.
* Improve the performance of your data stream by performing background operations that will optimise the way your data stream is stored.

**Elastic Curator** is a tool that allows you to manage your indices and snapshots using user-defined filters and predefined actions. If ILM provides the functionality to manage your index lifecycle, and you have at least a Basic license, consider using ILM in place of Curator. Many stack components make use of ILM by default. {curator-ref-current}/ilm.html[Learn more].

**Note:** Data rollup is a deprecated Elasticsearch feature that allows you to manage the amount of data that is stored in your cluster, similar to the downsampling functionality of ILM and data stream lifecycle. This feature should not be used for new deployments.

**Tip:**
ILM is not available on {es-serverless}.

In an Elastic Cloud or self-managed environment, ILM lets you automatically transition indices through data tiers according to your performance needs and retention requirements. This allows you to balance hardware costs with performance. {es-serverless} eliminates this complexity by optimizing your cluster performance for you.

Data stream lifecycle is an optimized lifecycle tool that lets you focus on the most common lifecycle management needs, without unnecessary hardware-centric concepts like data tiers.

(See `ilm/index.md`)
(See `datatiers.md`)
