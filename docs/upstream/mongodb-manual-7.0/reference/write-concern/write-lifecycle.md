<!-- Converted from reference/write-concern/write-lifecycle.txt (reStructuredText). Includes are inlined. -->

# Write Lifecycle Diagrams

These diagrams show the lifecycle of a `findAndModify`
operation on primary and secondary replica set members. The lifecycles
of other write commands are similar, but the number of resulting oplog
entries may vary.

## Write Lifecycle on a Primary Member

(Figure: /images/write-lifecycle/write-lifecycle-primary-7-0.png)

## Write Lifecycle on a Secondary Member

(Figure: /images/write-lifecycle/write-lifecycle-secondary-7-0.png)
