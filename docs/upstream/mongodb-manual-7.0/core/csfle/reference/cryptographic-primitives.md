<!-- Converted from core/csfle/reference/cryptographic-primitives.txt (reStructuredText). Includes are inlined. -->

# Cryptographic Primitives

MongoDB encrypts all fields in CSFLE with the [AEAD](https://en.wikipedia.org/w/index.php?title=Authenticated_encryption&oldid=1079879470#Authenticated_encryption_with_associated_data_(AEAD))
AES-256-CBC encryption algorithm.

- If you specify deterministic encryption for a field, your application
  passes a deterministic initialization vector to AEAD.
  
- If you specify random encryption for a field, your application passes
  a random initialization vector to AEAD.

**Note:** Authenticated Encryption

MongoDB CSFLE uses the  [encrypt-then-MAC](https://en.wikipedia.org/wiki/Authenticated_encryption#Encrypt-then-MAC_(EtM))
approach to perform authenticated encryption. Both Queryable Encryption and
CSFLE use the HMAC-SHA-256 algorithm to generate your
MAC.
