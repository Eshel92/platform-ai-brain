<!-- Converted from synonyms/apis/put-synonyms-set.asciidoc (AsciiDoc). Includes are inlined. -->

### Create or update synonyms set

**New API reference**
For the most up-to-date API details, refer to [Synonyms APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-synonyms).

Creates or updates a synonyms set.

**Note:** Synonyms sets are limited to a maximum of 10,000 synonym rules per set.
If you need to manage more synonym rules, you can create multiple synonyms sets.

#### Request

`PUT _synonyms/<synonyms_set>`

#### Prerequisites

Requires the `manage_search_synonyms` cluster privilege.

#### Path parameters

`<synonyms_set>`::
(Required, string)
Synonyms set identifier to create.
This identifier will be used by other synonyms-apis to manage the synonyms set.

#### Request body

`synonyms_set`::
(Required, array of synonym rules objects)
The synonym rules definitions for the synonyms set.

**Properties of `synonyms_set` objects**
=====

`id`::
(Optional, string)
The identifier associated to the synonym rule, that can be used to manage individual synonym rules via synonym rules APIs.
In case a synonym rule id is not specified, an identifier will be created automatically by Elasticsearch.

`synonyms`::
(Required, string)
The synonym rule. This needs to be in Solr format. Some examples are:
* "i-pod, i pod => ipod",
* "universe, cosmos"

=====

#### Examples

The following example creates a new synonyms set called `my-synonyms-set`:

```console
PUT _synonyms/my-synonyms-set
{
  "synonyms_set": [
    {
      "id": "test-1",
      "synonyms": "hello, hi"
    },
    {
      "synonyms": "bye, goodbye"
    },
    {
      "id": "test-2",
      "synonyms": "test => check"
    }
  ]
}
```

If any of the synonym rules included is not valid, the API will return an error.

```console
PUT _synonyms/my-synonyms-set
{
  "synonyms_set": [
    {
      "synonyms": "hello => hi => howdy"
    }
  ]
}
```

```console-result
{
  "error": {
    "root_cause": [
      {
        "type": "action_request_validation_exception",
        "reason": "Validation Failed: 1: More than one explicit mapping specified in the same synonyms rule: [hello => hi => howdy];",
        "stack_trace": ...
      }
    ],
    "type": "action_request_validation_exception",
    "reason": "Validation Failed: 1: More than one explicit mapping specified in the same synonyms rule: [hello => hi => howdy];",
    "stack_trace": ...
  },
  "status": 400
}
```

#### Analyzer reloading

When an existing synonyms set is updated, the search analyzers that use the synonyms set are reloaded automatically for all indices.
This would be equivalent to invoking indices-reload-analyzers for all indices that use the synonyms set.

For example, creating an index with a synonyms set and updating it:

```console
PUT _synonyms/my-synonyms-set
{
    "synonyms_set": [
        {
            "id": "test-1",
            "synonyms": "hello, hi"
        }
    ]
}

PUT /test-index
{
  "settings": {
    "analysis": {
      "filter": {
        "synonyms_filter": {
          "type": "synonym_graph",
          "synonyms_set": "my-synonyms-set",
          "updateable": true
        }
      },
      "analyzer": {
        "my_index_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": ["lowercase"]
        },
        "my_search_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": ["lowercase", "synonyms_filter"]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "title": {
        "type": "text",
        "analyzer": "my_index_analyzer",
        "search_analyzer": "my_search_analyzer"
      }
    }
  }
}

PUT _synonyms/my-synonyms-set
{
    "synonyms_set": [
        {
            "id": "test-1",
            "synonyms": "hello, hi, howdy"
        }
    ]
}
```

The reloading result is included as part of the response:

```console-result
{
  "result": "updated",
  "reload_analyzers_details": {
    "_shards": {
      "total": 2,
      "successful": 1,
      "failed": 0
    },
    "reload_details": [
      {
        "index": "test-index",
        "reloaded_analyzers": [
          "my_search_analyzer"
        ],
        "reloaded_node_ids": [
          "1wYFZzq8Sxeu_Jvt9mlbkg"
        ]
      }
    ]
  }
}
```
