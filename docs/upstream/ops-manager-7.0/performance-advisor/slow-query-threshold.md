<!-- Converted from performance-advisor/slow-query-threshold.txt (reStructuredText). Includes are inlined. -->

# Configure the Slow Query Threshold

The Performance Advisor recognizes a query as slow if it takes longer
to execute than the value of
slowms.
By default, this value is `100` milliseconds. You can change the
threshold with either the
profile
command or the db.setProfilingLevel()
`mongosh` method.

**Example:**

The following `profile` command example sets the threshold at 200
milliseconds:

```json
db.runCommand({
  profile: 0,
  slowms: 200
})
```

If you are running MongoDB 3.6 or later, you can customize the
percentage of slow queries in your logs used by the Performance Advisor
by specifying the `sampleRate` parameter.

**Example:**

This sets the slow query threshold to a lower value of 100
milliseconds but also sets the sample rate to 10%.

```json
db.runCommand({
  profile: 0,
  slowms: 100,
  sampleRate: 0.1
})
```

**Note:**

By default, the value of `profile` is `0`. MongoDB recommends
leaving this value unchanged since other values can negatively
impact database performance. To learn more, see the
profile command.
