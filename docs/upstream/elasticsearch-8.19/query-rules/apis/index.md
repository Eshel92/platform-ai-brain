<!-- Converted from query-rules/apis/index.asciidoc (AsciiDoc). Includes are inlined. -->

## Query rules APIs

---

**New API reference**
For the most up-to-date API details, refer to [Query rules APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-query_rules).

Query rules allow you to configure per-query rules that are applied at query time to queries that match the specific rule.
Query rules are organized into _rulesets_, collections of query rules that are matched against incoming queries.
Query rules are applied using the rule query.

If a query matches one or more rules in the ruleset, the query is re-written to apply the rules before searching.
This allows pinning documents for only queries that match a specific term.

Use the following APIs to manage query rulesets:

* put-query-ruleset
* get-query-ruleset
* list-query-rulesets
* delete-query-ruleset
* put-query-rule
* get-query-rule
* delete-query-rule
* preview:[] test-query-ruleset

(See `query-rules/apis/put-query-ruleset.md`)
(See `query-rules/apis/get-query-ruleset.md`)
(See `query-rules/apis/list-query-rulesets.md`)
(See `query-rules/apis/delete-query-ruleset.md`)
(See `query-rules/apis/put-query-rule.md`)
(See `query-rules/apis/get-query-rule.md`)
(See `query-rules/apis/delete-query-rule.md`)
(See `query-rules/apis/test-query-ruleset.md`)
