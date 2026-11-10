<!-- Converted from getting-started/quick-start-guide.asciidoc (AsciiDoc). Includes are inlined. -->

## Quick start

To quickly get up and running with Kibana, set up on Cloud, then add a sample data set that you can explore and visualize.

When you're done, you'll know how to:

* Explore the data with *Discover*.

* Visualize the data with *Dashboard*.

### Required privileges

You must have `read`, `write`, and `manage` privileges on the `kibana_sample_data_*` indices.
Learn how to secure access to Kibana, or refer to [Security privileges](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/security-privileges.html) for more information.

## Set up on cloud

(Include not available offline: {docs-root}/shared/cloud/ess-getting-started.asciidoc)

## Add sample data

Sample data sets come with sample visualizations, dashboards, and more to help you explore Kibana before you ingest or add your own data.

. Open the **Integrations** page from the navigation menu or using the global search field.

. In the list of integrations, select **Sample Data**.

. On the page that opens, select *Other sample data sets*. 

. Install the sample data sets that you want.

Once installed, you can access the sample data in the various Kibana apps available to you. 

## Explore the data

*Discover* displays the data in an interactive histogram that shows the distribution of data, or documents, over time, and a table that lists the fields for each document that matches the {data-source}. To view a subset of the documents, you can apply filters to the data, and customize the table to display only the fields you want to explore.

. Go to *Discover*.

. Change the time filter to *Last 7 days*.
(Figure: images/timeFilter_discover_8.4.0.png)

. To view the sales orders for women's clothing that are $60 or more, use the *KQL* search field:
products.taxless_price >= 60 and category : Women's Clothing
(Figure: images/kql_discover_8.4.0.png)

. To view only the product categories that contain sales orders, hover over the *category* field, then click *+*.
(Figure: images/availableFields_discover_8.4.0.png)

## Visualize the data

A dashboard is a collection of panels that you can use to visualize the data. Panels contain visualizations, interactive controls, text, and more.

. Go to *Dashboards*.

. Click *[eCommerce] Revenue Dashboard*.
(Figure: images/dashboard_ecommerceRevenueDashboard_8.6.0.png)

### Create a visualization panel

Create a treemap visualization panel that shows the top sales regions and manufacturers, then add the panel to the dashboard.

. In the toolbar, click *Edit*.

. On the dashboard, click *Create visualization*.

. In the drag-and-drop visualization editor, open the *Visualization type* dropdown, then select *Treemap*.
(Figure: getting-started/images/visualizationTypeDropdown_lens_8.4.0.png)

. From the *Available fields* list, drag the following fields to the workspace:

* *geoip.city_name*

* *manufacturer.keyword*
(Figure: getting-started/images/ecommerceTreemap_lens_8.4.0.png)

. Click *Save and return*.
The treemap appears as the last visualization panel on the dashboard.

### Interact with the data

You can interact with the dashboard data using controls that allow you to apply dashboard-level filters. Interact with the *[eCommerce] Controls* panel to view the women's clothing data from the Gnomehouse manufacturer.

. From the *Manufacturer* dropdown, select *Gnomehouse*.

. From the *Category* dropdown, select *Women's Clothing*.
(Figure: images/sampleDataFilter_dashboard_8.6.0.png)

### Filter the data

To view a subset of the data, you can apply filters to the dashboard data. Apply a filter to view the women's clothing data generated on Wednesday from the Gnomehouse manufacturer.

. Click *Add filter*.
(Figure: images/addFilter_dashboard_8.6.0.png)

. From the *Field* dropdown, select *day_of_week*.

. From the *Operator* dropdown, select *is*.

. From the *Value* dropdown, select *Wednesday*.
(Figure: images/addFilterOptions_dashboard_8.6.0.png)

. Click *Add filter*.
(Figure: images/dashboard_sampleDataAddFilter_8.6.0.png)

## What's next?

*Add your own data.* Ready to add your own data? Go to {observability-guide}/observability-get-started.html[Get started with Elastic Observability], or go to Add data to Kibana and learn about all the ways you can add data.

*Explore your own data in Discover.* Ready to learn more about exploring your data in *Discover*? Go to Discover.

*Create a dashboard with your own data.* Ready to learn more about visualizing your data on a *Dashboard*? Go to Dashboard.

*Try out the {ml-features}.* Ready to analyze the sample data sets and generate models for its patterns of behavior? Go to {ml-docs}/ml-getting-started.html[Getting started with machine learning].
