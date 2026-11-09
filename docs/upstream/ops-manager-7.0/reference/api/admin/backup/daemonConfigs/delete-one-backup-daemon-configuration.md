<!-- Converted from reference/api/admin/backup/daemonConfigs/delete-one-backup-daemon-configuration.txt (reStructuredText). Includes are inlined. -->

# Delete One Backup Daemon Configuration

Deletes the configuration of one backup daemon.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup`

## Resource

```http
DELETE /daemon/configs/{MACHINE}/{HEAD-ROOT-DIRECTORY}
```

### Request Path Parameters

| Name | Type | Necessity | Description |
|---|---|---|---|
| MACHINE | string | Required | Hostname or IP address of the machine that serves the Backup Daemon. |
| HEAD-ROOT-DIRECTORY | string | Optional | Root-relative [URL-encoded path](https://en.wikipedia.org/wiki/Percent-encoding?oldid=810929127) of the head directory on this `Backup Daemon` host. May be omitted if the Backup Daemon has not been configured. |

### Request Query Parameters

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

### Request Body Parameters

This endpoint doesn't use HTTP request body parameters.

## Response

This endpoint does not have response elements.

## Example Request

```sh
curl --user '{PUBLIC-KEY}:{PRIVATE-KEY}' --digest \ 
 --include \ 
 --request DELETE 'https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup/daemon/configs/{HOST}/{HEAD-ROOT-DIRECTORY}' 
```

## Example Response

This endpoint doesn't return a response body.
