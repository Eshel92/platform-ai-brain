<!-- Converted from api/synthetics/params/add-param.asciidoc (AsciiDoc). Includes are inlined. -->

## Add Parameters API

Adds one or more parameters to the synthetics app.

### Request

`POST <kibana host>:<port>/api/synthetics/params`

`POST <kibana host>:<port>/s/<space_id>/api/synthetics/params`

### Prerequisites

You must have `all` privileges for the *Synthetics* feature in the *Observability* section of the
Kibana feature privileges.

#### Request body

The request body can contain either a single parameter object or an array of parameter objects. The parameter object schema includes the following attributes:

`key`::
(Required, string) The key of the parameter.

`value`::
(Required, string) The value associated with the parameter.

`description`::
(Optional, string) A description of the parameter.

`tags`::
(Optional, array of strings) An array of tags to categorize the parameter.

`share_across_spaces`::
(Optional, boolean) Whether the parameter should be shared across spaces.

When adding a single parameter, provide a single object. When adding multiple parameters, provide an array of parameter objects.

#### Example

Here are examples of POST requests to add parameters, either as a single parameter or as an array of parameters:

To add a single parameter:

```sh
POST /api/synthetics/params
{
  "key": "your-key-name",
  "value": "your-parameter-value",
  "description": "Param to use in browser monitor",
  "tags": ["authentication", "security"],
  "share_across_spaces": true
}
```

To add multiple parameters:

```sh
POST /api/synthetics/params
[
  {
    "key": "param1",
    "value": "value1"
  },
  {
    "key": "param2",
    "value": "value2"
  }
]
```

The API returns a response based on the request. If you added a single parameter, it will return a single parameter object. If you added multiple parameters, it will return an array of parameter objects.

#### Response Example

The API response includes the created parameter(s) as JSON objects, where each parameter object has the following attributes:

- `id` (string): The unique identifier of the parameter.
- `key` (string): The key of the parameter.
- `value` (string): The value associated with the parameter.
- `description` (string, optional): The description of the parameter.
- `tags` (array of strings, optional): An array of tags associated with the parameter.
- `share_across_spaces` (boolean, optional): Indicates whether the parameter is shared across spaces.

Here's an example response for a single added parameter:

```json
{
  "id": "unique-parameter-id",
  "key": "your-key-name",
  "value": "your-param-value",
  "description": "Param to use in browser monitor",
  "tags": ["authentication", "security"],
  "share_across_spaces": true
}
```

And here's an example response for adding multiple parameters:

```json
[
  {
    "id": "param1-id",
    "key": "param1",
    "value": "value1"
  },
  {
    "id": "param2-id",
    "key": "param2",
    "value": "value2"
  }
]
```
