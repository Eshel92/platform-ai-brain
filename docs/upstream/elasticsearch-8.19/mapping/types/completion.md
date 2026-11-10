<!-- Converted from mapping/types/completion.asciidoc (AsciiDoc). Includes are inlined. -->

### Completion field type

To use the `completion` suggester, map the field from
which you want to generate suggestions as type `completion`. This indexes the 
field values for fast completions.

```console
PUT music
{
  "mappings": {
    "properties": {
      "suggest": {
        "type": "completion"
      }
    }
  }
}
```

#### Parameters for `completion` fields

The following parameters are accepted by `completion` fields:

`analyzer`::

    The index analyzer to use, defaults to `simple`.

`search_analyzer`::

    The search analyzer to use, defaults to value of `analyzer`.

`preserve_separators`::

    Preserves the separators, defaults to `true`.
    If disabled, you could find a field starting with `Foo Fighters`, if you
    suggest for `foof`.

`preserve_position_increments`::

    Enables position increments, defaults to `true`.
    If disabled and using stopwords analyzer, you could get a
    field starting with `The Beatles`, if you suggest for `b`. *Note*: You
    could also achieve this by indexing two inputs, `Beatles` and
    `The Beatles`, no need to change a simple analyzer, if you are able to
    enrich your data.

`max_input_length`::

    Limits the length of a single input, defaults to `50` UTF-16 code points.
    This limit is only used at index time to reduce the total number of
    characters per input string in order to prevent massive inputs from
    bloating the underlying datastructure. Most use cases won't be influenced
    by the default value since prefix completions seldom grow beyond prefixes longer
    than a handful of characters.
