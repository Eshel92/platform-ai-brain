<!-- Converted from tutorial/configure-mongodb-agent-for-tls.txt (reStructuredText). Includes are inlined. -->

# Configure MongoDB Agent to Use TLS

Ops Manager uses TLS (Transport Layer Security) to encrypts connections between MongoDB Agent and:

- MongoDB instances.

- Ops Manager.

## Prerequisite

To configure the MongoDB Agent to use TLS (Transport Layer Security), you must:

- Have the trusted Certificate Authority certificate that signed the MongoDB 
  instance's certificate.
- Ensure that all TLS (Transport Layer Security) certificates contain the Subject Alternative 
  Name field.

## Procedures

### Configure Connections between MongoDB Agent and MongoDB Instances

To use TLS (Transport Layer Security) for the MongoDB Agent's connection to a MongoDB deployment,
specify the deployment's TLS (Transport Layer Security) settings when adding the
deployment or editing
the deployment's settings.

**Note:**

Ops Manager can manage TLS (Transport Layer Security) for you if you are using Automation for
the deployment. With Automation, Ops Manager prompts you for the
certificates to use to connect to the deployment when you enable
TLS (Transport Layer Security) and then configures the agents appropriately. To learn
how to configure TLS (Transport Layer Security), see
/tutorial/enable-ssl-for-a-deployment.

### Configure Connections between MongoDB Agent and Ops Manager

To ensure that the MongoDB Agent uses TLS (Transport Layer Security) when connecting to
Ops Manager, configure Ops Manager to use TLS (Transport Layer Security) for all connections.
The /tutorial/configure-ssl-connection-to-web-interface
tutorial describes how to set up Ops Manager to run over TLS (Transport Layer Security).

By default, the MongoDB Agent validates the Ops Manager TLS (Transport Layer Security)
certificate.

If a trusted third party did not sign your certificate,
you must configure the MongoDB Agent to trust Ops Manager.

To specify a self-signed certificate for Ops Manager that the
MongoDB Agent should trust:

**Step 1: Install your certificate file to your Ops Manager configuration directory.**

Copy your TLS (Transport Layer Security) certificate to your Ops Manager configuration directory:

**windows:**

The location of the MongoDB Agent configuration directory is
`C:\MMSData\Automation\`.

**Note:**

The MongoDB Agent configuration directory is named
`Automation` to simplify upgrades
for those using legacy agents.

**linux:**

The location of the MongoDB Agent configuration file is
`/path/to/install/`.

**rhel:**

The location of the MongoDB Agent configuration file is
`/etc/mongodb-mms/`.

**debian:**

The location of the MongoDB Agent configuration file is
`/etc/mongodb-mms/`.

**windows:**

**linux:**

Then, set the system user (username of the MongoDB Agent) as the 
owner of the TLS (Transport Layer Security) certificate. Grant that user read and write 
permissions on the certificate.

**Example:**

For Linux operating systems, use the following commands to set
ownership and permissions:

```sh
sudo cp -a mms-ssl-unified.pem /etc/mongodb-mms/
sudo chown mongod:mongod /etc/mongodb-mms/mms-ssl-unified.pem
sudo chmod 600 /etc/mongodb-mms/mms-ssl-unified.pem
```

**rhel:**

Then, set the `mongod` system user as the owner of 
the TLS (Transport Layer Security) certificate. Grant that user read and write 
permissions on the certificate.

**Example:**

For Linux operating systems, use the following commands to set
ownership and permissions:

```sh
sudo cp -a mms-ssl-unified.pem /etc/mongodb-mms/
sudo chown mongod:mongod /etc/mongodb-mms/mms-ssl-unified.pem
sudo chmod 600 /etc/mongodb-mms/mms-ssl-unified.pem
```

**debian:**

Then, set the `mongodb` system user as the owner of 
the TLS (Transport Layer Security) certificate. Grant that user read and write 
permissions on the certificate.

**Example:**

For Linux operating systems, use the following commands to set
ownership and permissions:

```sh
sudo cp -a mms-ssl-unified.pem /etc/mongodb-mms/
sudo chown mongod:mongod /etc/mongodb-mms/mms-ssl-unified.pem
sudo chmod 600 /etc/mongodb-mms/mms-ssl-unified.pem
```

**Step 2: Edit the following parameter in the configuration file.**

**windows:**

The location of the MongoDB Agent configuration file is
`C:\MMSData\Automation\automation-agent.config`.

**Note:**

The MongoDB Agent configuration file is named
`automation-agent.config` as a way to enable easier upgrades
for those using legacy agents.

**linux:**

The location of the MongoDB Agent configuration file is
`/path/to/install/local.config`.

**rhel:**

The location of the MongoDB Agent configuration file is
`/etc/mongodb-mms/automation-agent.config`.

**Note:**

The MongoDB Agent configuration file is named
`automation-agent.config` as a way to enable easier upgrades
for those using legacy agents.

**debian:**

The location of the MongoDB Agent configuration file is
`/etc/mongodb-mms/automation-agent.config`.

**Note:**

The MongoDB Agent configuration file is named
`automation-agent.config` as a way to enable easier upgrades
for those using legacy agents.

**Example:**

The following setting specifies the
`httpsCAFile` file as
`/etc/mongodb-mms/mms-ssl-unified.pem`.

**Step 3: Restart the MongoDB Agent for the configuration update to take effect.**

**Example:**

```sh
sudo /etc/init.d/mongodb-mms-automation-agent restart
```

If you don't want to have Ops Manager validate the SSL (Secure Sockets Layer) certificates, set
`Client Certificate Mode` to None.
