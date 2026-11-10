<!-- Converted from api/synthetics/private-locations/delete-private-location.asciidoc (AsciiDoc). Includes are inlined. -->

## Delete Private Location API

Deletes a private location using the provided location ID.

### Request

`DELETE <kibana host>:<port>/api/synthetics/private_locations/<location_id>`

`DELETE <kibana host>:<port>/s/<space_id>/api/synthetics/private_locations/<location_id>`

### Prerequisites

You must have `all` privileges for the *Synthetics and Uptime* feature in the *Observability* section of the
Kibana feature privileges.

#### Path Parameters

`location_id`::
(Required, string) The unique identifier of the private location to be deleted. It must be between 1 and 1024 characters.

#### Example

Here is an example of a DELETE request to delete a private location:

```sh
DELETE /api/private-locations/<location_id>
```

The API does not return a response body for deletion, but it will return an appropriate status code upon successful deletion.

This API will delete the private location with the specified `locationId`.

A location cannot be deleted if it has associated monitors in use. You must delete all monitors associated with the location before deleting the location.
