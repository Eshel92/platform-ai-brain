<!-- Converted from administration/replica-set-member-configuration.txt (reStructuredText). Includes are inlined. -->

# Self-Managed Member Configuration Tutorials

The following tutorials provide information on configuring replica set
members to support specific operations, such as to provide dedicated
backups, to support reporting, or to act as a cold standby.

**Warning:**

Avoid reconfiguring replica sets that contain members of different
MongoDB versions as validation rules may differ across MongoDB versions.

/tutorial/adjust-replica-set-member-priority
   Change the precedence given to a replica set members in an
   election for primary.

/tutorial/configure-secondary-only-replica-set-member
   Make a secondary member ineligible for election as primary.

/tutorial/configure-a-hidden-replica-set-member
   Configure a secondary member to be invisible to applications in
   order to support significantly different usage, such as a
   dedicated backups.

/tutorial/configure-a-delayed-replica-set-member
   Configure a secondary member to keep a delayed copy of the data
   set in order to provide a rolling backup.

/tutorial/configure-a-non-voting-replica-set-member
   Create a secondary member that keeps a copy of the data set but
   does not vote in an election.

/tutorial/convert-secondary-into-arbiter
   Convert a secondary to an arbiter.
