<!-- Converted from user/api.asciidoc (AsciiDoc). Includes are inlined. -->

# REST API

Some Kibana features are provided via a REST API, which is ideal for creating an
integration with Kibana, or automating certain aspects of configuring and
deploying Kibana.

**Note:** Access to internal Kibana API endpoints will be restricted in 9.0. Please move any integrations to publicly documented APIs.

**Note:** For the latest details, refer to [Kibana API](https://www.elastic.co/docs/api/doc/kibana).

## Using the APIs

Prepend any Kibana API endpoint with `kbn:` and send the request through <<console-kibana, Dev Tools > Console>>.
For example:

```sh
`GET kbn:/api/index_management/indices`
```

Note: this will automatically prefix `s/{space_id}/` on the API request if ran from a non-default Kibana Space.

### Authentication

The Kibana APIs support key- and token-based authentication.

#### Token-based authentication

To use token-based authentication, you use the same username and password that you use to log into Elastic.
In a given HTTP tool, and when available, you can select to use its 'Basic Authentication' option,
which is where the username and password are stored in order to be passed as part of the call.

#### Key-based authentication

To use key-based authentication, you create an API key using the Elastic Console, then specify the key in the header of your API calls.

For information about API keys, refer to API keys.

### API calls

API calls are stateless. Each request that you make happens in isolation from other calls and must include all of the necessary information for Kibana to fulfill the request. API requests return JSON output, which is a format that is machine-readable and works well for automation.

Calls to the API endpoints require different operations. To interact with the Kibana APIs, use the following operations:

* *GET* - Fetches the information.

* *POST* - Adds new information.

* *PUT* - Updates the existing information.

* *PATCH* - Applies partial modifications to the existing information.

* *DELETE* - Removes the information.

### Request headers

For all APIs, you must use a request header. The Kibana APIs support the `kbn-xsrf` and `Content-Type` headers.

`kbn-xsrf: true`::
  By default, you must use `kbn-xsrf` for all API calls, except in the following scenarios:

* The API endpoint uses the `GET` or `HEAD` operations
* The path is allowed using the `server.xsrf.allowlist` setting
* XSRF protections are disabled using the `server.xsrf.disableProtection` setting

`Content-Type: application/json`::
  Applicable only when you send a payload in the API request. Kibana API requests and responses use JSON.
  Typically, if you include the `kbn-xsrf` header, you must also include the `Content-Type` header.

Request header example:

```sh
curl -X POST \
  http://localhost:5601/api/spaces/space \
  -H 'Content-Type: application/json' \
  -H 'kbn-xsrf: true' \
  -d '{
	"id": "sales",
	"name": "Sales",
	"description": "This is your Sales Space!",
	"disabledFeatures": []
}
'
```

(See `api/features.md`)
(See `api/spaces-management.md`)
(See `api/role-management.md`)
(See `api/session-management.md`)
(See `api/saved-objects.md`)
(See `api/data-views.md`)
(See `api/index-patterns.md`)
(See `api/alerting.md`)
(See `api/actions-and-connectors.md`)
(See `api/cases.md`)
(See `api/dashboard-api.md`)
(See `api/logstash-configuration-management.md`)
(See `api/machine-learning.md`)
(See `api/short-urls.md`)
(See `api/task-manager/health.md`)
(See `api/upgrade-assistant.md`)
(See `api/synthetics/synthetics-api.md`)
(See `api/uptime-api.md`)
