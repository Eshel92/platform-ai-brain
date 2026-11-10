<!-- Converted from analysis/analyzers/keyword-analyzer.asciidoc (AsciiDoc). Includes are inlined. -->

### Keyword analyzer

The `keyword` analyzer is a ``noop'' analyzer which returns the entire input
string as a single token.

### Example output

```console
POST _analyze
{
  "analyzer": "keyword",
  "text": "The 2 QUICK Brown-Foxes jumped over the lazy dog's bone."
}
```

```console-result
{
  "tokens": [
    {
      "token": "The 2 QUICK Brown-Foxes jumped over the lazy dog's bone.",
      "start_offset": 0,
      "end_offset": 56,
      "type": "word",
      "position": 0
    }
  ]
}
```

The above sentence would produce the following single term:

```text
[ The 2 QUICK Brown-Foxes jumped over the lazy dog's bone. ]
```

### Configuration

The `keyword` analyzer is not configurable.

### Definition

The `keyword` analyzer consists of:

Tokenizer::
* Keyword Tokenizer

If you need to customize the `keyword` analyzer then you need to
recreate it as a `custom` analyzer and modify it, usually by adding
token filters. Usually, you should prefer the
Keyword type when you want strings that are not split
into tokens, but just in case you need it, this would recreate the
built-in `keyword` analyzer and you can use it as a starting point
for further customization:

```console
PUT /keyword_example
{
  "settings": {
    "analysis": {
      "analyzer": {
        "rebuilt_keyword": {
          "tokenizer": "keyword",
          "filter": [         <1>
          ]
        }
      }
    }
  }
}
```

<1> You'd add any token filters here.
