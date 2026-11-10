<!-- Converted from maps/geojson-upload.asciidoc (AsciiDoc). Includes are inlined. -->

## Upload GeoJSON data

Maps makes it easy to import geospatial data into the Elastic Stack.
Using the GeoJSON Upload feature, you can drag and drop your point and shape
data files directly into Elasticsearch, and then use them as layers
in the map.  You can also use the GeoJSON data in the broader Kibana ecosystem,
for example, in visualizations and Canvas workpads.

### Why GeoJSON?

GeoJSON is an open-standard file format for storing geospatial vector data.
Although many vector data formats are available in the GIS community,
GeoJSON is the most commonly used and flexible option.

### Upload a GeoJSON file

Follow these instructions to upload a GeoJSON data file, or try the
end-to-end integrated example.

. Go to *Maps*, and select *Add layer*.
. Select *Uploaded GeoJSON*.
(Figure: maps/images/fu_gs_select_source_file_upload.png)

. Use the file chooser to select a valid GeoJSON file. The file will load
a preview of the data on the map.
. Use the default *Index type* of [geo_point](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/geo-point.html) for point data,
or override it and select [geo_shape](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/geo-shape.html).
All other shapes will default to a type of `geo_shape`.
. Leave the default *Index name* and *Data view* names (the name of the uploaded
file minus its extension). You might need to change the index name if it is invalid.
. Click *Import file*.
Upon completing the indexing process and creating the associated data view,
the Elasticsearch responses are shown on the *Layer add panel* and the indexed data
appears on the map. The geospatial data on the map
should be identical to the locally-previewed data, but now it's indexed data from Elasticsearch.

. To continue adding data to the map, click *Add and continue*.
. In *Layer settings*, adjust any settings or properties as needed.
. Click *Keep changes*.
