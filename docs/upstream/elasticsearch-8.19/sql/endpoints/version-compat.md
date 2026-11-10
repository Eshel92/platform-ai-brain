<!-- Converted from sql/endpoints/version-compat.asciidoc (AsciiDoc). Includes are inlined. -->

Your driver must be compatible with your Elasticsearch version.

**Important:** The driver version cannot be newer than the Elasticsearch version.
For example, Elasticsearch version 7.10.0 is not compatible with {version} drivers.

|====
| Elasticsearch version
| Compatible driver versions
| Example

| 8.0.0–{version}
| * The same version
  * Any earlier 8.x version
  * Any 7.x version after 7.7.0.
| Elasticsearch {version} is compatible with {version} and earlier 8.x drivers. Elasticsearch {version} is also compatible with 7.7.0 and later 7.x drivers.

| 8.0.0
| * The same version
  * Any 7.x version after 7.7.0.
| Elasticsearch 8.0.0 is compatible with 8.0.0 drivers. Elasticsearch 8.0.0 is also
compatible with 7.7.0 and later 7.x drivers.

| 7.7.1-{prev-major-last}
| * The same version
  * An earlier 7.x version, back to 7.7.0.
| Elasticsearch 7.10.0 is compatible with 7.7.0-7.10.0 drivers.

| 7.7.1-{version}
| * The same version
  * An earlier 7.x version, back to 7.7.0.
| Elasticsearch 7.10.0 is compatible with 7.7.0-7.10.0 drivers.

| 7.7.0 and earlier versions
| * The same version.
| Elasticsearch 7.6.1 is only compatible with 7.6.1 drivers.
|====
