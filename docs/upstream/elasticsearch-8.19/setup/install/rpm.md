<!-- Converted from setup/install/rpm.asciidoc (AsciiDoc). Includes are inlined. -->

### Install Elasticsearch with RPM

The RPM for Elasticsearch can be downloaded from our website
or from our  RPM repository. It can be used to install
Elasticsearch on any RPM-based system such as OpenSuSE, SLES, Centos, Red Hat,
and Oracle Enterprise.

**Note:** RPM install is not supported on distributions with old versions of RPM,
such as SLES 11 and CentOS 5. Please see targz instead.

This package contains both free and subscription features.
Start a 30-day trial to try out all of the features.

The latest stable version of Elasticsearch can be found on the
link:/downloads/elasticsearch[Download Elasticsearch] page. Other versions can
be found on the link:/downloads/past-releases[Past Releases page].

**Note:** Elasticsearch includes a bundled version of [OpenJDK](https://openjdk.java.net)
from the JDK maintainers (GPLv2+CE). To use your own version of Java,
see the JVM version requirements

**Tip:** For a step-by-step example of setting up the Elastic Stack on your own premises, try out our tutorial: {stack-ref}/installing-stack-demo-self.html[Installing a self-managed Elastic Stack].

#### Import the Elasticsearch GPG Key

We sign all of our packages with the Elasticsearch Signing Key (PGP key
[D88E42B4](https://pgp.mit.edu/pks/lookup?op=vindex&search=0xD27D666CD88E42B4),
available from https://pgp.mit.edu) with fingerprint:

    4609 5ACC 8548 582C 1A26 99A9 D27D 666C D88E 42B4

Download and install the public signing key:

```sh
rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch
```

#### Installing from the RPM repository

**Warning:** Version {version} of Elasticsearch has not yet been released.

Create a file called `elasticsearch.repo` in the `/etc/yum.repos.d/` directory
for RedHat based distributions, or in the `/etc/zypp/repos.d/` directory for
OpenSuSE based distributions, containing:

```
[elasticsearch]
name=Elasticsearch repository for {major-version} packages
baseurl=https://artifacts.elastic.co/packages/{major-version}/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=0
autorefresh=1
type=rpm-md
```

```
[elasticsearch]
name=Elasticsearch repository for {major-version} packages
baseurl=https://artifacts.elastic.co/packages/{major-version}-prerelease/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=0
autorefresh=1
type=rpm-md
```

And your repository is ready for use. You can now install Elasticsearch with one of the following commands:

```sh
sudo yum install --enablerepo=elasticsearch elasticsearch <1>
sudo dnf install --enablerepo=elasticsearch elasticsearch <2>
sudo zypper modifyrepo --enable elasticsearch && \
  sudo zypper install elasticsearch; \
  sudo zypper modifyrepo --disable elasticsearch <3>
```
<1> Use `yum` on CentOS and older Red Hat based distributions.
<2> Use `dnf` on Fedora and other newer Red Hat distributions.
<3> Use `zypper` on OpenSUSE based distributions

**Note:** The configured repository is disabled by default. This eliminates the possibility of accidentally
upgrading `elasticsearch` when upgrading the rest of the system. Each install or upgrade command
must explicitly enable the repository as indicated in the sample commands above.

#### Download and install the RPM manually

**Warning:** Version {version} of Elasticsearch has not yet been released.

The RPM for Elasticsearch v{version} can be downloaded from the website and installed as follows:

```
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-{version}-x86_64.rpm
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-{version}-x86_64.rpm.sha512
shasum -a 512 -c elasticsearch-{version}-x86_64.rpm.sha512 <1>
sudo rpm --install elasticsearch-{version}-x86_64.rpm
```
<1> Compares the SHA of the downloaded RPM and the published checksum, which should output
    `elasticsearch-{version}-x86_64.rpm: OK`.

**Note:** On systemd-based distributions, the installation scripts will attempt to set kernel parameters (e.g.,
`vm.max_map_count`); you can skip this by masking the systemd-sysctl.service unit.

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

:include-xpack!: true

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

The RPM also has a system configuration file (`/etc/sysconfig/elasticsearch`),
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

#### Directory layout of RPM

The RPM places config files, logs, and the data directory in the appropriate
locations for an RPM-based system:

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
  | /etc/sysconfig/elasticsearch
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
    in `/etc/sysconfig/elasticsearch`.
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
