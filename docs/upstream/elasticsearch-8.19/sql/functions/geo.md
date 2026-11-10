<!-- Converted from sql/functions/geo.asciidoc (AsciiDoc). Includes are inlined. -->

### Geo Functions

beta[]

The geo functions work with geometries stored in `geo_point`, `geo_shape` and `shape` fields, or returned by other geo functions.

#### Limitations

`geo_point`, `geo_shape` and `shape` and types are represented in SQL as
geometry and can be used interchangeably with the following exceptions:

* `geo_shape` and `shape` fields don't have doc values, therefore these fields cannot be used for filtering, grouping
  or sorting.

* `geo_points` fields are indexed and have doc values by default, however only latitude and longitude are stored and
  indexed with some loss of precision from the original values (4.190951585769653E-8 for the latitude and
  8.381903171539307E-8 for longitude). The altitude component is accepted but not stored in doc values nor indexed.
  Therefore calling `ST_Z` function in the filtering, grouping or sorting will return `null`.

#### Geometry Conversion

##### `ST_AsWKT`

**Synopsis:**
```sql
ST_AsWKT(
    geometry <1>
)
```

*Input*:

<1> geometry. If `null`, the function returns `null`.

*Output*: string

*Description*: Returns the WKT representation of the `geometry`.

```
include-tagged::{sql-specs}/docs/geo.csv-spec[aswkt]
```

##### `ST_WKTToSQL`

**Synopsis:**
```sql
ST_WKTToSQL(
    string <1>
)
```

*Input*:

<1> string WKT representation of geometry. If `null`, the function returns
`null`.

*Output*: geometry

*Description*: Returns the geometry from WKT representation.

```
include-tagged::{sql-specs}/docs/geo.csv-spec[wkttosql]
```

#### Geometry Properties

##### `ST_GeometryType`

**Synopsis:**
```sql
ST_GeometryType(
    geometry <1>
)
```

*Input*:

<1> geometry. If `null`, the function returns `null`.

*Output*: string

*Description*: Returns the type of the `geometry` such as POINT, MULTIPOINT, LINESTRING, MULTILINESTRING, POLYGON, MULTIPOLYGON, GEOMETRYCOLLECTION, ENVELOPE or CIRCLE.

```
include-tagged::{sql-specs}/docs/geo.csv-spec[geometrytype]
```

##### `ST_X`

**Synopsis:**
```sql
ST_X(
    geometry <1>
)
```

*Input*:

<1> geometry. If `null`, the function returns `null`.

*Output*: double

*Description*: Returns the longitude of the first point in the geometry.

```
include-tagged::{sql-specs}/docs/geo.csv-spec[x]
```

##### `ST_Y`

**Synopsis:**
```sql
ST_Y(
    geometry <1>
)
```

*Input*:

<1> geometry. If `null`, the function returns `null`.

*Output*: double

*Description*: Returns the latitude of the first point in the geometry.

```
include-tagged::{sql-specs}/docs/geo.csv-spec[y]
```

##### `ST_Z`

**Synopsis:**
```sql
ST_Z(
    geometry <1>
)
```

*Input*:

<1> geometry. If `null`, the function returns `null`.

*Output*: double

*Description*: Returns the altitude of the first point in the geometry.

```
include-tagged::{sql-specs}/docs/geo.csv-spec[z]
```

##### `ST_Distance`

**Synopsis:**
```sql
ST_Distance(
    geometry, <1>
    geometry  <2>
)
```

*Input*:

<1> source geometry. If `null`, the function returns `null`.
<2> target geometry. If `null`, the function returns `null`.

*Output*: Double

*Description*: Returns the distance between geometries in meters. Both geometries have to be points.

```
include-tagged::{sql-specs}/docs/geo.csv-spec[distance]
```
