<!-- Part 3 of 7 of reference/configuration-options.md (split because the page is big). -->

### `processManagement` Options

```yaml
processManagement:
   fork: <boolean>
   pidFilePath: <string>
   timeZoneInfo: <string>
```

**`processManagement.fork`**

*Type*: boolean

*Default*: false

Enable a daemon mode that runs the `mongos` or
`mongod` process in the background. By default 
`mongos` or `mongod` does not run as a daemon.
To use `mongos` or `mongod` as a daemon, set 
`processManagement.fork` or use a controlling process that 
handles the daemonization process (for example, `systemd`).

The `processManagement.fork` option is not supported on Windows.

The Linux package init scripts do not expect `processManagement.fork` to change from the
defaults. If you use the Linux packages and change `processManagement.fork`, you must
use your own init scripts and disable the built-in scripts.

   

**`processManagement.pidFilePath`**

*Type*: string

Specifies a file location to store the process ID (PID) of the `mongos` or `mongod`
process. The user running the `mongod` or `mongos`
process must be able to write to this path. If the `processManagement.pidFilePath` option is not
specified, the process does not create a PID file. This option is generally
only useful in combination with the `processManagement.fork` setting.

**Note:** Linux

On Linux, PID file management is generally the responsibility of
your distro's init system: usually a service file in the `/etc/init.d`
directory, or a systemd unit file registered with `systemctl`. Only
use the `processManagement.pidFilePath` option if you are not using one of these init
systems. For more information, please see the respective
Installation Guide for your operating system.

**Note:** macOS

On macOS, PID file management is generally handled by `brew`. Only use
the `processManagement.pidFilePath` option if you are not using `brew` on your macOS system. 
For more information, please see the respective
Installation Guide for your operating system.

**`processManagement.timeZoneInfo`**

*Type*: string

The full path from which to load the time zone database. If this option
is not provided, then MongoDB uses its built-in time zone database.

The configuration file included with Linux and macOS packages sets the
time zone database path to `/usr/share/zoneinfo` by default.

The built-in time zone database is a copy of the [Olson/IANA time zone database](https://www.iana.org/time-zones). It is updated along with
MongoDB releases, but the time zone database release cycle
differs from the MongoDB release cycle. The most recent release of
the time zone database is available on our [download site](https://downloads.mongodb.org/olson_tz_db/timezonedb-latest.zip).

**Warning:**

MongoDB uses the third party [timelib](https://github.com/derickr/timelib) library to provide accurate
conversions between timezones. Due to a recent update, `timelib`
could create inaccurate time zone conversions in older versions of
MongoDB.

To explicitly link to the time zone database in versions of MongoDB
prior to 5.0, download the [time zone database](https://downloads.mongodb.org/olson_tz_db/timezonedb-latest.zip).
and use the `timeZoneInfo` parameter.
