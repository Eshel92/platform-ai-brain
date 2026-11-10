<!-- Converted from setup/install/targz.asciidoc (AsciiDoc). Includes are inlined. -->

### Install Elasticsearch from archive on Linux or MacOS

Elasticsearch is available as a `.tar.gz` archive for Linux and MacOS.

This package contains both free and subscription features.
Start a 30-day trial to try out all of the features.

The latest stable version of Elasticsearch can be found on the
link:/downloads/elasticsearch[Download Elasticsearch] page.
Other versions can be found on the
link:/downloads/past-releases[Past Releases page].

**Note:** Elasticsearch includes a bundled version of [OpenJDK](https://openjdk.java.net)
from the JDK maintainers (GPLv2+CE). To use your own version of Java,
see the JVM version requirements

#### Download and install archive for Linux

**Warning:** Version {version} of Elasticsearch has not yet been released.

The Linux archive for Elasticsearch v{version} can be downloaded and installed as follows:

```
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-{version}-linux-x86_64.tar.gz
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-{version}-linux-x86_64.tar.gz.sha512
shasum -a 512 -c elasticsearch-{version}-linux-x86_64.tar.gz.sha512 <1>
tar -xzf elasticsearch-{version}-linux-x86_64.tar.gz
cd elasticsearch-{version}/ <2>
```
<1> Compares the SHA of the downloaded `.tar.gz` archive and the published checksum, which should output
    `elasticsearch-{version}-linux-x86_64.tar.gz: OK`.
<2> This directory is known as `$ES_HOME`.

#### Download and install archive for MacOS

**Warning:** Version {version} of Elasticsearch has not yet been released.

**macOS Gatekeeper warnings**

**Important:**
Apple's rollout of stricter notarization requirements affected the notarization of the {version} Elasticsearch artifacts. If macOS displays a dialog when you first run Elasticsearch that interrupts it, then you need to take an action to allow it to run.

To prevent Gatekeeper checks on the Elasticsearch files, run the following command on the downloaded .tar.gz archive or the directory to which was extracted:

```sh
xattr -d -r com.apple.quarantine <archive-or-directory>
```

Alternatively, you can add a security override by following the instructions in the _If you want to open an app that hasn't been notarized or is from an unidentified developer_ section of [Safely open apps on your Mac](https://support.apple.com/en-us/HT202491).

The MacOS archive for Elasticsearch v{version} can be downloaded and installed as follows:

```
curl -O https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-{version}-darwin-x86_64.tar.gz
curl https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-{version}-darwin-x86_64.tar.gz.sha512 | shasum -a 512 -c - <1>
tar -xzf elasticsearch-{version}-darwin-x86_64.tar.gz
cd elasticsearch-{version}/ <2>
```

<1> Compares the SHA of the downloaded `.tar.gz` archive and the published checksum, which should output
    `elasticsearch-{version}-darwin-x86_64.tar.gz: OK`.
<2> This directory is known as `$ES_HOME`.

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

(See `setup/install/targz-start.md`)

(See `setup/install/check-running.md`)
Log printing to `stdout` can be disabled using the `-q` or `--quiet`
option on the command line.

(See `setup/install/targz-daemon.md`)

#### Configure Elasticsearch on the command line

Elasticsearch loads its configuration from the `$ES_HOME/config/elasticsearch.yml`
file by default. The format of this config file is explained in
settings.

Any settings that can be specified in the config file can also be specified on
the command line, using the `-E` syntax as follows:

```sh
./bin/elasticsearch -d -Ecluster.name=my_cluster -Enode.name=node_1
```

**Tip:** Typically, any cluster-wide settings (like `cluster.name`) should be
added to the `elasticsearch.yml` config file, while any node-specific settings
such as `node.name` could be specified on the command line.

(See `setup/install/connect-clients.md`)

#### Directory layout of archives

The archive distributions are entirely self-contained. All files and
directories are, by default, contained within `$ES_HOME` -- the directory
created when unpacking the archive.

This is very convenient because you don't have to create any directories to
start using Elasticsearch, and uninstalling Elasticsearch is as easy as
removing the `$ES_HOME` directory. However, it is advisable to change the
default locations of the config directory, the data directory, and the logs
directory so that you do not delete important data later on.

|=======================================================================
| Type | Description | Default Location | Setting
| home
  | Elasticsearch home directory or `$ES_HOME`
 d| Directory created by unpacking the archive
  |

| bin
  | Binary scripts including `elasticsearch` to start a node
    and `elasticsearch-plugin` to install plugins
  | $ES_HOME/bin
 d|

| conf
  | Configuration files including `elasticsearch.yml`
  | $ES_HOME/config
  | ES_PATH_CONF

| conf
  | Generated TLS keys and certificates for the transport and HTTP layer.
  | $ES_HOME/config/certs
 d|

| data
  | The location of the data files of each index / shard allocated
    on the node.
  | $ES_HOME/data
  | path.data

| logs
  | Log files location.
  | $ES_HOME/logs
  | path.logs

| plugins
  | Plugin files location. Each plugin will be contained in a subdirectory.
  | $ES_HOME/plugins
  |

| repo
  | Shared file system repository locations. Can hold multiple locations. A file system repository can be placed in to any subdirectory of any directory specified here.
 d| Not configured
  | path.repo

|=======================================================================

(See `setup/install/security-files-reference.md`)
(See `setup/install/next-steps.md`)
