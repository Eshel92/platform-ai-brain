---
mapped_pages:
  - https://www.elastic.co/guide/en/elasticsearch/reference/current/sql-spec.html
navigation_title: SQL
---

# SQL overview [sql-overview]

Elasticsearch SQL aims to provide a powerful yet lightweight SQL interface to Elasticsearch.

## What's SQL in Elasticsearch? [sql-introduction]

Elasticsearch SQL is a feature that allows SQL-like queries to be executed in real-time against Elasticsearch. Whether using the REST interface, command-line or JDBC, any client can use SQL to search and aggregate data *natively* inside Elasticsearch. One can think of Elasticsearch SQL as a *translator*, one that understands both SQL and Elasticsearch and makes it easy to read and process data in real-time, at scale by leveraging Elasticsearch capabilities.

## Why Elasticsearch SQL ? [sql-why]

Native integration
:   Elasticsearch SQL is built from the ground up for Elasticsearch. Each and every query is efficiently executed against the relevant nodes according to the underlying storage.

No external parts
:   No need for additional hardware, processes, runtimes or libraries to query Elasticsearch; Elasticsearch SQL eliminates extra moving parts by running *inside* the Elasticsearch cluster.

Lightweight and efficient
:   Elasticsearch SQL does not abstract Elasticsearch and its search capabilities - on the contrary, it embraces and exposes SQL to allow proper full-text search, in real-time, in the same declarative, succinct fashion.

The following chapters aim to cover everything from usage, to syntax and drivers. Experienced users might want to jump directly to the list of SQL [commands](elasticsearch://reference/query-languages/sql/sql-commands.md) and [functions](elasticsearch://reference/query-languages/sql/sql-functions.md).

[Getting started](sql/sql-getting-started.md)
:   Start using SQL right away in Elasticsearch.

[Concepts and terminology](sql/sql-concepts.md)
:   Language conventions across SQL and Elasticsearch.

[Security](sql/sql-security.md)
:   Secure Elasticsearch SQL and Elasticsearch.

[REST API](sql/sql-rest.md)
:   Execute SQL in JSON format over REST.

[Translate API](sql/sql-translate.md)
:   Translate SQL in JSON format to Elasticsearch native query.

[JDBC](sql/sql-jdbc.md)
:   JDBC driver for Elasticsearch.

[ODBC](sql/sql-odbc.md)
:   ODBC driver for Elasticsearch.

[Client Applications](sql/sql-client-apps.md)
:   Setup various SQL/BI tools with Elasticsearch SQL.

[SQL Language](sql/sql-spec.md)
:   Overview of the Elasticsearch SQL language, such as supported data types, commands and syntax.

[Functions and Operators](sql/sql-functions.md)
:   List of functions and operators supported.

[Limitations](sql/sql-limitations.md)
:   Elasticsearch SQL current limitations.

