<!-- Converted from release-notes/dbtools-100.0.0-changelog.txt (reStructuredText). Includes are inlined. -->

# Database Tools 100.0.0 Changelogs

## 100.0.2 Changelog

This release contains several bugfixes. It also adds support for dumping
and restoring collections with long names since the 120 byte name limit
will be raised to 255 bytes in MongoDB version 4.4.

The full list of changes is below:

### Bug

- TOOLS-1785 Typo in mongodump help
- TOOLS-2495 Oplog replay can't handle entries > 16 MB
- TOOLS-2498 Nil pointer error mongodump
- TOOLS-2559 Error on uninstalling database-tools 99.0.1-1 RPM
- TOOLS-2575 mongorestore panic during convertLegacyIndexes from 4.4 mongodump
- TOOLS-2593 Fix special handling of $admin filenames

### Task

- TOOLS-2446 Add MMAPV1 testing to Tools tests
- TOOLS-2469 Accept multiple certs in CA
- TOOLS-2530 Mongorestore can restore from new mongodump format
- TOOLS-2537 Ignore config.system.indexBuilds namespace
- TOOLS-2544 Add 4.4 tests to Evergreen
- TOOLS-2551 Split release uploading into per-distro tasks
- TOOLS-2555 Support directConnection option
- TOOLS-2561 Sign mongodb-tools tarballs
- TOOLS-2605 Cut 100.0.2 release

## 100.0.1 Changelog

This release was a test of our new release infrastructure and contains
no changes from 100.0.0.

### Task

- TOOLS-2493 Cut tools 100.0.0 and 100.0.1 GA releases

## 100.0.0 Changelog

This is the first separate release of the Database Tools from the
Server. We decided to move to a separate release so we can ship new
features and bugfixes more frequently. The new separate release version
starts from `100.0.0` to make it clear the versioning is separate from
the Server. You can read more about this on the
[MongoDB blog](https://www.mongodb.com/blog/post/separating-database-tools-server).

This release contains bugfixes, some new command-line options, and
quality of life improvements. A full list can be found below, but here
are some highlights:

- There are no longer restrictions on using `--uri` with other
  connection options such as `--port` and `--password` as long as
  the URI and the explicit option don't provide conflicting information.
  Connection strings can now be specified as a positional argument
  without the `--uri` option.

- The new `--useArrayIndexFields` flag for `mongoimport`
  interprets natural numbers in fields as array indexes when importing
  csv or tsv files.

- The new `--convertLegacyIndexes` flag for `mongorestore`
  removes any invalid index options specified in the corresponding
  `mongodump` output, and rewrites any legacy index key values
  to use valid values.

- A new `delete` `mode` for
  `mongoimport`. With `--mode`
  `delete`, `mongoimport` deletes existing documents in the
  database that match a document in the import file.

### Build Failure

- TOOLS-2489 format-go task failing on master

### Bug

- TOOLS-1493 Tools crash running help when terminal width is low
- TOOLS-1786 mongodump does not create metadata.json file for views dumped as collections
- TOOLS-1826 mongorestore panic in archive mode when replay oplog failed
- TOOLS-1909 mongoimport does not report that it supports the decimal type
- TOOLS-2275 autoIndexId:false is not supported in 4.0
- TOOLS-2334 Skip system collections during oplog replay
- TOOLS-2336 Wrong deprecation error message printed when restoring from stdin
- TOOLS-2346 mongodump --archive to stdout corrupts archive when prompting for password
- TOOLS-2379 mongodump/mongorestore error if source database has an invalid index option
- TOOLS-2380 mongodump fails against hidden node with authentication enabled
- TOOLS-2381 Restore no socket timeout behavior
- TOOLS-2395 Incorrect message for oplog overflow
- TOOLS-2403 mongorestore hang while replaying last oplog failed in archive mode
- TOOLS-2422 admin.tempusers is not dropped by mongorestore
- TOOLS-2423 mongorestore does not drop admin.tempusers if it exists in the dump
- TOOLS-2455 mongorestore hangs on invalid archive
- TOOLS-2462 Password prompt does not work on windows
- TOOLS-2497 mongorestore may incorrectly validate index name length before calling createIndexes
- TOOLS-2513 Creating client options results in connection string validation error
- TOOLS-2520 Fix options parsing for SSL options
- TOOLS-2547 Installing database tools fails on rhel 7.0
- TOOLS-2548 Installing database tools fails on SLES 15

### New Feature

- TOOLS-1954 Support roundtrip of mongoexport array notation in mongoimport
- TOOLS-2268 Add remove mode to mongoimport
- TOOLS-2412 Strip unsupported legacy index options
- TOOLS-2430 mongorestore: in dotted index keys, replace "hashed" with "1"
- TOOLS-2459 Allow --uri to be used with other connection string options
- TOOLS-2460 A connection string can be set as a positional argument
- TOOLS-2521 Add support for the tlsDisableOCSPEndpointCheck URI option
- TOOLS-2529 Mongodump outputs new file format for long collection names

### Task

- TOOLS-2418 Remove mongoreplay from mongo-tools
- TOOLS-2421 Maintain test coverage after moving tools tests from server
- TOOLS-2438 Create MSI installer in dist task
- TOOLS-2439 Tools formula included in homebrew tap
- TOOLS-2440 Sign MSI installer
- TOOLS-2441 Update release process documentation
- TOOLS-2442 Automate release uploads
- TOOLS-2443 Generate tarball archive in dist task
- TOOLS-2444 Generate deb packages in dist task
- TOOLS-2449 Create sign task
- TOOLS-2464 Update platform support
- TOOLS-2470 Sign linux packages
- TOOLS-2471 Automate JSON download feed generation
- TOOLS-2472 Automate linux package publishing
- TOOLS-2473 Consolidate community and enterprise buildvariants
- TOOLS-2475 Manually verify tools release
- TOOLS-2480 Generate rpm packages in dist task
- TOOLS-2488 Update package naming and versioning
- TOOLS-2493 Cut tools 100.0.0 and 100.0.1 GA releases
- TOOLS-2506 Update maintainer in linux packages
- TOOLS-2523 Remove Ubuntu 12.04 and Debian 7.1 variants
- TOOLS-2536 ignoreUnknownIndexOptions option in the createIndexes command for servers >4.1.9
- TOOLS-2538 Move convertLegacyIndexKeys() from mongorestore to mongo-tools-common
- TOOLS-2539 Publish linux packages to curator with correct names
- TOOLS-2549 Push GA releases to server testing repo
- TOOLS-2550 Push GA releases to the 4.4 repo
- TOOLS-2551 Split release uploading into per-distro tasks
