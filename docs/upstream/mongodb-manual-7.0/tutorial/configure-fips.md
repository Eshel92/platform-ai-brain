<!-- Converted from tutorial/configure-fips.txt (reStructuredText). Includes are inlined. -->

# Configure MongoDB for FIPS

## Overview

The Federal Information Processing Standard (FIPS) is a U.S. government
computer security standard used to certify software modules and
libraries that encrypt and decrypt data securely.  You can configure
MongoDB to run with a FIPS 140-2 certified library
for OpenSSL. Configure FIPS to run by default or as needed from the
command line.

A full description of FIPS and TLS/SSL is beyond the scope of this document.
This tutorial assumes prior knowledge of FIPS and TLS/SSL.

**Important:** MongoDB and FIPS

FIPS is a property of the encryption system and not the access 
control system. However, if your environment requires FIPS compliant 
encryption *and* access control, you must ensure that the access 
control system uses only FIPS-compliant encryption.

MongoDB's FIPS support covers the way that MongoDB uses SSL/TLS
libraries for network encryption, SCRAM authentication, and X.509
authentication. If you use Kerberos or LDAP authentication, you must
ensure that these external mechanisms are FIPS-compliant.

**Note:**

MongoDB disables support for TLS 1.0
encryption on systems where TLS 1.1+ is available. 

## Platform Support

FIPS mode is only available with MongoDB Enterprise edition. See
/administration/install-enterprise to download and install
MongoDB Enterprise.

FIPS mode is supported on the following platforms:

| Platform | TLS/SSL library |
|---|---|
| Linux | OpenSSL |
| Windows | Secure Channel (SChannel) |
| macOS | Secure Transport |

## OpenSSL3 Support

Starting in MongoDB 6.0.7, FIPS mode supports 
[OpenSSL3](https://www.openssl.org/docs/man3.0/man7/migration_guide.html)
for the following operating systems:

- Ubuntu 22.04
- RHEL 9 
- Amazon Linux 2023

## Configuring FIPS

Select the tab below for your platform:

**linux-fips-config:**

### Prerequisites

Your Linux system must have an OpenSSL library configured with the FIPS
140-2 module in order to support FIPS mode for MongoDB.

- Verify that your OpenSSL software includes FIPS support by running
  the following command:

  ```bash
  openssl version
  ```

- For Red Hat Enterprise Linux 6.x (RHEL 6.x) or its derivatives such
  as CentOS 6.x, the OpenSSL toolkit must be at least version
  `openssl-1.0.1e-16.el6_5` to use FIPS mode. To upgrade the OpenSSL
  library on these platforms, run the following command:

  ```bash
  sudo yum update openssl
  ```

- Some versions of Linux periodically execute a process to prelink
  dynamic libraries with pre-assigned addresses. This process modifies
  the OpenSSL libraries, specifically `libcrypto`. The OpenSSL FIPS
  mode will subsequently fail the signature check performed upon
  startup to ensure `libcrypto` has not been modified since
  compilation.

  To configure the Linux prelink process to not prelink `libcrypto`,
  run the following command:

  ```bash
  sudo bash -c "echo '-b /usr/lib64/libcrypto.so.*' >>/etc/prelink.conf.d/openssl-prelink.conf"
  ```

Once you have configured your Linux system to support FIPS-compliant
operation, follow the steps below to configure your
`mongod` or `mongos` instance to operate in
FIPS mode.

### Procedure

#### A. Configure MongoDB to use TLS/SSL

See /tutorial/configure-ssl for details about configuring your
deployment to use TLS/SSL. Ensure that your certificate is
FIPS-compliant.

#### B. Run MongoDB instance in FIPS mode

Perform these steps after you /tutorial/configure-ssl.

**Step 1: Change configuration file.**

To configure your `mongod` or `mongos` instance to use
FIPS mode, shut down the instance and update the configuration file with
the `net.tls.FIPSMode` setting:

```yaml
net:
   tls:
      FIPSMode: true
```

**Step 2: Start `mongod` or `mongos` instance with configuration file.**

For example, run this command to start the  `mongod` instance with its configuration file:

```javascript
mongod --config /etc/mongod.conf
```

#### C. Confirm that FIPS mode is running

Check the server log file for a message that FIPS is active:

```bash
FIPS 140-2 mode activated
```

**windows-fips-config:**

### Prerequisites

Microsoft provides the following resource on configuring FIPS mode for
Windows 10 and Windows Server 2016 or later:

→ FIPS 140-2 Validation on Windows

Once you have configured your Windows system to support FIPS-compliant
operation, follow the steps below to configure your
`mongod` or `mongos` instance to operate in
FIPS mode.

### Procedure

#### A. Configure MongoDB to use TLS/SSL

See /tutorial/configure-ssl for details about configuring your
deployment to use TLS/SSL. Ensure that your certificate is
FIPS-compliant.

#### B. Run MongoDB instance in FIPS mode

Perform these steps after you /tutorial/configure-ssl.

**Step 1: Change configuration file.**

To configure your `mongod` or `mongos` instance to use
FIPS mode, shut down the instance and update the configuration file with
the `net.tls.FIPSMode` setting:

```yaml
net:
   tls:
      FIPSMode: true
```

**Step 2: Start `mongod` or `mongos` instance with configuration file.**

For example, run this command to start the  `mongod` instance with its configuration file:

```javascript
mongod.exe --config /etc/mongod.conf
```

#### C. Confirm that FIPS mode is running

Check the server log file for a message that FIPS is active:

```bash
FIPS 140-2 mode activated
```

**macos-fips-config:**

### Prerequisites

Supported versions of macOS are FIPS-compliant by default. Check the
documentation for your version of macOS to verify its compliance
status. For example, Apple provides the following resource for
macOS 10.14:

→ Apple FIPS Cryptographic Modules for 10.14

On compliant versions of macOS, follow the steps below to configure your
`mongod` or `mongos` instance to operate in
FIPS mode.

### Procedure

#### A. Configure MongoDB to use TLS/SSL

See /tutorial/configure-ssl for details about configuring your
deployment to use TLS/SSL. Ensure that your certificate is
FIPS-compliant.

#### B. Run MongoDB instance in FIPS mode

Perform these steps after you /tutorial/configure-ssl.

**Step 1: Change configuration file.**

To configure your `mongod` or `mongos` instance to use
FIPS mode, shut down the instance and update the configuration file with
the `net.tls.FIPSMode` setting:

```yaml
net:
   tls:
      FIPSMode: true
```

**Step 2: Start `mongod` or `mongos` instance with configuration file.**

For example, run this command to start the  `mongod` instance with its configuration file:

```javascript
mongod --config /etc/mongod.conf
```

#### C. Confirm that FIPS mode is running

Check the server log file for a message that FIPS is active:

```bash
FIPS 140-2 mode activated
```

## Additional Considerations

### SCRAM SHA and FIPS Mode

Starting in MongoDB 5.1, instances running in 
FIPS mode have the 
SCRAM-SHA-1 authentication mechanism
disabled by default. You can enable the SCRAM-SHA-1 authentication
mechanism with the
setParameter.authenticationMechanisms command.

This change will not affect drivers which target MongoDB 
`setFeatureCompatibilityVersion` 4.0+.

If you use SCRAM-SHA-1:

- md5 is necessary but is not used for cryptographic purposes,
  and

- if you use FIPS mode, then instead of
  SCRAM-SHA-1 use:

  - SCRAM-SHA-256,
  - Kerberos,
  - LDAP, or
  - X.509

### `mongod`, `mongos`, and FIPS Mode

If you configure `mongod` and `mongos` to use
FIPS mode, `mongod` and `mongos` use FIPS-compliant connections.

### Database Tools and FIPS Mode

The following programs no longer support the 
`--sslFIPSMode` option:

- `mongodump`
- `mongoexport`
- `mongofiles`
- `mongoimport`
- `mongorestore`
- `mongostat`
- `mongotop`

If you configure `mongod` and `mongos` to use
FIPS mode, the preceding database tools use FIPS-compliant connections 
automatically.

### MongoDB Shell and FIPS Mode

The default `mongosh` distribution:

- Contains OpenSSL 3.
- Uses FIPS-compliant connections to `mongod` and
  `mongos` if you configure `mongod` and `mongos` to
  use FIPS mode.

MongoDB also provides a MongoDB Shell distribution that can use:

- OpenSSL 1.1 and OpenSSL 3 installed on your server.
- `--tlsFIPSMode` option, which enables the `mongosh` FIPS mode.

**See also:**

- To download MongoDB Shell distributions that contain OpenSSL 1.1
  and OpenSSL 3, go to the [MongoDB Download Center](https://www.mongodb.com/try/download/shell).
- mdb-shell-install
