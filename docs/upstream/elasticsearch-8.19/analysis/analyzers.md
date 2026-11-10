<!-- Converted from analysis/analyzers.asciidoc (AsciiDoc). Includes are inlined. -->

## Built-in analyzer reference

Elasticsearch ships with a wide range of built-in analyzers, which can be used
in any index without further configuration:

Standard Analyzer::

The `standard` analyzer divides text into terms on word boundaries, as defined
by the Unicode Text Segmentation algorithm. It removes most punctuation,
lowercases terms, and supports removing stop words.

Simple Analyzer::

The `simple` analyzer divides text into terms whenever it encounters a
character which is not a letter. It lowercases all terms.

Whitespace Analyzer::

The `whitespace` analyzer divides text into terms whenever it encounters any
whitespace character. It does not lowercase terms.

Stop Analyzer::

The `stop` analyzer is like the `simple` analyzer, but also supports removal
of stop words.

Keyword Analyzer::

The `keyword` analyzer is a ``noop'' analyzer that accepts whatever text it is
given and outputs the exact same text as a single term.

Pattern Analyzer::

The `pattern` analyzer uses a regular expression to split the text into terms.
It supports lower-casing and stop words.

Language Analyzers::

Elasticsearch provides many language-specific analyzers like `english` or
`french`.

Fingerprint Analyzer::

The `fingerprint` analyzer is a specialist analyzer which creates a
fingerprint which can be used for duplicate detection.

### Custom analyzers

If you do not find an analyzer suitable for your needs, you can create a
`custom` analyzer which combines the appropriate
character filters,
tokenizer, and token filters.

(See `analysis/analyzers/fingerprint-analyzer.md`)
(See `analysis/analyzers/keyword-analyzer.md`)
(See `analysis/analyzers/lang-analyzer.md`)
(See `analysis/analyzers/pattern-analyzer.md`)
(See `analysis/analyzers/simple-analyzer.md`)
(See `analysis/analyzers/standard-analyzer.md`)
(See `analysis/analyzers/stop-analyzer.md`)
(See `analysis/analyzers/whitespace-analyzer.md`)
