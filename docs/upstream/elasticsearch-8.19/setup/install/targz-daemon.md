<!-- Converted from setup/install/targz-daemon.asciidoc (AsciiDoc). Includes are inlined. -->

#### Run as a daemon

To run Elasticsearch as a daemon, specify `-d` on the command line, and record
the process ID in a file using the `-p` option:

```sh
./bin/elasticsearch -d -p pid
```

If you have password-protected the Elasticsearch keystore, you will be prompted
to enter the keystore's password. See secure-settings for more
details.

Log messages can be found in the `$ES_HOME/logs/` directory.

To shut down Elasticsearch, kill the process ID recorded in the `pid` file:

```sh
pkill -F pid
```

**Note:** The Elasticsearch `.tar.gz` package does not include the `systemd` module. To
manage Elasticsearch as a service, use the Debian or RPM
package instead.
