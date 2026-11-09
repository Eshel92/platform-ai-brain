<!-- Converted from tutorial/configure-ssl-connection-to-web-interface.txt (reStructuredText). Includes are inlined. -->

# Configure TLS Connections to Ops Manager

You can configure Ops Manager to encrypt connections from all MongoDB
Agents to Ops Manager, from website clients to the Ops Manager Application, and from
API (Application Programming Interface) clients to the REST (Representational State Transfer) API (Application Programming Interface).

To encrypt connections, you can:

- Set up an HTTPS (Hypertext Transfer Protocol Secure) proxy in front of Ops Manager, or

- Run the Ops Manager Application over HTTPS (Hypertext Transfer Protocol Secure), as described on this page.

The following procedure configures Ops Manager with a `.pem` file that
contains the Ops Manager host's TLS (Transport Layer Security) certificate.

The MongoDB Agent uses HTTPS (Hypertext Transfer Protocol Secure) after successfully completing the
procedure.

**See also:**

To learn more about `.pem` files, read the
.pem file section in the
MongoDB manual.

## Prequisites

- Update to or
  install the MongoDB Agent.
- Add any TLS (Transport Layer Security)\-related
  custom settings to your
  MongoDB Agent configuration.

## Configure Ops Manager Application for TLS (Transport Layer Security)

**Step 1: Upload the certificate file to each Ops Manager host.**

a. Upload your `.pem` file to each Ops Manager Application host. This
   certificate must be uploaded to each Ops Manager host so they can
   accept TLS (Transport Layer Security) connections.

b. Change the owner of the `.pem` file to the user and group that
   own the Ops Manager process.

c. Change the permissions of the `.pem` file so only the file
   owner can read and write the file.

**Step 2: Enable TLS (Transport Layer Security) for the Ops Manager Application.**

a. Click Admin in the Ops Manager application to view the
   Admin interface.

#. Click the General tab

#. Click Ops Manager Config.

#. Click Web Server & Email.

#. Set the following options under Web Server heading:

   * - Option
     - Action

   * - `URL to Access Ops Manager`
     - Provide the full URL (Uniform Resource Locator) for Ops Manager Application including port
       `8443` for HTTPS (Hypertext Transfer Protocol Secure) access.

       For example:

       ```ini
       https://opsmanager.example.com:8443
       ```

   * - `HTTPS PEM Key File`
     - Type the absolute file system path where the `.pem`
       file is located on all Ops Manager hosts in this box.

   * - `HTTPS PEM Key File Password`
     - If you encrypted the HTTPS (Hypertext Transfer Protocol Secure) PEM (Privacy-Enhanced Mail) Key File, type the
       password needed to decrypt it in this box.

   * - `Client Certificate Mode`
     - Select if client applications or MongoDB Agents must
       present a TLS (Transport Layer Security) certificate when connecting to a
       TLS (Transport Layer Security)\-enabled Ops Manager. Ops Manager checks for certificates
       from these client hosts when they try to connect. If you
       choose to require the client TLS (Transport Layer Security) certificates, make sure
       they are valid.

       Accepted values are:

       - None
       - Required for Agents Only
       - Required for All Requests

#. Click Save.

**Step 3: *(Optional)* Change the minimum TLS (Transport Layer Security) version.**

In opsmgr-server-4.4.13 and later, the Ops Manager Application
requires its clients to use TLS (Transport Layer Security) version 1.2 by default.

To change the minimum TLS (Transport Layer Security) version:

a. Click Admin in the Ops Manager application to view the
   `Admin` interface.

#. Click the General tab

#. Click Ops Manager Config.

#. Click Custom.

#. Configure the minimum TLS (Transport Layer Security) version.

#. Enter `mms.minimumTLSVersion` in the Key box.

#. Enter a minimum TLS (Transport Layer Security) version in the Value box.

   The following values are accepted:

   - `TLSv1`
   - `TLSv1.1`
   - `TLSv1.2`

#. Click Save.

**Step 4: *(Optional)* Specify which TLS (Transport Layer Security) cipher suites you want to exclude.**

To exclude specific TLS (Transport Layer Security) cipher suites from TLS (Transport Layer Security) connections
with the Ops Manager Application.

a. Click Admin in the Ops Manager application to view the
   `Admin` interface.

#. Click the General tab

#. Click Ops Manager Config.

#. Click Custom.

#. Enter `mms.disableCiphers` in the Key box.

#. Enter a comma-separated list of cipher suites to disable in the
   Value box.

   **Important:**

   Cipher suite names used in Ops Manager must follow RFC 5246 naming conventions. Do not use the OpenSSL
   naming convention.

   For example, use `TLS_RSA_WITH_NULL_SHA256`, not `NULL-SHA256`.

#. Click Save.

**Step 5: Restart each Ops Manager host to enable TLS (Transport Layer Security).**

Restart the Ops Manager Application per the instructions to
Start and Stop Ops Manager Application.

## Configure MongoDB Agents to use TLS (Transport Layer Security)

On each MongoDB host in your cluster:

**Step 1: Open MongoDB Agent configuration file in your preferred text editor.**

The location of the MongoDB Agent configuration file depends on
your platform:

tabs:

  - id: macos
    content: |

      ```sh
      /path/to/install/local.config
      ```

  - id: linux
    content: |

      ```sh
      /path/to/install/local.config
      ```

  - id: rhel
    content: |

      ```sh
      /etc/mongodb-mms/automation-agent.config
      ```

  - id: debian
    content: |

      ```sh
      /etc/mongodb-mms/automation-agent.config
      ```

**Step 2: Change `mmsBaseUrl` and TLS (Transport Layer Security) settings.**

Set or add the following properties where needed:

* - Option
  - Necessity
  - Action

* - mmsbaseurl
  - Required
  - Set this value to match the URL (Uniform Resource Locator) you entered in the
    URL to Access Ops Manager box.

    IMPORTANT: Ensure that you update both this property and the 
    URL to Access Ops Manager box. Both values must 
    match. If Monitoring and Backup are enabled for the 
    MongoDB Agent, they use the URL to Access Ops 
    Manager configured on the Ops Manager server, unless the 
    `mmsBaseURL` custom monitoring setting is set for the 
    MongoDB Agent. For more information, see the 
    MongoDB Agent Monitoring Settings.

* - `tlsRequireValidMMSServerCertificates`
  - Conditional
  - Set this value to `true` if all of the following apply:

    - You want the agent to validate TLS (Transport Layer Security) certificates of
      Ops Manager.
    - You signed the TLS (Transport Layer Security) certificates of your Ops Manager
      hosts with a known external Certificate Authority or self-signed
      Certificate Authority.

    If you set this value to `true`, you must set
    `httpsCAFile`.

* - `httpsCAFile`
  - Conditional
  - If you are using your own self-signed Certificate Authority `.pem`
    files, add this property and set it to the absolute path to
    your Certificate Authority file on the MongoDB host.

    IMPORTANT: This Certificate Authority file must be in the same 
    location on each MongoDB host in the same sharded cluster 
    or replica set. Any MongoDB host that does not have the file 
    in the same file location as the others may become unaccessible.

    Add the Certificate Authority for the `downloads.mongodb.com`
    certificate to this `.pem` file if you:

    1. Need your MongoDB Agents to download their MongoDB
          installers from the Internet,

    #. Use TLS to encrypt connections, and

    #. Signed your certificates with a private CA. (You set the
       `httpsCAFile` option.)

    To learn how to download TLS certificates from another web
    site, see the [OpenSSL Cookbook entry](https://www.feistyduck.com/library/openssl-cookbook/online/ch-testing-with-openssl.html#extracting-remote-certificates).

* - `tlsMMSServerClientCertificate`
  - Conditional
  - If you set Client Certificate Mode in Ops Manager to
    `Required for Agents Only` or ``Required for All
    Requests``, add this value and specify the absolute path to
    the file containing the client's private key, certificate, and
    optional intermediate certificates in `.pem` format .

* - `tlsMMSServerClientCertificatePassword`
  - Conditional
  - If you encrypted the
    `tlsMMSServerClientCertificate` `.pem` file,
    provide the password needed to decrypt it.

**Step 3: Click Save.**

**Step 4: Restart the MongoDB Agent.**
