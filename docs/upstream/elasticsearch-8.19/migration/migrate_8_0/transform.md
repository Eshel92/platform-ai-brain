<!-- Converted from migration/migrate_8_0/transform.asciidoc (AsciiDoc). Includes are inlined. -->

#### Transform changes

.Transforms created in 7.4 or earlier versions must be upgraded.
*Details* +
Early beta versions of transforms had configuration information in a format
that is no longer supported.

*Impact* +
Use the [upgrade transforms API](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/upgrade-transforms.html) to fix your
transforms. This upgrade does not affect the source or destination indices.
