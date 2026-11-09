<!-- Converted from modules/cassandra/pages/installing/installing.adoc (AsciiDoc). Includes are inlined. -->

# Installing Cassandra

Apache Cassandra can be installed on a number of Linux distributions:

* AlmaLinux
* Amazon Linux Amazon Machine Images (AMIs)
* Debian
* RedHat Enterprise Linux (RHEL)
* SUSE Enterprise Linux
* Ubuntu

This is not an exhaustive list of operating system platforms, nor is it prescriptive.
However, users are well-advised to conduct exhaustive tests if using a less-popular distribution of Linux.
Deploying on older Linux versions is not recommended unless you have previous experience with the older distribution in a production environment.

## Prerequisites

* Install the latest version of Java 11 or Java 17, from one of the following locations:
** [Oracle Java Standard Edition 11 Archived Version](https://www.oracle.com/java/technologies/javase/jdk11-archive-downloads.html)
** [Oracle Java Standard Edition 17](https://www.oracle.com/java/technologies/downloads/#java17)
** [OpenJDK 11](https://jdk.java.net/archive/)
** [OpenJDK 17](https://jdk.java.net/archive/)

. Verify the version of Java installed. For example:

Command::
+
--
```shell
$ java -version

```
--

Result::
+
--
```plaintext
openjdk version "11.0.20" 2023-07-18
OpenJDK Runtime Environment Temurin-11.0.20+8 (build 11.0.20+8)
OpenJDK 64-Bit Server VM Temurin-11.0.20+8 (build 11.0.20+8, mixed mode)
```
--

* To use the CQL shell `cqlsh`, install the latest version of Python 3.8-3.11.

To verify that you have the correct version of Python installed, type `python --version`.

**Note:**
Support for Python 2.7 is deprecated.

## Choosing an installation method

There are three methods of installing Cassandra that are common:

* Docker image
* Tarball binary file
* Package installation (RPM, YUM)

If you are a current Docker user, installing a Docker image is simple.
You'll need to install Docker Desktop for Mac, Docker Desktop for Windows, or have `docker` installed on Linux.
Pull the appropriate image from the Docker Hub and start Cassandra with a `docker run` command.

For many users, installing the binary tarball is also a simple choice.
The tarball unpacks all its contents into a single location with binaries and configuration files located in their own subdirectories.
The most obvious advantage of a tarball installation is that it does not require `root` permissions and can be installed on any Linux
distribution.

Packaged installations require `root` permissions, and are most appropriate for production installs.
Install the RPM build on CentOS and RHEL-based distributions if you want to install Cassandra using YUM.
Install the Debian build on Ubuntu and other Debian-based distributions if you want to install Cassandra using APT.

**Warning:**
Note that both the YUM and APT methods required `root` permissions and will install the binaries and configuration files as the `cassandra` OS user.

## Install with Docker

. Pull the docker image. For the latest image, use:
+
```shell
docker pull cassandra:latest

```
+
This `docker pull` command will get the latest version of the official Docker
Apache Cassandra image available from the [Dockerhub](https://hub.docker.com/_/cassandra).
. Start Cassandra with a `docker run` command:
+
```shell
docker run --name cass_cluster cassandra:latest

```
+
The `--name` option will be the name of the Cassandra cluster created.
This example uses the name `cass_cluster`.
. Start the CQL shell, `cqlsh` to interact with the Cassandra node created:
+
```shell
docker exec -it cass_cluster cqlsh

```

## Install tarball file

. Verify the version of Java installed. For example:

Command::
+
--
```shell
$ java -version

```
--

Result::
+
--
```plaintext
openjdk version "11.0.20" 2023-07-18
OpenJDK Runtime Environment Temurin-11.0.20+8 (build 11.0.20+8)
OpenJDK 64-Bit Server VM Temurin-11.0.20+8 (build 11.0.20+8, mixed mode)
```
--

. Download the binary tarball from one of the mirrors on the {cass_url}download/[Apache Cassandra Download] site.
For example, to download Cassandra {40_version}:
+
```shell
$ curl -OL http://apache.mirror.digitalpacific.com.au/cassandra/4.0.0/apache-cassandra-4.0.0-bin.tar.gz

```
+

**Note:**
The mirrors only host the latest versions of each major supported release.
To download an earlier version of Cassandra, visit the [Apache Archives](http://archive.apache.org/dist/cassandra/).
. OPTIONAL: Verify the integrity of the downloaded tarball using one of the methods [here](https://www.apache.org/dyn/closer.cgi#verify).
For example, to verify the hash of the downloaded file using GPG:
+
Command::
+
--
```shell
$ gpg --print-md SHA256 apache-cassandra-4.0.0-bin.tar.gz

```
--

Result::
+
--
```plaintext
apache-cassandra-4.0.0-bin.tar.gz: 28757DDE 589F7041 0F9A6A95 C39EE7E6
                                   CDE63440 E2B06B91 AE6B2006 14FA364D

```
--
+
Compare the signature with the SHA256 file from the Downloads site:
+
Command::
+
--
```shell
$ curl -L https://downloads.apache.org/cassandra/4.0.0/apache-cassandra-4.0.0-bin.tar.gz.sha256

```
--

Result::
+
--
```console
28757dde589f70410f9a6a95c39ee7e6cde63440e2b06b91ae6b200614fa364d
```
--
. Unpack the tarball:
+
```shell
$ tar xzvf apache-cassandra-4.0.0-bin.tar.gz

```
+
The files will be extracted to the `apache-cassandra-4.0.0/` directory.
This is the tarball installation location.
. Located in the tarball installation location are the directories for the scripts, binaries, utilities, configuration, data and log files:
+
```plaintext
<tarball_installation>/
    bin/		<1>
    conf/		<2>
    data/		<3>
    doc/
    interface/
    javadoc/
    lib/
    logs/		<4>
    pylib/
    tools/		<5>

```
<1> location of the commands to run cassandra, cqlsh, nodetool, and SSTable tools
<2> location of cassandra.yaml and other configuration files
<3> location of the commit logs, hints, and SSTables
<4> location of system and debug logs
<5>location of cassandra-stress tool
+
. Start Cassandra:
+
```shell
$ cd apache-cassandra-4.0.0/ && bin/cassandra

```
+

**Note:**
This will run Cassandra as the authenticated Linux user.
+
. Monitor the progress of the startup with:
+
Command::
+
--
```shell
$ tail -f logs/system.log

```
--

Result::
+
--
Cassandra is ready when you see an entry like this in the `system.log`:
+
```plaintext
INFO  [main] 2019-12-17 03:03:37,526 Server.java:156 - Starting listening for CQL clients on localhost/127.0.0.1:9042 (unencrypted)...

```
--

+

**Note:**
See configuring Cassandra for configuration information.

. Check the status of Cassandra:
+
```shell
$ bin/nodetool status

```
+
The status column in the output should report `UN` which stands for "Up/Normal".
+
Alternatively, connect to the database with:
+
```shell
$ bin/cqlsh

```

## Install as Debian package

. Verify the version of Java installed. For example:

Command::
+
--
```shell
$ java -version

```
--

Result::
+
--
```plaintext
openjdk version "11.0.20" 2023-07-18
OpenJDK Runtime Environment Temurin-11.0.20+8 (build 11.0.20+8)
OpenJDK 64-Bit Server VM Temurin-11.0.20+8 (build 11.0.20+8, mixed mode)
```
--

. Add the Apache repository of Cassandra to the file `cassandra.sources.list`.
+
The latest major version is {50_version} and the corresponding distribution name is `50x` (with an "x" as the suffix).
For older releases use:

* `50x` for C* {50_version} series
* `41x` for C* {41_version} series
* `40x` for C* {40_version} series

For example, to add the repository for version {50_version} (`50x`):

+
```shell
$ echo "deb [signed-by=/etc/apt/keyrings/apache-cassandra.asc] https://debian.cassandra.apache.org 50x main" | sudo tee -a /etc/apt/sources.list.d/cassandra.sources.list
deb https://debian.cassandra.apache.org 50x main

```
. Add the Apache Cassandra repository keys to the list of trusted keys on the server:
+
Command::
+
--
```shell
$ curl -o /etc/apt/keyrings/apache-cassandra.asc https://downloads.apache.org/cassandra/KEYS

```
--

Result::
+
--
```plaintext
% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  266k  100  266k    0     0   320k      0 --:--:-- --:--:-- --:--:--  320k
OK

```
--
. Update the package index from sources:
+
```shell
$ sudo apt-get update

```
. Install Cassandra with APT:
+
```shell
$ sudo apt-get install cassandra

```
+
. Monitor the progress of the startup with:
+
Command::
+
--
```shell
$ tail -f logs/system.log

```
--

Result::
+
--
Cassandra is ready when you see an entry like this in the `system.log`:
+
```plaintext
INFO  [main] 2019-12-17 03:03:37,526 Server.java:156 - Starting listening for CQL clients on localhost/127.0.0.1:9042 (unencrypted)...

```
--

+

**Note:**
See configuring Cassandra for configuration information.

. Check the status of Cassandra:
+
```shell
$ nodetool status

```
+
The status column in the output should report `UN` which stands for "Up/Normal".
+
Alternatively, connect to the database with:
+
```shell
$ cqlsh

```

## Install as RPM package

. Verify the version of Java installed. For example:

Command::
+
--
```shell
$ java -version

```
--

Result::
+
--
```plaintext
openjdk version "11.0.20" 2023-07-18
OpenJDK Runtime Environment Temurin-11.0.20+8 (build 11.0.20+8)
OpenJDK 64-Bit Server VM Temurin-11.0.20+8 (build 11.0.20+8, mixed mode)
```
--

. Add the Apache repository of Cassandra to the file `/etc/yum.repos.d/cassandra.repo` (as the `root` user).
+
The latest major version is {50_version} and the corresponding distribution name is `50x` (with an "x" as the suffix).
For older releases use:

* `50x` for C* {50_version} series
* `41x` for C* {41_version} series
* `40x` for C* {40_version} series

For example, to add the repository for version {50_version} (`50x`):

+
```plaintext
[cassandra]
name=Apache Cassandra
baseurl=https://redhat.cassandra.apache.org/42x/
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://downloads.apache.org/cassandra/KEYS

```
. Update the package index from sources:
+
```shell
$ sudo yum update

```
. Install Cassandra with YUM:
+
```shell
$ sudo yum install cassandra

```
+

**Note:**
A new Linux user `cassandra` will get created as part of the installation.
The Cassandra service will also be run as this user.
. Start the Cassandra service:
+
```shell
$ sudo service cassandra start

```
+
. Monitor the progress of the startup with:
+
Command::
+
--
```shell
$ tail -f logs/system.log

```
--

Result::
+
--
Cassandra is ready when you see an entry like this in the `system.log`:
+
```plaintext
INFO  [main] 2019-12-17 03:03:37,526 Server.java:156 - Starting listening for CQL clients on localhost/127.0.0.1:9042 (unencrypted)...

```
--

+

**Note:**
See configuring Cassandra for configuration information.

. Check the status of Cassandra:
+
```shell
$ nodetool status

```
+
The status column in the output should report `UN` which stands for "Up/Normal".
+
Alternatively, connect to the database with:
+
```shell
$ cqlsh

```

## Further installation info

For help with installation issues, see the Troubleshooting section.
