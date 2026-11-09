<!-- Converted from tutorial/configure-public-api-access.txt (reStructuredText). Includes are inlined. -->

# Configure API Access

To access the Ops Manager API (Application Programming Interface), you must generate an API (Application Programming Interface) key for
programmatic access for an organization.

**Note:** API Keys can't use the Ops Manager Console

Organization-based API (Application Programming Interface) Keys aren't associated with user
credentials. You can't use these API (Application Programming Interface) Keys to log in to the Ops Manager
console.

## Prerequisite

### (Optional) Require an API Access List for Your Organization

Ops Manager allows your Ops Manager Administration API keys to make requests from
any address on the internet unless you require an IP access list for
the Ops Manager Administration API. If you require an IP access list, your API (Application Programming Interface)
keys can make API (Application Programming Interface) requests only from the location-based IP or CIDR (Classless Inter-Domain Routing)
addresses that you specify in the IP access list. 

Each API (Application Programming Interface) key has its own IP access list. If you require an IP
access list for all Ops Manager Administration API requests, you must define at
least one IP access list entry for an API (Application Programming Interface) key before you can use the 
API (Application Programming Interface) key.

When you create a new organization using the Ops Manager UI, Ops Manager enables
the API (Application Programming Interface) access list requirement by default. To disable the IP
access list requirement when you create an organization, toggle 
Require IP Access List for Ops Manager Administration API
to OFF when you create an organization.

To set your organization to require IP access lists for every 
Ops Manager Administration API key after organization creation, follow these steps:

1. Log into Ops Manager.

#. Access the Organization using the Context picker in
   the top-left hand corner of the Ops Manager UI.

#. Click Settings from the left hand navigation.

#. Toggle the Require IP Access List for Ops Manager Administration API
   setting to On.

## Manage Access to the API

You can set API Keys for an entire organization or project.
