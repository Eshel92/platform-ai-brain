<!-- Converted from tutorial/install-on-prem-with-rpm-packages.txt (reStructuredText). Includes are inlined. -->

# Install Ops Manager with an `rpm` Package

This tutorial describes how to install Ops Manager using an `rpm`
package. If you are instead upgrading an existing deployment, please
see /tutorial/upgrade-ops-manager.

## Prerequisites

You must have administrative access on the hosts to which you install.

Before you install Ops Manager, you must:

1. Plan your configuration. See /core/installation-checklist.

2. Deploy hosts that meet the /core/requirements.

   **Warning:** Potential for Production Failure

   Your Ops Manager instance can fail in production if you fail to configure the following:

   - Ops Manager hosts per the /core/requirements.

   - MongoDB hosts per the
     Production Notes in
     the MongoDB manual. MongoDB instances in Ops Manager include:

     - The Ops Manager Application Database,
     - Each blockstore.
     - Each Ops Manager Backup Daemon `head database`. This only
       applies to FCV 4.0 and earlier. FCV 4.2 and later do not use
       `head databases` for backups.

3. Install the Ops Manager Application Database and optional
   Backup Database. The
   databases require *dedicated* MongoDB instances. *Don't* use
   MongoDB installations that store other data. Ops Manager requires the
   Backup Database if you use the Backup feature.

   The Ops Manager Application must authenticate to the backing databases as a
   MongoDB user with appropriate access.

   **See also:**

   To learn more about connecting to your backing database with
   authentication, see `mongo.mongoUri`.

   **Note:**

   You must deploy application databases manually. However, you can deploy backup databases
   with Ops Manager. For more information, see Deploy Backing
   Databases.

4. Install and verify an Email Server. Ops Manager needs an email server
   to send alerts and recover
   user accounts. You may use an SMTP Server or
   an AWS (Amazon Web Services) SES (Simple Email Service) server. To configure your Email Server, see
   `Email Delivery Method Configuration`.

## Install Ops Manager

**Warning:**

`rpm` packages for Ops Manager versions 6.0.0, 6.0.1, 6.0.2, and 8.0.0 
contained incorrect version information that could cause standard 
upgrades to fail. If upgrading from any of these versions to 
version 6.0.3 or greater, upgrade the package using the 
`--oldpackage` flag:

```sh
sudo rpm -Uvh --oldpackage mongodb-mms-<version>.x86_64.rpm
```

To install Ops Manager:

**Step 1: Download the latest version of the Ops Manager package.**

a. Open your preferred browser to visit the
   MongoDB Download Center on
   MongoDB.com.

   If you start from MongoDB.com, click Products
   arrow-right Ops Manager
   arrow-right Try it now.

#. From the Platforms dropdown menu, click one of the
   following options:

   - Red Hat + CentOS 7, 8, 9 / SUSE 12 + 15 / Amazon Linux 2, Amazon Linux 2023

#. From the Packages dropdown menu, click
   RPM.

#. Click Download.

   The downloaded package is named
   `mongodb-mms-<version>.x86_64.rpm`, where `<version>` is the
   version number.

**Step 2: Verify Ops Manager package integrity.**

To verify the integrity of the Ops Manager download, see
om-verify-packages.

**Step 3: Install the Ops Manager package on each server being used for Ops Manager.**

**Note:** **RHEL 9+**

On RHEL 9+ platforms, you must install the `initscripts` package before installing Ops Manager.

Install the `.rpm` package by issuing the following command, where
`<version>` is the version of the `.rpm` package:

```sh
sudo rpm -ivh mongodb-mms-<version>.x86_64.rpm
```

When installed, the base directory for the Ops Manager software is
`/opt/mongodb/mms/`. The `.rpm` package creates a new system user
`mongodb-mms` under which the server runs.

**Step 4: Configure the Ops Manager connection to the Ops Manager Application Database.**

On a server that is to run the Ops Manager, open
`/opt/mongodb/mms/conf/conf-mms.properties` with root privileges and
configure the settings described here, as appropriate.

Configure the following setting to provide the connection string
Ops Manager uses to connect to the database:

- `mongo.mongoUri`

To configure Ops Manager to use the Ops Manager Application Database
over TLS (Transport Layer Security), configure the following TLS settings.

- `mongo.ssl`
- `mongodb.ssl.CAFile`
- `mongodb.ssl.PEMKeyFile`
- `mongodb.ssl.PEMKeyFilePassword`

Ops Manager also uses these settings for TLS (Transport Layer Security) connections to Backup Databases

To configure Ops Manager to use Kerberos to manage access to the
Ops Manager Application Database, configure the following
Kerberos settings:

- `jvm.java.security.krb5.conf`
- `jvm.java.security.krb5.kdc`
- `jvm.java.security.krb5.realm`
- `mms.kerberos.principal`
- `mms.kerberos.keyTab`

**Step 5: On the same server, start Ops Manager.**

For [platforms that use](https://en.wikipedia.org/wiki/Systemd?oldid=804870621#Adoption_and_reception)
[systemd](https://freedesktop.org/wiki/Software/systemd) (
[RHEL 7+](https://access.redhat.com/documentation/en/red-hat-enterprise-linux/?version=7/),
[CentOS 7.14+](https://wiki.centos.org/Manuals(2f)ReleaseNotes.html),
[SUSE 12+](https://www.suse.com/documentation/sles-12/)
):

```sh
sudo service mongodb-mms start
```

For platforms that use `SysVInit` (
[RHEL 6](https://access.redhat.com/documentation/en/red-hat-enterprise-linux/?version=6),
[CentOS 6](https://wiki.centos.org/Manuals(2f)ReleaseNotes.html)
):

```sh
sudo /etc/init.d/mongodb-mms start
```

**Step 6: Open the Ops Manager home page and register the first user.**

a. Enter the following URL (Uniform Resource Locator) in a browser, where `<host>` is the
   fully qualified domain name of the server:

   ```sh
   http://<OpsManagerHost>:8080
   ```

b. Click the Sign Up link and follow the prompts to
   register the first user and create the first project. The first
   user is automatically assigned the Global Owner role.

**Step 7: Configure Ops Manager.**

Ops Manager walks you through several configuration pages. Required
settings are marked with an asterisk. Enter information as
appropriate. When configuration is complete, Ops Manager opens the
Deployment page.

In addition to the common required settings, the following are
required for particular deployment configurations. For more
information on a setting, see /reference/configuration.

| Configuration | Required Settings |
|---|---|
| If you are running multiple Ops Manager instances behind a load balancer | Set Load Balancer Remote IP Header to the name of the header the load balancer will use when forwarding the client's IP address to the application server. If you set this, do not allow clients to connect directly to any of the application servers. The load balancer must not return cached content. You will set up the additional servers as part of the next steps in this procedure. |
| If you are using Automation or Backup without an internet connection | Set the *MongoDB Version Management* settings. You will need to put the tarballs for every MongoDB release used in your deployment in the configured `Versions Directory` on every Ops Manager host. To learn more, see /tutorial/configure-local-mode. |

**Step 8: Copy the `gen.key` file from the current server to the other servers.**

Ops Manager requires an identical gen.key file be stored
on both servers running Ops Manager and uses the file to encrypt data at
rest in the Ops Manager Application Database and Backup Database.

You must copy the `gen.key` file from the current server, on which you
just installed Ops Manager, to every server that will run Ops Manager. You
must copy the `gen.key` to the other servers **before** starting
Ops Manager on them.

Use `scp` to copy the `gen.key` file from the
`/etc/mongodb-mms/` directory on the current server to the same
directory on the other servers.

**Important:**

Back up the `gen.key` file to a secure location.

**Step 9: If you will run multiple Ops Manager Applications behind a load balancer, configure and start the applications.**

For each Ops Manager instance, repeat the step to configure the connection to
the Ops Manager Application Database and the step to start the application.

For more information on running multiple applications behind a load
balancer, see /tutorial/configure-application-high-availability.

**Step 10: If you will run Ops Manager Backup, configure the Backup Daemon and Backup Storage.**

a. Deploy your backup databases. You can
   use Ops Manager to manage replica set deployment after you install MongoDB on each host.

#. On each Ops Manager server that you activate as a Backup Daemon, 
   create the directory that will be used as the 
   head directory. The directory must be:

   - dedicated for this purpose on a local disk partition.

   - sized appropriately according to the /core/requirements.

   - writable by the `mongodb-mms` user.

#. Configure the Backup Storage you
   want to use for your snapshots.

#. Open Ops Manager and verify that you are logged in as the user you
   registered when installing Ops Manager. This user is the
   global owner.

#. Click the Admin link at the top right of the page.

#. Click the Backup tab.

#. Follow the prompts to configure the Backup Daemon and Backup Storage.
   Ops Manager walks you through configuration of the daemon and snapshot
   storage.

   After you select how to store snapshots, you are prompted to
   configure the connection string to the Backup Database. If you use
   filesystem storage for your snapshots, the Backup Database is used
   only for the `oplog store`.

   WARNING: Once the connection string is saved, any change to the string
   requires you to restart all the Ops Manager instances, including
   those running activated Backup Daemons. Making the change and
   clicking Save is not sufficient. Ops Manager will
   continue to use the previous string until you restart the
   instances.

   |  |  |
   |---|---|
   | <hostname>: | Enter a comma-separated list of the fully qualified domain names and port numbers for all replica set members for the Backup Database. |
   | MongoDB Auth Username and MongoDB Auth Password | Enter the user credentials if the database uses authentication. WARNING: If you did not use the credentialstool to encrypt this password, it is stored as plaintext in the database. |
   | Encrypted Credentials | Check this if the user credentials use the Ops Manager credentialstool. |
   | Use SSL | Check this if the database uses SSL. If you select this, you must configure SSL settings Ops Manager. See /reference/configuration. |
   | Connection Options | To add additional connection options, enter them using the MongoDB Connection String URI Format. This field supports un-escaped values only. |

## Next Steps

After you install the Ops Manager Application to your Ops Manager hosts, you
must install MongoDB Agents
on the hosts that will run your MongoDB deployments.

You can Enable Application Database Monitoring.

You can install the MongoDB Agent on hosts running existing MongoDB
deployments or on hosts on which you will create new MongoDB
deployments. Hosts that serve your MongoDB deployments must meet the
minimum MongoDB production requirements.
