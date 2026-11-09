<!-- Converted from tutorial/nav/host-mappings.txt (reStructuredText). Includes are inlined. -->

# Host Mappings

Host mappings are based on the data that the Monitoring
retrieves on a regular interval. Ops Manager regenerates the entries on the
Host Mappings page after each retrieval.

Host mappings are displayed in three-column rows:

| Column | Content |
|---|---|
| Host | The preferred hostname and port for the deployment. |
| Alias | One alternative hostname or address and port for the deployment. |
| Last Updated | The timestamp when the host mapping was updated. |

If a host has multiple aliases, each mapping of host to alias is 
listed in its own row.

## Preferred Hostnames

The preferred hostname also appears in the Name column of
the Deployment page. This hostname can be a hostname, an
FQDN (fully qualified domain name), an IPv4 (Internet Protocol version 4) address, or an IPv6 (Internet Protocol version 6) address. If you want a
different preferred hostname than what Ops Manager chose, regenerate the list
of mappings in one of the following ways:

* Specify constraints on how Ops Manager picks a preferred hostname. For
  more information, see Preferred Hostnames in
  /tutorial/manage-project-settings.

* Reset the mapping list. For more information, see
  Reset Duplicates in
  /tutorial/manage-project-settings.

**Important:**

Resetting duplicates and setting constraints on the selection of a
preferred hostname cause Ops Manager to lose the monitoring history for
affected hosts. Chart data based on this history is also lost.

  

## Aliases

Depending on what Ops Manager obtains from a monitored host, the alias may be
in any one of the following forms:

* Fully qualified domain name (FQDN)

* Internal hostname

* External IPv4 (Internet Protocol version 4) or IPv6 (Internet Protocol version 6) address

* Internal IPv4 (Internet Protocol version 4) or IPv6 (Internet Protocol version 6) address

**Important:**

To prevent naming conflicts, Ops Manager does not use `localhost` or
similar local designations for new or remapped hosts unless no
other hostname option is possible.
