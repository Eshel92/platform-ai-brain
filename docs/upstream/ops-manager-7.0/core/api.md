<!-- Converted from core/api.txt (reStructuredText). Includes are inlined. -->

# Public API (Application Programming Interface) Principles

The Ops Manager Public API (Application Programming Interface) follows the REST (Representational State Transfer) architecture principles to
expose internal resources that provide programmatic access to Ops Manager's
features.

The API (Application Programming Interface) has the following features:

JSON (Javascript Object Notation) entities
  All entities are expressed in JSON (Javascript Object Notation).

Key-based access
  Each Ops Manager user or application needing to connect to Ops Manager
  must
  generate an API key
  before accessing the Ops Manager API (Application Programming Interface).

Digest authentication
  To ensure that your `public API key` is never sent over the
  network, API (Application Programming Interface) requests are authenticated using
  HTTP Digest Authentication.

Browsable interface
  Using a consistent linking mechanism, you can browse the entire API
  by starting at the root resource and following links to related
  resources.

User Access Control
  Each Ops Manager user's API (Application Programming Interface) capabilities match the permissions that
  their /reference/user-roles grant.

  **Example:**

  A user with the `Project Read Only` role cannot modify
  any resource within that project whether through the Ops Manager UI or
  the API (Application Programming Interface).

API (Application Programming Interface) Network Access List
  The Ops Manager API (Application Programming Interface) can secure access to the Ops Manager Administration API through an
  API Access List. This list
  restricts access to the API (Application Programming Interface) to specific IP (Internet Protocol) or CIDR (Classless Inter-Domain Routing)
  addresses. Each API (Application Programming Interface) key has its own Ops Manager Administration API access list. When
  you create a new organization using the Ops Manager UI, the MongoDB Atlas
  enables the API (Application Programming Interface) access list requirement by default.

  To learn more, see access-list-for-api-operations.

## HTTP (Hypertext Transfer Protocol) Methods

All resources support a subset of these common HTTP (Hypertext Transfer Protocol) Methods:

| Method | Purpose |
|---|---|
| `GET` | Retrieve the JSON (Javascript Object Notation) representation of a resource. |
| `POST` | Create a new resource using the provided JSON (Javascript Object Notation) representation. |
| `PUT` | Replace a resource with the provided JSON (Javascript Object Notation) representation. |
| `PATCH` | Update the specified fields in a resource using the provided JSON (Javascript Object Notation) representation. |
| `DELETE` | Remove a resource. |
| `HEAD` | Retrieve the response header without the JSON (Javascript Object Notation) representation of the resource. |

## JSON (Javascript Object Notation)

All entities are represented in JSON (Javascript Object Notation). The following rules for
requests and conventions of responses apply:

### Request Rules

Apply the Correct Content Type Header
  When sending JSON (Javascript Object Notation) to the server via `POST` or `PUT`, make sure
  to specify the correct content type request header:
  `Content-Type: application/json`

Set Dates as ISO 8601 Strings
  When sending dates to the server (as query parameters or fields in
  `POST` or `PATCH` request entities), use dates formatted
  according to the ISO 8601 standard. If you don't specify a time
  zone, Ops Manager assumes UTC (Coordinated Universal Time). Include a time zone designator to avoid
  any ambiguity.

  **Example:**

  - September 27, 2018 is expressed as `2018-09-27`.

  - September 27, 2018 at 4:00 PM EDT is expressed (with time zone)
    as `2018-09-27T16:00-04:00`.

  In some cases, a timestamp is returned as a JSON (Javascript Object Notation) representation of
  a BSON timestamp, most notably in the backup resources. This
  representation of a BSON (Binary Javascript Object Notation) timestamp provides a JSON (Javascript Object Notation) document as
  an object with two fields:

  | Field | Definition |
  |---|---|
  | `date` | Seconds since the UNIX Epoch |
  | `increment` | An incrementing 32-bit integer ordinal for operations within a given second. |

  **Example:**

  The third operation at September 27, 2018 at 4:00 PM EDT is expressed (with time zone) as

  ```json
  { date: 2018-09-27T16:00-04:00, increment: 3 }
  ```

### Response Conventions

Rejects Invalid Fields
  Invalid fields are *rejected* rather than *ignored*.

  **Example:**

  You attempt to create a new entity and misspell one of the
  fields, or if you attempt to update an existing entity and
  include a field that cannot be modified, the Ops Manager responds with
  an HTTP (Hypertext Transfer Protocol) 400 status code and an error message stating which
  field was invalid.

Returns Dates as ISO 8601 Strings
  All dates are returned as ISO 8601\-formatted strings designated
  in UTC (Coordinated Universal Time).

Labels Field to Disambiguate Units
  Fields that contain numeric values in a particular unit are named so
  as to disambiguate the unit being used.

  **Example:**

  A host's uptime is returned in millseconds, so the name of the
  host entity field is `uptimeMsec`.

Returns Default Values for Fields without Other Values
  Fields that do not have a current value are returned with an
  appropriate default value.

  **Example:**

  Ops Manager does not have any statistics for a newly discovered host,
  so any statistics-related fields have a value of zero.

  Fields that do not have a sensible default value are omitted from
  the entity.

  **Example:**

  A host that is not using authentication omits the `username`
  field from the returned entity.

Returns Fields in Alphabetical Order
  The fields in the JSON (Javascript Object Notation) documents that the Ops Manager Application returns are
  in alphabetical order. The order could change. Do not depend on the
  order of the fields.

## Linking

Each resource includes one or more links to sub-resources and/or related resources.

**Example:**

A host has a link to the project it belongs to, the replica set it
belongs to, and so on.

Links are placed in the `links` field of an entity, which is an
array of link relation objects. Each link relation has two fields:

| Field | Definition |
|---|---|
| `rel` | Name (or type) of the relation. Many of these are considered Extension Relation Types and are prefixed by `http://mms.mongodb.com`. |
| `href` | Target URL (Uniform Resource Locator). |

All entities include at least one link relation called `self`, which
is simply its own URL (Uniform Resource Locator). When an entity is part of a list (i.e., when
requesting all hosts in a project), then it only includes the `self`
link relation.

**Example:**

This is a portion of a `host` resource with a few links:

```json
{
  "rel": "http://mms.mongodb.com/project",
  "href": "https://cloud.mongodb.com/api/public/v1.0/projects/xxx"
  "id": "xxx",
  "projectId": "yyy",
  "hostname": "mongodb.example.com",
  "port": 27017,
  "links": [
    {
      "rel": "self",
      "href": "https://<ops-manager-host>/api/public/v1.0/projects/xxx/hosts/yyy"
    },
    {
      "rel": "http://mms.mongodb.com/project",
      "href": "https://<ops-manager-host>/api/public/v1.0/projects/xxx"
    }
  ]
}
```

To learn more, see the [Web Linking Specification](http://tools.ietf.org/html/rfc5988).

**Note:**

Although the
[Web Linking Specification](http://tools.ietf.org/html/rfc5988)
describes a format for including links in the HTTP (Hypertext Transfer Protocol) response
headers, it is not required. To make the API (Application Programming Interface) easily browsable, it
includes the links in the response body rather than in the response
headers.

## Lists

Some resources return a list of entities.

**Example:**

You can request a list of all **hosts** in a **project**.

When a list of entities is expected in a response, the results are
returned in batches bounded by two query parameters:

| Field | Definition |
|---|---|
| `pageNum` | Page number (1-based). Defaults to 1 if not specified. |
| `itemsPerPage` | Number of items to return per page, up to a maximum of 500. Defaults to 100 if not specified. |

The response entity contains three fields:

* - Field
  - Definition

* - `totalCount`
  - Total number of items in the entire result set.

    For example, if a project has a total of 57 hosts, and you make a request
    with `pageNum=6` and `itemsPerPage=10`, then
    `totalCount` is **57**.

* - `results`
  - Result set, which is an array of entity documents.

* - `links`
  - Contains one to three link relations:

    - `previous` for the previous page of results
      (omitted for the first page);
    - `next` for the next page of results
      (omitted for the last page);
    - `self` for the current page (always present).

If you make a request for a list of entities and there are no results,
then the API (Application Programming Interface) responds with an HTTP (Hypertext Transfer Protocol) 200 status code and an empty
`results` array. It does *not* respond with a 404 in this case,
since the list of entities may not be empty at some point in the
future.

If you had requested a list of entities in a context that does not
exist (i.e., the list of hosts for a non-existent project), then this
results in a an HTTP (Hypertext Transfer Protocol) 404 response status.

**Example:**

This is an HTTP (Hypertext Transfer Protocol) response for the second page of 10 hosts in a
project with a total of 57 hosts:

```json
{

  "totalCount": 57,
  "results": [
    {
      "id": "yyy",
      "projectId": "xxx",
      // additional host properties...
    },
    // additional host documents...
  ],
  "links": [
    {
      "rel" : "self",
      "href" : "https://www.mongodb.com/api/public/v1.0/projects/xxx/hosts?pageNum=2&itemsPerPage=10"
    },
    {
      "rel": "previous",
      "href": "https://www.mongodb.com/api/public/v1.0/projects/xxx/hosts?itemsPerPage=10&pageNum=1"
    },
    {
      "rel": "next",
      "href": "https://www.mongodb.com/api/public/v1.0/projects/xxx/hosts?itemsPerPage=10&pageNum=3"
    }
  ]
}
```

## Envelopes

Some clients may not be able to access the HTTP (Hypertext Transfer Protocol) response headers
and/or status code. In that case, you can request that the response
include an `envelope`, which is simply an extra layer of information
in the JSON (Javascript Object Notation) document that contains any relevant details that would
normally be in the response headers.

By default, the API (Application Programming Interface) does *not* include the response in an envelope.
To request one, simply add the query parameter `envelope=true`.

For responses that contain a single entity, the envelope contains two
fields:

| Field | Definition |
|---|---|
| `status` | HTTP (Hypertext Transfer Protocol) status code. |
| `content` | Requested entity. |

For responses that contain a list of entities, there is already an
envelope that wraps the results, so specifying `envelope=true` as a
query parameter in this case only adds the `status` field to the
existing envelope.

## Pretty Printing

By default, extraneous whitespace is stripped from the JSON (Javascript Object Notation) that
Ops Manager returns. To ask for pretty-printed JSON (Javascript Object Notation), simply append the
`pretty=true` query parameter to any request:

```shell
curl --user '{USERNAME}:{APIKEY}' --digest \
--header 'Accept: application/json' \
--include \
--request GET "{opsManagerHost}:{Port}/api/public/v1.0?pretty=true"
```

**Note:**

All the examples in this document show pretty-printed JSON (Javascript Object Notation) for
clarity, although some example URL (Uniform Resource Locator)\s *may not contain this
additional query parameter*.

## Response Codes

Responses utilize the standard HTTP (Hypertext Transfer Protocol) response codes, including:

| Code | Meaning | Notes |
|---|---|---|
| 200 | OK | The request was successful. This is the typical response to a successful `GET` request. |
| 201 | Created | A new resource was created. This is the typical response to a successful `POST` request. |
| 202 | Accepted | A request for an asynchronous operation was accepted. |
| 400 | Bad Request | Something was wrong with the client request. |
| 401 | Unauthorized | Authentication is required but was not present in the request. Typically this means that the digest authentication information was omitted from the request, the provided credentials are incorrect, or the user associated with the given API (Application Programming Interface) key is not allowed to access the requested resource. |
| 403 | Forbidden | Access to the specified resource is not permitted. |
| 404 | Not Found | The requested resource does not exist. |
| 405 | Method Not Allowed | The HTTP (Hypertext Transfer Protocol) method is not supported for the specified resource. Keep in mind that each resource may only support a subset of HTTP (Hypertext Transfer Protocol) methods. For example, you are not allowed to `DELETE` the root resource. |
| 409 | Conflict | This is typically the response to a request to create or modify a property of an entity that is unique when an existing entity already exists with the same value for that property. For example, if you attempt to create a project with the same name as an existing project, the request fails. |
| 5xx | Various server errors | Something unexpected went wrong. Try again later and consider notifying Ops Manager Support. |

## Errors

When a request results in an error, the response body contains a JSON (Javascript Object Notation)
document with additional details about what went wrong. The document
contains five fields:

| Field | Data Type | Definition |
|---|---|---|
| `detail` | string | Human-readable description of the API (Application Programming Interface) request error. |
| `error` | integer | HTTP (Hypertext Transfer Protocol) status code. |
| `errorCode` | string | Named constant representing the API (Application Programming Interface) request error as shown in api-error-codes. |
| `parameters` | array of strings | List of parameters that provide further details about the error. |
| `reason` | string | HTTP (Hypertext Transfer Protocol) status code definition. |

**Example:**

Ops Manager returns this response body for an incorrectly formatted
request:

```json
{
  "detail" : "Cannot find resource /api/public/v1.0/softwareComponents/version.",
  "error" : 404,
  "errorCode" : "RESOURCE_NOT_FOUND",
  "parameters" : [ "/api/public/v1.0/softwareComponents/version" ],
  "reason" : "Not Found"
}
```

To review the list of codes, see /reference/api-error-codes.

## Authentication

As previously mentioned, the Ops Manager API (Application Programming Interface) uses HTTP (Hypertext Transfer Protocol) Digest
Authentication. The details of digest authentication are beyond the
scope of this document, but it essentially requires a username and a
password which are hashed using a unique server-generated value called
a **nonce**. The username is the username of a registered Ops Manager
account, and the password is a `public API key` associated
with that account.

Keep the following points in mind:

- The server-generated nonce is used by the client to hash the
  username and password before sending them back to the server to
  authenticate a request. The nonce is only valid for a short amount
  of time as per the digest authentication specification. This is to
  prevent replay attacks, so you cannot cache a nonce and use it
  forever.

- Some resource methods require even more security and are additionally
  protected by access lists
  that allow access to the resource only from the IP (Internet Protocol) addresses
  listed. Each user configures their own access list of IP (Internet Protocol)
  addresses that allow access to the resource.

- The Ops Manager Application has a concept of **roles**, which allow more
  fine-grained control of the operations a user is allowed to perform.
  The API (Application Programming Interface) resources also enforce the same authorization rules, so
  the resources and methods that can be accessed by an API (Application Programming Interface) key are
  governed by the roles granted to the associated user.

  **Example:**

  To `DELETE` a host, the user that owns the API (Application Programming Interface) key used to
  make the request must be a `Project Monitoring Admin`
  or `Project Owner` in the project to which the host
  belongs.

- Many resources are tied to a project (former known as a *group*),
  as evidenced by URL (Uniform Resource Locator)\s of the following form:

  ```shell
  /api/public/v1.0/groups/{PROJECT-ID}/
  ```

  For these resources, the user tied to the API (Application Programming Interface) key must be a
  member of the project *or* must be assigned to one of the
  `GLOBAL` roles. Otherwise Ops Manager Application responds with an HTTP (Hypertext Transfer Protocol)
  401 error.

## Automation

The /reference/api/automation-config and
/reference/api/automation-status resources provide endpoints
that let you modify a project's deployment and retrieve deployment
status. You can modify a deployment by sending a new
automation configuration to
Ops Manager. The automation configuration is where you describe and
configure the MongoDB processes to be deployed. Ops Manager refers to this
as the deployment's "goal state." When you submit a new automation
configuration through the API (Application Programming Interface), the Automations adjust the
current state of the system to match the goal state.

**Important:**

There is no protection in the API (Application Programming Interface) to prevent concurrent
modifications. If two administrators both start with a
configuration based on the current version, make their own
modifications, and then submit their modifications, the later
modification wins.

## Additional Information

See /reference/api for a complete reference
of all resources available in the Ops Manager Public API (Application Programming Interface).
