<!-- Converted from mongotop/mongotop-behavior.txt (reStructuredText). Includes are inlined. -->

# mongotop Behavior, Access, and Usage

   

## Behavior

### Polling

The `mongotop` program uses the `top`
command to collect data. However, while `top` returns cumulative
usage statistics, `mongotop` resets the usage statistics for 
each polling interval.

### FIPS

`mongotop` automatically creates FIPS-compliant
connections to a `mongod`/`mongos` that is
configured to use FIPS mode.

## Required Access

In order to connect to a `mongod` that enforces
authorization, the connecting user must have the
`serverStatus` and `top` privileges.

The built-in role `clusterMonitor` provides these privileges.

## Limitations

### Atlas Infinite

`mongotop` has the following limitations when run against an
Atlas Infinite Database cluster:

- Running `mongotop` with the `--locks` option against an
  Atlas Infinite Database cluster returns an error instead
  of usage statistics.
- Running `mongotop` without the `--locks` option against an
  Atlas Infinite Database cluster continues to work, but the
  output may have incomplete information.

## Learn More

- mongotop
- mongotop-compatibility-and-installation
- mongotop-examples
