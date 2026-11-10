<!-- Converted from setup/install.asciidoc (AsciiDoc). Includes are inlined. -->

## Installing Elasticsearch

### Hosted Elasticsearch Service

Elastic Cloud offers all of the features of Elasticsearch, Kibana, and  Elastic’s Observability, {ents}, and Elastic Security solutions as a hosted service
available on AWS, GCP, and Azure.

To set up Elasticsearch in Elastic Cloud, sign up for a {ess-trial}[free Elastic Cloud trial].

### Self-managed Elasticsearch options

If you want to install and manage Elasticsearch yourself, you can:

* Run Elasticsearch using a Linux, MacOS, or Windows install package.
* Run Elasticsearch in a Docker container.
* Set up and manage Elasticsearch, Kibana, Elastic Agent, and the rest of the Elastic Stack on Kubernetes with {eck-ref}[Elastic Cloud on Kubernetes].

**Tip:** To try out Elasticsearch on your own machine, we recommend using Docker and running both Elasticsearch and Kibana. For more information, see Run Elasticsearch locally. Please note that this setup is *not suitable for production use*.

### Elasticsearch install packages

Elasticsearch is provided in the following package formats:

Linux and MacOS `tar.gz` archives::

The `tar.gz` archives are available for installation on any Linux distribution and MacOS.
targz

Windows `.zip` archive::

The `zip` archive is suitable for installation on Windows.
zip-windows

`deb`::

The `deb` package is suitable for Debian, Ubuntu, and other Debian-based
systems. Debian packages may be downloaded from the Elasticsearch website or
from our Debian repository.
deb

`rpm`::

The `rpm` package is suitable for installation on Red Hat, Centos, SLES,
OpenSuSE and other RPM-based systems. RPMs may be downloaded from the
Elasticsearch website or from our RPM repository.
rpm

**Tip:** For a step-by-step example of setting up the Elastic Stack on your own premises, try out our tutorial: {stack-ref}/installing-stack-demo-self.html[Installing a self-managed Elastic Stack].

### Elasticsearch container images

You can also run Elasticsearch inside a container image.

`docker`::

Docker container images may be downloaded from the Elastic Docker Registry.
[Install Elasticsearch with Docker](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/docker.html)

### Java (JVM) Version

Elasticsearch is built using Java, and includes a bundled version of [OpenJDK](https://openjdk.java.net) within each distribution. We strongly
recommend using the bundled JVM in all installations of Elasticsearch.

The bundled JVM is treated the same as any other dependency of Elasticsearch in terms of support and maintenance. This means that Elastic takes
responsibility for keeping it up to date, and reacts to security issues and bug reports as needed to address vulnerabilities and other bugs
in Elasticsearch. Elastic's support of the bundled JVM is subject to Elastic's [support policy](https://www.elastic.co/support_policy) and
[end-of-life schedule](https://www.elastic.co/support/eol) and is independent of the support policy and end-of-life schedule offered by the
original supplier of the JVM. Elastic does not support using the bundled JVM for purposes other than running Elasticsearch.

**Tip:** Elasticsearch uses only a subset of the features offered by the JVM. Bugs and security issues in the bundled JVM often relate to features that
Elasticsearch does not use. Such issues do not apply to Elasticsearch. Elastic analyzes reports of security vulnerabilities in all its dependencies, including
in the bundled JVM, and will issue an [Elastic Security Advisory](https://www.elastic.co/community/security) if such an advisory is needed.

If you decide to run Elasticsearch using a version of Java that is different from the bundled one, prefer to use the latest release of a
[LTS version of Java](https://www.oracle.com/technetwork/java/eol-135779.html) which is link:/support/matrix[listed in the support matrix].
Although such a configuration is supported, if you encounter a security issue or other bug in your chosen JVM then Elastic may not be able
to help unless the issue is also present in the bundled JVM. Instead, you must seek assistance directly from the supplier of your chosen
JVM. You must also take responsibility for reacting to security and bug announcements from the supplier of your chosen JVM. Elasticsearch may not
perform optimally if using a JVM other than the bundled one. Elasticsearch is closely coupled to certain OpenJDK-specific features, so it may not
work correctly with JVMs that are not OpenJDK. Elasticsearch will refuse to start if you attempt to use a known-bad JVM version.

To use your own version of Java, set the `ES_JAVA_HOME` environment variable to the path to your own JVM installation. The bundled JVM is
located within the `jdk` subdirectory of the Elasticsearch home directory. You may remove this directory if using your own JVM.

### JDK locale database

The locale database used by Elasticsearch, used to map from various date formats to
the underlying date storage format, depends on the version of the JDK
that Elasticsearch is running on. On JDK version 23 and above, Elasticsearch will use the
_CLDR_ database. On JDK version 22 and below, Elasticsearch will use the _COMPAT_
database. This may mean that the strings used for textual date formats,
and the output of custom week-date formats, may change when moving from
a previous JDK version to JDK 23 or above. For more information, see
custom date formats.

### JVM and Java agents

Don't use third-party Java agents that attach to the JVM. These agents
can reduce Elasticsearch performance, including freezing or crashing nodes.

(See `setup/install/targz.md`)
(See `setup/install/zip-windows.md`)
(See `setup/install/deb.md`)
(See `setup/install/rpm.md`)
(See `setup/install/docker.md`)
