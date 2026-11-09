<!-- Converted from tutorial/add-monitored-deployment-to-automation.txt (reStructuredText). Includes are inlined. -->

# Add Monitored Processes to Automation

## Overview

Ops Manager Automation lets you deploy, reconfigure and upgrade your MongoDB
databases directly from the Ops Manager console.

If Ops Manager is already monitoring your MongoDB processes, you can add them
to Automation.

Automation relies on the MongoDB Agent, which you install on each
server that hosts a process to be added to automated management. The
MongoDB Agents regularly poll Ops Manager to determine goal configuration
and deploy changes as needed.

## Considerations

Automation doesn't support all MongoDB options, which can result in 
failed import attempts. To learn more, see 
om-unsupported-mdb-settings.

When adding a MongoDB deployment requiring authentication, you have the
option of importing that process's users and roles. During import,
Ops Manager prompts you to resolve any conflicts that may occur between the
imported users and roles and the managed users and roles.

### Automation and Updated Security Settings Upon Import

Adding a MongoDB deployment to automation may affect the security
settings of the Ops Manager project and the MongoDB deployment.

- **Automation enables the Project Security Setting**. If the
  MongoDB deployment requires authentication but the Ops Manager project doesn't
  have authentication settings enabled, when you add the MongoDB deployment
  to automation, Ops Manager updates the project's security settings to the security
  settings of the newly imported deployment.

  The import process only updates the Ops Manager project's security setting
  if the project's security setting is currently disabled. The import
  process doesn't disable the project's security setting or change its
  enabled authentication mechanism.

- **Automation Imports MongoDB Users and Roles**. The following statements
  apply to situations where a MongoDB deployment requires authentication
  or the Ops Manager project has authentication settings enabled.

  If the MongoDB deployment contains users or user-defined roles, you can
  choose to import these users and roles for Ops Manager to manage. The imported
  users and roles are Synced to all managed deployments in
  the Ops Manager project.

  - If you set the project's Enforce Consistent Set value to `Yes`,
    Ops Manager deletes from the MongoDB deployments those users and roles
    that are *not* imported.

  - If you set the project's Enforce Consistent Set value to `No`,
    Ops Manager stops managing non-imported users and roles in the project. These
    users and roles remain in the MongoDB deployment. To manage these
    users and roles, you must connect directly to the MongoDB deployment.

  If you don't want the Ops Manager project to manage specific users and roles,
  use the Authentication & Users and
  Authentication & Roles pages to remove these users and roles
  during import before you confirm and deploy the changes. To learn more,
  see manage-unmanage-mongodb-users.

  If the imported MongoDB deployment already has `mms-backup-agent` and
  `mms-monitoring-agent` users in its `admin` database, the import
  process overrides these users' roles with the roles for `mms-backup-agent`
  and `mms-monitoring-agent` users as set in the Ops Manager project.

- **Automation Applies to All Deployments in the Project**.
  The project's updated security settings, including all users and roles
  managed by the Ops Manager project, apply to *all* deployments in the project,
  including the imported MongoDB deployment.

  Ops Manager restarts all deployments in the project with the new setting,
  including the imported MongoDB deployment. After import, all deployments
  in the project use the Ops Manager automation keyfile upon restart.

  The deployment that you import must use the same keyfile as the existing
  processes in the destination project or the import process may not
  proceed. To learn more, see Authentication Credentials on Source
  and Destination Clusters.

  If the existing deployments in the project require a different security
  profile from the imported process, create a new project into which you
  can import the source MongoDB deployment.

#### Examples of Imported Users

The following examples apply to situations where the MongoDB deployment
requires authentication or the Ops Manager project has authentication settings enabled.

If you import the MongoDB users and custom roles, once the Ops Manager project
begins to manage the MongoDB deployment, the following happens, regardless
of the Enforce Consistent Set value:

- The Ops Manager project enables authentication, manages imported users and roles,
  and syncs the new users and roles to all its managed deployments.
- The MongoDB deployment's access control is enabled and requires
  authentication. The MongoDB deployment has all users and roles that
  the Ops Manager project manages. These users and roles have `Synced` set to
  `Yes`.

If you don't import the MongoDB users and custom roles, once the Ops Manager
project begins to manage the MongoDB deployment, the following happens:

If Enforce Consistent Set is set to `Yes`:

- The Ops Manager project enables authentication and doesn't change its managed
  users and roles.
- The MongoDB deployment's access control is enabled and requires authentication.
- Ops Manager deletes the non-imported MongoDB users and roles from the deployment.
- The MongoDB deployment has all users and roles that the Ops Manager project
  manages. These users and roles have `Synced` set to `Yes`.

If Enforce Consistent Set is set to `No`:

- The Ops Manager project enables authentication and doesn't change its security
  settings, including users and roles.
- The MongoDB deployment's access control is enabled and requires authentication.
- The non-imported MongoDB users and roles remain in the MongoDB deployment.
- The MongoDB deployment has all users and roles managed by the Ops Manager project.
  These users and roles have `Synced` set to `Yes`.

## Prerequisites

- Ensure that your deployment satisfies the  
  deployment requirements.

- Ops Manager must be currently monitoring the MongoDB processes, and the
  MongoDB Agent must be running. The processes must appear on the
  Ops Manager Deployment page.

  **See also:**

  /tutorial/add-existing-mongodb-processes to enable Ops Manager to
  automate and monitor your MongoDB processes if Ops Manager does not
  currently do so. 

- If mongod is enabled as a service on the deployment, 
  a race condition might result where `systemd` starts `mongod` on reboot, 
  rather than the Automation. To prevent this issue, ensure the `mongod` 
  service is disabled before you add your deployment to Automation:

  1. Verify whether the `mongod` service is enabled:

     ```sh
     sudo systemctl is-enabled mongod.service
     ```

  2. If the service is enabled, disable it:

     ```sh
     sudo systemctl disable mongod.service
     ```

- If the Ops Manager project doesn't have authentication settings enabled but
  the MongoDB process requires authentication, add the MongoDB Agent user
  for the Ops Manager project with the appropriate roles. The import process
  displays the required roles for the user. The added user becomes the
  project's MongoDB Agent user.

- If the Ops Manager project has authentication settings enabled, add the
  Ops Manager project's MongoDB Agent user to the MongoDB process.

  - To find the MongoDB Agent user, click Deployments, then
    Security, then Users.

  - To find the password for the Ops Manager project's MongoDB Agent user, use
    one of the following methods:

    **ui:**

    Follow the steps in the Add MongoDB Processes procedure to launch the wizard in the UI.
    When you reach the modal that says Do you want to add automation to this deployment?:

    1. Select 
       Add Automation and Configure Authentication.
    #. Click Show Password.

    **api:**

    Use the /reference/api/automation-config endpoint:

    ```sh
    curl --user "{username}:{apiKey}" --digest \
      --header "Accept: application/json" \
      --include \
      --request GET "<host>/api/public/v1.0/groups/<Group-ID>/automationConfig"
    ```

    **file:**

    Open the `mmsConfigBackup` file in your preferred text editor and find the `autoPwd` value.

  - In `mongosh`, use the `db.createUser()` method to add the
    Ops Manager project's MongoDB Agent user to the MongoDB process.
    For example, if the Ops Manager project uses Username/Password authentication,
    run the following command to add the `mms-automation` user to
    the `admin` database in the MongoDB deployment to import:

    ```javascript
    db.getSiblingDB("admin").createUser(
      {
        user: "mms-automation",
        pwd: "<password>",
        roles: [
          'clusterAdmin',
          'dbAdminAnyDatabase',
          'readWriteAnyDatabase',
          'userAdminAnyDatabase',
          'restore',
          'backup',
          'directShardOperations'  // Required for sharded clusters
        ]
      }
    )
    ```

    You must specify the `directShardOperations` role for sharded cluster
    automation. This role allows the automation agent to perform maintenance
    operations that require direct access to shards, such as adding shards to
    existing clusters. For non-sharded deployments (standalone or replica sets),
    you can omit this role.

- When you add a cluster under Ops Manager, Ops Manager automatically enables log
  rotation, which could collide
  with your existing `logRotate` configuration for `mongod` or
  `mongos` logs. To prevent this collision, do the following:  

  - Disable your `logRotate` configuration for `mongod` or `mongos`
    processes. 
  - Remove the `systemLog.logRotate` and `systemLog.logAppend`
    options from the 
    `mongod` or `mongos` process configuration to use the
    default of Ops Manager. 

- The import process requires that the authentication credentials and
  keyfiles are the same on the source and destination clusters. To learn
  more, see Authentication Credentials on Source and Destination Clusters.

- To successfully import an existing replica set to Ops Manager, 
  the instance must be healthy.

## Procedure

**Step 1: Navigate to the Clusters view for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Clusters view.

**Step 2: On the line listing the process, click Add.**

**Step 3: Follow the prompts to add the deployment item to Automation.**

If either the MongoDB deployment requires authentication or the Ops Manager
project has authentication enabled, you may import
the MongoDB's users and roles for Ops Manager to manage. The imported 
users and roles will be Synced to all deployments in the 
Ops Manager project.

**Warning:**

If the `Enforce Consistent Set` value for the Ops Manager project is
`YES`, any users and roles not imported are deleted from the MongoDB
deployment.

If the `Enforce Consistent Set` value for the Ops Manager project is
`No`, any users and roles not imported remain in the MongoDB
deployment and are not managed by Ops Manager.

To import users and roles:

a. Check Yes, import users and roles from this deployment
   item to have Ops Manager manage these MongoDB users and roles.

b. Click Continue.

**Note:** Adding a MongoDB Windows Service to Automation

If you are adding an existing MongoDB process that runs as a
Windows Service to Automation, Automation:

- Stops and disables the existing service
- Creates and starts a new service

**Step 4: Resolve conflicts for merged users and roles. (Optional)**

If you chose to import the MongoDB users and roles and one or more
conflict with those already in the automated deployment, you are
prompted to select which versions of the users and roles should be
used:

a. Select the correct user or role.

b. Click Review & Deploy. 

**Warning:**

If you choose not to resolve conflicts, the conflicting
records are overridden by the current configuration. Any
non-conflicting users can be imported later. You can create
new, or modify existing, users and roles for the added deployment
once it is under automation.

See /tutorial/manage-users for how to create or modify
users and /reference/user-roles for the list and
definitions of roles in Ops Manager.
