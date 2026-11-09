<!-- Converted from tutorial/manage-organizations.txt (reStructuredText). Includes are inlined. -->

# Manage Organizations

An organization can contain multiple projects. Under this hierarchy structure, you can:

- Use the same alert settings across all projects in your organization.

- View all projects within an organization.

- Bulk assign users to projects with teams.

## Create an Organization

**Note:**

When you create an organization, you are added as an
`Organization Owner` for the organization.

**Step 1: View all of your organizations.**

a. Expand the Organizations menu in the navigation bar.
b. Click View All Organizations.

**Step 2: Click New Organization.**

**Step 3: Provide a name and default server type for your Organization.**

* - Name
  - Enter the name for this organization.
* - Default Organization Server Type
  - Select the default server type to be suggested when a new
    project is created under this organization.

    You can change the server type for individual hosts.

    You can override this default setting for any project
    when you create a new project or
    modify an existing project.

    * - Server Intention
      - Environment Purpose
      - License Requirement

    * - Production Server
      - Hosts your application to your internal or external end users.

        If an end user might use an environment, it functions as a
        Production environment. This applies whether the environment
        also provides testing, quality assurance, evaluation, or
        development capabilities.

      - One license per server

    * - Test/QA Server
      - This type of environment can be used to:

        |  |  |
        |---|---|
        | Test | Exercises your application to verify that it works as designed and expected. The platform configuration might be a less performant version of Production in compute, network, and storage capability. |
        | Assure system quality | Validates your application against a combination of data, hardware, and software configured to simulate Production. The platform configuration should be a smaller scale of Production in compute, network, and storage capability. |
        | Stage | Simulates the Production environment including performance testing and release candidate approval. The platform configuration should mirror Production in compute, network, and storage capability. |

      - One license per server

    * - Development Server
      - Hosts in progress design, code, debugging or some combination
        thereof for your application. Used to evaluate if the current
        state of your application can be promoted to another
        environment.
      - None

    * - RAM Pool
      - Provides any combination of servers for any environment purpose.
      - One license for any number of servers up to the maximum of
        the total GB of RAM you purchased across these servers.

    |  |  |  |
    |---|---|---|
    | Backing Database | Hosts your Ops Manager backing database. enable-application-database-monitoring to enable this option. | None |

**Step 4: Add members to your organization.**

a. For existing Ops Manager users, enter their username. Usually, this is
   the email the person used to register.

b. For new Ops Manager users, enter their email address to send an
   invitation.

**Step 5: Specify the access you want to grant the organization members.**

**Step 7: (Optional) Disable the IP access list requirement for the Ops Manager Administration API.**

When you create a new organization, Ops Manager requires IP access
lists for the Ops Manager Administration API by default. If you require an IP
access list, your Ops Manager Administration API keys can make API requests
only from the location-based IP or CIDR (Classless Inter-Domain Routing) addresses that you specify
in the IP access list.

To disable the IP access list requirement and allow your 
Ops Manager Administration API keys to make requests from any address on the internet, toggle 
Require IP Access List for the Ops Manager Administration API
to OFF.

To learn more, see access-list-for-api-operations.

**Step 6: Click the Create Organization button create the organization.**

Once you create the organization, you can add projects and users.

## Leave an Organization

**Important:**

You can't leave an organization if you are the last `Organization Owner` for that organization.

**Step 1: View all of your organizations.**

a. Expand the Organizations menu in the navigation bar.
b. Click View All Organizations.

**Step 2: Leave the organization.**

For the organization you wish to leave, click its Leave
button to open the Leave Organization modal.

**Step 3: Click Leave Organization to confirm.**

## Delete an Organization

**Important:**

To delete an organization, you must have
`Organization Owner` role for the organization.

You cannot delete an organization that has active projects. You must
delete the organization's projects before you can delete the
organization.

**Step 1: Navigate to the Settings page for your organization.**

a. If it is not already displayed, select your desired organization
   from the `office` Organizations menu in the
   navigation bar.

#. Click the Organization Settings icon next to the
   Organizations menu.

**Step 2: Delete the organization.**

a. If it is not already displayed, click the 
   General Settings tab.
#. Click Delete.

   This displays the Delete Organization dialog.

#. Click Delete Organization to confirm
