<!-- Part 3 of 3 of ml/ml-shared.md (split because the page is big). -->

job must be opened before it can accept further data.
* `closing`: The job close action is in progress and has not yet completed. A
closing job cannot accept further data.
* `failed`: The job did not finish successfully due to an error. This situation
can occur due to invalid input data, a fatal error occurring during the
analysis, or an external interaction such as the process being killed by the
Linux out of memory (OOM) killer. If the job had irrevocably failed, it must be
force closed and then deleted. If the datafeed can be corrected, the job can be
closed and then re-opened.
* `opened`: The job is available to receive and process data.
* `opening`: The job open action is in progress and has not yet completed.
end::state-anomaly-job[]

tag::state-datafeed[]
The status of the datafeed, which can be one of the following values:
* `starting`: The datafeed has been requested to start but has not yet started.
* `started`: The datafeed is actively receiving data.
* `stopping`: The datafeed has been requested to stop gracefully and is
completing its final action.
* `stopped`: The datafeed is stopped and will not receive data until it is
re-started.
end::state-datafeed[]

tag::summary-count-field-name[]
If this property is specified, the data that is fed to the job is expected to be
pre-summarized. This property value is the name of the field that contains the
count of raw data points that have been summarized. The same
`summary_count_field_name` applies to all detectors in the job.
**Note:** The `summary_count_field_name` property cannot be used with the `metric`
function.

end::summary-count-field-name[]

tag::tags[]
A comma delimited string of tags. A trained model can have many tags, or none.
When supplied, only trained models that contain all the supplied tags are
returned.
end::tags[]

tag::timeout-start[]
Controls the amount of time to wait until the {dfanalytics-job} starts. Defaults
to 20 seconds.
end::timeout-start[]

tag::timeout-stop[]
Controls the amount of time to wait until the {dfanalytics-job} stops. Defaults
to 20 seconds.
end::timeout-stop[]

tag::time-format[]
The time format, which can be `epoch`, `epoch_ms`, or a custom pattern. The
default value is `epoch`, which refers to UNIX or Epoch time (the number of
seconds since 1 Jan 1970). The value `epoch_ms` indicates that time is measured
in milliseconds since the epoch. The `epoch` and `epoch_ms` time formats accept
either integer or real values. +
**Note:** Custom patterns must conform to the Java `DateTimeFormatter` class.
When you use date-time formatting patterns, it is recommended that you provide
the full date, time and time zone. For example: `yyyy-MM-dd'T'HH:mm:ssX`.
If the pattern that you specify is not sufficient to produce a complete
timestamp, job creation fails.
end::time-format[]

tag::time-span[]
The time span that each search will be querying. This setting is only applicable
when the mode is set to `manual`. For example: `3h`.
end::time-span[]

tag::timestamp-results[]
The start time of the bucket for which these results were calculated.
end::timestamp-results[]

tag::tokenizer[]
The name or definition of the tokenizer to use after
character filters are applied. This property is compulsory if
`categorization_analyzer` is specified as an object. Machine learning provides
a tokenizer called `ml_standard` that tokenizes in a way that has been
determined to produce good categorization results on a variety of log
file formats for logs in English. If you want to use that tokenizer but
change the character or token filters, specify `"tokenizer": "ml_standard"`
in your `categorization_analyzer`. Additionally, the `ml_classic` tokenizer
is available, which tokenizes in the same way as the non-customizable
tokenizer in old versions of the product (before 6.2). `ml_classic` was
the default categorization tokenizer in versions 6.2 to 7.13, so if you
need categorization identical to the default for jobs created in these
versions, specify `"tokenizer": "ml_classic"` in your `categorization_analyzer`.

**Note:** From Elasticsearch 8.10.0,  a new version number is used to
track the configuration and state changes in the machine learning plugin. This new
version number is decoupled from the product version and will increment
independently.
end::tokenizer[]

tag::total-by-field-count[]
The number of `by` field values that were analyzed by the models. This value is
cumulative for all detectors in the job.
end::total-by-field-count[]

tag::total-category-count[]
The number of categories created by categorization.
end::total-category-count[]

tag::total-over-field-count[]
The number of `over` field values that were analyzed by the models. This value
is cumulative for all detectors in the job.
end::total-over-field-count[]

tag::total-partition-field-count[]
The number of `partition` field values that were analyzed by the models. This
value is cumulative for all detectors in the job.
end::total-partition-field-count[]

tag::training-percent[]
Defines what percentage of the eligible documents that will
be used for training. Documents that are ignored by the analysis (for example
those that contain arrays with more than one value) won’t be included in the
calculation for used percentage. Defaults to `100`.
end::training-percent[]

tag::use-null[]
Defines whether a new series is used as the null series when there is no value
for the by or partition fields. The default value is `false`.
end::use-null[]

tag::verbose[]
Defines whether the stats response should be verbose. The default value is `false`.
end::verbose[]
