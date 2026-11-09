<!-- Converted from reference/api/agents.txt (reStructuredText). Includes are inlined. -->

# Agents

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Endpoints

### Agents

The following endpoints are available for Agents:

| Method | Endpoint | Description |
|---|---|---|
| GET | /groups/{PROJECT-ID}/agents | Return list of links to Agent resources in one Ops Manager `project`. |
| GET | /groups/{PROJECT-ID}/agents/{TYPE} | Return list of Agents of a specified type in one Ops Manager `project`. |

|  |  |  |
|---|---|---|
| GET | /softwareComponents/versions | Return list of earliest and latest versions of MongoDB Agent, MongoDB Tools, and `BI Connector` in your Ops Manager environment. |
| GET | /groups/{PROJECT-ID}/agents/versions | Return list of versions of all MongoDB Agents, in the provided your Ops Manager Project. |

### Agents API Keys

The following endpoints are available for Agent API Keys:

| Method | Endpoint | Description |
|---|---|---|
| POST | /groups/{PROJECT-ID}/agentapikeys | Create one Agent API Key in one Ops Manager `project`. |
| GET | /groups/{PROJECT-ID}/agentapikeys | Return list of all Agent API Keys in one Ops Manager `project`. |
| DELETE | /groups/{PROJECT-ID}/agentapikeys/{API-AGENT-KEY-ID} | Remove one Agent API Key in one Ops Manager `project`. |
