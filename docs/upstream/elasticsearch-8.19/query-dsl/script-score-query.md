<!-- Converted from query-dsl/script-score-query.asciidoc (AsciiDoc). Includes are inlined. -->

### Script score query

Uses a script to provide a custom score for returned
documents.

The `script_score` query is useful if, for example, a scoring function is expensive and you only need to calculate the score of a filtered set of documents.

#### Example request

The following `script_score` query assigns each returned document a score equal to the `my-int` field value divided by `10`.

```console
GET /_search
{
  "query": {
    "script_score": {
      "query": {
        "match": { "message": "elasticsearch" }
      },
      "script": {
        "source": "doc['my-int'].value / 10 "
      }
    }
  }
}
```

#### Top-level parameters for `script_score`

`query`::
(Required, query object) Query used to return documents.

`script`::
(Required, script object) Script used to compute the score of documents returned by the `query`.

**Important:** Final relevance scores from the `script_score` query cannot be
negative. To support certain search optimizations, Lucene requires
scores be positive or `0`.

`min_score`::
(Optional, float) Documents with a score lower
than this floating point number are excluded from the search results.

`boost`::
(Optional, float) Documents' scores produced by `script` are
multiplied by `boost` to produce final documents' scores. Defaults to `1.0`.

#### Notes

##### Use relevance scores in a script

Within a script, you can
[access](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/modules-scripting-fields.html#scripting-score)
the `_score` variable which represents the current relevance score of a
document.

##### Use term statistics in a script

Within a script, you can
[access](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/modules-scripting-fields.html#scripting-term-statistics)
the `_termStats` variable which provides statistical information about the terms used in the child query of the `script_score` query.

##### Predefined functions

You can use any of the available {painless}/painless-contexts.html[painless
functions] in your `script`. You can also use the following predefined functions
to customize scoring:

* script-score-saturation
* script-score-sigmoid
* random-score-function
* decay-functions-numeric-fields
* decay-functions-geo-fields
* decay-functions-date-fields
* script-score-functions-vector-fields

We suggest using these predefined functions instead of writing your own.
These functions take advantage of efficiencies from Elasticsearch' internal mechanisms.

###### Saturation

`saturation(value,k) = value/(k + value)`

```js
"script" : {
    "source" : "saturation(doc['my-int'].value, 1)"
}
```

###### Sigmoid

`sigmoid(value, k, a) = value^a/ (k^a + value^a)`

```js
"script" : {
    "source" : "sigmoid(doc['my-int'].value, 2, 1)"
}
```

###### Random score function

`random_score` function generates scores that are uniformly distributed
from 0 up to but not including 1.

`randomScore` function has the following syntax:
`randomScore(<seed>, <fieldName>)`.
It has a required parameter - `seed` as an integer value,
and an optional parameter - `fieldName` as a string value.

```js
"script" : {
    "source" : "randomScore(100, '_seq_no')"
}
```

If the `fieldName` parameter is omitted, the internal Lucene
document ids will be used as a source of randomness. This is very efficient,
but unfortunately not reproducible since documents might be renumbered
by merges.

```js
"script" : {
    "source" : "randomScore(100)"
}
```

Note that documents that are within the same shard and have the
same value for field will get the same score, so it is usually desirable
to use a field that has unique values for all documents across a shard.
A good default choice might be to use the `_seq_no`
field, whose only drawback is that scores will change if the document is
updated since update operations also update the value of the `_seq_no` field.

###### Decay functions for numeric fields

You can read more about decay functions
[here](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/query-dsl-function-score-query.html#function-decay).

* `double decayNumericLinear(double origin, double scale, double offset, double decay, double docValue)`
* `double decayNumericExp(double origin, double scale, double offset, double decay, double docValue)`
* `double decayNumericGauss(double origin, double scale, double offset, double decay, double docValue)`

```js
"script" : {
    "source" : "decayNumericLinear(params.origin, params.scale, params.offset, params.decay, doc['dval'].value)",
    "params": { <1>
        "origin": 20,
        "scale": 10,
        "decay" : 0.5,
        "offset" : 0
    }
}
```
<1> Using `params` allows to compile the script only once, even if params change.

###### Decay functions for geo fields

* `double decayGeoLinear(String originStr, String scaleStr, String offsetStr, double decay, GeoPoint docValue)`

* `double decayGeoExp(String originStr, String scaleStr, String offsetStr, double decay, GeoPoint docValue)`

* `double decayGeoGauss(String originStr, String scaleStr, String offsetStr, double decay, GeoPoint docValue)`

```js
"script" : {
    "source" : "decayGeoExp(params.origin, params.scale, params.offset, params.decay, doc['location'].value)",
    "params": {
        "origin": "40, -70.12",
        "scale": "200km",
        "offset": "0km",
        "decay" : 0.2
    }
}
```

###### Decay functions for date fields

* `double decayDateLinear(String originStr, String scaleStr, String offsetStr, double decay, JodaCompatibleZonedDateTime docValueDate)`

* `double decayDateExp(String originStr, String scaleStr, String offsetStr, double decay, JodaCompatibleZonedDateTime docValueDate)`

* `double decayDateGauss(String originStr, String scaleStr, String offsetStr, double decay, JodaCompatibleZonedDateTime docValueDate)`

```js
"script" : {
    "source" : "decayDateGauss(params.origin, params.scale, params.offset, params.decay, doc['date'].value)",
    "params": {
        "origin": "2008-01-01T01:00:00Z",
        "scale": "1h",
        "offset" : "0",
        "decay" : 0.5
    }
}
```

**Note:** Decay functions on dates are limited to dates in the default format
and default time zone. Also calculations with `now` are not supported.

###### Functions for vector fields

Functions for vector fields are accessible through
`script_score` query.

##### Allow expensive queries

Script score queries will not be executed if `search.allow_expensive_queries`
is set to false.

##### Faster alternatives

The `script_score` query calculates the score for
every matching document, or hit. There are faster alternative query types that
can efficiently skip non-competitive hits:

* If you want to boost documents on some static fields, use the
 `rank_feature` query.
 * If you want to boost documents closer to a date or geographic point, use the
 `distance_feature` query.

##### Transition from the function score query

We recommend using the `script_score` query instead of
`function_score` query for the simplicity
of the `script_score` query.

You can implement the following functions of the `function_score` query using
the `script_score` query:

* script-score
* weight
* random-score
* field-value-factor
* decay-functions

###### `script_score`

What you used in `script_score` of the Function Score query, you
can copy into the Script Score query. No changes here.

###### `weight`

`weight` function can be implemented in the Script Score query through
the following script:

```js
"script" : {
    "source" : "params.weight * _score",
    "params": {
        "weight": 2
    }
}
```

###### `random_score`

Use `randomScore` function
as described in random score function.

###### `field_value_factor`

`field_value_factor` function can be easily implemented through script:

```js
"script" : {
    "source" : "Math.log10(doc['field'].value * params.factor)",
    "params" : {
        "factor" : 5
    }
}
```

For checking if a document has a missing value, you can use
`doc['field'].size() == 0`. For example, this script will use
a value `1` if a document doesn't have a field `field`:

```js
"script" : {
    "source" : "Math.log10((doc['field'].size() == 0 ? 1 : doc['field'].value()) * params.factor)",
    "params" : {
        "factor" : 5
    }
}
```

This table lists how `field_value_factor` modifiers can be implemented
through a script:

|=======================================================================
| Modifier | Implementation in Script Score

| `none` | -
| `log` |  `Math.log10(doc['f'].value)`
| `log1p` | `Math.log10(doc['f'].value + 1)`
| `log2p` | `Math.log10(doc['f'].value + 2)`
| `ln` | `Math.log(doc['f'].value)`
| `ln1p` | `Math.log(doc['f'].value + 1)`
| `ln2p` | `Math.log(doc['f'].value + 2)`
| `square` | `Math.pow(doc['f'].value, 2)`
| `sqrt` | `Math.sqrt(doc['f'].value)`
| `reciprocal` | `1.0 / doc['f'].value`
|=======================================================================

###### `decay` functions

The `script_score` query has equivalent <<decay-functions-numeric-fields, decay
functions>> that can be used in scripts.

(See `vectors/vector-functions.md`)

##### Explain request

Using an explain request provides an explanation of how the parts of a score were computed. The `script_score` query can add its own explanation by setting the `explanation` parameter:

```console
GET /my-index-000001/_explain/0
{
  "query": {
    "script_score": {
      "query": {
        "match": { "message": "elasticsearch" }
      },
      "script": {
        "source": """
          long count = doc['count'].value;
          double normalizedCount = count / 10;
          if (explanation != null) {
            explanation.set('normalized count = count / 10 = ' + count + ' / 10 = ' + normalizedCount);
          }
          return normalizedCount;
        """
      }
    }
  }
}
```

Note that the `explanation` will be null when using in a normal `_search` request, so having a conditional guard is best practice.
