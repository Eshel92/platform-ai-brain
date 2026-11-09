<!-- Converted from tutorial/om-perf-multi-cluster.txt (reStructuredText). Includes are inlined. -->

# Performance

The geographical distribution of the Application Database and Ops Manager
instances might impact the performance of the Ops Manager Application and backup and
restore processes. To learn more, see
`Performance in Multi-Region Deployments`.

To get all the benefits of increased resilience and availability from
deploying Ops Manager across multiple Kubernetes clusters, consider deploying all
components in the same geographical area.

The source of possible degraded performance might stem from increased
network latency (due to the physical distance) between the following components:

- The Ops Manager Application serving the UI or API requests and a primary
  Application Database node writing the data.
- The MongoDB database nodes and the Ops Manager Application performing backup jobs.

If you plan to deploy the Ops Manager Application and the Application Database in
multiple, geographically distant regions, contact [MongoDB Support](https://support.mongodb.com/welcome) for
further assistance.
