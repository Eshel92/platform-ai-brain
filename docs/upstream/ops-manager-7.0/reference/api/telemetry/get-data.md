<!-- Converted from reference/api/telemetry/get-data.txt (reStructuredText). Includes are inlined. -->

# Retrieve Telemetry Data

Retrieve telemetry collection status and configuration details for your  
Ops Manager installation.

## Required Roles

This endpoint requires an API key that has the `Global Owner` role.

## Endpoint

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/private/v1.0/telemetry`

```http
GET /collection/details
```

## Request

### Path Parameters

This endpoint doesn't use HTTP request path parameters.

### Query Parameters

This endpoint doesn't use HTTP request query parameters.

### Body Parameters

This endpoint doesn't use HTTP request body parameters.

## Response

### Response Document

The response JSON document includes the following fields:

| Name | Type | Description |
|---|---|---|
| enabled | boolean | Indicates if the system collects and sends telemetry. |
| last_successful_send | datetime | Date and time of the last successful telemetry send. |
| next_job | datetime | Date and time when the next telemetry send is scheduled. |
| data | array | Array of objects defined in the Telemetry Data embedded object. |

### Telemetry Data Embedded Object

Each element in the `data` array describes telemetry details for the
Ops Manager installation.

| Name | Type | Description |
|---|---|---|
| app_db_nodes | integer | Number of AppDB nodes that this Ops Manager installation uses. |
| uuid | string | Static unique identifier for this Ops Manager installation. |
| os | array of strings | Operating systems that run on the Ops Manager hosts. |
| version | string | Current Ops Manager version. |
| instances | integer | Number of Ops Manager instances in this installation. |
| backup_daemons | integer | Number of backup daemons running in this installation. |
| auth_method | string | Authentication method that Ops Manager uses. Possible values: `DB`, `LDAP`, or `SAML`. |
| cpu | array of integers | Number of CPU cores provisioned for each Ops Manager host. |
| memory | array of integers | Amount of memory provisioned for each Ops Manager host. |
| infrastructure | string | Infrastructure type that hosts Ops Manager. Possible values: `Kubernetes`, `VM`, or `Bare Metal`. |
| projects | integer | Total number of projects that currently exist. |
| orgs | integer | Total number of organizations that currently exist. |
| deployments | array | Array of objects defined in the Telemetry Deployments Embedded Object. |

### Telemetry Deployments Embedded Object

Each element in the `deployments` array describes a MongoDB
deployment that Ops Manager manages.

| Name | Type | Description |
|---|---|---|
| version | array of strings | MongoDB versions that the deployment uses. |
| uuid | string | Static unique identifier for the deployment. |
| tls_enabled | boolean | Indicates if TLS (Transport Layer Security) is enabled for the deployment. |
| auth_method | string | Authentication method that the deployment uses. Possible values: `MONGODB-CR`, `GSSAPI`, `PLAIN`, or `MONGODB-X509`. |
| type | string | Deployment type. Possible values: `SC`, `RS`, or `SA`. |
| nodes | integer | Number of nodes in the deployment if it is a replica set. |
| shards | integer | Number of shards in the deployment if it is a sharded cluster. |
| data_size | integer | Total data size for the deployment, not including local metadata. |
| edition | object | Object that contains two keys, `community` and `enterprise`. Each key has an integer value that represents the number of nodes of that edition in the deployment. |

## Example Request

```sh
curl --user "{publicApiKey}:{privateApiKey}" --digest \
  --header "Accept: application/json" \
  --header "Content-Type: application/json" \
  --include \
  --request GET "https://<OpsManagerHost>:<Port>/api/private/v1.0/telemetry/collection/details"
```

## Example Response

### Response Header

```http
HTTP/1.1 401 Unauthorized
Content-Type: application/json;charset=ISO-8859-1
Date: {dateInUnixFormat}
WWW-Authenticate: Digest realm="MMS Public API", domain="", nonce="{nonce}", algorithm=MD5, op="auth", stale=false
Content-Length: {requestLengthInBytes}
Connection: keep-alive
```

```http
HTTP/1.1 200 OK
Vary: Accept-Encoding
Content-Type: application/json
Strict-Transport-Security: max-age=300
Date: {dateInUnixFormat}
Connection: keep-alive
Content-Length: {requestLengthInBytes}
X-MongoDB-Service-Version: gitHash={gitHash}; versionString={ApplicationVersion}
```

### Response Body

```json
{
  "data": {
    "app_db_nodes": 1,
    "auth_method": "DB",
    "backup_daemons": 3,
    "cpu": [
      14,12
    ],
    "infrastructure": "Bare Metal",
    "instances": 2,
    "memory": [
      "3221225472","221225472"
    ],
    "os": [
      "RHEL 8.10 aarch64","RHEL 8.11 aarch64"
    ],
    "orgs": 3,
    "projects": 12,
    "uuid": "84248c7e-94df-4a0c-942a-dfb1fa987edd",
    "version": "8.0.13",
    "deployments": [
      {
        "auth_method": "MONGODB-CR",
        "data_size": 3221225472,
        "edition": {
          "community": 3,
          "enterprise": 0
       },
        "nodes": 3,
        "tls_enabled": true,
        "type": "RS",
        "uuid": "6907dd45d61b992049366140",
        "version": [
          "8.15","7.11"
        ]
       },
       {
         "auth_method": "MONGODB-CR",
           "data_size": 221225472,
           "edition": {
             "community": 1,
             "enterprise": 2
             },
             "shards": 3,
             "tls_enabled": false,
             "type": "SC",
             "uuid": "6907de15d61b9920493664ca",
             "version": [
               "8.15"
             ]
         }
     ],
  },
  "enabled": true,
  "last_successful_send": "2025-10-02T22:26:10Z",
  "next_job": "2025-10-09T22:26:10Z"
}
```
