<!-- Converted from admin/general/global-access-list-page.txt (reStructuredText). Includes are inlined. -->

# Global Access List

This page lists the Global Access List Entries configured for the
Ops Manager instance. Each entry represents a host IP or CIDR (Classless Inter-Domain Routing) block from
which Ops Manager accepts incoming API (Application Programming Interface) requests. You can search for a
access list entry, add access list entries, and edit or delete existing
access list entries.

**Note:**

Ops Manager limits all actions in this section to users or Global API (Application Programming Interface)
Keys that were granted the `Global Owner` role.

## Add an Access List Entry

1. Click Add Access List Entry to open the
   Add Global Access List Entry modal.

#. Set all values in the access list form:

   |  |  |
   |---|---|
   | Access List Entry | Type the IPv4 (Internet Protocol version 4) address, IPv6 (Internet Protocol version 6) address, or CIDR (Classless Inter-Domain Routing) block that you want to allow to use the Ops Manager API (Application Programming Interface). You can click Use Current IP Address to add the public IP address of the host you are using to access Ops Manager. |
   | Description | Type the purpose this IP address serves. |

#. Click Add Entry if this global access list entry is
   correct. Click Cancel to close the modal without adding
   a new access list entry.

## Edit an Access List Entry

**Warning:**

Once saved, any changes to this value impact applications that
require the previous access list entry.

1. To the right of the access list entry that you want to edit, click
   `ellipsis` then select Edit Access List Entry to
   open the Edit Global Access List Entry modal. Ops Manager
   displays the IPv4 (Internet Protocol version 4) address, IPv6 (Internet Protocol version 6) address, or CIDR (Classless Inter-Domain Routing) block for
   this access list entry in the modal.

#. Change the values in the access list form as needed:

   |  |  |
   |---|---|
   | Access List Entry | Type the  IPv4 (Internet Protocol version 4) address, IPv6 (Internet Protocol version 6) address, or CIDR (Classless Inter-Domain Routing) block that you want to allow to use the Ops Manager API (Application Programming Interface). You can click Use Current IP Address to add the public IP address of the host you are using to access Ops Manager. |
   | Description | Type the purpose this IP address serves. |

#. Click Save Entry if you made changes to your global
   access list entry. Click Cancel to close the modal without
   editing the access list entry.

   It might take up to an hour for the changes to take effect. Ops Manager
   returns an error if you send an API (Application Programming Interface) request before the changes take 
   effect. 

## Delete an Access List Entry

**Warning:**

Deleting a Global Access List Entry impacts applications that require
that access list entry, unless another access list entry includes that
address. If no entries cover the application address, the
application cannot access the API (Application Programming Interface).

1. To the right of the access list entry that you want to delete, click
   `ellipsis` then select Delete Access List Entry.

   The Delete Global Access List Entry modal displays.

#. Type the entry's  IPv4 (Internet Protocol version 4) address, IPv6 (Internet Protocol version 6) address, or CIDR (Classless Inter-Domain Routing) block in
   the box to confirm that you want to delete this entry.

#. Click Delete if you want to delete your global
   access list entry. Click Cancel to close the modal without
   deleting the access list entry.
