<!-- Converted from appendix/security/appendixA-openssl-ca.txt (reStructuredText). Includes are inlined. -->

# Appendix A - OpenSSL CA Certificate for Testing Self-Managed Deployments

**Warning:** Disclaimer

This page is provided for testing purposes only and the
certificates are for testing purposes only.

The following tutorial provides some guidelines for creating 
test X.509 certificates:

- Do not use these certificates for production. Instead, follow your
  security policies.

- For information on OpenSSL, refer to the official OpenSSL docs.
  Although this tutorial uses OpenSSL, the material should not be
  taken as an authoritative reference on OpenSSL.

## Procedures

The following procedures outlines the steps to create a test CA PEM
file. The procedure creates both the CA PEM file and an intermediate
authority certificate and key files to sign server/client test
certificates.

### A. Create the OpenSSL Configuration File

#. Create a configuration file `openssl-test-ca.cnf` with the
   following content:

   ```cfg
   # NOT FOR PRODUCTION USE. OpenSSL configuration file for testing. 

   # For the CA policy
   [ policy_match ]
   countryName = match
   stateOrProvinceName = match
   organizationName = match
   organizationalUnitName = optional
   commonName = supplied
   emailAddress = optional

   [ req ]
   default_bits = 4096
   default_keyfile = myTestCertificateKey.pem    ## The default private key file name. 
   default_md = sha256                           ## Use SHA-256 for Signatures
   distinguished_name = req_dn
   req_extensions = v3_req
   x509_extensions = v3_ca # The extentions to add to the self signed cert

   [ v3_req ]
   subjectKeyIdentifier  = hash
   basicConstraints = CA:FALSE
   keyUsage = critical, digitalSignature, keyEncipherment
   nsComment = "OpenSSL Generated Certificate for TESTING only.  NOT FOR PRODUCTION USE."
   extendedKeyUsage  = serverAuth, clientAuth

   [ req_dn ]
   countryName = Country Name (2 letter code)
   countryName_default = 
   countryName_min = 2
   countryName_max = 2

   stateOrProvinceName = State or Province Name (full name)
   stateOrProvinceName_default = TestCertificateStateName 
   stateOrProvinceName_max = 64

   localityName = Locality Name (eg, city)
   localityName_default = TestCertificateLocalityName
   localityName_max = 64

   organizationName = Organization Name (eg, company)
   organizationName_default = TestCertificateOrgName
   organizationName_max = 64

   organizationalUnitName = Organizational Unit Name (eg, section)
   organizationalUnitName_default = TestCertificateOrgUnitName 
   organizationalUnitName_max = 64

   commonName = Common Name (eg, YOUR name)
   commonName_max = 64

   [ v3_ca ]
   # Extensions for a typical CA

   subjectKeyIdentifier=hash
   basicConstraints = critical,CA:true
   authorityKeyIdentifier=keyid:always,issuer:always
   ```

#. *Optional*. You can update the default Distinguished Name (DN)
   values.

### B. Generate the Test CA PEM File

#. Create the test CA key file `mongodb-test-ca.key`. 

   ```bash
   openssl genrsa -out mongodb-test-ca.key 4096
   ```

   **Tip:**

   This private key is used to generate valid certificates for the
   CA. Although this private key, like all files in this appendix,
   is intended for testing purposes only, you should engage in good
   security practices and secure this key file.

#. Create the CA certificate `mongod-test-ca.crt` using the
   generated key file. When asked for Distinguished Name values, enter
   the appropriate values for your test CA certificate.

   ```bash
   openssl req -new -x509 -days 1826 -key mongodb-test-ca.key -out mongodb-test-ca.crt -config openssl-test-ca.cnf
   ```

#. Create the private key for the intermediate certificate.

   ```bash
   openssl genrsa -out mongodb-test-ia.key 4096
   ```

   **Tip:**

   This private key is used to generate valid certificates for the
   intermediate authority. Although this private key, like all files
   in this appendix, is intended for testing purposes only, you
   should engage in good security practices and secure this key file.

#. Create the certificate signing request for the intermediate
   certificate. When asked for Distinguished Name values, enter the
   appropriate values for your test Intermediate Authority certificate.

   ```bash
   openssl req -new -key mongodb-test-ia.key -out mongodb-test-ia.csr -config openssl-test-ca.cnf
   ```

#. Create the intermediate certificate `mongodb-test-ia.crt`.

   ```bash
   openssl x509 -sha256 -req -days 730 -in mongodb-test-ia.csr -CA mongodb-test-ca.crt -CAkey mongodb-test-ca.key -set_serial 01 -out mongodb-test-ia.crt -extfile openssl-test-ca.cnf -extensions v3_ca
   ```

#. Create the test CA PEM file from the test CA certificate  `mongod-test-ca.crt` and
   test intermediate certificate `mongodb-test-ia.crt`.

   ```bash
   cat mongodb-test-ia.crt mongodb-test-ca.crt > test-ca.pem
   ```

You can use the test PEM file when configuring `mongod`,
`mongos`, or `mongosh` for TLS/SSL testing.

You can use the test intermediate authority to sign the test
certificates for both the server(s) and client(s). A single authority
must issue the certificates for both the client and the server.

      

**See also:**

- appendix-server-certificate
- appendix-client-certificate
