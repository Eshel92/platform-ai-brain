<!-- Converted from tutorial/encrypt-user-credentials.txt (reStructuredText). Includes are inlined. -->

# Encrypt User Credentials

For configuration settings that store credentials, you can either store
the credentials in plain text or use the Ops Manager `credentialstool`
to encrypt the credentials. If you choose to store credentials in plain
text, reduce the permissions on the conf-mms.properties
file on each server.

This procedure is valid only for SCRAM username and password authentication and (LDAP) PLAIN authentication.
It doen't apply to `MONGODB-X509` or `GSSAPI` authentication, both of which use usernames but not passwords.

**Important:**

When installed with `rpm` or `deb` packages on Linux systems,
the `credentialstool` tool requires root (`sudo`) privileges,
because it reads the `/etc/mongodb-mms/gen.key` file. Ops Manager
uses the `gen.key` to encrypt sensitive data in the database and
configuration files.

Use the `credentialstool` to generate encrypted credentials for the MongoDB deployments:

**Step 1: Run the shell command to create a pair of encrypted credentials.**

```sh
sudo <install_dir>/bin/credentialstool --username <username> 
--password
```

| Variable | Definition |
|---|---|
| `<username>` | Your MongoDB username |
| `<install_dir>` | Path where Ops Manager was installed. |

**Step 2: Enter the password when prompted.**

The `credentialstool` then outputs the encrypted credential pair.

**Step 3: Add the encrypted credentials to the `conf-mms.properties` file.**

a. Enter the encrypted credential pair in the `mongo.mongoUri`
   settings where needed.

b. Add the `mongo.encryptedCredentials` setting and set it to `true`.

   **Example:**

   ```sh
   mongo.mongoUri=mongodb://da83ex3s:a4fbcf3a1@mydb1.example.net:40000/admin
   mongo.encryptedCredentials=true
   ```

   **Important:**

   The `conf-mms.properties` file can contain multiple
   `mongo.mongoUri` settings. If
   `mongo.encryptedCredentials` is `true`, you must
   encrypt all user credentials found in the various
   `mongo.mongoUri` settings.
