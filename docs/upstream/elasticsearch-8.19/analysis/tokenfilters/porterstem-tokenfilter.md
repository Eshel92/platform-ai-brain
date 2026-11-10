<!-- Converted from analysis/tokenfilters/porterstem-tokenfilter.asciidoc (AsciiDoc). Includes are inlined. -->

### Porter stem token filter

Provides algorithmic stemming for the English language,
based on the https://snowballstem.org/algorithms/porter/stemmer.html[Porter
stemming algorithm].

This filter tends to stem more aggressively than other English
stemmer filters, such as the `kstem` filter.

The `porter_stem` filter is equivalent to the
`stemmer` filter's
`english` variant.

The `porter_stem` filter uses Lucene's
{lucene-analysis-docs}/en/PorterStemFilter.html[PorterStemFilter].

#### Example

The following analyze API request uses the `porter_stem` filter to stem
`the foxes jumping quickly` to `the fox jump quickli`:

```console
GET /_analyze
{
  "tokenizer": "standard",
  "filter": [ "porter_stem" ],
  "text": "the foxes jumping quickly"
}
```

The filter produces the following tokens:

```text
[ the, fox, jump, quickli ]
```

#### Add to an analyzer

The following create index API request uses the
`porter_stem` filter to configure a new <<analysis-custom-analyzer,custom
analyzer>>.

**Important:**
To work properly, the `porter_stem` filter requires lowercase tokens. To ensure
tokens are lowercased, add the `lowercase`
filter before the `porter_stem` filter in the analyzer configuration.

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
            "porter_stem"
          ]
        }
      }
    }
  }
}
```
