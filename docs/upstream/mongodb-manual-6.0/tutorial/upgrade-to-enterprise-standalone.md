<!-- Converted from tutorial/upgrade-to-enterprise-standalone.txt (reStructuredText). Includes are inlined. -->

# Upgrade to MongoDB Enterprise (Standalone)

MongoDB Enterprise provides various features not available in the
MongoDB Community edition, such as:

- /core/inmemory

- /core/auditing

- /core/kerberos

- /core/security-ldap and /core/security-ldap-external

- /core/security-encryption-at-rest

The following steps outline the procedure to upgrade a standalone
`mongod` from the MongoDB Community Edition to the MongoDB
Enterprise Edition. For example, the steps can be used to upgrade
MongoDB 6.0 Community to MongoDB 6.0 Enterprise.

## About This Task

### Upgrade Major Releases

**Warning:**

Do not use these instructions to upgrade to another release version.
To upgrade release versions, refer to the appropriate release
upgrade instructions, such as Upgrade to MongoDB 6.0.

### Ops Manager

With `Ops Manager`, you can automatically upgrade
from MongoDB Community Server to MongoDB Enterprise Server.

For more information, see
`Change MongoDB Version`.

## Steps

**Step 1: Stop MongoDB Community Server**

Upgrades to a running MongoDB Server process can have 
unexpected results. Before you begin, stop the existing
`mongod` process.

**linux:**

To stop the `mongod` process, run the following
command:

```bash
sudo systemctl stop mongodb
```

**win:**

To stop the `mongod` process, run the following command
on `cmd.exe`:

```text
net stop MongoDB
```

**Step 2: Remove MongoDB Community Server**

If you installed MongoDB Community Server with a package manager
on Linux, you must remove the existing packages before you
install MongoDB Enterprise Server.

To remove MongoDB Community Server:

**rhel:**

To remove MongoDB Community Server from RHEL, CentOS, Alma
Linux, Oracle, Rocky, and Amazon Linux, run the following
command:

```bash
sudo dnf remove $(sudo rpm -qa | grep mongodb-org)
```

**debian-ubuntu:**

To remove MongoDB Community Server from Ubuntu and Debian,
run the following command:

```bash
sudo apt remove mongodb-org\*
```

**suse:**

To remove MongoDB Community Server from SUSE Enterprise
Linux, run the following command:

```bash
sudo zypper remove $(sudo rpm -qa | grep mongodb-org)
```

**macos:**

To remove MongoDB Community Server for macOS (if you
installed it with Homebrew), run the following command:

```bash
brew uninstall mongodb-community mongodb-database-tools
```

To remove the MongoDB tap from Homebrew, run the following
command:

```bash
brew untap mongodb/brew
```

**Step 3: Install MongoDB Enterprise Server**

(Include not available offline: /includes/extracts/enterprise-install-binaries)

**Step 4: Start MongoDB Enterprise Server**

Start the Enterprise `mongod` process.

**linux:**

To start MongoDB Enterprise Server, run the following
command:

```bash
sudo systemctl start mongodb
```

**win:**

To start MongoDB Enterprise Server, run the following
command in `cmd.exe`:

```bash
net start MongoDB
```

**macos:**

To start MongoDB Enterprise Server, run the following
command from the console:

```bash
mongod --config /usr/local/etc/mongodb.conf
```
