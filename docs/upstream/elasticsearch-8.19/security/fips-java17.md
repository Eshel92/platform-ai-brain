<!-- Converted from security/fips-java17.asciidoc (AsciiDoc). Includes are inlined. -->

Elasticsearch 8.0 requires Java 17 or later. Elasticsearch 8.13 has been tested with [Bouncy Castle](https://www.bouncycastle.org/java.html)'s Java 17
[certified](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4616) FIPS implementation and is the
recommended Java security provider when running Elasticsearch in FIPS 140-2 mode.
Note - Elasticsearch does not ship with a FIPS certified security provider and requires explicit installation and configuration.

Alternatively, consider using Elasticsearch Service in the
[FedRAMP-certified GovCloud region](https://www.elastic.co/industries/public-sector/fedramp).
