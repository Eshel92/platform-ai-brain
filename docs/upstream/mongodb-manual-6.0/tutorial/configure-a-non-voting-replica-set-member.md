<!-- Converted from tutorial/configure-a-non-voting-replica-set-member.txt (reStructuredText). Includes are inlined. -->

# Configure a Non-Voting Self-Managed Replica Set Member

Non-voting members allow you to add additional members for read
distribution beyond the maximum seven voting members.

To configure a member as non-voting, use the
`replSetReconfig` command *or* its
`mongosh` helper method `rs.reconfig()` to set its
`members[n].votes` and `members[n].priority` values to
`0`. Non-voting replica set members *must* have a 
`priority` of `0`.

**Note:**

Replica reconfiguration can add or remove no more than *one* voting replica 
set member at a time. To modify the votes of multiple members, issue a series 
of `replSetReconfig` or `rs.reconfig()` operations to
modify one member at a time. See
replSetReconfig-cmd-single-node for more information.

## Procedure

The following procedure converts configures a single secondary
replica set member to be non-voting. To convert the primary
member to be non-voting, you must first successfully step the primary
down using `replSetStepDown` or its shell helper
`rs.stepDown()` before performing this procedure.

\1) Connect to the Replica Set Primary
   Connect `mongosh` to the replica set primary:

   ```bash
   mongosh --host "<hostname>:<port>"
   ```

   Replace the `<hostname>` and `<port>` with the hostname and 
   port of the replica set primary. Include any other parameters 
   required for your deployment. 

\2) Retrieve the Replica Configuration
   Issue the `rs.conf()` method in the shell and assign the 
   result to a variable `cfg`:

   ```javascript
   cfg = rs.conf();
   ```

   The returned document contains a 
   `members` array, where each element in the array contains 
   the configuration for a single replica set member.

\3) Configure the Member to be Non-Voting
   For the replica member to change to be non-voting, 
   set its `votes` and
   `priority` to `0`.

   ```javascript
   cfg.members[n].votes = 0;
   cfg.members[n].priority = 0;
   ```

   Replace `n` with the array index position of the member 
   to modify. The `members` array is *zero-indexed*, 
   where the first element in the array has an index position of 
   `0`. 

   The array index position of a member in the 
   `members` array is *distinct* from the 
   `members[n]._id` of a specific member. Do *not* 
   use the `_id` to reference the array 
   index position of any any member in `members`.

\4) Reconfigure the Replica Set with the New Configuration
   Use `rs.reconfig()` method to reconfigure the replica set
   with the updated replica set configuration document.

   ```javascript
   rs.reconfig(cfg);
   ```

**Warning:**

- The `rs.reconfig()` shell method can force the current
  primary to step down, which causes an election. When the primary steps down, the
  `mongod` closes all client connections. While this
  typically takes 10-20 seconds, try to make these changes during
  scheduled maintenance periods.

- .. include:: /includes/warning-mixed-version-rs-config.rst

## Related Documents

- `members[n].votes`

- Replica Set Reconfiguration

- /core/replica-set-elections
