<!-- Converted from core/csfle/reference/decryption.txt (reStructuredText). Includes are inlined. -->

# How CSFLE Decrypts Documents

This page describes how CSFLE uses metadata from your
Data Encryption Key and Customer Master Key to decrypt data.

## Metadata Used for Decryption

When you encrypt data using CSFLE, the data you encrypt is
stored as a `BinData` subtype 6 object that includes
the following metadata:

- The `_id` of the Data Encryption Key used to encrypt the data
- The encryption algorithm used to encrypt the data

Data Encryption Keys contain metadata that describes what Customer Master Key was used
to encrypt them.

Drivers and `mongosh` use this metadata to attempt
to automatically decrypt your data.

## Automatic Decryption Process

To automatically decrypt your data, your CSFLE-enabled client
performs the following procedure:

#. Check the `BinData` blob metadata of the field you intend to
   decrypt for the Data Encryption Key and encryption algorithm used to encrypt
   the value.

#. Check the Key Vault collection configured in the current database
   connection for the specified Data Encryption Key. If the Key Vault collection
   does not contain the specified key, automatic decryption fails and
   the driver returns an error.

#. Check the Data Encryption Key metadata for the Customer Master Key
   (CMK) used to encrypt the key material.

#. Decrypt the Data Encryption Key. This process varies by KMS provider:

   **aws:**

   For the Amazon Web Services (AWS) KMS, send the Data Encryption Key to
   your AWS KMS instance for decryption. If the CMK does not exist
   *or* if the connection configuration does not grant access to
   the CMK, decryption fails and the driver returns an error.

   **Tip:**

   To learn how to use the Amazon Web Services KMS for
   automatic encryption, see
   csfle-tutorial-automatic-aws.

   **gcp:**

   For the Google Cloud Platform (GCP) KMS, send the Data Encryption Key
   to your GCP KMS instance for decryption. If the CMK does not
   exist *or* if the connection configuration does not grant
   access to the CMK, decryption fails and the driver returns an
   error.

   **Tip:**

   To learn how to use the Google Cloud Platform KMS for automatic
   encryption, see csfle-tutorial-automatic-gcp.

   **azure:**

   For the Azure Key Vault, send the Data Encryption Key to the your
   Azure Key Vault instance for decryption. If the CMK does not exist
   *or* if the connection configuration does not grant access to
   the CMK, decryption fails and the driver returns an error.

   **Tip:**

   To learn how to use the Azure Key Vault for automatic
   encryption, see csfle-tutorial-automatic-azure.

   **kmip:**

   For a KMIP-compliant KMS, retrieve the CMK from the KMS and
   then use the CMK locally to decrypt the Data Encryption Key. If the
   CMK does not exist *or* if the connection configuration does
   not grant access to the CMK, decryption fails and the driver
   returns an error.

   **Tip:**

   To learn how to use a KMIP-compliant KMS for automatic
   encryption, see csfle-tutorial-automatic-kmip.

   **local:**

   For a Local Key Provider, retrieve the CMK from your filesystem
   and use it to decrypt the Data Encryption Key. If the local key specified in
   the database configuration was not used to encrypt the
   Data Encryption Key, decryption fails and the driver returns an
   error.

   **Warning:** Do Not Use the Local Key Provider in Production

   The Local Key Provider is an insecure method of storage and is
   **not recommended** for production. Instead,
   you should store your Customer Master Keys in a remote
   Key Management System
   (KMS).

   To learn how to use a remote KMS in your CSFLE implementation,
   see the csfle-tutorial-automatic-encryption guide.

#. Decrypt the `BinData` value using the decrypted
   Data Encryption Key and appropriate algorithm.

Applications with access to the MongoDB server that do not *also* have
access to the required CMK and Data Encryption Keys cannot
decrypt the `BinData` values.

## Automatically Encrypted Read Behavior

For read operations, the driver encrypts field values in the query
document using your encryption schema *prior* to issuing the read
operation.

Your client application then uses the `BinData` metadata to
automatically decrypt the document you receive from MongoDB.

To learn more about encryption schemas, see
csfle-fundamentals-create-schema.

## Learn More

To learn how to configure the database connection for Client-Side Field Level Encryption, see
csfle-reference-mongo-client.

To learn more about the relationship between Data Encryption Keys and
Customer Master Keys, see csfle-reference-keys-key-vaults.
