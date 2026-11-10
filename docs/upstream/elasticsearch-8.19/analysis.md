<!-- Converted from analysis.asciidoc (AsciiDoc). Includes are inlined. -->

# Text analysis

_Text analysis_ is the process of converting unstructured text, like
the body of an email or a product description, into a structured format that's optimized for search.

### When to configure text analysis

Elasticsearch performs text analysis when indexing or searching `text` fields.

If your index doesn't contain `text` fields, no further setup is needed; you can
skip the pages in this section.

However, if you use `text` fields or your text searches aren't returning results
as expected, configuring text analysis can often help. You should also look into
analysis configuration if you're using Elasticsearch to:

* Build a search engine
* Mine unstructured data
* Fine-tune search for a specific language
* Perform lexicographic or linguistic research

### In this section

* analysis-overview
* analysis-concepts
* configure-text-analysis
* analysis-analyzers
* analysis-tokenizers
* analysis-tokenfilters
* analysis-charfilters
* analysis-normalizers

(See `analysis/overview.md`)
(See `analysis/concepts.md`)
(See `analysis/configure-text-analysis.md`)
(See `analysis/analyzers.md`)
(See `analysis/tokenizers.md`)
(See `analysis/tokenfilters.md`)
(See `analysis/charfilters.md`)
(See `analysis/normalizers.md`)
