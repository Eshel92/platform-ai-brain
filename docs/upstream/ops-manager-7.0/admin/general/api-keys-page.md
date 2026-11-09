<!-- Converted from admin/general/api-keys-page.txt (reStructuredText). Includes are inlined. -->

# API Keys Page

This page lists the available Global API (Application Programming Interface) Keys for this Ops Manager
instance. You can:

- Search for an API (Application Programming Interface) Key,
- Add new API (Application Programming Interface) Keys,
- Edit existing API (Application Programming Interface) Keys, or
- Delete existing API (Application Programming Interface) Keys.

**Note:**

Ops Manager limits all actions in this section to users or Global API (Application Programming Interface)
Keys that were granted the `Global Owner` role.

## Add a Global API (Application Programming Interface) Key

1. Click Create API Key to open the Add API Key
   page.

#. At the Enter API Key Information step, set both required
   values in the Global API (Application Programming Interface) Key form:

   |  |  |
   |---|---|
   | Description | Type the purpose this Global API (Application Programming Interface) Key serves. This description can't be longer than 250 characters. |
   | Global Permissions | Select the new role or roles to be assigned to the API (Application Programming Interface) Key. |

   Ops Manager generates the Public Key at this step.

#. Click Next.

#. At the Private Key step, click the Copy
   button to add the Private Key to the clipboard. Save and secure this
   Private Key as you would any other password. To use your Global
   API (Application Programming Interface) Key with the Ops Manager API (Application Programming Interface), you need both the public key, which
   serves as a username, and the private key, which serves as a
   password.

   **Warning:**

   Copy your full private key at this point. Store it in a secure
   location. Ops Manager doesn't and can't display the full private key
   after you leave this page.

#. To add an access list entry, click
   Go to Global Access List.

#. Click Done.

## Edit a Global API (Application Programming Interface) Key

**Warning:**

Once saved, any changes to these permissions impact applications
that use this Global API (Application Programming Interface) Key.

1. To the right of the Global API (Application Programming Interface) Key that you want to edit, click
   `ellipsis` then select Edit API Key to open
   the Edit Global API Key modal. Ops Manager displays the
   Public Key in this modal.

#. Change the values in the Global API (Application Programming Interface) Key form as needed:

   |  |  |
   |---|---|
   | Description | Type the purpose this Global API (Application Programming Interface) Key serves. This description can't be longer than 250 characters. |
   | Global Permissions | Select the new role or roles to be assigned to the API (Application Programming Interface) Key. |

#. Click Save if you made changes to your Global API (Application Programming Interface)
   Key. Click Cancel to close the page without editing the
   Global API (Application Programming Interface) Key.

## Delete a Global API (Application Programming Interface) Key

**Warning:**

Deleting a Global API (Application Programming Interface) Key might impact applications that use that
key.

1. To the right of the Global API (Application Programming Interface) Key that you want to delete, click
   `ellipsis` then select Delete API Key to open
   the Delete Global API Key modal.

#. Type the public key for the Global API (Application Programming Interface) Key in the box to confirm
   that you want to delete this key.

#. Click Delete to delete your Global API (Application Programming Interface)
   Key. Click Cancel to close the modal without deleting
   the Global API (Application Programming Interface) Key.
