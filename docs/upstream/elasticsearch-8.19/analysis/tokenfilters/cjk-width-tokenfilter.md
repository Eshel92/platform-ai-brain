<!-- Converted from analysis/tokenfilters/cjk-width-tokenfilter.asciidoc (AsciiDoc). Includes are inlined. -->

### CJK width token filter

Normalizes width differences in CJK (Chinese, Japanese, and Korean) characters
as follows:

* Folds full-width ASCII character variants into the equivalent basic Latin
characters
* Folds half-width Katakana character variants into the equivalent Kana
characters

This filter is included in Elasticsearch's built-in <<cjk-analyzer,CJK language
analyzer>>. It uses Lucene's
{lucene-analysis-docs}/cjk/CJKWidthFilter.html[CJKWidthFilter].

**Note:** This token filter can be viewed as a subset of NFKC/NFKD Unicode
normalization. See the
{plugins}/analysis-icu-normalization-charfilter.html[`analysis-icu` plugin] for
full normalization support.

#### Example

```console
GET /_analyze
{
  "tokenizer" : "standard",
  "filter" : ["cjk_width"],
  "text" : "ｼｰｻｲﾄﾞﾗｲﾅｰ"
}
```

The filter produces the following token:

```text
シーサイドライナー
```

```console-result
{
  "tokens" : [
    {
      "token" : "シーサイドライナー",
      "start_offset" : 0,
      "end_offset" : 10,
      "type" : "<KATAKANA>",
      "position" : 0
    }
  ]
}
```

#### Add to an analyzer

The following create index API request uses the
CJK width token filter to configure a new 
custom analyzer.

```console
PUT /cjk_width_example
{
  "settings": {
    "analysis": {
      "analyzer": {
        "standard_cjk_width": {
          "tokenizer": "standard",
          "filter": [ "cjk_width" ]
        }
      }
    }
  }
}
```
