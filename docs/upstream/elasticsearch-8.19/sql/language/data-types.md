<!-- Converted from sql/language/data-types.asciidoc (AsciiDoc). Includes are inlined. -->

### Data Types

|===
s|Elasticsearch type
s|{es-sql} type
s|SQL type
s|SQL precision

4+h| Core types

| `null`                   | null            | NULL        | 0
| `boolean`                   | boolean         | BOOLEAN     | 1
| `byte`                       | byte            | TINYINT     | 3
| `short`                      | short           | SMALLINT    | 5
| `integer`                    | integer         | INTEGER     | 10
| `long`                       | long            | BIGINT      | 19
| `unsigned_long`              | experimental:[] unsigned_long   | BIGINT      | 20
| `double`                     | double          | DOUBLE      | 15
| `float`                      | float           | REAL        | 7
| `half_float`                 | half_float      | FLOAT       | 3
| `scaled_float`               | scaled_float    | DOUBLE      | 15
| keyword type family         | keyword         | VARCHAR     | 32,766
| `text`                         | text            | VARCHAR     | 2,147,483,647
| `binary`                     | binary          | VARBINARY   | 2,147,483,647
| `date`                         | datetime        | TIMESTAMP   | 29
| `ip`                             | ip              | VARCHAR     | 39
| `version`                   | version         | VARCHAR     | 32,766

4+h| Complex types

| `object`        | object        | STRUCT      | 0
| `nested`        | nested        | STRUCT      | 0

4+h| Unsupported types

| _types not mentioned above_ | unsupported   | OTHER       | 0

|===

Most of Elasticsearch data types are available in {es-sql}, as indicated above.
As one can see, all of Elasticsearch data types are mapped to the data type with the same
name in {es-sql}, with the exception of **date** data type which is mapped to **datetime** in {es-sql}.
This is to avoid confusion with the ANSI SQL types **DATE** (date only) and **TIME** (time only), which are also
supported by {es-sql} in queries (with the use of
sql-functions-type-conversion-cast/sql-functions-type-conversion-convert), but don't correspond to an
actual mapping in Elasticsearch (see the `table` below).

Obviously, not all types in Elasticsearch have an equivalent in SQL and vice-versa hence why, {es-sql}
uses the data type _particularities_ of the former over the latter as ultimately Elasticsearch is the backing store.

In addition to the types above, {es-sql} also supports at _runtime_ SQL-specific types that do not have an equivalent in Elasticsearch.
Such types cannot be loaded from Elasticsearch (as it does not know about them) however can be used inside {es-sql} in queries or their results.

The table below indicates these types:

|===
s|SQL type
s|SQL precision

| date                      | 29
| time                      | 18
| interval_year             | 7
| interval_month            | 7
| interval_day              | 23
| interval_hour             | 23
| interval_minute           | 23
| interval_second           | 23
| interval_year_to_month    | 7
| interval_day_to_hour      | 23
| interval_day_to_minute    | 23
| interval_day_to_second    | 23
| interval_hour_to_minute   | 23
| interval_hour_to_second   | 23
| interval_minute_to_second | 23
| geo_point                 | 52
| geo_shape                 | 2,147,483,647
| shape                     | 2,147,483,647

|===

#### SQL and multi-fields

A core concept in Elasticsearch is that of an `analyzed` field, that is a full-text value that is interpreted in order
to be effectively indexed. These fields are of type `text` and are not used for sorting or aggregations as their actual value depends on the `analyzer` used hence why Elasticsearch also offers the `keyword` type for storing the _exact_
value.

In most case, and the default actually, is to use both types for strings which Elasticsearch supports through multi-fields, that is the ability to index the same string in multiple ways; for example index it both as `text` for search but also as `keyword` for sorting and aggregations.

As SQL requires exact values, when encountering a `text` field {es-sql} will search for an exact multi-field that it can use for comparisons, sorting and aggregations.
To do that, it will search for the first `keyword` that it can find that is _not_ normalized and use that as the original field _exact_ value.

Consider the following `string` mapping:

```js
{
  "first_name": {
    "type": "text",
    "fields": {
      "raw": {
        "type": "keyword"
      }
    }
  }
}
```

The following SQL query:

```sql
SELECT first_name FROM index WHERE first_name = 'John'
```

is identical to:

```sql
SELECT first_name FROM index WHERE first_name.raw = 'John'
```

as {es-sql} automatically _picks_ up the `raw` multi-field from `raw` for exact matching.
