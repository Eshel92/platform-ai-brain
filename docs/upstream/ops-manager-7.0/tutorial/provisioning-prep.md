<!-- Converted from tutorial/provisioning-prep.txt (reStructuredText). Includes are inlined. -->

# Deployment Prerequisites

## System Requirements

### Hardware and Software

Each host must meet the following requirements.

- At least 10 GB of free disk space plus whatever space is necessary to
  hold your MongoDB data.

- At least 4 GB of RAM.

- If you use AWS (Amazon Web Services) EC2 instances, you should use a minimum of an
  `m3.medium` instance.

- The MongoDB Agent must be installed only on 64-bit architectures.

### Server Networking Access

The hosts that serve the MongoDB deployments must:

- Have full networking access to each other through their FQDN (fully qualified domain name)\s.
  Each host must be able to reach every other host through the FQDN (fully qualified domain name).
  To find the FQDN (fully qualified domain name) for each host, run the following command in the
  shell:

  ```sh
  hostname -f
  ```

- Resolve each FQDN (fully qualified domain name) to a unique IP address. Run the following
  command in the shell to resolve the FQDN (fully qualified domain name):

  ```sh
  dig +short myip.opendns.com @resolver1.opendns.com
  ```

- Set the Common Name or Subject Alternative Name value
  of any SSL (Secure Sockets Layer) certificates to the MongoDB host’s FQDN (fully qualified domain name).

The network configuration must allow each MongoDB Agent to make a direct
connection to every MongoDB deployment listed on the
Deployment page. Ops Manager does not support port forwarding.

### MongoDB 4.2 Backup Support

Enabling backup on MongoDB 4.2 hosts with an
FCV of
`4.2` has the following impact:

- Increased disk usage, disk I/O, and network I/O on each MongoDB 4.2
  host with backup enabled while a snapshot is being taken.

- Increased inbound network load to the Ops Manager host or hosts while a
  snapshot is being taken.

- Snapshots and backups use no storage capacity on Ops Manager application
  or Backup Daemon hosts.

### MongoDB Agent System User Permissions

If you want the MongoDB Agent to manage your MongoDB deployments, the
MongoDB Agent System User must have permission:

- To stop the MongoDB processes. The MongoDB Agent System User restarts
  the processes using the agent's own set of MongoDB binaries.

  If you had installed MongoDB with a package manager, use the same
  package manager to install the MongoDB Agent. This gives the
  MongoDB Agent the same owner as MongoDB.

- To `Read` and `Write` the MongoDB data directories and log
  directories.

- Set to the same user ID (UID) and group ID (GID) of the MongoDB
  process to be automated. If the MongoDB processes to be automated are
  not running as the same user and group, the Agent cannot manage those
  processes.

  **Example:**

  If your MongoDB Agent runs as the `mongod` system user in the
  `mongod` system group, the MongoDB process must also run as the
  `mongod` system user in the `mongod` system group.

  **Note:**

  On Microsoft Windows systems, the MongoDB Agent, and therefore the
  `mongod` or `mongos` services it manages, run as Windows
  services as the `SYSTEM` user. The existing MongoDB process
  should run as either `SYSTEM` or `Administrator` before adding
  it to Automation.

## Installation Options

### Installing MongoDB Enterprise Dependencies

**Warning:**

If you want to run
`MongoDB Enterprise`, you
must manually install a set of dependencies to each host *before
installing MongoDB*. Automation cannot install MongoDB Enterprise if
these dependencies are not installed.

**ubuntu:**

**ubuntu18:**

```sh
sudo apt-get install \
     libcurl4 libgssapi-krb5-2 libldap-2.4-2 liblzma5 \
     libsasl2-2 libsasl2-modules \
     libsasl2-modules-gssapi-mit libwrap0 openssl snmp
```

**ubuntu20:**

```sh
sudo apt-get install \
     libcurl4 libgssapi-krb5-2 libldap-2.4-2 liblzma5 \
     libsasl2-2 libsasl2-modules \
     libsasl2-modules-gssapi-mit libwrap0 openssl snmp
```

**ubuntu22:**

```sh
sudo apt-get install \
     libcurl4 libgssapi-krb5-2 libldap-2.5-0 liblzma5 \
     libsasl2-2 libsasl2-modules \
     libsasl2-modules-gssapi-mit libwrap0 openssl snmp
```

**Note:**

`MongoDB Connector for BI` isn't supported on Ubuntu 22.04.

**debian:**

**debian9:**

```sh
sudo apt-get install \
     libcurl3 libgssapi-krb5-2 libldap-2.4-2 liblzma5 \
     libsasl2-2 libsasl2-modules \
     libsasl2-modules-gssapi-mit libwrap0 openssl snmp
```

**debian10:**

```sh
sudo apt-get install \
     libcurl4 libgssapi-krb5-2 libldap-2.4-2 liblzma5 \
     libsasl2-2 libsasl2-modules \
     libsasl2-modules-gssapi-mit libwrap0 openssl snmp
```

**rhel:**

**rhel6:**

```sh
sudo yum install cyrus-sasl cyrus-sasl-gssapi \
     cyrus-sasl-plain krb5-libs libcurl net-snmp \
     net-snmp-libs openldap openssl xz-libs
```

**rhel7:**

```sh
sudo yum install cyrus-sasl cyrus-sasl-gssapi \
     cyrus-sasl-plain krb5-libs libcurl \
     lm_sensors-libs net-snmp net-snmp-agent-libs \
     openldap openssl tcp_wrappers-libs xz-libs
```

**rhel8:**

```sh
sudo yum install cyrus-sasl cyrus-sasl-gssapi \
     cyrus-sasl-plain krb5-libs libcurl \
     lm_sensors-libs net-snmp net-snmp-agent-libs \
     openldap openssl xz-libs
```

**suse:**

**12:**

```sh
sudo zypper install cyrus-sasl cyrus-sasl-plain \
     cyrus-sasl-gssapi krb5 libcurl4 libldap-2_4-2 \
     libopenssl1_0_0 libsensors4 libsnmp30 libwrap0 \
     liblzma5
```

**15:**

```sh
sudo zypper install cyrus-sasl cyrus-sasl-plain \
     cyrus-sasl-gssapi krb5 libcurl4 libldap-2_4-2 \
     libopenssl1_1 libsensors4 libsnmp30 libwrap0 \
     liblzma5
```

**amz:**

**v1:**

```sh
sudo yum install cyrus-sasl cyrus-sasl-gssapi \
     cyrus-sasl-plain krb5-libs libcurl net-snmp \
     net-snmp-libs openldap openssl xz-libs
```

**v2:**

```sh
sudo yum install cyrus-sasl cyrus-sasl-gssapi \
     cyrus-sasl-plain krb5-libs libcurl \
     lm_sensors-libs net-snmp net-snmp-agent-libs \
     openldap openssl tcp_wrappers-libs xz-libs
```

**v2023:**

```sh
sudo yum install cyrus-sasl cyrus-sasl-gssapi \
     cyrus-sasl-plain krb5-libs libcurl \
     lm_sensors-libs net-snmp net-snmp-agent-libs \
     openldap openssl xz-libs
```

### Installing to a Host Before Installing MongoDB

If you deploy the MongoDB Agent to a host onto which you want to have
Automation install MongoDB, ensure the system user that owns the
MongoDB Agent has `Read` and `Write` permissions on the MongoDB data
and log directories you plan to use.

### Installing to a Host that Already Runs MongoDB

If you install the MongoDB Agent to a host on which Automation is
managing a MongoDB process, the MongoDB Agent system user must have the following permissions:

- To stop the MongoDB process. The MongoDB Agent restarts the process
  using its own set of MongoDB binaries. If you had installed MongoDB
  with a package manager, use the same package manager to install the
  MongoDB Agent. This gives the MongoDB Agent the same owner as MongoDB.

- To `Read` and `Write` to the MongoDB data and log directories.
