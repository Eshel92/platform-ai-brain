<!-- Part 1 of 5 of anomaly-detection/UI.md (split because the page is big). -->

## Introduction

{{< available_from "v1.26.0" anomaly >}} `vmanomaly` includes a built-in [vmui-like](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui) [UI](https://en.wikipedia.org/wiki/Graphical_user_interface) for exploring queries, comparing anomaly detection models, and tuning model or domain settings before production deployment.

![vmanomaly-ui-overview](vmanomaly-ui-overview.webp)


## Accessing the UI

The UI is available at `http://<vmanomaly-host>:8490` by default. Change the port with `server.port` in the [configuration file](https://docs.victoriametrics.com/anomaly-detection/components/):

```yaml
server:
  port: 8490

# other vmanomaly configuration sections, e.g. schedulers, models, reader, writer, etc.
```

For impactful parameters please refer to [optimize resource usage](#optimize-resource-usage) section of this page.


## Playgrounds

> [!TIP]
> For a prepared query, model, and schedule with expected results, try the [model-selection recipes](https://docs.victoriametrics.com/anomaly-detection/guides/model-selection/#steady-baseline-small-fluctuations).

Try the UI with preconfigured queries and models in the public VictoriaMetrics, VictoriaLogs, and VictoriaTraces playgrounds:

<div class="collapse-group mb-3">

{{% collapse name="Playground on VictoriaMetrics Datasource" %}}

<div class="position-relative mb-3">
  <button
    type="button"
    class="btn btn-primary btn-sm position-absolute top-0 end-0 m-2"
    style="z-index: 2;"
    onclick="document.getElementById('vmui-playground-vmanomaly-metrics')?.requestFullscreen?.()"
  >
    Fullscreen
  </button>

  <iframe
    id="vmui-playground-vmanomaly-metrics"
    title="VictoriaMetrics Anomaly Detection Playground (Metrics)"
    allow="fullscreen"
    loading="lazy"
    class="w-100 border rounded"
    style="height: 400px; background: white;"
    src="https://play-vmanomaly.victoriametrics.com/metrics/"
  ></iframe>
</div>

{{% /collapse %}}

{{% collapse name="Playground on VictoriaLogs Datasource" %}}

<div class="position-relative mb-3">
  <button
    type="button"
    class="btn btn-primary btn-sm position-absolute top-0 end-0 m-2"
    style="z-index: 2;"
    onclick="document.getElementById('vmui-playground-vmanomaly-logs')?.requestFullscreen?.()"
  >
    Fullscreen
  </button>

  <iframe
    id="vmui-playground-vmanomaly-logs"
    title="VictoriaMetrics Anomaly Detection Playground (Logs)"
    allow="fullscreen"
    loading="lazy"
    class="w-100 border rounded"
    style="height: 400px; background: white;"
    src="https://play-vmanomaly.victoriametrics.com/logs/"
  ></iframe>
</div>

{{% /collapse %}}

{{% collapse name="Playground on VictoriaTraces Datasource" %}}

<div class="position-relative mb-3">
  <button
    type="button"
    class="btn btn-primary btn-sm position-absolute top-0 end-0 m-2"
    style="z-index: 2;"
    onclick="document.getElementById('vmui-playground-vmanomaly-traces')?.requestFullscreen?.()"
  >
    Fullscreen
  </button>

  <iframe
    id="vmui-playground-vmanomaly-traces"
    title="VictoriaMetrics Anomaly Detection Playground (Traces)"
    allowfullscreen
    allow="fullscreen"
    loading="lazy"
    class="w-100 border rounded"
    style="height: 400px; background: white;"
    src="https://play-vmanomaly.victoriametrics.com/traces/"
  ></iframe>
</div>

{{% /collapse %}}

</div>


## Authentication

> [!TIP]
{{< available_from "v1.29.2" anomaly >}} You can proxy connection settings to UI, defined in [reader](https://docs.victoriametrics.com/anomaly-detection/components/reader/#config-parameters) section of the configuration file, so that UI can connect to the data sources with the same settings (e.g. credentials, TLS, etc.). Set `server.use_reader_connection_settings` [arg](https://docs.victoriametrics.com/anomaly-detection/components/server/#parameters) to `true` in the configuration file to enable this feature, and UI will automatically use the connection settings from the reader configuration when connecting to the data sources. If `pass auth headers` option is enabled in the UI settings, it will take precedence over the reader-wise settings. See [example configuration](https://docs.victoriametrics.com/anomaly-detection/components/server/#example-configuration) for details.


{{< available_from "v1.27.0" anomaly >}} The vmanomaly UI supports proxying authentication headers from [v1.1.0](#v110) and onwards.

Consider using [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/) in front of both vmanomaly (UI and API) and data sources (VictoriaMetrics / VictoriaLogs) to enforce end-to-end setup for accessing the data from the UI.

> Please refer to [config format](https://docs.victoriametrics.com/victoriametrics/vmauth/#auth-config) of `vmauth` and check [generic proxy example for different backends](https://docs.victoriametrics.com/victoriametrics/vmauth/#generic-http-proxy-for-different-backends)

Use the following example configuration snippet for `vmauth` to proxy auth headers to VictoriaMetrics, VictoriaLogs and vmanomaly instances:

```yaml
users:
  - username: '<username>'
    password: '<password>'
    url_map:
      - src_hosts:
          - "metrics.local.some-domain.net"
        url_prefix: "http://victoriametrics:8428"
      - src_hosts:
          - "vl.local.some-domain.net"
        url_prefix: "http://victorialogs:9428"
      - src_hosts:
          - "vmanomaly.local.some-domain.net"
        url_prefix: "http://vmanomaly:8490"
        keep_original_host: true
```

Then, on [settings panel](#settings-panel) of the UI, set the URLs accordingly, also check the option to forward auth headers to the datasource:

![vmanomaly-ui-sections-settings](vmanomaly-ui-sections-settings.webp)
{class="w-50 mx-auto"}

### Pre-configured Datasource

{{< available_from "v1.28.2" anomaly >}} For a shared deployment with a fixed datasource, set these environment variables at `vmanomaly` startup. The UI then hides its datasource selectors:

- `VMANOMALY_UI_DATASOURCE_URL` - to set static datasource URL
- `VMANOMALY_UI_DATASOURCE_TYPE` - to set datasource type, supported options are `vm` for VictoriaMetrics, `vmlogs` for both VictoriaLogs and VictoriaTraces.

Example usage:
```shell
export VMANOMALY_UI_DATASOURCE_URL=https://play.victoriametrics.com/select/0:0/prometheus
export VMANOMALY_UI_DATASOURCE_TYPE=vm
```

Start `vmanomaly` as usual. All UI queries will use the configured datasource:

![vmanomaly-ui-preconfigured-datasource-1](vmanomaly-ui-preconfigured-datasource-1.webp)


## Preset

Vmanomaly can be deployed in efficient "UI mode" [preset](https://docs.victoriametrics.com/anomaly-detection/presets/#ui), with as simple configuration as:

```yaml
preset: ui
```

This will start vmanomaly instance with a no-operation schedulers, readers, models and the other components, and **will only enable the UI for interactive exploration of anomaly detection models**, so all the resources are dedicated to the UI and no resources are wasted on other components, such as production jobs of anomaly detection (retrieving metrics, running models, writing results, etc.).

The best applications of this mode are:
- Deploy vmanomaly UI as a service to hide the deployment complexity and allow internal users to explore anomaly detection models and their configurations, without the need to run any production jobs of anomaly detection.
- When there is a quick need to explore and validate anomaly detection models and their configurations before deploying them in production jobs, at minimal resource usage.


> However, the UI can be **combined with existing production jobs of anomaly detection, as it is available in non-blocking mode for all running vmanomaly instances** {{< available_from "v1.26.0" anomaly >}}, regardless of the preset or configuration used, just at a cost of increased resource usage.


## Investigate a firing alert

{{< available_from "v1.30.7" anomaly >}} Add an `investigation_url` annotation to a vmalert rule to open the persisted results, configured model and absolute incident window in VMUI. Opening the link does not rerun detection.

```yaml
annotations:
  investigation_url: 'https://vmanomaly.example.com/api/v1/incident/open?model={{ $labels.model_alias | queryEscape }}&scheduler={{ $labels.scheduler_alias | queryEscape }}&preset={{ $labels.preset | queryEscape }}&query_key={{ index $labels "for" | queryEscape }}&at={{ $activeAt.Unix }}&before=2m&after=30s'
```

Use the public vmanomaly URL, including any `path_prefix`, and preserve the emitted model, scheduler, preset and `for` labels in the alert expression. Optional `label.<name>` parameters select exact source-series labels; omit alert-only labels. Append `view=inputs` to open the original inputs instead. The link resolves the current configuration on the selected shard and initially supports a shared VictoriaMetrics reader/writer URL and tenant with default metric naming.

> [!WARNING]
> Protect VMUI and both `/api/v1/incident/` endpoints behind the same authenticated gateway. Labels filter results; they do not grant access. If the datasource requires reader credentials, configure [`server.use_reader_connection_settings`](https://docs.victoriametrics.com/anomaly-detection/components/server/#parameters) or supported request authentication. Authorized UI users can then query with those reader permissions.

See [vmalert annotation templating](https://docs.victoriametrics.com/victoriametrics/vmalert/#templating) for template syntax. The annotation can coexist with the [vmalert Source link](https://docs.victoriametrics.com/victoriametrics/vmalert/#link-to-alert-source).
