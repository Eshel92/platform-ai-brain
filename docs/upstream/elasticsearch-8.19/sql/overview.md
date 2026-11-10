<!-- Converted from sql/overview.asciidoc (AsciiDoc). Includes are inlined. -->

## Overview

{es-sql} aims to provide a powerful yet lightweight SQL interface to Elasticsearch.

### Introduction

{es-sql} is a feature that allows SQL-like queries to be executed in real-time against Elasticsearch.
Whether using the REST interface, command-line or JDBC, any client can use SQL to search and aggregate data
_natively_ inside Elasticsearch.
One can think of {es-sql} as a _translator_, one that understands both SQL and Elasticsearch and makes it easy to read and process data in real-time, at scale by leveraging Elasticsearch capabilities.

### Why {es-sql} ?

Native integration::

{es-sql} is built from the ground up for Elasticsearch. Each and every query is efficiently executed against the relevant nodes according to the underlying storage.

No external parts::

No need for additional hardware, processes, runtimes or libraries to query Elasticsearch; {es-sql} eliminates extra moving parts by running _inside_ the Elasticsearch cluster.

Lightweight and efficient::

{es-sql} does not abstract Elasticsearch and its search capabilities - on the contrary, it embraces and exposes SQL to allow proper full-text search, in real-time, in the same declarative, succinct fashion.
