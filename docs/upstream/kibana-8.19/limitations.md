<!-- Converted from limitations.asciidoc (AsciiDoc). Includes are inlined. -->

# Limitations

Following are the known limitations in Kibana.

### Nested objects

Kibana cannot perform aggregations across fields that contain nested objects.
It also cannot search on nested objects when Lucene Query Syntax is used in
the query bar.

==============================================
Using `include_in_parent` or `copy_to` as a workaround is not supported and may stop functioning in future releases.
==============================================
