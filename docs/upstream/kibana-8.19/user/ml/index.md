<!-- Converted from user/ml/index.asciidoc (AsciiDoc). Includes are inlined. -->

# Machine learning

As data sets increase in size and complexity, the human effort required to
inspect dashboards or maintain rules for spotting infrastructure problems,
cyber attacks, or business issues becomes impractical. Elastic {ml-features}
such as anomaly detection and {oldetection} make it easier to notice suspicious
activities with minimal human interference.

Kibana includes a free *{data-viz}* to learn more about your data. In particular,
if your data is stored in Elasticsearch and contains a time field, you can use the
*{data-viz}* to identify possible fields for anomaly detection:

(Figure: user/ml/images/ml-data-visualizer-sample.png)

You can upload different file formats for analysis with the *{data-viz}*.

File formats supported up to 500 MB:

* CSV
* TSV
* NDJSON
* Log files

File formats supported up to 60 MB:

* PDF
* Microsoft Office files (Word, Excel, PowerPoint)
* Plain Text (TXT)
* Rich Text (RTF)
* Open Document Format (ODF)

The *{data-viz}* identifies the file format and field mappings, and you can import the data into an Elasticsearch index. To change the default file size limit, see `fileUpload:maxFileSize` in advanced settings.

If {stack-security-features} are enabled, users must have the necessary
privileges to use {ml-features}. Refer to
{ml-docs}/setup.html#setup-privileges[Set up {ml-features}].

**Note:** There are limitations in {ml-features} that affect Kibana. For more 
information, refer to {ml-docs}/ml-limitations.html[Machine learning].

## Data drift

preview::[]

You can find the data drift view in **{ml-app}** > *{data-viz}* in Kibana or by using
the global search field. 
The data drift view shows you the differences in each field for two 
different time ranges in a given {data-source}. The view helps you to visualize 
the changes in your data over time and enables you to understand its behavior 
better.

(Figure: user/ml/images/ml-data-drift.png)

Select a {data-source} that you want to analyze, then select a time range for 
the reference and the comparison data in the appearing histogram chart. You can 
adjust the time range for both the reference and the comparison data by moving 
the respective brushes. When you finished setting the time ranges, click 
*Run analysis*. 

You can decide whether you want to see all the fields in the {data-source} or 
only the ones that contains drifted data. The analysis results table displays 
the fields, their types, if drift is detected, the p-value that indicates how 
significant the detected change is, the reference and comparison distribution, 
and the comparison chart. You can expand the results for a particular field by 
clicking the arrow icon at the beginning of the field's row. 

## {anomaly-detect-cap}

The Elastic machine learning anomaly detection feature automatically models the normal
behavior of your time series data — learning trends, periodicity, and more — in
real time to identify anomalies, streamline root cause analysis, and reduce
false positives. {anomaly-detect-cap} runs in and scales with Elasticsearch, and
includes an intuitive UI on the Kibana *Machine Learning* page for creating
anomaly detection jobs and understanding results.

If you have a license that includes the {ml-features}, you can
create anomaly detection jobs and manage jobs and datafeeds from the *Job Management*
pane:

(Figure: user/ml/images/ml-job-management.png)

You can use the *Settings* pane to create and edit calendars and the
filters that are used in custom rules:

(Figure: user/ml/images/ml-settings.png)

The *Anomaly Explorer* and *Single Metric Viewer* display the results of your
anomaly detection jobs. For example:

(Figure: user/ml/images/ml-single-metric-viewer.png)

You can optionally add annotations by drag-selecting a period of time in
the *Single Metric Viewer* and adding a description. For example, you can add an
explanation for anomalies in that time period or provide notes about what is
occurring in your operational environment at that time:

(Figure: user/ml/images/ml-annotations-list.png)

In some circumstances, annotations are also added automatically. For example, if
the anomaly detection job detects that there is missing data, it annotates the affected
time period. For more information, see
{ml-docs}/ml-delayed-data-detection.html[Handling delayed data]. The
*Job Management* pane shows the full list of annotations for each job.

**Note:** The Kibana {ml-features} use pop-ups. You must configure your web
browser so that it does not block pop-up windows or create an exception for your
Kibana URL.

For more information about the anomaly detection feature, see
[Machine learning in the Elastic Stack](https://www.elastic.co/what-is/elastic-stack-machine-learning)
and {ml-docs}/ml-ad-overview.html[Machine learning anomaly detection].

## {dfanalytics-cap}

The Elastic machine learning {dfanalytics} feature enables you to analyze your data using
{classification}, {oldetection}, and {regression} algorithms and generate new
indices that contain the results alongside your source data.

If you have a license that includes the {ml-features}, you can create
{dfanalytics-jobs} and view their results on the *Data Frame Analytics* page in
Kibana. For example:

(Figure: user/ml/images/classification.png)

For more information about the {dfanalytics} feature, see
{ml-docs}/ml-dfanalytics.html[Machine learning {dfanalytics}].

## AIOps Labs

AIOps Labs is a part of {ml-app} in Kibana which provides features that use 
advanced statistical methods to help you interpret your data and its behavior.

### Log rate analysis

Log rate analysis uses advanced statistical methods to identify reasons for increases or decreases in log rates and displays the statistically significant data in a tabular format.
It makes it easy to find and investigate causes of unusual spikes or drops by using the analysis workflow view.
Examine the histogram chart of the log rates for a given {data-source}, and find the reason behind a particular change possibly in millions of log events across multiple fields and values.

You can find log rate analysis embedded in multiple applications.
In Kibana, you can find it under **{ml-app}** > **AIOps Labs** or by using the global search field. Here, you can select the {data-source} or saved Discover session that you want to analyze.

(Figure: user/ml/images/ml-log-rate-analysis-before.png)

Select a spike or drop in the log event histogram chart to start the analysis.
It identifies statistically significant field-value combinations that contribute to the spike or drop and displays them in a table.
You can optionally choose to summarize the results into groups.
The table also shows an indicator of the level of impact and a sparkline showing the shape of the impact in the chart.
Hovering over a row displays the impact on the histogram chart in more detail.
You can inspect a field in **Discover**, further investigate in **Log pattern analysis**, or copy the table row information as a query filter to the clipboard by selecting the corresponding option under the **Actions** column.
You can also pin a table row by clicking on it then move the cursor to the histogram chart. 
It displays a tooltip with exact count values for the pinned field which enables closer investigation.

Brushes in the chart show the baseline time range and the deviation in the analyzed data.
You can move the brushes to redefine both the baseline and the deviation and rerun the analysis with the modified values.

(Figure: user/ml/images/ml-log-rate-analysis.png)

### Log pattern analysis

Log pattern analysis helps you to find patterns in unstructured log messages and 
makes it easier to examine your data. It performs categorization analysis on a 
selected field of a {data-source}, creates categories based on the data and 
displays them together with a chart that shows the distribution of each category 
and an example document that matches the category.

You can find log pattern analysis under **{ml-app}** > **AIOps Labs** or by using the global search field. 
Here, you can select the {data-source} or saved Discover session that you want to analyze, or in 
**Discover** as an available action for any text field.

(Figure: user/ml/images/ml-log-pattern-analysis.png)

Select a field for categorization and optionally apply any filters that you 
want, then start the analysis. The analysis uses the same algorithms as a machine learning 
categorization job. The results of the analysis are shown in a table that makes 
it possible to open **Discover** and show or filter out the given category 
there, which helps you to further examine your log messages.

### Change point detection

preview::[]

Change point detection uses the 
[change point aggregation](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/search-aggregations-change-point-aggregation.html) 
to detect distribution changes, trend changes, and other statistically 
significant change points in a metric of your time series data.

You can find change point detection under **{ml-app}** > **AIOps Labs** or by using the global search field. 
Here, you can select the {data-source} or saved Discover session that you want to analyze.

(Figure: user/ml/images/ml-change-point-detection.png)

Select a function and a metric field, then pick a date range to start detecting 
change points in the defined range. Optionally, you can split the data by a 
field. If the cardinality of the split field exceeds 10,000, then only the first 
10,000, sorted by document count, are analyzed. You can configure a maximum of 6 
combinations of a function applied to a metric field, partitioned by a split 
field to identify change points.

When a change point is detected, a row displays basic information including the 
timestamp of the change point, a preview chart, the type of change point, its 
p-value, the name and value of the split field. You can further examine the 
selected change point in a detailed view. A chart visualizes the identified 
change point within the analyzed time window, making the interpretation easier. 
If the analysis is split by a field, a separate chart is shown for every 
partition that has a detected change point. The chart displays the type of 
change point, its value, and the timestamp of the bucket where the change point 
has been detected. The corresponding `p-value` indicates the magnitude of the 
change; lower values indicate more significant changes. You can use the change 
point type selector to filter the results by specific types of change points.

(Figure: user/ml/images/ml-change-point-detection-selected.png)

You can attach change point charts to a dashboard or a case by using the context 
menu. If the split field is selected, you can either select specific charts 
(partitions) or set the maximum number of top change points to plot. It's 
possible to preserve the applied time range or use the time bound from the page 
date picker. You can also add or edit change point charts directly from the 
**Dashboard** app.
