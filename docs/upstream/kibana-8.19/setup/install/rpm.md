<!-- Converted from setup/install/rpm.asciidoc (AsciiDoc). Includes are inlined. -->

### Install Kibana with RPM

The RPM for Kibana can be downloaded from our website
or from our RPM repository. It can be used to install
Kibana on any RPM-based system such as OpenSuSE, SLES, Red Hat,
and Oracle Enterprise.

**Note:** RPM install is not supported on distributions with old versions of RPM,
such as SLES 11. Refer to targz instead.

This package contains both free and subscription features.
Start a 30-day trial to try out all of the features.

The latest stable version of Kibana can be found on the
link:/downloads/kibana[Download Kibana] page. Other versions can
be found on the link:/downloads/past-releases[Past Releases page].

**Tip:** For a step-by-step example of setting up the Elastic Stack on your own premises, try out our tutorial: {stack-ref}/installing-stack-demo-self.html[Installing a self-managed Elastic Stack].

#### Import the Elastic PGP key

We sign all of our packages with the Elastic Signing Key (PGP key
[D88E42B4](https://pgp.mit.edu/pks/lookup?op=vindex&search=0xD27D666CD88E42B4),
available from https://pgp.mit.edu) with fingerprint:

    4609 5ACC 8548 582C 1A26 99A9 D27D 666C D88E 42B4

Download and install the public signing key:

```sh
rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch
```

#### Installing from the RPM repository

Version {version} of Kibana has not yet been released.

Create a file called `kibana.repo` in the `/etc/yum.repos.d/` directory
for RedHat based distributions, or in the `/etc/zypp/repos.d/` directory for
OpenSuSE based distributions, containing:

```
[kibana-{major-version}]
name=Kibana repository for {major-version} packages
baseurl=https://artifacts.elastic.co/packages/{major-version}/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=1
autorefresh=1
type=rpm-md
```

```
[kibana-{major-version}]
name=Kibana repository for {major-version} packages
baseurl=https://artifacts.elastic.co/packages/{major-version}-prerelease/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=1
autorefresh=1
type=rpm-md
```

And your repository is ready for use. You can now install Kibana with one of the following commands:

```sh
sudo yum install kibana <1>
sudo dnf install kibana <2>
sudo zypper install kibana <3>
```
<1> Use `yum` on older Red Hat based distributions.
<2> Use `dnf` on Fedora and other newer Red Hat distributions.
<3> Use `zypper` on OpenSUSE based distributions

#### Download and install the RPM manually

Version {version} of Kibana has not yet been released.

The RPM for Kibana v{version} can be downloaded from the website and installed as follows:

```
wget https://artifacts.elastic.co/downloads/kibana/kibana-{version}-x86_64.rpm
wget https://artifacts.elastic.co/downloads/kibana/kibana-{version}-x86_64.rpm.sha512
shasum -a 512 -c kibana-{version}-x86_64.rpm.sha512 <1>
sudo rpm --install kibana-{version}-x86_64.rpm
```
<1> Compares the SHA of the downloaded RPM and the published checksum, which should output
    `kibana-{version}-x86_64.rpm: OK`.

#### Start Elasticsearch and generate an enrollment token for Kibana

When you start Elasticsearch for the first time, the following security configuration
occurs automatically:

* Authentication and authorization are enabled, and a password is generated for the `elastic` built-in superuser.
* Certificates and keys for TLS are generated for the transport and HTTP layer, and TLS is enabled and configured with these keys and certificates.

The password and certificate and keys are output to your terminal.

You can then generate an enrollment token for Kibana with the
[`elasticsearch-create-enrollment-token`](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/create-enrollment-token.html) tool:

```sh
bin/elasticsearch-create-enrollment-token -s kibana
```

Start Kibana and enter the enrollment token to securely connect Kibana with Elasticsearch.

(See `setup/install/systemd.md`)

#### Configure Kibana via the config file

Kibana loads its configuration from the `/etc/kibana/kibana.yml`
file by default.  The format of this config file is explained in
[Configuring Kibana](https://www.elastic.co/guide/en/kibana/8.19/settings.html).

#### Directory layout of RPM

The RPM places config files, logs, and the data directory in the appropriate
locations for an RPM-based system:

|=======================================================================
| Type | Description | Default Location | Setting
| home
  | Kibana home directory or `$KIBANA_HOME`
  | /usr/share/kibana
 d|

| bin
  | Binary scripts including `kibana` to start the Kibana server
    and `kibana-plugin` to install plugins
  | /usr/share/kibana/bin
 d|

| config
  | Configuration files including `kibana.yml`
  | /etc/kibana
  | KBN_PATH_CONF

| data
  | The location of the data files written to disk by Kibana and its plugins
  | /var/lib/kibana
  | path.data

| logs
  | Logs files location
  | /var/log/kibana
  | Logging configuration

| plugins
  | Plugin files location. Each plugin will be contained in a subdirectory.
  | /usr/share/kibana/plugins
 d|

|=======================================================================
