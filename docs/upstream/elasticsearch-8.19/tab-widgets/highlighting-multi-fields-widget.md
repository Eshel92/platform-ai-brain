<!-- Converted from tab-widgets/highlighting-multi-fields-widget.asciidoc (AsciiDoc). Includes are inlined. -->

In the following examples, `comment` is analyzed by the `standard`
analyzer and `comment.english` is analyzed by the `english` analyzer.

```console
PUT index1
{
  "mappings": {
    "properties": {
      "comment": {
        "type": "text",
        "analyzer": "standard",
        "fields": {
          "english": {
            "type": "text",
            "analyzer": "english"
          }
        }
      }
    }
  }
}
```

```console
PUT index1/_bulk?refresh=true
{"index": {"_id": "doc1" }}
{"comment": "run with scissors"}
{ "index" : {"_id": "doc2"} }
{"comment": "running with scissors"}

```

```console
GET index1/_search
{
  "query": {
    "query_string": {
      "query": "running with scissors",
      "fields": ["comment", "comment.english"]
    }
  },
  "highlight": {
    "order": "score",
    "fields": {
      "comment": {}
    }
  }
}
```

The above request matches both "run with scissors" and "running with scissors"
and would highlight "running" and "scissors" but not "run". If both
phrases appear in a large document then "running with scissors" is
sorted above "run with scissors" in the fragments list because there
are more matches in that fragment.

```console-result
{
  ...
  "hits" : {
    "total" : {
      "value" : 2,
      "relation" : "eq"
    },
    "max_score": 1.0577903,
    "hits" : [
      {
        "_index" : "index1",
        "_id" : "doc2",
        "_score" : 1.0577903,
        "_source" : {
          "comment" : "running with scissors"
        },
        "highlight" : {
          "comment" : [
            "<em>running</em> <em>with</em> <em>scissors</em>"
          ]
        }
      },
      {
        "_index" : "index1",
        "_id" : "doc1",
        "_score" : 0.36464313,
        "_source" : {
          "comment" : "run with scissors"
        },
        "highlight" : {
          "comment" : [
            "run <em>with</em> <em>scissors</em>"
          ]
        }
      }
    ]
  }
}
```

The below request highlights "run" as well as "running" and "scissors",
because the `matched_fields` parameter instructs that for highlighting
we need to combine matches from the `comment.english` field with
the matches from the original `comment` field.

```console
GET index1/_search
{
  "query": {
    "query_string": {
      "query": "running with scissors",
      "fields": ["comment", "comment.english"]
    }
  },
  "highlight": {
    "order": "score",
    "fields": {
      "comment": {
        "matched_fields": ["comment.english"]
      }
    }
  }
}
```

```console-result
{
  ...
  "hits" : {
    "total" : {
      "value" : 2,
      "relation" : "eq"
    },
    "max_score": 1.0577903,
    "hits" : [
      {
        "_index" : "index1",
        "_id" : "doc2",
        "_score" : 1.0577903,
        "_source" : {
          "comment" : "running with scissors"
        },
        "highlight" : {
          "comment" : [
            "<em>running</em> <em>with</em> <em>scissors</em>"
          ]
        }
      },
      {
        "_index" : "index1",
        "_id" : "doc1",
        "_score" : 0.36464313,
        "_source" : {
          "comment" : "run with scissors"
        },
        "highlight" : {
          "comment" : [
            "<em>run</em> <em>with</em> <em>scissors</em>"
          ]
        }
      }
    ]
  }
}
```

In the following examples, `comment` is analyzed by the `standard`
analyzer and `comment.english` is analyzed by the `english` analyzer.

```console
PUT index2
{
  "mappings": {
    "properties": {
      "comment": {
        "type": "text",
        "analyzer": "standard",
        "term_vector": "with_positions_offsets",
        "fields": {
          "english": {
            "type": "text",
            "analyzer": "english",
            "term_vector": "with_positions_offsets"
          }
        }
      }
    }
  }
}
```

```console
PUT index2/_bulk?refresh=true
{"index": {"_id": "doc1" }}
{"comment": "run with scissors"}
{ "index" : {"_id": "doc2"} }
{"comment": "running with scissors"}

```

```console
GET index2/_search
{
  "query": {
    "query_string": {
      "query": "running with scissors",
      "fields": ["comment", "comment.english"]
    }
  },
  "highlight": {
    "order": "score",
    "fields": {
      "comment": {
        "type" : "fvh"
      }
    }
  }
}
```

The above request matches both "run with scissors" and "running with scissors"
and would highlight "running" and "scissors" but not "run". If both
phrases appear in a large document then "running with scissors" is
sorted above "run with scissors" in the fragments list because there
are more matches in that fragment.

```console-result
{
  ...
  "hits" : {
    "total" : {
      "value" : 2,
      "relation" : "eq"
    },
    "max_score": 1.0577903,
    "hits" : [
      {
        "_index" : "index2",
        "_id" : "doc2",
        "_score" : 1.0577903,
        "_source" : {
          "comment" : "running with scissors"
        },
        "highlight" : {
          "comment" : [
            "<em>running</em> <em>with</em> <em>scissors</em>"
          ]
        }
      },
      {
        "_index" : "index2",
        "_id" : "doc1",
        "_score" : 0.36464313,
        "_source" : {
          "comment" : "run with scissors"
        },
        "highlight" : {
          "comment" : [
            "run <em>with</em> <em>scissors</em>"
          ]
        }
      }
    ]
  }
}
```

The below request highlights "run" as well as "running" and "scissors",
because the `matched_fields` parameter instructs that for highlighting
we need to combine matches from the `comment` and `comment.english` fields.

```console
GET index2/_search
{
  "query": {
    "query_string": {
      "query": "running with scissors",
      "fields": ["comment", "comment.english"]
    }
  },
  "highlight": {
    "order": "score",
    "fields": {
      "comment": {
        "type" : "fvh",
        "matched_fields": ["comment", "comment.english"]
      }
    }
  }
}
```

```console-result
{
  ...
  "hits" : {
    "total" : {
      "value" : 2,
      "relation" : "eq"
    },
    "max_score": 1.0577903,
    "hits" : [
      {
        "_index" : "index2",
        "_id" : "doc2",
        "_score" : 1.0577903,
        "_source" : {
          "comment" : "running with scissors"
        },
        "highlight" : {
          "comment" : [
            "<em>running</em> <em>with</em> <em>scissors</em>"
          ]
        }
      },
      {
        "_index" : "index2",
        "_id" : "doc1",
        "_score" : 0.36464313,
        "_source" : {
          "comment" : "run with scissors"
        },
        "highlight" : {
          "comment" : [
            "<em>run</em> <em>with</em> <em>scissors</em>"
          ]
        }
      }
    ]
  }
}
```

The below request wouldn't highlight "run" or "scissor" but shows that
it is just fine not to list the field to which the matches are combined
(`comment.english`) in the matched fields.

```console
GET index2/_search
{
  "query": {
    "query_string": {
      "query": "running with scissors",
      "fields": ["comment", "comment.english"]
    }
  },
  "highlight": {
    "order": "score",
    "fields": {
      "comment.english": {
        "type" : "fvh",
        "matched_fields": ["comment"]
      }
    }
  }
}
```

```console-result
{
  ...
  "hits" : {
    "total" : {
      "value" : 2,
      "relation" : "eq"
    },
    "max_score": 1.0577903,
    "hits" : [
      {
        "_index" : "index2",
        "_id" : "doc2",
        "_score" : 1.0577903,
        "_source" : {
          "comment" : "running with scissors"
        },
        "highlight" : {
          "comment.english" : [
            "<em>running</em> <em>with</em> <em>scissors</em>"
          ]
        }
      },
      {
        "_index" : "index2",
        "_id" : "doc1",
        "_score" : 0.36464313,
        "_source" : {
          "comment" : "run with scissors"
        },
        "highlight" : {
          "comment.english" : [
            "run <em>with</em> <em>scissors</em>"
          ]
        }
      }
    ]
  }
}
```

===================================================================
There is a small amount of overhead involved with setting
`matched_fields` to a non-empty array so always prefer
```js
    "highlight": {
        "fields": {
            "comment": {}
        }
    }
```
to
```js
    "highlight": {
        "fields": {
            "comment": {
                "matched_fields": ["comment"],
                "type" : "fvh"
            }
        }
    }
```
