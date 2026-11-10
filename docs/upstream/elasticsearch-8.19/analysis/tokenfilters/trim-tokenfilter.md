<!-- Converted from analysis/tokenfilters/trim-tokenfilter.asciidoc (AsciiDoc). Includes are inlined. -->

### Trim token filter

Removes leading and trailing whitespace from each token in a stream. While this
can change the length of a token, the `trim` filter does _not_ change a token's
offsets.

The `trim` filter uses Lucene's
[TrimFilter](https://lucene.apache.org/core/{lucene_version_path}/analysis/common/org/apache/lucene/analysis/miscellaneous/TrimFilter.html).

**Tip:**
Many commonly used tokenizers, such as the
`standard` or
`whitespace` tokenizer, remove whitespace by
default. When using these tokenizers, you don't need to add a separate `trim`
filter.

#### Example

To see how the `trim` filter works, you first need to produce a token
containing whitespace.

The following analyze API request uses the
`keyword` tokenizer to produce a token for 
`" fox "`.

```console
GET _analyze
{
  "tokenizer" : "keyword",
  "text" : " fox "
}
```

The API returns the following response. Note the `" fox "` token contains the
original text's whitespace. Note that despite changing the token's length, the
`start_offset` and `end_offset` remain the same.

```console-result
{
  "tokens": [
    {
      "token": " fox ",
      "start_offset": 0,
      "end_offset": 5,
      "type": "word",
      "position": 0
    }
  ]
}
```

To remove the whitespace, add the `trim` filter to the previous analyze API
request.

```console
GET _analyze
{
  "tokenizer" : "keyword",
  "filter" : ["trim"],
  "text" : " fox "
}
```

The API returns the following response. The returned `fox` token does not
include any leading or trailing whitespace.

```console-result
{
  "tokens": [
    {
      "token": "fox",
      "start_offset": 0,
      "end_offset": 5,
      "type": "word",
      "position": 0
    }
  ]
}
```

#### Add to an analyzer

The following create index API request uses the `trim`
filter to configure a new custom analyzer.

```console
PUT trim_example
{
  "settings": {
    "analysis": {
      "analyzer": {
        "keyword_trim": {
          "tokenizer": "keyword",
          "filter": [ "trim" ]
        }
      }
    }
  }
}
```
