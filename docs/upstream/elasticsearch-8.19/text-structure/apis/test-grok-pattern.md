<!-- Converted from text-structure/apis/test-grok-pattern.asciidoc (AsciiDoc). Includes are inlined. -->

# Test Grok pattern API

**New API reference**
For the most up-to-date API details, refer to [Text structure APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-text_structure).

Tests a Grok pattern on lines of text, see also Grokking grok.

## Request

`GET _text_structure/test_grok_pattern` +

`POST _text_structure/test_grok_pattern` +

## Description

The test Grok pattern API allows you to execute a Grok pattern on one
or more lines of text. It returns whether the lines match the pattern
together with the offsets and lengths of the matched substrings.

## Query parameters

`ecs_compatibility`::
(Optional, string) The mode of compatibility with ECS compliant Grok patterns.
Use this parameter to specify whether to use ECS Grok patterns instead of
legacy ones when the structure finder creates a Grok pattern. Valid values
are `disabled` and `v1`. The default value is `disabled`.

## Request body

`grok_pattern`::
(Required, string)
The Grok pattern to run on the lines of text.

`text`::
(Required, array of strings)
The lines of text to run the Grok pattern on.

## Examples

```console
GET _text_structure/test_grok_pattern
{
  "grok_pattern": "Hello %{WORD:first_name} %{WORD:last_name}",
  "text": [
    "Hello John Doe",
    "this does not match"
  ]
}
```

The API returns the following response:

```console-result
{
  "matches": [
    {
      "matched": true,
      "fields": {
        "first_name": [
          {
            "match": "John",
            "offset": 6,
            "length": 4
          }
        ],
        "last_name": [
          {
            "match": "Doe",
            "offset": 11,
            "length": 3
          }
        ]
      }
    },
    {
      "matched": false
    }
  ]
}
```
