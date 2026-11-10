<!-- Converted from search-application/apis/delete-search-application.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete Search Application

**New API reference**
For the most up-to-date API details, refer to [Search application APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-search_application).

beta::[]

Removes a Search Application and its associated alias.
Indices attached to the Search Application are not removed.

#### Request

`DELETE _application/search_application/<name>`

#### Prerequisites

Requires the `manage_search_application` cluster privilege.
Also requires manage privileges on all indices that are included in the Search Application.

#### Path parameters

`<name>`::
(Required, string)

#### Response codes

`400`::
The `name` was not provided.

`404` (Missing resources)::
No Search Application matching `name` could be found.

#### Examples

The following example deletes the Search Application named `my-app`:

```console
DELETE _application/search_application/my-app/
```
