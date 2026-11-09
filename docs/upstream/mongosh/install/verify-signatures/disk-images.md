<!-- Converted from install/verify-signatures/disk-images.txt (reStructuredText). Includes are inlined. -->

# Verify Packages with Disk Image Verification (macOS)

The MongoDB release team digitally signs MongoDB Shell packages to
certify that packages are a valid and unaltered MongoDB release. Before
you install MongoDB Shell, you can use the digital signature to validate
the package.

This page describes how to verify `.dmg` packages on macOS.

## Before you Begin

If you don't have MongoDB Shell installed, download the MongoDB Shell
binary from the [Download Center](https://www.mongodb.com/try/download/shell).

## Steps

To verify the MongoDB Shell package, run:

```sh
codesign -dv --verbose=4 <path_to_mongosh_executable>
```

If the package is signed by MongoDB, the output includes the following
information:

```sh
Authority=Developer ID Application: MongoDB, Inc. (4XWMY46275)
Authority=Developer ID Certification Authority
Authority=Apple Root CA
```
