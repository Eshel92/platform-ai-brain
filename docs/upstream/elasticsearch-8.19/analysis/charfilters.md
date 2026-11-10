<!-- Converted from analysis/charfilters.asciidoc (AsciiDoc). Includes are inlined. -->

## Character filters reference

_Character filters_ are used to preprocess the stream of characters before it
is passed to the tokenizer.

A character filter receives the original text as a stream of characters and
can transform the stream by adding, removing, or changing characters. For
instance, a character filter could be used to convert Hindu-Arabic numerals
(٠‎١٢٣٤٥٦٧٨‎٩‎) into their Arabic-Latin equivalents (0123456789), or to strip HTML
elements like `<b>` from the stream.

Elasticsearch has a number of built in character filters which can be used to build
custom analyzers.

HTML Strip Character Filter::

The `html_strip` character filter strips out HTML elements like `<b>` and
decodes HTML entities like `&amp;`.

Mapping Character Filter::

The `mapping` character filter replaces any occurrences of the specified
strings with the specified replacements.

Pattern Replace Character Filter::

The `pattern_replace` character filter replaces any characters matching a
regular expression with the specified replacement.

(See `analysis/charfilters/htmlstrip-charfilter.md`)
(See `analysis/charfilters/mapping-charfilter.md`)
(See `analysis/charfilters/pattern-replace-charfilter.md`)
