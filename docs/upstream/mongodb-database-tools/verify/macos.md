<!-- Converted from verify/macos.txt (reStructuredText). Includes are inlined. -->

# Verify macOS Binaries

The MongoDB release team digitally signs Database Tools packages to
certify that packages are a valid and unaltered MongoDB release. Before
you install the Database Tools, you can use the digital signature to
validate the package.

The Database Tools `.zip` download for macOS is notarized. This page
describes how to use `codesign` to verify the integrity of individual
Database Tools binaries.

## Before you Begin

If you don't have the MongoDB Database Tools installed, download the
Database Tools binaries from the [Download Center](https://www.mongodb.com/try/download/database-tools).

## Steps

To verify a Database Tools binary, run:

```sh
codesign -dv --verbose=4 <path_to_binary>
```

For example, the following command verifies the `mongorestore` binary
in the `/usr/local/bin/` folder:

```sh
codesign -dv --verbose=4 /usr/local/bin/mongorestore
```

If the binary is signed by MongoDB, the output includes the following
information:

```sh
Authority=Developer ID Application: MongoDB, Inc. (4XWMY46275)
Authority=Developer ID Certification Authority
Authority=Apple Root CA
```
