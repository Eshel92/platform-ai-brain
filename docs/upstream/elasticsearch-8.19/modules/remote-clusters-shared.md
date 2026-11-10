<!-- Converted from modules/remote-clusters-shared.asciidoc (AsciiDoc). Includes are inlined. -->

|====
| 9+^h| Local cluster
h| Remote cluster     | 5.0–5.5    | 5.6        | 6.0–6.6    | 6.7        | 6.8        | 7.0        | 7.1–7.16   | 7.17       | 8.0–{minor-version}
| 5.0–5.5             | ✓ | ✓ | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗
| 5.6                 | ✓ | ✓ | ✓ | ✓ | ✓ | ✗  | ✗  | ✗  | ✗
| 6.0–6.6             | ✗  | ✓ | ✓ | ✓ | ✓ | ✗  | ✗  | ✗  | ✗
| 6.7                 | ✗  | ✓ | ✓ | ✓ | ✓ | ✓ | ✗  | ✗  | ✗
| 6.8                 | ✗  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗
| 7.0                 | ✗  | ✗  | ✗  | ✓ | ✓ | ✓ | ✓ | ✓ | ✗
| 7.1–7.16            | ✗  | ✗  | ✗  | ✗  | ✓ | ✓ | ✓ | ✓ | ✗
| 7.17                | ✗  | ✗  | ✗  | ✗  | ✓ | ✓ | ✓ | ✓ | ✓
| 8.0–{minor-version} | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✗  | ✓ | ✓
|====

**Note:** This documentation is for Elasticsearch version {version}, which is not yet
released. The above compatibility table applies if both clusters are running a
released version of Elasticsearch, or if one of the clusters is running a released
version and the other is running a pre-release build with a later build date. A
cluster running a pre-release build of Elasticsearch can also communicate with remote
clusters running the same pre-release build. Running a mix of pre-release
builds is unsupported and typically will not work, even if the builds have the
same version number.
