<!-- Converted from verify/gpg.txt (reStructuredText). Includes are inlined. -->

# Verify Packages with GPG (Linux)

The MongoDB release team digitally signs Database Tools packages to
certify that packages are a valid and unaltered MongoDB release. Before
you install the Database Tools, you can use the digital signature to
validate the package.

This page describes how to use GPG to verify Linux packages.

## Before you Begin

If you don't have the MongoDB Database Tools installed, download the
Database Tools binaries from the [Download Center](https://www.mongodb.com/try/download/database-tools).

## Steps

**Step 1: Import the MongoDB Database Tools public key**

```sh
curl https://pgp.mongodb.com/server-Tools.asc | gpg --import
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

**Step 2: Download the MongoDB Database Tools public signature**

To download the Database Tools public signature, run the following
command, replacing the placeholder values with your platform,
architecture, and Database Tools version:

```sh
curl -LO https://s3.amazonaws.com/downloads.mongodb.org/tools/db/mongodb-database-tools-<platform>-<architecture>-<version>.tgz.sig
```

**Example:**

The following URL contains the signature file for Database
Tools on Amazon Linux 2, version {+version+}:

`https://s3.amazonaws.com/downloads.mongodb.org/tools/db/mongodb-database-tools-amazon2-x86_64-{+version+}.tgz.sig`

**Step 3: Verify the package**

```sh
gpg --verify <path_to_signature_file> <path_to_db_tools_executable>
```

If the package is signed by MongoDB, the command returns:

```sh
gpg: Signature made Wed 19 Feb 2025 02:19:15 PM EST
gpg:                using RSA key D4E45C292A5C94962F0D10E13132835C1D925D5B
gpg: Good signature from "MongoDB CLI Tools Release Signing Key <packaging@mongodb.com>" [unknown]
```

If the package is signed but the signing key is not added to your
local `trustdb`, the command returns:

```sh
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
```

If the package is not properly signed, the command returns an
error message:

```sh
gpg: Signature made Wed 19 Feb 2025 02:19:15 PM EST
gpg:                using RSA key D4E45C292A5C94962F0D10E13132835C1D925D5B
gpg: BAD signature from "MongoDB CLI Tools Release Signing Key <packaging@mongodb.com>" [unknown]
```
