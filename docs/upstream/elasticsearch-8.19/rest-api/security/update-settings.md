<!-- Converted from rest-api/security/update-settings.asciidoc (AsciiDoc). Includes are inlined. -->

### Update Security index settings

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Updates the settings of the security internal indices.

#### Prerequisites

* To use this API, you must have at least the `manage_security` cluster privilege.

#### Request body

`security`::
(Optional, object) Settings to be used for the index used for most security
configuration, including Native realm users and roles configured via the API.

`security-tokens`::
(Optional, object) Settings to be used for the index used to store
tokens.

`security-profile`::
(Optional, object) Settings to be used for the index used to store
profile information.

#### Description

This API allows a user to modify the settings for the Security internal indices
(`.security` and associated indices). Only a subset of settings are allowed to
be modified. This includes:

- `index.auto_expand_replicas`
- `index.number_of_replicas`

**Note:** If `index.auto_expand_replicas` is set, `index.number_of_replicas` will be ignored during updates.

#### Examples

An example of modifying the Security settings:

```console
PUT /_security/settings
{
    "security": {
        "index.auto_expand_replicas": "0-all"
    },
    "security-tokens": {
        "index.auto_expand_replicas": "0-all"
    },
    "security-profile": {
        "index.auto_expand_replicas": "0-all"
    }
}
```

The configured settings can be retrieved using the
Get Security index settings API. If a given index
is not in use on the system, but settings are provided for it, the request will
be rejected - this API does not yet support configuring the settings for these
indices before they are in use.
