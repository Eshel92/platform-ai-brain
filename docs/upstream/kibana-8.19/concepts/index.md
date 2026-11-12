<!-- Converted from concepts/index.asciidoc (AsciiDoc). Includes are inlined. -->

## Kibana concepts

**_Learn the shared concepts for analyzing and visualizing your data_**

As an analyst, you will use a combination of Kibana apps to analyze and
visualize your data. Kibana contains both general-purpose apps and apps for the
[*Enterprise Search*](https://www.elastic.co/guide/en/enterprise-search/current/index.html),
{observability-guide}/observability-introduction.html[*Elastic Observability*],
and {security-guide}/es-overview.html[*Elastic Security*] solutions.
These apps share a common set of concepts.

### Three things to know about Elasticsearch

You don't need to know everything about Elasticsearch to use Kibana, but the most important concepts follow:

* *Elasticsearch makes JSON documents searchable and aggregatable.* The documents are
stored in an [index](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/documents-indices.html) or [data stream](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/data-streams.html), which represent one type of data.

* **_Searchable_ means that you can filter the documents for conditions.**
For example, you can filter for data "within the last 7 days" or data that "contains the word Kibana".
Kibana provides many ways for you to construct filters, which are also called queries or search terms.

* **_Aggregatable_ means that you can extract summaries from matching documents.**
The simplest aggregation is *count*, and it is frequently used in combination
with the *date histogram*, to see count over time. The *terms* aggregation shows the most frequent values.

### Finding your apps and objects

Kibana offers a global search bar on every page that you can use to find any app or saved object.
Open the search bar using the keyboard shortcut Ctrl/ on Windows and Linux, Command/ on MacOS.

image:concepts/images/global-search.png["Global search showing matches to apps and saved objects for the word visualize"]

### Accessing data with data views

Kibana requires a data view to tell it which Elasticsearch data you want to access,
and whether the data is time-based. A data view can point to one or more Elasticsearch
data streams, indices, or index aliases by name.

Data views are typically created by an administrator when sending data to Elasticsearch.
You can create or update data views in *Stack Management*, or by using a script
that accesses the Kibana API.

Kibana uses the data view to show you a list of fields, such as
`event.duration`. You can customize the display name and format for each field.
For example, you can tell Kibana to display `event.duration` in seconds.
Kibana has field formatters for strings,
dates, geopoints, and numbers.

### Searching your data

Kibana provides you several ways to build search queries,
which will reduce the number of document matches that you get from Elasticsearch.
Kibana apps provide a time filter, and most apps also include semi-structured search and extra filters.

image:concepts/images/top-bar.png["Time filter, semi-structured search, and filters in a Kibana app"]

If you frequently use any of the search options, click
image:concepts/images/saved-query-icon.png["save icon", width=20px] next to the
semi-structured search to save or load a previously saved query.
The saved query always contains the semi-structured search query,
and optionally the time filter and extra filters.

#### Time filter

The global time filter limits the time range of data displayed.
In most cases, the time filter applies to the time field in the data view,
but some apps allow you to use a different time field.

Using the time filter, you can configure a refresh rate to periodically
resubmit your searches.

image:concepts/images/refresh-every.png["section of time filter where you can configure a refresh rate", width=75%]

To manually resubmit a search, click the *Refresh* button.
This is useful when you use Kibana to view the underlying data.

#### Semi-structured search

Combine free text search with field-based search using the Kibana Query Language (KQL).
Type a search term to match across all fields, or start typing a field name to
get suggestions for field names and operators that you can use to build a structured query.
The semi-structured search will filter documents for matches, and only return matching documents.

Following are some example KQL queries.  For more detailed examples, refer to Kibana Query Language.

|===
| Exact phrase query
| `http.response.body.content.text:"quick brown fox"`

| Terms query
| http.response.status_code:400 401 404

| Boolean query
| `response:200 or extension:php`

| Range query
| `account_number >= 100 and items_sold <= 200`

| Wildcard query
| `machine.os:win*`
|===

#### Additional filters with AND

Structured filters are a more interactive way to create Elasticsearch queries,
and are commonly used when building dashboards that are shared by multiple analysts.
Each filter can be disabled, inverted, or pinned across all apps.
Each of the structured
filters is combined with AND logic on the rest of the query.

image:concepts/images/add-filter-popup.png["Add filter popup"]

### Saving objects

Kibana lets you save objects for your own future use or for sharing with others.
Each saved object type has different abilities. For example, you can save
your search queries made with *Discover*, which lets you:

* Share a link to your search
* Download the full search results in CSV form
* Start an aggregated visualization using the same search query
* Embed the *Discover* search results into a dashboard
* Embed the *Discover* search results into a Canvas workpad

For organization, every saved object can have a name, tags, and type.
Use the global search to quickly open a saved object.

### What's next?

* Try the Kibana Quick start, which shows you how to put these concepts into action.
* Go to Discover for instructions on searching your data.

(See `concepts/data-views.md`)
(See `concepts/set-time-filter.md`)
(See `concepts/esql.md`)
(See `concepts/kuery.md`)
(See `concepts/lucene.md`)
(See `concepts/save-query.md`)
