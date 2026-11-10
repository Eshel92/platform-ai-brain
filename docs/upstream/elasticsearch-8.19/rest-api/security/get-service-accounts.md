<!-- Converted from rest-api/security/get-service-accounts.asciidoc (AsciiDoc). Includes are inlined. -->

### Get service accounts API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Retrieves information about service accounts.

**Note:** Currently, only the `elastic/fleet-server` service account is available.

#### Request

`GET /_security/service`

`GET /_security/service/<namespace>`

`GET /_security/service/<namespace>/<service>`

#### Prerequisites

* To use this API, you must have at least the `manage_service_account`
cluster privilege.

#### Description

This API returns a list of service accounts that match the provided path parameter(s).

#### Path parameters

`namespace`::
  (Optional, string) Name of the namespace. Omit this parameter to retrieve information about all service accounts. If you omit this parameter, you must also omit the `service` parameter.

`service`::
  (Optional, string) Name of the service name. Omit this parameter to
  retrieve information about all service accounts that belong to the specified
  `namespace`.

#### Response body

A successful call returns a JSON object of service accounts. The API returns an
empty object if no service account is found.

#### Examples

To following request retrieves a service account for the `elastic/fleet-server`
service account:

```console
GET /_security/service/elastic/fleet-server
```

```console-result
{
  "elastic/fleet-server": {
    "role_descriptor": {
      "cluster": [
        "monitor",
        "manage_own_api_key",
        "read_fleet_secrets"
      ],
      "indices": [
        {
          "names": [
            "logs-*",
            "metrics-*",
            "traces-*",
            ".logs-endpoint.diagnostic.collection-*",
            ".logs-endpoint.action.responses-*",
            ".logs-endpoint.heartbeat-*"
          ],
          "privileges": [
            "write",
            "create_index",
            "auto_configure"
          ],
          "allow_restricted_indices": false
        },
        {
          "names": [
            "profiling-*"
          ],
          "privileges": [
            "read",
            "write"
          ],
          "allow_restricted_indices": false
        },
        {
          "names": [
            "traces-apm.sampled-*"
          ],
          "privileges": [
            "read",
            "monitor",
            "maintenance"
          ],
          "allow_restricted_indices": false
        },
        {
          "names": [
            ".fleet-secrets*"
          ],
          "privileges": [
            "read"
          ],
          "allow_restricted_indices": true
        },
        {
          "names": [
            ".fleet-actions*"
          ],
          "privileges": [
            "read",
            "write",
            "monitor",
            "create_index",
            "auto_configure",
            "maintenance"
          ],
          "allow_restricted_indices": true
        },
        {
          "names": [
            ".fleet-agents*"
          ],
          "privileges": [
            "read",
            "write",
            "monitor",
            "create_index",
            "auto_configure",
            "maintenance"
          ],
          "allow_restricted_indices": true
        },
        {
          "names": [
            ".fleet-artifacts*"
          ],
          "privileges": [
            "read",
            "write",
            "monitor",
            "create_index",
            "auto_configure",
            "maintenance"
          ],
          "allow_restricted_indices": true
        },
        {
          "names": [
            ".fleet-enrollment-api-keys*"
          ],
          "privileges": [
            "read",
            "write",
            "monitor",
            "create_index",
            "auto_configure",
            "maintenance"
          ],
          "allow_restricted_indices": true
        },
        {
          "names": [
            ".fleet-policies*"
          ],
          "privileges": [
            "read",
            "write",
            "monitor",
            "create_index",
            "auto_configure",
            "maintenance"
          ],
          "allow_restricted_indices": true
        },
        {
          "names": [
            ".fleet-policies-leader*"
          ],
          "privileges": [
            "read",
            "write",
            "monitor",
            "create_index",
            "auto_configure",
            "maintenance"
          ],
          "allow_restricted_indices": true
        },
        {
          "names": [
            ".fleet-servers*"
          ],
          "privileges": [
            "read",
            "write",
            "monitor",
            "create_index",
            "auto_configure",
            "maintenance"
          ],
          "allow_restricted_indices": true
        },
        {
          "names": [
            ".fleet-fileds*"
          ],
          "privileges": [
            "read",
            "write",
            "monitor",
            "create_index",
            "auto_configure",
            "maintenance"
          ],
          "allow_restricted_indices": true
        },
        {
          "names": [
            "synthetics-*"
          ],
          "privileges": [
            "read",
            "write",
            "create_index",
            "auto_configure"
          ],
          "allow_restricted_indices": false
        },
        {
          "names": [
            "agentless-*",
          ],
          "privileges": [
            "read",
            "write",
            "monitor",
            "create_index",
            "auto_configure",
            "maintenance",
            "view_index_metadata"
          ],
          "allow_restricted_indices": false
        }
      ],
      "applications": [
        {
          "application": "kibana-*",
          "privileges": [
            "reserved_fleet-setup"
          ],
          "resources": [
            "*"
          ]
        }
      ],
      "run_as": [],
      "metadata": {},
      "transient_metadata": {
        "enabled": true
      }
    }
  }
}
```

Omit the `namespace` and `service` to retrieve all service accounts:

```console
GET /_security/service
```
