<!-- Converted from reference/method/db.collection.configureQueryAnalyzer.txt (reStructuredText). Includes are inlined. -->

# db.collection.configureQueryAnalyzer() (mongosh method)

## Definition

**`db.collection.configureQueryAnalyzer(options)`**

Configures query sampling for a collection on a replica set or
sharded cluster. Sampled queries provide information to 
`analyzeShardKey` to calculate metrics about read and 
write distribution of a shard key.

The `db.collection.configureQueryAnalyzer()` method wraps the
`configureQueryAnalyzer` command.

:returns: 
   A document containing fields describing the old configuration, if
   one exists, and fields describing the new configuration. For
   details, see cqa-output.

## Compatibility

This method is available in deployments hosted in the following environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0 and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The method has the following syntax:

```javascript
db.collection.configureQueryAnalyzer( 
   {
     mode: <string>,
     samplesPerSecond: <double>
   } 
)
```

### Fields

`db.collection.configureQueryAnalyzer()` has the following fields:

* - Field
  - Type
  - Necessity
  - Description

* - `mode`
  - string
  - Required
  - Mode the query analyzer runs in. Must be set to either
    `"full"` or `"off"`.

* - `samplesPerSecond`
  - double
  - Optional
  - Number of samples per second.

    - When `mode` is set to `"full"`, `samplesPerSecond` must
      be set between `0` and `50`.
    - When `mode` is set to `"off"`, the server ignores
      `samplesPerSecond`.

    For details, see samplesPerSeconds Upper Limit.

## Access Control

For details, see configureQueryAnalyzer Access Control.

## Behavior

For behavior, see configureQueryAnalyzer Behavior.

## Output

For details, see configureQueryAnalyzer Output.

## Examples

For examples, see configureQueryAnalyzer Examples.

## Learn More

- `analyzeShardKey`
- `configureQueryAnalyzer`
- `$listSampledQueries`
