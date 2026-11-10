<!-- Converted from geospatial-analysis.asciidoc (AsciiDoc). Includes are inlined. -->

# Geospatial analysis

Did you know that Elasticsearch has geospatial capabilities? [Elasticsearch and geo](https://www.elastic.co/blog/geo-location-and-search) go way back, to 2010. A lot has happened since then and today Elasticsearch provides robust geospatial capabilities with speed, all with a stack that scales automatically.

Not sure where to get started with Elasticsearch and geo? Then, you have come to the right place.

### Geospatial mapping

Elasticsearch supports two types of geo data: geo_point fields which support lat/lon pairs, and geo_shape fields, which support points, lines, circles, polygons, multi-polygons, and so on. Use explicit mapping to index geo data fields.

Have an index with lat/lon pairs but no geo_point mapping? Use runtime fields to make a geo_point field without reindexing.

### Ingest

Data is often messy and incomplete. Ingest pipelines lets you clean, transform, and augment your data before indexing.

* Use csv-processor together with explicit mapping to index CSV files with geo data.
  Kibana's [Import CSV](https://www.elastic.co/guide/en/kibana/8.19/import-geospatial-data.html) feature can help with this.
* Use geoip-processor to add geographical location of an IPv4 or IPv6 address.
* Use geo-grid processor to convert grid tiles or hexagonal cell ids to bounding boxes or polygons which describe their shape.
* Use geo_match enrich policy for reverse geocoding. For example, use [reverse geocoding](https://www.elastic.co/guide/en/kibana/8.19/reverse-geocoding-tutorial.html) to visualize metropolitan areas by web traffic.

### Query

Geo queries answer location-driven questions. Find documents that intersect with, are within, are contained by, or do not intersect your query geometry. Combine geospatial queries with full text search queries for unparalleled searching experience. For example, "Show me all subscribers that live within 5 miles of our new gym location, that joined in the last year and have running mentioned in their profile".

### ES|QL

ES|QL has support for Geospatial Search functions, enabling efficient index searching for documents that intersect with, are within, are contained by, or are disjoint from a query geometry. In addition, the `ST_DISTANCE` function calculates the distance between two points.

* esql-st_intersects
* esql-st_disjoint
* esql-st_contains
* esql-st_within
* esql-st_distance

### Aggregate

Aggregations summarizes your data as metrics, statistics, or other analytics. Use bucket aggregations to group documents into buckets, also called bins, based on field values, ranges, or other criteria. Then, use metric aggregations to calculate metrics, such as a sum or average, from field values in each bucket. Compare metrics across buckets to gain insights from your data.

Geospatial bucket aggregations:

* Geo-distance aggregation evaluates the distance of each geo_point location from an origin point and determines the buckets it belongs to based on the ranges (a document belongs to a bucket if the distance between the document and the origin falls within the distance range of the bucket).
* Geohash grid aggregation groups geo_point and geo_shape values into buckets that represent a grid.
* Geohex grid aggregation groups geo_point and geo_shape values into buckets that represent an H3 hexagonal cell.
* Geotile grid aggregation groups geo_point and geo_shape values into buckets that represent a grid. Each cell corresponds to a [map tile](https://en.wikipedia.org/wiki/Tiled_web_map) as used by many online map sites.

Geospatial metric aggregations:

* Geo-bounds aggregation computes the geographic bounding box containing all values for a Geopoint or Geoshape field.
* Geo-centroid aggregation computes the weighted centroid from all coordinate values for geo fields.
* Geo-line aggregation aggregates all geo_point values within a bucket into a LineString ordered by the chosen sort field. Use geo_line aggregation to create [vehicle tracks](https://www.elastic.co/guide/en/kibana/8.19/asset-tracking-tutorial.html).

Combine aggregations to perform complex geospatial analysis. For example, to calculate the most recent GPS tracks per flight, use a terms aggregation to group documents into buckets per aircraft. Then use geo-line aggregation to compute a track for each aircraft. In another example, use geotile grid aggregation to group documents into a grid. Then use geo-centroid aggregation to find the weighted centroid of each grid cell.

### Integrate

Use vector tile search API to consume Elasticsearch geo data within existing GIS infrastructure.

### Visualize

Visualize geo data with [Kibana](https://www.elastic.co/guide/en/kibana/8.19/maps.html). Add your map to a [dashboard](https://www.elastic.co/guide/en/kibana/8.19/dashboard.html) to view your data from all angles.

This dashboard shows the effects of the [Cumbre Vieja eruption](https://www.elastic.co/blog/understanding-evolution-volcano-eruption-elastic-maps/).

image:images/spatial/cumbre_vieja_eruption_dashboard.png[Kibana dashboard showing Cumbre Vieja eruption from Aug 31 2021 to Dec 14 2021]

### Machine learning

Put machine learning to work for you and find the data that should stand out with anomaly detections. Find credit card transactions that occur in an unusual locations or a web request that has an unusual source location. {ml-docs}/geographic-anomalies.html[Location-based anomaly detections] make it easy to find and explore and compare anomalies with their typical locations.

### Alerting

Let your location data drive insights and action with [geographic alerts](https://www.elastic.co/guide/en/kibana/8.19/geo-alerting.html). Commonly referred to as geo-fencing, track moving objects as they enter or exit a boundary to receive notifications through common business systems (email, Slack, Teams, PagerDuty, and more).

Interested in learning more? Follow [step-by-step instructions](https://www.elastic.co/guide/en/kibana/8.19/asset-tracking-tutorial.html) for setting up tracking containment alerts to monitor moving vehicles.
