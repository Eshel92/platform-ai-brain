<!-- Part 3 of 5 of anomaly-detection/UI.md (split because the page is big). -->

## Multivariate Investigation

{{< available_from "v1.30.5" anomaly >}} UI v1.9.0 can investigate supported multivariate models using multiple aligned signals. Choose a multivariate class exposed by the connected server, select the query aliases it should use, and configure `groupby` with the labels identifying independent entities. For example, grouping by `service` creates a separate joint model for each service label value; signals from different services are not mixed. One query can return several channels, and several named queries can contribute channels to the same group.

> [!WARNING]
> The multivariate UI is experimental. Its layout and interactions may change. Validate results against representative history before using the configuration in production. Availability depends on the connected server's model catalog; this does not imply support for every model topology or custom model.

The workspace lets you select an anomaly-ranked group, compare normalized input signals, inspect its joint anomaly score and anomaly regions, and focus or pin individual channels with forecast and interval diagnostics. A joint anomaly score describes the group; per-channel plots help investigate contributing behavior and do not turn the result into independent univariate detections. Empty or misaligned inputs require correcting the queries, grouping labels or time range.

1. Execute the intended queries and check that each required group has matching input channels.
2. Select a supported multivariate model and set `groupby` to the entity labels. Keep query-specific policies on their query rows.
3. Detect anomalies, choose a group, and inspect the joint score alongside its channels. Consecutive-point filtering controls which anomalous streaks are displayed; it is separate from model fitting and production alert persistence.
4. Review the resulting configuration before exporting it. Additional channel diagnostics can increase output cardinality; UI experiments do not change production writer settings automatically.

![Multivariate investigation with normalized input signals, a joint anomaly score and expanded per-channel forecast diagnostics](vmanomaly-ui-multivariate-investigation.webp)

### Multivariate suggestions and autotune

With [mcp-vmanomaly](https://github.com/VictoriaMetrics/mcp-vmanomaly/releases) **v0.4.0 or later**, **vmanomaly v1.30.5 or later** and **UI v1.9.0 or later**, Copilot can propose named queries and their policies, then tune the actual multivariate class with all active inputs in one shared study. Grouping and per-query policies are preserved. Each candidate is evaluated across the aligned groups, and the returned model configuration is shared across them; separately tuned univariate configurations are not a substitute for joint tuning.

Review and approve suggestions before applying them. If the queries changed while a suggestion was pending, request a refreshed suggestion. Upgrade the MCP server to v0.4.0 or later to use this workflow; updating the UI alone does not upgrade its tools.

For online-model experiments intended to run without refits, use `exact: true`, match `infer_every` to the query step, and choose `fit_every` longer than the displayed inference range. For example, a 30-day range can use `fit_every: 35d`; `fit_window` independently provides initialization history. Exact inference alone does not disable refits. Choose production refit cadence separately according to drift and operational needs.


## Configuration Sharing

Based on the needs, either 
- Full UI state can be [shared via URL](#url-sharing)
- Or model part / full service configuration can be [viewed and exported in production-ready YAML format](#yaml-configuration).

[Default state](#default-state) can simplify both sharing and experimentation by preconfiguring the UI state on vmanomaly startup.

### URL Sharing

Similarly to vmui, vmanomaly UI supports **configuration sharing via URL** by encoding the UI state in the URL. This allows users to share their UI state (including queries, time ranges, model type and hyperparameters, and other settings) by copying and sharing the URL from the browser's address bar.

Once the desired UI state is set up (query, time range, model configuration, etc.), the URL can be copied from the browser's address bar and shared with others, who can then open the URL in their browsers to see the same UI state (given that the data source is accessible to them).

![vmanomaly-ui-state-sharing-url](vmanomaly-ui-state-sharing-url.webp)

<p></p>
<p>Example URL content:</p>

```shellhelp
http://localhost:8490/vmui/#/?anomaly_threshold=1.0&fit_window=1d&fit_every=7d&g0.range_input=7d&g0.end_input=2025-09-30T16%3A56%3A13&g0.relative_time=last_7_days&g0.tab=0&g0.tenantID=0&datasourceUrl=https%3A%2F%2Fplay.victoriametrics.com%2Fselect%2F0%2Fprometheus&g0.expr=sum%28rate%28node_cpu_seconds_total%7Bmode%3D%7E%22%28softirq%7Cuser%7Ciowait%29%22%7D%5B10m%5D%29%29+by+%28container%2C+mode%29&g0.step_input=30m&model_config=%257B%2522modelType%2522%253A%2522rolling_quantile%2522%252C%2522settings%2522%253A%257B%2522detection_direction%2522%253A%2522above_expected%2522%252C%2522data_range%2522%253A%255B0%252C100%255D%252C%2522scale%2522%253A%255B1%252C1%255D%252C%2522clip_predictions%2522%253Atrue%252C%2522min_dev_from_expected%2522%253A%255B0%252C6%255D%252C%2522anomaly_score_outside_data_range%2522%253A1.01%252C%2522quantile%2522%253A0.9%252C%2522window_steps%2522%253A48%257D%252C%2522modelSpec%2522%253A%257B%2522class_name%2522%253A%2522rolling_quantile%2522%252C%2522class%2522%253A%2522model.rolling_quantile.RollingQuantileModel%2522%252C%2522detection_direction%2522%253A%2522above_expected%2522%252C%2522data_range%2522%253A%255B0%252C100%255D%252C%2522scale%2522%253A%255B1%252C1%255D%252C%2522clip_predictions%2522%253Atrue%252C%2522min_dev_from_expected%2522%253A%255B0%252C6%255D%252C%2522anomaly_score_outside_data_range%2522%253A1.01%252C%2522window_steps%2522%253A48%252C%2522quantile%2522%253A0.9%257D%252C%2522isValidated%2522%253Atrue%257D
```

### Default State

{{< available_from "v1.28.5" anomaly >}} It is possible to preconfigure the default UI state via url-encoded `ui_default_state` parameter, so that `/vmui/` opens with the intended model settings, time range, query and other parameters, which improves user experience by allowing direct access to specific views without manual configuration each time, including state sharing or faster experimentation for internal teams.

This parameter can be set in `server` [section](https://docs.victoriametrics.com/anomaly-detection/components/server/) of the [configuration file](https://docs.victoriametrics.com/anomaly-detection/components/) using the `ui_default_state` parameter. 

> Default state is static by nature, so changing it requires either vmanomaly service restart or enabling [hot-reload mode](https://docs.victoriametrics.com/anomaly-detection/components/#hot-reload) via `--watch` flag.

Example usage (based on [UI preset](#preset) mode):

```yaml
preset: ui
# other sections, if needed e.g. settings

server:
  ui_default_state: '#/?anomaly_threshold=1.0&anomaly_consecutive=true&fit_window=3d'
  # other server parameters, if needed e.g. port, max_concurrent_tasks, etc.
```

After that, accessing `http://<vmanomaly-host>:<port>/vmui/` (e.g. `http://localhost:8490/vmui/`) will open the UI with the preconfigured default state: `anomaly_threshold=1.0`, consecutive anomaly mode turned on and `fit_window=3d` given the example above.

> Please refer to [URL sharing](#url-sharing) section for details on how to construct and copy the desired UI state URL.

### YAML Configuration

Once the configuration is set up and saved in the UI (selected model type and validated hyperparameters), equivalent configuration in production-ready YAML format can be obtained by:

Accessing the "YAML" Tab in the model configuration section
![vmanomaly-ui-model-config-menu](vmanomaly-ui-model-config-menu.webp)
![vmanomaly-ui-model-config-yaml-tab](vmanomaly-ui-model-config-menu-yaml-tab.webp)


Clicking the "Show Config" button to access (model-only or full) configuration and hitting "Download" button to get the configuration as a YAML file.

![vmanomaly-ui-open-config-btn](vmanomaly-ui-open-config-btn.webp)

![vmanomaly-ui-open-config-menu](vmanomaly-ui-open-config-menu.webp)


## Optimize Resource Usage

Based on expected usage patterns (quick experiments, internal team serving, number of users, etc.) it is recommended to tune resource usage by adjusting the following parameters in the `server` [section](https://docs.victoriametrics.com/anomaly-detection/components/server/#parameters) and `settings` [section](https://docs.victoriametrics.com/anomaly-detection/components/settings/) of the configuration file:

```yaml
server:
  # Port for the UI server (default: 8490)
  port: 8490
  # Limit on concurrent tasks to manage UI load (default: 2) 
  max_concurrent_tasks: 2

settings:
  # Number of workers for single job speed-ups (default: 1)
  n_workers: 2
  # Adjust logging levels to reduce verbosity  
  logger_levels: 
    vmanomaly: WARNING
    reader: INFO
    model: INFO
    # ...
```

`max_concurrent_tasks` limits the number of concurrent tasks (e.g. running anomaly detection on queried data) to avoid overloading the UI when multiple users are using it simultaneously, and `n_workers` [option](https://docs.victoriametrics.com/anomaly-detection/components/settings/#parallelization) controls the number of workers for parallel processing of single tasks (e.g. running anomaly detection on queried data faster).

Please note that numbers <= 0 for `n_workers` mean number of available CPU cores, and these workers would be shared with other components of vmanomaly, such as production jobs of anomaly detection (retrieving metrics, running models, writing results, etc.), if they are enabled.

### Preset Usage

If using the `ui` preset, just specify:

```yaml
preset: ui

server:
  # Port for the UI server (default: 8490)
  port: 8490
  # Limit on concurrent tasks to manage UI load (default: 2)
  max_concurrent_tasks: 5
  # path_prefix: /my-app  # optional, available from v1.28.4
  # To locate the UI at http://<vmanomaly-host>:8490/my-app/vmui/

settings:
  # Number of workers for single job speed-ups (default: 1)
  n_workers: 2
  # Adjust logging levels to reduce verbosity
  logger_levels:
    vmanomaly: WARNING
    # ...
```

in instance configuration file, it will be recursively merged with preset pre-filled configuration to produce the final configuration.

### Mixed Usage

If mixing the UI alongside production jobs of anomaly detection is expected, it is recommended to adjust the parameters to optimize resource usage, as well as configuring the `reader` and `writer` components appropriately for the production jobs.

```yaml

settings:
  # Number of workers for mixed usage (numbers <= 0 mean number of available CPU cores)
  n_workers: -1        
  # Adjust logging levels to reduce verbosity
  logger_levels:
    vmanomaly: WARNING
    reader: INFO
    model: INFO
    writer: INFO
    # ...

server:
  # Port for the UI server (default: 8490)
  port: 8490
  # Limit on concurrent tasks to manage UI load (default: 2)
  max_concurrent_tasks: 5
  # override server's configured URL path prefix for all HTTP routes
  # e.g. locate the UI at http://<vmanomaly-host>:8490/my-app/vmui/
  # available from v1.28.4
  # path_prefix: /my-app

# other production components, e.g. schedulers, models, reader, writer, etc.
```
