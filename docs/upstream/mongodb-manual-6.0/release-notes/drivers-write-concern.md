<!-- Converted from release-notes/drivers-write-concern.txt (reStructuredText). Includes are inlined. -->

:orphan:

# Default Write Concern Change

These release notes outline a change to all driver interfaces released
in November 2012. See release notes for specific drivers for
additional information.

## Changes

As of the releases listed below, there are two major changes to all
drivers:

#. All drivers will add a new top-level connection class that will
   increase consistency for all MongoDB client interfaces.

   This change is non-backward breaking: existing connection classes
   will remain in all drivers for a time, and will continue to operate
   as expected. However, those previous connection classes are now
   deprecated as of these releases, and will eventually be removed
   from the driver interfaces.

   The new top-level connection class is named `MongoClient`, or
   similar depending on how host languages handle namespacing.

#. The default write concern on the new `MongoClient` class will be
   to acknowledge all write operations [#without-arguments]_. This
   will allow your application to receive acknowledgment of all write
   operations.

   See the documentation of Write Concern for
   more information about write concern in MongoDB.

   Please migrate to the new `MongoClient` class expeditiously.

## Releases

The following driver releases will include the changes outlined in
write-concern-change-notes. See each driver's release notes for
a full account of each release as well as other related
driver-specific changes.

- C#, version 1.7
- Java, version 2.10.0
- Node.js, version 1.2
- Perl, version 0.501.1
- Legacy PHP, version 1.4
- Python, version 2.4
- Ruby, version 1.8
