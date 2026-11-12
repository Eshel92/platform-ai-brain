<!-- Part 4 of 8 of victoriametrics/Cluster-VictoriaMetrics.md (split because the page is big). -->

## Multitenancy

VictoriaMetrics cluster supports multiple isolated tenants (aka namespaces).
Tenants are identified by `accountID` or `accountID:projectID` inside request URLs or HTTP headers{{% available_from "v1.143.0" %}}
for writes and reads. See [these docs](#url-format) for details.

Some facts about tenants in VictoriaMetrics:

- Each `accountID` and `projectID` is identified by an arbitrary 32-bit integer in the range `[0 .. 2^32)`.
  If `projectID` is missing, then it is automatically assigned to `0`. It is expected that other information about tenants
  such as auth tokens, tenant names, limits, accounting, etc. is stored in a separate relational database. This database must be managed
  by a separate service sitting in front of VictoriaMetrics cluster such as [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/)
  or [vmgateway](https://docs.victoriametrics.com/victoriametrics/vmgateway/). [Contact us](mailto:info@victoriametrics.com) if you need assistance with such service.

- Tenants are automatically created when the first data point is written into the given tenant.

- Data for all the tenants is evenly spread among available `vmstorage` nodes. This guarantees even load among `vmstorage` nodes
  when different tenants have different amounts of data and different query load.

- The database performance and resource usage do not depend on the number of tenants. It depends mostly on the total number of
  [active time series](https://docs.victoriametrics.com/victoriametrics/faq/#what-is-an-active-time-series) in all the tenants.

- The list of registered tenants can be obtained via `http://<vmselect>:8481/admin/tenants` url. See [these docs](#url-format).

- VictoriaMetrics exposes various per-tenant statistics via metrics - see [these docs](https://docs.victoriametrics.com/victoriametrics/pertenantstatistic/).

See also multitenancy [via headers](#multitenancy-via-headers) and [via labels](#multitenancy-via-labels).

### Multitenancy via headers

With `--enableMultitenancyViaHeaders` {{% available_from "v1.143.0" %}} command-line flag enabled (enabled by default {{% available_from "v1.150.0" %}})
tenant ID can be specified via HTTP headers `AccountID` and `ProjectID`. This flag needs to be enabled on vminserts and vmselects.

With `--enableMultitenancyViaHeaders` enabled [URL format](#url-format) can be simplified to the following:
- `http://<vminsert>:8480/insert/<suffix>` for writes
- `http://<vmselect>:8481/select/prometheus/<suffix>` for reads

> Set --enableMultitenancyViaHeaders=false to disable simplified URL format.

For example, the following query will only select metric `up` from `accountID=2` and `projectID=3`:
```
curl 'https://<vmselect>:8481/select/prometheus/api/v1/query' \
  -d 'query=up' \
  --header "AccountID: 2" \
  --header "ProjectID: 3"
```

The following example will ingest metric `up{instance="foo"}` to `accountID=2` and `projectID=0`:
```
curl --header "AccountID: 2" -d 'up{instance="foo"} 123' -X POST https://<vminsert>:8480/insert/prometheus/api/v1/import/prometheus
```

> When simplified path `/(insert|select)/<suffix>` is used and headers `AccountID`, `ProjectID` are missing, then IDs are set to `0:0` as default.
> If tenant IDs are specified in URL, then headers are ignored.

The `AccountID` header can be set to `multitenant` string: `AccountID: multitenant`. See more in [multitenancy via labels](#multitenancy-via-labels).

### Multitenancy via labels

Multitenancy via labels allows specifying [tenants](#multitenancy) as labels `vm_account_id` and `vm_project_id` during
ingestion or querying. This feature allows [ingesting workload with mixed tenants](#multitenant-writes) and [querying
data from multiple tenants](#multitenant-reads) via the same URL.

#### Multitenant writes

`vminsert` can accept data from multiple [tenants](#multitenancy) via special `multitenant` endpoints:
- `http://vminsert:8480/insert/multitenant/<suffix>`
- `http://vminsert:8480/insert/<suffix>` and HTTP header `AccountID: multitenant`. See how to enable headers [here](#multitenancy-via-headers).
  where `<suffix>` can be replaced with any supported suffix for data ingestion from [this list](#url-format).
  The `accountID` and `projectID` are obtained from optional `vm_account_id` and `vm_project_id` [labels](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#labels) of the incoming samples.
  If `vm_account_id` or `vm_project_id` labels are missing or invalid, then the corresponding `accountID` and `projectID` are set to 0.
  These labels are automatically removed from samples before forwarding them to `vmstorage`.
  For example, if the following samples are written into `http://vminsert:8480/insert/multitenant/prometheus/api/v1/write`:

```promtextmetric
http_requests_total{path="/foo",vm_account_id="42"} 12
http_requests_total{path="/bar",vm_account_id="7",vm_project_id="9"} 34
```

Then the `http_requests_total{path="/foo"} 12` would be stored in the tenant `accountID=42, projectID=0`,
while the `http_requests_total{path="/bar"} 34` would be stored in the tenant `accountID=7, projectID=9`.

The `vm_account_id` and `vm_project_id` labels are extracted after applying the [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/)
set via `-relabelConfig` command-line flag, so these labels can be set at this stage.

The `vm_account_id` and `vm_project_id` labels are also taken into account when ingesting data via non-http-based protocols
such as [Graphite](https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#ingesting),
[InfluxDB line protocol via TCP and UDP](https://docs.victoriametrics.com/victoriametrics/integrations/influxdb/) and
[OpenTSDB telnet put protocol](https://docs.victoriametrics.com/victoriametrics/integrations/opentsdb/#sending-data-via-telnet).

#### Multitenant reads

_For better performance prefer specifying [tenants in read URL](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#url-format)._

`vmselect` can execute {{% available_from "v1.104.0" %}} queries over multiple [tenants](#multitenancy) via special `multitenant` endpoints:
- `http://vmselect:8481/select/multitenant/<suffix>`
- `http://vmselect:8481/select/<suffix>` and HTTP header `AccountID: multitenant`. See how to enable headers [here](#multitenancy-via-headers).

Currently supported endpoints for `<suffix>` are:

- `/prometheus/api/v1/query`
- `/prometheus/api/v1/query_range`
- `/prometheus/api/v1/series`
- `/prometheus/api/v1/labels`
- `/prometheus/api/v1/label/<label_name>/values`
- `/prometheus/api/v1/status/active_queries`
- `/prometheus/api/v1/status/top_queries`
- `/prometheus/api/v1/status/tsdb`
- `/prometheus/api/v1/export`
- `/prometheus/api/v1/export/csv`
- `/prometheus/api/v1/metadata`
- `/vmui`

It is allowed to explicitly specify tenant IDs via `vm_account_id` and `vm_project_id` labels in the query.
For example, the following query fetches metric `up` for the tenants `accountID=42` and `accountID=7, projectID=9`:

```promtextmetric
up{vm_account_id="7", vm_project_id="9" or vm_account_id="42"}
```

`vm_account_id` and `vm_project_id` labels support all operators for label matching. For example:

```promtextmetric
up{vm_account_id!="42"} # selects all the time series except those belonging to accountID=42
up{vm_account_id=~"4.*"} # selects all the time series belonging to accountIDs starting with 4
```

Alternatively, it is possible to use [`extra_filters[]` and `extra_label`](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#prometheus-querying-api-enhancements)
query args to apply additional filters for the query:

```bash
curl 'http://vmselect:8481/select/multitenant/prometheus/api/v1/query' \
  -d 'query=up' \
  -d 'extra_filters[]={vm_account_id="7",vm_project_id="9"}' \
  -d 'extra_filters[]={vm_account_id="42"}'
```

The precedence for applying filters for tenants follows this order:

1. Filter tenants by `extra_label`, `extra_filters` and `extra_filters[]` filters.
   These filters have the highest priority and are applied first when provided through the query arguments.
   Filters use `OR` logic - a tenant is selected if it matches any of the filters.
2. Filter tenants from labels selectors defined at metricsQL query expression.

> **Security considerations**
It is recommended restricting access to `multitenant` endpoints only to trusted sources,
since untrusted source may break per-tenant data by writing unwanted samples or get access to data of arbitrary tenants.
See also [vmauth security doc](https://docs.victoriametrics.com/victoriametrics/vmauth/#security).
