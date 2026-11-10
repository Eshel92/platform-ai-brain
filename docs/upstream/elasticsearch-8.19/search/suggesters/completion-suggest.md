<!-- Converted from search/suggesters/completion-suggest.asciidoc (AsciiDoc). Includes are inlined. -->

#### Completion Suggester

The `completion` suggester provides auto-complete/search-as-you-type
functionality. This is a navigational feature to guide users to
relevant results as they are typing, improving search precision.
It is not meant for spell correction or did-you-mean functionality
like the `term` or `phrase` suggesters.

Ideally, auto-complete functionality should be as fast as a user
types to provide instant feedback relevant to what a user has already
typed in. Hence, `completion` suggester is optimized for speed.
The suggester uses data structures that enable fast lookups,
but are costly to build and are stored in-memory.

##### Mapping

(See `search/suggesters/../../mapping/types/completion.md`)

##### Indexing

You index suggestions like any other field. A suggestion is made of an
`input` and an optional `weight` attribute. An `input` is the expected
text to be matched by a suggestion query and the `weight` determines how
the suggestions will be scored. Indexing a suggestion is as follows:

```console
PUT music/_doc/1?refresh
{
  "suggest" : {
    "input": [ "Nevermind", "Nirvana" ],
    "weight" : 34
  }
}
```

The following parameters are supported:

`input`::
    The input to store, this can be an array of strings or just
    a string. This field is mandatory.

**Note:**
This value cannot contain the following UTF-16 control characters:

* `\u0000` (null)
* `\u001f` (information separator one)
* `\u001e` (information separator two)

`weight`::
    A positive integer or a string containing a positive integer,
    which defines a weight and allows you to rank your suggestions.
    This field is optional.

You can index multiple suggestions for a document as follows:

```console
PUT music/_doc/1?refresh
{
  "suggest": [
    {
      "input": "Nevermind",
      "weight": 10
    },
    {
      "input": "Nirvana",
      "weight": 3
    }
  ]
}
```

You can use the following shorthand form. Note that you can not specify
a weight with suggestion(s) in the shorthand form.

```console
PUT music/_doc/1?refresh
{
  "suggest" : [ "Nevermind", "Nirvana" ]
}
```

##### Querying

Suggesting works as usual, except that you have to specify the suggest
type as `completion`. Suggestions are near real-time, which means
new suggestions can be made visible by refresh and
documents once deleted are never shown. This request:

```console
POST music/_search?pretty
{
  "suggest": {
    "song-suggest": {
      "prefix": "nir",        <1>
      "completion": {         <2>
          "field": "suggest"  <3>
      }
    }
  }
}
```

<1> Prefix used to search for suggestions
<2> Type of suggestions
<3> Name of the field to search for suggestions in

returns this response:

```console-result
{
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits": ...
  "took": 2,
  "timed_out": false,
  "suggest": {
    "song-suggest" : [ {
      "text" : "nir",
      "offset" : 0,
      "length" : 3,
      "options" : [ {
        "text" : "Nirvana",
        "_index": "music",
        "_id": "1",
        "_score": 1.0,
        "_source": {
          "suggest": ["Nevermind", "Nirvana"]
        }
      } ]
    } ]
  }
}
```

**Important:** `_source` metadata field must be enabled, which is the default
behavior, to enable returning `_source` with suggestions.

The configured weight for a suggestion is returned as `_score`. The
`text` field uses the `input` of your indexed suggestion. Suggestions
return the full document `_source` by default. The size of the `_source`
can impact performance due to disk fetch and network transport overhead.
To save some network overhead, filter out unnecessary fields from the `_source`
using source filtering to minimize
`_source` size. Note that the _suggest endpoint doesn't support source
filtering but using suggest on the `_search` endpoint does:

```console
POST music/_search
{
  "_source": "suggest",     <1>
  "suggest": {
    "song-suggest": {
      "prefix": "nir",
      "completion": {
        "field": "suggest", <2>
        "size": 5           <3>
      }
    }
  }
}
```

<1> Filter the source to return only the `suggest` field
<2> Name of the field to search for suggestions in
<3> Number of suggestions to return

Which should look like:

```console-result
{
  "took": 6,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 0,
      "relation": "eq"
    },
    "max_score": null,
    "hits": []
  },
  "suggest": {
    "song-suggest": [ {
        "text": "nir",
        "offset": 0,
        "length": 3,
        "options": [ {
            "text": "Nirvana",
            "_index": "music",
            "_id": "1",
            "_score": 1.0,
            "_source": {
              "suggest": [ "Nevermind", "Nirvana" ]
            }
          } ]
      } ]
  }
}
```

The basic completion suggester query supports the following parameters:

`field`:: The name of the field on which to run the query (required).
`size`::  The number of suggestions to return (defaults to `5`).
`skip_duplicates`:: Whether duplicate suggestions should be filtered out (defaults to `false`).

**Note:** The completion suggester considers all documents in the index.
See context-suggester for an explanation of how to query a subset of
documents instead.

**Note:** In case of completion queries spanning more than one shard, the suggest
is executed in two phases, where the last phase fetches the relevant documents
from shards, implying executing completion requests against a single shard is
more performant due to the document fetch overhead when the suggest spans
multiple shards. To get best performance for completions, it is recommended to
index completions into a single shard index. In case of high heap usage due to
shard size, it is still recommended to break index into multiple shards instead
of optimizing for completion performance.

##### Skip duplicate suggestions

Queries can return duplicate suggestions coming from different documents.
It is possible to modify this behavior by setting `skip_duplicates` to true.
When set, this option filters out documents with duplicate suggestions from the result.

```console
POST music/_search?pretty
{
  "suggest": {
    "song-suggest": {
      "prefix": "nor",
      "completion": {
        "field": "suggest",
        "skip_duplicates": true
      }
    }
  }
}
```

**Warning:** When set to true, this option can slow down search because more suggestions
need to be visited to find the top N.

##### Fuzzy queries

The completion suggester also supports fuzzy queries -- this means
you can have a typo in your search and still get results back.

```console
POST music/_search?pretty
{
  "suggest": {
    "song-suggest": {
      "prefix": "nor",
      "completion": {
        "field": "suggest",
        "fuzzy": {
          "fuzziness": 2
        }
      }
    }
  }
}
```

Suggestions that share the longest prefix to the query `prefix` will
be scored higher.

The fuzzy query can take specific fuzzy parameters.
The following parameters are supported:

`fuzziness`::
    The fuzziness factor, defaults to `AUTO`.
    See  fuzziness for allowed settings.

`transpositions`::
    if set to `true`, transpositions are counted
    as one change instead of two, defaults to `true`

`min_length`::
    Minimum length of the input before fuzzy
    suggestions are returned, defaults `3`

`prefix_length`::
    Minimum length of the input, which is not
    checked for fuzzy alternatives, defaults to `1`

`unicode_aware`::
    If `true`, all measurements (like fuzzy edit
    distance, transpositions, and lengths) are
    measured in Unicode code points instead of
    in bytes. This is slightly slower than raw
    bytes, so it is set to `false` by default.

**Note:** If you want to stick with the default values, but
      still use fuzzy, you can either use `fuzzy: {}`
      or `fuzzy: true`.

##### Regex queries

The completion suggester also supports regex queries meaning
you can express a prefix as a regular expression

```console
POST music/_search?pretty
{
  "suggest": {
    "song-suggest": {
      "regex": "n[ever|i]r",
      "completion": {
        "field": "suggest"
      }
    }
  }
}
```

The regex query can take specific regex parameters.
The following parameters are supported:

`flags`::
    Possible flags are `ALL` (default), `ANYSTRING`, `COMPLEMENT`,
    `EMPTY`, `INTERSECTION`, `INTERVAL`, or `NONE`. See regexp-syntax
    for their meaning

`max_determinized_states`::
    Regular expressions are dangerous because it's easy to accidentally
    create an innocuous looking one that requires an exponential number of
    internal determinized automaton states (and corresponding RAM and CPU)
    for Lucene to execute. Lucene prevents these using the
    `max_determinized_states` setting (defaults to 10000). You can raise
    this limit to allow more complex regular expressions to execute.
