<!-- Converted from analysis/tokenizers/simplepatternsplit-tokenizer.asciidoc (AsciiDoc). Includes are inlined. -->

### Simple pattern split tokenizer

The `simple_pattern_split` tokenizer uses a regular expression to split the
input into terms at pattern matches. The set of regular expression features it
supports is more limited than the `pattern`
tokenizer, but the tokenization is generally faster.

This tokenizer does not produce terms from the matches themselves. To produce
terms from matches using patterns in the same restricted regular expression
subset, see the `simple_pattern`
tokenizer.

This tokenizer uses {lucene-core-javadoc}/org/apache/lucene/util/automaton/RegExp.html[Lucene regular expressions].
For an explanation of the supported features and syntax, see Regular Expression Syntax.

The default pattern is the empty string, which produces one term containing the
full input. This tokenizer should always be configured with a non-default
pattern.

### Configuration

The `simple_pattern_split` tokenizer accepts the following parameters:

`pattern`::
    A {lucene-core-javadoc}/org/apache/lucene/util/automaton/RegExp.html[Lucene regular expression], defaults to the empty string.

### Example configuration

This example configures the `simple_pattern_split` tokenizer to split the input
text on underscores.

```console
PUT my-index-000001
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_analyzer": {
          "tokenizer": "my_tokenizer"
        }
      },
      "tokenizer": {
        "my_tokenizer": {
          "type": "simple_pattern_split",
          "pattern": "_"
        }
      }
    }
  }
}

POST my-index-000001/_analyze
{
  "analyzer": "my_analyzer",
  "text": "an_underscored_phrase"
}
```

```console-result
{
  "tokens" : [
    {
      "token" : "an",
      "start_offset" : 0,
      "end_offset" : 2,
      "type" : "word",
      "position" : 0
    },
    {
      "token" : "underscored",
      "start_offset" : 3,
      "end_offset" : 14,
      "type" : "word",
      "position" : 1
    },
    {
      "token" : "phrase",
      "start_offset" : 15,
      "end_offset" : 21,
      "type" : "word",
      "position" : 2
    }
  ]
}
```

The above example produces these terms:

```text
[ an, underscored, phrase ]
```
