<!-- Converted from core/queryable-encryption/features.txt (reStructuredText). Includes are inlined. -->

# Features

## Overview

On this page, you can learn about the security benefits of Queryable Encryption,
how it works, and how it compares to other security mechanisms supported
by MongoDB. You can also view a fictional scenario that demonstrates the
value of Queryable Encryption in securing your data.

## Queryable Encryption

Queryable Encryption is a feature of MongoDB that enables a client application to
encrypt data before transporting it over the network using fully
randomized encryption, while maintaining queryability.
Sensitive data is transparently encrypted and decrypted by the client
and only communicated to and from the server in encrypted form.
The security guarantees for sensitive fields containing both low
cardinality (low-frequency) data and high cardinality data are identical

Unlike Client-Side Field Level Encryption
that can use Deterministic Encryption,
Queryable Encryption uses fast, searchable encryption schemes based on structured encryption.
These schemes produce different encrypted output values even when given
the same cleartext input.

## Security Considerations

* Queryable Encryption doesn't provide any cryptographic integrity
  guarantees against adversaries with access to your Customer Master Key or
  Data Encryption Keys.
  
* Queryable Encryption doesn't provide any cryptographic integrity
  guarantees against adversaries with arbitrary write access to collections
  containing encrypted data.
 
* MongoDB uses schema validation to enforce
  encryption of specific fields in a collection. Without a client-side schema,
  the client downloads the server-side schema for the collection to determine 
  which fields to encrypt. To avoid this issue, use client-side schema validation.
  
  Because Queryable Encryption doesn't provide a mechanism to verify
  the integrity of a schema, relying on a server-side schema means
  trusting that the server's schema has not been tampered with. If an adversary
  compromises the server, they can modify the schema so that a previously
  encrypted field is no longer labeled for encryption. This causes the client 
  to send plaintext values for that field.

  For an example of configuration for client and server-side
  schemas, see the CSFLE example at CSFLE Server-Side Field Level Encryption Enforcement.

## How Queryable Encryption Works

The diagram below shows the process and architecture of how Queryable Encryption is
used in a customer environment.

(Figure: /images/QE-how-it-works.png)

In this diagram, the user is able to query on fully randomly encrypted
data such as SSN number.

The process and mechanisms that makes this possible within the
Queryable Encryption framework are as follows:

1. When the application submits the query, MongoDB drivers first analyze
   the query.

2. The driver recognizes the query is against an encrypted field and
   requests the encryption keys from the customer-provisioned key
   provider such as:

   - AWS Key Management Service (AWS KMS)
   - Google Cloud KMS
   - Azure Key Vault
   - Any {+kmip-hover+}-compliant key provider

3. The driver submits the query to the MongoDB server with the encrypted
   fields rendered as ciphertext.

4. Queryable Encryption implements a fast, searchable scheme that allows
   the server to process queries on fully encrypted data, without knowing
   anything about the data. The data and the query itself remain encrypted
   at all times on the server.

5. The MongoDB server returns the encrypted results of the query to the
   driver.

6. The query results are decrypted with the keys held by the driver and
   returned to the client and shown as plaintext.

Queryable Encryption functions with the help of the following data structures. It is critical
that these are not modified or deleted, or query results will be incorrect.

- Queryable Encryption adds a `__safeContent__` field to documents in any collection where there's a Queryable Encryption
  encrypted field.
- Queryable Encryption creates three metadata collections in the same database as the collection where there's a
  Queryable Encryption encrypted field. These are named as follows:

  - `enxcol_.<collectionName>.esc`
  - `enxcol_.<collectionName>.ecc`
  - `enxcol_.<collectionName>.ecoc`

**Warning:**

Do not modify these data structures or query results will be incorrect
and security could be impacted.

Queryable Encryption keeps encrypted fields secure in the following scenarios:

- Direct access to encrypted fields by a database superuser
- Access to encrypted fields by reading the server's memory
- Capture of encrypted fields over an insecure network
- Access to on-disk encrypted fields by reading database or backup files
- Frequency analysis attacks by identifying patterns in encrypted documents

While all clients have access to the non-sensitive data fields,
only appropriately-configured Queryable Encryption clients are able to run
read and write queries using the encrypted data fields.

**Important:** Remote Key Management System

When you use Queryable Encryption in production, you must use a remote
Key Management System (KMS) to store your encryption key.

To view a step-by-step guide demonstrating how to use a remote KMS with
Queryable Encryption, see qe-tutorial-automatic-encryption.

To view a list of all supported KMS providers, see
qe-fundamentals-kms-providers.

To learn more about why you should use a remote KMS, see
qe-reasons-to-use-remote-kms.

## Other Security Mechanisms

This section describes the following security mechanisms supported by
MongoDB and explains their use cases and limitations:

- qe-features-role-based-access-control
- qe-features-encryption-at-rest
- qe-features-transport-encryption

### Role-Based Access Control

Role-Based Access Control is a security mechanism that
allows administrators to grant and restrict collection-level permissions
for users. With the appropriate role definition and assignment, this
solution prevents accidental disclosure of data and access.

Role-Based Access control cannot protect against the following scenarios:

- Capture of the data over an insecure network
- Access to on-disk data by reading database or backup files
- Access to data by reading the server's memory
- Direct access to data by a database superuser

To learn more, see
Role-Based Access Control.

### Encryption at Rest

Encryption at Rest is a mechanism that encrypts database files on disk.
This mechanism prevents a person who lacks database credentials, but has
access to the computer hosting your database, from viewing your data.

This mechanism does not protect your data against the following scenarios:

- Capture of the data over an insecure network
- Access to data by reading the server's memory
- Direct access to data by a database superuser

To learn more, see
Encryption at Rest.

### Transport Encryption (TLS/SSL)

Transport Encryption using TLS/SSL encrypts your data over the network.
TLS/SSL protects your data as it travels over an insecure network, but
cannot protect your data from a privileged user or as it sits on disk.

To learn more, see
Transport Encryption using TLS/SSL

## Comparison of Features

The following diagram describes security features MongoDB supports and
the potential security vulnerabilities that they address:

(Figure: /images/QE_Security_Feature_Chart.png)

**Important:** Use the Mechanisms Together

To secure a production deployment, use Role-Based Access
Control, Encryption at Rest, Transport Encryption, and optionally, the
In-Use Encryption security mechanisms together. Please note that you cannot
use both Client-Side Field Level Encryption and Queryable Encryption to encrypt different fields in the same
collection.

To learn more about Client-Side Field Level Encryption, see Client-Side Field Level Encryption Features.

## Scenario

The following fictional scenario demonstrates the value of Queryable Encryption
in securing your application's data, and how
Queryable Encryption interacts with the other security mechanism discussed
in this guide.

In this scenario, we secure sensitive data on a medical care management
system that stores patients' personal information, billing
information, and medical records for a fictional company, *MedcoMD*.
None of the patient data is public, and specific data such as their
social security number (SSN, a US government-issued ID number), patient ID number,
billing information, and medication information are particularly sensitive and
subject to privacy compliance. It is important for the company and the patient
that the data is kept private and secure.

MedcoMD needs this system to satisfy the following use cases:

- Doctors use the system to access patients' medical records, billing
  information, and update medications.

- Receptionists use the system to verify patients' identities
  using their contact information.

- Receptionists can view a patient's billing information, but not
  their patient ID number.

- Receptionists cannot access a patient's medical records.

MedcoMD is also concerned with the disclosure of sensitive data through any
of the following methods:

- Accidental disclosure of data on a receptionist's publicly-viewable
  screen.

- Direct access to the database by a superuser such as a database
  administrator.

- Capture of data over an insecure network.

- Access to data by reading the database server's memory.

- Access to data by reading database or backup files.

What can MedcoMD do to balance the functionality and access restrictions
of their medical care management system?

### Solution

MedcoMD uses the following security mechanisms to satisfy their use cases
and protect against the disclosure of sensitive medical data:

- Transport Encryption (TLS/SSL)
  to secure data as it travels over the network.
- Encryption at Rest
  to protect against disclosure of data by reading database
  or backup files.
- Role-Based Access Control
  to limit the access of database users to the collections necessary for them
  to perform their tasks.
- Encrypting sensitive fields with Queryable Encryption to satisfy the following
  use cases and constraints:

  * Prevent reading data from server memory as the
    Queryable Encryption encrypted data is never on the database server in
    an unencrypted form.
  * Allow receptionists to verify patients' identities and
    prevent accidental disclosure of sensitive data on a receptionist's
    publicly viewable screen by providing receptionists with a client
    that is not Queryable Encryption enabled.
  * Allow doctors to view sensitive data privately in their offices
    by providing doctors with a Queryable Encryption enabled client.

## Learn More

To view a list of security measures you should implement to protect
your MongoDB deployment, see the
Security Checklist.

To start using Queryable Encryption, see the qe-quick-start.
