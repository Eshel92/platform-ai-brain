<!-- Converted from tab-widgets/esql/esql-getting-started-discover-console.asciidoc (AsciiDoc). Includes are inlined. -->

To get started with ES|QL in Console, open the main menu and select
*Dev Tools*.

The general structure of an ES|QL query API request is:

```txt
POST /_query?format=txt
{
  "query": """

  """
}
```

Enter the actual ES|QL query between the two sets of triple quotes. For
example:

```txt
POST /_query?format=txt
{
  "query": """
FROM kibana_sample_data_logs
  """
}
```

Inside quotes, Console suggests possible commands and functions to autocomplete your query:

(Figure: images/esql/console-esql-autocomplete.png)

To get started with ES|QL in Discover, open the main menu and select
*Discover*. Next, select *Try ES|QL* from the application menu bar.
Adjust the time filter so it includes the timestamps in the sample data (October
23rd, 2023).

After switching to ES|QL mode, the query bar shows a sample query. You can
replace this query with the queries in this getting started guide.

Discover suggests possible commands and functions to autocomplete your query:

(Figure: images/esql/esql-kibana-auto-complete.png)
You can adjust the editor's height by dragging its bottom border to your liking.
