<!-- Converted from query-dsl/regexp-query.asciidoc (AsciiDoc). Includes are inlined. -->

### Regexp query

Returns documents that contain terms matching a
[regular expression](https://en.wikipedia.org/wiki/Regular_expression).

A regular expression is a way to match patterns in data using placeholder
characters, called operators. For a list of operators supported by the
`regexp` query, see Regular expression syntax.

#### Example request

The following search returns documents where the `user.id` field contains any term
that begins with `k` and ends with `y`. The `.*` operators match any
characters of any length, including no characters. Matching
terms can include `ky`, `kay`, and `kimchy`.

```console
GET /_search
{
  "query": {
    "regexp": {
      "user.id": {
        "value": "k.*y",
        "flags": "ALL",
        "case_insensitive": true,
        "max_determinized_states": 10000,
        "rewrite": "constant_score_blended"
      }
    }
  }
}
```

#### Top-level parameters for `regexp`

`<field>`::
(Required, object) Field you wish to search.

#### Parameters for `<field>`

`value`::
(Required, string) Regular expression for terms you wish to find in the provided
`<field>`. For a list of supported operators, see <<regexp-syntax, Regular
expression syntax>>.
By default, regular expressions are limited to 1,000 characters. You can change
this limit using the `index.max_regex_length`
setting.

=====
The performance of the `regexp` query can vary based on the regular expression
provided. To improve performance, avoid using wildcard patterns, such as `.*` or
`.*?+`, without a prefix or suffix.
=====

`flags`::
(Optional, string) Enables optional operators for the regular expression. For
valid values and more information, see <<regexp-optional-operators, Regular
expression syntax>>.

`case_insensitive` added:[7.10.0]::
(Optional, Boolean) Allows case insensitive matching of the regular expression
value with the indexed field values when set to true. Default is false which means
the case sensitivity of matching depends on the underlying field's mapping.

`max_determinized_states`::
(Optional, integer) Maximum number of
[automaton states](https://en.wikipedia.org/wiki/Deterministic_finite_automaton)
required for the query. Default is `10000`.

Elasticsearch uses [Apache Lucene](https://lucene.apache.org/core/) internally to parse
regular expressions. Lucene converts each regular expression to a finite
automaton containing a number of determinized states.

You can use this parameter to prevent that conversion from unintentionally
consuming too many resources. You may need to increase this limit to run complex
regular expressions.

`rewrite`::
(Optional, string) Method used to rewrite the query. For valid values and more
information, see the `rewrite` parameter.

#### Notes

##### Allow expensive queries

Regexp queries will not be executed if `search.allow_expensive_queries`
is set to false.
