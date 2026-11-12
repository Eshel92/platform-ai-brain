<!-- Part 5 of 5 of anomaly-detection/UI.md (split because the page is big). -->

## Changelog

<div class="collapse-group mb-3">

{{% collapse name="Release history" %}}

### v1.11.0
Released: 2026-11-04

Recommended vmanomaly version: [v1.32.0](https://docs.victoriametrics.com/anomaly-detection/changelog/#v1320)

- FEATURE: Added [dynamic preset downloads](https://docs.victoriametrics.com/anomaly-detection/presets/#dynamic-presets) in Copilot, with YAML previews, draft requirements and validation warnings. Tool activity is collapsed between messages while approvals and files remain visible.
- FEATURE: Added guided tours for getting started and tuning with marked anomalies, using a built-in demo datasource. Tours restore the previous workspace when they end.
- FEATURE: Download query and anomaly results as JSON, with current-range selection and optional consistent privacy replacements.
- IMPROVEMENT: Added resizable query editors, searchable multi-select model options and query-alias chips with expressions available on hover or focus. Shared URLs preserve configurator visibility.
- BUGFIX: Improved query controls, chat progress and peer-history hover details; [AI Copilot](#ai-assistance) no longer automatically retries requests that exceed its conversation context limit.

### v1.10.0
Released: 2026-10-09

Recommended vmanomaly version: [v1.31.1](https://docs.victoriametrics.com/anomaly-detection/changelog/#v1311) or newer, which fixes data fetching for peer-group models in periodic deployments.

- FEATURE: Added experimental [model tuning](#tune-a-model) with supervised marked-anomaly and unsupervised expected-anomaly-rate objectives, progress, suggested parameters and point-level detection-quality statistics for marked anomalies.
- FEATURE: Added [peer-group investigation](#peer-group-investigation), searchable group labels, accepted-range overlays, peer rankings and percentage activity with exact hover counts.
- IMPROVEMENT: Made **Tune** the preferred UI tuning workflow. Moved `auto` to its own final model-selector group with a planned UI removal notice; backend `auto` configurations remain supported.
- IMPROVEMENT: Distinguished multivariate channel-range diagnostics from the joint anomaly decision.
- IMPROVEMENT: Prediction clipping defaults to enabled in the UI, while explicit opt-outs are preserved.
- IMPROVEMENT: Expanded theme-aware series colors, matched table swatches to plotted peers and improved accepted-range contrast.
- IMPROVEMENT: Simplified model/query controls, collapsed domain-knowledge defaults, and scrolled successful manual detection to the results header.
- BUGFIX: Preserved shared business settings across model changes and non-optimized settings when applying tuning candidates.
- BUGFIX: Aligned supervised replay with query policies and restored multivariate drag zoom across signal-selection modes.
- BUGFIX: Selected fresh results using each view's active ranking policy while preserving manual selections within the current results.
- BUGFIX: Fixed drag-selection focus changes, drawer-edge pointer actions, theme updates and asynchronous configuration highlighting.

### v1.9.2
Released: 2026-09-24

Recommended vmanomaly version: [v1.30.7](https://docs.victoriametrics.com/anomaly-detection/changelog/#v1307)

- FEATURE: Added [incident investigation links](#investigate-a-firing-alert) for persisted results.
- IMPROVEMENT: Added configurable model choices through `server.ui_allowed_models`.
- BUGFIX: Changed generated alert rules from `>=` to `>` for anomaly-score thresholds and fixed metric selectors to preserve preset version suffixes.

### v1.9.1
Released: 2026-09-17

Recommended vmanomaly version: [v1.30.6](https://docs.victoriametrics.com/anomaly-detection/changelog/#v1306)

- IMPROVEMENT: Reworked the Queries sheet's Server tab into a searchable list with model filters and badges, consistent row actions, and bulk actions that retain selections hidden by the current filter.
- IMPROVEMENT: Documented Queries-sheet keyboard shortcuts in the UI help.

### v1.9.0
Released: 2026-09-10

Recommended vmanomaly version: [v1.30.5](https://docs.victoriametrics.com/anomaly-detection/changelog/#v1305)

- FEATURE: Added multiple named queries with per-query policies, preserved query sets, and model query selection.
- FEATURE: [AI Copilot usage details](#copilot-usage-and-estimated-cost) show per-response and conversation token totals, approximate costs, cached input, and provider/model information.
- FEATURE: Added the experimental multivariate investigation workspace with group selection, coordinated channels and joint anomaly scores.
- FEATURE: [AI Copilot](#ai-assistance) can suggest complete named query sets with aliases and individual business policies, and shared multivariate autotune configurations through compatible tools. Approved suggestions preserve policy inheritance and reject changes based on stale query state.

### v1.8.3
Released: 2026-08-27

Recommended vmanomaly version: [v1.30.4](https://docs.victoriametrics.com/anomaly-detection/changelog/#v1304)

- IMPROVEMENT: Fresh anomaly investigations default to the online univariate Temporal Envelope, and the model selector lists online models before offline alternatives.

- BUGFIX: AI-suggested business settings remain synchronized with both the model wizard and the generated model configuration.

- BUGFIX: Advanced model drop-downs display the selected option label instead of the control's internal numeric option position while preserving correctly typed configuration values.

### v1.8.2
Released: 2026-08-13

vmanomaly version: [v1.30.2](https://docs.victoriametrics.com/anomaly-detection/changelog/#v1302)

- BUGFIX: Fixed tenant discovery for VictoriaMetrics datasource URLs containing `/select/multitenant/prometheus`. The UI now loads available numeric tenants from `/admin/tenants` and can switch the datasource URL from `multitenant` to the selected tenant.

### v1.8.1
Released: 2026-08-06

vmanomaly version: [v1.30.1](https://docs.victoriametrics.com/anomaly-detection/changelog/#v1301)

- IMPROVEMENT: Model settings are validated and normalized when applied. Invalid drafts remain open with actionable feedback, and advanced-setting summaries open the corresponding editor directly.

- BUGFIX: Server-query counts load when the query drawer opens, and numeric model fields preserve valid scalar and range values while reporting parsing errors on blur.

- BUGFIX: The anomaly visualization empty state now follows the active theme instead of using light-theme colors in dark mode.

- BUGFIX: Tenant selection now follows the datasource URL resolved by the server, avoiding an incorrect switch to tenant `0` when it is unavailable.

### v1.8.0
Released: 2026-07-23

vmanomaly version: [v1.30.0](https://docs.victoriametrics.com/anomaly-detection/changelog/#v1300)

- FEATURE: UX Improvements, refreshed interface with clearer model and query forms, inline configuration previews, and fullscreen chart controls.

- FEATURE: Server (production-running) models and queries can be accessed and selected from the UI, with a new "Queries" button, while model selection now includes a drop-down for server-configured scheduled models in model wizard.

- IMPROVEMENT: Boosted [AI Copilot](#ai-assistance) stability and suggestions quality, aligned with MCP/skills toolset, and proper handling of canceled or incomplete tool calls.

- IMPROVEMENT: Added query prettification and stable value formatting, including platform-aware keyboard-shortcut hints.

- IMPROVEMENT: Results now visibly switch to an out-of-date state after the query, time range, or model configuration changes. The action updates to rerun detection and remains visible in both expanded and collapsed model views.

- IMPROVEMENT: Chart range navigation commits one query on interaction completion instead of issuing many intermediate requests.

- IMPROVEMENT: Compact consecutive identical [AI Copilot](#ai-assistance) tool calls, keep query/model/anomaly suggestions synchronized, and recover cleanly from canceled or incomplete tool calls.

- BUGFIX: Fixed exact UI backtesting across multiple fit cycles and for auto-tuned online wrappers, preventing *duplicate or missing predictions* while retaining causal model updates and restoration of compatible legacy auto-tuned state.

- BUGFIX: Kept automatic trailing-slash redirects for configured path prefixes and `/vmui` relative to the public origin, preventing internal backend hostnames from leaking through reverse proxies such as `vmauth`.

### v1.7.2
Released: 2026-06-25

vmanomaly version: [v1.29.7](https://docs.victoriametrics.com/anomaly-detection/changelog/#v1297)

- FEATURE: Added controls for selecting server-configured scheduled models (drop-down inside [model wizard](#model-panel)) and browsing scheduled queries from the running vmanomaly instance ("Queries" button, "scheduled queries" tab).

- IMPROVEMENT: Surfaced datasource fetch failures from ad-hoc VMUI raw queries as query-level errors instead of returning a successful empty result that triggers a generic "No match" warning. Now the user can see the actual error message from the datasource (e.g. "unauthorized", "not found", etc.) and take appropriate action.

- BUGFIX: Fixed [UI/query-server](#settings-panel) handling of VictoriaMetrics datasource URLs that already include `/select/multitenant/prometheus`. Such URLs are now recognized as cluster datasource URLs, preserving the multitenant path when proxying VMUI requests and allowing `server.use_reader_connection_settings` to reuse [configured reader credentials for authenticated datasources](#authentication).

- BUGFIX: Fixed [settings](#settings-panel) inputs for server and datasource URLs so editing, deleting, or pasting text is no longer immediately reverted to the previous value before applying changes.

- BUGFIX: Fixed [model wizard](#model-panel) settings for [`IsolationForestModel`](https://docs.victoriametrics.com/anomaly-detection/components/models/#isolation-forest-multivariate) `contamination`, allowing decimal float values such as `0.1` or `0,1` to be typed or pasted without being collapsed to `0`, while preserving the `"auto"` value.

### v1.7.1
Released: 2026-06-11

vmanomaly version: [v1.29.5](https://docs.victoriametrics.com/anomaly-detection/changelog/#v1295)

- FEATURE: Added bulk Apply/Decline actions for [Copilot](#ai-assistance) chat suggestions.

- BUGFIX: Fixed modal windows closing when the mouse is released outside the window during text selection.

- BUGFIX: Fixed tooltip hover behavior so tooltips do not disappear while the cursor moves into the hover content.

### v1.7.0
Released: 2026-05-15

vmanomaly version: [v1.29.4](https://docs.victoriametrics.com/anomaly-detection/changelog/#v1294)

- FEATURE: Improved [AI Copilot](#ai-assistance) to 
  - support textual attachments, such as configuration files, query examples, model outputs, etc.
  - operate with current time when suggesting time range changes, e.g. "current month" or "from the beginning of the last month until now"
- FEATURE: improve infer jobs scheduled from UI to
  - run 2-100x faster for [online models](https://docs.victoriametrics.com/anomaly-detection/components/models/#online-models) depending on a configuration vs [1.6.1](#v161) timings
  - show stage-aware progress bar, e.g. "getting data", "fitting model", "inferring on chunk".
- IMPROVEMENT: "Advanced Options" design is improved, section is collapsed by default to save vertical space, yet can be encoded as always open in UI state URL.
- IMPROVEMENT: dropdowns in UI are now searchable and constrained in size for better UX, especially when many options are available (e.g. models list, tenants list, etc.).
- BUGFIX: in generated config ("Show Config" menu)
  - special YAML values (like `-.inf`, `.inf`, `.nan`) are now properly quoted and formatted to avoid JSON converting issues when copied to Kubernetes CRs, which previously led to rejection of the manifest before vmanomaly can consume it.
  - with Data Source selected as "Logs/Traces" `reader.class` is now correctly set to `vlogs` (previously `vm`) in generated config, when "model only" toggle is turned off.
- BUGFIX: now "Hide Common Labels" toggle in "Table View" works correctly and does not show common labels in the legend columns when turned on.
- BUGFIX: "Prettify query" now works correctly for "Metrics" datasources.

### v1.6.1
Released: 2026-04-16

vmanomaly version: [v1.29.3](https://docs.victoriametrics.com/anomaly-detection/changelog/#v1293)

- IMPROVEMENT: Consecutive anomalies (when "streaks" option is enabled) are now grouped in the Visualization Panel as a single anomaly line instead of multiple dots for reduced visual noise and better representation of prolonged anomalous periods, while still showing the exact anomaly score and labels on hover.

- IMPROVEMENT: Raw query results now refresh automatically after time range changes; yet anomaly detection results are preserved until "Detect Anomalies" button is hit again, to avoid recalculating anomalies on the new time range without explicit user action, which could be costly if the new time range is large and the model is complex.

- IMPROVEMENT: Table legend view is now enabled by default for sorting and filtering enablement.

- BUGFIX: Generated config and example alert outputs now preserve configured fit/infer values correctly and avoid invalid float-based duration strings in generated YAML, which could lead to data validation errors if copied to production configuration without adjustments.

- BUGFIX: Fixed multiple confusing anomaly UI behaviors around scheduler fields (fit_every, infer_every) and generated artifacts.

- BUGFIX: Chart y-axis range is now updating after legend series selection (regression introduced in v1.6.0).

### v1.6.0
Released: 2026-04-02

vmanomaly version: [v1.29.2](https://docs.victoriametrics.com/anomaly-detection/changelog/#v1292)

- FEATURE: Now AI assistant can see and modify main UI components state (queries, time range, model configuration, etc.) to provide more contextual and accurate suggestions and actions.

- FEATURE: Added support for UI to use reader-wise settings (credentials, TLS, etc.) for connecting to data sources, which otherwise would require having `vmauth` in front of both UI and data sources, just for the UI to be able to connect to them. See [Authentication](#authentication) section for details.

### v1.5.1
Released: 2026-03-25

vmanomaly version: [v1.29.1](https://docs.victoriametrics.com/anomaly-detection/changelog/#v1291)

- FEATURE: GCP/AWS/OpenRouter Copilot LLM providers are now supported in addition to OpenAI and Anthropic, for more choice and flexibility in AI assistance. See [AI Assistance](#ai-assistance) section for details on supported providers and configuration.

- BUGFIX: Now Visualization Panel correctly switches in between "query" and "detect" modes when respective buttons are hit in the [Visualization Panel](#visualization-panel), without showing stale results from the previous mode, once running anomaly detection task is explicitly cancelled (regression introduced in [v1.5.0](#v150)).

- BUGFIX: Fixed an issue with [crypto.randomUUID](https://developer.mozilla.org/en-US/docs/Web/API/Crypto/randomUUID) introduced in [v1.29.0](https://docs.victoriametrics.com/anomaly-detection/changelog/#v1290) in [UI copilot](https://docs.victoriametrics.com/anomaly-detection/ui/#ai-assistance) that led to the front app showing a blank page.

### v1.5.0
Released: 2026-03-05

vmanomaly version: [v1.29.0](https://docs.victoriametrics.com/anomaly-detection/changelog/#v1290)

- FEATURE: Allowed AI assistance use for documentation Q&A, model configuration suggestion and application, optionally backed by [MCP Server tools](https://github.com/VictoriaMetrics/mcp-vmanomaly/tree/main). Please refer to [AI Assistance](https://docs.victoriametrics.com/anomaly-detection/ui/#ai-assistance) section for details.
- FEATURE: Added filtering of timeseries in the Visualization Panel by labels and statistics (e.g. anomaly count) to focus on the most relevant series when many series are returned by the query.
- BUGFIX: Fixed missing datapoints in [BacktestingScheduler](https://docs.victoriametrics.com/anomaly-detection/components/scheduler/#backtesting-scheduler) windows combined with [exact mode](https://docs.victoriametrics.com/anomaly-detection/components/scheduler/#defining-inference-timeframe-1), leading to "gaps" in plotted predictions and scores.

### v1.4.3
Released: 2026-02-09

vmanomaly version: [v1.28.7](https://docs.victoriametrics.com/anomaly-detection/changelog/#v1287)

- Update color palette in dark theme for more contrast and better visibility of anomalies and confidence intervals in the Visualization Panel.

- Align Model Panel content to improve layout for smaller screens and embedded documentation.

### v1.4.2
Released: 2026-01-17

vmanomaly version: [v1.28.5](https://docs.victoriametrics.com/anomaly-detection/changelog/#v1285)

- Enable preconfigured default UI state via url-encoded `ui_default_state`, so `/vmui/` opens with the intended model settings, time range, query and other parameters. This improves user experience by allowing direct access to specific views without manual configuration each time. See [Default State](https://docs.victoriametrics.com/anomaly-detection/ui/#default-state) section for details.

- Enable autocomplete for VictoriaLogs / VictoriaTraces data sources in query input area.

### v1.4.1
Released: 2026-01-12

vmanomaly version: [v1.28.4](https://docs.victoriametrics.com/anomaly-detection/changelog/#v1284)

- FEATURE: Allow `path_prefix` parameter to override the server's configured URL path prefix for all HTTP routes. This is useful when the UI is served behind a reverse proxy that modifies the base path. For example, if the server is configured with `path_prefix: /my-app`, accessing the UI at `/my-app/` will work correctly even if the proxy serves it at a different base path. It can be set in the `server` [section](https://docs.victoriametrics.com/anomaly-detection/components/server/#parameters) of the configuration file.

### v1.4.0
Released: 2025-12-11

vmanomaly version: [v1.28.2](https://docs.victoriametrics.com/anomaly-detection/changelog/#v1282)

- FEATURE: Added an option to show **consecutive anomalies** (if N points in a row exceed anomaly threshold T) in the Visualization Panel, to reduce visual clutter when many anomalies are detected in a row. The option is available as "Streaks" button in the [Model Panel](#model-panel). Respective "streaks: N" stats appears in legend for each series. Example alerting rule's `for` parameter is adjusted accordingly if streaks are used.
- FEATURE: Timeseries are now sortable in the legend of the [Visualization Panel](#visualization-panel) by clicking on the respective column headers (both label- and statistics-based columns are supported, e.g., sort by series name, anomaly count).
- IMPROVEMENT: It's now possible to pre-configure datasource, so the UI users cannot re-configure datasource from UI or change its type. Suitable for internal team-serving deployments. Please refer to [pre-configured datasource](#pre-configured-datasource) section for details.

### v1.3.0
Released: 2025-12-01

vmanomaly version: [v1.28.1](https://docs.victoriametrics.com/anomaly-detection/changelog/#v1281)

- FEATURE: [Forecasting mode](https://docs.victoriametrics.com/anomaly-detection/faq/#forecasting) is now available in the UI for models that support it (e.g., `Prophet`), allowing users to visualize model predictions into the future (alongside with confidence intervals). Please use "forecast offsets" parameter in the wizard to set the desired forecast horizon(s).
- IMPROVEMENT: Plot area in the Visualization Panel now supports vertical resizing by dragging its right bottom border, followed by respective recalculations of the tick grid of both y-axes.
- IMPROVEMENT: Added explicit versioning information in the UI footer, showing the current service and UI versions for easier tracking and debugging.
- IMPROVEMENT: Tooltips inside [model wizard menu](#model-panel) are now persistent upon (i) icon click and rendered as markdown. To close the tooltip, click outside of it or on the icon again.

### v1.2.0
Released: 2025-11-17

vmanomaly version: [v1.28.0](https://docs.victoriametrics.com/anomaly-detection/changelog/#v1280)

- FEATURE: Added "exact" mode to use in combination with "infer every" control for [online models](https://docs.victoriametrics.com/anomaly-detection/components/models/#online-models) such as `mad_online` or `quantile_online`, to provide unbiased estimates of how production scheduler would perform anomaly detection on incoming data streams. In "exact" mode, the model is updated exactly at every "infer every" micro-batch interval, at a cost of increased computation time. See [model panel](#model-panel) for details.

- FEATURE: Added "Example Alert" button in the [Model Panel](#model-panel) to provide an example of parametrized [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/) alerting rule snippet based on the current UI configuration.

- IMPROVEMENT: Added support for clipboard copy in addition to existing file download of the model/service configuration in YAML format from the [Model Panel](#model-panel) configuration menu.

### v1.1.0
Released: 2025-10-31

vmanomaly version: [v1.27.0](https://docs.victoriametrics.com/anomaly-detection/changelog/#v1270)

> A bug, found in [v1.27.0](https://docs.victoriametrics.com/anomaly-detection/changelog/#v1270) that prevents "Detect Anomalies" button ([model panel](#model-panel)) from working has been fixed in the patch release [v1.27.1](https://docs.victoriametrics.com/anomaly-detection/changelog/#v1271). Please do the upgrade.

- FEATURE: Added support of auth headers, that can be forwarded from vmanomaly to datasources configured in the UI (VictoriaMetrics, VictoriaLogs), see [authentication](#authentication) for details.

- FEATURE: queries (`config.reader.queries.[xxx].expr` values) if [mixed mode is used](#mixed-usage) are read from the server reader config on the first UI initialization, to ease the exploration of existing production queries without the need to retype them in the UI. Press "show history" button next to "execute query" button (in the [Query Explorer](#query-explorer) section) and choose the tab "Server Queries".

- IMPROVEMENT: autocomplete of example parameters for model param fields by hitting Tab key in the [Model Settings wizard](#model-panel), e.g. hitting Tab in the "detection direction" field will cycle through the available options.

- IMPROVEMENT: anomaly threshold element on [Model Panel](#model-panel) is now reactive - no need to refit a model ("Detect Anomalies" button) to see the effect from changed anomaly threshold value.

- IMPROVEMENT: datasource value is initialized from the server reader config (on the first UI initialization) if [mixed mode is used](#mixed-usage). Can be reset to the default value anytime by hitting the "Reset to Default" button next to the datasource field in the [Settings Panel](#settings-panel).

### v1.0.0
Released: 2025-10-02

vmanomaly version: [v1.26.0](https://docs.victoriametrics.com/anomaly-detection/changelog/#v1260)

Initial public release of the vmanomaly UI.

{{% /collapse %}}

</div>
