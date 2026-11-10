<!-- Converted from user/dashboard/tutorial-create-a-dashboard-of-lens-panels.asciidoc (AsciiDoc). Includes are inlined. -->

## Create a simple dashboard to monitor website logs

Learn the most common ways to create a dashboard from your own data.
The tutorial will use sample data from the perspective of an analyst looking
at website logs, but this type of dashboard works on any type of data.

When you're done, you'll have a complete overview of the sample web logs data. 

(Figure: images/lens_logsDashboard_8.4.0.png)

Before you begin, you should be familiar with the kibana-concepts-analysts.

### Add the data and create the dashboard

Add the sample web logs data, and create and set up the dashboard.

. Install the web logs sample data set.

. Go to *Dashboards*.

. Click *Create dashboard*.

. Set the time filter to *Last 90 days*.

### Open the visualization editor and get familiar with the data

Open the visualization editor, then make sure the correct fields appear.

. On the dashboard, click *Create visualization*.

. Make sure the *Kibana Sample Data Logs* {data-source} appears.
(Figure: images/lens_dataViewDropDown_8.4.0.png)

To create the visualizations in this tutorial, you'll use the following fields:

* *Records*

* *timestamp*

* *bytes*

* *clientip*

* *referer.keyword*

Click a field name to view more details, such as its top values and distribution.

(Figure: https://images.contentstack.io/v3/assets/bltefdd0b53724fa2ce/blt25c7a05e0f5daaa3/671966b9b1d3dd705a2ae650/tutorial-field-more-info.gif)

### Create your first visualization

Pick a field you want to analyze, such as *clientip*. To analyze only the *clientip* field, use the *Metric* visualization to display the field as a number.

The only number function that you can use with *clientip* is *Unique count*, also referred to as cardinality, which approximates the number of unique values.

. Open the *Visualization type* dropdown, then select *Metric*.
(Figure: images/visualization-type-dropdown-8.16.0.png)

. From the *Available fields* list, drag *clientip* to the workspace or layer pane.
(Figure: images/tutorial-unique-count-of-client-ip-8.16.0.png)
In the layer pane, *Unique count of clientip* appears because the editor automatically applies the *Unique count* function to the *clientip* field. *Unique count* is the only numeric function that works with IP addresses.

. In the layer pane, click *Unique count of clientip*.

.. In the *Name* field, enter `Unique visitors`.

.. Click *Close*.

. Click *Save and return*.

### View a metric over time

There are two shortcuts you can use to view metrics over time. 
When you drag a numeric field to the workspace, the visualization editor adds the default
time field from the {data-source}. When you use the *Date histogram* function, you can
replace the time field by dragging the field to the workspace.

To visualize the *bytes* field over time:

. On the dashboard, click *Create visualization*. 

. From the *Available fields* list, drag *bytes* to the workspace. 
The visualization editor creates a bar chart with the *timestamp* and *Median of bytes* fields. 

. To zoom in on the data, click and drag your cursor across the bars. 
(Figure: images/lens_end_to_end_3_1_1.gif)

To emphasize the change in *Median of bytes* over time, change the visualization type to *Line* with one of the following options:

* In the *Suggestions*, click the line chart.
* In the editor toolbar, open the *Visualization type* dropdown, then select *Line*.
* In the layer pane, open the *Layer visualization type* menu, then click *Line*.

To increase the minimum time interval:

. In the layer pane, click *timestamp*.

. Change the *Minimum interval* to *1d*, then click *Close*.
You can increase and decrease the minimum interval, but you are unable to decrease the interval below the configured *Advanced Settings*. 

To save space on the dashboard, hide the axis labels.

. Open the *Left axis* menu, then select *None* from the *Axis title* dropdown.
(Figure: images/line-chart-left-axis-8.16.0.png)

. Open the *Bottom axis* menu, then select *None* from the *Axis title* dropdown.
(Figure: images/line-chart-bottom-axis-8.16.0.png)

. Click *Save and return*

Since you removed the axis labels, add a panel title:

. Hover over the panel and click image:dashboard/images/settings-icon-hover-action.png[Settings icon, width=3%]. The *Settings* flyout appears.

. In the *Title* field, enter `Median of bytes`, then click *Apply*.
(Figure: images/lens_lineChartMetricOverTime_8.4.0.png)

### View the top values of a field

Create a visualization that displays the most frequent values of *request.keyword* on your website, ranked by the unique visitors.
To create the visualization, use *Top values of request.keyword* ranked by *Unique count of clientip*, instead of being ranked by *Count of records*.

The *Top values* function ranks the unique values of a field by another function.
The values are the most frequent when ranked by a *Count* function, and the largest when ranked by the *Sum* function.

. On the dashboard, click *Create visualization*. 

. From the *Available fields* list, drag *clientip* to the *Vertical axis* field in the layer pane. 
The visualization editor automatically applies the *Unique count* function. If you drag *clientip* to the workspace, the editor adds the field to the incorrect axis.

. Drag *request.keyword* to the workspace.
(Figure: images/tutorial-top-values-of-field-8.16.0.png)
When you drag a text or IP address field to the workspace,
the editor adds the *Top values* function ranked by *Count of records* to show the most frequent values.

The chart labels are unable to display because the *request.keyword* field contains long text fields. You could use one of the *Suggestions*, but the suggestions also have issues with long text. The best way to display long text fields is with the *Table* visualization.

. Open the *Visualization type* dropdown, then select *Table*.
(Figure: images/table-with-request-keyword-and-client-ip-8.16.0.png)

. In the layer pane, click *Top 5 values of request.keyword*.

.. In the *Number of values* field, enter `10`.

.. In the *Name* field, enter `Page URL`.

.. Click *Close*.
(Figure: images/lens_tableTopFieldValues_7.16.png)

. Click *Save and return*.
Since the table columns are labeled, you do not need to add a panel title.

### Compare a subset of documents to all documents

Create a proportional visualization that helps you determine if your users transfer more bytes from documents under 10KB versus documents over 10Kb.

. On the dashboard, click *Create visualization*. 

. From the *Available fields* list, drag *bytes* to the *Vertical axis* field in the layer pane.

. In the layer pane, click *Median of bytes*. 

. Click the *Sum* quick function, then click *Close*.

. From the *Available fields* list, drag *bytes* to the *Breakdown* field in the layer pane.

To select documents based on the number range of a field, use the *Intervals* function.
When the ranges are non numeric, or the query requires multiple clauses, you could use the *Filters* function.

Specify the file size ranges: 

. In the layer pane, click *bytes*.

. Click *Create custom ranges*, enter the following in the *Ranges* field, then press Return:

* *Ranges* &mdash; `0` -> `10240`

* *Label* &mdash; `Below 10KB`

. Click *Add range*, enter the following, then press Return:

* *Ranges* &mdash; `10240` -> `+∞`

* *Label* &mdash; `Above 10KB`
(Figure: images/lens_end_to_end_6_1.png)

. From the *Value format* dropdown, select *Bytes (1024)*, then click *Close*.

To display the values as a percentage of the sum of all values, use the *Pie* chart. 

. Open the *Visualization Type* dropdown, then select *Pie*.
(Figure: images/lens_pieChartCompareSubsetOfDocs_7.16.png)

. Click *Save and return*.

Add a panel title:

. Hover over the panel and click image:dashboard/images/settings-icon-hover-action.png[Settings icon, width=3%]. The *Settings* flyout appears.

. In the *Title* field, enter `Sum of bytes from large requests`, then click *Apply*.

### View the distribution of a number field

The distribution of a number can help you find patterns. For example, you can analyze the website traffic per hour to find the best time for routine maintenance.

. On the dashboard, click *Create visualization*. 

. From the *Available fields* list, drag *bytes* to *Vertical axis* field in the layer pane.

. In the layer pane, click *Median of bytes*.

.. Click the *Sum* quick function.

.. In the *Name* field, enter `Transferred bytes`.

.. From the *Value format* dropdown, select *Bytes (1024)*, then click *Close*.

. From the *Available fields* list, drag *hour_of_day* to *Horizontal axis* field in the layer pane.

. In the layer pane, click *hour_of_day*, then slide the *Intervals granularity* slider until the horizontal axis displays hourly intervals.
(Figure: images/lens_barChartDistributionOfNumberField_7.16.png)

. Click *Save and return*.

Add a panel title:

. Hover over the panel and click image:dashboard/images/settings-icon-hover-action.png[Settings icon, width=3%]. The *Settings* flyout appears.

. In the *Title* field, enter `Website traffic`, then click *Apply*.

### Create a multi-level chart

*Table* and *Proportion* visualizations support multiple functions. For example, to create visualizations that break down the data by website traffic sources and user geography, apply the *Filters* and *Top values* functions.

. On the dashboard, click *Create visualization*. 

. Open the *Visualization type* dropdown, then select *Treemap*.

. From the *Available fields* list, drag *Records* to the *Size by* field in the layer pane. 

. In the layer pane, click *Add or drag-and-drop a field* for *Group by*.

Create a filter for each website traffic source:

. Click *Filters*.

. Click *All records*, enter the following in the query bar, then press Return:

* *KQL* &mdash; `referer : *facebook.com*`

* *Label* &mdash; `Facebook`

. Click *Add a filter*, enter the following in the query bar, then press Return:

* *KQL* &mdash; `referer : *twitter.com*`

* *Label* &mdash; `Twitter`

. Click *Add a filter*, enter the following in the query bar, then press Return:

* *KQL* &mdash; `NOT referer : *twitter.com* OR NOT referer: *facebook.com*`

* *Label* &mdash; `Other`

. Click *Close*.

Add the user geography grouping:

. From the *Available fields* list, drag *geo.srcdest* to the workspace.

. To change the *Group by* order, drag *Top 3 values of geo.srcdest* in the layer pane so that appears first.
(Figure: images/lens_end_to_end_7_2.png)

Remove the documents that do not match the filter criteria:

. In the layer pane, click *Top 3 values of geo.srcdest*.

. Click *Advanced*, deselect *Group other values as "Other"*, then click *Close*.
(Figure: images/lens_treemapMultiLevelChart_7.16.png)

. Click *Save and return*.

Add a panel title:

. Hover over the panel and click image:dashboard/images/settings-icon-hover-action.png[Settings icon, width=3%]. The *Settings* flyout appears.

. In the *Title* field, enter `Page views by location and referrer`, then click *Apply*.

### Arrange the dashboard panels

Resize and move the panels so they all appear on the dashboard without scrolling.

Decrease the size of the following panels, then move the panels to the first row:

* *Unique visitors* 

* *Median of bytes*

* *Sum of bytes from large requests*

* *Website traffic*
(Figure: images/lens_logsDashboard_8.4.0.png)

### Save the dashboard

Now that you have a complete overview of your web server data, save the dashboard.

. In the toolbar, click *Save*.

. On the *Save dashboard* window, enter `Logs dashboard` in the *Title* field.

. Select *Store time with dashboard*.

. Click *Save*. You will be identified as the **creator** of the dashboard. If you or another user edit the dashboard, you can also view the **last editor** when checking the dashboard information.

(Figure: images/dashboard-creator-editor.png)
