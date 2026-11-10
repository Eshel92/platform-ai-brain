<!-- Converted from api/synthetics/params/edit-param.asciidoc (AsciiDoc). Includes are inlined. -->

## Edit Parameter by ID API

Edits a parameter with the specified ID.

### Request

`PUT <kibana host>:<port>/api/synthetics/params`

`PUT <kibana host>:<port>/s/<space_id>/api/synthetics/params`

### Prerequisites

You must have `all` privileges for the *Synthetics* feature in the *Observability* section of the
Kibana feature privileges.

#### Path Parameters

`id`::
(Required, string) The unique identifier of the parameter to be edited.

#### Request body

The request body can contain the following attributes, it can't be empty at least one attribute is required.:

`key`::
(Optional, string) The key of the parameter.

`value`::
(Optional, string) The updated value associated with the parameter.

`description`::
(Optional, string) The updated description of the parameter.

`tags`::
(Optional, array of strings) An array of updated tags to categorize the parameter.

#### Example

Here is an example of a PUT request to edit a parameter by its ID:

```sh
PUT /api/synthetics/params/param_id1
{
  "key": "updated_param_key",
  "value": "updated-param-value",
  "description": "Updated Param to be used in browser monitor",
  "tags": ["authentication", "security", "updated"]
}
```

The API returns the updated parameter as follows:

```json
{
  "id": "param_id1",
  "key": "updated_param_key",
  "value": "updated-param-value",
  "description": "Updated Param to be used in browser monitor",
  "tags": ["authentication", "security", "updated"]
}
```
