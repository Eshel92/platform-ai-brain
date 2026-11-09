<!-- Converted from reference/api/access-list.txt (reStructuredText). Includes are inlined. -->

# Access List

**Note:**

The `whitelist` resource is deprecated for Ops Manager 5.0 and later. 
Use the `accessList` resource instead to control access to 
API operations.

The `accessList` resource lets you retrieve and update a user's
access list, which controls the user's
access to API operations. Users can issue API
operations only from addresses on their own access list. To use the 
`accessList` resource you must know the unique identifier of the user who owns
the access list. To retrieve a user's ID, see api-get-all-users-in-group.

The `accessList` resource's `POST` and `DELETE` operations are 
in the access list themselves. They must originate from an address already on 
the user's access list.

You can retrieve access list information only for the user issuing the request.
The **USER-ID** in the URL *must* match the ID of the user associated with the
`public API key` used to send the request.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Endpoints

The following endpoints are available for `hosts`.

| Method | Endpoint | Description |
|---|---|---|
| GET | /users/{USER-ID}/accessList | Retrieves the access list for the current user. |
| GET | /users/{USER-ID}/accessList/{IP-ADDRESS} | Retrieves the access list for the specified IP address. |
| POST | /users/{USER-ID}/accessList/{IP-ADDRESS} | Adds entries to the access list for the current user. |
| DELETE | /users/{USER-ID}/accessList/{IP-ADDRESS} | Deletes an entry from the access list for the current user. |
