<!-- Converted from behavioral-analytics/apis/put-analytics-collection.asciidoc (AsciiDoc). Includes are inlined. -->

### Put Analytics Collection

beta::[]

**New API reference**
For the most up-to-date API details, refer to [Behavioral analytics APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-analytics).

Creates a Behavioral Analytics Collection.

#### Request

`PUT _application/analytics/<name>`

#### Path parameters

`<name>`::
(Required, string)

#### Prerequisites

Requires the `manage_behavioral_analytics` cluster privilege.

#### Response codes

`400`::
Analytics Collection `<name>` exists.

#### Examples

The following example creates a new Analytics Collection called `my_analytics_collection`:

```console
PUT _application/analytics/my_analytics_collection
```
