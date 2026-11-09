<!-- Converted from appendix/security/appendixB-openssl-server.txt (reStructuredText). Includes are inlined. -->

# Appendix B - OpenSSL Server Certificates for Testing Self-Managed Deployments

**Warning:** Disclaimer

This page is provided for testing purposes only and the
certificates are for testing purposes only.

The following tutorial provides some basic steps for creating
test X.509 certificates:

- Do not use these certificates for production. Instead, follow your
  security policies.

- For information on OpenSSL, refer to the official OpenSSL docs.
  Although this tutorial uses OpenSSL, the material should not be
  taken as an authoritative reference on OpenSSL.

## Prerequisite

The procedure outlined on this page uses the test intermediate authority
certificate and key `mongodb-test-ia.crt` and `mongodb-test-ia.key`
created in /appendix/security/appendixA-openssl-ca .

## Procedure

The following procedure outlines the steps to create test certificates
for MongoDB servers. For steps to create test certificates for MongoDB
clients, see /appendix/security/appendixC-openssl-client.

### A. Create the OpenSSL Configuration File

#. Create a test configuration file `openssl-test-server.cnf` for
   your server with the following content:

   ```cfg
   # NOT FOR PRODUCTION USE. OpenSSL configuration file for testing.

   [ req ]
   default_bits = 4096
   default_keyfile = myTestServerCertificateKey.pem    ## The default private key file name.
   default_md = sha256
   distinguished_name = req_dn
   req_extensions = v3_req

   [ v3_req ]
   subjectKeyIdentifier  = hash
   basicConstraints = CA:FALSE
   keyUsage = critical, digitalSignature, keyEncipherment
   nsComment = "OpenSSL Generated Certificate for TESTING only.  NOT FOR PRODUCTION USE."
   extendedKeyUsage  = serverAuth, clientAuth
   subjectAltName = @alt_names

   [ alt_names ]
   DNS.1 =         ##TODO: Enter the DNS names. The DNS names should match the server names.
   DNS.2 =         ##TODO: Enter the DNS names. The DNS names should match the server names.
   IP.1 =          ##TODO: Enter the IP address.
   IP.2 =          ##TODO: Enter the IP address. 

   [ req_dn ]
   countryName = Country Name (2 letter code)
   countryName_default = TestServerCertificateCountry
   countryName_min = 2
   countryName_max = 2

   stateOrProvinceName = State or Province Name (full name)
   stateOrProvinceName_default = TestServerCertificateState
   stateOrProvinceName_max = 64

   localityName = Locality Name (eg, city)
   localityName_default = TestServerCertificateLocality
   localityName_max = 64

   organizationName = Organization Name (eg, company)
   organizationName_default = TestServerCertificateOrg
   organizationName_max = 64

   organizationalUnitName = Organizational Unit Name (eg, section)
   organizationalUnitName_default = TestServerCertificateOrgUnit
   organizationalUnitName_max = 64

   commonName = Common Name (eg, YOUR name)
   commonName_max = 64
   ```

#. In the `[alt_names]` section, enter the appropriate
   DNS names and/or IP addresses for the MongoDB server. You can
   specify multiple DNS names for a MongoDB server.
   
   For OpenSSL SAN identifiers, MongoDB supports:

   - DNS names and/or
   - IP address fields 

#. *Optional*. You can update the default Distinguished Name (DN)
   values. 

**Tip:**

- Specify a non-empty value for at least one of the following
  attributes: Organization (`O`), the Organizational Unit
  (`OU`), or the Domain Component (`DC`).

- When creating test server certificates for internal membership
  authentication, the following attributes, if specified, must match
  exactly across the member certificates: Organization (`O`),
  Organizational Unit (`OU`), the Domain Component (`DC`).

  For more information on requirements for internal membership
  authentication, see membership authentication.

### B. Generate the Test PEM File for Server

**Important:**

Before proceeding, ensure that you have entered the
appropriate DNS names in the `[alt_names]` section of the
configuration file `openssl-test-server.cnf`.

#. Create the test key file `mongodb-test-server1.key`.

   ```bash
   openssl genrsa -out mongodb-test-server1.key 4096
   ```

#. Create the test certificate signing request `mongodb-test-server1.csr`.

   When asked for Distinguished Name values, enter the appropriate
   values for your test certificate:

   - Specify a non-empty value for at least one of the following
     attributes: Organization (`O`), the Organizational Unit
     (`OU`), or the Domain Component (`DC`).

   - When creating test server certificates for internal membership
     authentication, the following attributes, if specified, must match
     exactly across the member certificates: Organization (`O`),
     Organizational Unit (`OU`), the Domain Component (`DC`).

   ```bash
   openssl req -new -key mongodb-test-server1.key -out mongodb-test-server1.csr -config openssl-test-server.cnf
   ```

#. Create the test server certificate `mongodb-test-server1.crt`.

   ```bash
   openssl x509 -sha256 -req -days 365 -in mongodb-test-server1.csr -CA mongodb-test-ia.crt -CAkey mongodb-test-ia.key -CAcreateserial -out mongodb-test-server1.crt -extfile openssl-test-server.cnf -extensions v3_req
   ```

#. Create the test PEM file for the server.

   ```bash
   cat mongodb-test-server1.crt mongodb-test-server1.key > test-server1.pem
   ```

   You can use the test PEM file when configuring a
   `mongod` or a `mongos` for TLS/SSL
   testing.  For example:

   **Example:**

   ```javascript
   mongod --tlsMode requireTLS --tlsCertificateKeyFile test-server1.pem  --tlsCAFile test-ca.pem
   ```

   On macOS,
      If you are testing with Keychain Access to manage
      certificates, create a pkcs-12 file to add to Keychain Access
      instead of a PEM file:

      ```bash
      openssl pkcs12 -export -out test-server1.pfx -inkey mongodb-test-server1.key -in mongodb-test-server1.crt -certfile mongodb-test-ia.crt
      ```

      Once added to Keychain Access, instead of specifying the certificate key
      file, you can use the `--tlsCertificateSelector` to specify the certificate to use. If
      the CA file is also in Keychain Access, you can omit
      `--tlsCAFile` as well.

      ```javascript
      mongod --tlsMode requireTLS --tlsCertificateSelector subject="<TestServerCertificateCommonName>"
      ```

**See also:**

- appendix-ca-certificate
- appendix-client-certificate
- x509-member-certificate
