<!-- Converted from user/canvas.asciidoc (AsciiDoc). Includes are inlined. -->

# Canvas

*Canvas* is a data visualization and presentation tool that allows you to pull live data from Elasticsearch, 
then combine the data with colors, images, text, and your imagination to create dynamic, multi-page, pixel-perfect displays. 
If you are a little bit creative, a little bit technical, and a whole lot curious, then *Canvas* is for you.

With *Canvas*, you can:

* Create and personalize your work space with backgrounds, borders, colors, fonts, and more.

* Customize your workpad with your own visualizations, such as images and text.

* Pull your data directly from Elasticsearch, then show it off with charts, graphs, progress monitors, and more.

* Focus the data you want to display with filters.

(Figure: images/canvas_logWebTrafficWorkpadTemplate_7.17.0.png)

## Create workpads

A _workpad_ provides you with a space where you can build presentations of your live data. You can create a workpad from scratch, start with a preconfigured workpad, 
import an existing workpad, or use a sample data workpad.

### Minimum requirements

To create workpads, you must meet the minimum requirements. 

* If you need to set up Kibana, use [our free trial](https://www.elastic.co/cloud/elasticsearch-service/signup?baymax=docs-body&elektra=docs).

* Make sure you have [data indexed into Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/getting-started-index.html) and a data view.

* Have an understanding of [Elasticsearch documents and indices](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/documents-indices.html).

* Make sure you have sufficient privileges to create and save workpads. When the read-only indicator appears, you have insufficient privileges,
and the options to create and save workpads are unavailable. For more information, refer to Granting access to Kibana.

You can open *Canvas* using the navigation menu or the 
global search field.

### Start with a blank workpad

To use the background colors, images, and data of your choice, start with a blank workpad.

. On the *Canvas* page, click *Create workpad*.

. Specify the *Workpad settings*.

.. Add a *Name* to your workpad.

.. In the *Width* and *Height* fields, specify the size, or select one of default layouts. 

.. Click the *Background* color picker, then select the color for your workpad.

### Create workpads from templates

If you're unsure about where to start, you can use one of the preconfigured templates that come with *Canvas*.

. On the *Canvas* page, select *Templates*.

. Click the preconfigured template that you want to use.

. Add your own *Name* to the workpad.

### Import existing workpads

When you want to use a workpad that someone else has already started, import the JSON file.

On the *Canvas* page, drag the file to the *Import workpad JSON file* field. 

### Use sample data workpads

Each of the Kibana sample data sets comes with a workpad that you can use for your own workpad inspiration.

. Add a sample data set.

. On a sample data card, click *View data*, then select *Canvas*.

## Add elements

Create a story about your data by adding elements to your workpad that include images, text, charts, and more.

### Create elements

Choose the type of element you want to use, then use the preconfigured demo data to familiarize yourself with the element. When you're ready, connect the element to your own data. 
By default, most of the elements you create use the demo data until you change the data source. The demo data includes a small data set that you can use to experiment with your element.

. Click *Add element*, then select the element you want to use.

. To connect the element to your data, select *Data > Demo data*, then select one of the following data sources:

* *Elasticsearch SQL* &mdash; Access your data in Elasticsearch using [SQL syntax](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/sql-spec.html).

* *Elasticsearch documents* &mdash; Access your data in Elasticsearch without using aggregations. To use, select a {data-source} and fields. 
Use *Elasticsearch documents* when you have low-volume datasets, and you want to view raw documents or to plot exact, non-aggregated values on a chart.

* *Timelion* &mdash; Access your time series data using *Timelion* queries. To use *Timelion* queries, you can enter a query using the Lucene Query Syntax.
Each element can display a different {data-source}, and pages and workpads often contain multiple {data-sources}.

. To save, use the following options:

* To save a single element, select the element, then click *Edit > Save as new element*.

* To save a group of elements, press and hold Shift, select the elements you want to save, then click *Edit > Save as new element*.

To access your saved elements, click *Add element > My elements*.

### Add panels from the Visualize Library

Add a panel that you saved in *Visualize Library* to your workpad. 

. Click *Add from library*, then select the panel you want to add.

. To use the customization options, open the panel menu, then select one of the following options:

* *Edit map* &mdash; Opens Maps so that you can edit the panel.

* *Edit Visualization* &mdash; Opens the visualization editor so that you can edit the panel.

* *Panel settings* &mdash; Allows you to change the title, description, and time range for the panel.

* *Inspect* &mdash; Allows you to drill down into the panel data.

### Add your own images

To personalize your workpad, add your own logos and graphics.

. Click *Add element > Manage assets*.

. On the *Manage workpad assets* window, drag and drop your images.

. To add the image to the workpad, click *Create image element*.

## Add pages

Organize and separate your ideas by adding more pages.

. Click *Page 1*, then click *+*.

. On the *Page* editor panel, select the page transition from the *Transition* dropdown.

## Share your workpad

To share workpads with a larger audience, click *Share* in the toolbar. For detailed information about the sharing options, refer to Reporting.

## Export workpads

Want to export multiple workpads? Go to the *Canvas* page, select the workpads you want to export, then click *Export*.

(See `canvas/canvas-edit-workpads.md`)
(See `canvas/canvas-present-workpad.md`)
(See `canvas/canvas-tutorial.md`)
(See `canvas/canvas-expression-lifecycle.md`)
(See `canvas/canvas-function-reference.md`)
(See `canvas/canvas-tinymath-functions.md`)
