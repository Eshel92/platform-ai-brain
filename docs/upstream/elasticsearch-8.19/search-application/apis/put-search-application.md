<!-- Converted from search-application/apis/put-search-application.asciidoc (AsciiDoc). Includes are inlined. -->

### Put Search Application

**New API reference**
For the most up-to-date API details, refer to [Search application APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-search_application).

beta::[]

Creates or updates a Search Application.

#### Request

`PUT _application/search_application/<name>`

#### Prerequisites

Requires the `manage_search_application` cluster privilege.
Also requires manage privileges on all indices that are added to the Search Application.

#### Path parameters

`create`::
(Optional, Boolean) If `true`, this request cannot replace or update existing Search Applications.
Defaults to `false`.

`<body>`::
(Required, object)
Contains parameters for a search application:
**Properties of `<body>` objects**
`indices`::
(Required, array of strings)
The indices associated with this search application. All indices need to exist in order to be added to a search application.

`template`::
(Optional, object)
The search template associated with this search application. The search application's template is only stored and accessible through the search application.

- This search template must be a Mustache template.
- The template must contain a Mustache script and script source.
- The template may be modified with subsequent put search application requests.
- If no template is specified when creating a search application, or if a template is removed from a search application, we use the query_string defined in the template examples as a default.
- This template will be used by the search application search API to execute searches.
- The template accepts an optional `dictionary` parameter which defines a [JSON schema](https://json-schema.org) used for validating parameters sent to the search application search API.

**Properties of `<template>`**
=====

`script`::
(Required, object)
The associated mustache template.

`dictionary`::
(Optional, object)
The dictionary used to validate the parameters used with the search application search API. The dictionary must be a valid JSON schema.
If `dictionary` is not specified, then the parameters will not be validated before being applied in the template.
=====

#### Response codes

`404`::
Search Application `<name>` does not exist.

`409`::
Search Application `<name>` exists and `create` is `true`.

#### Examples

The following example creates or updates a new Search Application called `my-app`:

```console
PUT _application/search_application/my-app
{
  "indices": [ "index1", "index2" ],
  "template": {
    "script": {
      "source": {
        "query": {
          "query_string": {
            "query": "{{query_string}}",
            "default_field": "{{default_field}}"
          }
        }
      },
      "params": {
        "query_string": "*",
        "default_field": "*"
      }
    },
    "dictionary": {
      "properties": {
        "query_string": {
          "type": "string"
        },
        "default_field": {
          "type": "string",
          "enum": [
            "title",
            "description"
          ]
        },
        "additionalProperties": false
      },
      "required": [
        "query_string"
      ]
    }
  }
}
```

When the above `dictionary` parameter is specified, the search application search API will perform the following parameter validation:

* It accepts only the `query_string` and `default_field` parameters
* It verifies that `query_string` and `default_field` are both strings
* It accepts `default_field` only if it takes the values `title` or `description`

If the parameters are not valid, the search application search API will return an error.
```console
POST _application/search_application/my-app/_search
{
  "params": {
    "default_field": "author",
    "query_string": "Jane"
  }
}
```

In the above example, the value of the `default_field` parameter is not valid, therefore Elasticsearch will return an error:

```JSON
{
  "error": {
    "root_cause": [
      {
        "type": "validation_exception",
        "reason": 'Validation Failed: 1: $.default_field: does not have a value in the enumeration [title, description];',
        "stack_trace": ...
      }
    ],
    "type": "validation_exception",
    "reason": 'Validation Failed: 1: $.default_field: does not have a value in the enumeration [title, description];',
    "stack_trace": ...
  },
  "status": 400
}
```
