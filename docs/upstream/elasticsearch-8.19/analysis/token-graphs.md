<!-- Converted from analysis/token-graphs.asciidoc (AsciiDoc). Includes are inlined. -->

### Token graphs

When a tokenizer converts a text into a stream of
tokens, it also records the following:

* The `position` of each token in the stream
* The `positionLength`, the number of positions that a token spans

Using these, you can create a
[directed acyclic graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph),
called a _token graph_, for a stream. In a token graph, each position represents
a node. Each token represents an edge or arc, pointing to the next position.

(Figure: images/analysis/token-graph-qbf-ex.svg)

#### Synonyms

Some token filters can add new tokens, like
synonyms, to an existing token stream. These synonyms often span the same
positions as existing tokens.

In the following graph, `quick` and its synonym `fast` both have a position of
`0`. They span the same positions.

(Figure: images/analysis/token-graph-qbf-synonym-ex.svg)

#### Multi-position tokens

Some token filters can add tokens that span multiple positions. These can
include tokens for multi-word synonyms, such as using "atm" as a synonym for
"automatic teller machine."

However, only some token filters, known as _graph token filters_, accurately
record the `positionLength` for multi-position tokens. These filters include:

* `synonym_graph`
* `word_delimiter_graph`

Some tokenizers, such as the
{plugins}/analysis-nori-tokenizer.html[`nori_tokenizer`], also accurately
decompose compound tokens into multi-position tokens.

In the following graph, `domain name system` and its synonym, `dns`, both have a
position of `0`. However, `dns` has a `positionLength` of `3`. Other tokens in
the graph have a default `positionLength` of `1`.

(Figure: images/analysis/token-graph-dns-synonym-ex.svg)

##### Using token graphs for search 

Indexing ignores the `positionLength` attribute
and does not support token graphs containing multi-position tokens.

However, queries, such as the `match` or
`match_phrase` query, can use these graphs to
generate multiple sub-queries from a single query string.

.*Example*

A user runs a search for the following phrase using the `match_phrase` query:

`domain name system is fragile`

During search analysis, `dns`, a synonym for
`domain name system`, is added to the query string's token stream. The `dns`
token has a `positionLength` of `3`.

(Figure: images/analysis/token-graph-dns-synonym-ex.svg)

The `match_phrase` query uses this graph to generate sub-queries for the
following phrases:

```text
dns is fragile
domain name system is fragile
```

This means the query matches documents containing either `dns is fragile` _or_
`domain name system is fragile`.

##### Invalid token graphs

The following token filters can add tokens that span multiple positions but
only record a default `positionLength` of `1`:

* `synonym`
* `word_delimiter`

This means these filters will produce invalid token graphs for streams
containing such tokens.

In the following graph, `dns` is a multi-position synonym for `domain name
system`. However, `dns` has the default `positionLength` value of `1`, resulting
in an invalid graph.

(Figure: images/analysis/token-graph-dns-invalid-ex.svg)

Avoid using invalid token graphs for search. Invalid graphs can cause unexpected
search results.
