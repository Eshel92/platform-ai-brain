<!-- Converted from api/synthetics/private-locations/create-private-location.asciidoc (AsciiDoc). Includes are inlined. -->

## Create Private Location API

Creates a private location with the following schema.

### Request

`POST <kibana host>:<port>/api/synthetics/private_locations`

`POST <kibana host>:<port>/s/<space_id>/api/synthetics/private_locations`

### Prerequisites

You must have `all` privileges for the *Synthetics and Uptime* feature in the *Observability* section of the
Kibana feature privileges.

#### Request body

The request body should contain the following attributes:

`label`::
(Required, string) A label for the private location.

`agentPolicyId`::
(Required, string) The ID of the agent policy associated with the private location.

`tags`::
(Optional, array of strings) An array of tags to categorize the private location.

`geo`::
(Optional, object) Geographic coordinates (WGS84) for the location. It should include the following attributes:

- `lat` (Required, number): The latitude of the location.
- `lon` (Required, number): The longitude of the location.

`spaces`::
(Optional, array of strings) An array of space IDs where the private location is available. If not provided, the private location is available in all spaces, the API will throw an error if user
does not have access to all spaces. In that case you can provide the space ID where the private location should be available.

#### Example

Here is an example of a POST request to create a private location:

```sh
POST /api/private_locations
{
  "label": "Private Location 1",
  "agentPolicyId": "abcd1234",
  "tags": ["private", "testing"],
  "geo": {
    "lat": 40.7128,
    "lon": -74.0060
  }
  "spaces": ["default"]
}
```

The API returns the created private location as follows:

```json
{
  "id": "abcd1234",
  "label": "Private Location 1",
  "agentPolicyId": "abcd1234",
  "tags": ["private", "testing"],
  "geo": {
    "lat": 40.7128,
    "lon": -74.0060
  }
}
```

If the `agentPolicyId` is already used by an existing private location, or if the `label` already exists, the API will return a `400 Bad Request` response with a corresponding error message.
