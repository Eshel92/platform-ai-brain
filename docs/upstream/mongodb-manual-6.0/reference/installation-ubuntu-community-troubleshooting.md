<!-- Converted from reference/installation-ubuntu-community-troubleshooting.txt (reStructuredText). Includes are inlined. -->

# Troubleshooting

## Errors when retrieving the public key

During Import the public key used by the package management system
step of the install-community-ubuntu-pkg procedure,  you may
encounter a `"gpg: no valid OpenPGP data found."` error.

Ensure you are copying the command exactly as documented. The operation
should respond with `OK`.

To check that the MongoDB public GPG key exists on your system,
run the following command in the terminal:

```text
sudo apt-key list
```

The output should include an entry that resembles the following:

```text
/etc/apt/trusted.gpg
--------------------
pub   rsa4096 2018-04-18 [SC] [expires: 2023-04-17]
      E162 F504 A20C DF15 827F  718D 4B7C 549A 058F 8B6B
uid           [ unknown] MongoDB {+version+} Release Signing Key <packaging@mongodb.com> 
```

## Errors when running `sudo apt update`

You may encounter one or more errors that resemble the following 
when running `sudo apt-get update` as part of the 
install-community-ubuntu-pkg procedure:

```text
W: GPG error: https://repo.mongodb.org/apt/ubuntu <release>/mongodb-org/6.0 Release: \
   The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 4B7C549A058F8B6B
E: The repository 'https://repo.mongodb.org/apt/ubuntu <release>/mongodb-org/6.0 Release' \
   is not signed.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
```

These errors indicate that the MongoDB Public GPG key was not
added in step
Import the public key used by the package management system
of the install-community-ubuntu-pkg procedure. 

Repeating the 
Import the public key used by the package management system
step of the
install-community-ubuntu-pkg procedure typically resolves this
issue. Ensure you are copying the command and key exactly as documented. 

You can validate that the MongoDB public GPG key exists on your system
by running the following command in the terminal:

```text
sudo apt-key list
```

The output should include an entry that resembles the following:

```text
--------------------
pub   rsa4096 2018-04-18 [SC] [expires: 2023-04-17]
      E162 F504 A20C DF15 827F  718D 4B7C 549A 058F 8B6B
uid           [ unknown] MongoDB {+version+} Release Signing Key <packaging@mongodb.com>
```

## Errors when running `sudo apt install -y mongodb-org`

You may encounter an error that resembles the following when running
`sudo apt install -y mongodb-org`
in step Create a list file for MongoDB of the
install-community-ubuntu-pkg procedure:

```text
Reading package lists... Done
Building dependency tree       
Reading state information... Done
E: Unable to locate package mongodb-org
```

This error indicates that the 
`/etc/apt/sources.list.d/mongodb-org-{+version+}.list`
may be configured incorrectly or is missing.

To review the contents of the `mongodb-org-{+version+}.list` file,
run the following command in the terminal or shell:

```text
cat /etc/apt/sources.list.d/mongodb-org-{+version+}.list
```

If the file contents do not exactly match the documentation for
your Ubuntu version in the step linked above, remove the file and
repeat the Create a list file for MongoDB step. 
If the file does not exist, create it as part of that step. 

Once you have validated that the `mongodb-org-{+version+}.list`
file exists and has the correct contents, run
`sudo apt update` to update the `apt` repositories and 
retry `sudo apt install -y mongodb-org`.

## Unable to install package due to `dpkg-deb: error`

You may encounter an error that resembles the following when 
installing the `mongodb-org` package:

```text
dpkg: error processing archive /var/cache/apt/archives/mongodb-org-server_6.0.0_amd64.deb (--unpack):
trying to overwrite '/usr/bin/mongod', which is also in package mongodb-server-core 1:3.6.3-0ubuntu1
```

This error indicates that the system already had the Ubuntu
`mongodb` package installed prior to installing the official
MongoDB Inc. `mongodb-org` packages. To confirm wheter the 
host has the Ubuntu `mongodb` package installed, run the 
following command in a terminal or shell:

```text
sudo apt list --installed | grep mongo
```

If your output resembles the following, you **must** uninstall
the Ubuntu `mongodb` package before retrying the
install-community-ubuntu-pkg procedure:

```text
mongodb/bionic,now 1:3.6.3-0ubuntu1 amd64 [installed]
mongodb-clients/bionic,now 1:3.6.3-0ubuntu1 amd64 [installed,automatic]
mongodb-server/bionic,bionic,now 1:3.6.3-0ubuntu1 all [installed,automatic]
mongodb-server-core/bionic,now 1:3.6.3-0ubuntu1 amd64 [installed,automatic]
```

Run the following commands in a terminal or shell to fully remove the
Ubuntu `mongodb` package before retrying the installation
procedure:

```text
sudo apt remove mongodb
sudo apt purge mongodb
sudo apt autoremove
```

**Note:**

`sudo apt purge mongodb` removes any default configuration files
installed by the Ubuntu `mongodb` package. If you have
modified these configuration files *and* want to keep those
modifications, copy the files to another directory such as 
`/home/your-user-name`.

If your output includes a mix of `mongodb-org` and
`mongodb` binaries, you may need to first `apt remove`, ``apt
purge`, and `apt autoremove` the `mongodb-org`` package
before attempting to remove and purge the Ubuntu `mongodb`
package. After clearing  all MongoDB-related packages, retry the
installation procedure.

## `mongod` reports errors related to opening a socket

You may encounter the `Socket is already in use` or
`Failed to unlink socket file` errors when starting a 
`mongod`. These errors generally indicate
another process using the configured port for the 
`mongod` process, typically another 
`mongod` running on the system.

The following example uses the `ss` utility to list all open 
TCP (`-t`) or UDP (`-u`) sockets in the `LISTEN` (`-l`) state 
and the process using each socket (`-p`)
without resolving any service names or hostnames (`-n`).

```text
sudo ss -tulpn
```

The following partial output shows a `mongod` process 
listening on the `27017` port. Attempting to run another `mongod` 
process on that same port will result in socket errors.

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

If the system has a `mongod` or other system 
process running on your desired port, you must either shut the 
existing process down *or* select a new port for the new
`mongod` process. You can specify the 
`net.port` configuration file 
option to change the port that the `mongod` 
listens on.

## `mongod` reports errors related to the data directory

Users may encounter errors that resemble the following in the
`mongod` 
process log:

```text
Data directory ... not found

Attempted to create lock file on a read-only directory: ...
```

Generally, these errors indicate that the MongoDB data directory
either doesn't exist, or isn't accessible to the
`mongod`.

### The data directory must exist

The data directory is specified with the `storage.dbPath`
setting in the configuration file, or
with the `--dbpath` option to
`mongod` on the command line.

- If you installed MongoDB via the `apt` package manager, the default
  `/etc/mongod.conf` configuration file
  sets `storage.dbPath` to `/var/lib/mongodb`.

- If you are running `mongod` on the command
  line, and omitting the `--dbpath` option
  entirely, MongoDB uses a default `--dbpath` of `/data/db`.

Whether you are using one of the data directory paths above, or
providing your own path in the configuration file or on the command
line, make sure that the data directory exists on your filesystem
prior to starting the `mongod`. You can create
directories on Ubuntu with the `mkdir` command.

### The data directory must be accessible

The data directory must be configured with the appropriate
permissions and ownership settings to allow the
`mongod` to read, write, and
navigate the directory contents (`rwx` user or group permissions).

Use `chown`, and `chmod` to modify permissions and set
`user:group` ownership as appropriate prior to starting the
`mongod`.

### Starting `mongod` using the data directory

Users starting the `mongod` as a service (e.g. using either ``sudo
systemctl start mongod` or `sudo service mongod start``) typically
only see these errors if they modified the default
`dbPath` value in the `/etc/mongod.conf` to:

* A directory that does not allow the `mongodb` user or `mongodb` 
  group to read, write, or execute (`rwx`) the directory and its 
  contents, *or*

* A directory that does not exist.

Users starting the `mongod` without using the
service definition (e.g. using the terminal to launch `mongod`) 
typically see these errors if:

* The directory specified to `dbPath` or 
  `--dbpath` does not allow the user or a 
  group to which the user belongs to read, write, and execute 
  (`rwx`) the directory or its contents, *or*

* The specified data directory does not exist.
