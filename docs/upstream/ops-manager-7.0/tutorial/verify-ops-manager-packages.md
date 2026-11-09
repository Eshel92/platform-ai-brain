<!-- Converted from tutorial/verify-ops-manager-packages.txt (reStructuredText). Includes are inlined. -->

# Verify Integrity of Ops Manager Packages

Starting in Ops Manager 4.4.14, the MongoDB release team digitally signs Ops Manager
packages to certify that they are valid and unaltered MongoDB releases.
Before installing Ops Manager, validate the package using the provided
PGP (Pretty Good Privacy) signature.

PGP signatures provide the strongest guarantees by checking both the
authenticity and integrity of a file to prevent tampering.

## Verify a `deb` Package

**Step 1: Download the latest version of the Ops Manager package.**

a. Open your preferred browser to visit the
   MongoDB Download Center on
   MongoDB.com.

   If you start from MongoDB.com, click Products
   arrow-right Ops Manager
   arrow-right Try it now.

#. From the Platforms drop-down menu, click 
   Ubuntu 22.04.

#. From the Packages drop-down menu, click
   DEB for x86_64 architecture.

#. Click Download.

   The downloaded package is named
   `mongodb-mms-<version>.x86_64.deb`,
   where `<version>` is the version number.

**Step 2: Use cURL to download the public key file from MongoDB.**

In the following command, replace `<version>` with the major version of
the Ops Manager package. For example, use 7.0 for any release in the 7.x release series.

```sh
curl -O https://pgp.mongodb.com/opsmanager-<version>.asc
```

**Step 3: Use cURL to download the public signature file from MongoDB.**

In the following command, replace `<version>` with the major version of
the Ops Manager package. For example, use 7.0 for any release in the 7.x release series.

```sh
curl -O https://downloads.mongodb.com/on-prem-mms/deb/mongodb-mms-<version>_x86_64.deb.sig
```

**Step 4: Import the public key.**

```sh
gpg --import opsmanager-<version>.asc
```

**Step 5: Verify the Ops Manager package integrity.**

In the following command, replace `<download>` with the file name for the Ops Manager package you downloaded.

```sh
gpg --verify <download>.sig \ <download>.deb
```

When the package is successfully verified, you receive a response like
the following:

```sh
gpg: Signature made Wed Jun 23 15:44:30 2021 UTC
gpg:                using RSA key 056AB6A90E47FE40
gpg: Good signature from "Ops Manager <version> Release Signing Key <packaging@mongodb.com>" [unknown]
```

If the package is properly signed, but you don't currently trust the
signing key in your local `trustdb`, `gpg` also returns the
following message:

```sh
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: D657 EF0E F51C 41B7 AE11  1CAF 056A B6A9 0E47 FE40
```

## Verify an `rpm` Package

**Step 1: Download the latest version of the Ops Manager package.**

a. Open your preferred browser to visit the
   MongoDB Download Center on
   MongoDB.com.

   If you start from MongoDB.com, click Products
   arrow-right Ops Manager
   arrow-right Try it now.

#. From the Platforms dropdown menu, click one of the
   following options:

   - Red Hat + CentOS 7, 8, 9 / SUSE 12 + 15 / Amazon Linux 2, Amazon Linux 2023

#. From the Packages dropdown menu, click
   RPM.

#. Click Download.

   The downloaded package is named
   `mongodb-mms-<version>.x86_64.rpm`, where `<version>` is the
   version number.

**Step 2: Use cURL to download the public key file from MongoDB.**

In the following command, replace `<version>` with the major version of
the Ops Manager package. For example, use 7.0 for any release in the 7.x release series.

```sh
curl -O https://pgp.mongodb.com/opsmanager-<version>.asc
```

**Step 3: Import the public key.**

In the following command, replace `<version>` with the major version of
the Ops Manager package. For example, use 7.0 for any release in the 7.x release series.

```sh
sudo rpm --import opsmanager-<version>.asc
```

**Step 4: Verify the Ops Manager package integrity.**

In the following command, replace:

- `<download>` with the file name for the Ops Manager package you downloaded.

```sh
sudo rpm -K <download>.rpm
```

When the package is successfully verified, you receive a response like
the following:

```sh
<download>.rpm: rsa sha1 (md5) pgp md5 OK
```

## Verify a `tar.gz` Archive

**Step 1: Download the latest version of the Ops Manager archive.**

a. Open your preferred browser to visit the
   MongoDB Download Center on
   MongoDB.com.

   If you start from MongoDB.com, click Products
   arrow-right Ops Manager
   arrow-right Try it now.

#. From the Version dropdown menu, click one of the
   provided stable versions.

#. From the Platform dropdown menu, click one of the
   following options:

   - Red Hat + CentOS 7, 8, 9 / SUSE 12 + 15 / Amazon Linux 2, Amazon Linux 2023
   - Debian 9, 10, 11 / Ubuntu 18.04

#. From the Package dropdown menu, click
   tar.gz.

#. Click Download.

   The downloaded package is named
   `mongodb-mms-<version>.x86_64.tar.gz`,
   where `<version>` is the version number.

**Step 2: Use cURL to download the public key file from MongoDB.**

In the following command, replace `<version>` with the major version of
the Ops Manager package. For example, use 7.0 for any release in the 7.x release series.

```sh
curl -O https://pgp.mongodb.com/opsmanager-<version>.asc
```

**Step 3: Use cURL to download the public signature file from MongoDB.**

In the following command, replace:

- `<download>` with the file name for the Ops Manager package you downloaded.

```sh
curl -O https://downloads.mongodb.com/on-prem-mms/tar/<download>.tar.gz.sig
```

**Step 4: Import the public key.**

In the following command, replace `<version>` with the major version of
the Ops Manager package. For example, use 7.0 for any release in the 7.x release series.

```sh
gpg --import opsmanager-<version>.asc
```

**Step 5: Verify the Ops Manager package integrity.**

In the following command, replace:

- `<download>` with the file name for the Ops Manager package you downloaded.

```sh
gpg --verify <download>.tar.gz.sig \ <download>.tar.gz
```

When the package is successfully verified, you receive a response like
the following:

```sh
gpg: Signature made Wed Jun 23 15:44:30 2021 UTC
gpg:                using RSA key 056AB6A90E47FE40
gpg: Good signature from "Ops Manager <version> Release Signing Key <packaging@mongodb.com>" [unknown]
```

If the package is properly signed, but you don't currently trust the
signing key in your local `trustdb`, `gpg` also returns the
following message:

```sh
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: D657 EF0E F51C 41B7 AE11  1CAF 056A B6A9 0E47 FE40
```
