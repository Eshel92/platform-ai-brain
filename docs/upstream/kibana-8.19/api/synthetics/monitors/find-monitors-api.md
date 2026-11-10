<!-- Converted from api/synthetics/monitors/find-monitors-api.asciidoc (AsciiDoc). Includes are inlined. -->

## Find Monitors API

Get a list of monitors based on query parameters.

### Request

`GET <kibana host>:<port>/api/synthetics/monitors`

`GET <kibana host>:<port>/s/<space_id>/api/synthetics/monitors`

### Prerequisites

You must have `read` privileges for the *Synthetics* feature in the *Observability* section of the
Kibana feature privileges.

### Path parameters

`space_id`::
(Optional, string) An identifier for the space. If `space_id` is not provided in
the URL, the default space is used.

### Query parameters

`page`::
(optional, integer): Page number for paginated results.

`perPage`::
(optional, integer): Number of items per page.

`sortField`::
(optional, string): Field to sort the results by. Possible values: `name`, `createdAt`, `updatedAt`, `status`.

`sortOrder`::
(optional, string): Sort order (asc or desc).

`query`::
(optional, string): Free-text query string.

`filter`::
(optional, string): Additional filtering criteria.

`tags`::
(optional, string or array): Tags to filter monitors.

`monitorTypes`::
(optional, string or array): Monitor types to filter, (e.g., `http` , `tcp` , `icmp` or `browser`)

`locations`::
(optional, string or array): Locations to filter by.

`projects`::
(optional, string or array): Projects to filter by.

`schedules`::
(optional, string or array): Schedules to filter by.

`status`::
(optional, string or array): Status to filter by.

#### Examples

Here is an example of how to use this API:

```sh
GET /api/synthetics/monitors?tags=prod&monitorTypes=http&locations=us-east-1&projects=project1&status=up
{
    "page": 1,
    "total": 24,
    "monitors": [
        {
            "type": "icmp",
            "enabled": false,
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
            "config_id": "e59142e5-1fe3-4aae-b0b0-19d6345e65a1",
            "timeout": "16",
            "name": "8.8.8.8:80",
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
            "id": "e59142e5-1fe3-4aae-b0b0-19d6345e65a1",
            "max_attempts": 2,
            "wait": "7",
            "revision": 3,
            "mode": "all",
            "ipv4": true,
            "ipv6": true,
            "created_at": "2023-11-07T09:57:04.152Z",
            "updated_at": "2023-12-04T19:19:34.039Z",
            "host": "8.8.8.8:80"
        }
    ],
    "absoluteTotal": 24,
    "perPage": 10,
}
```
