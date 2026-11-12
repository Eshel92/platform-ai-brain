<!-- Converted from ilm/index.asciidoc (AsciiDoc). Includes are inlined. -->

## ILM: Manage the index lifecycle

You can configure index lifecycle management (ILM) policies to automatically manage indices
according to your performance, resiliency, and retention requirements.
For example, you could use ILM to:

* Spin up a new index when an index reaches a certain size or number of documents
* Create a new index each day, week, or month and archive previous ones
* Delete stale indices to enforce data retention standards

You can create and manage index lifecycle policies through Kibana Management
or the ILM APIs. Default index lifecycle management policies are created automatically
when you use Elastic Agent, Beats, or the Logstash Elasticsearch output plugin to send data
to the Elastic Stack.

image:images/ilm/index-lifecycle-policies.png[]

To automatically back up your indices and manage snapshots, use
snapshot lifecycle policies.

* example-using-index-lifecycle-policy
* getting-started-index-lifecycle-management
* overview-index-lifecycle-management
* ilm-concepts
* set-up-lifecycle-policy
* migrate-index-allocation-filters
* index-lifecycle-error-handling
* start-stop-ilm
* ilm-with-existing-indices
* skipping-rollover
* index-lifecycle-and-snapshots
* index-lifecycle-management-api
* ilm-actions

(See `ilm/example-index-lifecycle-policy.md`)
(See `ilm/ilm-tutorial.md`)
(See `ilm/../indices/index-mgmt.md`)
(See `ilm/ilm-overview.md`)
(See `ilm/ilm-concepts.md`)
(See `ilm/ilm-actions.md`)
(See `ilm/set-up-lifecycle-policy.md`)
(See `ilm/../data-management/migrate-index-allocation-filters.md`)
(See `ilm/error-handling.md`)
(See `ilm/start-stop.md`)
(See `ilm/ilm-with-existing-indices.md`)
(See `ilm/ilm-skip-rollover.md`)
(See `ilm/ilm-and-snapshots.md`)
