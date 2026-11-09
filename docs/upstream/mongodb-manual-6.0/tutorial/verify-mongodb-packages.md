<!-- Converted from tutorial/verify-mongodb-packages.txt (reStructuredText). Includes are inlined. -->

# Verify Integrity of MongoDB Packages

The MongoDB release team digitally signs all software packages to
certify that a particular MongoDB package is a valid and unaltered
MongoDB release. Before installing MongoDB, you should validate the 
package using either the provided PGP signature or SHA-256 checksum.

PGP signatures provide the strongest guarantees by checking both the
authenticity and integrity of a file to prevent tampering.

Cryptographic checksums only validate file integrity to prevent network
transmission errors.

## Verify Linux/macOS Packages

### Use PGP/GPG

MongoDB signs each release branch with a different PGP key. The public 
key files for each release branch are available for download from the 
[key server](https://pgp.mongodb.com/) in both textual `.asc` and binary 
`.pub` formats.

**Step 1: Download the MongoDB installation file.**

Download the binaries from [MongoDB Download Center](https://www.mongodb.com/try/download?tck=docs_server)
based on your environment.

For example, to download the `6.0.21` release for macOS through the
shell, run this command:

```sh
curl -LO https://fastdl.mongodb.org/osx/mongodb-macos-x86_64-6.0.21.tgz
```

**Step 2: Download the public signature file.**

```sh
curl -LO https://fastdl.mongodb.org/osx/mongodb-macos-x86_64-6.0.21.tgz.sig
```

**Step 3: Download then import the key file.**

If you have not downloaded and imported the MongoDB 6.0 public key,
run these commands:

```sh
curl -LO https://pgp.mongodb.com/server-6.0.21.asc
gpg --import server-6.0.21.asc
```

PGP should return this response:

```sh
gpg: key 4B7C549A058F8B6B: "MongoDB 6.0 Release Signing Key <packaging@mongodb.com>" imported
gpg: Total number processed: 1
gpg:               imported: 1
```

**Step 4: Verify the MongoDB installation file.**

Run this command:

```sh
gpg --verify mongodb-macos-x86_64-6.0.21.tgz.sig mongodb-macos-x86_64-6.0.21.tgz
```

GPG should return this response:

```sh
gpg: Signature made Wed Jun  5 03:17:20 2019 EDT
gpg:                using RSA key 4B7C549A058F8B6B
gpg: Good signature from "MongoDB 6.0 Release Signing Key <packaging@mongodb.com>" [unknown]
```

If the package is
properly signed, but you do not currently trust the signing key
in your local `trustdb`, `gpg` will also return the following message :

```sh
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: E162 F504 A20C DF15 827F  718D 4B7C 549A 058F 8B6B
```

If you receive the following error message, confirm that you imported the correct
public key:

```sh
gpg: Can't check signature: public key not found
```

### Use SHA-256

**Step 1: Download the MongoDB installation file.**

Download the binaries from [MongoDB Download Center](https://www.mongodb.com/try/download?tck=docs_server)
based on your environment.

For example, to download the `6.0.21` release for macOS through the
shell, type this command:

```sh
curl -LO https://fastdl.mongodb.org/osx/mongodb-macos-x86_64-6.0.21.tgz
```

**Step 2: Download the SHA256 file.**

```sh
curl -LO https://fastdl.mongodb.org/osx/mongodb-macos-x86_64-6.0.21.tgz.sha256
```

**Step 3: Use the SHA-256 checksum to verify the MongoDB package file.**

Compute the checksum of the package file:

```sh
shasum -c mongodb-macos-x86_64-6.0.21.tgz.sha256
```

which should return the following if the checksum matched the downloaded
package:

```sh
mongodb-macos-x86_64-6.0.21.tgz: OK
```

## Verify Windows Packages

This verifies the MongoDB binary against its SHA256 key.

**Step 1: Download the installer.**

Download the MongoDB `.msi` installer. For example, to download the
latest version of MongoDB Community Edition:

→ [MongoDB Community Download Center](https://www.mongodb.com/try/download/community?tck=docs_server)

a. In the Version dropdown, select
   `6.0.21 (current release)`.

#. In the Platform dropdown, select Windows.

#. In the Package dropdown, select msi.

#. Click Download and save the file to your Downloads
   folder.

**Step 2: Get the public signature file.**

Get the public signature file for your MongoDB version.

For example, for the SHA256 signature of the latest version
of MongoDB Community Edition:

#. From <https://fastdl.mongodb.org/windows/mongodb-windows-x86_64-6.0.21-signed.msi.sha256>, copy the content.

#. Save the content to a file `mongodb-windows-x86_64-6.0.21-signed.msi.sha256` in your Downloads folder.

**Step 3: Compare the signature file to the MongoDB installer hash.**

To compare the signature file to the hash of the MongoDB binary, 
invoke this Powershell script:

```powershell
$sigHash = (Get-Content $Env:HomePath\Downloads\mongodb-windows-x86_64-6.0.21-signed.msi.sha256 | Out-String).SubString(0,64).ToUpper(); `
$fileHash = (Get-FileHash $Env:HomePath\Downloads\mongodb-windows-x86_64-6.0.21-signed.msi).Hash.Trim(); `
echo $sigHash; echo $fileHash; `
$sigHash -eq $fileHash
```

```bat
C777DF7816BB8C9A760FDEA782113949408B6F39D72BE29A2551FA51E2FE0473
C777DF7816BB8C9A760FDEA782113949408B6F39D72BE29A2551FA51E2FE0473
True
```

The command outputs three lines:

- A `SHA256` hash that you downloaded directly from MongoDB.
- A `SHA256` hash computed from the MongoDB binary you
  downloaded from MongoDB.
- A `True` or `False` result depending if the hashes match.

If the hashes match, the MongoDB binary is verified.
