<!-- Converted from analysis/analyzers/simple-analyzer.asciidoc (AsciiDoc). Includes are inlined. -->

### Simple analyzer

The `simple` analyzer breaks text into tokens at any non-letter character, such
as numbers, spaces, hyphens and apostrophes, discards non-letter characters, 
and changes uppercase to lowercase.

#### Example

```console
POST _analyze
{
  "analyzer": "simple",
  "text": "The 2 QUICK Brown-Foxes jumped over the lazy dog's bone."
}
```

The `simple` analyzer parses the sentence and produces the following 
tokens: 

```text
[ the, quick, brown, foxes, jumped, over, the, lazy, dog, s, bone ]
```

#### Definition

The `simple` analyzer is defined by one tokenizer:

Tokenizer::
* Lowercase Tokenizer

#### Customize

To customize the `simple` analyzer, duplicate it to create the basis for 
a custom analyzer. This custom analyzer can be modified as required, usually by 
adding token filters.

```console
PUT /my-index-000001
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_custom_simple_analyzer": {
          "tokenizer": "lowercase",
          "filter": [                          <1>
          ]
        }
      }
    }
  }
}
```
<1> Add token filters here.
