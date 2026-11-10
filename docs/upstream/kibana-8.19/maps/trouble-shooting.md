<!-- Converted from maps/trouble-shooting.asciidoc (AsciiDoc). Includes are inlined. -->

## Troubleshoot Maps

Use the information in this section to inspect Elasticsearch requests and find solutions to common problems.

### Inspect Elasticsearch requests

Maps uses the [Elasticsearch vector tile search API](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/search-vector-tile-api.html) and the [Elasticsearch search API](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/search-search.html) to get documents and aggregation results from Elasticsearch. Use *Vector tiles* inspector to view Elasticsearch vector tile search API requests. Use *Requests* inspector to view Elasticsearch search API requests.

(Figure: maps/images/vector_tile_inspector.png)

(Figure: maps/images/requests_inspector.png)

### Solutions to common problems

#### Data view not listed when adding layer

* Verify your geospatial data is correctly mapped as [geo_point](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/geo-point.html) or [geo_shape](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/geo-shape.html).
  ** Run `GET myIndexName/_field_caps?fields=myGeoFieldName` in Console, replacing `myIndexName` and `myGeoFieldName` with your index and geospatial field name.
  ** Ensure response specifies `type` as `geo_point` or `geo_shape`.
* Verify your geospatial data is correctly mapped in your data view.
  ** Open your data view in Stack Management.
  ** Ensure your geospatial field type is `geo_point` or `geo_shape`.
  ** Ensure your geospatial field is searchable and aggregatable.
  ** If your geospatial field type does not match your Elasticsearch mapping, click the *Refresh* button to refresh the field list from Elasticsearch.
* Data views with thousands of fields can exceed the default maximum payload size.
Increase `server.maxPayload` for large data views.

#### Features are not displayed

* Use Inspector to view Elasticsearch responses. Ensure the response is not empty.
* Ensure geometry uses the correct latitude and longitude ordering.
  ** Geo-points expressed as strings are ordered as `"latitude,longitude"`. Geo-points expressed as arrays are ordered as the reverse: `[longitude, latitude]`.
  ** Geo-shapes expressed as geojson provide coordinates as `[longitude, latitude]`.
* Ensure fill color and border color are distinguishable from map tiles. It's hard to see white features on a white background.

#### Elastic Maps Service basemaps are not displayed

*Maps* uses tile and vector data from Elastic Maps Service by default. See Connect to Elastic Maps Service for more info.

#### Custom tiles are not displayed

* When using a custom tile service, ensure your tile server has configured [Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) so tile requests from your Kibana domain have permission to access your tile server domain.
* Ensure custom vector and tile services have the required coordinate system. Vector data must use EPSG:4326 and tiles must use EPSG:3857.
