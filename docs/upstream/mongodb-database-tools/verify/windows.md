<!-- Converted from verify/windows.txt (reStructuredText). Includes are inlined. -->

# Verify Windows Packages

The MongoDB release team digitally signs Database Tools packages to
certify that packages are a valid and unaltered MongoDB release. Before
you install the Database Tools, you can use the digital signature to
validate the package.

This page describes how to verify Windows `.msi` packages.

## Before you Begin

If you don't have the MongoDB Database Tools installed, download the
Database Tools binaries from the [Download Center](https://www.mongodb.com/try/download/database-tools).

## Steps

To verify the Database Tools package on Windows, you can use one of these
methods:

- db-tools-verify-signatures-windows-command-line

- db-tools-verify-signatures-windows-check-properties

### Verify Packages with PowerShell

To verify Windows packages with PowerShell, run:

```sh
powershell Get-AuthenticodeSignature -FilePath <path_to_db_tools_msi>
```

   
If the package is signed, the command returns:

```sh
SignerCertificate     Status     Path                               
-----------------     ------     ----
A5BBE2A6DA1D2A...     Valid      <path_to_db_tools_msi>
```

   

### Verify Packages by Checking Properties

**Step 1: Open the properties for your Database Tools package**

**Step 2: Check the package's digital signatures**

In the properties window, open the Digital Signatures
tab.

If the package is properly signed, the Embedded Signatures show
these properties:

| Name of signer | Digest algorithm | Timestamp |
|---|---|---|
| MongoDB, Inc. | sha256 | <Timestamp> |
