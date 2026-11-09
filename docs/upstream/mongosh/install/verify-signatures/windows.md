<!-- Converted from install/verify-signatures/windows.txt (reStructuredText). Includes are inlined. -->

# Verify Windows Packages

The MongoDB release team digitally signs MongoDB Shell packages to
certify that packages are a valid and unaltered MongoDB release. Before
you install MongoDB Shell, you can use the digital signature to validate
the package.

This page describes how to verify Windows `.exe` and `.msi`
packages.

## Before you Begin

If you don't have MongoDB Shell installed, download the MongoDB Shell
binary from the [Download Center](https://www.mongodb.com/try/download/shell).

## Steps

To verify the MongoDB Shell package on Windows, you can use one of these
methods:

- mongosh-verify-signatures-windows-command-line

- mongosh-verify-signatures-windows-check-properties

### Verify Packages with PowerShell

To verify Windows packages with PowerShell, run:

```sh
powershell Get-AuthenticodeSignature -FilePath <path_to_mongosh_exe_or_msi>
```

   
If the package is signed, the command returns:

```sh
SignerCertificate     Status     Path                               
-----------------     ------     ----
F2D7C28591847B...     Valid      <path_to_mongosh_exe_or_msi>
```

### Verify Packages by Checking Properties

**Step 1: Open the properties for your MongoDB Shell package**

**Step 2: Check the package's digital signatures**

In the properties window, open the Digital Signatures
tab.

If the package is properly signed, the Digital Signatures show
these properties:

| Name of signer | Digest algorithm | Timestamp |
|---|---|---|
| MONGODB, INC. | sha256 | <Timestamp> |
