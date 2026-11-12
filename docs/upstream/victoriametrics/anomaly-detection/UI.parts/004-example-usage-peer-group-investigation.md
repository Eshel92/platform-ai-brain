<!-- Part 4 of 5 of anomaly-detection/UI.md (split because the page is big). -->

## Example Usage

Run vmanomaly in `ui` preset mode (experimenting) with a configuration file `config.yaml` (see [preset usage](#preset-usage) section for details):

```yaml
preset: ui

# other optional server/settings parameters, e.g. port, max_concurrent_tasks, n_workers, logger_levels, etc.
```

using one of the [deployment methods](https://docs.victoriametrics.com/anomaly-detection/quickstart/#how-to-install-and-run-vmanomaly) in a [QuickStart guide](https://docs.victoriametrics.com/anomaly-detection/quickstart/), e.g. via Docker.

Retrieve the UI at `http://<vmanomaly-host>:<port>` (e.g. at `http://localhost:8490` if running locally with default port) and start exploring anomaly detection models and their configurations interactively.

### Explore Input Data

Start by entering valid MetricsQL/LogsQL queries in the Query Explorer to visualize the data from the configured data source (see [settings panel](#settings-panel) for data source configuration) - that's the data on which anomaly detection models will be applied.

Set appropriate tenants (if data source supports multi-tenancy) and access [settings panel](#settings-panel) for global UI configuration, if needed.

Set up the time range and resolution (step) for data visualization and anomaly detection purposes - e.g. last 7 days with 30m step, especially if the data has daily/weekly seasonality. Also, set the step according to the desired granularity of anomaly detection results (e.g. 30m step for 30m granularity) which itself is based on alerting needs and latency requirements.

![Query Explorer with two named queries, per-query business policies and model-default inheritance controls](vmanomaly-ui-sections-explore.webp)

Pay attention to trends, seasonality, noise, outliers, and other patterns in the data, which can influence the choice of anomaly detection model and its hyperparameters. Use [Temporal Envelope](https://docs.victoriametrics.com/anomaly-detection/components/models/#temporal-envelope) for complex data with trend or calendar patterns, and [Online MAD](https://docs.victoriametrics.com/anomaly-detection/components/models/#online-mad) for simple, mostly stationary data where robustness to outliers matters.

![vmanomaly-ui-sections-plot-area-query-mode](vmanomaly-ui-sections-plot-area-query-mode.webp)


### Select and Configure Model

Choose an appropriate anomaly detection model from the Model Panel based on the characteristics of the data and the specific requirements (domain knowledge) of the use case.

![vmanomaly-ui-sections-model](vmanomaly-ui-sections-model.webp)

Set the "Fit Every" and "Fit Window" parameters to control how often and over what time window the model is retrained on new data to imitate production behavior - e.g. fit every 7 days on a rolling window of last 14 days.

{{< available_from "v1.28.0" anomaly >}} Set the "Infer Every" and toggle "Exact" mode parameters for [online models](https://docs.victoriametrics.com/anomaly-detection/components/models/#online-models) to imitate production inference behavior - e.g. infer every = 1h with step = 1m will result in exact mode for hourly micro-batches of up to 60 1m datapoints.

Tune the model hyperparameters and apply domain knowledge settings using the form-based menu in the Model Panel. See (i) tooltips for parameter descriptions and [model documentation](https://docs.victoriametrics.com/anomaly-detection/components/models/) link for recommended values and guidelines.

To try suggested parameter settings, use [Tune a model](#tune-a-model), then review the results before applying them.

![vmanomaly-ui-model-config-wizard](vmanomaly-ui-model-config-wizard.webp)
{class="w-75 mx-auto"}

For example, for a **MAD online** [model](https://docs.victoriametrics.com/anomaly-detection/components/models/#online-mad), that should be run on a query, returning per-mode CPU utilization (as fractions of 1, data range `[0, 1]`), where you are interested in capturing **spikes of at least 6% deviations** from expected behavior:

Set the **model-agnostic** parameters to encode the domain knowledge:
- [detection direction](https://docs.victoriametrics.com/anomaly-detection/components/models/#detection-direction) to `above expected` for capturing high anomalies (spikes)
- data range to `[0, 1]` for CPU utilization fractions and proper prediction clipping
- [minimum deviation from expected](https://docs.victoriametrics.com/anomaly-detection/components/models/#minimal-deviation-from-expected) to `[0, 0.06]` for capturing spikes of at least 6% deviations in magnitude
- (optionally) [anomaly score outside data range](https://docs.victoriametrics.com/anomaly-detection/components/models/#score-outside-data-range) to `5.0` for automatically marking values outside data range as anomalies (e.g. to catch improper query returning CPU > 100% or < 0%)
- [clip predictions](https://docs.victoriametrics.com/anomaly-detection/components/models/#clip-predictions) to `true` for avoiding nonsensical predictions outside data range
- [scale](https://docs.victoriametrics.com/anomaly-detection/components/models/#scale) to `[1, 1]` unless you will see improper width of confidence intervals from the experiments (e.g. too wide/narrow) given the model-specific hyperparameters and false positives/negatives observed in the results.

Set the **model-specific** hyperparameters:
- `threshold` to `3` for capturing significant deviations
- `decay` to `0.995` for adapting to changing data patterns reasonably fast.

Check the parameters for validity and consistency by hitting the "Validate" button, which will also provide warnings if some parameters are inconsistent (e.g. decay is set outside of `[0, 1]` range or `threshold` is set to a negative value), then hit "Save" to apply the changes.

### Detect Anomalies

Hit the "Detect Anomalies" button to run anomaly detection on the queried data with the selected model and its configuration.

> The long running task (e.g. detection on misconfigured query returning too much metrics) can be canceled by hitting the "Cancel" button.

![vmanomaly-ui-sections-plot-area-detect-mode](vmanomaly-ui-sections-plot-area-detect-mode.webp)

Iterate over the legend to view **individual vmanomaly output** (e.g. actual values, expected values, confidence intervals, anomalies, etc.) for different series returned by the query.

Iterate over **returned timeseries by query** to see how the model performed on different series, and whether the detected anomalies make sense in the context of the data and the use case (their % of total points, magnitude, duration, etc.).

> {{< available_from "v1.28.2" anomaly >}} Starting from [v1.4.0](#v140) The timeseries are now sortable in the legend by clicking on the respective column headers (both label- and statistics-based columns are supported, e.g., sort by series name, anomaly count). Press "Table View" toggle to use this feature.

Until satisfied with the results, finetune the model hyperparameters and domain knowledge settings in the Model Panel (or change the model type), and rerun anomaly detection on the queried data.

Once satisfied with the results, do the following.

>  Many tabs can be opened in parallel in the browser, so multiple experiments can be run in parallel, and the results can be compared by switching between tabs. Local settings (e.g. queries, time ranges, model configurations, etc.) are preserved in each tab, so different experiments do not interfere with each other.

### Work with Results

If the **results** do not look good, the model hyperparameters and domain knowledge settings can be further finetuned in the Model Panel, and anomaly detection can be [rerun on the queried](#detect-anomalies) data until satisfactory results are achieved.

If the **results** look good, but should be shared with others first, {{< available_from "v1.32.0" anomaly >}} use **More → Download results** to export query or anomaly results as JSON. Choose the current range and, when needed, privacy replacements that stay consistent within the loaded results. See also [configuration sharing](#configuration-sharing) section for details.

If the **results** look good and the **model configuration should be deployed in production jobs of anomaly detection**, the equivalent configuration in production-ready YAML format can be obtained by accessing the "YAML" Tab in the model configuration section and hitting the "Show Config" button to access (model-only or full) configuration to download/copy as a YAML file.

![vmanomaly-ui-open-config-menu](vmanomaly-ui-open-config-menu.webp)

{{< available_from "v1.28.0" anomaly >}} **Example alerting rules are generated** based on the current UI configuration. Hit the "Example Alert" button in the Model Panel to access and copy/download an example of parametrized [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/) alerting rule snippet in YAML format to finetune and use in production alerting setup.

![vmanomaly-ui-example-alert-btn](vmanomaly-ui-example-alert-btn.webp)

![vmanomaly-ui-example-alert-menu](vmanomaly-ui-example-alert-menu.webp)


## Tune a model

Open **Tune** {{< available_from "v1.31.0" anomaly >}} in the model card to try experimental shared parameter tuning. Choose **Marked anomalies** for supervised tuning using regions you mark on the query chart, or an expected anomaly rate (including **No anomalies**) for unsupervised tuning. Set the trial/time budget, run tuning, then review the suggested parameters and, for marked anomalies, the detection-quality report before **Apply and detect**.

![Tune model panel with objectives, trial budget, suggested candidate and detection-quality statistics](vmanomaly-ui-tune-model.webp)

For supervised tuning, use **Mark on chart** to select expected anomalous regions. Resize marks to adjust their boundaries and use the scope selector to choose which series they apply to.

![Chart marking mode with selected anomaly regions and the series-scope toolbar](vmanomaly-ui-mark-anomalies.webp)

Quality metrics are point-level results, not counts of visual spikes. Marked regions guide tuning, so this is not an independent test. For multivariate models, a group timestamp is marked when any channel is marked; channels do not count as separate detections. Check the report's evaluated coverage and replay settings when comparing results.

For peer models, scope marks to all or selected peer groups, or individual series. Quality counts are per peer and timestamp, while multivariate quality uses the joint decision. Applying a candidate retains non-optimized model settings and explicit query policies. Changing model type preserves shared domain-knowledge settings.

Prefer **Tune** to obtain a concrete configuration you can review and deploy. The `auto` wrapper appears in its own final selector group and is planned for removal from the UI selector. This does not deprecate backend `auto` configurations, which remain available for retuning during each fit.


## Peer-group investigation

Selecting the [`peer_outlier` model](https://docs.victoriametrics.com/anomaly-detection/components/models/#peer-outlier) {{< available_from "v1.31.0" anomaly >}} opens a dedicated results panel. It overlays peers and their learned accepted range, highlights qualified anomaly regions, and ranks individual peers with score histories. Select a peer to inspect its observations and range; use **Show all** to return to the population.

![Peer-group investigation with a selected peer, accepted range and anomaly tooltip](vmanomaly-ui-peer-investigation.webp)

The group picker searches all labels, including hidden common labels. Its **Peak affected %** order compares the peak affected proportion in the visible window, then anomalous-peer count, region count and alphabetical labels. Common labels are shown once, and full labels remain available without expanding the layout indefinitely.

The **Affected peers** curve measures the percentage of reporting peers anomalous at each timestamp, not anomaly severity. Horizontal extent represents duration. All loaded groups share an adaptive vertical scale, which stays unchanged during group switches and zoom. Hover shows exact affected/reporting counts and percentages. This distinguishes a widespread event from an extreme value in only one peer, including when population size changes.

Use **Peer anomaly ranking** to filter peers by label or value and compare their anomaly regions and score histories. Color swatches match the plotted series.

![Peer anomaly ranking with label filtering, matching series colors and score histories](vmanomaly-ui-peer-ranking.webp)

In multivariate results, **Channels outside expected range** is a diagnostic view, not the joint detection decision. Use **Joint anomaly score** to identify multivariate anomalies; individual channels may exceed their ranges without the joint score crossing its threshold.
