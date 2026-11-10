<!-- Converted from rest-api/security/get-settings.asciidoc (AsciiDoc). Includes are inlined. -->

### Get Security index settings

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Retrieves settings for the security internal indices.

#### Prerequisites

* To use this API, you must have at least the `read_security` cluster privilege.

#### Description

This API allows a user to retrieve the user-configurable settings for the 
Security internal index (`.security` and associated indices). Only a subset of 
the index settings — those that are user-configurable—will be shown. This
includes:

- `index.auto_expand_replicas`
- `index.number_of_replicas`

#### Examples

An example of retrieving the security settings:

```console
GET /_security/settings
```

The configurable settings can be modified using the 
Update Security index settings API.
