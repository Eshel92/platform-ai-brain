<!-- Converted from tutorial/authenticate-a-user.txt (reStructuredText). Includes are inlined. -->

# Authenticate a User with Self-Managed Deployments

To authenticate as a user, you must provide a username, password, and the 
`authentication database` associated 
with that user.

**Important:**

It is not possible to switch between users in the same
`mongosh` session. Authenticating as a different user
means the session has the privileges of **both** authenticated
users. To switch between users exit and relaunch
`mongosh`.

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

        Using `mongosh`, connect to the
        `mongod` or `mongos` instance:

        ```bash
        mongosh --port 27017
        ```

        In `mongosh`, switch to the
        authentication database (in this case, `admin`), and
        use the `db.auth(<username>, <pwd>)` method 
        or the `authenticate` command to authenticate against the 
        `authentication database`:

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

For examples using a MongoDB driver, see the `driver documentation`.
