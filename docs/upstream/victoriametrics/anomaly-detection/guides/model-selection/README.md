---
build:
  list: never
  publishResources: false
  render: never
sitemap:
  disable: true
---

Start with the operational question you want to answer, then choose a recipe that matches your data. You do not need a machine learning background: each recipe explains what to look for, which model to use, and how to try it before connecting your own metrics.

> [!TIP]
> **Get a starting configuration faster with AI.** Try [AI Copilot in the UI](https://docs.victoriametrics.com/anomaly-detection/ui/#ai-assistance), or use your AI assistant with the [MCP server](https://docs.victoriametrics.com/ai-tools/#vmanomaly-mcp-server) and [agent skills](https://docs.victoriametrics.com/ai-tools/#agent-skills). Ask it to search the docs, inspect your query's data, suggest a model, validate the configuration, and autotune supported parameters.

<!-- This page was over 60 KB, so its sections are separate files. -->

## Sections (in `README.parts/`)

- `001-choose-what-to-compare-follow-each-metric-over-tim.md`: Choose what to compare … Follow each metric over time
- `002-follow-each-metric-over-time-steady-baseline-small.md`: Follow each metric over time › Steady baseline, small fluctuations
- `003-follow-each-metric-over-time-steady-baseline-with-.md`: Follow each metric over time › Steady baseline with extreme values
- `004-follow-each-metric-over-time-predictable-repeating.md`: Follow each metric over time › Predictable repeating patterns
- `005-follow-each-metric-over-time-changing-baselines-an.md`: Follow each metric over time › Changing baselines and calendar effects
- `006-watch-related-signals-together.md`: Watch related signals together
- `007-find-the-odd-one-out-apply-a-recipe-to-your-own-me.md`: Find the odd one out … Apply a recipe to your own metrics
