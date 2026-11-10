<!-- Converted from docs/termvectors.asciidoc (AsciiDoc). Includes are inlined. -->

### Term vectors API

**New API reference**
For the most up-to-date API details, refer to [Document APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-document).

Retrieves information and statistics for terms in the fields of a particular document. 

```console
GET /my-index-000001/_termvectors/1
```

#### Request

`GET /<index>/_termvectors/<_id>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `read`
index privilege for the target index or index alias.

#### Description

You can retrieve term vectors for documents stored in the index or 
for _artificial_ documents passed in the body of the request. 

You can specify the fields you are interested in through the `fields` parameter,
or by adding the fields to the request body. 

```console
GET /my-index-000001/_termvectors/1?fields=message
```

Fields can be specified using wildcards, similar to the multi match query.

Term vectors are real-time by default, not near real-time. 
This can be changed by setting `realtime` parameter to `false`.

You can request three types of values: _term information_, _term statistics_
and _field statistics_. By default, all term information and field
statistics are returned for all fields but term statistics are excluded.

##### Term information

 * term frequency in the field (always returned)
 * term positions (`positions` : true)
 * start and end offsets (`offsets` : true)
 * term payloads (`payloads` : true), as base64 encoded bytes

If the requested information wasn't stored in the index, it will be
computed on the fly if possible. Additionally, term vectors could be computed
for documents not even existing in the index, but instead provided by the user.

======
Start and end offsets assume UTF-16 encoding is being used. If you want to use
these offsets in order to get the original text that produced this token, you
should make sure that the string you are taking a sub-string of is also encoded
using UTF-16.
======

##### Term statistics

Setting `term_statistics` to `true` (default is `false`) will
return

 * total term frequency (how often a term occurs in all documents) +
 * document frequency (the number of documents containing the current
   term)

By default these values are not returned since term statistics can
have a serious performance impact.

##### Field statistics

Setting `field_statistics` to `false` (default is `true`) will
omit :

 * document count (how many documents contain this field)
 * sum of document frequencies (the sum of document frequencies for all
   terms in this field)
 * sum of total term frequencies (the sum of total term frequencies of
   each term in this field)

##### Terms filtering

With the parameter `filter`, the terms returned could also be filtered based
on their tf-idf scores. This could be useful in order find out a good
characteristic vector of a document. This feature works in a similar manner to
the second phase of the
More Like This Query. See example 5
for usage.

The following sub-parameters are supported:

`max_num_terms`::
  Maximum number of terms that must be returned per field. Defaults to `25`.
`min_term_freq`::
  Ignore words with less than this frequency in the source doc. Defaults to `1`.
`max_term_freq`::
  Ignore words with more than this frequency in the source doc. Defaults to unbounded.
`min_doc_freq`::
  Ignore terms which do not occur in at least this many docs. Defaults to `1`.
`max_doc_freq`::
  Ignore words which occur in more than this many docs. Defaults to unbounded.
`min_word_length`::
  The minimum word length below which words will be ignored. Defaults to `0`.
`max_word_length`::
  The maximum word length above which words will be ignored. Defaults to unbounded (`0`).

#### Behaviour

The term and field statistics are not accurate. Deleted documents
are not taken into account. The information is only retrieved for the
shard the requested document resides in.
The term and field statistics are therefore only useful as relative measures
whereas the absolute numbers have no meaning in this context. By default,
when requesting term vectors of artificial documents, a shard to get the statistics
from is randomly selected. Use `routing` only to hit a particular shard.

#### Path parameters

`<index>`::
(Required, string) Name of the index that contains the document.

`<_id>`::
(Optional, string) Unique identifier of the document.

#### Query parameters

`fields`::
(Optional, string)
Comma-separated list or wildcard expressions of fields
to include in the statistics.

Used as the default list
unless a specific field list is provided
in the `completion_fields` or `fielddata_fields` parameters.
`field_statistics`::
(Optional, Boolean) If `true`, the response includes the document count, sum of document frequencies,
and sum of total term frequencies.
Defaults to `true`.
`<offsets>`::
(Optional, Boolean) If `true`, the response includes term offsets.
Defaults to `true`.
`payloads`::
(Optional, Boolean) If `true`, the response includes term payloads.
Defaults to `true`.
`positions`::
(Optional, Boolean) If `true`, the response includes term positions.
Defaults to `true`.
`preference`::
(Optional, string) Specifies the node or shard the operation should be
performed on. Random by default.
`routing`::
(Optional, string)
Custom value used to route operations to a specific shard.
`realtime`::
(Optional, Boolean) If `true`, the request is real-time as opposed to near-real-time.
Defaults to `true`. See realtime.
`term_statistics`::
(Optional, Boolean) If `true`, the response includes term frequency and document frequency.
Defaults to `false`.
`version`::
(Optional, Boolean) If `true`, returns the document version as part of a hit.
`version_type`::
(Optional, enum) Specific version type: `external`,
`external_gte`.

#### Examples

##### Returning stored term vectors

First, we create an index that stores term vectors, payloads etc. :

```console
PUT /my-index-000001
{ "mappings": {
    "properties": {
      "text": {
        "type": "text",
        "term_vector": "with_positions_offsets_payloads",
        "store" : true,
        "analyzer" : "fulltext_analyzer"
       },
       "fullname": {
        "type": "text",
        "term_vector": "with_positions_offsets_payloads",
        "analyzer" : "fulltext_analyzer"
      }
    }
  },
  "settings" : {
    "index" : {
      "number_of_shards" : 1,
      "number_of_replicas" : 0
    },
    "analysis": {
      "analyzer": {
        "fulltext_analyzer": {
          "type": "custom",
          "tokenizer": "whitespace",
          "filter": [
            "lowercase",
            "type_as_payload"
          ]
        }
      }
    }
  }
}
```

Second, we add some documents:

```console
PUT /my-index-000001/_doc/1
{
  "fullname" : "John Doe",
  "text" : "test test test "
}

PUT /my-index-000001/_doc/2?refresh=wait_for
{
  "fullname" : "Jane Doe",
  "text" : "Another test ..."
}
```

The following request returns all information and statistics for field
`text` in document `1` (John Doe):

```console
GET /my-index-000001/_termvectors/1
{
  "fields" : ["text"],
  "offsets" : true,
  "payloads" : true,
  "positions" : true,
  "term_statistics" : true,
  "field_statistics" : true
}
```

Response:

```console-result
{
  "_index": "my-index-000001",
  "_id": "1",
  "_version": 1,
  "found": true,
  "took": 6,
  "term_vectors": {
    "text": {
      "field_statistics": {
        "sum_doc_freq": 4,
        "doc_count": 2,
        "sum_ttf": 6
      },
      "terms": {
        "test": {
          "doc_freq": 2,
          "ttf": 4,
          "term_freq": 3,
          "tokens": [
            {
              "position": 0,
              "start_offset": 0,
              "end_offset": 4,
              "payload": "d29yZA=="
            },
            {
              "position": 1,
              "start_offset": 5,
              "end_offset": 9,
              "payload": "d29yZA=="
            },
            {
              "position": 2,
              "start_offset": 10,
              "end_offset": 14,
              "payload": "d29yZA=="
            }
          ]
        }
      }
    }
  }
}
```

##### Generating term vectors on the fly

Term vectors which are not explicitly stored in the index are automatically
computed on the fly. The following request returns all information and statistics for the
fields in document `1`, even though the terms haven't been explicitly stored in the index.
Note that for the field `text`, the terms are not re-generated.

```console
GET /my-index-000001/_termvectors/1
{
  "fields" : ["text", "some_field_without_term_vectors"],
  "offsets" : true,
  "positions" : true,
  "term_statistics" : true,
  "field_statistics" : true
}
```

##### Artificial documents

Term vectors can also be generated for artificial documents,
that is for documents not present in the index. For example, the following request would
return the same results as in example 1. The mapping used is determined by the `index`.

*If dynamic mapping is turned on (default), the document fields not in the original
mapping will be dynamically created.*

```console
GET /my-index-000001/_termvectors
{
  "doc" : {
    "fullname" : "John Doe",
    "text" : "test test test"
  }
}
```

###### Per-field analyzer

Additionally, a different analyzer than the one at the field may be provided
by using the `per_field_analyzer` parameter. This is useful in order to
generate term vectors in any fashion, especially when using artificial
documents. When providing an analyzer for a field that already stores term
vectors, the term vectors will be re-generated.

```console
GET /my-index-000001/_termvectors
{
  "doc" : {
    "fullname" : "John Doe",
    "text" : "test test test"
  },
  "fields": ["fullname"],
  "per_field_analyzer" : {
    "fullname": "keyword"
  }
}
```

Response:

```console-result
{
  "_index": "my-index-000001",
  "_version": 0,
  "found": true,
  "took": 6,
  "term_vectors": {
    "fullname": {
       "field_statistics": {
          "sum_doc_freq": 2,
          "doc_count": 4,
          "sum_ttf": 4
       },
       "terms": {
          "John Doe": {
             "term_freq": 1,
             "tokens": [
                {
                   "position": 0,
                   "start_offset": 0,
                   "end_offset": 8
                }
             ]
          }
       }
    }
  }
}
```

##### Terms filtering

Finally, the terms returned could be filtered based on their tf-idf scores. In
the example below we obtain the three most "interesting" keywords from the
artificial document having the given "plot" field value. Notice
that the keyword "Tony" or any stop words are not part of the response, as
their tf-idf must be too low.

```console
GET /imdb/_termvectors
{
  "doc": {
    "plot": "When wealthy industrialist Tony Stark is forced to build an armored suit after a life-threatening incident, he ultimately decides to use its technology to fight against evil."
  },
  "term_statistics": true,
  "field_statistics": true,
  "positions": false,
  "offsets": false,
  "filter": {
    "max_num_terms": 3,
    "min_term_freq": 1,
    "min_doc_freq": 1
  }
}
```

Response:

```console-result
{
   "_index": "imdb",
   "_version": 0,
   "found": true,
   "term_vectors": {
      "plot": {
         "field_statistics": {
            "sum_doc_freq": 3384269,
            "doc_count": 176214,
            "sum_ttf": 3753460
         },
         "terms": {
            "armored": {
               "doc_freq": 27,
               "ttf": 27,
               "term_freq": 1,
               "score": 9.74725
            },
            "industrialist": {
               "doc_freq": 88,
               "ttf": 88,
               "term_freq": 1,
               "score": 8.590818
            },
            "stark": {
               "doc_freq": 44,
               "ttf": 47,
               "term_freq": 1,
               "score": 9.272792
            }
         }
      }
   }
}
```
