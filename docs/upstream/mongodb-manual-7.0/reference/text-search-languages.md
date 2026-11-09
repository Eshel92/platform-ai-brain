<!-- Converted from reference/text-search-languages.txt (reStructuredText). Includes are inlined. -->

# Text Search Languages on Self-Managed Deployments

**Note:**

This page describes text query capabilities for self-managed
(non-Atlas) deployments. For data hosted on MongoDB Atlas, MongoDB
offers an improved full-text query solution, Atlas Search and a vector search solution, Atlas Vector Search. 

The text index and the `$text`
operator may be used with the following languages, and accepts either the
two-letter ISO 639-1 language code or the long form of the
language name:

| Language Name | ISO 639-1 (Two letter codes) |
|---|---|
| `danish` | `da` |
| `dutch` | `nl` |
| `english` | `en` |
| `finnish` | `fi` |
| `french` | `fr` |
| `german` | `de` |
| `hungarian` | `hu` |
| `italian` | `it` |
| `norwegian` | `nb` |
| `portuguese` | `pt` |
| `romanian` | `ro` |
| `russian` | `ru` |
| `spanish` | `es` |
| `swedish` | `sv` |
| `turkish` | `tr` |

If you specify a `default_language` value of `none`, the text index
parses through each word in the field, including stop words, and ignores
suffix stemming.

**See also:**

/core/indexes/index-types/index-text/specify-text-index-language
