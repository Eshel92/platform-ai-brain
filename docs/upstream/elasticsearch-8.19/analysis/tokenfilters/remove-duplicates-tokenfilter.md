<!-- Converted from analysis/tokenfilters/remove-duplicates-tokenfilter.asciidoc (AsciiDoc). Includes are inlined. -->

### Remove duplicates token filter

Removes duplicate tokens in the same position.

The `remove_duplicates` filter uses Lucene's
{lucene-analysis-docs}/miscellaneous/RemoveDuplicatesTokenFilter.html[RemoveDuplicatesTokenFilter].

#### Example

To see how the `remove_duplicates` filter works, you first need to produce a
token stream containing duplicate tokens in the same position.

The following analyze API request uses the
`keyword_repeat` and
`stemmer` filters to create stemmed and
unstemmed tokens for `jumping dog`.

```console
GET _analyze
{
  "tokenizer": "whitespace",
  "filter": [
    "keyword_repeat",
    "stemmer"
  ],
  "text": "jumping dog"
}
```

The API returns the following response. Note that the `dog` token in position
`1` is duplicated.

```console-result
{
  "tokens": [
    {
      "token": "jumping",
      "start_offset": 0,
      "end_offset": 7,
      "type": "word",
      "position": 0
    },
    {
      "token": "jump",
      "start_offset": 0,
      "end_offset": 7,
      "type": "word",
      "position": 0
    },
    {
      "token": "dog",
      "start_offset": 8,
      "end_offset": 11,
      "type": "word",
      "position": 1
    },
    {
      "token": "dog",
      "start_offset": 8,
      "end_offset": 11,
      "type": "word",
      "position": 1
    }
  ]
}
```

To remove one of the duplicate `dog` tokens, add the `remove_duplicates` filter
to the previous analyze API request.

```console
GET _analyze
{
  "tokenizer": "whitespace",
  "filter": [
    "keyword_repeat",
    "stemmer",
    "remove_duplicates"
  ],
  "text": "jumping dog"
}
```

The API returns the following response. There is now only one `dog` token in
position `1`.

```console-result
{
  "tokens": [
    {
      "token": "jumping",
      "start_offset": 0,
      "end_offset": 7,
      "type": "word",
      "position": 0
    },
    {
      "token": "jump",
      "start_offset": 0,
      "end_offset": 7,
      "type": "word",
      "position": 0
    },
    {
      "token": "dog",
      "start_offset": 8,
      "end_offset": 11,
      "type": "word",
      "position": 1
    }
  ]
}
```

#### Add to an analyzer

The following create index API request uses the
`remove_duplicates` filter to configure a new <<analysis-custom-analyzer,custom
analyzer>>.

This custom analyzer uses the `keyword_repeat` and `stemmer` filters to create a
stemmed and unstemmed version of each token in a stream. The `remove_duplicates`
filter then removes any duplicate tokens in the same position.

```console
PUT my-index-000001
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_custom_analyzer": {
          "tokenizer": "standard",
          "filter": [
            "keyword_repeat",
            "stemmer",
            "remove_duplicates"
          ]
        }
      }
    }
  }
}
```
