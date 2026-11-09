<!-- Converted from tutorial/change-own-password-and-custom-data.txt (reStructuredText). Includes are inlined. -->

# Change Your Password and Custom Data on Self-Managed Deployments

## Overview

Users with appropriate privileges can change their own passwords and
custom data. `Custom data` stores
optional user information.

## Considerations

To generate a strong password for use in this procedure, you can use the
`openssl` utility's `rand` command. For example, issue ``openssl
rand`` with the following options to create a base64-encoded string of 48
pseudo-random bytes:

```bash
openssl rand -base64 48
```

## Prerequisites

To modify your own password and custom data, you must have privileges
that grant `changeOwnPassword` and
`changeOwnCustomData` actions respectively on the user's database.

**Step 1: Connect as a user with privileges to manage users and roles.**

Connect to the `mongod` or `mongos` with privileges
to manage users and roles, such as a user with
`userAdminAnyDatabase` role. The following procedure uses the
`myUserAdmin` created in /tutorial/enable-authentication.

```javascript
mongosh --port 27017 -u myUserAdmin -p  --authenticationDatabase 'admin'
```

If you do not specify the password to the `-p`
command-line option, `mongosh` prompts for the
password.

**Step 2: Create a role with appropriate privileges.**

In the `admin` database, `create` a new
role with `changeOwnPassword` and
`changeOwnCustomData`.

```javascript
use admin
db.createRole(
   { role: "changeOwnPasswordCustomDataRole",
     privileges: [
        { 
          resource: { db: "", collection: ""},
          actions: [ "changeOwnPassword", "changeOwnCustomData" ]
        }
     ],
     roles: []
   }
)
```

**Step 3: Add a user with this role.**

In the `test` database, `create` a new user with
the created `"changeOwnPasswordCustomDataRole"` role. For example, the following
operation creates a user with both the built-in role `readWrite` and
the user-created `"changeOwnPasswordCustomDataRole"`.

**Tip:**

You can use the `passwordPrompt()` method in conjunction with
various user authentication/management methods/commands to prompt
for the password instead of specifying the password directly in the
method/command call. However, you can still specify the password
directly as you would with earlier versions of the
`mongo` shell.

```javascript
use test
db.createUser(
   {
     user:"user123",
     pwd: passwordPrompt(),  // or cleartext password
     roles:[ "readWrite", { role:"changeOwnPasswordCustomDataRole", db:"admin" } ] 
   }
)
```

To grant an existing user the new role, use
`db.grantRolesToUser()`.

## Procedure

**Step 1: Connect with the appropriate privileges.**

Connect to the `mongod` or `mongos` as a user with
appropriate privileges.

For example, the following operation connects to MongoDB as
`user123` created in the change-own-password-prereq
section.

```javascript
mongosh --port 27017 -u user123 --authenticationDatabase 'test' -p
```

If you do not specify the password to the `-p`
command-line option, `mongosh` prompts for the
password.

To check that you have the privileges specified in the
change-own-password-prereq section as well as to see user
information, use the `usersInfo` command with the
`showPrivileges` option.

**Step 2: Change your password and custom data.**

Use the `db.updateUser()` method to update the password and
custom data.

For example, the following operation changes the user's password to
`KNlZmiaNUp0B` and custom data to `{ title: "Senior Manager" }`:

**Tip:**

You can use the `passwordPrompt()` method in conjunction with
various user authentication/management methods/commands to prompt
for the password instead of specifying the password directly in the
method/command call. However, you can still specify the password
directly as you would with earlier versions of the
`mongo` shell.

```javascript
use test
db.updateUser(
   "user123",
   {
      pwd: passwordPrompt(),  // or cleartext password
      customData: { title: "Senior Manager" }
   }
)
```

Enter the password when prompted.
