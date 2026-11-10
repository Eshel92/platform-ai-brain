<!-- Converted from api/synthetics/monitors/get-monitor-api.asciidoc (AsciiDoc). Includes are inlined. -->

## Get Monitor API

Get a monitor with the config_id. If the monitor is not found, then this API returns a 404 error.

### Request

`GET <kibana host>:<port>/api/synthetics/monitors/<config_id>`

`GET <kibana host>:<port>/s/<space_id>/api/synthetics/monitors/<config_id>`

### Prerequisites

You must have `read` privileges for the *Synthetics* feature in the *Observability* section of the
Kibana feature privileges.

### Path parameters

`config_id`::
(Required, string) The ID of the monitor that you want to update.

`space_id`::
(Optional, string) An identifier for the space. If `space_id` is not provided in
the URL, the default space is used.

#### Examples

Here is an example of how to use this API:

```sh
GET /api/synthetics/monitors/<config_id>
{
    "type": "http",
    "enabled": true,
    "alert": {
        "status": {
            "enabled": true
        },
        "tls": {
            "enabled": true
        }
    },
    "schedule": {
        "number": "3",
        "unit": "m"
    },
    "config_id": "a8188705-d01e-4bb6-87a1-64fa5e4b07ec",
    "timeout": "16",
    "name": "am i something",
    "locations": [
        {
            "id": "us_central",
            "label": "North America - US Central",
            "geo": {
                "lat": 41.25,
                "lon": -95.86
            },
            "isServiceManaged": true
        }
    ],
    "namespace": "default",
    "origin": "ui",
    "id": "a8188705-d01e-4bb6-87a1-64fa5e4b07ec",
    "max_attempts": 2,
    "__ui": {
        "is_tls_enabled": false
    },
    "max_redirects": "0",
    "response.include_body": "on_error",
    "response.include_headers": true,
    "check.request.method": "GET",
    "mode": "any",
    "response.include_body_max_bytes": "1024",
    "ipv4": true,
    "ipv6": true,
    "ssl.verification_mode": "full",
    "ssl.supported_protocols": [
        "TLSv1.1",
        "TLSv1.2",
        "TLSv1.3"
    ],
    "revision": 13,
    "created_at": "2023-11-08T08:45:29.334Z",
    "updated_at": "2023-12-18T20:31:44.770Z",
    "url": "https://<example-url>"
}
```
