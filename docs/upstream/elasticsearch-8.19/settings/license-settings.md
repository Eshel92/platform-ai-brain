<!-- Converted from settings/license-settings.asciidoc (AsciiDoc). Includes are inlined. -->

### License settings

You can configure this licensing setting in the `elasticsearch.yml` file.
For more information, see
[License management](https://www.elastic.co/guide/en/kibana/8.19/managing-licenses.html).

`xpack.license.self_generated.type`::
(Static)
Set to `basic` (default) to enable basic X-Pack features. +
If set to `trial`, the self-generated license gives access only to all the features
of a x-pack for 30 days. You can later downgrade the cluster to a basic license if
needed.
