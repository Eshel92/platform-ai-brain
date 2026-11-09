<!-- Converted from verify/rpm.txt (reStructuredText). Includes are inlined. -->

# Verify RPM Packages (RHEL)

The MongoDB release team digitally signs Database Tools packages to
certify that packages are a valid and unaltered MongoDB release. Before
you install the Database Tools, you can use the digital signature to
validate the package.

This page describes how to verify `.rpm` packages on RHEL operating
systems.

## Before you Begin

If you don't have the MongoDB Database Tools installed, download the
Database Tools binaries from the [Download Center](https://www.mongodb.com/try/download/database-tools).

## Steps

**Step 1: Import the MongoDB Database Tools public key in gpg and rpm**

```sh
curl https://pgp.mongodb.com/server-Tools.asc | gpg --import

rpm --import https://pgp.mongodb.com/server-Tools.asc
```

If the key imports successfully, the command returns:

```sh
gpg: key 3132835C1D925D5B: public key "MongoDB CLI Tools Release Signing Key <packaging@mongodb.com>" imported
gpg: Total number processed: 1
gpg:               imported: 1
```

If you have previously imported the key, the command returns:

```sh
gpg: key 3132835C1D925D5B: "MongoDB CLI Tools Release Signing Key <packaging@mongodb.com>" not changed
gpg: Total number processed: 1
gpg:              unchanged: 1
```

**Step 2: Verify the rpm file**

```sh
rpm --checksig <path_to_db_tools_rpm_file>
```

If the file is signed, the command returns:

```sh
<path_to_db_tools_rpm_file> digests signatures OK
```
