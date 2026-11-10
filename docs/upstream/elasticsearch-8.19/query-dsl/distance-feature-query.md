<!-- Converted from query-dsl/distance-feature-query.asciidoc (AsciiDoc). Includes are inlined. -->

### Distance feature query

Boosts the relevance score of documents closer to a
provided `origin` date or point. For example, you can use this query to give
more weight to documents closer to a certain date or location.

You can use the `distance_feature` query to find the nearest neighbors to a
location. You can also use the query in a `bool`
search's `should` filter to add boosted relevance scores to the `bool` query's
scores.

#### Example request

##### Index setup

To use the `distance_feature` query, your index must include a `date`,
`date_nanos` or `geo_point` field.

To see how you can set up an index for the `distance_feature` query, try the
following example.

. Create an `items` index with the following field mapping:

* `name`, a `keyword` field
* `production_date`, a `date` field
* `location`, a `geo_point` field

```console
PUT /items
{
  "mappings": {
    "properties": {
      "name": {
        "type": "keyword"
      },
      "production_date": {
        "type": "date"
      },
      "location": {
        "type": "geo_point"
      }
    }
  }
}
```

. Index several documents to this index.
```console
PUT /items/_doc/1?refresh
{
  "name" : "chocolate",
  "production_date": "2018-02-01",
  "location": [-71.34, 41.12]
}

PUT /items/_doc/2?refresh
{
  "name" : "chocolate",
  "production_date": "2018-01-01",
  "location": [-71.3, 41.15]
}

PUT /items/_doc/3?refresh
{
  "name" : "chocolate",
  "production_date": "2017-12-01",
  "location": [-71.3, 41.12]
}
```

##### Example queries

###### Boost documents based on date

The following `bool` search returns documents with a `name` value of
`chocolate`. The search also uses the `distance_feature` query to increase the
relevance score of documents with a `production_date` value closer to `now`.

```console
GET /items/_search
{
  "query": {
    "bool": {
      "must": {
        "match": {
          "name": "chocolate"
        }
      },
      "should": {
        "distance_feature": {
          "field": "production_date",
          "pivot": "7d",
          "origin": "now"
        }
      }
    }
  }
}
```

###### Boost documents based on location

The following `bool` search returns documents with a `name` value of
`chocolate`. The search also uses the `distance_feature` query to increase the
relevance score of documents with a `location` value closer to `[-71.3, 41.15]`.

```console
GET /items/_search
{
  "query": {
    "bool": {
      "must": {
        "match": {
          "name": "chocolate"
        }
      },
      "should": {
        "distance_feature": {
          "field": "location",
          "pivot": "1000m",
          "origin": [-71.3, 41.15]
        }
      }
    }
  }
}
```

#### Top-level parameters for `distance_feature`

`field`::
(Required, string) Name of the field used to calculate distances. This field
must meet the following criteria:

* Be a `date`, `date_nanos` or
`geo_point` field
* Have an `index` mapping parameter value of `true`, which is
the default
* Have an `doc_values` mapping parameter value of `true`, which
is the default

`origin`::
(Required, string) Date or point of origin used to calculate distances.

If the `field` value is a `date` or `date_nanos`
field, the `origin` value must be a date.
Date Math, such as `now-1h`, is supported.

If the `field` value is a `geo_point` field, the `origin` value
must be a geopoint.

`pivot`::
(Required, time unit or distance unit)
Distance from the `origin` at which relevance scores receive half of the `boost`
value.

If the `field` value is a `date` or `date_nanos`
field, the `pivot` value must be a time unit, such as `1h` or
`10d`.

If the `field` value is a `geo_point` field, the `pivot` value
must be a distance unit, such as `1km` or `12m`.

`boost`::
(Optional, float) Floating point number used to multiply the
relevance score of matching documents. This value
cannot be negative. Defaults to `1.0`.

#### Notes

##### How the `distance_feature` query calculates relevance scores

The `distance_feature` query dynamically calculates the distance between the
`origin` value and a document's field values. It then uses this distance as a
feature to boost the relevance score of closer
documents.

The `distance_feature` query calculates a document's
relevance score as follows:

```
relevance score = boost * pivot / (pivot + distance)
```

The `distance` is the absolute difference between the `origin` value and a
document's field value.

##### Skip non-competitive hits

Unlike the `function_score` query or other
ways to change relevance scores, the
`distance_feature` query efficiently skips non-competitive hits when the
`track_total_hits` parameter is **not** `true`.
