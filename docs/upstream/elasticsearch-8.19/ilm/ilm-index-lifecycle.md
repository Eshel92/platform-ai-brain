<!-- Converted from ilm/ilm-index-lifecycle.asciidoc (AsciiDoc). Includes are inlined. -->

### Index lifecycle

ILM defines five index lifecycle _phases_:

* **Hot**: The index is actively being updated and queried.
* **Warm**: The index is no longer being updated but is still being queried.
* **Cold**: The index is no longer being updated and is queried infrequently. The information still
needs to be searchable, but it's okay if those queries are slower.
* **Frozen**: The index is no longer being updated and is queried rarely. The information still
needs to be searchable, but it's okay if those queries are extremely slow.
* **Delete**: The index is no longer needed and can safely be removed.

An index's _lifecycle policy_ specifies which phases
are applicable, what actions are performed in each phase,
and when it transitions between phases.

You can manually apply a lifecycle policy when you create an index.
For time series indices, you need to associate the lifecycle policy with
the index template used to create new indices in the series.
When an index rolls over, a manually-applied policy isn't automatically applied to the new index.

If you use Elasticsearch's security features, ILM performs operations as the user
who last updated the policy. ILM only has the
roles assigned to the user at the time of the last policy
update.

### Phase transitions

ILM moves indices through the lifecycle according to their age.
To control the timing of these transitions, you set a _minimum age_ for each phase. For an index to
move to the next phase, all actions in the current phase must be complete and the index must be
older than the minimum age of the next phase. Configured minimum ages must increase between
subsequent phases, for example, a "warm" phase with a minimum age of 10 days can only be followed by
a "cold" phase with a minimum age either unset, or >= 10 days.

The minimum age defaults to zero, which causes ILM to move indices to the next phase
as soon as all actions in the current phase complete.

**Note:**
If an index has been rolled over, then the `min_age` value is relative to the time 
the index was rolled over, not the index creation time. Learn more.

If an index has unallocated shards and the cluster health status is yellow,
the index can still transition to the next phase according to its index lifecycle management policy.
However, because Elasticsearch can only perform certain clean up tasks on a green
cluster, there might be unexpected side effects.

To avoid increased disk usage and reliability issues,
address any cluster health problems in a timely fashion.

### Phase execution

ILM controls the order in which the actions in a phase are executed and
what _steps_ are executed to perform the necessary index operations for each action.

When an index enters a phase, ILM caches the phase definition in the index metadata.
This ensures that policy updates don't put the index into a state where it can never exit the phase.
If changes can be safely applied, ILM updates the cached phase definition.
If they cannot, phase execution continues using the cached definition.

ILM runs periodically, checks to see if an index meets policy criteria,
and executes whatever steps are needed.
To avoid race conditions, ILM might need to run more than once to execute all of the steps
required to complete an action.
For example, if ILM determines that an index has met the rollover criteria,
it begins executing the steps required to complete the rollover action.
If it reaches a point where it is not safe to advance to the next step, execution stops.
The next time ILM runs, ILM picks up execution where it left off.
This means that even if `indices.lifecycle.poll_interval` is set to 10 minutes and an index meets
the rollover criteria, it could be 20 minutes before the rollover is complete.

### Phase actions

ILM supports the following actions in each phase. ILM executes the
actions in the order listed.

* Hot
  - Set Priority
  - Unfollow
  - Rollover
  - Read-Only
  - Downsample
  - Shrink
  - Force Merge
  - Searchable Snapshot
* Warm
  - Set Priority
  - Unfollow
  - Read-Only
  - Downsample
  - Allocate
  - Migrate
  - Shrink
  - Force Merge
* Cold
  - Set Priority
  - Unfollow
  - Read-Only
  - Downsample
  - Searchable Snapshot
  - Allocate
  - Migrate
* Frozen
  - Unfollow
  - Searchable Snapshot
* Delete
  - Wait For Snapshot
  - Delete
