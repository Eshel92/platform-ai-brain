<!-- Converted from reference/operator/aggregation/queryStats/toggle-logging.txt (reStructuredText). Includes are inlined. -->

# Toggle $queryStats Log Output

MongoDB records `$queryStats` operations in the deployment logs. By default, MongoDB only logs the invocation of
`$queryStats` operations, not the operation's output. For
`$queryStats` operations that include the `transformIdentifiers`
option, you can specify whether the transformed output is included in
the log entry.

Including `$queryStats` output in the logs provides more information
on specific `$queryStats` operations, but can negatively impact
cluster performance as log updates take more time and resources.

## About this Task

When MongoDB logs `$queryStats` output, the results are redacted and
anonymized. `$queryStats` output does not contain literals or field
values.

For an example of transformed `$queryStats` output, see
queryStats-example-transformed.

## Steps

**Step 1: In the MongoDB Atlas UI, go to the Clusters page for your project.**

a. If it's not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it's not already displayed, select your project
   from the Projects menu in the navigation bar.

#. In the sidebar, click Clusters under 
   the Database heading.

   The [Clusters](https://cloud.mongodb.com/go?l=https%3A%2F%2Fcloud.mongodb.com%2Fv2%2F%3Cproject%3E%23%2Fclusters) page displays.

**Step 2: Click Edit Config**

**Step 3: Select your cluster from the dropdown**

**Step 4: Open the Additional Settings dropdown**

**Step 5: Open the More Configuration Options dropdown**

**Step 6: Toggle the Enable Logging of Redacted and Anonymized Query Data setting**

**Step 7: Click Review Changes**

**Step 8: Click Apply Changes**

## Examples

The following examples show the differences in log messages when
`$queryStats` output is included.

**Note:**

The example log entries are reformatted for readability.

### `$queryStats` Output Omitted (Default Behavior)

```javascript
{
  "t":{"$date":"2023-11-27T20:58:59.212+00:00"},"s":"D1", "c":"QRYSTATS",
  "id":7808300, "ctx":"conn31","msg":"Logging invocation
  $queryStats","attr":{"commandSpec":{"transformIdentifiers":{"algorithm":"hmac-sha-256","hmacKey":"###"}}
}
```

### `$queryStats` Output Included

```javascript
{
  "t":{"$date":"2023-11-27T20:58:59.212+00:00"},"s":"D1", "c":"QRYSTATS",
  "id":7808300, "ctx":"conn31","msg":"Logging invocation
  $queryStats","attr":{"commandSpec":{"transformIdentifiers":{"algorithm":"hmac-sha-256","hmacKey":"###"}}
}

{
  "t":{"$date":"2023-11-27T20:58:59.212+00:00"},"s":"D3", "c":"QRYSTATS",
  "id":7808301, "ctx":"conn31","msg":"Logging all outputs of
  $queryStats","attr":{"thisOutput":"{key: {queryShape: {cmdNs: {db:
  \"hYt+nW/sr1/Zc3YR8nlGWFoesJdvywkw+cR9rMGzXU4=\", coll:
  \"TRx6R3rvstYgX96gNmeOi5E3QVsOqzRbv7A9j3q7OvM=\"}, command: \"find\",
  filter: {Wb/Uu22DzKZ/Os+ZvLgPKFKGZPV4cIMZ3Ybv1HfYih4=: {$lt:
  \"?date\"}}, projection: {r5zQZllsGoqQuQp4Jm0eH2M6RrMqH84KHowcFaiverg=:
  true}, sort: {r5zQZllsGoqQuQp4Jm0eH2M6RrMqH84KHowcFaiverg=: 1}},
  readConcern: {}, collectionType: \"nonExistent\"}, metrics:
  {lastExecutionMicros: 208, execCount: 21, totalExecMicros: {sum: 6079,
  max: 1875, min: 198, sumOfSquares: 4401645}, firstResponseExecMicros:
  {sum: 6079, max: 1875, min: 198, sumOfSquares: 4401645}, docsReturned:
  {sum: 0, max: 0, min: 0, sumOfSquares: 0}, firstSeenTimestamp:
  2023-11-27T19:15:51.317Z, latestSeenTimestamp:
  2023-11-27T20:55:51.309Z}, asOf: 2023-11-27T20:58:59.212Z}"}
}

{
  "t":{"$date":"2023-11-27T20:58:59.213+00:00"},"s":"D3", "c":"QRYSTATS",
  "id":7808301, "ctx":"conn31","msg":"Logging all outputs of
  $queryStats","attr":{"thisOutput":"{key: {queryShape: {cmdNs: {db:
  \"j+Caz+gxt7vl++gmeCAWrvyhDL17WaNrSIDi6Au7VI0=\", coll:
  \"f/LCkK/kVEbt4fk2NNbyDPhxas+kzCLLcVbjeNBbhyg=\"}, let:
  {pUZAyEEImSXcu8deG05tfIf6F/H92YsFnkZXIeRQtgc=: \"?number\"}, command:
  \"aggregate\", pipeline: [{$group: {_id: \"?number\",
  5E6FSc5VxCvIZK0jrqkY3k3aX51jSc73hQwO/8kH0lo=: {$sum: \"?number\"}}}],
  explain: true, allowDiskUse: false}, client: {driver: {name:
  \"nodejs|mongosh\", version: \"5.1.0\"}, os: {type: \"Darwin\", name:
  \"darwin\", architecture: \"arm64\", version: \"22.6.0\"}, platform:
  \"Node.js v16.19.1, LE (unified)\", version: \"5.1.0|1.8.0\",
  application: {name: \"mongosh 1.8.0\"}}, collectionType: \"collection\",
  cursor: {batchSize: \"?number\"}}, metrics: {lastExecutionMicros: 0,
  execCount: 1, totalExecMicros: {sum: 0, max: 0, min: 0, sumOfSquares:
  0}, firstResponseExecMicros: {sum: 0, max: 0, min: 0, sumOfSquares: 0},
  docsReturned: {sum: 0, max: 0, min: 0, sumOfSquares: 0},
  firstSeenTimestamp: 2023-11-27T19:31:36.463Z, latestSeenTimestamp:
  2023-11-27T19:31:36.463Z}, asOf: 2023-11-27T20:58:59.213Z}"}
}

// Additional $queryStats output...
```

## Learn More

- auditing

- audit-message

- Configure a Custom Auditing Filter
