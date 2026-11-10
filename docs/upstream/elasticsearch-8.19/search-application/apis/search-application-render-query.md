<!-- Converted from search-application/apis/search-application-render-query.asciidoc (AsciiDoc). Includes are inlined. -->

### Render Search Application Query

**New API reference**
For the most up-to-date API details, refer to [Search application APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-search_application).

preview::[]

Given specified query parameters, generates an Elasticsearch query using the search template associated with the search
application or a default template if none is specified.
Unspecified template parameters will be assigned their default values (if applicable).
Returns the specific Elasticsearch query that would be generated and executed by calling
search application search.

#### Request

`POST _application/search_application/<name>/_render_query`

#### Prerequisites

Requires read privileges on the backing alias of the search application.

#### Request body

`params`::
(Optional, map of strings to objects)
Query parameters used to generate the Elasticsearch query from the search template associated with the search application.
If a parameter used in the search template is not specified in `params`, the parameter's default value will be used.

**Note:**
The search application can be configured to validate search template parameters.
See the `dictionary` parameter in the put search application API for more
information.

#### Response codes

`400`::
Invalid parameter passed to search template.
Examples include:

- Missing required parameter
- Invalid parameter data type
- Invalid parameter value

`404`::
Search Application `<name>` does not exist.

#### Examples

The following example generates a query for a search application called `my-app` that uses the search template from
the text search example:

```console
POST _application/search_application/my-app/_render_query
{
  "params": {
    "query_string": "my first query",
    "text_fields": [
      {"name": "title", "boost": 5},
      {"name": "description", "boost": 1}
    ]
  }
}
```

A sample response:

```console-result
{
  "from": 0,
  "size": 10,
  "query": {
    "multi_match": {
      "query": "my first query",
      "fields": [
        "description^1.0",
        "title^5.0"
      ]
    }
  },
  "explain": false
}
```

In this case, the `from`, `size`, and `explain` parameters are not specified in the request, so the default values
specified in the search template are used.
