<!-- Converted from reference/api/automation-config/update-monitoring-log-attributes.txt (reStructuredText). Includes are inlined. -->

# Update Monitoring Configuration Settings

## Required Roles

This resource requires the `Project Automation Admin` role.

## Resource

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

```http
PUT /groups/{PROJECT-ID}/automationConfig/monitoringAgentConfig
```

## Request

### Path Parameters

| Name | Type | Necessity | Description |
|---|---|---|---|
| PROJECT-ID | string | Required | Unique 24-hexadecimal digit string that identifies the `project` that owns the configuration. |

### Query Parameters

The following query parameters are optional:

* - Name
  - Type
  - Necessity
  - Description
  - Default

* - pretty
  - boolean
  - Optional
  - Flag indicating whether the response body should be in a
    prettyprint format.
  - `false`

* - envelope
  - boolean
  - Optional
  - Flag that indicates whether or not to wrap the response in an
    envelope.

    Some API (Application Programming Interface) clients cannot access the HTTP (Hypertext Transfer Protocol) response headers or
    status code. To remediate this, set **envelope=true** in the
    query.

    For endpoints that return one result, the response body
    includes:

    | Name | Description |
    |---|---|
    | status | HTTP (Hypertext Transfer Protocol) response code |
    | envelope | Expected response body |

  - `false`

### Body Parameters

To change these settings with the MongoDB Agent, include one or more
of these parameters in the request body.

* - Parameter
  - Type
  - Necessity
  - Description

* - configOverrides
  - object
  - Optional
  - List of MongoDB Agent settings that you need to change because
    your monitoring settings differ from those of the
    MongoDB Agent. Configure
    this option when upgrading from legacy agents to the
    MongoDB Agent.

    | Setting | Data Type |
    |---|---|
    | `mmsGroupId` | string |
    | `mmsApiKey` | string |
    | `mmsBaseUrl` | string |
    | `httpProxy` | string |
    | `krb5Principal` | string |
    | `krb5Keytab` | string |
    | `krb5ConfigLocation` | string |
    | `gssapiServiceName` | string |
    | `useSslForAllConnections` | boolean |
    | `sslClientCertificate` | string |
    | `sslClientCertificatePassword` | string |
    | `sslTrustedServerCertificates` | string |
    | `sslRequireValidServerCertificates` | boolean |
    | `enableMunin` | boolean |

* - logPath
  - string
  - Optional
  - Absolute file path to which this MongoDB Agent writes its logs.
    If this is not specified, the log writes to standard error
    (`stderr`) on UNIX- and Linux-based systems and to the Event
    Log on Windows systems.

* - logRotate
  - object
  - Optional
  - Thresholds after which this MongoDB Agent rotates the monitoring
    log.

* - | logRotate
    | .sizeThresholdMB
  - integer
  - Optional
  - Maximum size, in MB, of a log file before this MongoDB Agent
    rotates the logs.

* - | logRotate
    | .timeDurationHrs
  - integer
  - Optional
  - Number of hours after which this MongoDB Agent rotates the log
    file.

* - username
  - string
  - Optional
  - MongoDB user in the application database that manages the
    monitoring logs.

    If you use the API (Application Programming Interface) to enable authentication for the
    MongoDB Agent, set this parameter to **mms-automation** when
    executing this endpoint.

## Response

* - Parameter
  - Type
  - Necessity
  - Description

* - configOverrides
  - object
  - Optional
  - List of MongoDB Agent settings that you need to change because
    your monitoring settings differ from those of the
    MongoDB Agent. Configure
    this option when upgrading from legacy agents to the
    MongoDB Agent.

    | Setting | Data Type |
    |---|---|
    | `mmsGroupId` | string |
    | `mmsApiKey` | string |
    | `mmsBaseUrl` | string |
    | `httpProxy` | string |
    | `krb5Principal` | string |
    | `krb5Keytab` | string |
    | `krb5ConfigLocation` | string |
    | `gssapiServiceName` | string |
    | `useSslForAllConnections` | boolean |
    | `sslClientCertificate` | string |
    | `sslClientCertificatePassword` | string |
    | `sslTrustedServerCertificates` | string |
    | `sslRequireValidServerCertificates` | boolean |
    | `enableMunin` | boolean |

* - logPath
  - string
  - Optional
  - Absolute file path to which this MongoDB Agent writes its logs.
    If this is not specified, the log writes to standard error
    (`stderr`) on UNIX- and Linux-based systems and to the Event
    Log on Windows systems.

* - logRotate
  - object
  - Optional
  - Thresholds after which this MongoDB Agent rotates the monitoring
    log.

* - | logRotate
    | .sizeThresholdMB
  - integer
  - Optional
  - Maximum size, in MB, of a log file before this MongoDB Agent
    rotates the logs.

* - | logRotate
    | .timeDurationHrs
  - integer
  - Optional
  - Number of hours after which this MongoDB Agent rotates the log
    file.

* - username
  - string
  - Optional
  - MongoDB user in the application database that manages the
    monitoring logs.

    If you use the API (Application Programming Interface) to enable authentication for the
    MongoDB Agent, set this parameter to **mms-automation** when
    executing this endpoint.

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --header "Accept: application/json" \
     --header "Content-Type: application/json" \
     --include \
     --request PUT "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/automationConfig/monitoringAgentConfig"
     --data '{
         "configOverrides" : {
           "mmsBaseUrl" : "http://new.example.org"
         },
         "logPath": "/var/log/mongodb-mms-automation/monitoring-agent.log",
         "logRotate": {
           "sizeThresholdMB": 1000,
           "timeThresholdHrs": 12
         },
         "username": "mms-automation"
       }'
```

## Response

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

This endpoint returns an empty JSON (Javascript Object Notation) object.
