<!-- Converted from ml/anomaly-detection/ml-delayed-data-detection.asciidoc (AsciiDoc). Includes are inlined. -->

# Handling delayed data

Delayed data are documents that are indexed late. That is to say, it is data 
related to a time that your datafeed has already processed and it is therefore
never analyzed by your anomaly detection job.

When you create a datafeed, you can specify a
[`query_delay`](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/ml-put-datafeed.html#ml-put-datafeed-request-body) setting.
This setting enables the datafeed to wait for some time past real-time, which
means any "late" data in this period is fully indexed before the datafeed tries
to gather it. However, if the setting is set too low, the datafeed may query for
data before it has been indexed and consequently miss that document. Conversely,
if it is set too high, analysis drifts farther away from real-time. The balance
that is struck depends upon each use case and the environmental factors of the
cluster.

**Important:** If you get an error that says
`Datafeed missed XXXX documents due to ingest latency`, consider increasing 
the value of `query_delay'. If it doesn't help, investigate the ingest latency and its 
cause. You can do this by comparing event and ingest timestamps. High latency 
is often caused by bursts of ingested documents, misconfiguration of the ingest 
pipeline, or misalignment of system clocks.

## Why worry about delayed data?

If data are delayed randomly (and consequently are missing from analysis), the
results of certain types of functions are not really affected. In these
situations, it all comes out okay in the end as the delayed data is distributed
randomly. An example would be a `mean` metric for a field in a large collection
of data. In this case, checking for delayed data may not provide much benefit.
If data are consistently delayed, however, anomaly detection jobs with a `low_count`
function may provide false positives. In this situation, it would be useful to
see if data comes in after an anomaly is recorded so that you can determine a
next course of action.

## How do we detect delayed data?

In addition to the `query_delay` field, there is a delayed data check config,
which enables you to configure the datafeed to look in the past for delayed data.
Every 15 minutes or every `check_window`, whichever is smaller, the datafeed
triggers a document search over the configured indices. This search looks over a
time span with a length of `check_window` ending with the latest finalized bucket.
That time span is partitioned into buckets, whose length equals the bucket span
of the associated anomaly detection job. The `doc_count` of those buckets are then
compared with the job's finalized analysis buckets to see whether any data has
arrived since the analysis. If there is indeed missing data due to their ingest
delay, the end user is notified. For example, you can see annotations in Kibana
for the periods where these delays occur:

(Figure: images/ml-annotations.png)

**Important:**
The delayed data check will not work correctly in the following cases:

* if the datafeed uses aggregations that filter data,
* if the datafeed uses aggregations and the job's `analysis_config` does not have
its `summary_count_field_name` set to `doc_count`,
* if the datafeed is _not_ using aggregations and `summary_count_field_name` is
set to any value.

If the datafeed is using aggregations, set the job's `summary_count_field_name`
to `doc_count`. If `summary_count_field_name` is set to any value other than
`doc_count`, the delayed data check for the datafeed must be disabled.
There is another tool for visualizing the delayed data on the *Annotations* tab
in the anomaly detection job management page:

(Figure: images/ml-datafeed-chart.png)

## What to do about delayed data?

The most common course of action is to simply to do nothing. For many functions
and situations, ignoring the data is acceptable. However, if the amount of
delayed data is too great or the situation calls for it, the next course of
action to consider is to increase the `query_delay` of the datafeed. This
increased delay allows more time for data to be indexed. If you have real-time
constraints, however, an increased delay might not be desirable. In which case,
you would have to [tune for better indexing speed](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/tune-for-indexing-speed.html).
