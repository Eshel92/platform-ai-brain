<!-- Converted from tutorial/rotate-encryption-key.txt (reStructuredText). Includes are inlined. -->

# Rotate Encryption Keys

Most regulatory requirements mandate that a managed key used to decrypt
sensitive data must be rotated out and replaced with a new key once a
year.

**Note:** Disambiguation

To roll over database keys configured with AES256-GCM cipher afer a
filesystem restore, see `--eseDatabaseKeyRollover` instead.

MongoDB provides two options for key rotation. You can rotate out the
binary with a new instance that uses a new key. Or, if you are using a
KMIP server for key management, you can rotate the Customer Master Key.

## Rotate a Replica Set Member

**Note:**

To prevent changing the write quorum, never rotate more than one
replica set member at a time.

For a replica set, to rotate out a member:

#. Start a new `mongod` instance, configured to use a new key.
   Include the `--replSet` option with the name of the replica set as
   well as any other options specific to your configuration, such as
   `--dbpath` and `--bind_ip`.

   ```bash
   mongod --replSet myReplSet --enableEncryption \
   --kmipServerName <KMIP Server HostName> \
   --kmipServerCAFile ca.pem --kmipClientCertificateFile client.pem
   ```

#. Connect `mongosh` to the replica set's primary.

#. Add the instance to the replica set:

   ```javascript
   rs.add( { host: <host:port> } )
   ```

   **Warning:**

   Before MongoDB 5.0, a newly added secondary still counts as a voting
   member even though it can neither serve reads nor become primary until
   its data is consistent. If you are running a MongoDB version earlier
   than 5.0 and add a secondary with its `votes`
   and `priority` settings greater than zero, this can
   lead to a case where a majority of the voting members are
   online but no primary can be elected. To avoid such situations,
   consider adding the new secondary initially with
   `priority :0` and `votes :0`. Then, run `rs.status()` to ensure the
   member has transitioned into `SECONDARY` state. Finally, use
   `rs.reconfig()` to update its priority and votes.

   During the initial sync process, the re-encryption of the data with
   an entirely new set of database keys as well as a new system key
   occurs.

#. Remove the old node from the replica set and delete all its data.
   For instructions, see /tutorial/remove-replica-set-member

## KMIP Master Key Rotation

If you are using a KMIP server for key management, you can rotate
the Customer Master Key, the only externally managed key. With the new
master key, the internal keystore will be re-encrypted but the
database keys will be otherwise left unchanged. This obviates the need
to re-encrypt the entire data set.

#. Rotate the master key for the secondary members of the replica set one at a
   time.

   a. Restart the secondary, including the
      `--kmipRotateMasterKey` option. Include any other
      options specific to your configuration, such as `--bind_ip`. If
      the member already includes the `--kmipKeyIdentifier`
      option, either update the `--kmipKeyIdentifier` option
      with the new key to use or omit to request a new key from the
      KMIP server:

      ```bash
      mongod --enableEncryption --kmipRotateMasterKey \
        --kmipServerName <KMIP Server HostName> \
        --kmipServerCAFile ca.pem --kmipClientCertificateFile client.pem
      ```

      If using a configuration file, include the
      `security.kmip.rotateMasterKey`.

   b. Upon successful completion of the master key rotation and
      re-encryption of the database keystore, the `mongod`
      will exit.

   c. Restart the secondary without the `--kmipRotateMasterKey`
      parameter. Include any other options specific to your
      configuration, such as `--bind_ip`.

      ```bash
      mongod --enableEncryption --kmipServerName <KMIP Server HostName> \
        --kmipServerCAFile ca.pem --kmipClientCertificateFile client.pem
      ```

      If using a configuration file, remove the
      `security.kmip.rotateMasterKey` setting.

#. Step down the replica set primary.

   Connect `mongosh` to the primary and use
   `rs.stepDown()` to step down the primary and force an
   election of a new primary:

   ```javascript
   rs.stepDown()
   ```

#. When `rs.status()`
   shows that the primary has stepped down and another member
   has assumed `PRIMARY` state, rotate the master key for the stepped down member:

   a. Restart the stepped-down member, including the
      `--kmipRotateMasterKey` option. Include any other
      options specific to your configuration, such as `--bind_ip`. If the member already
      includes the `--kmipKeyIdentifier` option, either update
      the `--kmipKeyIdentifier` option with the new key to use
      or omit.

      ```bash
      mongod --enableEncryption --kmipRotateMasterKey \
        --kmipServerName <KMIP Server HostName> \
        --kmipServerCAFile ca.pem --kmipClientCertificateFile client.pem
      ```

      If using a configuration file, include the
      `security.kmip.rotateMasterKey`.

   b. Upon successful completion of the master key rotation and
      re-encryption of the database keystore, the `mongod`
      will exit.

   c. Restart the stepped-down member without the
      `--kmipRotateMasterKey` option. Include any other options
      specific to your configuration, such as `--bind_ip`.

      ```bash
      mongod --enableEncryption --kmipServerName <KMIP Server HostName> \
        --kmipServerCAFile ca.pem --kmipClientCertificateFile client.pem
      ```

      If using a configuration file, remove the
      `security.kmip.rotateMasterKey` setting.
