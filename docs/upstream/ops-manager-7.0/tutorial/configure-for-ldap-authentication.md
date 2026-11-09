<!-- Converted from tutorial/configure-for-ldap-authentication.txt (reStructuredText). Includes are inlined. -->

# Configure Ops Manager Users for LDAP Authentication and Authorization

## Overview

You can use a Lightweight Directory Access Protocol (LDAP) service to
manage Ops Manager user authentication and authorization. Users log in
through Ops Manager, then Ops Manager searches the LDAP directory for the user and
synchronizes the user's name and email addresses in the Ops Manager user
records with the values in the LDAP user records.

To configure Ops Manager to use LDAP, go to: Admin >
General > Ops Manager Config > User
Authentication.

**Note:**

This tutorial describes authenticating users of the Ops Manager web
interface.

If your MongoDB deployments **also** use LDAP (Lightweight Directory Access Protocol), you must separately
create MongoDB users for the MongoDB Agents, as described in
/tutorial/configure-mongodb-agent-for-ldap.

This tutorial describes how to:

* Configure LDAP authentication for Ops Manager

* Map LDAP groups to both Ops Manager organization-roles and
  project-roles
  

### User Authentication

When a user attempts to log in, Ops Manager searches for a matching user and
the user's groups using an LDAP query.

- Ops Manager logs into LDAP as the `search` user, using the credentials
  specified in the LDAP Bind Dn and LDAP Bind
  Password fields.

- Ops Manager searches under the base distinguished name specified in
  the LDAP User Base Dn field and matches the user
  according to the LDAP attribute specified in the LDAP User
  Search Attribute field.

- Ops Manager searches under the base distinguished name specified in the
  LDAP Group Base Dn field and matches the user's groups
  according to the LDAP attribute specified in the LDAP Group
  Member Attribute field. If no value is provided for the LDAP
  Group Base Dn, Ops Manager uses the value of LDAP User Base Dn
  to search for LDAP group memberships.

- If a matching user is found, Ops Manager authenticates the supplied
  password against the LDAP password for the provided user.

### Authorization/Access Control

LDAP groups let you control access to Ops Manager. You associate LDAP groups
with organization and project Ops Manager roles and assign the LDAP groups
to the users who should have those roles.

LDAP entries map to Ops Manager records as follows: 

| LDAP | Ops Manager |
|---|---|
| User | User |
| Group | Organization/Project Role |

To use LDAP groups effectively, 
create additional projects
within Ops Manager to control access to specific deployments in your
organization, such as creating separate Ops Manager projects for development
and production environments. You can then map an LDAP group to a role
in the Ops Manager project to provide access to a deployment.

**Note:**

- Changes made to LDAP groups can take up to an hour to take effect 
  in Ops Manager. Changes take effect immediately for users in affected 
  groups when they log out and log back in to Ops Manager.

- If an LDAP user does not belong to any LDAP group, Ops Manager does not
  assign any roles, organization or project, to the user.

- If an LDAP user is assigned a project role but no organization role,
  Ops Manager automatically assigns the user the Organization Member
  Role.

If you have multiple departments with their own billing needs, alert settings,
and project members, create a new organization
for each department.

### LDAP Over SSL

If you use LDAP over an SSL connection (LDAPS), complete these fields:

| Field | Needed Value |
|---|---|
| LDAP SSL CA File | The path to a PEM key file for a trusted certificate authority. |
| LDAP SSL PEM Key File | The path to a PEM key file containing a client certificate and private key. |
| LDAP SSL PEM Key File Password | The password to decrypt it if the LDAP SSL PEM Key File is encrypted. |

## Prerequisites

The LDAP server must:

- Be installed, configured and accessible to Ops Manager.

- Embed each user's group memberships as an attribute of each user's
  LDAP Entry.

  **Important:**

  Use the `member` LDAP user attribute if you want to include
  nested LDAP groups in Ops Manager group memberships. 

  For example, if LDAP user `jsmith` belongs to LDAP group `B` and LDAP Group `B` belongs
  to LDAP group `A`, then Ops Manager recognizes `jsmith` as a member of groups `A` and `B`.

- Include a user that can search the base DN (Distinguished Name) that includes Ops Manager users
  and groups.

- Include a group for `Global Owners`.

  - You **must** enter this group into the LDAP Global Role
    Owner field when you configure LDAP in
    Ops Manager.

    **Example:**

    If LDAP has an `admin` group for use by Ops Manager administrators,
    enter `admin` in the LDAP Global Role Owner field.

  - After you enable LDAP authentication, you **must** first log in to
    Ops Manager as a user who belongs to this group to create the initial
    Ops Manager project (if applicable) and map LDAP groups to
    project and organization roles.

    **Important:**

    Once Ops Manager is converted to LDAP Authentication, only the user with
    the Global Owner role who changes the authentication method remains
    logged in. All other users are logged out and need to log
    back in to Ops Manager using their LDAP username and password. Users
    without an LDAP username and password can no longer log in to Ops Manager.

## Procedure

To configure LDAP authentication:

**Step 1: Define your user records in the LDAP system of your choice.**

To find a description of standard LDAP object classes and attribute
types, see Lightweight Directory Access Protocol Schema for
User Applications.

**Step 2: Navigate to the User Authentication tab of the Ops Manager Config page.**

a. Click Admin link at the upper right corner of the
   page.

b. Click the General tab.

c. Click the Ops Manager Config page.

d. Click User Authentication tab.

**Step 3: Type LDAP configuration settings.**

a. Enter values for the following **required LDAP configuration** fields:

   | Field | Action | Example |
   |---|---|---|
   | User Authentication Method | Select LDAP. | `LDAP` |
   | LDAP URI | Type the hostname and port of the LDAP server. If you are using multiple LDAP servers for load balancing, separate each URI with a space. Each LDAP server must be a replica of the others or Ops Manager LDAP authentication won't work as expected. IMPORTANT: Ops Manager does not support hostnames that contain an underscore character (`_`) in the LDAP URI field. | `ldap://ldap.example.com:389` |
   | LDAP SSL CA File | Type the path to a PEM key file containing the certificate for the CA who signed the certificate used by the LDAPS server. This optional field is used by the Ops Manager application to verify the identify of the LDAPS server and prevent man-in- the-middle Attacks. If this configuration is not provided, Ops Manager uses the default root CA certificate bundle that comes with the Java Runtime Environment (JRE). If your LDAPS server certificate cannot be verified by a root CA (i.e. if it is self-signed), requests to the LDAPS server fail. | `/opt/cert/ca.pem` |
   | LDAP SSL PEM Key File | Type the path to a PEM key file containing a client certificate and private key. This field is optional and should be used only if your LDAPS server requires client certificates be passed by client applications. This is used to sign requests sent from the Ops Manager application server to the LDAPS server. This allows the LDAPS server to verify the identify of Ops Manager application server. | `/opt/cert/ldap.pem` |
   | LDAP SSL PEM Key File Password | Type the password that decrypts the LDAP SSL PEM Key File. If your client certificates specified in the LDAP SSL PEM Key File field are required by the LDAPS server and if the client certificate specified in LDAP SSL PEM Key File is stored encrypted on the file system, this field is required. | `<encrypted-password>` |
   | LDAP Bind Dn | Type a credentialed user on the LDAP server that can conduct searches for users. | `cn=admin, dc=example, dc=com` |
   | LDAP Bind Password | Type the password for the Bind Dn user on the LDAP server. | `<password>` |
   | LDAP User Base Dn | Type the Distinguished Name that Ops Manager uses to search for users on the LDAP server. | `dc=example, dc=com` |
   | LDAP User Search Attribute | Type the LDAP field in the LDAP server that specifies the username. | `uid` |
   | LDAP Group Base Dn | Type the Distinguished Name that Ops Manager uses to search for groups on the LDAP server. | `ou=othergroups, dc=example, dc=com` |
   | LDAP Group Member Attribute | Type the LDAP group attribute that specifies the list of LDAP users who belong to that group. | `member` |
   | LDAP User Group | Type the LDAP user attribute that specifies the LDAP groups to which the user belongs. The LDAP attribute can use any format to list the groups, including Common Name (`cn`) or Distinguished Name (`dn`). All Ops Manager settings that specify groups must match the chosen format. | `memberOf` |
   | LDAP Global Role Owner | Type the LDAP group to which Ops Manager Global Owners belong. | `cn=global-owner, ou=groups, dc=example, dc=com` |

   **Note:**

   Each Global Role group provides the members of its associated
   LDAP group or groups with an Ops Manager global role. Global roles provide access to all the Ops Manager
   projects in the Ops Manager deployment.

b. Type values for the following **Optional LDAP Configuration**
   fields if needed.

   **Important:**

   You must use the fully qualified distinguished name for each
   group. If multiple LDAP or SAML groups correspond to the same role,
   separate them with two semicolons (`;;`). Remove a group
   from a role's field to revoke the group's access for that
   role.

   | Field | Action |
   |---|---|
   | LDAP User First Name | Type the attribute of LDAP users that specifies the user's first name. |
   | LDAP User Last Name | Type the attribute of LDAP users that specifies the user's last name. |
   | LDAP User Email | Type the attribute of LDAP users that specifies the user's email address. |
   | LDAP Global Role Automation Admin | Type the LDAP group(s) to which Ops Manager Global Automation Administrators belong. You can type multiple LDAP groups into this field if they are separated by two semicolons (`;;`). |
   | LDAP Global Role Backup Admin | Type the LDAP group(s) to which Ops Manager Global Backup Administrators belong. You can type multiple LDAP groups into this field if they are separated by two semicolons (`;;`). |
   | LDAP Global Role Monitoring Admin | Type the LDAP group(s) to which Ops Manager Global Monitoring Administrators belong. You can type multiple LDAP groups into this field if they are separated by two semicolons (`;;`). |
   | LDAP Global Role User Admin | Type the LDAP group(s) to which the Ops Manager Global User Administrators belong. You can type multiple LDAP groups into this field if they are separated by two semicolons (`;;`). |
   | LDAP Global Role Read Only | Type the LDAP group(s) to which Ops Manager Global Read Only Users belong. You can type multiple LDAP groups into this field if they are separated by two semicolons (`;;`). |

**Step 4: Click Save.**

**Step 5: Log in as a global owner.**

Log into Ops Manager as an LDAP user that is part of the LDAP group
specified in the Ops Manager LDAP Global Role Owner field.

Upon successful login, Ops Manager displays your projects page.

**Step 6: Associate LDAP groups with project roles.**

**Note:**

You must have any global role
to create a new project.

a. Click Admin > General > Projects.

#. Click Create a New Project.

#. In Project Name, type a name for the new Ops Manager project.

#. Enter the LDAP groups that correspond to
   each project role.

   **Important:**

   You must use the fully qualified distinguished name for each
   group. If multiple LDAP or SAML groups correspond to the same role,
   separate them with two semicolons (`;;`). Remove a group
   from a role's field to revoke the group's access for that
   role.

#. Click Add Project.

a. Click Admin > General > Projects.

#. In the Actions column for a project, click
   `ellipsis`, then click
   Edit LDAP Settings.

#. Enter the LDAP groups that correspond to each project
   role. 

   **Important:**

   You must use the fully qualified distinguished name for each
   group. If multiple LDAP or SAML groups correspond to the same role,
   separate them with two semicolons (`;;`). Remove a group
   from a role's field to revoke the group's access for that
   role.

#. Click Save Changes.

**Step 7: Associate LDAP groups with organization roles.**

**Note:**

You must have any global role
to create a new organization.

a. Click Admin > General > Organizations.

#. Click Create a New Organization.

#. In Organization Name, type a name for the new Ops Manager organization.

#. Enter the LDAP groups that correspond to
   each organization role.

   **Important:**

   You must use the fully qualified distinguished name for each
   group. If multiple LDAP or SAML groups correspond to the same role,
   separate them with two semicolons (`;;`). Remove a group
   from a role's field to revoke the group's access for that
   role.

#. Click Add Organization.

a. Click Admin > General > Organizations.

b. Click the Edit Org button.

c. Enter the LDAP groups that correspond to
   each organization role.

   **Important:**

   You must use the fully qualified distinguished name for each
   group. If multiple LDAP or SAML groups correspond to the same role,
   separate them with two semicolons (`;;`). Remove a group
   from a role's field to revoke the group's access for that
   role.

#. Click Save Changes.

**Step 8: Add your MongoDB deployments.**

Specify the LDAP authentication settings when adding a MongoDB
deployment.

## Troubleshooting

Ops Manager enables endpoint detection by default in the JDK (Java Development Kit). You must use
trusted server certificates for your Ops Manager hosts.

If you can't use trusted certificates:

1. Disable endpoint identification. Add the
   `-Dcom.sun.jndi.ldap.object.disableEndpointIdentification=true` to
   the `JAVA_MMS_UI_OPTS` property in the `mms.conf`.
2. Restart all Ops Manager services after this change.

**Warning:**

Disabling this functionality impacts Ops Manager security. You should
configure a valid and trusted certificate instead.
