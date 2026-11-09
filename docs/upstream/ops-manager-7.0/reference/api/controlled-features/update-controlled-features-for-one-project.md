<!-- Converted from reference/api/controlled-features/update-controlled-features-for-one-project.txt (reStructuredText). Includes are inlined. -->

# Update Feature Policies for One Project

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Required Roles

This resource requires the `Project Owner`.

## Resource

```http
PUT /groups/{PROJECT-ID}/controlledFeature
```

**Important:**

You must include every policy that you want to include and maintain.
This resource overwrites any existing policy. If you omit a policy
when using this resource, that policy isn't enforced after the
update. That policy has been removed.

### Request Path Parameters

| Name | Type | Necessity | Description |
|---|---|---|---|
| `PROJECT-ID` | string | Required | Unique identifier of the project that has the controlled features. |

### Request Query Parameters

The following query parameters are optional:

* - Name
  - Type
  - Description
  - Default

* - pageNum
  - integer
  - Page number (1-index based).
  - `1`

* - itemsPerPage
  - integer
  - Number of items to return per page, up to a maximum of 500.
  - `100`

* - pretty
  - boolean
  - Indicates whether the response body should be in a
    prettyprint format.
  - `false`

* - envelope
  - boolean
  - Indicates whether or not to wrap the response in an envelope.

    Some API (Application Programming Interface) clients cannot access the HTTP (Hypertext Transfer Protocol) response headers or
    status code. To remediate this, set `"envelope" : true` in the
    query.

    For endpoints that return one result, response body
    includes:

    | status | HTTP (Hypertext Transfer Protocol) response code |
    |---|---|
    | envelope | Expected response body |

    For endpoints that return a list of results, the `results`
    object is an envelope. Ops Manager adds the `status` field to the
    response body.
  - None

### Request Body Parameters

* - Name
  - Type
  - Description

* - `externalManagementSystem`
  - object
  - Identifying parameters for the external system that manages this
    Ops Manager Project.

* - | `externalManagementSystem`
    | `.name`
  - string
  - Identifying label for the external system that manages this
    Ops Manager Project.

* - | `externalManagementSystem`
    | `.systemId`
  - string
  - Unique identifier of the external system that manages this
    Ops Manager Project.

* - | `externalManagementSystem`
    | `.version`
  - string
  - Active release of the external system that manages this Ops Manager
    Project.

* - `policies`
  - array
  - List of policies that the external system applies to this
    Ops Manager Project.

* - | `policies`
    | `.policy[n]`
  - object
  - Single policy set for this Ops Manager Project. This parameter can
    be set one or more times in the `policies` array.

    Accepted values are:

    | Value | Purpose |
    |---|---|
    | `EXTERNALLY_MANAGED_LOCK` | Users can't use Ops Manager to manage other settings given in the `policies.policy[n]` array. These same users may use a configured external system, like the Kubernetes Operator to manage these settings. |
    | `DISABLE_USER_MANAGEMENT` | Users can't manage users or roles. |
    | \| `DISABLE_AUTHENTICATION_` \| `MECHANISMS` | Users can't change authentication settings. |
    | \| `DISABLE_SET_MONGOD_` \| `CONFIG` | Users can't change any `mongod` settings listed in the `policies[n].disabledParams` array. |
    | \| `DISABLE_SET_MONGOD_` \| `VERSION` | Users can't change the version of any `mongod` or `mongos`. |
    | `DISABLE_BACKUP_AGENT` | Users can't enable or disable the Backup agent. |
    | \| `DISABLE_MONGOD_LOG_` \| `MANAGEMENT` | Users can't change log management settings. |
    | \| `DISABLE_IMPORT_TO_` \| `AUTOMATION` | Users can't manage deployments using Automation. |
    | \| `DISABLE_AGENT_API_KEY_` \| `MANAGEMENT` | Users can't create or update Agent API keys. |
    | \| `DISABLE_MONGOD_HOST_` \| `MANAGEMENT` | Users can't change the server type of hosts. |

* - | `policies[n]`
    | `.disabledParams`
  - array
  - List of `mongod` settings to disable when you apply the
    `DISABLE_SET_MONGOD_CONFIG` policy. Automation doesn't support 
    all MongoDB options, which can result in failed import attempts. 
    To learn more, see om-unsupported-mdb-settings.

## Response

* - Name
  - Type
  - Description

* - `_id`
  - string
  - Unique identifier of the Project for which you are setting this
    policy.

* - `created`
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when this feature control policy was created.

* - `updated`
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when this feature control policy was updated.

* - `externalManagementSystem`
  - object
  - Identifying parameters for the external system that manages this
    Ops Manager Project.

* - | `externalManagementSystem`
    | `.name`
  - string
  - Identifying label for the external system that manages this
    Ops Manager Project.

* - | `externalManagementSystem`
    | `.systemId`
  - string
  - Unique identifier of the external system that manages this
    Ops Manager Project.

* - | `externalManagementSystem`
    | `.version`
  - string
  - Active release of the external system that manages this Ops Manager
    Project.

* - `policies`
  - array
  - List of policies that the external system applies to this
    Ops Manager Project.

* - | `policies`
    | `.policy[n]`
  - object
  - Single policy set for this Ops Manager Project. This parameter can
    be set one or more times in the `policies` array.

    Possible values are:

    | Value | Purpose |
    |---|---|
    | `EXTERNALLY_MANAGED_LOCK` | Users can't use Ops Manager to manage other settings given in the `policies.policy[n]` array. These same users may use a configured external system, like the Kubernetes Operator to manage these settings. |
    | `DISABLE_USER_MANAGEMENT` | Users can't manage users or roles. |
    | \| `DISABLE_AUTHENTICATION_` \| `MECHANISMS` | Users can't change authentication settings. |
    | \| `DISABLE_SET_MONGOD_` \| `CONFIG` | Users can't change any `mongod` settings listed in the `policies[n].disabledParams` array. |
    | \| `DISABLE_SET_MONGOD_` \| `VERSION` | Users can't change the version of any `mongod` or `mongos`. |
    | `DISABLE_BACKUP_AGENT` | Users can't enable or disable the Backup agent. |
    | \| `DISABLE_MONGOD_LOG_` \| `MANAGEMENT` | Users can't change log management settings. |
    | \| `DISABLE_IMPORT_TO_` \| `AUTOMATION` | Users can't manage deployments using Automation. |
    | \| `DISABLE_AGENT_API_KEY_` \| `MANAGEMENT` | Users can't create or update Agent API keys. |
    | \| `DISABLE_MONGOD_HOST_` \| `MANAGEMENT` | Users can't change the server type of hosts. |

* - | `policies[n]`
    | `.disabledParams`
  - array
  - List of `mongod` settings to disable if you apply the
    `DISABLE_SET_MONGOD_CONFIG` policy. Automation doesn't support 
    all MongoDB options, which can result in failed import attempts. 
    To learn more, see om-unsupported-mdb-settings.

## Example Request

```sh
curl --user "{USERNAME}:{APIKEY}" --digest \
     --header "Accept: application/json" \
     --header "Content-Type: application/json" \
     --include \
     --request PUT "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/controlledFeature?pretty=true" \
     --data '{
       "externalManagementSystem":
       {
         "name": "Operator",
         "systemId": "6d6c139ae5528707b6e8e3b2",
         "version": "0.2.1"
       },
       "policies": [
         {"policy": "ExternallyManagedLock"},
         {"policy": "DisableUserManagement"},
         {"policy": "DisableAuthenticationMechanisms"},
         {"policy": "DisableSetMongodVersion"},
         {
           "policy": "DisableSetMongodConfig",
           "disabledParams": ["net.tls.CAFile"]
         }
       ]
     }'
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
  "_id": "{PROJECT-ID}",
  "created": "2019-08-29T15:03:24Z",
  "updated": "2019-08-29T15:03:24Z",
  "externalManagementSystem":
  {
    "name": "Operator",
    "systemId": "6d6c139ae5528707b6e8e3b2",
    "version": "0.2.1"
  },
  "policies": [
    {"policy": "ExternallyManagedLock"},
    {"policy": "DisableUserManagement"},
    {"policy": "DisableAuthenticationMechanisms"},
    {"policy": "DisableSetMongodVersion"},
    {
      "policy": "DisableSetMongodConfig",
      "disabledParams": ["net.tls.CAFile"]
    }
  ]
}
```
