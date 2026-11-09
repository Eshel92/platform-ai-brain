<!-- Converted from reference/command/applyOps.txt (reStructuredText). Includes are inlined. -->

# applyOps

## Definition

**`applyOps`**

Applies specified oplog entries to a `mongod`
instance. The `applyOps` command is an internal
command.

## Compatibility

This command is available in deployments hosted in the following environments: 

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Behavior

**Warning:**

This command obtains a global write lock and will block other
operations until it has completed.

## Required Access

If the specified oplog entries contain
collection UUIDs, executing this command
requires both the `useUUID` and `forceUUID`
privileges on the cluster resource to which the oplog entries are
attempting to be written.
