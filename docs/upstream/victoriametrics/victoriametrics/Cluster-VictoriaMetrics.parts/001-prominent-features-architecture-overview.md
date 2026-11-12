<!-- Part 1 of 8 of victoriametrics/Cluster-VictoriaMetrics.md (split because the page is big). -->

## Prominent features

- Supports all the features of the [single-node version](https://github.com/VictoriaMetrics/VictoriaMetrics).
- Performance and capacity scale horizontally. See [these docs for details](#cluster-resizing-and-scalability).
- Supports multiple independent namespaces for time series data (aka multi-tenancy). See [these docs for details](#multitenancy).
- Supports replication. See [these docs for details](#replication-and-data-safety).

> It is recommended to use the [single-node version](https://github.com/VictoriaMetrics/VictoriaMetrics) for ingestion rates
> lower than a million data points per second. The single-node version [scales perfectly](https://medium.com/@valyala/measuring-vertical-scalability-for-time-series-databases-in-google-cloud-92550d78d8ae)
> with the number of CPU cores, RAM and available storage space and can be set up in [High Availability](https://docs.victoriametrics.com/victoriametrics/#high-availability) mode.
> The single-node version is easier to configure and operate compared to the cluster version, so think twice before choosing the cluster version.
> See [this question](https://docs.victoriametrics.com/victoriametrics/faq/#which-victoriametrics-type-is-recommended-for-use-in-production---single-node-or-cluster) for more details.


## Architecture overview

VictoriaMetrics cluster consists of the following services:

- `vmstorage` - stores the raw data and returns the queried data on the given time range for the given label filters
- `vminsert` - accepts the ingested data and spreads it among `vmstorage` nodes according to consistent hashing over metric name and all its labels
- `vmselect` - performs incoming queries by fetching the needed data from all the configured `vmstorage` nodes

Each service may scale independently and may run on the most suitable hardware.
`vmstorage` nodes don't know about each other, don't communicate with each other and don't share any data.
This is a [shared nothing architecture](https://en.wikipedia.org/wiki/Shared-nothing_architecture).
It increases cluster availability, and simplifies cluster maintenance as well as cluster scaling.

![Cluster Scheme](Cluster-VictoriaMetrics-components.webp)

> Further reading, deep dives into how each service works internally:
> - `vmstorage`: [How vmstorage Handles Data Ingestion From vminsert](https://victoriametrics.com/blog/vmstorage-how-it-handles-data-ingestion/), [How vmstorage's IndexDB Works](https://victoriametrics.com/blog/vmstorage-how-indexdb-works/), [How vmstorage Handles Query Requests From vmselect](https://victoriametrics.com/blog/vmstorage-how-it-handles-query-requests/).
> - `vminsert`: [When Metrics Meet vminsert: A Data-Delivery Story](https://victoriametrics.com/blog/vminsert-how-it-works/).
> - `vmselect`: [Inside vmselect: The Query Processing Engine of VictoriaMetrics](https://victoriametrics.com/blog/vmselect-how-it-works/).
