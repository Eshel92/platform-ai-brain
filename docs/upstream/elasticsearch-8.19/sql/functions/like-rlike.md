<!-- Converted from sql/functions/like-rlike.asciidoc (AsciiDoc). Includes are inlined. -->

### LIKE and RLIKE Operators

`LIKE` and `RLIKE` operators are commonly used to filter data based on string patterns. They usually act on a field placed on the left-hand side of
the operator, but can also act on a constant (literal) expression. The right-hand side of the operator represents the pattern.
Both can be used in the `WHERE` clause of the `SELECT` statement, but `LIKE` can also be used in other places, such as defining an
index pattern or across various SHOW commands.
This section covers only the `SELECT ... WHERE ...` usage.

**Note:** One significant difference between `LIKE`/`RLIKE` and the full-text search predicates is that the former
act on exact fields while the latter also work on analyzed fields. If the field used with `LIKE`/`RLIKE` doesn't
have an exact not-normalized sub-field (of keyword type) {es-sql} will not be able to run the query. If the field is either exact
or has an exact sub-field, it will use it as is, or it will automatically use the exact sub-field even if it wasn't explicitly specified in the statement.

#### `LIKE`

**Synopsis:**
```sql
expression        <1>
LIKE constant_exp <2>
```

<1> typically a field, or a constant expression
<2> pattern

*Description*: The SQL `LIKE` operator is used to compare a value to similar values using wildcard operators. There are two wildcards used in conjunction
with the `LIKE` operator:

* The percent sign (%)
* The underscore (_)

The percent sign represents zero, one or multiple characters. The underscore represents a single number or character. These symbols can be used in combinations.

**Note:** No other characters have special meaning or act as wildcard. Characters often used as wildcards in other languages (`*` or `?`) are treated as normal characters.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[simpleLike]
```

There is, also, the possibility of using an escape character if one needs to match the wildcard characters themselves. This can be done
by using the `ESCAPE [escape_character]` statement after the `LIKE ...` operator:

 SELECT name, author FROM library WHERE name LIKE 'Dune/%' ESCAPE '/';

In the example above `/` is defined as an escape character which needs to be placed before the `%` or `_` characters if one needs to
match those characters in the pattern specifically. By default, there is no escape character defined.

**Important:** Even though `LIKE` is a valid option when searching or filtering in {es-sql}, full-text search predicates
`MATCH` and `QUERY` are faster and much more powerful and are the preferred alternative.

#### `RLIKE`

**Synopsis:**
```sql
expression         <1>
RLIKE constant_exp <2>
```

<1> typically a field, or a constant expression
<2> pattern

*Description*: This operator is similar to `LIKE`, but the user is not limited to search for a string based on a fixed pattern with the percent sign (`%`)
and underscore (`_`); the pattern in this case is a regular expression which allows the construction of more flexible patterns.

For supported syntax, see regexp-syntax.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[simpleRLike]
```

**Important:** Even though `RLIKE` is a valid option when searching or filtering in {es-sql}, full-text search predicates
`MATCH` and `QUERY` are faster and much more powerful and are the preferred alternative.

#### Prefer full-text search predicates

When using `LIKE`/`RLIKE`, do consider using full-text search predicates which are faster, much more powerful
and offer the option of sorting by relevancy (results can be returned based on how well they matched).
