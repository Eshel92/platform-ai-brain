<!-- Converted from core/csfle/install.txt (reStructuredText). Includes are inlined. -->

# Installation Requirements

## Overview

Learn about the applications and libraries you must install to use
Client-Side Field Level Encryption (CSFLE).

## What You Need

Before you can use CSFLE, you must set up the following items
in your development environment:

- (Optional) Download the Automatic Encryption Shared Library. 
  The Automatic Encryption Shared Library is a preferred alternative to mongocryptd and
  does not require spawning a new process. `mongocryptd` is still supported.
- Install MongoDB Enterprise Edition.
- Install a MongoDB Driver Compatible with CSFLE.
- .. include:: /includes/see-get-started.rst

- Install [mongodb-crypt](https://mvnrepository.com/artifact/org.mongodb/mongodb-crypt).
  The `mongodb-crypt` library contains bindings to communicate
  with the native library that manages the encryption.

- (Optional) Download the Automatic Encryption Shared Library. 
  The Automatic Encryption Shared Library is a preferred alternative to mongocryptd and
  does not require spawning a new process. `mongocryptd` is still supported.
- Install MongoDB Enterprise Edition.
- Install a MongoDB Driver Compatible with CSFLE.
- .. include:: /includes/see-get-started.rst

- Install [mongodb-client-encryption](https://www.npmjs.com/package/mongodb-client-encryption),
  a Node.js wrapper for the `libmongocrypt` encryption library.
  The `libmongocrypt` library contains bindings to communicate
  with the native library that manages the encryption.

When using Node.js driver version `6.0.0` or later,
`mongodb-client-encryption` must have the same major version number as the driver.

For example, Node.js driver v6.x.x requires `mongodb-client-encryption`
v6.x.x.

- (Optional) Download the Automatic Encryption Shared Library. 
  The Automatic Encryption Shared Library is a preferred alternative to mongocryptd and
  does not require spawning a new process. `mongocryptd` is still supported.
- Install MongoDB Enterprise Edition.
- Install a MongoDB Driver Compatible with CSFLE.
- .. include:: /includes/see-get-started.rst

- Install [pymongocrypt](https://pypi.org/project/pymongocrypt/), a Python
  wrapper for the `libmongocrypt` encryption library.
  The `libmongocrypt` library contains bindings to communicate
  with the native library that manages the encryption.

- (Optional) Download the Automatic Encryption Shared Library. 
  The Automatic Encryption Shared Library is a preferred alternative to mongocryptd and
  does not require spawning a new process. `mongocryptd` is still supported.
- Install MongoDB Enterprise Edition.
- Install a MongoDB Driver Compatible with CSFLE.
- .. include:: /includes/see-get-started.rst

- Ensure that you're using an x64 operating system. CSFLE requires
  x64 support.

If you're using driver version 3.0 or later, you must also complete the following steps:

- Install the [MongoDB.Driver.Encryption](https://www.nuget.org/packages/MongoDB.Driver.Encryption)
  package from NuGet. This package enables automatic encryption. 
- If your application runs on Linux, install [libmongocrypt](https://www.mongodb.com/docs/manual/core/queryable-encryption/reference/libmongocrypt/)
  manually. Then, set the `LIBMONGOCRYPT_PATH` environment variable to 
  the absolute path of the `libmongocrypt` file.
- If your application runs on 64-bit Linux, and you're using driver version 3.4.3 or earlier,
  add the following lines of XML to your `.csproj` file. Change the value of the
  `<MongoDriverEncryptionVersion>` element to match the version of the
  `MongoDB.Driver.Encryption` package that you have installed.

```xml
<PropertyGroup>
    <!-- replace the version here with your package version --> 
    <MongoDriverEncryptionVersion>3.4.2</MongoDriverEncryptionVersion>
    <MongoDriverEncryptionPath>$(NuGetPackageRoot)mongodb.driver.encryption\$(MongoDriverEncryptionVersion)</MongoDriverEncryptionPath>
</PropertyGroup>
<PropertyGroup>
    <!-- Suppresses the duplicate file error -->
    <ErrorOnDuplicatePublishOutputFiles>false</ErrorOnDuplicatePublishOutputFiles>
</PropertyGroup>
<!-- Ensures the correct library after build or publish -->
<Target Name="EnsureCorrectMongoEncryption" AfterTargets="Build;Publish" Condition="'$(RuntimeIdentifier)' != ''">
    <!-- Determine paths based on current operation -->
    <PropertyGroup>
        <_TargetDir Condition="Exists('$(PublishDir)')">$(PublishDir)</_TargetDir>
        <_TargetDir Condition="'$(_TargetDir)' == ''">$(OutputPath)</_TargetDir>
    </PropertyGroup>
    <!-- Copy the correct library based on runtime identifier (RID) -->
    <ItemGroup>
        <_CorrectMongoLib Include="$(MongoDriverEncryptionPath)/runtimes/linux/native/x64/libmongocrypt.so"
                          Condition="'$(RuntimeIdentifier)' == 'linux-x64'" />
        <_CorrectMongoLib Include="$(MongoDriverEncryptionPath)/runtimes/linux/native/arm64/libmongocrypt.so"
                          Condition="'$(RuntimeIdentifier)' == 'linux-arm64'" />
        <_CorrectMongoLib Include="$(MongoDriverEncryptionPath)/runtimes/linux/native/alpine/libmongocrypt.so"
                          Condition="'$(RuntimeIdentifier)' == 'linux-musl-arm64'" />
    </ItemGroup>
    <!-- Copy with overwrite -->
    <Copy SourceFiles="@(_CorrectMongoLib)"
          DestinationFolder="$(_TargetDir)"
          Condition="'@(_CorrectMongoLib)' != ''"
          OverwriteReadOnlyFiles="true" />
    <Message Text="Fixed MongoDB encryption library for $(RuntimeIdentifier)"
             Condition="'@(_CorrectMongoLib)' != ''" />
</Target> 
```

- (Optional) Download the Automatic Encryption Shared Library. 
  The Automatic Encryption Shared Library is a preferred alternative to mongocryptd and
  does not require spawning a new process. `mongocryptd` is still supported.
- Install MongoDB Enterprise Edition.
- Install a MongoDB Driver Compatible with CSFLE.
- .. include:: /includes/see-get-started.rst

- Install libmongocrypt.
  The `libmongocrypt` library contains bindings to communicate
  with the native library that manages the encryption.

## Learn More

To start using CSFLE, see csfle-quick-start.

To learn how to use CSFLE with a remote Key Management System
provider, see csfle-tutorial-automatic-encryption.
