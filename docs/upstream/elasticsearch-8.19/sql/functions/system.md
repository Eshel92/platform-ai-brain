<!-- Converted from sql/functions/system.asciidoc (AsciiDoc). Includes are inlined. -->

### System Functions

These functions return metadata type of information about the system being queried.

#### `DATABASE`

**Synopsis:**
```sql
DATABASE()
```

*Input*: _none_

*Output*: string

*Description*: Returns the name of the database being queried. In the case of Elasticsearch SQL, this
is the name of the Elasticsearch cluster. This function should always return a non-null
value.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[database]
```

#### `USER`

**Synopsis:**
```sql
USER()
```
*Input*: _none_

*Output*: string

*Description*: Returns the username of the authenticated user executing the query. This function can
return `null` in case security is disabled.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[user]
```
