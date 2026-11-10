<!-- Converted from setup/install.asciidoc (AsciiDoc). Includes are inlined. -->

## Install Kibana

### Kibana on Elastic Cloud

If you are using Elastic Cloud, you access Kibana with a single click. (You can {ess-trial}[sign up for a free trial] and start exploring data in minutes.)

### Install Kibana yourself

**Tip:** For a step-by-step example of setting up the Elastic Stack on your own premises, try out our tutorial: {stack-ref}/installing-stack-demo-self.html[Installing a self-managed Elastic Stack].

**Note:** Starting with version 6.0.0, Kibana only supports 64 bit operating systems.

Kibana is provided in the following package formats:

`tar.gz`/`zip`::

The `tar.gz` packages are provided for installation on Linux and Darwin and are
the easiest choice for getting started with Kibana.
The `zip` package is the only supported package for Windows.
targz or windows

`deb`::

The `deb` package is suitable for Debian, Ubuntu, and other Debian-based
systems.  Debian packages may be downloaded from the Elastic website or from
our Debian repository.
deb

`rpm`::

The `rpm` package is suitable for installation on Red Hat, SLES,
OpenSuSE and other RPM-based systems.  RPMs may be downloaded from the
Elastic website or from our RPM repository.
rpm

`docker`::

Images are available for running Kibana as a Docker container. They may be
downloaded from the Elastic Docker Registry.
Running Kibana on Docker

**Important:** If your Elasticsearch installation is protected by
[{stack-security-features}](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/elasticsearch-security.html) see
[Configuring security in Kibana](https://www.elastic.co/guide/en/kibana/8.19/using-kibana-with-security.html) for
additional setup instructions.

(See `setup/install/targz.md`)
(See `setup/install/windows.md`)
(See `setup/install/deb.md`)
(See `setup/install/rpm.md`)
(See `setup/docker.md`)
