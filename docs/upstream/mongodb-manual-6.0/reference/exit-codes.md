<!-- Converted from reference/exit-codes.txt (reStructuredText). Includes are inlined. -->

# Exit Codes and Statuses for a Self-Managed Deployment

MongoDB will return one of the following codes and statuses when
exiting. Use this guide to interpret logs and when troubleshooting
issues with `mongod` and `mongos` instances.

* - Code
  - Cause

* - .. error:: 0
  - Returned by MongoDB applications upon successful exit.

* - .. error:: 2
  - The specified options are in error or are incompatible
    with other options.

* - .. error:: 3
  - Returned by `mongod` if there is a mismatch
    between hostnames specified on the command line and in the
    `local.sources` collection, in master/slave mode.

* - .. error:: 4
  - The version of the database is different from the version
    supported by the `mongod` (or
    `mongod.exe`) instance.  The instance exits
    cleanly.

* - .. error:: 5
  - Returned by `mongos` if a problem is encountered
    during initialization.

* - .. error:: 12
  - Returned by the `mongod.exe` process on Windows
    when it receives a Control-C, Close, Break or Shutdown event.

* - .. error:: 14
  - Returned by MongoDB applications which encounter an
    unrecoverable error, an uncaught exception or uncaught signal.
    The system exits without performing a clean shutdown.

* - .. error:: 20
  - *Message:* `ERROR: wsastartup failed <reason>`

    Returned by MongoDB applications on Windows following an error
    in the WSAStartup function, used to initialize the networking
    subsystem.

    *Message:* `NT Service Error`

    Returned by MongoDB applications for Windows due to failures
    installing, starting or removing the NT Service for the
    application.

* - .. error:: 48
  - A newly started `mongod` or `mongos`
    could not start listening for incoming connections, due to an
    error.

* - .. error:: 61
  - Returned by the storage-node-watchdog if any of the 
    filesystems with monitored directories are unresponsive.

* - .. error:: 62
  - Returned by `mongod` if the datafiles in
    `--dbpath` are incompatible with the
    version of `mongod` currently running.

* - .. error:: 100
  - Returned by `mongod` when the process throws an
    uncaught exception.
