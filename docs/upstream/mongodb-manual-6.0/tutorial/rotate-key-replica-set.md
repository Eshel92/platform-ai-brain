<!-- Converted from tutorial/rotate-key-replica-set.txt (reStructuredText). Includes are inlined. -->

# Rotate Keys for Self-Managed Replica Sets

Replica set members can use keyfiles to
authenticate each other as members of the same deployment.

A keyfile can
contain multiple keys and membership authentication is established if
at least one key is common across members. This allows for rolling
upgrade of the keys without downtime.

The following tutorial steps through the process to update the key for
a replica set without downtime. [#exclude-encryption-keyfile]_ 

**Warning:**

The example keys in this tutorial are for illustrative purposes
only. Do NOT use for your deployment. Instead, generate a
keyfile using any method you choose (for example, ``openssl rand -base64
756``, etc.).

Consider a replica set where each member's keyfile contains the
following key:

(Figure: /images/example-key1.png)

The following procedure updates the replica set members to use a new
key:

(Figure: /images/example-key2.png)

## Procedure

### 1. Modify the Keyfile to Include Old and New Keys

Modify each member's keyfile to include both the old and new keys. You
can specify multiple keys either as strings enclosed in quotes or as a
sequence of keys.

**Warning:**

The example keys in this tutorial are for illustrative purposes
only. Do NOT use for your deployment. Instead, generate a
keyfile using any method you choose (e.g. ``openssl rand -base64
756``, etc.).

You can specify multiple key strings as a sequence of key
strings (optionally enclosed in single or double quotes).

(Figure: /images/example-multiple-keys2.png)

### 2. Restart Each Member

Once all the keyfiles contain both the old and new keys, restart each
member one at a time.

**For each secondary member**, connect `mongosh` to the
member and:

a. Use the `db.shutdownServer()` method to shut down the member:

   ```javascript
   use admin
   db.shutdownServer()
   ```

b.   Restart the member.

**For the primary**, connect `mongosh` to the member and

a. Use `rs.stepDown()` to step down the member:

   ```javascript
   rs.stepDown()
   ```

#. Use the `db.shutdownServer()` method to shut down the member:

   ```javascript
   use admin
   db.shutdownServer()
   ```

#. Restart the member.

Since the keyfiles contains both the old and new keys, all members can
now accept either keys for membership authentication.

### 3. Update Keyfile Content to the New Key Only

**Warning:**

The example keys in this tutorial are for illustrative purposes
only. Do NOT use for your deployment. Instead, generate a
keyfile using any method you choose (e.g. ``openssl rand -base64
756``, etc.).

Modify each member's keyfile to include only the new password.

(Figure: /images/example-key2.png)

### 4. Restart Each Member

Once all the keyfiles contain the new key only, restart each member one
at a time.

**For each secondary member**, connect `mongosh` to the
member and:

a. Use the `db.shutdownServer()` method to shut down the member:

   ```javascript
   use admin
   db.shutdownServer()
   ```

b.   Restart the member.

**For the primary**, connect `mongosh` to the member and

a. Use `rs.stepDown()` to step down the member:

   ```javascript
   rs.stepDown()
   ```

#. Use the `db.shutdownServer()` method to shut down the member:

   ```javascript
   use admin
   db.shutdownServer()
   ```

#. Restart the member.

All members now accept only the new key for membership authentication.
