<!-- Converted from setup/install/targz.asciidoc (AsciiDoc). Includes are inlined. -->

### Install Kibana from archive on Linux or macOS

Kibana is provided for Linux and Darwin as a `.tar.gz` package. These packages
are the easiest formats to use when trying out Kibana.

This package contains both free and subscription features.
Start a 30-day trial to try out all of the features.

The latest stable version of Kibana can be found on the
link:/downloads/kibana[Download Kibana] page.
Other versions can be found on the
link:/downloads/past-releases[Past Releases page].

**Note:**
macOS is supported for development purposes only and is not covered under the support SLA for [production-supported operating systems](https://www.elastic.co/support/matrix#kibana). 

#### Download and install the Linux 64-bit package

Version {version} of Kibana has not yet been released.

The Linux archive for Kibana v{version} can be downloaded and installed as follows:

```
curl -O https://artifacts.elastic.co/downloads/kibana/kibana-{version}-linux-x86_64.tar.gz
curl https://artifacts.elastic.co/downloads/kibana/kibana-{version}-linux-x86_64.tar.gz.sha512 | shasum -a 512 -c - <1>
tar -xzf kibana-{version}-linux-x86_64.tar.gz
cd kibana-{version}/ <2>
```
<1> Compares the SHA of the downloaded `.tar.gz` archive and the published checksum, which should output
    `kibana-{version}-linux-x86_64.tar.gz: OK`.
<2> This directory is known as `$KIBANA_HOME`.

#### Download and install the Darwin package

**macOS Gatekeeper warnings**

**Important:**
Apple's rollout of stricter notarization requirements affected the notarization
of the {version} Kibana artifacts. If macOS displays a dialog when you
first run Kibana that interrupts it, you will need to take an action to allow it
to run.

To prevent Gatekeeper checks on the Kibana files, run the following command on the
downloaded `.tar.gz` archive or the directory to which was extracted:
```sh
xattr -d -r com.apple.quarantine <archive-or-directory>
```

Alternatively, you can add a security override if a Gatekeeper popup appears by
following the instructions in the _How to open an app that hasn’t been notarized
or is from an unidentified developer_ section of
[Safely open apps on your Mac](https://support.apple.com/en-us/HT202491).

Version {version} of Kibana has not yet been released.

The Darwin archive for Kibana v{version} can be downloaded and installed as follows:

```
curl -O https://artifacts.elastic.co/downloads/kibana/kibana-{version}-darwin-x86_64.tar.gz
curl https://artifacts.elastic.co/downloads/kibana/kibana-{version}-darwin-x86_64.tar.gz.sha512 | shasum -a 512 -c - <1>
tar -xzf kibana-{version}-darwin-x86_64.tar.gz
cd kibana-{version}/ <2>
```
<1> Compares the SHA of the downloaded `.tar.gz` archive and the published checksum, which should output
    `kibana-{version}-darwin-x86_64.tar.gz: OK`.
<2> This directory is known as `$KIBANA_HOME`.

(See `setup/install/start-es-and-enroll.md`)
(See `setup/install/targz-running.md`)

#### Configure Kibana via the config file

Kibana loads its configuration from the `$KIBANA_HOME/config/kibana.yml`
file by default.  The format of this config file is explained in
[Configuring Kibana](https://www.elastic.co/guide/en/kibana/8.19/settings.html).

#### Directory layout of `.tar.gz` archives

The `.tar.gz` packages are entirely self-contained. All files and directories
are, by default, contained within `$KIBANA_HOME` -- the directory created when
unpacking the archive.

This is very convenient because you don't have to create any directories to
start using Kibana, and uninstalling Kibana is as easy as removing the
`$KIBANA_HOME` directory.  However, it is advisable to change the default
locations of the config and data directories so that you do not delete
important data later on.

|=======================================================================
| Type | Description | Default Location | Setting
| home
  | Kibana home directory or `$KIBANA_HOME`
 d| Directory created by unpacking the archive
  |

| bin
  | Binary scripts including `kibana` to start the Kibana server
    and `kibana-plugin` to install plugins
  | $KIBANA_HOME\bin
 d|

| config
  | Configuration files including `kibana.yml`
  | $KIBANA_HOME\config
  | KBN_PATH_CONF

| data
  | The location of the data files written to disk by Kibana and its plugins
  | $KIBANA_HOME\data
 d|

| plugins
  | Plugin files location. Each plugin will be contained in a subdirectory.
  | $KIBANA_HOME\plugins
 d|

|=======================================================================
