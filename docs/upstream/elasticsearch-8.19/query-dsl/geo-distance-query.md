<!-- Converted from query-dsl/geo-distance-query.asciidoc (AsciiDoc). Includes are inlined. -->

### Geo-distance query

Matches `geo_point` and `geo_shape` values within
a given distance of a geopoint.

#### Example

Assume the following documents are indexed:

```console
PUT /my_locations
{
  "mappings": {
    "properties": {
      "pin": {
        "properties": {
          "location": {
            "type": "geo_point"
          }
        }
      }
    }
  }
}

PUT /my_locations/_doc/1
{
  "pin": {
    "location": {
      "lat": 40.12,
      "lon": -71.34
    }
  }
}

PUT /my_geoshapes
{
  "mappings": {
    "properties": {
      "pin": {
        "properties": {
          "location": {
            "type": "geo_shape"
          }
        }
      }
    }
  }
}

PUT /my_geoshapes/_doc/1
{
  "pin": {
    "location": {
      "type" : "polygon",
      "coordinates" : [[[13.0 ,51.5], [15.0, 51.5], [15.0, 54.0], [13.0, 54.0], [13.0 ,51.5]]]
    }
  }
}
```

Use a `geo_distance` filter to match `geo_point` values within a specified
distance of another geopoint:

```console
GET /my_locations/_search
{
  "query": {
    "bool": {
      "must": {
        "match_all": {}
      },
      "filter": {
        "geo_distance": {
          "distance": "200km",
          "pin.location": {
            "lat": 40,
            "lon": -70
          }
        }
      }
    }
  }
}
```

Use the same filter to match `geo_shape` values within the given distance:

```console
GET my_geoshapes/_search
{
  "query": {
    "bool": {
      "must": {
        "match_all": {}
      },
      "filter": {
        "geo_distance": {
          "distance": "200km",
          "pin.location": {
            "lat": 40,
            "lon": -70
          }
        }
      }
    }
  }
}
```

To match both `geo_point` and `geo_shape` values, search both indices:

```console
GET my_locations,my_geoshapes/_search
{
  "query": {
    "bool": {
      "must": {
        "match_all": {}
      },
      "filter": {
        "geo_distance": {
          "distance": "200km",
          "pin.location": {
            "lat": 40,
            "lon": -70
          }
        }
      }
    }
  }
}
```

#### Accepted formats

In much the same way the `geo_point` type can accept different
representations of the geo point, the filter can accept it as well:

##### Lat lon as properties

```console
GET /my_locations/_search
{
  "query": {
    "bool": {
      "must": {
        "match_all": {}
      },
      "filter": {
        "geo_distance": {
          "distance": "12km",
          "pin.location": {
            "lat": 40,
            "lon": -70
          }
        }
      }
    }
  }
}
```

##### Lat lon as array

Format in `[lon, lat]`, note, the order of lon/lat here in order to
conform with [GeoJSON](http://geojson.org/).

```console
GET /my_locations/_search
{
  "query": {
    "bool": {
      "must": {
        "match_all": {}
      },
      "filter": {
        "geo_distance": {
          "distance": "12km",
          "pin.location": [ -70, 40 ]
        }
      }
    }
  }
}
```

##### Lat lon as WKT string

Format in [Well-Known Text](https://docs.opengeospatial.org/is/12-063r5/12-063r5.html).

```console
GET /my_locations/_search
{
  "query": {
    "bool": {
      "must": {
        "match_all": {}
      },
      "filter": {
        "geo_distance": {
          "distance": "12km",
          "pin.location": "POINT (-70 40)"
        }
      }
    }
  }
}
```

##### Geohash

```console
GET /my_locations/_search
{
  "query": {
    "bool": {
      "must": {
        "match_all": {}
      },
      "filter": {
        "geo_distance": {
          "distance": "12km",
          "pin.location": "drm3btev3e86"
        }
      }
    }
  }
}
```

#### Options

The following are options allowed on the filter:

`distance`::

    The radius of the circle centred on the specified location. Points which
    fall into this circle are considered to be matches. The `distance` can be
    specified in various units. See distance-units.

`distance_type`::

    How to compute the distance. Can either be `arc` (default), or `plane` (faster, but inaccurate on long distances and close to the poles).

`_name`::

    Optional name field to identify the query

`validation_method`::

    Set to `IGNORE_MALFORMED` to accept geo points with invalid latitude or
    longitude, set to `COERCE` to additionally try and infer correct
    coordinates (default is `STRICT`).

#### Multi location per document

The `geo_distance` filter can work with multiple locations / points per
document. Once a single location / point matches the filter, the
document will be included in the filter.

#### Ignore unmapped

When set to `true` the `ignore_unmapped` option will ignore an unmapped field
and will not match any documents for this query. This can be useful when
querying multiple indexes which might have different mappings. When set to
`false` (the default value) the query will throw an exception if the field
is not mapped.
