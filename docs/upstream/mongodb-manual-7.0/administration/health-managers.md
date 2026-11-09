<!-- Converted from administration/health-managers.txt (reStructuredText). Includes are inlined. -->

# Configure Sharded Cluster Health with Health Managers

This document describes how to use Health Managers to monitor and manage sharded 
cluster health issues.

## Overview

A Health Manager runs health checks on a health manager facet
at a specified intensity level. Health Manager checks
run at specified time intervals. A Health Manager can be configured to 
move a failing mongos out of a cluster automatically. 
Progress Monitor ensures 
that Health Manager checks do not become stuck or unresponsive.

### Health Manager Facets

The following table shows the available Health Manager facets:

| Facet | What the Health Observer Checks |
|---|---|
| `configServer` | Cluster health issues related to connectivity to the config server. |
| `dns` | Cluster health issues related to DNS availability and functionality. |
| `ldap` | Cluster health issues related to LDAP availability and functionality. |

### Health Manager Intensity Levels

The following table shows the available Health Manager intensity levels:

| Intensity Level | Description |
|---|---|
| `critical` | The Health Manager on this facet is enabled and has the ability to move the failing mongos out of the cluster if an error occurs. The Health Manager waits the amount of time specified by `activeFaultDurationSecs` before stopping and moving the mongos out of the cluster automatically. |
| `non-critical` | The Health Manager on this facet is enabled and logs errors, but the mongos remains in the cluster if errors are encountered. |
| `off` | The Health Manager on this facet is disabled. The mongos does not perform any health checks on this facet. This is the default intensity level. |

## Active Fault Duration

When a failure is detected and the Health Manager intensity level
is set to `critical`, the Health Manager waits the amount of time specified by 
`activeFaultDurationSecs` before stopping and moving the 
mongos out of the cluster automatically.

## Progress Monitor

Progress Monitor runs tests 
to ensure that Health Manager checks do not become stuck or 
unresponsive. Progress Monitor runs these tests in intervals specified 
by `interval`. If a health check begins but does not complete within
the timeout given by `deadline`, Progress Monitor stops the 
mongos and removes it from the cluster.

### `progressMonitor` Fields

| Field | Description | Units |
|---|---|---|
| `interval` | How often to ensure Health Managers are not stuck or unresponsive. | Milliseconds |
| `deadline` | Timeout before automatically failing the mongos if a Health Manager check is not making progress. | Seconds |

## Examples

The following examples show how Health Managers can be configured. For
information on Health Manager parameters, see Health Manager Parameters.

### Intensity

For example, to set the `dns` Health Manager facet to the 
`critical` intensity level, issue the following at startup:

```bash
mongos --setParameter 'healthMonitoringIntensities={ values:[ { type:"dns", intensity: "critical"} ] }'
```

Or if using the `setParameter` command in a
`mongosh` session that is connected to a running
`mongos`:

```javascript
db.adminCommand( 
  {
      setParameter: 1, 
      healthMonitoringIntensities: { values: [ { type: "dns", intensity: "critical" } ] } } )
  }
)
```

Parameters set with `setParameter` do not persist across
restarts. See the setParameter page for details.

To make this setting persistent, set `healthMonitoringIntensities`
in your mongos config file using the
`setParameter` option as in the following example:

```yaml
setParameter:
   healthMonitoringIntensities: "{ values:[ { type:\"dns\", intensity: \"critical\"} ] }"
```

`healthMonitoringIntensities` accepts an array of documents,
`values`. Each document in `values` takes two fields: 

- `type`, the Health Manager facet 
- `intensity`, the intensity level

See `healthMonitoringIntensities` for details.

### Intervals

For example, to set the `ldap` Health Manager facet to the 
run health checks every 30 seconds, issue the following at startup:

```bash
mongos --setParameter 'healthMonitoringIntervals={ values:[ { type:"ldap", interval: "30000"} ] }'
```

Or if using the `setParameter` command in a
`mongosh` session that is connected to a running
`mongos`:

```javascript
db.adminCommand( 
  {
      setParameter: 1, 
      healthMonitoringIntervals: { values: [ { type: "ldap", interval: "30000" } ] } } )
  }
)
```

Parameters set with `setParameter` do not persist across
restarts. See the setParameter page for details.

To make this setting persistent, set `healthMonitoringIntervals`
in your mongos config file using the
`setParameter` option as in the following example:

```yaml
setParameter:
   healthMonitoringIntervals: "{ values: [{type: \"ldap\", interval: 200}] }"
```

`healthMonitoringIntervals` accepts an array of documents,
`values`. Each document in `values` takes two fields:

- `type`, the Health Manager facet 
- `interval`, the time interval it runs at, in milliseconds

See `healthMonitoringIntervals` for details.

### Active Fault Duration

For example, to set the duration from failure to crash to five
minutes, issue the following at startup:

```bash
mongos --setParameter activeFaultDurationSecs=300
```

Or if using the `setParameter` command in a
`mongosh` session that is connected to a running
`mongos`:

```javascript
db.adminCommand( 
  {
      setParameter: 1, 
      activeFaultDurationSecs: 300 
  }
)
```

Parameters set with `setParameter` do not persist across
restarts. See the setParameter page for details.

To make this setting persistent, set `activeFaultDurationSecs`
in your mongos config file using the
`setParameter` option as in the following example:

```yaml
setParameter:
   activeFaultDurationSecs: 300
```

See `activeFaultDurationSecs` for details.

### Progress Monitor

Progress Monitor runs tests 
to ensure that Health Manager checks do not become stuck or 
unresponsive. Progress Monitor runs these tests in intervals specified 
by `interval`. If a health check begins but does not complete within
the timeout given by `deadline`, Progress Monitor stops the 
mongos and removes it from the cluster.

To set the `interval` to 1000 milliseconds and the `deadline` 
to 300 seconds, issue the following at startup:

```bash
mongos --setParameter 'progressMonitor={"interval": 1000, "deadline": 300}'
```

Or if using the `setParameter` command in a
`mongosh` session that is connected to a running
`mongos`:

```javascript
db.adminCommand( 
  {
      setParameter: 1, 
      progressMonitor: { interval: 1000, deadline: 300 } )
  }
)
```

Parameters set with `setParameter` do not persist across
restarts. See the setParameter page for details.

To make this setting persistent, set `progressMonitor`
in your mongos config file using the
`setParameter` option as in the following example:

```yaml
setParameter:
   progressMonitor: "{ interval: 1000, deadline: 300 }"
```

See `progressMonitor` for details.
