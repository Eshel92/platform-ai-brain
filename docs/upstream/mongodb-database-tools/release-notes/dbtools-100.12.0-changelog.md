<!-- Converted from release-notes/dbtools-100.12.0-changelog.txt (reStructuredText). Includes are inlined. -->

# Database Tools 100.12.0 Changelogs

## 100.12.2 Changelog

*Released 2025-06-04*

This release fixes a mongorestore bug that caused namespaces that contain 
newlines to be silently excluded from restorations.

### Bug

- TOOLS-3822 - Mongorestore misses collection names with newlines

### Task

- TOOLS-3820 - Change use of the macOS service to only notarize releases

## 100.12.1 Changelog

*Released 2025-05-21*

This version includes security updates.

### Vulnerability

- TOOLS-3819 - Security Finding: Update package `net@v0.36.0`

### Release

- TOOLS-3889 - Release Database Tools 100.12.1

## 100.12.0 Changelog

*Released 2025-04-01*

This version adds support for MongoDB Server 8.1, along with security updates 
and bug fixes. 

### Vulnerability

- TOOLS-3787 - Security Finding: Update package `crypto`
- TOOLS-3793 - Security Finding: Update package `net`
- TOOLS-3797 - Security Finding: Update package `jwt`

### Release

- TOOLS-3714 - Release Database Tools 100.12.0

### Bug

- TOOLS-3540 - Timestamp(0,0) is not replicated properly in mongorestore
  and mongoimport
- TOOLS-3697 - Missing {_id: "hashed"} index after running mongorestore
- TOOLS-3708 - mongorestore incorrectly converts small negative float64
  index keys to 1 instead of -1
- 3727 - Mongodump/mongorestore should not automatically upgrade
  unversioned 2dsphere indexes

### Task

- TOOLS-3719 - Database fails if --restoreDBUsersAndRoles used on wrong
  target
- TOOLS-3745 - mongorestore does not strip the 'system.buckets' prefix 
  when restoring a timeseries collection from a BSON file 
- TOOLS-3762 - Switch to Silkbomb 2.0 /Kondukto
- TOOLS-3782 - Handle removal of `authSchema` document in system.version
  in server 8.1
