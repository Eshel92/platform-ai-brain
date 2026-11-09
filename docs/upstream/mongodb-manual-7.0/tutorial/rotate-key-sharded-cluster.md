<!-- Converted from tutorial/rotate-key-sharded-cluster.txt (reStructuredText). Includes are inlined. -->

# Rotate Keys for Self-Managed Sharded Clusters

Sharded cluster members can use keyfiles
to authenticate each other as memers of the same deployment.

A keyfile can
contain multiple keys and membership authentication is established if
at least one key is common across members. This allows for rolling
upgrade of the keys without downtime.

The following tutorial steps through the process to update, without any
downtime, the key for a sharded cluster. [#exclude-encryption-keyfile]_

**Warning:**

The example keys in this tutorial are for illustrative purposes
only. Do NOT use for your deployment. Instead, generate a
keyfile using any method you choose (e.g. ``openssl rand -base64
756``, etc.).

Consider a sharded cluster where each member's keyfile contains the
following key:

(Figure: /images/example-key1.png)

The following procedure updates the sharded cluster members to use a
new key:

(Figure: /images/example-key2.png)

## Procedure

### 1. Modify the Keyfile to Include Old and New Keys

Modify each member's keyfile to include both the old and new keys.

**Warning:**

The example keys in this tutorial are for illustrative purposes
only. Do NOT use for your deployment. Instead, generate a
keyfile using any method you choose (e.g. ``openssl rand -base64
756``, etc.).

You can specify multiple key strings as a sequence of key strings (optionally 
enclosed in quotes):

(Figure: /images/example-multiple-keys2.png)

### 1. Restart Each Member

Once all the keyfiles contain both the old and new keys, restart each
member one at a time.

#### Config Servers

**For each secondary of the config server replica set (CSRS)**,
connect `mongosh` to the member and:

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

#### Shard Replica Sets

**For each secondary member of the shard replica sets**, connect
`mongosh` to the member and:

a. Use the `db.shutdownServer()` method to shut down the member:

   ```javascript
   use admin
   db.shutdownServer()
   ```

b.   Restart the member.

**For the primary of each shard replica set**, connect
`mongosh` to the member and

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

#### `mongos` Routers

**For each mongos/router instance**, connect
`mongosh` to the `mongos` instance and:

a. Use the `db.shutdownServer()` method to shut down the member:

   ```javascript
   use admin
   db.shutdownServer()
   ```

b.   Restart the member.

Once all members have been restarted, the members now accept either the
old or new key for membership authentication.

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

#### Config Servers

**For each secondary of the config server replica set (CSRS)**,
connect `mongosh` to the member and:

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

#### Shard Replica Sets

**For each secondary member of the shard replica sets**, connect
`mongosh` to the member and:

a. Use the `db.shutdownServer()` method to shut down the member:

   ```javascript
   use admin
   db.shutdownServer()
   ```

b.   Restart the member.

**For the primary of each shard replica set**, connect
`mongosh` to the member and

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

#### `mongos` Routers

**For each mongos/router instance**, connect
`mongosh` to the `mongos` instance and:

a. Use the `db.shutdownServer()` method to shut down the member:

   ```javascript
   use admin
   db.shutdownServer()
   ```

b.   Restart the member.

Once all members have been restarted, the members now accept only the
new key for membership authentication.
