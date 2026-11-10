<!-- Converted from analysis/tokenfilters/apostrophe-tokenfilter.asciidoc (AsciiDoc). Includes are inlined. -->

### Apostrophe token filter

Strips all characters after an apostrophe, including the apostrophe itself.

This filter is included in Elasticsearch's built-in <<turkish-analyzer,Turkish language
analyzer>>. It uses Lucene's
{lucene-analysis-docs}/tr/ApostropheFilter.html[ApostropheFilter], which was
built for the Turkish language.

#### Example

The following analyze API request demonstrates how the
apostrophe token filter works.

```console
GET /_analyze
{
  "tokenizer" : "standard",
  "filter" : ["apostrophe"],
  "text" : "Istanbul'a veya Istanbul'dan"
}
```

The filter produces the following tokens:

```text
[ Istanbul, veya, Istanbul ]
```

```console-result
{
  "tokens" : [
    {
      "token" : "Istanbul",
      "start_offset" : 0,
      "end_offset" : 10,
      "type" : "<ALPHANUM>",
      "position" : 0
    },
    {
      "token" : "veya",
      "start_offset" : 11,
      "end_offset" : 15,
      "type" : "<ALPHANUM>",
      "position" : 1
    },
    {
      "token" : "Istanbul",
      "start_offset" : 16,
      "end_offset" : 28,
      "type" : "<ALPHANUM>",
      "position" : 2
    }
  ]
}
```

#### Add to an analyzer

The following create index API request uses the
apostrophe token filter to configure a new 
custom analyzer.

```console
PUT /apostrophe_example
{
  "settings": {
    "analysis": {
      "analyzer": {
        "standard_apostrophe": {
          "tokenizer": "standard",
          "filter": [ "apostrophe" ]
        }
      }
    }
  }
}
```
