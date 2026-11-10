<!-- Converted from analysis/tokenfilters/_token-filter-template.asciidoc (AsciiDoc). Includes are inlined. -->

### Sample token filter

Does a cool thing. For example, the `sample` filter changes `x` to `y`.

The filter uses Lucene's
{lucene-analysis-docs}/sampleFilter.html[SampleFilter].

#### Example

The following analyze API request uses the `sample`
filter to do a cool thing to `the quick fox jumps the lazy dog`:

```console
GET /_analyze
{
  "tokenizer" : "standard",
  "filter" : ["sample"],
  "text" : "the quick fox jumps the lazy dog"
}
```

The filter produces the following tokens:

```text
[ the, quick, fox, jumps, the, lazy, dog ]
```

#### Add to an analyzer

The following create index API request uses the
`sample` filter to configure a new custom analyzer.

```console
PUT sample_example
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_sample_analyzer": {
          "tokenizer": "standard",
          "filter": [ "sample" ]
        }
      }
    }
  }
}
```

#### Configurable parameters

`foo`::
(Optional, Boolean)
If `true`, do a cool thing.
Defaults to `false`.

`baz`::
(Optional, string)
Path to another cool thing.

#### Customize

To customize the `sample` filter, duplicate it to create the basis
for a new custom token filter. You can modify the filter using its configurable
parameters.

For example, the following request creates a custom `sample` filter with
`foo` set to `true`:

```console
PUT sample_example
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_custom_analyzer": {
          "tokenizer": "whitespace",
          "filter": [ "my_custom_sample_token_filter" ]
        }
      },
      "filter": {
        "my_custom_sample_token_filter": {
          "type": "sample",
          "foo": true
        }
      }
    }
  }
}
```
