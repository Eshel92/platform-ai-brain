<!-- Converted from core/timeseries/timeseries-migrate-data-into-timeseries-collection.txt (reStructuredText). Includes are inlined. -->

# Migrate Data into a Time Series Collection

If your collection stores data that you want to compare across time intervals,
use a time series collection to improve performance and storage. For more
information on the benefits of time series collections, see
manual-timeseries-collection. 

You can use the following methods to
migrate data from an existing collection into a time series collection:

- Migrate with an Aggregation Pipeline
- Migrate with Database Tools
- [Migrate with Relational Migrator](https://www.mongodb.com/docs/relational-migrator/mapping-rules/mapping-rule-options/time-series/)

## Considerations

If you use MongoDB 7.0 or greater and already have your data in a MongoDB
database, migrate with an aggregation pipeline. 

If your data is in a relational database, use [Relational Migrator](https://www.mongodb.com/docs/relational-migrator/mapping-rules/mapping-rule-options/time-series/)
to migrate your data into a time series collection. 

If your deployment is not in one of those cases, use Database Tools to migrate your data.
