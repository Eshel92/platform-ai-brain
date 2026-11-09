<!-- Converted from tutorial/install-mongodb-agent-prereq.txt (reStructuredText). Includes are inlined. -->

# MongoDB Agent Prerequisites

This section describes the requirements for the hosts that run the 
MongoDB Agent.

Hosts that run MongoDB Agents must run on a 64-bit version of one of
the following hardware architectures and operating systems. The 
following table lists the MongoDB Server versions that you can deploy 
with the MongoDB Agent on the associated platforms:

| Architecture | Distro/OS | 7.0 | 6.0 | 5.0 |
|---|---|---|---|---|
| x86_64 | RHEL/Oracle Linux 7 `1` | check-circle | check-circle | check-circle |
|  | RHEL/Rocky/Alma Linux/Oracle Linux 8 `1` | check-circle | check-circle | check-circle |
|  | RHEL/Rocky/Alma Linux/Oracle Linux 9 `1` | check-circle | check-circle | check-circle |
|  | Amazon Linux 2 | check-circle | check-circle | check-circle |
|  | Amazon Linux 2023 | check-circle |  |  |
|  | SUSE12 | check-circle | check-circle | check-circle |
|  | SUSE15 | check-circle | check-circle | check-circle |
|  | Debian 9 |  |  | check-circle |
|  | Debian 10 |  | check-circle | check-circle |
|  | Debian 11 | check-circle | check-circle | check-circle |
|  | Debian 12 | check-circle |  |  |
|  | Ubuntu 18.x |  | check-circle | check-circle |
|  | Ubuntu 20.x | check-circle | check-circle | check-circle |
|  | Ubuntu 22.x `2` | check-circle | check-circle |  |
|  | Windows | check-circle | check-circle | check-circle |
| ARM | RHEL 8 | check-circle | check-circle | check-circle |
|  | RHEL 9 | check-circle | check-circle |  |
|  | Amazon Linux 2 | check-circle | check-circle | check-circle |
|  | Amazon Linux 2023 | check-circle |  |  |
|  | Ubuntu 20.x | check-circle |  |  |
| PowerPC/ ppc64le | RHEL 7 | check-circle | check-circle | check-circle |
|  | RHEL 8 | check-circle | check-circle | check-circle |
| zSeries/ 390x | RHEL 7 | check-circle | check-circle | check-circle |
|  | RHEL 8 | check-circle | check-circle | check-circle |
|  | RHEL 9 | check-circle |  |  |

`1` MongoDB supports Oracle Linux running
RHCK (Red Hat Compatible Kernel) only. 
MongoDB doesn't support Oracle Linux running
UEK (Unbreakable Enterprise Kernel).

`2` `MongoDB Connector for BI` isn't supported on Ubuntu 22.04.

## Hardware Requirements

### Use 64-bit Chip Architectures

The MongoDB Agent must run on 64-bit architectures.

### Provide Sufficient CPU and RAM

MongoDB recommends a minimum of 2 CPU cores and 2 GB of RAM for
MongoDB Agent hosts.

If you activate backup, all MongoDB Agent
hosts require *at least* an additional 2 CPU cores and 3 GB of RAM 
beyond basic platform requirements. Each backup job that the 
MongoDB Agent runs further impacts host performance.

## Set Host Network Access

The hosts that serve the MongoDB deployments must:

- Have full network access to each other through their Fully
  Qualified Domain Names (FQDNs). Each host must reach each other host
  through the FQDN (fully qualified domain name).

- Permit Automation to start `mongod` on a random ephemeral port and
  connect to that port when restoring your deployment from a backup.

**windows:**

- Find the FQDN (fully qualified domain name) for each host. Run the following command in
  Powershell:

  ```powershell
  net config workstation | findstr /C:"Full Computer name"
  ```

- Download and install the
  [Windows BIND](http://www.isc.org/downloads/) tools.

**debian:**

- Find the FQDN (fully qualified domain name) for each host. Run the following command in
  the shell:

  ```sh
  hostname -f
  ```

**rhel:**

- Find the FQDN (fully qualified domain name) for each host. Run the following command in
  the shell:

  ```sh
  hostname -f
  ```

**linux:**

- Find the FQDN (fully qualified domain name) for each host. Run the following command in
  the shell:

  ```sh
  hostname -f
  ```

- Resolve each FQDN (fully qualified domain name) to a unique IP address. Run the following
  command in the shell to resolve the FQDN (fully qualified domain name):

  ```shell
  dig +short myip.opendns.com @resolver1.opendns.com
  ```

- Set the Common Name or Subject Alternative Name value
  of any SSL (Secure Sockets Layer) certificates to the MongoDB host's FQDN (fully qualified domain name).

The network configuration must allow each MongoDB Agent to
make a direct connection to each MongoDB deployment listed on the
Deployment page. Ops Manager does not support port forwarding.

**windows:**

### Disable Windows Firewall Stealth Mode

For best performance,
[Disable Windows Firewall stealth mode](https://support.microsoft.com/en-us/help/2586744/disable-stealth-mode)
on the MongoDB hosts on which you installed the MongoDB Agent.

## Set Host Permissions

### On a Host that Already Runs MongoDB

If you install the MongoDB Agent on a host that is running a MongoDB
process, the agent must have:

- Permission to stop any MongoDB processes. The MongoDB Agent restarts the
  process using the Agent's own set of MongoDB binaries. If you installed
  MongoDB with a package manager, use the same package manager to install
  the MongoDB Agent. This gives the MongoDB Agent the same owner as MongoDB.

- `Read` and `Write` permissions on the MongoDB data directory and
  log directory.

### On a Host Before Installing MongoDB

If you deploy the MongoDB Agent to a host that doesn't have MongoDB
installed, ensure the user that owns the MongoDB Agent has `Read` and
`Write` permissions on the MongoDB data and log directories you plan
to use.

### Root Access

**debian:**

To install the MongoDB Agent using a `deb` package, log in as
`root` or a user with `sudo` privileges.

**rhel:**

To install the MongoDB Agent using a `.rpm` package, log in as
`root` or a user with `sudo` privileges.

**linux:**

To install the MongoDB Agent using a `.tar` package, log in as
`root` or a user with `sudo` privileges.

## Acquire an Agent API (Application Programming Interface) Key

The MongoDB Agent requires one Agent API (Application Programming Interface) Key per project to communicate
with the Ops Manager Application.

If you do not have an existing Agent API (Application Programming Interface) Key for your Ops Manager project,
create one:

1. Click Deployment.

#. Navigate to Agents.

#. Click Agent API Keys.

#. Click plus Generate.

   **Note:**

   This button appears if:

   1. The current user is the `Project Owner` and
   #. The project has no Agent API Keys other than the
      Original Group API Key with an exclamation exclamation-circle
      next to it. This type of key exists in projects created before
      the new Agent API Key model.
      In the new model, you can create multiple Agent API (Application Programming Interface) Keys in
      a project, and any the project's MongoDB Agents can use any of
      the keys.

#. In the Generate Key modal, provide a description of the
   new Agent API Key in the Description box.

#. Click Generate.

   **Important:**

   When you generate an Agent API Key, Ops Manager displays it **one time
   only**. You must copy this key. Treat it like a password; store
   it in a secure place. Ops Manager never displays the full key again.
