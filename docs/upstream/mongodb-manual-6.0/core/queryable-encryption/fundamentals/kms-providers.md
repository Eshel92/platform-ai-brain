<!-- Converted from core/queryable-encryption/fundamentals/kms-providers.txt (reStructuredText). Includes are inlined. -->

# KMS Providers

## Overview

Learn about the **Key Management Service** providers Queryable Encryption
supports.

A **Key Management Service** is a Key Management System provided as a service.

## Key Management Service Tasks

In Queryable Encryption, your Key Management Service:

- Creates and encrypts the Customer Master Key
- Encrypts the Data Encryption Keys created by your application
- Decrypts Data Encryption Keys

To learn more about Customer Master Keys and Data Encryption Keys, see
qe-reference-keys-key-vaults.

### Create and Store your Customer Master Key

To create a Customer Master Key, configure your Key Management Service
provider to generate your Customer Master Key as follows:

(Figure: /images/CSFLE_Master_Key_KMS.png)

To view a tutorial that demonstrates how to create and store a
CMK ({+cmk-long+}) in your preferred Key Management Service,
see qe-tutorial-automatic-encryption.

### Create and Encrypt a Data Encryption Key

To create a Data Encryption Key:

- Instantiate a `ClientEncryption` instance in your
  Queryable Encryption enabled application:

  * Provide a `kmsProviders` object that specifies the credentials
    your Queryable Encryption enabled application uses to authenticate with
    your KMS ({+kms-long+}).

- Create a Data Encryption Key with the `CreateDataKey` method of the
  `ClientEncryption` object in your Queryable Encryption enabled application.

  * Provide a `dataKeyOpts` object that specifies with which key
    your KMS ({+kms-long+}) should encrypt your new Data Encryption Key.

To view a tutorial demonstrating how to create and encrypt a
Data Encryption Key, see the following resources:

- qe-quick-start
- qe-tutorial-automatic-encryption

To view the structure of `kmsProviders` and `dataKeyOpts` objects
for all supported KMS ({+kms-long+}) providers, see
qe-reference-kms-providers-supported-kms.

## Supported Key Management Services

The following sections of this page present the following information
for all Key Management Service providers:

- Architecture of Queryable Encryption enabled client
- Structure of `kmsProviders` objects
- Structure of `dataKeyOpts` objects

Queryable Encryption supports the following Key Management Service
providers:

- qe-reference-kms-providers-aws
- qe-reference-kms-providers-azure
- qe-reference-kms-providers-gcp
- qe-reference-kms-providers-kmip
- qe-reference-kms-providers-local

### Amazon Web Services KMS

This section provides information related to using
[AWS Key Management Service](https://aws.amazon.com/kms/)
in your Queryable Encryption enabled application.

To view a tutorial demonstrating how to use AWS KMS in your
Queryable Encryption enabled application, see
qe-tutorial-automatic-aws.

#### Architecture

The following diagram describes the architecture of a
Queryable Encryption enabled application using AWS (Amazon Web Services) KMS.

(Figure: /images/CSFLE_Data_Key_KMS.png)

**Note:** Client Can't Access Customer Master Key

When using the preceding Key Management Service, your
Queryable Encryption enabled application does not have access to
your Customer Master Key.

#### kmsProviders Object

The following table presents the structure of a `kmsProviders`
object for AWS KMS:

| Field | Required for IAM User | Required for IAM Role | Description |
|---|---|---|---|
| Access Key ID | Yes | Yes | Identifies the account user. |
| Secret Access Key | Yes | Yes | Contains the authentication credentials of the account user. |
| Session Token | No | Yes | Contains a token obtained from AWS Security Token Service (STS). |

#### dataKeyOpts Object

The following table presents the structure of a `dataKeyOpts`
object for AWS KMS:

| Field | Required | Description |
|---|---|---|
| key | Yes | [Amazon Resource Number (ARN)](https://docs.aws.amazon.com/kms/latest/developerguide/viewing-keys.html#find-cmk-id-arn) of the master key. |
| region | No | AWS region of your master key, e.g. "us-west-2"; required only if not specified in your ARN. |
| endpoint | No | Custom hostname for the AWS endpoint if configured for your account. |

### Azure Key Vault

This section provides information related to using
[Azure Key Vault](https://azure.microsoft.com/en-us/services/key-vault/)
in your Queryable Encryption enabled application.

To view a tutorial demonstrating how to use Azure Key Vault in your
Queryable Encryption enabled application, see
qe-tutorial-automatic-azure.

#### Architecture

The following diagram describes the architecture of a
Queryable Encryption enabled application using Azure Key Vault.

(Figure: /images/CSFLE_Data_Key_KMS.png)

**Note:** Client Can't Access Customer Master Key

When using the preceding Key Management Service, your
Queryable Encryption enabled application does not have access to
your Customer Master Key.

#### kmsProviders Object

The following table presents the structure of a `kmsProviders`
object for Azure Key Vault:

| Field | Required | Description |
|---|---|---|
| azure.tenantId | Yes | Identifies the organization of the account. |
| azure.clientId | Yes | Identifies the clientId to authenticate your registered application. |
| azure.clientSecret | Yes | Used to authenticate your registered application. |
| azure.identityPlatformEndpoint | No | Specifies a hostname and port number for the authentication server. Defaults to login.microsoftonline.com and is only needed for non-commercial Azure instances such as a government or China account. |

#### dataKeyOpts Object

The following table presents the structure of a `dataKeyOpts` object for
Azure Key Vault:

| Field | Required | Description |
|---|---|---|
| keyName | Yes | Name of the master key |
| keyVersion | No | Version of the master key |
| keyVaultEndpoint | Yes | URL of the key vault. E.g. myVaultName.vault.azure.net |

### Google Cloud Platform KMS

This section provides information related to using
[Google Cloud Key Management](https://cloud.google.com/security-key-management)
in your Queryable Encryption enabled application.

To view a tutorial demonstrating how to use GCP KMS in your
Queryable Encryption enabled application, see
qe-tutorial-automatic-gcp.

#### Architecture

The following diagram describes the architecture of a
Queryable Encryption enabled application using GCP KMS.

(Figure: /images/CSFLE_Data_Key_KMS.png)

**Note:** Client Can't Access Customer Master Key

When using the preceding Key Management Service, your
Queryable Encryption enabled application does not have access to
your Customer Master Key.

#### kmsProviders Object

The following table presents the structure of a `kmsProviders`
object for GCP KMS:

* - Field
  - Required
  - Description

* - email
  - Yes
  - Identifies your service account email address.

* - privateKey
  - Yes
  - | Identifies your service account private key in either
      [base64 string](https://en.wikipedia.org/wiki/Base64) or
      Binary subtype 0
      format without the prefix and suffix markers.
    |
    | Suppose your service account private key value is as follows:

    ```none
    -----BEGIN PRIVATE KEY-----\nyour-private-key\n-----END PRIVATE KEY-----\n
    ```

    | The value you would specify for this field is:

    ```none
    your-private-key
    ```

    | If you have a `user-key.json` credential file, you can extract
      the string by executing the following command in a bash or
      similar shell:

    ```shell
    cat user-key.json | jq -r .private_key | openssl pkcs8 -topk8 -nocrypt -inform PEM -outform DER | base64 -w 0
    ```

* - endpoint
  - No
  - Specifies a hostname and port number for the authentication server.
    Defaults to oauth2.googleapis.com.

#### dataKeyOpts Object

The following table presents the structure of a `dataKeyOpts` object for
GCP KMS:

| Field | Required | Description |
|---|---|---|
| projectId | Yes | Identifier for your project in which you created the key. |
| location | Yes | Region specified for your key. |
| keyRing | Yes | Identifier for the group of keys your key belongs to. |
| keyName | Yes | Identifier for the symmetric master key. |
| keyVersion | No | Specifies the version of the named key. If not specified, the default version of the key is used. |
| endpoint | No | Specifies the host and optional port of the Cloud KMS. The default is `cloudkms.googleapis.com`. |

### KMIP

This section provides information related to using a
[KMIP](https://docs.oasis-open.org/kmip/spec/v1.0/os/kmip-spec-1.0-os.html)
compliant Key Management Service provider in your Queryable Encryption enabled application.

#### Architecture

The following diagram describes the architecture of a
Queryable Encryption enabled application using a {+kmip-hover+}-compliant key provider.

(Figure: /images/CSFLE_Data_Key_KMIP.png)

**Important:** Client Accesses Customer Master Key

When your Queryable Encryption enabled application uses
a {+kmip-hover+}-compliant key provider, your application
directly accesses your Customer Master Key.

#### kmsProviders Object

The following table presents the structure of a `kmsProviders`
object for a KMIP compliant Key Management Service:

**Note:** Authenticate through TLS/SSL

Your Queryable Encryption enabled application authenticates through
TLS/SSL (Transport Layer Security/Secure Sockets Layer)
when using KMIP.

| Field | Required | Description |
|---|---|---|
| endpoint | Yes | Specifies a hostname and port number for the authentication server. |

#### dataKeyOpts Object

The following table presents the structure of a `dataKeyOpts` object
for a KMIP compliant Key Management Service:

| Field | Required | Description |
|---|---|---|
| keyId | No | The `keyId` field of a 96 byte [Secret Data managed object](http://docs.oasis-open.org/kmip/spec/v1.4/os/kmip-spec-v1.4-os.html#_Toc490660780) stored in your {+kmip-hover+}-compliant key provider. If you do not specify the `keyId` field in the `masterKey` document you send to your {+kmip-hover+}-compliant key provider, the driver creates a new 96 Byte Secret Data managed object in your {+kmip-hover+}-compliant key provider to act as your master key. |
| endpoint | Yes | The URI of your {+kmip-hover+}-compliant key provider. |

### Local Key Provider

This section provides information related to using a Local Key Provider (your filesystem)
in your Queryable Encryption enabled application.

**Warning:** Do Not Use a Local Key File in Production

A local key file in your filesystem is insecure and is
**not recommended** for production. Instead,
you should store your Customer Master Keys in a remote
Key Management System
(KMS).

To learn how to use a remote KMS in your Queryable Encryption implementation,
see the qe-tutorial-automatic-encryption guide.

To view a tutorial demonstrating how to use a Local Key Provider
for testing Queryable Encryption, see
qe-quick-start.

#### Architecture

When you use a Local Key Provider, your application retrieves your
Customer Master Key from the filesystem of the computer it runs on. The
following diagram describes the architecture of a Queryable Encryption-enabled
application using a Local Key Provider.

(Figure: /images/CSFLE_Data_Key_Local.png)

#### kmsProviders Object

The following table presents the structure of a `kmsProviders`
object for a Local Key Provider:

| Field | Required | Description |
|---|---|---|
| key | Yes | The master key used to encrypt/decrypt data keys. The master key is passed as a base64 encoded string. |

#### dataKeyOpts Object

When you use a Local Key Provider, you specify your Customer Master Key
through your `kmsProviders` object.
