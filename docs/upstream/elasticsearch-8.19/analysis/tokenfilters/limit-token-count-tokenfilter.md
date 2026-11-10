<!-- Converted from analysis/tokenfilters/limit-token-count-tokenfilter.asciidoc (AsciiDoc). Includes are inlined. -->

### Limit token count token filter

Limits the number of output tokens. The `limit` filter is commonly used to limit
the size of document field values based on token count.

By default, the `limit` filter keeps only the first token in a stream. For
example, the filter can change the token stream `[ one, two, three ]` to 
`[ one ]`.

This filter uses Lucene's
{lucene-analysis-docs}/miscellaneous/LimitTokenCountFilter.html[LimitTokenCountFilter].

**Tip:**
 If you want to limit the size of field values based on
_character length_, use the `ignore_above` mapping parameter.

#### Configurable parameters

`max_token_count`::
(Optional, integer)
Maximum number of tokens to keep. Once this limit is reached, any remaining
tokens are excluded from the output. Defaults to `1`.

`consume_all_tokens`::
(Optional, Boolean)
If `true`, the `limit` filter exhausts the token stream, even if the
`max_token_count` has already been reached. Defaults to `false`.

#### Example

The following analyze API request uses the `limit`
filter to keep only the first two tokens in `quick fox jumps over lazy dog`:

```console
GET _analyze
{
  "tokenizer": "standard",
    "filter": [
    {
      "type": "limit",
      "max_token_count": 2
    }
  ],
  "text": "quick fox jumps over lazy dog"
}
```

The filter produces the following tokens:

```text
[ quick, fox ]
```

```console-result
{
  "tokens": [
    {
      "token": "quick",
      "start_offset": 0,
      "end_offset": 5,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "fox",
      "start_offset": 6,
      "end_offset": 9,
      "type": "<ALPHANUM>",
      "position": 1
    }
  ]
}
```

#### Add to an analyzer

The following create index API request uses the
`limit` filter to configure a new 
custom analyzer.

```console
PUT limit_example
{
  "settings": {
    "analysis": {
      "analyzer": {
        "standard_one_token_limit": {
          "tokenizer": "standard",
          "filter": [ "limit" ]
        }
      }
    }
  }
}
```

#### Customize

To customize the `limit` filter, duplicate it to create the basis
for a new custom token filter. You can modify the filter using its configurable
parameters.

For example, the following request creates a custom `limit` filter that keeps
only the first five tokens of a stream:

```console
PUT custom_limit_example
{
  "settings": {
    "analysis": {
      "analyzer": {
        "whitespace_five_token_limit": {
          "tokenizer": "whitespace",
          "filter": [ "five_token_limit" ]
        }
      },
      "filter": {
        "five_token_limit": {
          "type": "limit",
          "max_token_count": 5
        }
      }
    }
  }
}
```
