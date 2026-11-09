<!-- Converted from reference/installation-ubuntu-community-troubleshooting.txt (reStructuredText). Includes are inlined. -->

# Troubleshooting

## Public Key Retrieval Errors

Occurs during the Import the public key used by the package management system
step of install-community-ubuntu-pkg.

```text
gpg: no valid OpenPGP data found.
```

### Solution

Copy the command exactly as documented. The operation should respond with `OK`.

Verify that the MongoDB public GPG key exists on your system:

```text
sudo apt-key list
```

Expected output resembles the following:

```text
/etc/apt/trusted.gpg
--------------------
pub   rsa4096 2018-04-18 [SC] [expires: 2023-04-17]
      E162 F504 A20C DF15 827F  718D 4B7C 549A 058F 8B6B
uid           [ unknown] MongoDB {+version+} Release Signing Key <packaging@mongodb.com> 
```

## `sudo apt update` Errors

Occurs after running `sudo apt update` as part of the
install-community-ubuntu-pkg procedure. Often caused by a missing MongoDB Public GPG key.

```text
W: GPG error: https://repo.mongodb.org/apt/ubuntu <release>/mongodb-org/7.0 Release: \
   The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 4B7C549A058F8B6B
E: The repository 'https://repo.mongodb.org/apt/ubuntu <release>/mongodb-org/7.0 Release' \
   is not signed.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
```

### Solution

Repeat the Import the public key used by the package management system
step in install-community-ubuntu-pkg. Copy the command and key exactly
as documented.

Verify the key:

```text
sudo apt-key list
```

Expected output:

```text
--------------------
pub   rsa4096 2018-04-18 [SC] [expires: 2023-04-17]
      E162 F504 A20C DF15 827F  718D 4B7C 549A 058F 8B6B
uid           [ unknown] MongoDB {+version+} Release Signing Key <packaging@mongodb.com>
```

## `sudo apt install -y mongodb-org` Errors

Occurs after running `sudo apt install -y mongodb-org` 
in step Create a list file for MongoDB of the
install-community-ubuntu-pkg procedure. Often caused by a missing or 
misconfigured `/etc/apt/sources.list.d/mongodb-org-{+version+}.list` file.

```text
Reading package lists... Done
Building dependency tree       
Reading state information... Done
E: Unable to locate package mongodb-org
```

### Solution

1. Check the file contents:

   ```text
   cat /etc/apt/sources.list.d/mongodb-org-{+version+}.list
   ```

2. If contents don't match the documentation for your Ubuntu version, remove
   the file and repeat Create a list file for MongoDB step.

3. If the file doesn't exist, create it during that step.

4. Update repositories and retry installation:

   ```text
   sudo apt update
   sudo apt install -y mongodb-org
   ```

## `dpkg-deb: error` Package Conflicts

Occurs during `sudo apt install -y mongodb-org` step of the
install-community-ubuntu-pkg procedure. Often caused by a conflicting 
Ubuntu `mongodb` package already installed.

```text
dpkg: error processing archive /var/cache/apt/archives/mongodb-org-server_7.0.0_amd64.deb (--unpack):
trying to overwrite '/usr/bin/mongod', which is also in package mongodb-server-core 1:3.6.3-0ubuntu1
```

### Solution

Check for conflict:

```text
sudo apt list --installed | grep mongo
```

```text
mongodb/bionic,now 1:3.6.3-0ubuntu1 amd64 [installed]
mongodb-clients/bionic,now 1:3.6.3-0ubuntu1 amd64 [installed,automatic]
mongodb-server/bionic,bionic,now 1:3.6.3-0ubuntu1 all [installed,automatic]
mongodb-server-core/bionic,now 1:3.6.3-0ubuntu1 amd64 [installed,automatic]
```

If output shows Ubuntu packages like this, remove them:

```text
sudo apt remove mongodb
sudo apt purge mongodb
sudo apt autoremove
```

**Note:**

`sudo apt purge mongodb` removes default configuration files. To preserve 
modified configuration files, copy them to another directory (e.g., 
`/home/your-user-name`) before purging.

For mixed packages:

If output shows both `mongodb-org` and `mongodb` packages, remove
`mongodb-org` first, then remove `mongodb` packages. After
clearing all MongoDB-related packages, retry install-community-ubuntu-pkg.

## `mongod` Socket Errors

Occurs when starting a `mongod`. Often caused by another 
process (typically another `mongod`) using the
configured port.

```text
Socket is already in use
```

```text
Failed to unlink socket file
```

### Solution

Identify the process:

The following example uses `ss` to list all open TCP (`-t`) and UDP (`-u`)
sockets in the `LISTEN` (`-l`) state and the process using each socket 
(`-p`) without resolving any service names or hostnames (`-n`):

```text
sudo ss -tulpn
```

Example output showing `mongod` on port `27017`:

```text
Netid        State        Local Address:Port 
udp          UNCONN       127.0.0.53%lo:53        users:(("systemd-resolve",pid=663,fd=12))
udp          UNCONN   10.1.16.87%enp0s3:68        users:(("systemd-network",pid=652,fd=15))
tcp          LISTEN       127.0.0.53%lo:53        users:(("systemd-resolve",pid=663,fd=13))
tcp          LISTEN             0.0.0.0:22        users:(("sshd",pid=819,fd=3))
tcp          LISTEN        192.168.1.15:27017     users:(("mongod",pid=10027,fd=12))
tcp          LISTEN           127.0.0.1:27017     users:(("mongod",pid=10027,fd=11))
tcp          LISTEN                 ::]:22        users:(("sshd",pid=819,fd=4))
```

You can either:

- Shut down the existing process
- Select a new port for the conflicting `mongod` process:
   1. Modify `net.port` in the configuration file
   2. Use `--port` on the command line

## Data Directory Errors

Occurs in the `mongod` 
process log. Often caused by a data 
directory that doesn't exist or isn't accessible to the
`mongod`.

```text
Data directory ... not found

Attempted to create lock file on a read-only directory: ...
```

When starting as a service (`sudo systemctl start mongod` or ``sudo 
service mongod start``), this may mean:

- `dbPath` in `/etc/mongod.conf` points to a directory
  without `rwx` permissions for `mongodb` user or group
- `dbPath` points to a nonexistent directory

When starting from the terminal, this may mean:

- `dbPath` or `--dbpath` points to
  a directory without `rwx` permissions for the user or their group
- The Directory doesn't exist

### Solution

Depending on the cause, either create the data directory or set appropriate
permissions and ownership.

- Create the directory:

  Specify the data directory with `storage.dbPath` in the
  configuration file or
  `--dbpath` on the command line.

- Set default paths:

  - `apt` package manager installation: The default `/etc/mongod.conf`
    configuration file sets `storage.dbPath`
    to `/var/lib/mongodb`
  - `mongod` on the command line without
    `--dbpath`: `/data/db`

  Ensure that the data directory exists or create the directory  using `mkdir`
  before starting `mongod`.

- Set directory permissions:

  Set appropriate permissions and ownership:

  - The `mongod` needs `rwx` (read, write, execute)
    permissions
  - Use `chown` and `chmod` to configure `user:group` ownership and
    permissions prior to starting the `mongod`
