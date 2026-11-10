<!-- Converted from query-dsl/geo-polygon-query.asciidoc (AsciiDoc). Includes are inlined. -->

### Geo-polygon query

deprecated::[7.12,Use query-dsl-geo-shape-query instead where polygons are defined in GeoJSON or [Well-Known Text (WKT)](http://docs.opengeospatial.org/is/18-010r7/18-010r7.html).]

A query returning hits that only fall within a polygon of
points. Here is an example:

```console
GET /_search
{
  "query": {
    "bool": {
      "must": {
        "match_all": {}
      },
      "filter": {
        "geo_polygon": {
          "person.location": {
            "points": [
              { "lat": 40, "lon": -70 },
              { "lat": 30, "lon": -80 },
              { "lat": 20, "lon": -90 }
            ]
          }
        }
      }
    }
  }
}
```

#### Query options

|=======================================================================
|Option |Description
|`_name` |Optional name field to identify the filter

|`validation_method` |Set to `IGNORE_MALFORMED` to accept geo points with
invalid latitude or longitude, `COERCE` to try and infer correct latitude
or longitude, or `STRICT` (default is `STRICT`).
|=======================================================================

#### Allowed formats

##### Lat long as array

Format as `[lon, lat]`

Note: the order of lon/lat here must
conform with [GeoJSON](http://geojson.org/).

```console
GET /_search
{
  "query": {
    "bool": {
      "must": {
        "match_all": {}
      },
      "filter": {
        "geo_polygon": {
          "person.location": {
            "points": [
              [ -70, 40 ],
              [ -80, 30 ],
              [ -90, 20 ]
            ]
          }
        }
      }
    }
  }
}
```

##### Lat lon as string

Format in `lat,lon`.

```console
GET /_search
{
  "query": {
    "bool": {
      "must": {
        "match_all": {}
      },
      "filter": {
        "geo_polygon": {
          "person.location": {
            "points": [
              "40, -70",
              "30, -80",
              "20, -90"
            ]
          }
        }
      }
    }
  }
}
```

##### Geohash

```console
GET /_search
{
  "query": {
    "bool": {
      "must": {
        "match_all": {}
      },
      "filter": {
        "geo_polygon": {
          "person.location": {
            "points": [
              "drn5x1g8cu2y",
              "30, -80",
              "20, -90"
            ]
          }
        }
      }
    }
  }
}
```

#### `geo_point` type

The query *requires* the `geo_point` type to be set on the
relevant field.

#### Ignore unmapped

When set to `true` the `ignore_unmapped` option will ignore an unmapped field
and will not match any documents for this query. This can be useful when
querying multiple indexes which might have different mappings. When set to
`false` (the default value) the query will throw an exception if the field
is not mapped.
