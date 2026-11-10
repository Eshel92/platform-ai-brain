<!-- Converted from setup/install/etc-elasticsearch.asciidoc (AsciiDoc). Includes are inlined. -->

The `/etc/elasticsearch` directory contains the default runtime configuration
for Elasticsearch. The ownership of this directory and all contained files are set to
`root:elasticsearch` on package installations.

The `setgid` flag applies group permissions on the `/etc/elasticsearch`
directory to ensure that Elasticsearch can read any contained files and subdirectories.
All files and subdirectories inherit the `root:elasticsearch` ownership.
Running commands from this directory or any subdirectories, such as the
elasticsearch-keystore tool, requires `root:elasticsearch`
permissions.

Elasticsearch loads its configuration from the
`/etc/elasticsearch/elasticsearch.yml` file by default. The format of this
config file is explained in settings.
