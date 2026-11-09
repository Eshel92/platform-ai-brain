<!-- Converted from modules/cassandra/pages/developing/cql/indexing/2i/_2i-check.adoc (AsciiDoc). Includes are inlined. -->

# Check secondary index (2i) existence

Verify that an index exists:

CQL::
+
--
```language-bash
DESCRIBE TABLE cycling.birthday_list;
```
--

Result::
+
--
```console
CREATE TABLE cycling.birthday_list (
    cyclist_name text PRIMARY KEY,
.
.
.

CREATE INDEX blist_values_idx ON cycling.birthday_list (values(blist));

```
--
