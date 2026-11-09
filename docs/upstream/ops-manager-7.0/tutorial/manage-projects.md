<!-- Converted from tutorial/manage-projects.txt (reStructuredText). Includes are inlined. -->

# Manage Projects

**Note:**

Groups are now projects.

In Ops Manager, MongoDB deployments are associated with projects.

You can create multiple projects in an organization. Each project has
its own Monitoring, Backup and Automations associated with the
project. 

## Working with Multiple Environments

For a project, the Monitoring must be able to connect to all
hosts it monitors. If you have multiple MongoDB deployments in distinct
environments and cannot monitor all deployments with a single agent
(for instance, if your environments are separated by firewalls), you
will need to add new projects.

You can also use multiple projects and agents if you want to separately
monitor different MongoDB deployments that run in the same environment.

## Create One Project

**Important:**

- To create a project for an organization, you must be either an
  `Organization Owner` or an `Organization
  Project Creator`.

- When you create a project, you are added as an
  `Project Owner`
  of the project.

- When you create a project, Ops Manager automatically assigns a set of
  default alert configurations
  to the project.

**Step 1: Navigate to the Create a Project page.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. Click the Leaf icon in the upper left corner of the
   page.

#. Click New Project.

You can also expand the Projects menu in the navigation
bar, then click + New Project.

**Note:**

To create a new project when LDAP is the authentication method:

1. Go to the Admin Console.
2. Select Organizations.
3. Click New Project for the Organisation for which you wish to create the project.

**Step 2: Provide a name and default server type for your Project.**

* - Name
  - Enter the name for this project.
* - Default Project Server Type
  - Select the default server type to be applied to all hosts
    added to this project. This default type overrides the default
    type set for the parent organization.

    You can change the server type for individual hosts.

    You can modify this setting in
    /tutorial/manage-project-settings.

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

**Step 3: Configure LDAP (Lightweight Directory Access Protocol) options.**

If managing Ops Manager users through LDAP (Lightweight Directory Access Protocol), enter values for the
following **Optional LDAP Configuration** fields .

**Important:**

**Multiple LDAP Groups Can Map to One Role**

Ops Manager roles can include more than one LDAP group. Type
multiple LDAP group names in the relevant role fields separated
by two semicolons (`;;`).

| Field | Action |
|---|---|
| LDAP Groups for Project Owner Role | Type the LDAP group(s) to which the Project Owners of the Ops Manager project belong. You can type multiple LDAP groups into this field if they are separated by two semicolons (`;;`). |
| LDAP Groups for Automation Admin Role | Type the LDAP group(s) to which Ops Manager project's Automation Administrators belong. You can type multiple LDAP groups into this field if they are separated by two semicolons (`;;`). |
| LDAP Groups for Backup Admin Role | Type the LDAP group(s) to which Ops Manager project's Backup Administrators belong. You can type multiple LDAP groups into this field if they are separated by two semicolons (`;;`). |
| LDAP Groups for Monitoring Admin Role | Type the LDAP group(s) to which Ops Manager project's Monitoring Administrators belong. You can type multiple LDAP groups into this field if they are separated by two semicolons (`;;`). |
| LDAP Groups for User Admin Role | Type the LDAP group(s) to which Ops Manager project's User Administrators belong. You can type multiple LDAP groups into this field if they are separated by two semicolons (`;;`). |
| LDAP Groups for Read Only Role | Type the LDAP group(s) to which Ops Manager project's Read Only Users belong. You can type multiple LDAP groups into this field if they are separated by two semicolons (`;;`). |

**Step 4: Add members to your project.**

For existing Ops Manager users, enter their username. Usually, this is the
email the person used to register.

For new Ops Manager users, enter their email address to send an invitation.

**Step 5: Specify the access for the members.**

**Step 6: Click the Create Project button to create the project.**

## Move One Project from One Organization to Another

**Important:**

- To move a project between Organizations, you must have the
  `Organization Owner` on the source and target
  Organization.

- When you move the Project, Ops Manager removes users that don't
  belong to the target Organization.

**Step 1: Navigate to the Projects page for your organization.**

a. If it is not already displayed, select your desired organization
   from the `office` Organizations menu in the
   navigation bar.

#. Click the Leaf icon in the upper left corner of the
   page, or click Projects in the sidebar.

**Step 2: Choose the Project to move.**

a. Click `ellipsis` to the right of the project you want to
   move.

b. Click Move Project.

   The Move Project modal displays.

**Step 3: Choose the target Organization.**

a. Click the target Organization to which you want to move your
   project.

b. Click Confirm and Move.

## Delete One Project

**Important:**

Deleting a project removes all the project's artifacts, including
all monitoring data. Ops Manager no longer displays the project in
selection lists. You can't delete a project that has managed 
deployments.

You can delete a project if:

- You have `Project Owner` access for the project.

- The project has no backups. To terminate your backups prior to
  removing the project, see terminate-backup.

**Step 1: View all of your projects.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. Click the Leaf icon in the upper left corner of the
   page. You can also expand the Projects menu in the
   navigation bar, then click View All Projects.

**Step 2: Delete the project.**

Click the `trash-o` button for the project you wish to
delete to open the Delete Project modal.

**Step 3: Confirm that you want to delete this project.**

a. Click Delete Project.  
#. If /core/two-factor-authentication is enabled, enter 
   the verification code.
#. Click Delete Project again.

   If prompted for authentication, enter the verification code. After
   verifying, click Delete Project again.

**Step 4: Stop the MongoDB Agents.**

| Agent | Procedure |
|---|---|
| Automations | Stop the agent's process on each server. |
| Monitoring | See stop-monitoring-agent and /tutorial/delete-monitoring-agent. |
| Backup | See stop-backup-agent and /tutorial/delete-backup-agent. |

## Additional Information

Use the following procedure to modify project settings:

- /tutorial/manage-project-settings
