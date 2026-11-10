<!-- Converted from discover/get-started-discover.asciidoc (AsciiDoc). Includes are inlined. -->

## Explore fields and data with Discover

Learn how to use *Discover* to:

- **Select** and **filter** your Elasticsearch data.
- **Explore** the fields and content of your data in depth.
- **Present** your findings in a visualization.

*Prerequisites:*

- If you don’t already have Kibana, [start a free trial](https://www.elastic.co/cloud/elasticsearch-service/signup?baymax=docs-body&elektra=docs) on Elastic Cloud.
- You must have data in Elasticsearch. Examples on this page use the
ecommerce sample data set, but you can use your own data.
- You should have an understanding of [Elasticsearch documents and indices](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/documents-indices.html)
and Kibana concepts.

### Load data into Discover

Select the data you want to explore, and then specify the time range in which to view that data.

. Find **Discover** in the navigation menu or by using the global search field.

. Select the data view that contains the data you want to explore.
**Tip:** Kibana requires a {data-source} to access your Elasticsearch data. A {data-source} can point to one or more indices, [data streams](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/data-streams.html), or [index aliases](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/alias.html). When adding data to Elasticsearch using one of the many integrations available, sometimes data views are created automatically, but you can also create your own.
If you're using sample data, data views are automatically created and are ready to use.
(Figure: images/discover-data-view.png)

. If needed, adjust the time range, for example by setting it to the *Last 7 days*.
The range selection is based on the default time field in your data view.
If you are using the sample data, this value was set when the data view was created.
If you are using your own data view, and it does not have a time field, the range selection is not available.

**Discover** is populated with your data and you can view various areas with different information:

* All fields detected are listed in a dedicated panel.
* A chart allows you to visualize your data. 
* A table displays the results of your search.
By default, the table includes a column for the time field and a *Summary* column with an overview of each result.
You can modify the document table to display your fields of interest.

You can later filter the data that shows in the chart and in the table by specifying a query and changing the time range.

### Explore the fields in your data

**Discover** provides utilities designed to help you make sense of your data:

. In the sidebar, check the available fields. It's very common to have hundreds of fields. Use the search at the top of that sidebar to look for specific terms in the field names.
In this example, we've entered `ma` in the search field to find the `manufacturer` field.
image:images/discover-sidebar-available-fields.png[Fields list that displays the top five search results, width=40%]
**Tip:** You can combine multiple keywords or characters. For example, `geo dest` finds `geo.dest` and `geo.src.dest`.

. Select a field to view its most frequent values.
**Discover** shows the top 10 values and the number of records used to calculate those values.

. Select the *Plus* icon to add fields to the results table.
You can also drag them from the list into the table.
(Figure: images/discover-add-icon.png)
When you add fields to the table, the **Summary** column is replaced.
image:images/document-table.png[Document table with fields for manufacturer, customer_first_name, and customer_last_name]

. Arrange the view to your liking to display the fields and data you care most about using the various display options of **Discover**. For example, you can change the order and size of columns, expand the table to be in full screen or collapse the chart and the list of fields. Check Customize the Discover view.

. **Save** your changes to be able to open the same view later on and explore your data further.

#### Add a field to your {data-source}

What happens if you forgot to define an important value as a separate field? Or, what if you
want to combine two fields and treat them as one? This is where [runtime fields](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/runtime.html) come into play.
You can add a runtime field to your {data-source} from inside of **Discover**,
and then use that field for analysis and visualizations,
the same way you do with other fields.

. In the sidebar, select *Add a field*.

. Select the **Type** of the new field.

. **Name** the field. Name it in a way that corresponds to the way other fields of the data view are named.
You can set a custom label and description for the field to make it more recognizable in your data view. 

. Define the value that you want the field to show. By default, the field value is retrieved from the source data if it already contains a field with the same name. You can customize this with the following options:

** **Set value**: Define a script that will determine the value to show for the field. For more information on adding fields and Painless scripting language examples,
refer to Explore your data with runtime fields.
** **Set format**: Set your preferred format for displaying the value. Changing the format can affect the value and prevent highlighting in Discover.

. In the advanced settings, you can adjust the field popularity to make it appear higher or lower in the fields list. By default, Discover orders popular fields from most selected to least selected.

. **Save** your new field.

You can now find it in the list of fields and add it to the table.

In the following example, we're adding 2 fields: A simple "Hello world" field, and a second field that combines and transforms the `customer_first_name` and `customer_last_name` fields of the sample data into a single "customer" field:

**Hello world field example**:

* **Name**: `hello`
* **Type**: `Keyword`
* **Set value**: enabled
* **Script**:
```ts
emit("Hello World!");
```

**Customer field example**:

* **Name**: `customer`
* **Type**: `Keyword`
* **Set value**: enabled
* **Script**:
```ts
String str = doc['customer_first_name.keyword'].value;
char ch1 = str.charAt(0);
emit(doc['customer_last_name.keyword'].value  ", "  ch1);
```

#### Visualize aggregated fields

If a field can be [aggregated](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/search-aggregations.html), you can quickly
visualize it in detail by opening it in **Lens** from **Discover**. **Lens** is the default visualization editor in Kibana.

. In the list of fields, find an aggregatable field. For example, with the sample data, you can look for `day_of_week`.
image:images/discover-day-of-week.png[Top values for the day_of_week field, plus Visualize button, width=50%]

. In the popup, click **Visualize**.
Kibana creates a **Lens** visualization best suited for this field.

. In **Lens**, from the *Available fields* list, drag and drop more fields to refine the visualization. In this example, we're adding the `manufacturer.keyword` field onto the workspace, which automatically adds a breakdown of the top values to the visualization.
image:images/discover-from-visualize.png[Visualization that opens from Discover based on your data]

. Save the visualization if you'd like to add it to a dashboard or keep it in the Visualize library for later use.

For geo point fields (image:images/geoip-icon.png[Geo point field icon, width=20px]),
if you click **Visualize**,
your data appears in a map.

image:images/discover-maps.png[Map containing documents]

#### Find and highlight values in the table

Use the in-table search to find and highlight specific values beyond what's currently visible on your screen. 

The in-table search looks for all matching values in all results and pages currently loaded in the table. The number of results loaded depends on the Sample size. If you load more results, the search automatically updates and reflects the new number of matching values, if any more are found.

**Tip:** You can navigate between results with your keyboard by pressing "Enter" to go to the next result, and "Shift + Enter" to go to the previous result.

(Figure: https://images.contentstack.io/v3/assets/bltefdd0b53724fa2ce/blt30bf5f8b9a45ab74/67c234a787966d9fbc994ce0/in-table-search-demo.gif)

#### Compare documents

You can use *Discover* to compare and diff the field values of multiple results or documents in the table.

. Select the results you want to compare from the Documents or Results tab in Discover.

. From the **Selected** menu in the table toolbar, choose **Compare selected**. The comparison view opens and shows the selected results next to each other.

. Compare the values of each field. By default the first result selected shows as the reference for displaying differences in the other results. When the value remains the same for a given field, it's displayed in green. When the value differs, it's displayed in red. 
**Tip:** You can change the result used as reference by selecting **Pin for comparison** in the contextual menu of any other result.
image:images/discover-compare-rows.png[Comparison view in Discover]

. Optionally, customize the **Comparison settings** to your liking. You can for example choose to not highlight the differences, to show them more granularly at the line, word, or character level, or even to hide fields where the value matches for all results.

. Exit the comparison view at any time using the **Exit comparison mode** button.

#### Copy results as text or JSON

You can quickly copy the content currently displayed in the table for one or several results to your clipboard.

. Select the results you want to copy.

. Open the **Selected** menu in the table toolbar, and select **Copy selection as text** or **Copy documents as JSON**.

The content is copied to your clipboard in the selected format.
Fields that are not currently added to the table are ignored.

**Tip:** You can copy the content of a single cell to your clipboard from the quick actions that appear when hovering over the cell.

#### Explore individual result or document details in depth

Dive into an individual document to view its fields and the documents
that occurred before and after it.

. In the document table, click the expand icon
image:images/expand-icon-2.png[double arrow icon to open a flyout with the document details]
to show document details.
image:images/document-table-expanded.png[Table view with document expanded]

. Scan through the fields and their values. You can filter the table in several ways:
** If you find a field of interest,
hover your mouse over the *Field* or *Value* columns for filters and additional options. 
** Use the search above the table to filter for specific fields or values, or filter by field type using the options to the right of the search field.
** You can pin some fields by clicking the left column to keep them displayed even if you filter the table.
**Tip:** You can restrict the fields listed in the detailed view to just the fields that you explicitly added to the **Discover** table, using the **Selected only** toggle. In ES|QL mode, you also have an option to hide fields with null values. This toggle isn't available from the **View single document** page.

. To navigate to a view of the document that you can bookmark and share, select **View single document**.

. To view documents that occurred before or after the event you are looking at, select
**View surrounding documents**.

### Search and filter data

#### Default mode: Search and filter using KQL

One of the unique capabilities of **Discover** is the ability to combine
free text search with filtering based on structured data.
To search all fields, enter a simple string in the query bar.

image:images/discover-search-field.png[Search field in Discover]

**Note:** Free text searches that don't specify a field may not return expected results depending on how the [`index.query.default_field` index setting](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/index-modules.html#index-query-default-field) is configured for the indices matching the current data view.

To search particular fields and
build more complex queries, use the Kibana Query language.
As you type, KQL prompts you with the fields you can search and the operators
you can use to build a structured query.

For example, search the ecommerce sample data for documents where the country matches US:

. Enter `g`, and then select *geoip.country_iso_code*.
. Select *:* for equals, and *US* for the value, and then click the refresh button or press the Enter key.
. For a more complex search, try:
```ts
geoip.country_iso_code : US and products.taxless_price >= 75
```

With the query input, you can filter data using the KQL or Lucene languages. You can also use the **Add filter** function available next to the query input to build your filters one by one or define them as Query DSL.

For example, exclude results from the ecommerce sample data view where day of week is not Wednesday:

. Click image:images/add-icon.png[Add icon] next to the query bar.
. In the *Add filter* pop-up, set the field to *day_of_week*, the operator to *is not*,
and the value to *Wednesday*.
image:images/discover-add-filter.png[Add filter dialog in Discover]

. Click **Add filter**.
. Continue your exploration by adding more filters.
. To remove a filter, click the close icon (x) next to its name in the filter bar.

#### Search and filter using ES|QL

You can use **Discover** with the Elasticsearch Query Language, ES|QL. When using ES|QL,
you don't have to select a data view. It's your query that determines the data to explore and display in Discover.

You can switch to the ES|QL mode of Discover from the application menu bar.
If you've entered a KQL or Lucene query in the default mode of Discover, it automatically converts to ES|QL.

Note that in ES|QL mode, the **Documents** tab is named **Results**.

**Important:** When an ES|QL query times out, partial results that are available are shown. The timeout is defined by the `search:timeout` advanced setting, which is set to 10 minutes (600000 ms) by default. In serverless projects, this advanced setting is not customizable and the timeout is set to 10 minutes.

Learn more about how to use ES|QL queries in Using ES|QL.

#### Save your Discover session for later use

Save your Discover session so you can use it later, generate a CSV report, or use it to create visualizations, dashboards, and Canvas workpads.
Saving a Discover session saves the query text, filters,
and current view of *Discover*, including the columns selected in
the document table, the sort order, and the {data-source}.

. In the application menu bar, click **Save**.

. Give your session a title and a description.

. Optionally store tags and the time range with the session.

. Click **Save**.

#### Share your Discover session

To share your search and **Discover** view with a larger audience, click *Share* in the application menu bar.
For detailed information about the sharing options, refer to Reporting.

### Generate alerts

From *Discover*, you can create a rule to periodically
check when data goes above or below a certain threshold within a given time interval.

. Ensure that your data view,
query, and filters fetch the data for which you want an alert.
. In the application menu bar, click *Alerts > Create search threshold rule*.
The *Create rule* form is pre-filled with the latest query sent to Elasticsearch.
. Configure your query and select a connector type.

. Click *Save*.

For more about this and other rules provided in {alert-features}, go to alerting-getting-started.

### What’s next?

* Search for relevance.

* Configure the chart and document table to better meet your needs.

### Troubleshooting

This section references common questions and issues encountered when using Discover.
Also check the following blog post: {blog-ref}troubleshooting-guide-common-issues-kibana-discover-load[Learn how to resolve common issues with Discover.]

**Some fields show as empty while they should not be, why is that?**

This can happen in several cases:

* With runtime fields and regular keyword fields, when the string exceeds the value set for the [ignore_above](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/ignore-above.html) setting used when indexing the data into Elasticsearch.
* Due to the structure of nested fields, a leaf field added to the table as a column will not contain values in any of its cells. Instead, add the root field as a column to view a JSON representation of its values. Learn more in [this blog post](https://www.elastic.co/de/blog/discover-uses-fields-api-in-7-12).
