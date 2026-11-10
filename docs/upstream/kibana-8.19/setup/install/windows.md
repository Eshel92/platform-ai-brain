<!-- Converted from setup/install/windows.asciidoc (AsciiDoc). Includes are inlined. -->

### Install Kibana on Windows

Kibana can be installed on Windows using the `.zip` package.

This package contains both free and subscription features.
Start a 30-day trial to try out all of the features.

The latest stable version of Kibana can be found on the
link:/downloads/kibana[Download Kibana] page.
Other versions can be found on the
link:/downloads/past-releases[Past Releases page].

#### Download and install the `.zip` package

Version {version} of Kibana has not yet been released.

Download the `.zip` windows archive for Kibana v{version} from
https://artifacts.elastic.co/downloads/kibana/kibana-{version}-windows-x86_64.zip

Unzip it with your favourite unzip tool. This will create a folder called
kibana-{version}-windows-x86_64, which we will refer to as `$KIBANA_HOME`. In a
terminal window, `CD` to the `$KIBANA_HOME` directory, for instance:

```
CD c:\kibana-{version}-windows-x86_64
```

(See `setup/install/start-es-and-enroll.md`)
(See `setup/install/windows-running.md`)

#### Configure Kibana via the config file

Kibana loads its configuration from the `$KIBANA_HOME/config/kibana.yml`
file by default.  The format of this config file is explained in
[Configuring Kibana](https://www.elastic.co/guide/en/kibana/8.19/settings.html).

#### Directory layout of `.zip` archive

The `.zip` package is entirely self-contained. All files and directories are,
by default, contained within `$KIBANA_HOME` -- the directory created when
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
 d|

| bin
  | Binary scripts including `kibana` to start the Kibana server
    and `kibana-plugin` to install plugins
  | $KIBANA_HOME\bin
 d|

| config
  | Configuration files including `kibana.yml`
  | $KIBANA_HOME\config
  | KBN_PATH_CONF
 d|

| data
  | The location of the data files written to disk by Kibana and its plugins
  | $KIBANA_HOME\data
 d|

| plugins
  | Plugin files location. Each plugin will be contained in a subdirectory.
  | $KIBANA_HOME\plugins
 d|

|=======================================================================
