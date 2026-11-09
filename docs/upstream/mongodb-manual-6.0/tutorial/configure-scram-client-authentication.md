<!-- Converted from tutorial/configure-scram-client-authentication.txt (reStructuredText). Includes are inlined. -->

# Use SCRAM to Authenticate Clients on Self-Managed Deployments

The following procedure sets up SCRAM for client authentication on a
standalone `mongod` instance.

To use SCRAM authentication for replica sets or sharded clusters, see
/tutorial/deploy-replica-set-with-keyfile-access-control.

**Important:**

You cannot use both SCRAM authentication and another authentication type for the same user.

## Procedure

**Step 1: Start MongoDB without access control**

Start a standalone `mongod` instance without access
control.

Open a terminal and run the following command as the `mongod` user:

```sh
mongod --port 27017 --dbpath /var/lib/mongodb
```

The `mongod` instance in this tutorial uses
`port 27017` and the `/var/lib/mongodb`
data directory.

The tutorial assumes that the `/var/lib/mongodb` directory exists
and is the default `dbPath`. You may specify a
different data directory or port as needed.

**Tip:**

When `mongod` starts, it creates some system files in the
`/var/lib/mongodb` directory. To ensure the system files have
the correct ownership, follow this tutorial as the `mongod`
user. If you start `mongod` as the `root` user you will
have to update file ownership later. 

**Step 2: Connect to the instance**

Open a new terminal and connect to the cluster with
`mongosh`:

```sh
mongosh --port 27017
```

If you are connecting to a different deployment, specify additional
command line options, such as `--host`, as
needed to connect.

**Step 3: Create the user administrator**

**Important:** Localhost Exception

You can create the user administrator either before or after
enabling access control. If you enable access control before
creating any user, MongoDB provides a localhost exception which allows you to create a user
administrator in the `admin` database. Once created, you must
authenticate as the user administrator to create additional users.

Using `mongosh`:

1. switch to the `admin` database
2. add the `myUserAdmin` user with the
   `userAdminAnyDatabase` and
   `readWriteAnyDatabase` roles":

```javascript
use admin
db.createUser(
  {
    user: "myUserAdmin",
    pwd: passwordPrompt(), // or cleartext password
    roles: [
      { role: "userAdminAnyDatabase", db: "admin" },
      { role: "readWriteAnyDatabase", db: "admin" }
    ]
  }
)
```

**Tip:**

The `passwordPrompt()` method prompts you to enter the
password. You can also specify your password directly as a string. We
recommend to use the `passwordPrompt()` method to avoid the
password being visible on your screen and potentially leaking the
password to your shell history.

The `userAdminAnyDatabase` role allows this user to:

- create users
- grant or revoke roles from users
- create or modify customs roles

You can assign your user additional built-in roles or user-defined roles
as needed.

The database where you create the user, in this example `admin`,
is the user's authentication database. Although the user needs to
authenticate to this database, the user can have roles in other
databases. The user's authentication database doesn't limit the
user's privileges.

**Step 4: Re-start the MongoDB instance with access control**

Shut down the `mongod` instance. Using
`mongosh`, issue the following command:

```javascript
db.adminCommand( { shutdown: 1 } )
```

Exit `mongosh`.

Start the `mongod` with access control enabled.

- If you start the `mongod` from the command line, add
  the `--auth` command line option:

  ```bash
  mongod --auth --port 27017 --dbpath /var/lib/mongodb
  ```

- If you start the `mongod` using a
  configuration file, add the
  `security.authorization` configuration file setting:

  ```bash
  security:
      authorization: enabled
  ```

Clients that connect to this instance must now authenticate
themselves and can only perform actions as determined by their
assigned roles.

**Important:** Localhost Exception

You can create users either before or after enabling access
control. If you enable access control before creating any user,
MongoDB provides a localhost exception which allows you to create a user
administrator in the `admin` database. Once created, you must
authenticate as the user administrator to create additional users.

**Step 5: Connect and authenticate as the user administrator**

Using `mongosh`, you can:

tabs:
   - id: cmdline
     name: Authenticate during Connection
     content: |
        Start `mongosh` with the `-u
        <username>`, `-p`, and the
        `--authenticationDatabase <database>` command line options:

        ```bash
        mongosh --port 27017  --authenticationDatabase \
            "admin" -u "myUserAdmin" -p
        ```

        Enter your password when prompted.

   - id: authafter
     name: Authenticate after Connection
     content: |

        Using `mongosh`, connect to your database
        deployment:

        ```bash
        mongosh --port 27017
        ```

        In `mongosh`, switch to the
        authentication database (in this case, `admin`), and
        use the `db.auth(<username>, <pwd>)` method to authenticate:

        ```javascript
        use admin
        db.auth("myUserAdmin", passwordPrompt()) // or cleartext password
        ```

        **Tip:**

        The `passwordPrompt()` method prompts you to enter the
        password. You can also specify your password directly as a string. We
        recommend to use the `passwordPrompt()` method to avoid the
        password being visible on your screen and potentially leaking the
        password to your shell history.

        Enter the password when prompted.

## Next Steps

To use SCRAM authentication for replica sets or sharded clusters, see
/tutorial/deploy-replica-set-with-keyfile-access-control.
