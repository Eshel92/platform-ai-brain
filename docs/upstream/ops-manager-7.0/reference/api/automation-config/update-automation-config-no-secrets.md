<!-- Converted from reference/api/automation-config/update-automation-config-no-secrets.txt (reStructuredText). Includes are inlined. -->

# Update the Automation Configuration (Sensitive Information Ignored)

A project's automation configuration determines the goal state of its MongoDB
processes and agents. The MongoDB Agent builds the deployment according
to the goals specified. 

An automation configuration might contain sensitive information, such as
passwords and key values. This resource allows you to update a project's
automation configuration without updating any fields that contain
sensitive information.

`PUT` requests to the
`/groups/{PROJECT-ID}/automationConfig/noSecrets` endpoint ignore any
fields in the automation configuration in your request body that contain
sensitive information, leaving their current values unchanged and
updating all other fields. To update the full automation configuration,
including any sensitive information, use the
/groups/{PROJECT-ID}/automationConfig endpoint.

To update the configuration:

1. Retrieve the current configuration. 

   You can use the /groups/{PROJECT-ID}/automationConfig endpoint to get the full configuration, or use the
   /groups/{PROJECT-ID}/automationConfig/noSecrets endpoint to get the configuration with
   sensitive information redacted, such as passwords or key values.
#. Make changes to a copy of the current configuration, changing only
   those items you want modified.
#. Replace the entire configuration using `PUT`, with the updated
   configuration in the request body. You must use `PUT`. **Do not**
   use `PATCH`.

   When you submit updates, Ops Manager makes internal modifications to the
   data and then saves your new configuration version.

**Note:**

Some parameters cannot be updated through the `automationConfig`
endpoint. To learn more, see:

- update-monitoring-backup-versions
- update-backup-logs
- update-monitoring-logs

To make updates to the MongoDB Agent *other than* `hostname`, you
must do so through a different endpoint.

To see a tutorial on how to update an automation configuration, see
update-automation-configuration-tutorial.

The MongoDB Agents continuously poll Ops Manager for changes to the
configuration and fetch configuration updates when they occur. The
Agents then adjust the states of their live processes to match.

**Warning:**

Making changes to the automation configuration using a `PUT`
request can cause cluster downtime. Test your changes in lower
environments before you apply them to production environments.

   

**Warning:**

There is **no protection** in the Ops Manager Administration API to prevent
concurrent modifications. If two administrators both start with a
configuration based on the current version, make their own
modifications, and then submit their modifications, the later
modification wins.

**Warning:** Update Agent Username before Enabling Authentication

The automation configuration provides the sole means to enabling
authentication on your clusters using the API (Application Programming Interface). To enable
authentication, first call the following endpoints with
**"username": "mms-automation"**:

- Update the current backup log settings
- Update the current monitoring log settings

## Required Roles

This resource requires the `Project Automation Admin` role.

## Resource

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

```http
PUT /groups/{PROJECT-ID}/automationConfig/noSecrets
```

## Request

### Path Parameters

| Name | Type | Necessity | Description |
|---|---|---|---|
| PROJECT-ID | string | Required | Unique identifier of the `group` that owns the automation configuration. |

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

To review these parameters, see
/reference/api/automation-config/automation-config-parameters.

## Response

To review these parameters, see
/reference/api/automation-config/automation-config-parameters.

## Example Request

The following replaces the automation configuration with the updated
configuration saved in `/Users/admin/updated-conf.json`. For an
example of an updated configuration document, see
example-updated-configuration.

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --header "Accept: application/json" \
     --header "Content-Type: application/json" \
     --include \
     --request PUT "https://cloud.mongodb.com/api/public/v1.0/groups/{PROJECT-ID}/automationConfig/noSecrets?pretty=true" \
     --data-binary "@/Users/admin/updated-conf.json"
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

To review an example of this configuration, see
/reference/api/automation-config/automation-config-example.
