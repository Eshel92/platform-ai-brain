<!-- Converted from analysis/configure-text-analysis.asciidoc (AsciiDoc). Includes are inlined. -->

## Configure text analysis

By default, Elasticsearch uses the `standard` analyzer for
all text analysis. The `standard` analyzer gives you out-of-the-box support for
most natural languages and use cases. If you chose to use the `standard`
analyzer as-is, no further configuration is needed.

If the standard analyzer does not fit your needs, review and test Elasticsearch's other
built-in built-in analyzers. Built-in analyzers don't
require configuration, but some support options that can be used to adjust their
behavior. For example, you can configure the `standard` analyzer with a list of
custom stop words to remove.

If no built-in analyzer fits your needs, you can test and create a custom
analyzer. Custom analyzers involve selecting and combining different
analyzer components, giving you greater control over
the process.

* test-analyzer
* configuring-analyzers
* analysis-custom-analyzer
* specify-analyzer

(See `analysis/testing.md`)
(See `analysis/analyzers/configuring.md`)
(See `analysis/analyzers/custom-analyzer.md`)
(See `analysis/specify-analyzer.md`)
