<!-- Converted from search/render-search-template-api.asciidoc (AsciiDoc). Includes are inlined. -->

### Render search template API

**New API reference**
For the most up-to-date API details, refer to [Search APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-search).

Renders a <<search-template,search
template>> as a search request body.

```console
POST _render/template
{
  "id": "my-search-template",
  "params": {
    "query_string": "hello world",
    "from": 20,
    "size": 10
  }
}
```

#### Request

`GET _render/template`

`GET _render/template/<template-id>`

`POST _render/template`

`POST _render/template/<template-id>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `read`
index privilege for at least one index pattern.

#### Path parameters

`<template-id>`::
(Required*, string) ID of the search template to render. If no `source` is
specified, this or the `id` request body parameter is required.

#### Request body

`id`::
(Required*, string) ID of the search template to render. If no `source` is
specified, this or the `<template-id>` request path parameter is required. If
you specify both this parameter and the `<template-id>` parameter, the API uses
only `<template-id>`.

`params`::
(Optional, object) Key-value pairs used to replace Mustache variables in the
template. The key is the variable name. The value is the variable value.

`source`::
(Required*, object) An inline search template. Supports the same parameters as
the search API's request body. These parameters also support
[Mustache](https://mustache.github.io/) variables. If no `id` or `<templated-id>`
is specified, this parameter is required.
