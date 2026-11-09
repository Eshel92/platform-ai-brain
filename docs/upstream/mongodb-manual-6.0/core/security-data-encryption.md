<!-- Converted from core/security-data-encryption.txt (reStructuredText). Includes are inlined. -->

# Encryption

MongoDB provides the following encryption methods:

- security-in-use-encryption
- security-encryption-at-rest
- transport-encryption

## Encryption at Rest

Encryption at rest, when used in conjunction with transport encryption
and security policies that protect relevant accounts, passwords, and
encryption keys, can help ensure compliance with security and privacy
standards, including HIPAA, PCI-DSS, and FERPA.

For more information, see security-encryption-at-rest.

## TLS/SSL (Transport Encryption)

MongoDB supports TLS/SSL (Transport Layer Security/Secure Sockets Layer)
to encrypt all of MongoDB's network traffic. TLS/SSL ensures that
MongoDB network traffic is only readable by the intended client.

For more information, see transport-encryption.
