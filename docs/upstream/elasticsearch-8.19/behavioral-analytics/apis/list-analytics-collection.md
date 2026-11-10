<!-- Converted from behavioral-analytics/apis/list-analytics-collection.asciidoc (AsciiDoc). Includes are inlined. -->

### List Analytics Collections

beta::[]

**New API reference**
For the most up-to-date API details, refer to [Behavioral analytics APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-analytics).

Returns information about Behavioral Analytics Collections.

#### Request

`GET _application/analytics/<criteria>`

#### Prerequisites

Requires the `manage_behavioral_analytics` cluster privilege.

#### Path parameters

`<criteria>`::
(optional, string)
Criteria is used to find a matching analytics collection. This could be the name of the collection or a pattern to match multiple. If not specified, will return all analytics collections.

#### Response codes

`404`::
Criteria does not match any Analytics Collections.

#### Response codes

#### Examples

The following example lists all configured Analytics Collections:

```console
GET _application/analytics/
```

A sample response:

```console-result
{
  "my_analytics_collection": {
      "event_data_stream": {
          "name": "behavioral_analytics-events-my_analytics_collection"
      }
  },
  "my_analytics_collection2": {
      "event_data_stream": {
          "name": "behavioral_analytics-events-my_analytics_collection2"
      }
  }
}
```

The following example returns the Analytics Collection that matches `my_analytics_collection`:

```console
GET _application/analytics/my_analytics_collection
```

A sample response:

```console-result
{
  "my_analytics_collection": {
      "event_data_stream": {
          "name": "behavioral_analytics-events-my_analytics_collection"
      }
  }
}
```

The following example returns all Analytics Collections prefixed with `my`:

```console
GET _application/analytics/my*
```

A sample response:

```console-result
{
  "my_analytics_collection": {
      "event_data_stream": {
          "name": "behavioral_analytics-events-my_analytics_collection"
      }
  },
  "my_analytics_collection2": {
      "event_data_stream": {
          "name": "behavioral_analytics-events-my_analytics_collection2"
      }
  }
}
```
