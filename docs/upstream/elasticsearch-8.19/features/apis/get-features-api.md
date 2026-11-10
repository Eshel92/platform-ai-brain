<!-- Converted from features/apis/get-features-api.asciidoc (AsciiDoc). Includes are inlined. -->

### Get Features API

**New API reference**
For the most up-to-date API details, refer to [Features APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-features).

Gets a list of features which can be included in snapshots using the
`feature_states` field when creating a
snapshot.

```console
GET /_features
```

#### Request

`GET /_features`

#### Description

You can use the get features API to determine which feature states
to include when taking a snapshot. By default, all
feature states are included in a snapshot if that snapshot includes the global
state, or none if it does not.

A feature state includes one or more system indices necessary for a given
feature to function. In order to ensure data integrity, all system indices that
comprise a feature state are snapshotted and restored together.

The features listed by this API are a combination of built-in features and
features defined by plugins. In order for a feature's state to be listed in this
API and recognized as a valid feature state by the create snapshot API, the
plugin which defines that feature must be installed on the master node.

#### Examples

```console-result
{
    "features": [
        {
            "name": "tasks",
            "description": "Manages task results"
        },
        {
            "name": "kibana",
            "description": "Manages Kibana configuration and reports"
        }
    ]
}
```
