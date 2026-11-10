<!-- Converted from scripting/apis/create-stored-script-api.asciidoc (AsciiDoc). Includes are inlined. -->

### Create or update stored script API

**New API reference**
For the most up-to-date API details, refer to [Script APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-script).

Creates or updates a stored script or
search template.

```console
PUT _scripts/my-stored-script
{
  "script": {
    "lang": "painless",
    "source": "Math.log(_score * 2) + params['my_modifier']"
  }
}
```

#### Request

`PUT _scripts/<script-id>`

`POST _scripts/<script-id>`

`PUT _scripts/<script-id>/<context>`

`POST _scripts/<script-id>/<context>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
cluster privilege to use this API.

#### Path parameters

`<script-id>`::
(Required, string)
Identifier for the stored script or search template. Must be unique within the
cluster.

`<context>`::
(Optional, string)
Context in which the script or search template should run. To prevent errors,
the API immediately compiles the script or template in this context.

#### Query parameters

`context`::
(Optional, string)
Context in which the script or search template should run. To prevent errors,
the API immediately compiles the script or template in this context.
If you specify both this and the `<context>` request path parameter, the API
uses the request path parameter.

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

`timeout`::
(Optional, time units) Period to wait for a response from all relevant nodes in the cluster after updating the cluster metadata.
If no response is received before the timeout expires, the cluster metadata update still applies but the response will indicate that it was not completely acknowledged.
Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

#### Request body

`script`::
(Required, object)
Contains the script or search template, its parameters, and its language.
**Properties of `script`**
`lang`::
(Required, string)
Script language. For search templates, use
`mustache`.

`source`::
(Required, string or object)
For scripts, a string containing the script.
For search templates, an object containing the search template. The object
supports the same parameters as the search API's request body.
Also supports [Mustache](https://mustache.github.io/) variables. See
search-template.

`params`::
(Optional, object)
Parameters for the script or search template.
