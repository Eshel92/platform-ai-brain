<!-- Converted from core/security-transport-encryption.txt (reStructuredText). Includes are inlined. -->

# TLS/SSL (Transport Encryption)

## TLS/SSL

MongoDB supports TLS/SSL (Transport Layer Security/Secure Sockets Layer)
to encrypt all of MongoDB's network traffic. TLS/SSL ensures that
MongoDB network traffic is only readable by the intended client.

Starting in MongoDB 7.0 and 6.0.7, MongoDB supports OpenSSL 3.0 and the
OpenSSL FIPS provider with these operating systems:

- Red Hat Enterprise Linux 9
- Amazon Linux 2023
- Ubuntu Linux 22.04

To configure your deployment to use TLS, follow the quickstart.

### TLS Versions

MongoDB disables support for TLS 1.0
encryption on systems where TLS 1.1+ is available. 

### TLS Libraries

MongoDB uses the native TLS/SSL OS libraries:

| Platform | TLS/SSL Library |
|---|---|
| Windows | Secure Channel (Schannel) |
| Linux/BSD | OpenSSL |
| macOS | Secure Transport |

## TLS/SSL Ciphers

MongoDB's TLS/SSL encryption only allows use of strong TLS/SSL ciphers
with a minimum of 128-bit key length for all connections.

### Forward Secrecy

Forward Secrecy cipher suites create an ephemeral session key that is
protected by the server's private key but is never transmitted. The use
of an ephemeral key ensures that even if a server's private key is
compromised, you cannot decrypt past sessions with the compromised key.

MongoDB supports Forward Secrecy cipher suites that use Ephemeral
Diffie-Hellman (DHE) and Ephemeral Elliptic Curve Diffie-Hellman
(ECDHE) algorithms.

#### Ephemeral Elliptic Curve Diffie-Hellman (ECDHE)

| Platform | Level of Support |
|---|---|
| Linux | If the Linux platform's OpenSSL supports automatic curve selection, MongoDB enables support for Ephemeral Elliptic Curve Diffie-Hellman (ECDHE). Else if the Linux platform's OpenSSL does not support automatic curve selection, MongoDB attempts to enable ECDHE support using `prime256v1` as the named curve. |
| Windows | Ephemeral Elliptic Curve Diffie-Hellman (ECDHE) is implicitly supported through the use of Secure Channel (Schannel), the native Windows TLS/SSL library. |
| macOS | Ephemeral Elliptic Curve Diffie-Hellman (ECDHE) is implicitly supported through the use of Secure Transport, the native macOS TLS/SSL library. |

ECDHE cipher suites are slower than static RSA cipher suites. For
better performance with ECDHE, you can use certificates that use
Elliptic Curve Digital Signature Algorithm (`ECDSA`). See also
forward-secrecy-performance for more information.

#### Ephemeral Diffie-Hellman (DHE)

* - Platform
  - Level of Support

* - Linux

  - MongoDB enables support for Ephemeral Diffie-Hellman (DHE):

    - If the `opensslDiffieHellmanParameters` is set at
      startup (regardless of whether ECDHE is enabled
      or disabled).

    - Else, if the `opensslDiffieHellmanParameters`
      parameter is unset but if ECDHE is enabled,
      MongoDB enables DHE using the `ffdhe3072` parameter, as
      defined in 7919#appendix-A.2.

* - Windows

  - Ephemeral Diffie-Hellman (DHE) is implicitly supported through the use 
    of Secure Channel (Schannel), the native Windows TLS/SSL library.

* - macOS

  - Ephemeral Diffie-Hellman (DHE) is implicitly supported through the use 
    of Secure Transport, the native macOS TLS/SSL library.

**Note:**

If clients negotiate a cipher suite with DHE but cannot accept the
server selected parameter, the TLS connection fails.

Strong parameters (i.e. size is greater than 1024) are not supported
with Java 6 and 7 unless extended support has been purchased from
Oracle. However, Java 7 supports and prefers ECDHE, so will
negotiate ECDHE if available.

DHE (and ECDHE) cipher suites are slower performance than static
RSA cipher suites, with DHE being significantly slower than ECDHE. See
forward-secrecy-performance for more information.

#### Forward Secrecy Performance

DHE and ECDHE cipher suites are slower than static RSA cipher suites,
with DHE being significantly slower than ECDHE.

For better performance with ECDHE, you can use certificates that
use Elliptic Curve Digital Signature Algorithm (`ECDSA`).
Alternatively, you can disable ECDHE cipher suites with the
`opensslCipherConfig` parameter as in the following example
(which also disables DHE):

```bash
mongod --setParameter opensslCipherConfig='HIGH:!EXPORT:!aNULL:!kECDHE:!ECDHE:!DHE:!kDHE@STRENGTH'
```

If you need to disable support for DHE cipher suites due to
performance, you can use the `opensslCipherConfig`
parameter, as in the following example:

```bash
mongod --setParameter opensslCipherConfig='HIGH:!EXPORT:!aNULL:!DHE:!kDHE@STRENGTH'
```

## Certificates

To use TLS with MongoDB, you must have TLS certificates. See tls-certificate-tutorial.

### Certificate Expiry Warning

`mongod` / `mongos` logs a warning on
connection if the presented X.509 certificate expires within `30`
days of the `mongod/mongos` host system time.

### OCSP (Online Certificate Status Protocol)

Starting in MongoDB 6.0, if `ocspEnabled` is set to `true` during 
initial sync, all nodes must be able to reach the OCSP 
responder.

If a member fails in the `STARTUP2` state, set 
`tlsOCSPVerifyTimeoutSecs` to a value that is less than `5`. 

To check for certificate revocation, MongoDB `enables` 
the use of OCSP (Online Certificate Status Protocol) by default. The use of 
OCSP eliminates the need to periodically download a 
`Certificate Revocation List (CRL)` and restart the
`mongod` / `mongos` with the updated CRL.

(Text shared from another MongoDB docs repo, not available offline: server/lets-encrypt-ocsp-note.rst)

As part of its OCSP support, MongoDB supports the following on
Linux:

- [OCSP stapling](https://tools.ietf.org/html/rfc6961). With OCSP
  stapling, `mongod` and `mongos` instances
  attach or "staple" the OCSP status response to their certificates
  when providing these certificates to clients during the TLS/SSL
  handshake. OCSP stapling removes the need for clients to make a
  separate request to retrieve the OCSP status of the provided
  certificate. The OCSP status response is included with the
  certificates.

- [OCSP must-staple extension](https://tools.ietf.org/html/rfc7633).
  OCSP must-staple is an extension that can be added to the server
  certificate that tells the client to expect an OCSP staple when it
  receives a certificate during the TLS/SSL handshake.

MongoDB also provides the following OCSP-related parameters:

| Parameter | Description |
|---|---|
| `ocspEnabled` | Enables or disables the OCSP support. |
| `ocspStaplingRefreshPeriodSecs` | Specifies the number of seconds to wait before refreshing the stapled OCSP status response. |
| `tlsOCSPStaplingTimeoutSecs` | Specifies the maximum number of seconds the `mongod` / `mongos` instance should wait to receive the OCSP status response for its certificates. |
| `tlsOCSPVerifyTimeoutSecs` | Specifies the maximum number of seconds that the `mongod` / `mongos` should wait for the OCSP response when verifying client certificates. |

You can set these parameters at startup using the
`setParameter` configuration file setting or the
`--setParameter` command line option.

**Note:**

Starting in MongoDB 5.0, the `rotateCertificates` command
and `db.rotateCertificates()` method will also refresh any
stapled OCSP responses.

## FIPS Mode

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

The Federal Information Processing Standard (FIPS) is a U.S. government
computer security standard used to certify software modules and libraries
that encrypt and decrypt data securely. You can configure MongoDB to run
with a FIPS 140-2 certified library for OpenSSL. Configure FIPS to run by
default or as needed from the command line.

For an example, see /tutorial/configure-fips.
