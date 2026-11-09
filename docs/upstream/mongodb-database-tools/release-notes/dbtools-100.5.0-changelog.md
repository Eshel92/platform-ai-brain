<!-- Converted from release-notes/dbtools-100.5.0-changelog.txt (reStructuredText). Includes are inlined. -->

# Database Tools 100.5.0 Changelogs

## 100.5.4 Changelog

*Released 2022-07-19*

This release mostly consists of build failure fixes, support for new
platforms, and tests against server version 6.0. The new platforms are
Debian 11 on x86, Ubuntu 22.04 on x86 and ARM, and RHEL 8.3 on s390x.
The version of Go driver used by the tools has been updated to 1.10.0.

### Build Failure

- TOOLS-3100 - Fix native-cert-ssl-4.4 task failure in all
  build variants
- TOOLS-3101 - Fix failing aws-auth-6.0 and aws-auth-latest
  tasks
- TOOLS-3102 - Fix intermittent failures of qa-tests-{5.3, 6.0,
  latest} tasks
- TOOLS-3110 - Fix integration test failures with server 6.0+
- TOOLS-3111 - Fix intermittent legacy JS test task failure
- TOOLS-3122 - Fix SSL cert test(s) on RHEL 6.2
- TOOLS-3156 - Unable to publish to Ubuntu 22.04 repos

### Task

- TOOLS-3045 - Add tests for latest server release
- TOOLS-3051 - Release Tools with Debian 11
- TOOLS-3058 - Add Ubuntu 22.04 ARM to Tools
- TOOLS-3059 - Release Tools with Ubuntu 22.04 ARM
- TOOLS-3060 - Add Ubuntu 22.04 x86 to Tools
- TOOLS-3061 - Release Tools with Ubuntu 22.04 x86
- TOOLS-3103 - Add tests for 6.0 to evergreen
- TOOLS-3113 - Test secondary indexes on timeseries collections
- TOOLS-3130 - Add 6.0 to list of linux repos we release to
- TOOLS-3149 - Update the Go Driver to 1.10.0
- TOOLS-3155 - Repo config for RHEL 8.3 on s390x is incorrect
- TOOLS-2939 - Add Enterprise RHEL 8 zSeries

## 100.5.3 Changelog

*Released 2022-06-14*

This release contains a number of bug fixes and changes. Highlights 
include support for clustered collections in mongorestore, updating 
our Go version from 1.16.7 to 1.17.8 to address CVEs, and supported 
platform updates.

### Build Failure

- TOOLS-3119 - All builds are failing on RHEL6.2
- TOOLS-3126 - The unit tests for options processing segfault on macOS
- TOOLS-3127 - The dist CI task is failing on Windows

### Bug

- TOOLS-2958 - An index deletion or collMod in the oplog can be applied to the wrong index
- TOOLS-2961 - The RHEL82 ARM release does not use the correct architecture
- TOOLS-2963 - Tools are not prompting for a password in many cases where they should
- TOOLS-3044 - The zip file for tools on Windows contains invalid paths
- TOOLS-3071- Tools installed by RPM packages to /usr/bin are owned by mongod:mongod instead of root:root

### Task

- TOOLS-2906 - Update Evergreen config to use new merge key format
- TOOLS-3001 - bsondump should allow documents up to the internal max bson size (16mb + 16kb)
- TOOLS-3028 - Remove evergreen batchtimes from ZAP
- TOOLS-3049 - Update the Go version used to build mongo-tools to address several critical and high CVEs
- TOOLS-3050 - Add Debian 11 to platforms we publish tools packages for
- TOOLS-3095 - Remove Ubuntu 14.04 from CI and release platforms
- TOOLS-3104 - Add tests for 5.3 to evergreen
- TOOLS-3105 - Pin Go driver to version 1.9.1
- TOOLS-3106 - Remove tests for 5.1 and 5.2 for most platforms
- TOOLS-3108 - Update mongorestore to support clustered indexes
- TOOLS-3116 - Change Windows build to run on windows-vsCurrent-large

## 100.5.2 Changelog

*Released 2022-02-03*

This release fixes an issue where inserting large documents with
mongorestore or mongoimport
could cause extremely high memory usage (TOOLS-2875). It also
fixes a few minor bugs.

### Bug

- TOOLS-2745 Tools don't support setting `retryWrites=false`
  in URI parameter

- TOOLS-2983 Some error messages for conflicting URI/CLI
  arguments are misleading

### Task

- TOOLS-2875 Limit the `BufferedBulkInserter` batch size by
  bytes 

## 100.5.1 Changelog

*Released 2021-10-12*

This release fixes an issue where certain `config` collections which
should generally be ignored were included by `mongodump`
and `mongorestore`. This release also ensures that any
operations on these collections will not be applied during the oplog
replay phase of `mongorestore`.

### Bug

- TOOLS-2952 Filter config collections in dump/restore 

## 100.5.0 Changelog

*Released 2021-08-10*

This release includes support for the loadbalanced URI option, which
provides compatibility with MongoDB Atlas Serverless.

### Build Failure

- TOOLS-2938 Re-add Ubuntu 16.04 PowerPC platform

### Release

- TOOLS-2880 Release Database Tools 100.5.0

### Bug

- TOOLS-2863 cs.AuthMechanismProperties is not initialized
  when mechanism set by --authenticationMechanism

### New Feature

- TOOLS-2937 Set loadbalanced option in 
  db.configureClient()

### Task

- TOOLS-2932 Upgrade to Go Driver 1.7.1
