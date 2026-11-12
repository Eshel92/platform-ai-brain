<!-- Part 2 of 5 of anomaly-detection/UI.md (split because the page is big). -->

## AI Assistance

{{< available_from "v1.29.0" anomaly >}} Copilot is an AI assistant built into the vmanomaly UI. It understands current anomaly detection configuration in the UI and helps iterate faster and obtain better results - without leaving the UI, searching the docs manually, or being an expert in anomaly detection.

### What you can do with Copilot

- **Ask questions** about any model (e.g. [Temporal Envelope](https://docs.victoriametrics.com/anomaly-detection/components/models/#temporal-envelope), [Online Seasonal Quantile](https://docs.victoriametrics.com/anomaly-detection/components/models/#online-seasonal-quantile), or [Online Z-score](https://docs.victoriametrics.com/anomaly-detection/components/models/#online-z-score) - parameters, trade-offs, when to use each)
- **Improve detection quality** - describe what's wrong ("too many false positives", "missing spikes") and Copilot reads the config, searches the docs, and proposes a validated configuration change to fix the issue.
- **Get config suggestions inline** - suggestions appear as interactive cards with an explanation and a YAML diff; click **Apply** to write the change directly to your current settings, or **Decline** to keep the conversation going.
- {{< available_from "v1.30.0" anomaly >}} **Profile and tune the real query** - with [mcp-vmanomaly](#mcp-tools-server) connected, Copilot can inspect bounded time-series characteristics, recommend an online model, start an asynchronous autotune task, and apply its validated query and model suggestions.
- {{< available_from "v1.32.0" anomaly >}} **Discover available signals** — inspect metric names, labels and bounded series metadata in the selected datasource and tenant before choosing queries. Discovery respects the configured scope and reports truncated results.
- {{< available_from "v1.32.0" anomaly >}} **Build a [dynamic preset](https://docs.victoriametrics.com/anomaly-detection/presets/#dynamic-presets)** — prepare configuration, matching alert rules and optional Compose, Helm or VM Operator files, with resource estimates and explicit draft requirements.

### How it works

Copilot appears as a **chat popup** anchored to the bottom-right corner of the page. The panel is resizable by dragging its left edge, and can be opened or closed by clicking the respective icon.

> [!TIP] Copilot is context-aware
> It reads your active model, scheduler, and anomaly settings from the UI automatically, so you don't need to paste your config manually. {{< available_from "v1.29.2" anomaly >}} It also can read and modify full UI settings, such as data source URL, query parameters, scheduler settings, and more, to provide better suggestions.

Completed tool activity between chat messages is grouped in a collapsible **Tool activity** section. Approvals and generated file cards stay visible. Downloadable YAML has a syntax-highlighted preview; review draft requirements and validation warnings before using it.

### Configuration

AI Assistant is disabled by default; enable it with `VMANOMALY_COPILOT_ENABLED=true`, then configure credentials for the selected LLM provider and **explicitly set** `VMANOMALY_COPILOT_MODEL` to the exact model Copilot should use. Do not rely on an implicit default model being selected. Once enabled and configured, Copilot will appear as a chat popup in the bottom-right corner of the UI.


Supported providers and model formats:

- **Anthropic** - set `ANTHROPIC_API_KEY`; model format: `anthropic:<model>`
  - Examples: `claude-haiku-4-5`, `claude-sonnet-5`; see [full list](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison)
- **OpenAI** - set `OPENAI_API_KEY`; model format: `openai:<model>` or `openai-responses:<model>`
  - Examples: `gpt-5-mini`, `gpt-5.2`; see [full list](https://platform.openai.com/docs/models)
  - {{< available_from "v1.29.1" anomaly >}} OpenAI-compatible non-OpenAI providers are supported through `OPENAI_BASE_URL` + `OPENAI_API_KEY`
  - {{< available_from "v1.29.1" anomaly >}} Azure OpenAI is supported through `AZURE_OPENAI_ENDPOINT` + `OPENAI_API_VERSION` + `AZURE_OPENAI_API_KEY` (or `AZURE_OPENAI_AD_TOKEN`); do not set both `OPENAI_BASE_URL` and `AZURE_OPENAI_ENDPOINT`
- {{< available_from "v1.29.1" anomaly >}} **Google** - model format: `google-gla:<model>` or `google-vertex:<model>`
  - Use `GOOGLE_API_KEY` for `google-gla`; for `google-vertex`, use Application Default Credentials, a service account (`GOOGLE_APPLICATION_CREDENTIALS`), or `GOOGLE_API_KEY`
  - Example: `google-gla:gemini-2.5-pro-preview`
- {{< available_from "v1.29.1" anomaly >}} **AWS Bedrock** - use AWS credentials or an IAM role; model format: `bedrock:<model>`
  - Preferred: set `AWS_BEARER_TOKEN_BEDROCK` and `AWS_DEFAULT_REGION`
  - Alternative: set `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_DEFAULT_REGION` (add `AWS_SESSION_TOKEN` if using a session token)
  - Example: `bedrock:anthropic.claude-sonnet-4-5-20250929-v1:0`
- {{< available_from "v1.29.1" anomaly >}} **OpenRouter** - set `OPENROUTER_API_KEY`; model format: `openrouter:<model>`
  - Example: `openrouter:anthropic/claude-sonnet-4-5`

Set the credentials matching your selected provider:

```bash
# Anthropic
export ANTHROPIC_API_KEY=your_key_here

# OpenAI
export OPENAI_API_KEY=your_key_here

# OpenAI-compatible non-OpenAI providers
export OPENAI_BASE_URL=https://api.example.com/v1
export OPENAI_API_KEY=your_key_here

# Azure OpenAI
export AZURE_OPENAI_ENDPOINT=https://example.openai.azure.com
export OPENAI_API_VERSION=2024-10-21
export AZURE_OPENAI_API_KEY=your_key_here
# or: export AZURE_OPENAI_AD_TOKEN=your_entra_token

# Google Generative Language API
export GOOGLE_API_KEY=your_key_here

# Google Vertex AI service account
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json
# or use Application Default Credentials: gcloud auth application-default login

# OpenRouter
export OPENROUTER_API_KEY=your_key_here

# AWS Bedrock (preferred: bearer token)
export AWS_BEARER_TOKEN_BEDROCK=your_bearer_token
export AWS_DEFAULT_REGION=us-east-1
# AWS Bedrock (alternative: access key pair or IAM role)
# export AWS_ACCESS_KEY_ID=your_access_key
# export AWS_SECRET_ACCESS_KEY=your_secret_key
# export AWS_DEFAULT_REGION=us-east-1
# export AWS_SESSION_TOKEN=your_session_token  # if using a session token
```

Explicitly set the model Copilot should use:

```bash
export VMANOMALY_COPILOT_MODEL=openai:gpt-5-mini
```

For example, if a smaller OpenAI model is desired, set:

```bash
export VMANOMALY_COPILOT_MODEL=openai:gpt-5-nano
```

### Copilot usage and estimated cost

{{< available_from "v1.30.5" anomaly >}} To confirm that Copilot initialized for a particular instance, check `vmanomaly_copilot_enabled{instance="<scrape-target>"}` on its QueryServer metrics: `1` means available, `0` means disabled or unavailable at startup. Missing data does not mean disabled; check the scrape target’s `up` metric. Use `vmanomaly_copilot_configured` alongside it: `configured=0, enabled=0` means intentionally disabled; `configured=1, enabled=0` means requested but unavailable. This startup status does not test live provider credentials, quota, or MCP connectivity. See [AI Copilot metrics](https://docs.victoriametrics.com/anomaly-detection/components/monitoring/#ai-copilot-metrics).

{{< available_from "v1.30.5" anomaly >}} UI v1.9.0 shows token usage and approximate USD costs for individual responses and the current conversation. Expand a usage row to see model request and response counts, cached input tokens, and the provider/model used. For example (illustrative values):

```text
Conversation: 23,984 input · 863 output tokens · ≈ $0.084897
2 model requests · 2 reported responses.
Cached input: 0 read, 0 written (included in input).
anthropic:claude-sonnet-5
Estimate uses model list prices; actual billing may differ. Excludes tool/server compute costs.
Total covers this chat since it was opened or cleared.
```

Estimates use model list prices and provider-reported usage; they are not billing totals or a spending limit. Unknown prices display **Cost unavailable**, and incomplete accounting or a mix of priced and unpriced responses produces a partial estimate. Totals cover usage received by this browser chat and reset when the page is reloaded or the conversation is cleared. Closing and reopening the chat panel does not reset them. No extra provider requests are made to calculate costs.

See [AI Copilot metrics](https://docs.victoriametrics.com/anomaly-detection/components/monitoring/#ai-copilot-metrics) for process-wide estimated-cost and pricing-availability counters.

### Copilot context budgets

{{< available_from "v1.30.5" anomaly >}} Configure the backend with `VMANOMALY_COPILOT_MAX_CONTEXT_BYTES` (default `320000`) and `VMANOMALY_COPILOT_MAX_OUTPUT_TOKENS` (default `8192`). The backend compacts duplicate completed tool results while preserving query and approval data. Oversized requests can still be refused locally; start a fresh conversation or narrow the request. These byte and output-token ceilings are independent and do not guarantee that every provider request fits its context window.

See [AI Copilot metrics](https://docs.victoriametrics.com/anomaly-detection/components/monitoring/#ai-copilot-metrics) to inspect context growth, provider-reported usage and budget refusals.

{{< available_from "v1.32.0" anomaly >}} Preset analysis also has per-request tool budgets, including failed attempts. When analysis cannot finish, Copilot can return drafts with quality marked unverified. Context-budget failures are not automatically retried; start a new conversation when requested.

### MCP tools server

Connects Copilot to [mcp-vmanomaly](https://github.com/VictoriaMetrics/mcp-vmanomaly) for full tool access (built-in docs, models configuration and validation, alerts recommendation, service healthchecks, etc.). Full [tools list](https://github.com/VictoriaMetrics/mcp-vmanomaly?tab=readme-ov-file#toolset):

> [!NOTE]
> Only `http` [mode](https://github.com/VictoriaMetrics/mcp-vmanomaly?tab=readme-ov-file#modes) is supported. Set `VMANOMALY_MCP_SERVER_URL` to the MCP server HTTP endpoint. The server must be reachable from within the vmanomaly container.

For example:

```bash
export VMANOMALY_MCP_SERVER_URL=http://localhost:8081/mcp
```

For HTTPS access to VMUI/API and MCP client certificates, see [TLS and mutual TLS](https://docs.victoriametrics.com/anomaly-detection/components/server/#tls-and-mutual-tls). The MCP-to-vmanomaly connection is configured separately from `VMANOMALY_MCP_SERVER_URL`.

Use `localhost` only when the vmanomaly process can reach the MCP server on its own loopback interface (for example, both running on the host). If vmanomaly runs in a separate Docker container, use a reachable container or host address instead.

**Example**: if using Docker, run `mcp-vmanomaly` and vmanomaly UI in the same Docker network so they can reach each other by container name:

```bash
docker network create vmanomaly-network

docker run -d --rm \
  --name mcp-vmanomaly \
  --network vmanomaly-network \
  -e VMANOMALY_ENDPOINT=http://vmanomaly-instance:8490 \
  -e MCP_SERVER_MODE=http \
  -e MCP_LISTEN_ADDR=:8081 \
  ghcr.io/victoriametrics/mcp-vmanomaly

docker run -it --rm \
  --name vmanomaly-instance \
  --network vmanomaly-network \
  -e VMANOMALY_COPILOT_ENABLED=true \
  -e OPENAI_API_KEY="$OPENAI_API_KEY" \
  -e VMANOMALY_COPILOT_MODEL=openai:gpt-5-mini \
  -e VMANOMALY_MCP_SERVER_URL=http://mcp-vmanomaly:8081/mcp \
  -p 8080:8080 \
  -p 8490:8490 \
  victoriametrics/vmanomaly:v1.32.0 \
  vmanomaly_config.yaml
```



## Guided tours

{{< available_from "v1.32.0" anomaly >}} Use **Take a tour** in the header to explore the UI with built-in demo data, without connecting a datasource. **Get started** walks through queries, model settings and detection; **Tune a model with marks** demonstrates marking a missed anomaly and reviewing a tuned candidate. Tours start only when selected and restore your previous workspace when they end. Demo data is for exploration, not a production datasource.


## UI Navigation

The UI has four main areas:

- [**Query Explorer**](#query-explorer): A vmui-like interface for typing and executing MetricsQL/LogsQL queries to visualize data.
- [**Model Panel**](#model-panel): A form for editing anomaly detection model hyperparameters and applying domain knowledge settings.
- [**Visualization Panel**](#visualization-panel): A space for visualizing model performance and anomalies.
- [**Settings Panel**](#settings-panel): A section for configuring global settings and preferences for the vmanomaly UI, including data source configuration.

### Query Explorer

{{< available_from "v1.30.5" anomaly >}} UI v1.9.0 supports multiple named queries in one experiment. Add, remove, rename, reorder or disable query rows, and select which active aliases a model uses. Saved query sets and URL sharing retain query composition and business policies.

For each query, optionally configure [`data_range`](https://docs.victoriametrics.com/anomaly-detection/components/reader/#per-query-parameters), [`detection_direction`](https://docs.victoriametrics.com/anomaly-detection/components/models/#detection-direction), [`min_dev_from_expected`](https://docs.victoriametrics.com/anomaly-detection/components/models/#minimal-deviation-from-expected) and [`min_rel_dev_from_expected`](https://docs.victoriametrics.com/anomaly-detection/components/models/#minimal-relative-deviation-from-expected). **Use model default** means the field inherits its model fallback; turn it off to apply a **Query override**. Explicit zero deviations, `both`, and unbounded ranges are valid overrides. Editing a query override does not change the model defaults. Relative deviations are percentages of the expected value, not percentage-point differences.

Use Query Explorer to run MetricsQL or LogsQL queries and visualize input data.

![Query Explorer with two named queries, per-query business policies and model-default inheritance controls](vmanomaly-ui-sections-explore.webp)

Users can:
- Enter, autocomplete, prettify and execute queries to retrieve and plot the data from the configured data source (see [settings panel](#settings-panel) for data source configuration).
- Adjust the (inference) time range and resolution (step) for data visualization and anomaly detection purposes.
- Access query history and saved queries for quick access to frequently used queries.
- Switch tenants (if data source supports multi-tenancy) and access [settings panel](#settings-panel) for global UI configuration.

Open **Queries** to browse the **Session**, **History**, **Favorites** and **Server** tabs. In **Session**, **History** and **Favorites**, search for a query set and expand **Show query details** to inspect its named expressions and business policies before reusing it.

{{< available_from "v1.30.6" anomaly >}} UI v1.9.1 presents **Server** queries as a flat list. Use search and the model filter together; a query may belong to several models, shown as badges. Each row supports append or replace, with or without running, plus copy and favorite actions. Selecting queries opens a bulk-action bar showing selected aliases and indicating selections hidden by the current filter. Bulk actions apply to the entire selection. See the UI's keyboard-shortcuts help for Queries-sheet shortcuts.

![Queries menu showing history entries with named queries and expanded business policies](vmanomaly-ui-queries-menu.webp)

[Back to UI navigation](#ui-navigation)

### Visualization Panel

The Visualization Panel displays either raw query results or model output, depending on the selected action.

After selecting **Execute Query**:

![vmanomaly-ui-sections-plot-area-query-mode](vmanomaly-ui-sections-plot-area-query-mode.webp)

All returned series appear in one vmui-like plot with zooming and panning.

After selecting **Detect Anomalies**:

![vmanomaly-ui-sections-plot-area-detect-mode](vmanomaly-ui-sections-plot-area-detect-mode.webp)

The plot groups model output by input series and compares actual values (`y`) with predictions (`yhat`), confidence intervals (`yhat_lower`, `yhat_upper`), and detected anomalies. Hover over an anomaly marker to inspect its score and labels.

Toggle individual output series from the legend.

{{< available_from "v1.29.2" anomaly >}} Enable **Business Boundaries** to overlay the configured [detection direction](https://docs.victoriametrics.com/anomaly-detection/components/models/#detection-direction) and combined [absolute](https://docs.victoriametrics.com/anomaly-detection/components/models/#minimal-deviation-from-expected) and [relative](https://docs.victoriametrics.com/anomaly-detection/components/models/#minimal-relative-deviation-from-expected) minimum-deviation bands. Toggle individual bands from the legend or all bands with the main control.

[Back to UI navigation](#ui-navigation)

### Model Panel

![vmanomaly-ui-sections-model](vmanomaly-ui-sections-model.webp)

The Model Panel provides:

- Scheduling controls such as **Fit Every**, **Fit Window**, and {{< available_from "v1.28.0" anomaly >}} **Infer Every** for imitating [production scheduling](https://docs.victoriametrics.com/anomaly-detection/components/scheduler/#periodic-scheduler).
- An override for the default [anomaly detection threshold](https://docs.victoriametrics.com/anomaly-detection/faq/#what-is-anomaly-score) of `1.0`.
- Actions for running or canceling detection, downloading results, and exporting model configurations or example alerting rules.

> {{< available_from "v1.28.0" anomaly >}} For [online models](https://docs.victoriametrics.com/anomaly-detection/components/models/#online-models), combine **Exact** mode with **Infer Every** to reproduce causal production micro-batches. This gives a more representative backtest at the cost of additional computation.

A form-based menu configures model hyperparameters and domain knowledge:

- Model selection, for example Temporal Envelope or Online MAD.
![vmanomaly-ui-model-config-menu](vmanomaly-ui-model-config-menu.webp)
- A wizard with **model-agnostic settings** such as detection direction, data range, clipping, and minimum deviation, plus the selected model's hyperparameters. {{< available_from "v1.27.0" anomaly >}} Press **Tab** to autocomplete suggested values.
  <a class="content-image d-flex justify-content-center" data-bs-target="#image-modal" data-bs-toggle="modal" href="/anomaly-detection/vmanomaly-ui-model-config-wizard.webp"><img alt="vmanomaly-ui-model-config-wizard" class="w-75 mx-auto" src="/anomaly-detection/vmanomaly-ui-model-config-wizard.webp" style="min-width: 0;" /></a>

[Back to UI navigation](#ui-navigation)

### Settings Panel

The vmui-like "Settings" panel allows users to configure global settings and preferences for the vmanomaly UI, including:

- Server URL (vmanomaly)
- Datasource URL (VictoriaMetrics, VictoriaLogs)
- Timezone
- UI Theme
- {{< available_from "v1.27.0" anomaly >}} Auth Headers forwarding to datasource (VictoriaMetrics, VictoriaLogs).

![vmanomaly-ui-sections-settings](vmanomaly-ui-sections-settings.webp)
{class="w-50 mx-auto"}

[Back to navigation](#ui-navigation)
