<!-- Converted from core/security-scram.txt (reStructuredText). Includes are inlined. -->

# SCRAM

Salted Challenge Response Authentication Mechanism (SCRAM) is the
default authentication mechanism for MongoDB.

When a user authenticates
themselves, MongoDB uses SCRAM to verify the supplied user credentials
against the user's `name`,
`password` and
`authentication database`.

SCRAM is based on the IETF [RFC 5802](https://tools.ietf.org/html/rfc5802) standard that defines best
practices for challenge-response authentication with passwords.

**Important:**

You cannot use both SCRAM authentication and another authentication type for the same user.

## Features

The SCRAM implementation in MongoDB provides:

- A tunable work factor (the iteration count)
- Per-user random salts
- Bi-directional authentication between server and client

### SCRAM Mechanisms

MongoDB supports the following SCRAM mechanisms:

| SCRAM Mechanism | Description |
|---|---|
| `SCRAM-SHA-1` | Uses the SHA-1 hashing function. To modify the iteration count for `SCRAM-SHA-1`, see `scramIterationCount`. |
| `SCRAM-SHA-256` | Uses the SHA-256 hashing function. To modify the iteration count for `SCRAM-SHA-256`, see `scramSHA256IterationCount`. |

When you create or update a SCRAM user, you can indicate:

- the SCRAM mechanism to use
- whether the server or the client digests the password

When you use `SCRAM-SHA-256`, MongoDB requires server-side password
hashing, which means that the server digests the password. For more
information, see `db.createUser()` and
`db.updateUser()`.

## Driver Support

The minimum driver versions that support `SCRAM` are:

| Driver Language | Version | Driver Language | Version |
|---|---|---|---|
| `C` | [1.1.0](https://github.com/mongodb/mongo-c-driver/releases) | `PHP` | [1.0](https://pecl.php.net/package/mongodb) |
| `C++` | [1.0.0](https://github.com/mongodb/mongo-cxx-driver/releases) | `Python` | [2.8](https://pypi.python.org/pypi/pymongo/) |
| `C#` | [1.10](https://github.com/mongodb/mongo-csharp-driver/releases) | `Perl` | [1.0.0](https://metacpan.org/release/MongoDB) |
| `Go` | [1.0.0](https://github.com/mongodb/mongo-go-driver/releases) | `Ruby` | [1.12](https://rubygems.org/gems/mongo) |
| `Java` | [2.13](https://github.com/mongodb/mongo-java-driver/releases) | `Rust` | [1.0.0](https://github.com/mongodb/mongo-rust-driver/releases) |
| `Motor` | [0.4](https://pypi.python.org/pypi/motor/) | `Scala` | [2.8.0](https://github.com/mongodb/casbah/releases) |
| `Node.js` | [1.4.29](https://github.com/mongodb/node-mongodb-native/releases) | `Swift` | [1.0.0](https://github.com/mongodb/mongo-swift-driver/releases) |

## Additional Information

If you use SCRAM-SHA-1:

- md5 is necessary but is not used for cryptographic purposes,
  and

- if you use FIPS mode, then instead of
  SCRAM-SHA-1 use:

  - SCRAM-SHA-256,
  - Kerberos,
  - LDAP, or
  - X.509
