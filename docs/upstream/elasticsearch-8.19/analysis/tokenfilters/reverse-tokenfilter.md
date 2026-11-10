<!-- Converted from analysis/tokenfilters/reverse-tokenfilter.asciidoc (AsciiDoc). Includes are inlined. -->

### Reverse token filter

Reverses each token in a stream. For example, you can use the `reverse` filter
to change `cat` to `tac`.

Reversed tokens are useful for suffix-based searches,
such as finding words that end in `-ion` or searching file names by their
extension.

This filter uses Lucene's
{lucene-analysis-docs}/reverse/ReverseStringFilter.html[ReverseStringFilter].

#### Example

The following analyze API request uses the `reverse`
filter to reverse each token in `quick fox jumps`:

```console
GET _analyze
{
  "tokenizer" : "standard",
  "filter" : ["reverse"],
  "text" : "quick fox jumps"
}
```

The filter produces the following tokens:

```text
[ kciuq, xof, spmuj ]
```

```console-result
{
  "tokens" : [
    {
      "token" : "kciuq",
      "start_offset" : 0,
      "end_offset" : 5,
      "type" : "<ALPHANUM>",
      "position" : 0
    },
    {
      "token" : "xof",
      "start_offset" : 6,
      "end_offset" : 9,
      "type" : "<ALPHANUM>",
      "position" : 1
    },
    {
      "token" : "spmuj",
      "start_offset" : 10,
      "end_offset" : 15,
      "type" : "<ALPHANUM>",
      "position" : 2
    }
  ]
}
```

#### Add to an analyzer

The following create index API request uses the
`reverse` filter to configure a new
custom analyzer.

```console
PUT reverse_example
{
  "settings" : {
    "analysis" : {
      "analyzer" : {
        "whitespace_reverse" : {
          "tokenizer" : "whitespace",
          "filter" : ["reverse"]
        }
      }
    }
  }
}
```
