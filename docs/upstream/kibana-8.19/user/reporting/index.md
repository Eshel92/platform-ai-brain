<!-- Converted from user/reporting/index.asciidoc (AsciiDoc). Includes are inlined. -->

# Reporting and sharing

Kibana provides you with several options to share *Discover* sessions, dashboards, *Visualize Library* visualizations, and *Canvas* workpads. These sharing options are available from the *Share* and **Export** menus in the toolbar.

## Share with a direct link

You can share direct links to saved Discover sessions, dashboards, and visualizations. Look for the **Share** icon in the toolbar.

When applicable, you can choose to share the object using a relative or an absolute time range:

* **Relative time range**: The link shows current data. For example, if you share a "Last 7 days" view, users will see the most recent 7 days when they open the link.
* **Absolute time range** (default): The link shows a fixed time period. For example, if you share a "Last 7 days" view on January 7, 2025, the link will always show that exact week of January 1-7, 2025, regardless of when users open the link.

**Tip:** When sharing an object with unsaved changes, you get a temporary link that might break in the future, for example in case of upgrade. Save the object to get a permanent link instead.

To access the object shared with the link, users need to authenticate.

Anonymous users can also access the link if you have configured Anonymous authentication and your anonymous service account has privileges to access what you want to share.

(Figure: https://images.contentstack.io/v3/assets/bltefdd0b53724fa2ce/bltc45bb05c1fab3e60/68826ffb4f04ad6e224c2248/share-dashboard.gif)

## Export as a file

**Note:** For more information on how to grant access and configure reporting in Kibana, refer to Configure reporting in Kibana

Create and download PDF, PNG, or CSV reports of saved Discover sessions, dashboards, visualizations, and workpads.

* *PDF* &mdash; Generate and download PDF files of dashboards, visualizations, and *Canvas* workpads. PDF reports are a [subscription feature](https://www.elastic.co/subscriptions).

* *PNG* &mdash; Generate and download PNG files of dashboards and visualizations. PNG reports are a [subscription feature](https://www.elastic.co/subscriptions).

* *CSV Reports* &mdash; Generate CSV reports of saved Discover sessions. Certain limitations apply.

* *CSV Download* &mdash; Generate and download CSV files of *Lens* visualizations.

* *Download as JSON* &mdash; Generate and download JSON files of *Canvas* workpads.

The layout and size of the report depends on what you are sharing.
For saved Discover sessions, dashboards, and visualizations, the layout depends on the size of the panels.
For workpads, the layout depends on the size of the worksheet dimensions.

To change the output size, change the size of the browser, which resizes the shareable container before the report generates. It might take some trial and error before you're satisfied.

In the following dashboard, the shareable container is highlighted:

(Figure: user/reporting/images/shareable-container.png)

. Open the saved Discover session, dashboard, visualization, or **Canvas** workpad you want to share.

. From the toolbar, click the **Export** icon, then choose a file type. 
**Note:** When you create a dashboard report that includes a data table or Discover session, the PDF includes only the visible data.
=====
Tips for generating PDF reports: 

* If you are creating dashboard PDFs, select **For printing** to create printer-friendly PDFs with multiple A4 portrait pages and two visualizations per page.
* If you are creating workpad PDFs, select *Full page layout* to create PDFs without margins that surround the workpad.
=====
. Click the button that generates or exports the report. A message appears, indicating that the report is in the export queue.
**Note:** To generate the report from outside of Kibana or from Watcher, use the POST URL, then submit an HTTP `POST` request using a script or Watcher. In the Elastic Stack, you can schedule a recurring task in Kibana that generates reports on a repeating basis. Refer to automating-report-generation to learn more. 

Go to the **Reporting** page to access all of your reports. To find the page, navigate to **Stack Management > Alerts and Insights > Reporting** in the main menu, or use the global search field.

**Note:** In self-managed and Cloud hosted deployments, reports are stored in Elasticsearch and managed by the `kibana-reporting` index lifecycle management
(ILM) policy. By default, the policy stores reports forever. To learn more about ILM policies, refer
to the Elasticsearch [ILM documentation](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/index-lifecycle-management.html).

### CSV report limitations

We recommend using CSV reports to export moderate amounts of data only. The feature enables analysis of data in external tools, but it is not intended for bulk export or to backup Elasticsearch data. Report timeout and incomplete data issues are likely if you are exporting data where:

- More than 250 MB of data is being exported
- Data is stored on slow storage tiers
- Any shard needed for the search is unavailable
- Network latency between nodes is high
- Cross-cluster search is used
- ES|QL is used and result row count exceeds the limits of ES|QL queries

To work around the limitations, use filters to create multiple smaller reports, or extract the data you need directly with the Elasticsearch APIs.

For more information on using Elasticsearch APIs directly, see [Scroll API](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/scroll-api.html), [Point in time API](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/point-in-time-api.html), [ES|QL](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/esql-rest.html) or [SQL](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/sql-rest-format.html#_csv) with CSV response data format. We recommend that you use an official Elastic language client: details for each programming language library that Elastic provides are in the [Elasticsearch Client documentation](https://www.elastic.co/guide/en/elasticsearch/client/index.html).

Reporting parameters can be adjusted to overcome some of these limiting scenarios. Results are dependent on data size, availability, and latency factors and are not guaranteed.

### PNG/PDF report limitations

We recommend using PNG/PDF reports to export moderate amounts of data only. The feature enables a high-level
export capability, but it's not intended for bulk export. If you need to export several pages of image data,
consider using multiple report jobs to export a small number of pages at a time. If the screenshot of exported
dashboard contains a large number of pixels, consider splitting the large dashboard into smaller artifacts to
use less memory and CPU resources.

For the most reliable configuration of PDF/PNG {report-features}, consider installing Kibana using Docker or using Elastic Cloud.

## Create JSON files

Create and share JSON files for workpads.

. Go to *Canvas*.

. Open the workpad you want to share.

. From the toolbar, click *Export*, then select *JSON*.

## Embed outside of Kibana

* beta[] *Share on a website* &mdash; Download and securely share *Canvas* workpads on any website.

* *Embed code* &mdash; Embed fully interactive dashboards as an iframe on web pages.

**Note:** For Elastic Cloud hosted deployments, Kibana instances require a minimum of 2GB RAM to generate PDF or PNG reports. To
change Kibana sizing, {ess-console}[edit the deployment].

## Share workpads on a website

beta[] Create and securely share static *Canvas* workpads on a website. To customize the behavior of the workpad on your website, you can choose to autoplay the pages or hide the workpad toolbar.

. Go to *Canvas*.

. Open the workpad you want to share.

. Click *Share > Share on a website*.

. To customize the workpad behavior to autoplay the pages or hide the toolbar, use the inline parameters.
To make sure that your data remains secure, the data in the JSON file is not connected to Kibana. *Canvas* does not display elements that manipulate the data on the workpad.
**Note:** Shareable workpads encode the current state of the workpad in a JSON file. When you make changes to the workpad, the changes do not appear in the shareable workpad on your website.

. To change the settings, click the settings icon, then choose the settings you want to use.

## Embed code

Display your dashboards on an internal company website or personal web page with an iframe. To embed other Kibana objects, manually create the HTML code.

For information about granting access to embedded dashboards, refer to kibana-authentication.

. Open the dashboard you want to share.

. Click *Share > Embed code*.

. Specify which parts of the dashboard you want to include: Top menu, query, time filter, and filter bar.

. Click *Copy embed code*.

(See `user/reporting/automating-report-generation.md`)
(See `user/reporting/reporting-troubleshooting.md`)
(See `user/reporting/reporting-csv-troubleshooting.md`)
(See `user/reporting/reporting-pdf-troubleshooting.md`)
