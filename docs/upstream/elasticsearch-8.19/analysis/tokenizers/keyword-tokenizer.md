<!-- Converted from analysis/tokenizers/keyword-tokenizer.asciidoc (AsciiDoc). Includes are inlined. -->

### Keyword tokenizer

The `keyword` tokenizer is a ``noop'' tokenizer that accepts whatever text it
is given and outputs the exact same text as a single term. It can be combined
with token filters to normalise output, e.g. lower-casing email addresses.

### Example output

```console
POST _analyze
{
  "tokenizer": "keyword",
  "text": "New York"
}
```

```console-result
{
  "tokens": [
    {
      "token": "New York",
      "start_offset": 0,
      "end_offset": 8,
      "type": "word",
      "position": 0
    }
  ]
}
```

The above sentence would produce the following term:

```text
[ New York ]
```

### Combine with token filters

You can combine the `keyword` tokenizer with token filters to normalise
structured data, such as product IDs or email addresses.

For example, the following analyze API request uses the
`keyword` tokenizer and `lowercase` filter to
convert an email address to lowercase.

```console
POST _analyze
{
  "tokenizer": "keyword",
  "filter": [ "lowercase" ],
  "text": "john.SMITH@example.COM"
}
```

```console-result
{
  "tokens": [
    {
      "token": "john.smith@example.com",
      "start_offset": 0,
      "end_offset": 22,
      "type": "word",
      "position": 0
    }
  ]
}
```

The request produces the following token:

```text
[ john.smith@example.com ]
```

### Configuration

The `keyword` tokenizer accepts the following parameters:

`buffer_size`::

    The number of characters read into the term buffer in a single pass.
    Defaults to `256`. The term buffer will grow by this size until all the
    text has been consumed. It is advisable not to change this setting.
