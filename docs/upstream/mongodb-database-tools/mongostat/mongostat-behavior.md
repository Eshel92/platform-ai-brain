<!-- Converted from mongostat/mongostat-behavior.txt (reStructuredText). Includes are inlined. -->

# mongostat Behavior, Access, and Usage

   

## Behavior

### FIPS

`mongostat` automatically creates FIPS-compliant
connections to a `mongod`/`mongos` that is
configured to use FIPS mode.

## Required Access

In order to connect to a `mongod` that enforces authorization
with the `--auth` option, specify the
`--username` and `--password` options, and the connecting user must have the
`serverStatus` privilege action on the cluster resources.

**Important:**

Starting in MongoDB 8.0, to use `mongostat` to connect to a
sharded cluster, the user must also have the
`directShardOperations` role.

The built-in role `clusterMonitor` provides the
`serverStatus` privilege as well as other
privileges. To create a role with just the privilege to run
`mongostat`, see create-role-for-mongostat.

## Limitations

### Atlas Infinite

`mongostat` has the following limitations when run against an
Atlas Infinite Database cluster:

- `mongostat` does not report the storage engine correctly
  for an Atlas Infinite Database cluster.
- `mongostat` reports less information when run against an
  Atlas Infinite Database cluster. For example, `mongostat`
  reports no information about locks.

## Learn More

- mongostat
- mongostat-compatibility-and-installation
- mongostat-examples
