<!-- Converted from core/csfle/reference/encryption-schemas.txt (reStructuredText). Includes are inlined. -->

# CSFLE Encryption Schemas

## Overview

**Note:** Enterprise Feature

The automatic feature of field level encryption is only available
in MongoDB Enterprise 4.2 or later, and MongoDB Atlas 4.2 or later
clusters. 

Encryption schemas contain user-specified rules that identify which 
fields must be encrypted and how to encrypt those fields. Applications 
must specify the automatic encryption rules using a strict subset of 
the [JSON Schema Draft 4 standard syntax](https://tools.ietf.org/html/draft-zyp-json-schema-04) and
the following encryption-specific keywords:

- Encrypt 
  specifies the encryption options to use when encrypting the current 
  field. 

- Encrypt Metadata specifies 
  inheritable encryption options.

For the MongoDB shell, use the `Mongo` constructor
to create the database connection with the automatic encryption rules
included as part of the Client-Side Field Level Encryption
configuration object.
See mongo-connection-automatic-client-side-encryption-enabled
for an example.

For the official MongoDB drivers, use the
driver-specific database connection constructor (`MongoClient`)
to create the database connection with the automatic encryption rules
included as part of the Client-Side Field Level Encryption
configuration object. To learn more about CSFLE-specific 
`MongoClient` options, see the mongo client page.

**Important:** Don't Specify Schema Validation Keywords In Your Encryption Schema

Do  **not** specify schema validation keywords in the automatic
encryption rules. To define schema validation rules, configure
schema validation.

## Definition

**`encrypt`**

*Object*

```json
"bsonType" : "object",
"properties" : {
  "<fieldName>" : {
    "encrypt" : {
      "algorithm" : "<string>",
      "bsonType" : "<string>" | [ "<string>" ],
      "keyId" : [ <UUID> ]
    }
  }
}
```

Indicates that `<fieldName>` must be encrypted. The `encrypt`
object has the following requirements:

- `encrypt` cannot have any sibling fields in the 
  `<fieldName>` object. `encrypt` must be the only child of the
  `<fieldName>` object.

- `encrypt` cannot be specified within any subschema of the
  `items` or `additionalItems` keywords. Specifically,
  automatic Client-Side Field Level Encryption does not support encrypting individual 
  elements of an array.

The `encrypt` object can contain **only** the
following fields:

- `algorithm`
- `bsonType`
- `keyId`

Including any other field to the `encrypt` object
results in errors when issuing automatically encrypted read or write
operations

If `keyId` or
`algorithm` are omitted, the
Shared Library checks all parent
fields and attempts to construct those options from the nearest
`encryptMetadata` object that specifies the
option. `bsonType` cannot be inherited
and *may* be required depending on the value of
`algorithm`.

If the Shared Library cannot construct the full `encrypt` object using
the fields specified to the object and any required
`encryptMetadata`-inherited keys, automatic encryption fails and
returns an error.

**`encrypt.algorithm`**

*String*

Indicates which encryption algorithm to use when encrypting
values of `<fieldName>`. Supports the following algorithms
*only*:

- `AEAD_AES_256_CBC_HMAC_SHA_512-Random`
- `AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic`

For complete documentation on the encryption algorithms, see
csfle-reference-encryption-algorithms.

If omitted, the Shared Library checks
all parent fields for the closest ancestor containing an
`encryptMetadata.algorithm` key and inherits that value.
If no parent `algorithm` exists, automatic
field level encryption fails and returns an error.

- If `encrypt.algorithm` or its inherited value is
  `AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic`,
  the `encrypt` object *requires* the 
  `encrypt.bsonType` field.

- If `encrypt.algorithm` or its inherited value is
  `AEAD_AES_256_CBC_HMAC_SHA_512-Random`,
  the `encrypt` object *may* include the 
  `encrypt.bsonType` field. 

**`encrypt.bsonType`**

*String | Array of Strings*

The BSON type of the field being encrypted.
Required if `encrypt.algorithm` is
`AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic`.

If `encrypt.algorithm` or its inherited value is
`AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic`, `bsonType`
*must* specify a *single* type.  `bsonType` does **not**
support any of the following BSON types with the deterministic
encryption algorithm:

- `double`
- `decimal128`
- `bool`
- `object`
- `array`

If `encrypt.algorithm` or its inherited value is
`AED_AES_256_CBC_HMAC_SHA_512-Random`, `bsonType` is
optional and may specify an array of supported bson types. For
fields with `bsonType` of `array` or `object`, the client
encrypts the *entire* array or object and not their individual
elements. 

`encrypt.bsonType` does **not** support the following types
regardless of `encrypt.algorithm` or its inherited
value:

- `minKey`
- `maxKey`
- `null`
- `undefined` 

**`encrypt.keyId`**

*Array of single UUID*

The UUID of the Data Encryption Key to use for encrypting field
values. The UUID is a BSON [binary data](http://bsonspec.org/spec.html) element of subtype `4`.

Specify *one* string inside the array.

If omitted, the Shared Library checks
all parent fields for the closest ancestor containing an 
`encryptMetadata.keyId` key and inherits
that value. If no parent 
`keyId` exists,
automatic field level encryption fails and returns an error.

The `keyId` or its inherited value *must*
exist in the Key Vault collection specified as  part of the auto encryption
configuration options.
If the specified Data Encryption Key does not exist, automatic
encryption fails.

Official MongoDB drivers have language-specific requirements for specifying 
the UUID. Defer to the driver documentation for complete documentation on implementing 
client-side field level encryption.

**`encryptMetadata`**

*Object*

```json
{
  "bsonType" : "object",
  "encryptMetadata" : {
    "algorithm" : "<string>",
    "keyId" : [ <UUID> ]
  },
  "properties" : {
    "encrypt" : {}
  }
}
```

Defines encryption options which an `encrypt`
object nested in the sibling `properties` may inherit. If an
`encrypt` is missing an option required to support
encryption, the Shared Library searches all parent objects
to locate an `encryptMetadata` object that
specifies the missing option.

`encryptMetadata` must be specified in subschemas with ``bsonType:
"object"`. `encryptMetadata`` cannot be specified to any subschema
of the `items` or `additionalItems` keywords. Specifically,
automatic Client-Side Field Level Encryption does not support
encrypting individual elements of an array.

The `encryptMetadata` object can contain *only* the
following fields. Including any other field to the `encrypt` object
results in errors when issuing automatically encrypted read or write
operations:

- `algorithm`
- `keyId`

**`encryptMetadata.algorithm`**

*String*

The encryption algorithm to use to encrypt a given field. If an
`encrypt` object is missing the
`algorithm` field, the Shared Library
searches all parent objects to locate an
`encryptMetadata` object that specifies
`encryptMetadata.algorithm`.

Supports the following algorithms *only*:

- `AEAD_AES_256_CBC_HMAC_SHA_512-Random`
- `AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic`

For complete documentation on the encryption algorithms, see
field-level-encryption-algorithms.

If specifying `AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic`, 
any `encrypt` object inheriting that value *must* specify
`encrypt.bsonType`.

**`encryptMetadata.keyId`**

*Array of single UUID*

The UUID of a Data Encryption Key. The UUID is a BSON [binary data](http://bsonspec.org/spec.html) element of subtype `4`.

Specify *one* string inside the array.

If an `encrypt` object is missing the 
`keyId` field, the Shared Library
searches all parent objects to locate 
an `encryptMetadata` object that
specifies `encryptMetadata.keyId`.

The Data Encryption Key *must* exist in the Key Vault collection specified as
part of the auto encryption configuration options. The specified configuration
options must *also* include appropriate access to the
Key Management Service (KMS) and
Customer Master Key (CMK) used to create the data key. Automatic
encryption fails if the Data Encryption Key does not exist *or* if the
client cannot decrypt the key with the specified KMS and CMK.

Official MongoDB drivers have language-specific requirements for specifying 
the UUID. Defer to the driver documentation for complete documentation on implementing 
client-side field level encryption.

## Examples

### Encryption Schema -  Multiple Fields

Consider a collection `MedCo.patients` where each document has
the following structure:

```none
{
  "fname" : "<String>",
  "lname" : "<String>",
  "passportId" : "<String>",
  "bloodType" : "<String>",
  "medicalRecords" : [
    {<object>}
  ],
  "insurance" : {
    "policyNumber" : "<string>",
    "provider" : "<string>"
  }
}
```

The following fields contains personally identifiable information (PII)
that may be queried:

- `passportId`
- `bloodType`
- `insurance.policyNumber`
- `insurance.provider`

The deterministic
encryption algorithm guarantees that the encrypted output of a value
remains static. This allows queries for a specific value to return
meaningful results at the cost of increased susceptibility to frequency
analysis recovery. The deterministic encryption algorithm therefore
meets both the encryption and queryability requirements of the data.

The following fields contain legally protected personally identifiable
information (PII) that may never be queried:

- `medicalRecords`

The randomized encryption
algorithm guarantees that the encrypted output of a value is always
unique. This prevents queries for a specific field value from returning
meaningful results while supporting the highest possible protection of
the field contents. The randomized encryption algorithm therefore meets
both the encryption and queryability requirements of the data.

The following schema specifies automatic encryption rules which meet the
above requirements for the `MedCo.patients` collection:

```json
{
  "MedCo.patients" : {
    "bsonType" : "object",
    "properties" : {
      "passportId" : {
        "encrypt" : {
          "keyId" : [UUID("bffb361b-30d3-42c0-b7a4-d24a272b72e3")],
          "algorithm" : "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic",
          "bsonType" : "string"
        }
      },
      "bloodType" : {
        "encrypt" : {
          "keyId" : [UUID("bffb361b-30d3-42c0-b7a4-d24a272b72e3")],
          "algorithm" : "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic",
          "bsonType" : "string"
        }
      },
      "medicalRecords" : {
        "encrypt" : {
          "keyId" : [UUID("f3821212-e697-4d65-b740-4a6791697c6d")],
          "algorithm" : "AEAD_AES_256_CBC_HMAC_SHA_512-Random",
          "bsonType" : "array"
        }
      },
      "insurance" : {
        "bsonType" : "object",
        "properties" : {
          "policyNumber" : {
            "encrypt" : {
              "keyId" : [UUID("bffb361b-30d3-42c0-b7a4-d24a272b72e3")],
              "algorithm" : "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic",
              "bsonType" : "string"
            }
          },
          "provider" : {
            "encrypt" : {
              "keyId" : [UUID("bffb361b-30d3-42c0-b7a4-d24a272b72e3")],
              "algorithm" : "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic",
              "bsonType" : "string"
            }
          }
        }
      }
    }
  }
}
```

The above automatic encryption rules mark the `passportId`,
`bloodType`, `insurance.policyNumber`, `insurance.provider`,
and `medicalRecords` fields for encryption. 

- The `passportId`, `bloodType`, `insurance.policyNumber`, and
  `provider` fields require deterministic encryption using the
  specified key.

- The `medicalRecords` field requires randomized encryption using the
  specified key. 

While Client-Side Field Level Encryption does not support encrypting
individual array elements, randomized encryption supports encrypting the
*entire* array field rather than individual elements in the field. The
example automatic encryption rules specify randomized encryption for the
`medicalRecords` field to encrypt the entire array. If the automatic
encryption rules specified `encrypt` or
`encryptMetadata` within `medicalRecords.items` or
`medicalRecords.additionalItems`, automatic field level encryption
fails and returns an errors.

The official MongoDB 4.2+ compatible drivers, `mongosh`,
and the 4.2 or later legacy `mongo` shell require specifying the 
automatic encryption rules as part of creating the database connection 
object:

- For `mongosh`, use the `Mongo()`
  constructor to create a database connection. Specify the automatic
  encryption rules to the `schemaMap` key of the
  autoEncryptionOpts parameter. See
  mongo-connection-automatic-client-side-encryption-enabled
  for a complete example.

- For the official MongoDB 4.2+ compatible drivers, use the
  driver-specific database connection constructor (`MongoClient`)
  to create the database connection with the automatic encryption rules
  included as part of the Client-Side Field Level Encryption
  configuration object. Defer to the driver API reference for more complete documentation and
  tutorials.

For all clients, the `keyVault` and `kmsProviders` specified
to the Client-Side Field Level Encryption parameter *must* grant
access to both the Data Encryption Keys specified in the automatic
encryption rules *and* the Customer Master Key used to encrypt the
Data Encryption Keys.

### Encryption Schema -  Multiple Fields With Inheritance

Consider a collection `MedCo.patients` where each document has
the following structure:

```none
{
  "fname" : "<String>",
  "lname" : "<String>",
  "passportId" : "<String>",
  "bloodType" : "<String>",
  "medicalRecords" : [
    {<object>}
  ],
  "insurance" : {
    "policyNumber" : "<string>",
    "provider" : "<string>"
  }
}
```

The following fields contain private data that may be queried:

- `passportId`
- `bloodType`
- `insurance.policyNumber`
- `insurance.provider`

The deterministic
encryption algorithm guarantees that the encrypted output of a value
remains static. This allows queries for a specific value to return
meaningful results at the cost of increased susceptibility to frequency
analysis recovery. The deterministic encryption algorithm therefore
meets both the encryption and queryability requirements of the data.

The following fields contain private data that may never be queried:

- `medicalRecords`

The randomized encryption
algorithm guarantees that the encrypted output of a value is always
unique. This prevents queries for a specific field value from returning
meaningful results while supporting the highest possible protection of
the field contents. The randomized encryption algorithm therefore meets
both the encryption and queryability requirements of the data.

The following schema specifies automatic encryption rules which meet the
encryption requirements for the `MedCo.patients` collection:

```json
{
  "MedCo.patients" : {
    "bsonType" : "object",
    "encryptMetadata" : {
      "keyId" : [UUID("6c512f5e-09bc-434f-b6db-c42eee30c6b1")],
      "algorithm" : "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic"
    },
    "properties" : {
      "passportId" : {
        "encrypt" : {
          "bsonType" : "string"
        }
      },
      "bloodType" : {
        "encrypt" : {
          "bsonType" : "string"
        }
      },
      "medicalRecords" : {
        "encrypt" : {
          "keyId" : [UUID("6c512f5e-09bc-434f-b6db-c42eee30c6b1")],
          "algorithm" : "AEAD_AES_256_CBC_HMAC_SHA_512-Random",
          "bsonType" : "array"
        }
      },
      "insurance" : {
        "bsonType" : "object",
        "properties" : {
          "policyNumber" : {
            "encrypt" : {
              "bsonType" : "string"
            }
          },
          "provider" : {
            "encrypt" : {
              "bsonType" : "string"
            }
          }
        }
      }
    }
  }
}
```

The above automatic encryption rules mark the `passportId`,
`bloodType`, `insurance.policyNumber`, `insurance.provider`,
and `medicalRecords` fields for encryption. 

- The `passportId`, `bloodType`, `insurance.policyNumber`, and
  `provider` fields inherit their encryption settings from the parent
  `encryptMetadata` field. Specifically, these fields inherit
  the `algorithm` and
  `keyId` values specifying
  deterministic encryption with the specified Data Encryption Key.

- The `medicalRecords` field requires randomized encryption using the
  specified key. The `encrypt` options override those specified
  in the parent `encryptMetadata` field.

While Client-Side Field Level Encryption does not support encrypting
individual array elements, randomized encryption supports encrypting the
*entire* array field rather than individual elements in the field. The
example automatic encryption rules specify randomized encryption for the
`medicalRecords` field to encrypt the entire array. If the automatic
encryption rules specified `encrypt` or
`encryptMetadata` within `medicalRecords.items` or
`medicalRecords.additionalItems`, automatic field level encryption
fails and returns an errors.

The official MongoDB 4.2+ compatible drivers, `mongosh`,
and the 4.2 or later legacy `mongo` shell require specifying the 
automatic encryption rules as part of creating the database connection 
object:

- For `mongosh`, use the `Mongo()`
  constructor to create a database connection. Specify the automatic
  encryption rules to the `schemaMap` key of the
  autoEncryptionOpts parameter. See
  mongo-connection-automatic-client-side-encryption-enabled
  for a complete example.

- For the official MongoDB 4.2+ compatible drivers, use the
  driver-specific database connection constructor (`MongoClient`)
  to create the database connection with the automatic encryption rules
  included as part of the Client-Side Field Level Encryption
  configuration object. Defer to the driver API reference for more complete documentation and
  tutorials.

For all clients, the `keyVault` and `kmsProviders` specified
to the Client-Side Field Level Encryption parameter *must* grant
access to both the Data Encryption Keys specified in the automatic
encryption rules *and* the Customer Master Key used to encrypt the
Data Encryption Keys.

To learn more about your CMK and Key Vault collection, 
see the key vaults page.

To learn more about encryption algorithms, 
see the Encryption algorithms page.

To learn more about CSFLE-specific `MongoClient` options, 
see the mongo client page.

### Encryption Schema -  Encrypt with Pattern Properties

You can use the `patternProperties` keyword in your encryption schema to 
define encryption rules for all fields with names that match a regular expression.

Consider a collection `MedCo.patients` where each document has
the following structure:

```none
{
  "fname" : "<string>",
  "lname" : "<string>",
  "passportId_PIIString" : "<string>",
  "bloodType_PIIString" : "<string>",
  "medicalRecords_PIIArray" : [
    {<object>}
  ],
  "insurance" : {
    "policyNumber_PIINumber" : "<number>",
    "provider_PIIString" : "<string>"
  }
}
```

The fields that contain private data are identified by a "_PII<type>" 
tag appended the end of the field name.

- `passportId_PIIString`
- `bloodType_PIIString`
- `medicalRecords_PIIArray`
- `insurance.policyNumber_PIINumber`
- `insurance.provider_PIIString`

You can use the `patternProperties` keyword to configure these fields for 
encryption, without identifying each field individually, and without using the 
full field name. Do this by using regular expressions that match all fields that 
end with the "_PII<type>" tag.

The following JSON schema uses `patternProperties` and regular expressions to 
specify which fields to encrypt.

```json
{
  "MedCo.patients": {
  "bsonType": "object",
  "patternProperties": {
    "_PIIString$": {
      "encrypt": {
        "keyId": [UUID("6c512f5e-09bc-434f-b6db-c42eee30c6b1")],
        "bsonType": "string",
        "algorithm": "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic",
      },
    },
    "_PIIArray$": {
      "encrypt": {
        "keyId": [UUID("6c512f5e-09bc-434f-b6db-c42eee30c6b1")],
        "bsonType": "array",
        "algorithm": "AEAD_AES_256_CBC_HMAC_SHA_512-Random",
      },
    },
    "insurance": {
      "bsonType": "object",
      "patternProperties": {
        "_PIINumber$": {
          "encrypt": {
            "keyId": [UUID("6c512f5e-09bc-434f-b6db-c42eee30c6b1")],
            "bsonType": "int",
            "algorithm": "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic",
          },
        },
        "_PIIString$": {
          "encrypt": {
            "keyId": [UUID("6c512f5e-09bc-434f-b6db-c42eee30c6b1")],
            "bsonType": "string",
            "algorithm": "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic",
          },
        },
      },
    },
  },
  },
}
```

The above automatic encryption rules mark the `passportId_PIIString`, 
`bloodType_PIIString`, `medicalRecords_PIIArray`, `insurance.policyNumber_PIINumber`,
`insurance.provider_PIIString` fields for encryption.

To Learn more about the `patternProperties` keyword, see
csfle-fundamentals-pattern-properties.
