<!-- Converted from tutorial/manage-programmatic-api-keys.txt (reStructuredText). Includes are inlined. -->

# Programmatic Access to Ops Manager

To grant programmatic access to an organization or project using only
the API, you can create an API (Application Programming Interface) key. API (Application Programming Interface)
keys:

- Have two parts: a Public Key and a Private Key.
- Cannot be used to log into Ops Manager through the user interface.

- Must be granted roles as you would Users to make sure the API (Application Programming Interface) keys
  can call API (Application Programming Interface) endpoints without errors.

- Can belong to one organization, but may be granted access to
  any number of projects in that organization.

## Manage Programmatic Access to an Organization

**Note:** Required Permissions

To perform any of the following actions, you must have the
`Organization Owner` role.

### Create an API Key in an Organization

**Step 1: Navigate to the Access Manager page for your organization.**

a. If it is not already displayed, select your desired organization
   from the `office` Organizations menu in the
   navigation bar.

#. Click Access Manager in the sidebar, or click
   Access Manager in the navigation bar, then click
   your organization.

**Step 2: Click the API Keys tab.**

**Step 3: Click Create API Key.**

**Step 4: Complete the API Key Information form.**

From the API Key Information step of the
Add API Key page:

| Field | Value |
|---|---|
| Description | Enter a description for the new API (Application Programming Interface) Key. |
| Organization Permissions | Select the new role or roles for the API (Application Programming Interface) Key. |

**Step 5: Click Next.**

**Step 6: Add Access List Values for this API Key.**

From the Private Key & Access List step of the
Add API Key page, click Add Access List Entry.

For this API (Application Programming Interface) Key, You can choose to either:

- Enter an IPv4 (Internet Protocol version 4) address from which Ops Manager should accept API (Application Programming Interface)
  requests, or

- Click Use Current IP Address if the host you are using
  to access Ops Manager will make API (Application Programming Interface) requests.

**Step 7: Click Save.**

**Warning:** Copy the Private Key Before Leaving this Page

Ops Manager displays the Private Key once: *on this page*.
Click Copy to add the Private Key to the clipboard. Save
and secure this Private Key as you would any other password.

### View the Details of an API Key in an Organization

**Step 1: Navigate to the Access Manager page for your organization.**

a. If it is not already displayed, select your desired organization
   from the `office` Organizations menu in the
   navigation bar.

#. Click Access Manager in the sidebar, or click
   Access Manager in the navigation bar, then click
   your organization.

**Step 2: Click the API Keys tab.**

**Step 3: Navigate to View Details.**

a. Next to the API (Application Programming Interface) Key, click `ellipsis`.

b. Click View Details.

   The <Public Key> API Key Details modal displays the:

   - Obfuscated Private Key.
   - Date the Key was last used.
   - Date the Key was created.
   - IPv4 (Internet Protocol version 4) addresses on which the key is in the access list.
   - Projects to which the Key has been granted access.

### Change an API Key in an Organization

You can change the roles, description, or access list of an API (Application Programming Interface) Key in
an Organization.

**Step 1: Navigate to the Access Manager page for your organization.**

a. If it is not already displayed, select your desired organization
   from the `office` Organizations menu in the
   navigation bar.

#. Click Access Manager in the sidebar, or click
   Access Manager in the navigation bar, then click
   your organization.

**Step 2: Click the API Keys tab.**

**Step 3: Select the API Key to edit.**

a. Click the `ellipsis` next to the API (Application Programming Interface) Key you want to
   change.

b. Click Edit.

**Step 4: Complete the API Key Information form.**

From the API Key Information step of the
Add API Key page:

| Field | Value |
|---|---|
| Description | Enter a description for the new API (Application Programming Interface) Key. |
| Organization Permissions | Select the new role or roles for the API (Application Programming Interface) Key. |

**Step 5: Click Next.**

**Step 6: Add Access List Values for this API Key.**

From the Private Key & Access List step of the
Add API Key page, click Add Access List Entry.

For this API (Application Programming Interface) Key, You can choose to either:

- Enter an IPv4 (Internet Protocol version 4) address from which Ops Manager should accept API (Application Programming Interface)
  requests, or

- Click Use Current IP Address if the host you are using
  to access Ops Manager will make API (Application Programming Interface) requests.

**Step 7: Click Save.**

**Warning:** Copy the Private Key Before Leaving this Page

Ops Manager displays the Private Key once: *on this page*.
Click Copy to add the Private Key to the clipboard. Save
and secure this Private Key as you would any other password.

### Delete an API Key from an Organization

**Step 1: Navigate to the Access Manager page for your organization.**

a. If it is not already displayed, select your desired organization
   from the `office` Organizations menu in the
   navigation bar.

#. Click Access Manager in the sidebar, or click
   Access Manager in the navigation bar, then click
   your organization.

**Step 2: Click the API Keys tab.**

**Step 3: Delete the API Key.**

a. Click trash-alt next to the API (Application Programming Interface) Key that you want to
   delete.

b. Click Delete to confirm that you want to delete this
   API (Application Programming Interface) Key or Cancel to leave the key in the
   Organization.

**Note:**

Removing an API (Application Programming Interface) Key from an Organization also removes that key
from any projects to which the key was granted access.

## Manage Programmatic Access to a Project

**Note:** Required Permissions

To perform any of the following actions, you must have the
`Project User Admin` role.

### Create an API Key for a Project

**Step 1: Navigate to the Access Manager page for your project.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Project menu in the navigation bar.

#. Click Access Manager in the navigation bar, then click
   your project.

**Step 2: Click the API Keys tab.**

**Step 3: Click Create API Key.**

**Step 4: Complete the API Key Information form.**

From the API Key Information step of the
Add API Key page:

| Field | Value |
|---|---|
| Description | Enter a description for the new API (Application Programming Interface) Key. |
| Project Permissions | Select the new role or roles for the API (Application Programming Interface) Key. |

**Step 5: Click Next.**

**Step 6: Add Access List Values for this API Key.**

From the Private Key & Access List step of the
Add API Key page, click Add Access List Entry.

For this API (Application Programming Interface) Key, You can choose to either:

- Enter an IPv4 (Internet Protocol version 4) address from which Ops Manager should accept API (Application Programming Interface)
  requests, or

- Click Use Current IP Address if the host you are using
  to access Ops Manager will make API (Application Programming Interface) requests.

**Step 7: Click Save.**

**Warning:** Copy the Private Key Before Leaving this Page

Ops Manager displays the Private Key once: *on this page*.
Click Copy to add the Private Key to the clipboard. Save
and secure this Private Key as you would any other password.

### View the Details of an API Key in a Project

**Step 1: Navigate to the Access Manager page for your project.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Project menu in the navigation bar.

#. Click Access Manager in the navigation bar, then click
   your project.

**Step 2: Click the API Keys tab.**

**Step 3: Navigate to View Details.**

a. Next to the API (Application Programming Interface) Key, click `ellipsis`.

b. Click View Details.

   The <Public Key> API Key Details modal displays the:

   - Obfuscated Private Key.
   - Date the Key was last used.
   - Date the Key was created.
   - IPv4 (Internet Protocol version 4) addresses on which the key is in the access list.
   - Projects to which the Key has been granted access.

### Change an API Key's Roles in a Project

**Step 1: Navigate to the Access Manager page for your project.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Project menu in the navigation bar.

#. Click Access Manager in the navigation bar, then click
   your project.

**Step 2: Click the API Keys tab.**

**Step 3: Select the API Key to edit.**

a. Click the `ellipsis` next to the API (Application Programming Interface) Key you want to
   change.

b. Click Edit.

**Step 4: Complete the API Key Information form.**

From the API Key Information step of the
Add API Key page:

| Field | Value |
|---|---|
| Description | Enter a description for the new API (Application Programming Interface) Key. |
| Project Permissions | Select the new role or roles for the API (Application Programming Interface) Key. |

**Step 5: Click Next.**

**Step 6: Add Access List Values for this API Key.**

From the Private Key & Access List step of the
Add API Key page, click Add Access List Entry.

For this API (Application Programming Interface) Key, You can choose to either:

- Enter an IPv4 (Internet Protocol version 4) address from which Ops Manager should accept API (Application Programming Interface)
  requests, or

- Click Use Current IP Address if the host you are using
  to access Ops Manager will make API (Application Programming Interface) requests.

**Step 7: Click Save.**

**Warning:** Copy the Private Key Before Leaving this Page

Ops Manager displays the Private Key once: *on this page*.
Click Copy to add the Private Key to the clipboard. Save
and secure this Private Key as you would any other password.

### Delete an API Key from a Project

**Step 1: Navigate to the Access Manager page for your project.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Project menu in the navigation bar.

#. Click Access Manager in the navigation bar, then click
   your project.

**Step 2: Click the API Keys tab.**

**Step 3: Delete the API Key.**

a. Click trash-alt next to the API (Application Programming Interface) Key that you want to
   delete.

b. Click Delete to confirm that you want to delete this
   API (Application Programming Interface) Key or Cancel to leave the key in the
   Organization.

**Note:**

Removing an API (Application Programming Interface) Key from an Organization also removes that key
from any projects to which the key was granted access.
