<!-- Converted from reference/api/organizations/organization-rename.txt (reStructuredText). Includes are inlined. -->

# Update One Organization

Use this endpoint to make any of the following changes to one
organization:

- Change one organization's name.
- Map LDAP (Lightweight Directory Access Protocol) groups to Ops Manager roles for one organization.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```none
PATCH /orgs/{ORG-ID}
```

### Request Path Parameters

| Name | Type | Description |
|---|---|---|
| `ORG-ID` | string | The unique identifier of the organization. |

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

You must include at least one of the following fields in the request
body:

| Name | Type | Necessity | Description |
|---|---|---|---|
| name | string | Optional | The new name for the organization. |
| ldapGroupMappings | object array | Optional | For LDAP-backed Ops Manager, the mappings of LDAP groups to Ops Manager organization roles. Only accepted for LDAP-backed Ops Manager. |

## Response

* - Name
  - Type
  - Description

* - `id`
  - ObjectId
  - Unique identifier for the organization.
* - `links`
  - document array
  - One or more links to sub-resources and/or related resources. The
    relations between URLs are explained in the [Web Linking Specification](https://tools.ietf.org/html/rfc5988).

* - `name`
  - string
  - New name of the organization.

* - ldapGroupMappings
  - object array
  - For LDAP-backed Ops Manager, the mappings of
    LDAP groups
    to Ops Manager organization roles. Only present for LDAP-backed
    Ops Manager.

* - | ldapGroupMappings
    | .roleName
  - string
  - Ops Manager organization role. Possible values include:

    - `ORG_OWNER`
    - `ORG_MEMBER`
    - `ORG_GROUP_CREATOR`
    - `ORG_READ_ONLY`

* - | ldapGroupMappings
    | .ldapGroups
  - string array
  - LDAP group(s) that map to the Ops Manager role.

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
 --header "Accept: application/json" \
 --header "Content-Type: application/json" \
 --include \
 --request PATCH "https://{opsManagerHost}:{port}/api/public/v1.0/orgs/{ORG-ID}?pretty=true" \
 --data '
 {
   "ldapGroupMappings": [{
     "roleName": "ORG_OWNER",
     "ldapGroups": ["org-owner"]
   }]
 },
```

	       "name": "Organization Name 1"
    }'

## Example Response

```json
{
  "id": "{ORG-ID}",
  "links": [{
      "href": "http://{opsManagerHost}:{port}/api/public/v1.0/orgs/{ORG-ID}",
      "rel": "self"
    },
    {
      "href": "http://{opsManagerHost}:{port}/api/public/v1.0/orgs/{ORG-ID}/groups",
      "rel": "http://mms.mongodb.com/groups"
    },
    {
      "href": "http://{opsManagerHost}:{port}/api/public/v1.0/orgs/{ORG-ID}/teams",
      "rel": "http://mms.mongodb.com/teams"
    },
    {
      "href": "http://{opsManagerHost}:{port}/api/public/v1.0/orgs/{ORG-ID}/users",
      "rel": "http://mms.mongodb.com/users"
    }
  ],
  "name": "Organization Name 1",
  "ldapGroupMappings": [{
    "roleName": "ORG_OWNER",
    "ldapGroups": ["org-owner"]
  }]
}
```
