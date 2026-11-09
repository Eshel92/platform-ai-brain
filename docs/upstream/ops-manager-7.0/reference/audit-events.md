<!-- Converted from reference/audit-events.txt (reStructuredText). Includes are inlined. -->

# Audit Events

Ops Manager maintains an audit log of key operations that users and
administrators perform in the system. Unless otherwise stated, the
Audits page aggregates and displays these events.
You can access the Audits page through the
Admin link.

## User Audit Events

**`JOINED_GROUP`**

A user joined a Project.

This audit is not supported if using LDAP authentication for Ops Manager users

**`REMOVED_FROM_GROUP`**

A user was removed from a Project.

**`INVITED_TO_GROUP`**

A user was invited to a Project

**`MULTI_FACTOR_AUTH_RESET_EMAIL_SENT_AUDIT`**

A user requested and was sent an email with a link that will allow
them to reset their 2 factor authentication.

**`MULTI_FACTOR_AUTH_RESET_AUDIT`**

A user reset their two factor authentication.

**`MULTI_FACTOR_AUTH_UPDATED_AUDIT`**

A user updated their 2FA using the form in My Profile.

**`PASSWORD_RESET_EMAIL_SENT_AUDIT`**

A user requested and was sent an email with a link that will allow
them to reset their password.

**`PASSWORD_RESET_AUDIT`**

A user successfully reset their password via the *reset password*
flow.

**`PASSWORD_UPDATED_AUDIT`**

A user successfully updated their password using the form in
My Profile.

**`USER_EMAIL_ADDRESS_CHANGED_AUDIT`**

A user changed their email address.

**`USER_ROLES_CHANGED_AUDIT`**

A user's roles in a particular Project were changed.

**`SUCCESSFUL_LOGIN_AUDIT`**

A user successfully authenticated with their username and
password.

**`UNSUCCESSFUL_LOGIN_AUDIT`**

Login attempt was unsuccessful.

**`ACCOUNT_LOCKED_AUDIT`**

Ops Manager locked a user's account from the system, as a result of manual
action by the administrator, or because of a change in account
locking policies.

**`ACCOUNT_UNLOCKED_AUDIT`**

An administrator unlocked a user's account.

**`USER_CREATED_AUDIT`**

A new user was created.

## Host Audit Events

**`DELETE_HOST_AUDIT`**

A host was suppressed by a user.

**`ADD_HOST_AUDIT`**

A new host was added by a user, or auto-discovered by the system.

**`UNDELETE_HOST_AUDIT`**

A previously suppressed host was un-suppressed by a user.

**`HIDE_AND_DISABLE_HOST_AUDIT`**

The system determined that a host was a duplicate by the system,
and hid that host from the interface.

**`DB_PROFILER_ENABLE_AUDIT`**

Database profiling was enabled for a host

**`DB_PROFILER_DISABLE_AUDIT`**

Database profiling data collection was disabled for a host

**`HOST_IP_CHANGED_AUDIT`**

A change in IP address was detected for a host.

## Alert Config Audit Events

**`ALERT_ACKNOWLEDGED_AUDIT`**

A user acknowledged an open alert.

**`ALERT_UNACKNOWLEDGED_AUDIT`**

A user un-acknowledged an open alert.

**`ALERT_CONFIG_DISABLED_AUDIT`**

An alert configuration was disabled.

**`ALERT_CONFIG_ENABLED_AUDIT`**

An alert configuration was enabled.

**`ALERT_CONFIG_ADDED_AUDIT`**

An alert configuration was added.

**`ALERT_CONFIG_DELETED_AUDIT`**

An alert configuration was deleted.

**`ALERT_CONFIG_CHANGED_AUDIT`**

An alert configuration was edited.

## Backup Audit Events

**`RS_STATE_CHANGED_AUDIT`**

A user started, stopped, or terminated backup for a replica set. is started, stopped. or terminated by a user

**`CLUSTER_STATE_CHANGED_AUDIT`**

A user started, stopped or terminated backup for a sharded cluster.

**`RESTORE_REQUESTED_AUDIT`**

A restore was requested.

**`SYNC_REQUIRED_AUDIT`**

A user initiates a resync of a replica set or config server.

**`CLUSTERSHOT_DELETED_AUDIT`**

A user deletes a clustershot (e.g. a cluster checkpoint.)

**`SNAPSHOT_DELETED_AUDIT`**

A user delted a snapshot for a replica set.

**`RS_CREDENTIAL_UPDATED_AUDIT`**

A user updates the authentication credentials for a replica set.

**`CLUSTER_CREDENTIAL_UPDATED_AUDIT`**

A user updates the authentication credentials for a sharded cluster.

**`RS_BLACKLIST_UPDATED_AUDIT`**

A user updates the namespaces filter for a replica set.

**`CLUSTER_BLACKLIST_UPDATED_AUDIT`**

A user updates the namespaces filter for a sharded cluster.

**`RS_SNAPSHOT_SCHEDULE_UPDATED_AUDIT`**

A user updates the snapshot schedule for a replica set.

**`CLUSTER_SNAPSHOT_SCHEDULE_UPDATED_AUDIT`**

A user updates the snapshot schedule for a sharded cluster.

**`CLUSTER_CHECKKPOINT_UPDATED_AUDIT`**

A user updates the checkpoint schedule for a sharded cluster.

## Project Audit Events

**`GROUP_DELETED`**

A Project was deleted.

**`GROUP_CREATED`**

A new Project was created.

**`FLUSHED`**

All components of a deleted Project were removed from Ops Manager.

## Usage Audit Events

These events are only displayed to users with the
`Global Owner` role.

**`USAGE_DATA_ENABLED`**

Usage data was enabled.

**`USAGE_DATA_DISABLED`**

Usage data was disabled.

**`USAGE_DATA_RAW_DOWNLOAD`**

Unencrypted data was downloaded.

## Deployment Configuration Audit Events

**`AUTOMATION_CONFIG_PUBLISHED_AUDIT`**

An Ops Manager setting was changed. 

**Note:**

Only the first setting changed is displayed. To see the full set 
of changes, click the view all changes link.

## Data Explorer Events

**`DATA_EXPLORER`**

A user performed a Data Explorer read
operation.

**`DATA_EXPLORER_CRUD`**

A user performed a Data Explorer operation
which modified data.
