<!-- Converted from setup/start-stop.asciidoc (AsciiDoc). Includes are inlined. -->

## Start and stop Kibana

The method for starting and stopping Kibana varies depending on how you installed
it.  If a password protected keystore is used, the environment variable
`KBN_KEYSTORE_PASSPHRASE_FILE` can be used to point to a file containing the password,
the environment variable `KEYSTORE_PASSWORD` can be defined, or you will be prompted
to enter to enter the password on startup,

### Archive packages (`.tar.gz`)

If you installed Kibana on Linux or Darwin with a `.tar.gz` package, you can
start and stop Kibana from the command line.

(See `setup/install/targz-running.md`)

### Archive packages (`.zip`)

If you installed Kibana on Windows with a `.zip` package, you can
stop and start Kibana from the command line.

(See `setup/install/windows-running.md`)

### Debian and RPM packages

(See `setup/install/systemd.md`)
