<!-- Converted from reference/stable-api-changelog.txt (reStructuredText). Includes are inlined. -->

# Stable API Changelog

This page contains a changelog of the Stable API. The Stable API is
actively being expanded to include new database commands and
functionality.

The commands and operators included in the Stable API depend on the
MongoDB version you are using. This page describes the MongoDB and
Stable API versions when a database command or specific sub-features of
a command are available.

## Database Commands

The following table describes:

- The commands included in each version of the Stable API.

- The MongoDB version in which the command was added to the Stable API.

| Command | Stable API Version | Added to Stable API in Version |
|---|---|---|
| `count` | V1 | MongoDB 6.0, 5.0.9 |
| `abortTransaction` | V1 | MongoDB 5.0 |
| `aggregate` (with limitations) | V1 | MongoDB 5.0 |
| `authenticate` | V1 | MongoDB 5.0 |
| `collMod` | V1 | MongoDB 5.0 |
| `commitTransaction` | V1 | MongoDB 5.0 |
| `create` (with limitations) [#stable-api-command-limitations]_ | V1 | MongoDB 5.0 |
| `createIndexes` (with limitations) [#stable-api-command-limitations]_ | V1 | MongoDB 5.0 |
| `delete` | V1 | MongoDB 5.0 |
| `drop` | V1 | MongoDB 5.0 |
| `dropDatabase` | V1 | MongoDB 5.0 |
| `dropIndexes` | V1 | MongoDB 5.0 |
| `endSessions` | V1 | MongoDB 5.0 |
| `explain` [#stable-api-explain]_ | V1 | MongoDB 5.0 |
| `find` (with limitations) [#stable-api-command-limitations]_ | V1 | MongoDB 5.0 |
| `findAndModify` | V1 | MongoDB 5.0 |
| `getMore` | V1 | MongoDB 5.0 |
| `insert` | V1 | MongoDB 5.0 |
| `hello` | V1 | MongoDB 5.0 |
| `killCursors` | V1 | MongoDB 5.0 |
| `listCollections` | V1 | MongoDB 5.0 |
| `listDatabases` | V1 | MongoDB 5.0 |
| `listIndexes` | V1 | MongoDB 5.0 |
| `ping` | V1 | MongoDB 5.0 |
| `refreshSessions` | V1 | MongoDB 5.0 |
| `update` | V1 | MongoDB 5.0 |

## Aggregation

This section describes the aggregation stages and operators included in
the Stable API.

### Unsupported Aggregation Stages

The following aggregation stages are **not included** in the Stable API:

- `$currentOp`
- `$indexStats`
- `$listLocalSessions`
- `$listSessions`
- `$planCacheStats`
- `$search`

For more information on aggregation in the Stable API, see the
Stable API section of the
`aggregate` command page.

### Supported Aggregation Operators

The following aggregation operators are included in the Stable API:

| Operator | Stable API Version | Added to Stable API in Version |
|---|---|---|
| `$abs` | V1 | MongoDB 5.0 |
| `$add` | V1 | MongoDB 5.0 |
| `$addToSet` | V1 | MongoDB 6.0 |
| `$and` (aggregation) | V1 | MongoDB 5.0 |
| `$anyElementTrue` | V1 | MongoDB 5.0 |
| `$arrayElemAt` | V1 | MongoDB 5.0 |
| `$arrayToObject` | V1 | MongoDB 5.0 |
| `$avg` | V1 | MongoDB 6.0 |
| `$binarySize` | V1 | MongoDB 5.0 |
| `$bsonSize` | V1 | MongoDB 5.0 |
| `$bottom` | V1 | MongoDB 6.0 |
| `$bottomN` | V1 | MongoDB 6.0 |
| `$ceil` | V1 | MongoDB 5.0 |
| `$cmp` | V1 | MongoDB 5.0 |
| `$concat` | V1 | MongoDB 5.0 |
| `$concatArrays` | V1 | MongoDB 5.0 |
| `$cond` | V1 | MongoDB 5.0 |
| `$convert` | V1 | MongoDB 5.0 |
| `$count` | V1 | MongoDB 6.0 |
| `$covariancePop` | V1 | MongoDB 6.0 |
| `$covarianceSamp` | V1 | MongoDB 6.0 |
| `$dateAdd` | V1 | MongoDB 6.0 |
| `$dateDiff` | V1 | MongoDB 6.0 |
| `$dateFromParts` | V1 | MongoDB 5.0 |
| `$dateFromString` | V1 | MongoDB 5.0 |
| `$dateSubtract` | V1 | MongoDB 6.0 |
| `$dateToParts` | V1 | MongoDB 5.0 |
| `$dateToString` | V1 | MongoDB 5.0 |
| `$dateTrunc` | V1 | MongoDB 6.0 |
| `$denseRank` | V1 | MongoDB 6.0 |
| `$densify` | V1 | MongoDB 6.0 |
| `$derivative` | V1 | MongoDB 6.0 |
| `$divide` | V1 | MongoDB 5.0 |
| `$documentNumber` | V1 | MongoDB 6.0 |
| `$eq` | V1 | MongoDB 5.0 |
| `$exp` | V1 | MongoDB 5.0 |
| `$expMovingAvg` | V1 | MongoDB 6.0 |
| `$filter` | V1 | MongoDB 5.0 |
| `$first` | V1 | MongoDB 6.0 |
| `$floor` | V1 | MongoDB 5.0 |
| `$first` | V1 | MongoDB 5.0 |
| `$firstN` (aggregation accumulator) | V1 | MongoDB 6.0 |
| `$firstN` (array operator) | V1 | MongoDB 6.0 |
| `$getField` | V1 | MongoDB 6.0 |
| `$gt` | V1 | MongoDB 5.0 |
| `$gte` | V1 | MongoDB 5.0 |
| `$ifNull` | V1 | MongoDB 5.0 |
| `$in` | V1 | MongoDB 5.0 |
| `$indexOfArray` | V1 | MongoDB 5.0 |
| `$indexOfBytes` | V1 | MongoDB 5.0 |
| `$indexOfCP` | V1 | MongoDB 5.0 |
| `$integral` | V1 | MongoDB 6.0 |
| `$isArray` | V1 | MongoDB 5.0 |
| `$isNumber` | V1 | MongoDB 5.0 |
| `$last` | V1 | MongoDB 5.0 |
| `$lastN` (aggregation accumulator) | V1 | MongoDB 6.0 |
| `$lastN` (array operator) | V1 | MongoDB 6.0 |
| `$let` | V1 | MongoDB 5.0 |
| `$literal` | V1 | MongoDB 5.0 |
| `$locf` | V1 | MongoDB 6.0 |
| `$ln` | V1 | MongoDB 5.0 |
| `$log` | V1 | MongoDB 5.0 |
| `$log10` | V1 | MongoDB 5.0 |
| `$lt` | V1 | MongoDB 5.0 |
| `$lte` | V1 | MongoDB 5.0 |
| `$ltrim` | V1 | MongoDB 5.0 |
| `$map` | V1 | MongoDB 5.0 |
| `$max` | V1 | MongoDB 6.0 |
| `$maxN` (aggregation accumulator) | V1 | MongoDB 6.0 |
| `$maxN` (array operator) | V1 | MongoDB 6.0 |
| `$mergeObjects` | V1 | MongoDB 5.0 |
| `$min` | V1 | MongoDB 6.0 |
| `$minN` (aggregation accumulator) | V1 | MongoDB 6.0 |
| `$minN` (array operator) | V1 | MongoDB 6.0 |
| `$mod` | V1 | MongoDB 5.0 |
| `$multiply` | V1 | MongoDB 5.0 |
| `$ne` | V1 | MongoDB 5.0 |
| `$not` | V1 | MongoDB 5.0 |
| `$objectToArray` | V1 | MongoDB 5.0 |
| `$or` | V1 | MongoDB 5.0 |
| `$pow` | V1 | MongoDB 5.0 |
| `$push` | V1 | MongoDB 6.0 |
| `$rand` | V1 | MongoDB 5.0 |
| `$range` | V1 | MongoDB 5.0 |
| `$rank` | V1 | MongoDB 6.0 |
| `$reduce` | V1 | MongoDB 5.0 |
| `$regexFind` | V1 | MongoDB 5.0 |
| `$regexFindAll` | V1 | MongoDB 5.0 |
| `$regexMatch` | V1 | MongoDB 5.0 |
| `$replaceAll` | V1 | MongoDB 5.0 |
| `$replaceOne` | V1 | MongoDB 5.0 |
| `$reverseArray` | V1 | MongoDB 5.0 |
| `$round` | V1 | MongoDB 5.0 |
| `$rtrim` | V1 | MongoDB 5.0 |
| `$setDifference` | V1 | MongoDB 5.0 |
| `$setEquals` | V1 | MongoDB 5.0 |
| `$setField` | V1 | MongoDB 6.0 |
| `$setIntersection` | V1 | MongoDB 5.0 |
| `$setIsSubset` | V1 | MongoDB 5.0 |
| `$setUnion` | V1 | MongoDB 5.0 |
| `$setWindowFields` | V1 | MongoDB 6.0 |
| `$shift` | V1 | MongoDB 6.0 |
| `$slice` | V1 | MongoDB 5.0 |
| `$size` | V1 | MongoDB 5.0 |
| `$sortArray` | V1 | MongoDB 6.0 |
| `$split` | V1 | MongoDB 5.0 |
| `$sqrt` | V1 | MongoDB 5.0 |
| `$stdDevPop` | V1 | MongoDB 6.0 |
| `$stdDevSamp` | V1 | MongoDB 6.0 |
| `$strcasecmp` | V1 | MongoDB 5.0 |
| `$strLenBytes` | V1 | MongoDB 5.0 |
| `$strLenCP` | V1 | MongoDB 5.0 |
| `$substr` | V1 | MongoDB 5.0 |
| `$substrBytes` | V1 | MongoDB 5.0 |
| `$substrCP` | V1 | MongoDB 5.0 |
| `$subtract` | V1 | MongoDB 5.0 |
| `$sum` | V1 | MongoDB 6.0 |
| `$switch` | V1 | MongoDB 5.0 |
| `$toLower` | V1 | MongoDB 5.0 |
| `$top` | V1 | MongoDB 6.0 |
| `$topN` | V1 | MongoDB 6.0 |
| `$toUpper` | V1 | MongoDB 5.0 |
| `$trim` | V1 | MongoDB 5.0 |
| `$trunc` | V1 | MongoDB 5.0 |
| `$type` | V1 | MongoDB 5.0 |
| `$tsIncrement` | V1 | MongoDB 6.0 |
| `$tsSecond` | V1 | MongoDB 6.0 |
| `$zip` | V1 | MongoDB 5.0 |
