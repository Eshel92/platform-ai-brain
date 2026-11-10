<!-- Converted from settings/spaces-settings.asciidoc (AsciiDoc). Includes are inlined. -->

### Spaces settings in Kibana

By default, spaces is enabled in Kibana. To secure spaces, enable security.

`xpack.spaces.maxSpaces`::
The maximum number of spaces that you can use with the Kibana instance. Some Kibana operations
return all spaces using a single `_search` from Elasticsearch, so you must
configure this setting lower than the `index.max_result_window` in Elasticsearch.
The default is `1000`.

`xpack.spaces.defaultSolution`::
Sets the solution view for your default space.
