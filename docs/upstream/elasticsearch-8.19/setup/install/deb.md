<!-- Converted from setup/install/deb.asciidoc (AsciiDoc). Includes are inlined. -->

### Install Elasticsearch with Debian Package

The Debian package for Elasticsearch can be downloaded from our website
or from our APT repository. It can be used to install
Elasticsearch on any Debian-based system such as Debian and Ubuntu.

This package contains both free and subscription features.
Start a 30-day trial to try out all of the features.

The latest stable version of Elasticsearch can be found on the
link:/downloads/elasticsearch[Download Elasticsearch] page. Other versions can
be found on the link:/downloads/past-releases[Past Releases page].

**Note:** Elasticsearch includes a bundled version of [OpenJDK](https://openjdk.java.net)
from the JDK maintainers (GPLv2+CE). To use your own version of Java,
see the JVM version requirements

#### Import the Elasticsearch PGP Key

We sign all of our packages with the Elasticsearch Signing Key (PGP key
[D88E42B4](https://pgp.mit.edu/pks/lookup?op=vindex&search=0xD27D666CD88E42B4),
available from https://pgp.mit.edu) with fingerprint:

    4609 5ACC 8548 582C 1A26 99A9 D27D 666C D88E 42B4

Download and install the public signing key:

```sh
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo gpg --dearmor -o /usr/share/keyrings/elasticsearch-keyring.gpg
```

#### Installing from the APT repository

**Warning:** Version {version} of Elasticsearch has not yet been released.

You may need to install the `apt-transport-https` package on Debian before proceeding:

```sh
sudo apt-get install apt-transport-https
```

Save the repository definition to  /etc/apt/sources.list.d/elastic-{major-version}.list:

```
echo "deb [signed-by=/usr/share/keyrings/elasticsearch-keyring.gpg] https://artifacts.elastic.co/packages/{major-version}/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-{major-version}.list
```

```
echo "deb [signed-by=/usr/share/keyrings/elasticsearch-keyring.gpg] https://artifacts.elastic.co/packages/{major-version}-prerelease/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-{major-version}.list
```

==================================================

These instructions do not use `add-apt-repository` for several reasons:

. `add-apt-repository` adds entries to the system `/etc/apt/sources.list` file
  rather than a clean per-repository file in `/etc/apt/sources.list.d`
. `add-apt-repository` is not part of the default install on many distributions
  and requires a number of non-default dependencies.
. Older versions of `add-apt-repository` always add a `deb-src` entry which
  will cause errors because we do not provide a source package. If you have added
  the `deb-src` entry, you will see an error like the following until you delete
  the `deb-src` line:

    Unable to find expected entry 'main/source/Sources' in Release file
    (Wrong sources.list entry or malformed file)

==================================================

You can install the Elasticsearch Debian package with:

```sh
sudo apt-get update && sudo apt-get install elasticsearch
```

==================================================
If two entries exist for the same Elasticsearch repository, you will see an error like this during `apt-get update`:

Duplicate sources.list entry https://artifacts.elastic.co/packages/{major-version}/apt/ ...`

Examine /etc/apt/sources.list.d/elasticsearch-{major-version}.list for the duplicate entry or locate the duplicate entry amongst the files in `/etc/apt/sources.list.d/` and the `/etc/apt/sources.list` file.
==================================================

**Note:** On systemd-based distributions, the installation scripts will attempt to set kernel parameters (e.g.,
`vm.max_map_count`); you can skip this by masking the systemd-sysctl.service unit.

#### Download and install the Debian package manually

**Warning:** Version {version} of Elasticsearch has not yet been released.

The Debian package for Elasticsearch v{version} can be downloaded from the website and installed as follows:

```
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-{version}-amd64.deb
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-{version}-amd64.deb.sha512
shasum -a 512 -c elasticsearch-{version}-amd64.deb.sha512 <1>
sudo dpkg -i elasticsearch-{version}-amd64.deb
```
<1> Compares the SHA of the downloaded Debian package and the published checksum, which should output
    `elasticsearch-{version}-amd64.deb: OK`.

(See `setup/install/package-security.md`)

#### Enable automatic creation of system indices

Some commercial features automatically create indices within Elasticsearch.
By default, Elasticsearch is configured to allow automatic index creation, and no
additional steps are required. However, if you have disabled automatic index
creation in Elasticsearch, you must configure
`action.auto_create_index` in `elasticsearch.yml` to allow
the commercial features to create the following indices:

```yaml
action.auto_create_index: .monitoring*,.watches,.triggered_watches,.watcher-history*,.ml*
```

=============================================================================
If you are using [Logstash](https://www.elastic.co/products/logstash)
or [Beats](https://www.elastic.co/products/beats) then you will most likely
require additional index names in your `action.auto_create_index` setting, and
the exact value will depend on your local configuration. If you are unsure of
the correct value for your environment, you may consider setting the value to
 `*` which will allow automatic creation of all indices.
=============================================================================

(See `setup/install/systemd.md`)

(See `setup/install/check-running.md`)

#### Configuring Elasticsearch

The `/etc/elasticsearch` directory contains the default runtime configuration
for Elasticsearch. The ownership of this directory and all contained files are set to
`root:elasticsearch` on package installations.

The `setgid` flag applies group permissions on the `/etc/elasticsearch`
directory to ensure that Elasticsearch can read any contained files and subdirectories.
All files and subdirectories inherit the `root:elasticsearch` ownership.
Running commands from this directory or any subdirectories, such as the
elasticsearch-keystore tool, requires `root:elasticsearch`
permissions.

Elasticsearch loads its configuration from the
`/etc/elasticsearch/elasticsearch.yml` file by default. The format of this
config file is explained in settings.

The Debian package also has a system configuration file (`/etc/default/elasticsearch`),
which allows you to set the following parameters:

`ES_JAVA_HOME`::

  Set a custom Java path to be used.

`ES_PATH_CONF`::

    Configuration file directory (which needs to include `elasticsearch.yml`,
    `jvm.options`, and `log4j2.properties` files); defaults to
    `/etc/elasticsearch`.

`ES_JAVA_OPTS`::

    Any additional JVM system properties you may want to apply.

`RESTART_ON_UPGRADE`::

    Configure restart on package upgrade, defaults to `false`. This means you
    will have to restart your Elasticsearch instance after installing a
    package manually. The reason for this is to ensure, that upgrades in a
    cluster do not result in a continuous shard reallocation resulting in high
    network traffic and reducing the response times of your cluster.

**Note:** Distributions that use `systemd` require that system resource limits be
configured via `systemd` rather than via the `/etc/sysconfig/elasticsearch`
file. See systemd for more information.

(See `setup/install/connect-clients.md`)

#### Directory layout of Debian package

The Debian package places config files, logs, and the data directory in the appropriate
locations for a Debian-based system:

|=======================================================================
| Type | Description | Default Location | Setting
| home
  | Elasticsearch home directory or `$ES_HOME`
  | /usr/share/elasticsearch
 d|

| bin
  | Binary scripts including `elasticsearch` to start a node
    and `elasticsearch-plugin` to install plugins
  | /usr/share/elasticsearch/bin
 d|

| conf
  | Configuration files including `elasticsearch.yml`
  | /etc/elasticsearch
  | ES_PATH_CONF

| conf
  | Environment variables including heap size, file descriptors.
  | /etc/default/elasticsearch
 d|

| conf
| Generated TLS keys and certificates for the transport and http layer.
| /etc/elasticsearch/certs
d|

| data
  | The location of the data files of each index / shard allocated
    on the node.
  | /var/lib/elasticsearch
  | path.data

| jdk
  | The bundled Java Development Kit used to run Elasticsearch. Can
    be overridden by setting the `ES_JAVA_HOME` environment variable
    in `/etc/default/elasticsearch`.
  | /usr/share/elasticsearch/jdk
 d|

| logs
  | Log files location.
  | /var/log/elasticsearch
  | path.logs

| plugins
  | Plugin files location. Each plugin will be contained in a subdirectory.
  | /usr/share/elasticsearch/plugins
  |

| repo
  | Shared file system repository locations. Can hold multiple locations. A file system repository can be placed in to any subdirectory of any directory specified here.
 d| Not configured
  | path.repo

|=======================================================================

(See `setup/install/security-files-reference.md`)
(See `setup/install/next-steps.md`)
