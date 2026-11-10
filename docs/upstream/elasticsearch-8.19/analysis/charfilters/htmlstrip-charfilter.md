<!-- Converted from analysis/charfilters/htmlstrip-charfilter.asciidoc (AsciiDoc). Includes are inlined. -->

### HTML strip character filter

Strips HTML elements from a text and replaces HTML entities with their decoded
value (e.g, replaces `&amp;` with `&`).

The `html_strip` filter uses Lucene's
{lucene-analysis-docs}/charfilter/HTMLStripCharFilter.html[HTMLStripCharFilter].

#### Example

The following analyze API request uses the
`html_strip` filter to change the text `<p>I&apos;m so <b>happy</b>!</p>` to
`\nI'm so happy!\n`.

```console
GET /_analyze
{
  "tokenizer": "keyword",
  "char_filter": [
    "html_strip"
  ],
  "text": "<p>I&apos;m so <b>happy</b>!</p>"
}
```

The filter produces the following text:

```text
[ \nI'm so happy!\n ]
```

#### Add to an analyzer

The following create index API request uses the
`html_strip` filter to configure a new
custom analyzer.

```console
PUT /my-index-000001
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_analyzer": {
          "tokenizer": "keyword",
          "char_filter": [
            "html_strip"
          ]
        }
      }
    }
  }
}
```

#### Configurable parameters

`escaped_tags`::
(Optional, array of strings)
Array of HTML elements without enclosing angle brackets (`< >`). The filter
skips these HTML elements when stripping HTML from the text. For example, a
value of `[ "p" ]` skips the `<p>` HTML element.

#### Customize

To customize the `html_strip` filter, duplicate it to create the basis for a new
custom character filter. You can modify the filter using its configurable
parameters.

The following create index API request
configures a new custom analyzer using a custom
`html_strip` filter, `my_custom_html_strip_char_filter`.

The `my_custom_html_strip_char_filter` filter skips the removal of the `<b>`
HTML element.

```console
PUT my-index-000001
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_analyzer": {
          "tokenizer": "keyword",
          "char_filter": [
            "my_custom_html_strip_char_filter"
          ]
        }
      },
      "char_filter": {
        "my_custom_html_strip_char_filter": {
          "type": "html_strip",
          "escaped_tags": [
            "b"
          ]
        }
      }
    }
  }
}
```
