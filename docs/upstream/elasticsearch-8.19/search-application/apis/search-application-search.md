<!-- Converted from search-application/apis/search-application-search.asciidoc (AsciiDoc). Includes are inlined. -->

### Search Application Search

**New API reference**
For the most up-to-date API details, refer to [Search application APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-search_application).

beta::[]

Given specified query parameters, generates and executes an Elasticsearch query using the search template associated
with the search application or a default template if none is specified.
Unspecified template parameters will be assigned their default values (if applicable).

#### Request

`POST _application/search_application/<name>/_search`

#### Prerequisites

Requires read privileges on the backing alias of the search application.

#### Path parameters

`typed_keys`::
(Optional, Boolean) If `true`, aggregation and suggester names are prefixed
by their respective types in the response. Defaults to `false`.

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

The following example executes a search against a search application called `my-app` that uses the search template from
the text search example:

```console
POST _application/search_application/my-app/_search
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

The generated Elasticsearch query would look like:

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

The expected response is the search results from the Elasticsearch query that was generated & executed.
The response format is the same as that used by the Elasticsearch Search API:

```console-result
{
  "took": 5,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 1,
      "relation": "eq"
    },
    "max_score": 0.8630463,
    "hits": ...
  }
}
```
