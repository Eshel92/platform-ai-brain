<!-- Converted from analysis/tokenfilters/asciifolding-tokenfilter.asciidoc (AsciiDoc). Includes are inlined. -->

### ASCII folding token filter

Converts alphabetic, numeric, and symbolic characters that are not in the Basic
Latin Unicode block (first 127 ASCII characters) to their ASCII equivalent, if
one exists. For example, the filter changes `à` to `a`.

This filter uses Lucene's
{lucene-analysis-docs}/miscellaneous/ASCIIFoldingFilter.html[ASCIIFoldingFilter].

#### Example

The following analyze API request uses the `asciifolding`
filter to drop the diacritical marks in `açaí à la carte`:

```console
GET /_analyze
{
  "tokenizer" : "standard",
  "filter" : ["asciifolding"],
  "text" : "açaí à la carte"
}
```

The filter produces the following tokens:

```text
[ acai, a, la, carte ]
```

```console-result
{
  "tokens" : [
    {
      "token" : "acai",
      "start_offset" : 0,
      "end_offset" : 4,
      "type" : "<ALPHANUM>",
      "position" : 0
    },
    {
      "token" : "a",
      "start_offset" : 5,
      "end_offset" : 6,
      "type" : "<ALPHANUM>",
      "position" : 1
    },
    {
      "token" : "la",
      "start_offset" : 7,
      "end_offset" : 9,
      "type" : "<ALPHANUM>",
      "position" : 2
    },
    {
      "token" : "carte",
      "start_offset" : 10,
      "end_offset" : 15,
      "type" : "<ALPHANUM>",
      "position" : 3
    }
  ]
}
```

#### Add to an analyzer

The following create index API request uses the
`asciifolding` filter to configure a new 
custom analyzer.

```console
PUT /asciifold_example
{
  "settings": {
    "analysis": {
      "analyzer": {
        "standard_asciifolding": {
          "tokenizer": "standard",
          "filter": [ "asciifolding" ]
        }
      }
    }
  }
}
```

#### Configurable parameters

`preserve_original`::
(Optional, Boolean)
If `true`, emit both original tokens and folded tokens.
Defaults to `false`.

#### Customize

To customize the `asciifolding` filter, duplicate it to create the basis
for a new custom token filter. You can modify the filter using its configurable
parameters.

For example, the following request creates a custom `asciifolding` filter with
`preserve_original` set to true:

```console
PUT /asciifold_example
{
  "settings": {
    "analysis": {
      "analyzer": {
        "standard_asciifolding": {
          "tokenizer": "standard",
          "filter": [ "my_ascii_folding" ]
        }
      },
      "filter": {
        "my_ascii_folding": {
          "type": "asciifolding",
          "preserve_original": true
        }
      }
    }
  }
}
```
