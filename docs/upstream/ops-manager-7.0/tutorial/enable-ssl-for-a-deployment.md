<!-- Converted from tutorial/enable-ssl-for-a-deployment.txt (reStructuredText). Includes are inlined. -->

# Enable TLS for a Deployment

For Ops Manager to monitor, deploy, or back up a MongoDB deployment that uses
TLS (Transport Layer Security), you must enable TLS (Transport Layer Security) for the Ops Manager project.

## Considerations

### Topics Not in Scope

A full description of
Transport Layer Security,
public key infrastructure,
X.509 certificates, and
Certificate Authorities
exceeds the scope of this tutorial. This tutorial assumes prior
knowledge of TLS (Transport Layer Security) and access to valid X.509 certificates.

**Note:**

If you want to 
reset Authentication and TLS settings
for your project, first 
unmanage any MongoDB deployments 
that Ops Manager manages in your project.

## Prerequisite

### Get and Install the TLS Certificate on Each MongoDB Host

Acquire a TLS (Transport Layer Security) certificate for each host serving a MongoDB process.
This certificate must include the FQDN (fully qualified domain name) for the hostname of this
MongoDB host. The FQDN (fully qualified domain name) must be the Subject Alternative Name of this 
host. You must install this TLS (Transport Layer Security) certificate on the MongoDB host.

**Warning:**

The MongoDB Agent from version 11.12.0.7384 requires that TLS (Transport Layer Security)
certificates include a value in the Subject Alternative Name
field. Before upgrading to 11.12.0.7384, ensure that all TLS (Transport Layer Security)
certificates used in your MongoDB deployment contain a SAN (Subject Alternative Name).
To learn more, see tls-cert-no-san.

## Procedures

**Important:**

You must complete:

1. Set Existing Deployments to Use TLS,
   then
2. Enable TLS for the Project

before you click Review & Deploy.

### Set Existing Deployments to Use TLS (Transport Layer Security)

**Important:**

With the Client Certificate Mode setting, you can set
if the client must present a TLS (Transport Layer Security) certificate to connect to the
deployments in your project. If you enable TLS (Transport Layer Security) for your
project, all deployment must use TLS (Transport Layer Security).

If you wish to enable TLS (Transport Layer Security) for existing MongoDB deployments in your
Ops Manager project:

**Step 1: Navigate to the Clusters view for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Clusters view.

**Step 2: On the line listing the process, click Modify.**

**Step 3: Expand the Advanced Configuration Options section.**

**Step 4: Set the TLS (Transport Layer Security)/SSL (Secure Sockets Layer) startup options.**

a. Click Add Option to add each of the following options:

   * - Option
     - Required
     - Value

   * - `tlsMode`
     - Required
     - Select `requireTLS`.

   * - `tlsCertificateKeyFile`
     - Required
     - Provide the absolute path to the server certificate.

   * - `tlsCertificateKeyFilePassword`
     - Required
     - Provide the PEM key file password if you encrypted it.

       **Important:**

       If the encrypted private key for the `.pem` certificate file 
       is in PKCS #8 format, 
       it must use PBES2 encryption operations. 
       The MongoDB Agent does not support PKCS #8 with other encryption 
       operations.

   * - `tlsFIPSMode`
     - Optional
     - Select `true` if you want to
       enable FIPS mode.

b. After adding each option, click Add.

c. When you have added the required options, click Save.

### Enable TLS (Transport Layer Security) for the Project

**Step 1: Navigate to the Security Settings dialog for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Security tab.
#. Click the Settings tab.
#. Perform one of the following actions:

   - If this is your first time configuring TLS (Transport Layer Security),
     authentication, or authorization settings for this project, click
     Get Started.
   - If you have already configured TLS (Transport Layer Security) authentication, or
     authorization settings for this project, click Edit.

**Step 2: Choose your Authentication Mechanisms.**

a. On the Select Authentication Mechanisms screen,
   enable one or more Authentication Mechanisms.

   TLS (Transport Layer Security) works with all authentication mechanisms.

b. Click Next.

**Step 3: Specify the TLS (Transport Layer Security) Settings.**

* - Field
  - Action

* - MongoDB Deployment Transport Layer Security (TLS)
  - Toggle this slider to ON.

* - TLS CA File Path
  - The TLS (Transport Layer Security) Certificate Authority file is a `.pem`-format certificate
    file that contains the root certificate chain from the
    Certificate Authority. The MongoDB Agent uses this same Certificate Authority file
    to connect to every item in your deployment.

    The encrypted private key for the `.pem` certificate file must be in
    PKCS #1 format. The MongoDB Agent doesn't support
    the PKCS #8 format.

    Type the file path to the TLS (Transport Layer Security) Certificate Authority file on every host
    running a MongoDB process:

    - Type the file path on all Linux hosts in the first box.

    - Type the file path on all Windows hosts in the second box.

    This enables the `net.tls.CAFile` setting for the
    MongoDB processes in the project.

    Click Validate to test that each host in your
    deployment has a TLS (Transport Layer Security) Certificate Authority at the paths you specified.

* - Client Certificate Mode
  - Select if client applications or MongoDB Agent\s must present a
    TLS (Transport Layer Security) certificate when connecting to a TLS (Transport Layer Security)\-enabled MongoDB
    deployments. Each MongoDB deployment checks for certificates
    from these client hosts when they try to connect. If you
    choose to require the client TLS (Transport Layer Security) certificates, make sure
    they are valid.

    Accepted values are:

    |  |  |
    |---|---|
    | Optional | Every client may present a valid TLS (Transport Layer Security) certificate when connecting to MongoDB deployments. MongoDB Agent\s might use TLS (Transport Layer Security) certificates if you *don't* set the `mongod` `tlsMode` to `None`. |
    | Required | Every MongoDB deployment in this project starts with TLS (Transport Layer Security)\-encrypted network connections. All Agents must use TLS (Transport Layer Security) to connect to any MongoDB deployment. |

**Step 4: Configure the MongoDB Agents.**

a. In the Agent Auth Mechanism list, click the same
   authentication mechanisms that you did for the project.

b. Follow the procedure to configure the MongoDB Agent to use that
   authentication method:

   - SCRAM-SHA
   - X.509 Certificates
   - LDAP
   - Kerberos

**Note:**

If you had TLS (Transport Layer Security) certificates for Legacy Agents, see
**What if I had TLS certificates for Legacy Backup or Monitoring
Agents?** at the end of this procedure for guidance.

**Step 5: Click Save to set your changes.**

**Step 6: Click Review & Deploy to review your changes.**

Ops Manager displays your proposed changes.

a. If you are satisfied, click Confirm & Deploy.
b. If you want to make further configuration changes, 
   click Cancel. Click Modify for the
   cluster to make additional changes.

- If you updated to the MongoDB Agent from deployments that used
  Automation, the MongoDB Agent manages the TLS (Transport Layer Security) settings.

- If you updated to the MongoDB Agent from deployments that did not
  use Automation but you had Backup Agents, Monitoring Agents, or
  both, you *can* set your *Backup Agent and Monitoring
  Agent-specific* settings during the Agent update or through the
  following procedure:

  1. Navigate to Deployment arrow-right
     Agents arrow-right
     Downloads & Settings arrow-right
     Custom Configurations arrow-right
     Edit Custom Configuration.

  2. Click pencil-alt.

  3. Under the Backup Configurations section:

     a. Type the desired
        setting
        in the Setting box and its corresponding value
        in the Value box.

     #. To add more than one Setting, click the
        + Add Setting link. Another row appears.

     #. Repeat until all settings have been added.

  4. Under the Monitoring Configurations section:

     a. Type the desired
        setting
        in the Setting box and the corresponding value
        in the Value box.

     #. To add more than one Setting, click the
        + Add Setting link. Another row appears.

     #. Repeat until all settings have been added.

  You can click the trash-alt to remove any settings
  that you have added.
