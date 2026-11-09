<!-- Converted from tutorial/troubleshoot-kerberos.txt (reStructuredText). Includes are inlined. -->

# Troubleshoot Self-Managed Kerberos Authentication

## `mongokerberos` Validation Tool

The `mongokerberos` program provides a convenient method to 
verify your platform's Kerberos configuration for use with MongoDB, and to 
test that Kerberos authentication from a MongoDB client works as expected.

The `mongokerberos` tool can help diagnose common
configuration issues, and is the recommended place to start when
troubleshooting your Kerberos configuration. See the
`mongokerberos` documentation for more information.

`mongokerberos` is available in MongoDB Enterprise only.

## Kerberos Configuration Debugging Strategies

If you have difficulty starting or authenticating against
`mongod` or `mongos` with Kerberos, consider the following:

- Ensure that you are running MongoDB Enterprise, not MongoDB Community
  Edition. Kerberos authentication is a MongoDB Enterprise feature
  and will not work with MongoDB Community Edition binaries.

  To verify that you are using MongoDB Enterprise, pass the `--version`
  command line option to the `mongod` or `mongos`:

  ```bash
  mongod --version
  ```

  In the output from this command, look for the string ``modules:
  subscription` or `modules: enterprise`` to confirm you are using the
  MongoDB Enterprise binaries.

- Ensure that the canonical system hostname of the
  `mongod` or `mongos` instance is a resolvable,
  fully qualified domain name. 
  
  On Linux, you can verify the system hostname resolution with the ``hostname
  -f`` command at the system prompt.

- On Linux, ensure that the [primary component of the service principal name (SPN)](http://web.mit.edu/KERBEROS/krb5-1.5/krb5-1.5.4/doc/krb5-user/What-is-a-Kerberos-Principal_003f.html) 
  of the SPN is `mongodb`. If the primary component of the SPN
  **is not** `mongodb`,
  you must specify the primary component using
  `--setParameter saslServiceName`. 

- On Linux, ensure that the [instance component of the service principal name (SPN)](http://web.mit.edu/KERBEROS/krb5-1.5/krb5-1.5.4/doc/krb5-user/What-is-a-Kerberos-Principal_003f.html) 
  in the
  keytab file matches the canonical system hostname
  of the `mongod` or `mongos`
  instance. If the `mongod` or `mongos`
  instance's system hostname is not in the keytab file,
  authentication will fail with a ``GSSAPI error acquiring 
  credentials.`` error message.

  If the hostname of your `mongod` or `mongos` instance
  as returned by `hostname -f`
  is not fully qualified,
  use `--setParameter saslHostName` to set the instance's fully qualified domain name when
  starting your `mongod` or `mongos`.
  
- Ensure that each host that runs a `mongod` or
  `mongos` instance has `A` and `PTR` DNS records to
  provide both forward and reverse DNS lookup. The `A` record should
  map to the `mongod` or `mongos`'s FQDN.

- Ensure that clocks on the servers hosting your MongoDB instances and
  Kerberos infrastructure are within the maximum time skew: 5 minutes
  by default. Time differences greater than the maximum time skew
  prevent successful authentication.

- Ensure that Linux KRB5 keytabs contain principal names that end in 
  `@<KERBEROS REALM>`. To validate SPNs (service principal names), 
  run `setspn -Q <spn>` on Active Directory. If correctly configured, 
  this command returns one Distinguished Name for the account that is attached 
  to the SPN. If you run `klist -k <keytab>` on Linux, 
  `<spn>@<KERBEROS REALM>` appears in the 
  keytab.

- If you use Active Directory as a KDC (Key Distribution Center), ensure 
  that the MongoDB service account is a user account, not a machine account.

- If you use AES (Advanced Encryption Standard) encryption with Active 
  Directory, enable AES on the MongoDB service account with either the 
  `msDS-SupportedEncryptionTypes` property or the "Network Security: 
  Configure Encryption types allowed for Kerberos" policy setting.

- Kerberos salts its key generation algorithms to ensure that two users with the 
  same password result in distinct keys. `ktutil` on Linux and Active 
  Directory (AD) don't use the same process to generate salts. This discrepancy 
  can result in authentication failures when working across Linux and Windows 
  environments. To mitigate this issue, you can: 
  
  - Generate the keytab file on the AD server and move the resulting file to the 
    Linux server. 

    ```bash
    ktpass /out <outfile.keytab> /princ <spn>@<KERBEROS REALM> /mapuser <current userPrincipalName> /crypto ALL /ptype KRB5_NT_PRINCIPAL +rndpass
    ```

    

    **Note:**

    This will change `userPrincipalName` to the value in `/princ`.

    
  - Use `ktutil` on Linux and force it to use the correct salt. To force 
    `ktutil` to use the correct salt: 
    
    #. Generate a keytab entry that uses `userPrincipalName` as the principal 
       name.
       

       ```bash
       ktutil:  add_entry -password -p <userPrincipalName>@<KERBEROS REALM> -e aes256-cts-hmac-sha1-96 -k <KVNO>
       Password for <userPrincipalName>@<KERBEROS REALM>: 
       ktutil:  list -k
       slot KVNO Principal
       ```

    
    #. Hexdump the key. 
    
    #. Create a new keytab entry, using `<spn>@<KERBEROS REALM>` as the 
       principal name and use the hexdumped key.

       ```bash
       1    <KVNO> <userPrincipalName>@<KERBEROS REALM>(0x<HEXDUMP>)
       ktutil:  add_entry -key -p <spn>@<KERBEROS REALM> -e aes256-cts-hmac-sha1-96 -k <KVNO>
       Key for <spn>@<KERBEROS REALM> (hex): <HEXDUMP>
       ktutil:  write_kt mongodb_ad.keytab
       ```

    
  - Use RC4-HMAC, which does not use salts, although this is not recommended.

## Kerberos Trace Logging on Linux

MIT Kerberos provides the `KRB5_TRACE` environment variable for
trace logging output. If you are having persistent problems with
MIT Kerberos on Linux, you can set `KRB5_TRACE` when starting your
`mongod`, `mongos`, or `mongosh` instances to
produce verbose logging.

For example, the following command starts a standalone `mongod`
whose keytab file is at the default `/etc/krb5.keytab` path
and sets `KRB5_TRACE` to write to `/logs/mongodb-kerberos.log`:

```bash
env KRB5_KTNAME=/etc/krb5.keytab \
    KRB5_TRACE=/logs/mongodb-kerberos.log \
    mongod --dbpath /data/db --logpath /data/db/mongodb.log \
    --auth --setParameter authenticationMechanisms=GSSAPI \
    --bind_ip localhost,<hostname(s)|ip address(es)> --fork
```

## Common Error Messages

In some situations, MongoDB will return error messages from the GSSAPI
interface if there is a problem with the Kerberos service. Some common
error messages are:

`GSSAPI error in client while negotiating security context.`
  This error occurs on the client and reflects insufficient credentials
  or a malicious attempt to authenticate.

  If you receive this error, ensure that you are using the correct
  credentials and the correct fully qualified domain name when
  connecting to the host.

`GSSAPI error acquiring credentials.`
  This error occurs during the start of the `mongod` or
  `mongos` and reflects improper configuration of the system
  hostname or a missing or incorrectly configured keytab file.

**See also:**

- /core/kerberos

- /tutorial/control-access-to-mongodb-with-kerberos-authentication

- /tutorial/control-access-to-mongodb-windows-with-kerberos-authentication
