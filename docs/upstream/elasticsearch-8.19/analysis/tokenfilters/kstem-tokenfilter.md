<!-- Converted from analysis/tokenfilters/kstem-tokenfilter.asciidoc (AsciiDoc). Includes are inlined. -->

### KStem token filter

Provides [KStem](https://ciir.cs.umass.edu/pubfiles/ir-35.pdf)-based stemming for
the English language. The `kstem` filter combines
algorithmic stemming with a built-in
dictionary.

The `kstem` filter tends to stem less aggressively than other English stemmer
filters, such as the `porter_stem` filter.

The `kstem` filter is equivalent to the
`stemmer` filter's
`light_english` variant.

This filter uses Lucene's
{lucene-analysis-docs}/en/KStemFilter.html[KStemFilter].

#### Example

The following analyze API request uses the `kstem` filter to stem `the foxes
jumping quickly` to `the fox jump quick`:

```console
GET /_analyze
{
  "tokenizer": "standard",
  "filter": [ "kstem" ],
  "text": "the foxes jumping quickly"
}
```

The filter produces the following tokens:

```text
[ the, fox, jump, quick ]
```

#### Add to an analyzer

The following create index API request uses the
`kstem` filter to configure a new <<analysis-custom-analyzer,custom
analyzer>>.

**Important:**
To work properly, the `kstem` filter requires lowercase tokens. To ensure tokens
are lowercased, add the `lowercase` filter
before the `kstem` filter in the analyzer configuration.

```console
PUT /my-index-000001
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_analyzer": {
          "tokenizer": "whitespace",
          "filter": [
            "lowercase",
            "kstem"
          ]
        }
      }
    }
  }
}
```
