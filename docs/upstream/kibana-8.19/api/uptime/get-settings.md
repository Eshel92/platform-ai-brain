<!-- Converted from api/uptime/get-settings.asciidoc (AsciiDoc). Includes are inlined. -->

## Get settings API

Retrieve uptime settings existing settings.

### Request

`GET <kibana host>:<port>/api/uptime/settings`

`GET <kibana host>:<port>/s/<space_id>/api/uptime/settings`

### Prerequisites

You must have `read` privileges for the *uptime* feature in *Observability* section of the
Kibana feature privileges.

The API returns the following:

```sh
{
    "heartbeatIndices": "heartbeat-8*",
    "certExpirationThreshold": 30,
    "certAgeThreshold": 730,
    "defaultConnectors": [
        "08990f40-09c5-11ee-97ae-912b222b13d4",
        "db25f830-2318-11ee-9391-6b0c030836d6"
    ],
    "defaultEmail": {
        "to": [],
        "cc": [],
        "bcc": []
    }
}
```
