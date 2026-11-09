<!-- Converted from release-notes/dbtools-100.7.0-changelog.txt (reStructuredText). Includes are inlined. -->

# Database Tools 100.7.0 Changelogs

## 100.7.5 Changelog

*Released 2023-08-07*

This version updates Go to 1.19.12. This release of Go includes a security fix 
to the crypto/tls package.

This version no longer supports the PowerPC Ubuntu 18.04 platform.

### Task

* TOOLS-3349 - Add integration testing for mongodump/restore on 
  config db (and other special case dbs)

### Release

* TOOLS-3365 - Release Database Tools 100.7.5 with golang 1.19.12

## 100.7.4 Changelog

*Released 2023-07-21*

This release fixes issues with mongorestore that ommitted all namespaces 
containing "admin" when restoring to an Atlas Proxy Cluster. This release 
also fixes an issue with mongodump where the process failed against clusters 
using Atlas Online Archive.

### Bug

* TOOLS-3338 - Mongorestore to Atlas Proxy fails for any collection 
  containing "admin"
* TOOLS-3344 - Mongodump does not work with Atlas Data Federation.

## 100.7.3 Changelog

*Released 2023-06-26*

This release fixes an issue introduced in 100.7.1 where specifying 
`mongodump --db=confg` would not dump the entire config collection.

### Bug

- TOOLS-3324 Fix failure to dump needed sharded collections 
  from config database

### Task

- TOOLS-3319 Change mongorestore so that it works with atlas proxy 
  backup tests

## 100.7.2 Changelog

*Released 2023-05-30*

This release fixes an issue with installing Database Tools on RHEL AArch64 architecture. 

### Bug

- TOOLS-3309 Fix release issue on RHEL AArch64 architecture

## 100.7.1 Changelog

*Released 2023-05-24*

This release fixes a few bugs and adds downloads for the following platforms:

- macOS 11 on ARM
- RedHat Enterprise Linux 9 (x86 and ARM)
- Amazon Linux 2023 (x86 and ARM)

The tools were compiled with Go 1.19.9.

### Bug

- TOOLS-2598 Tools improperly parse multi-certs inside client certificate file
- TOOLS-3203 mongodump fails because it can’t query system.sharding_ddl_coordinators collection
- TOOLS-3273 Validation added in 100.7.0 prevents Atlas proxy from running mongodump
- TOOLS-3279 Test suite segfaults in some failure cases

### Task

- TOOLS-2722 Add MacOS 11.0 ARM to Tools
- TOOLS-3052 Add Amazon Linux 2023 ARM to Tools
- TOOLS-3054 Add RHEL9 ARM to Tools
- TOOLS-3062 Add Amazon Linux 2023 to Tools
- TOOLS-3276 Skip columnstore indexes tests in mongodump and mongorestore if error is NotImplemented

## 100.7.0 Changelog

*Released 2023-03-01*

This release adds tests against MongoDB 6.3. Highlights include:

- New tests for [Column Store Indexes](https://www.mongodb.com/products/column-store-indexes).

- Updating the minimum Go version to 1.19.

- Fixing a bug that caused the Tools to ignore a password supplied via a
  prompt.

- Several build failures are also fixed.

### Bug

- TOOLS-3243 Tools produce error about missing password after prompting for a password

### Epic

- TOOLS-3235 Tools 6.3 Support

### Task

- TOOLS-3169 Upgrade Go to 1.19
- TOOLS-3202 Fix legacy-jstests failure with latest Server
  (6.1)
- TOOLS-3208 Investigate test failures in HEAD and make more
  tickets as needed
- TOOLS-3229 Ignore admin database in dump/restore for
  atlasProxy
- TOOLS-3241 Fix flaky TestFailDuringResharding test
- TOOLS-3247 Remove mongo-tools support for ZAP PPC64LE Ubuntu
  16.04
- TOOLS-3248 Fix TestRestoreTimeseriesCollections for server
  6.3+
- TOOLS-3249 Remove mongo-tools support for server version 3.4
  on MacOS
- TOOLS-3250 Fix aws-auth task failures
- TOOLS-3251 Update common.yml to run tests with 6.3
- TOOLS-3252 Test support for Columnstore Indexes
- TOOLS-3255 Fix qa-tests-3.4
- TOOLS-3256 Make the push tasks only run on git tags
- TOOLS-3257 Override deprecated mongo shell functions to fix
  qa-tests-latest
- TOOLS-3259 Remove 6.3 tests on `ZAP s390x RHEL 7.2` and
  `ZAP PPC64LE RHEL 8.1`
- TOOLS-3260 Fix qa-tests on Debian 11
