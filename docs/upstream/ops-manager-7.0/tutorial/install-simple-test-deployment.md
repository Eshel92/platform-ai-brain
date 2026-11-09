<!-- Converted from tutorial/install-simple-test-deployment.txt (reStructuredText). Includes are inlined. -->

# Install a Simple Test Ops Manager Installation

**Warning:**

This setup is not suitable for a production deployment.

To evaluate Ops Manager, you can install the
mms-application-package and
mms-application-database on a single host. This setup provides
all the functionality of Ops Manager monitoring and automation but
provides **no** failover or high availability.

## Considerations

This test installation includes the following caveats:

- It uses one `mongod` for the Ops Manager Application database. In production,
  the database requires a dedicated replica set.

- It uses MongoDB Community Edition. MongoDB Community doesn't need
  additional libraries.

- It doesn't include backup functionality.

## Procedure

To install and configure an evaluation version of Ops Manager on hosts
running Red Hat Enterprise Linux 8.0:

**Step 1: Provision an Ops Manager host.**

Provision a host for Ops Manager. This host must meet the following
requirements:

|  |  |
|---|---|
| System Memory | 15 GB |
| Disk Capacity | 50 GB in `/` (The root directory of this host) |
| Host OS Permissions | `root` |
| Host OS | Red Hat Enterprise Linux 8.0 |

Cloud-based instances must meet the memory and storage requirements.

To verify the needed capacity, log in to the instance and execute the
following commands:

```sh
vmstat -S M -s | grep "total memory"
```

The output for the command shows that this instance has 16 GB of RAM.

```sh
16384 M total memory
```

```sh
df -h | grep "/$"
```

The output for the command shows that this instance has 73 GB of 
storage capacity.

```sh
/dev/sda1        73G   58G   12G  84% /
```

**Important:**

Verify that the `ulimit` settings meet the
minimum requirements.

**Step 2: Configure `yum` to install MongoDB.**

Create a `/etc/yum.repos.d/mongodb-org-7.0.repo` file so
that you can install MongoDB directly using `yum`:

```cfg
[mongodb-org-7.0]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/7.0/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://pgp.mongodb.com/server-7.0.asc
```

**Step 3: Install MongoDB.**

Invoke the following command to install the latest stable release of
MongoDB Community:

```sh
sudo yum install -y mongodb-org
```

**Step 4: Disable the `mongod` service.**

Ops Manager connects to its application database on port 27017. If
the host on which you want to install the application database has a
running `mongod`, disable that existing database.

To disable the `mongod` service, invoke the following command:

```sh
sudo systemctl disable mongod
```

**Step 5: Create the Ops Manager Application Database directory.**

a. Invoke the following command to create the data directory:

   ```sh
   sudo mkdir -p /data/appdb
   ```

b. Invoke the following command to change ownership of the data
   directory to MongoDB:

   ```sh
   sudo chown -R mongod:mongod /data
   ```

**Step 6: Update the MongoDB configuration file.**

The installer creates a configuration file saved at
`/etc/mongod.conf`.

a. Open the MongoDB file with your preferred text editor.

b. Edit the file to make the following changes:

   ```yaml
   systemLog:
     destination: file
     path: "/data/appdb/mongodb.log"
     logAppend: true
   storage:
     dbPath: "/data/appdb"
     wiredTiger:
       engineConfig:
         cacheSizeGB: 1
   processManagement:
     fork: true
     timeZoneInfo: /usr/share/zoneinfo
     pidFilePath: /var/run/mongodb/mongod.pid
   net:
     bindIp: 127.0.0.1
     port: 27017
   setParameter:
     enableLocalhostAuthBypass: false
   ```

c. Save the file when you have made the edits.

**Step 7: Start the Ops Manager Application Database mongod instance.**

```sh
sudo -u mongod mongod -f /etc/mongod.conf
```

**Step 8: Download the Ops Manager package.**

a. Navigate to the Ops Manager Download Center.

#. From the Platforms drop-down menu, click
   Red Hat + CentOS 6, 7, 8 / SUSE 12 + 15 / Amazon Linux.

#. From the Packages drop-down menu, click
   RPM.

#. Click Download.

**Note:**

MongoDB names the downloaded package
`mongodb-mms-<version>.x86_64.rpm`. `<version>` represents the
version number for Ops Manager.

**Step 9: Verify Ops Manager package integrity.**

To verify the integrity of the Ops Manager download, see
om-verify-packages.

**Step 10: Copy the Ops Manager `.rpm` package to your host.**

If you install Ops Manager on a remote host, such as a cloud service
provider instance, use `scp` to copy the installer to your host:

```sh
scp -i <keyfile> mongodb-mms-<version>.x86_64.rpm \
       <username>@<public-ip>:~
```

**Step 11: Install Ops Manager.**

To install the `.rpm` package, invoke the following command.
`<version>` represents the Ops Manager version in the `.rpm` package:

```sh
sudo rpm -ivh mongodb-mms-<version>.x86_64.rpm
```

This command creates the following artifacts:

| Artifact | Value |
|---|---|
| Ops Manager software base directory | `/opt/mongodb/mms/` |
| New system user that owns the Ops Manager processes | `mongodb-mms`. |
| Ops Manager configuration file with the `connection string to access the Application Database`. Don't change this value defaults from `locahost:27017`. | `/opt/mongodb/mms/conf/conf-mms.properties` |

**Step 12: Start Ops Manager.**

Invoke the following command:

```sh
sudo service mongodb-mms start
```

**Step 13: Get your instance hostname.**

If you use an cloud service provider instance, find the hostname
following the directions of the relevant provider:

- `AWS`
- [Azure](https://docs.microsoft.com/en-us/azure/virtual-network/virtual-networks-viewing-and-modifying-hostnames)
- [GCP](https://cloud.google.com/compute/docs/instances/custom-hostname-vm)

If you don't have a hostname, use the public IP address. To find your
host's public IP address, paste this URL (Uniform Resource Locator) into your preferred
browser:

```sh
https://www.google.com/search?q=myip
```

**Step 14: Open the Ops Manager home page and register the first user.**

a. In a browser, enter the following URL (Uniform Resource Locator) using the hostname.
   If do not have a hostname, use the public IP address instead:

   ```sh
   http://<OpsManagerHost>:<Port>
   ```

#. Click the Sign Up link.
#. Follow the console prompts to register the first user and create
   the first organization and project. Ops Manager assigns the
   Global Owner role to the first user.

**Step 15: Configure Ops Manager.**

Ops Manager opens the
configuration console.
Ops Manager marks required settings with an asterisk.

Enter the information as appropriate. When you finish the
configuration, Ops Manager opens the Deployment page.

**Step 16: Set up your first deployment.**

a. Click MongoDB Ops Manager in the upper left corner of
   the page to return to the Deployment page.

#. Click Add to deploy a MongoDB instance.

   **See also:**

   - replica set
   - sharded cluster
