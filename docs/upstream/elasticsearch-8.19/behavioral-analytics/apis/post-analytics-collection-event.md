<!-- Converted from behavioral-analytics/apis/post-analytics-collection-event.asciidoc (AsciiDoc). Includes are inlined. -->

### Post Event to an Analytics Collection

beta::[]

**New API reference**
For the most up-to-date API details, refer to [Behavioral analytics APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-analytics).

Post an event to a Behavioral Analytics Collection.

#### Request

`POST _application/analytics/<collection_name>/event/<event_type>`

#### Path parameters

`<collection_name>`::
(Required, string) Analytics collection name you want to ingest event in.

`<event_type>`::
(Required, string) Analytics event type. Can be one of `page_view`, `search`, `search_click`.

#### Request body

Full request body parameters can be found in: behavioral-analytics-event-reference.

#### Prerequisites

Requires the `post_behavioral_analytics_event` cluster privilege.

#### Response codes

`202`::
Event has been accepted and will be ingested.

`404`::
Analytics Collection `<collection_name>` does not exists.

`400`::
Occurs either when the event type is unknown or when event payload contains invalid data.

#### Examples

The following example send a `search_click` event to an Analytics Collection called `my_analytics_collection`:

```console
POST _application/analytics/my_analytics_collection/event/search_click
{
  "session": {
    "id": "1797ca95-91c9-4e2e-b1bd-9c38e6f386a9"
  },
  "user": {
    "id": "5f26f01a-bbee-4202-9298-81261067abbd"
  },
  "search":{
    "query": "search term",
    "results": {
      "items": [
        {
          "document": {
            "id": "123",
            "index": "products"
          }
        }
      ],
      "total_results": 10
    },
    "sort": {
      "name": "relevance"
    },
    "search_application": "website"
  },
  "document":{
    "id": "123",
    "index": "products"
  }
}
```
