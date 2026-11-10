<!-- Converted from transform/limitations.asciidoc (AsciiDoc). Includes are inlined. -->

# Transform limitations

The following limitations and known problems apply to the {version} release of 
the Elastic transform feature. The limitations are grouped into the following 
categories:

* transform-config-limitations apply to the configuration process of the 
  transforms.
* transform-operational-limitations affect the behavior of the transforms 
  that are running.
* transform-ui-limitations only apply to transforms managed via the user 
  interface.

## Configuration limitations

### Field names prefixed with underscores are omitted from latest transforms

If you use the `latest` type of transform and the source index has field names
that start with an underscore (_) character, they are assumed to be internal
fields. Those fields are omitted from the documents in the destination index.

### Transforms support cross-cluster search if the remote cluster is configured properly

If you use cross-cluster search, the remote cluster must 
support the search and aggregations you use in your transforms. 
Transforms validate their configuration; if you use cross-cluster search and the 
validation fails, make sure that the remote cluster supports the query and 
aggregations you use.

### Using scripts in transforms

Transforms support scripting in every case when aggregations support them. 
However, there are certain factors you might want to consider when using scripts 
in transforms:

* Transforms cannot deduce index mappings for output fields when the 
  fields are created by a script. In this case, you might want to create the 
  mappings of the destination index yourself prior to creating the transform.

* Scripted fields may increase the runtime of the transform.
  
* Transforms cannot optimize queries when you use scripts for all the 
  groupings defined in `group_by`, you will receive a warning message when you 
  use scripts this way.

### Deprecation warnings for Painless scripts in transforms

If a transform contains Painless scripts that use deprecated syntax, 
deprecation warnings are displayed when the transform is previewed or started. 
However, it is not possible to check for deprecation warnings across all 
transforms as a bulk action because running the required queries might be a 
resource intensive process. Therefore any deprecation warnings due to deprecated 
Painless syntax are not available in the Upgrade Assistant.

### Transforms perform better on indexed fields

Transforms sort data by a user-defined time field, which is frequently 
accessed. If the time field is a [runtime field](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/runtime.html), the 
performance impact of calculating field values at query time can significantly 
slow the transform. Use an indexed field as a time field when using 
transforms.

### {ctransform-cap} scheduling limitations

A {ctransform} periodically checks for changes to source data. The functionality
of the scheduler is currently limited to a basic periodic timer which can be 
within the `frequency` range from 1s to 1h. The default is 1m. This is designed 
to run little and often. When choosing a `frequency` for this timer consider 
your ingest rate along with the impact that the transform 
search/index operations has other users in your cluster. Also note that retries 
occur at `frequency` interval.

## Operational limitations

### Aggregation responses may be incompatible with destination index mappings

When a pivot transform is first started, it will deduce the mappings 
required for the destination index. This process is based on the field types of 
the source index and the aggregations used. If the fields are derived from 
`scripted_metrics`
or `bucket_scripts`, 
dynamic mappings will be used. In some instances the 
deduced mappings may be incompatible with the actual data. For example, numeric 
overflows might occur or dynamically mapped fields might contain both numbers 
and strings. Please check Elasticsearch logs if you think this may have occurred. 

You can view the deduced mappings by using the 
preview transform API.
See the `generated_dest_index` object in the API response.

If it's required, you may define custom mappings prior to starting the 
transform by creating a custom destination index using the 
create index API.
As deduced mappings cannot be overwritten by an index template, use the create 
index API to define custom mappings. The index templates only apply to fields 
derived from scripts that use dynamic mappings. 

### Batch transforms may not account for changed documents

A batch transform uses a 
composite aggregation
which allows efficient pagination through all buckets. Composite aggregations 
do not yet support a search context, therefore if the source data is changed 
(deleted, updated, added) while the batch data frame is in progress, then the 
results may not include these changes.

### {ctransform-cap} consistency does not account for deleted or updated documents

While the process for transforms allows the continual recalculation of the 
transform as new data is being ingested, it does also have some limitations.

Changed entities will only be identified if their time field has also been 
updated and falls within the range of the action to check for changes. This has 
been designed in principle for, and is suited to, the use case where new data is 
given a timestamp for the time of ingest. 

If the indices that fall within the scope of the source index pattern are 
removed, for example when deleting historical time-based indices, then the 
composite aggregation performed in consecutive checkpoint processing will search 
over different source data, and entities that only existed in the deleted index 
will not be removed from the data frame destination index.

Depending on your use case, you may wish to recreate the transform entirely 
after deletions. Alternatively, if your use case is tolerant to historical 
archiving, you may wish to include a max ingest timestamp in your aggregation. 
This will allow you to exclude results that have not been recently updated when 
viewing the destination index.

### Deleting a transform does not delete the destination index or Kibana index pattern

When deleting a transform using `DELETE _transform/index` 
neither the destination index nor the Kibana index pattern, should one have been 
created, are deleted. These objects must be deleted separately.

### Handling dynamic adjustment of aggregation page size

During the development of transforms, control was favoured over performance. 
In the design considerations, it is preferred for the transform to take longer 
to complete quietly in the background rather than to finish quickly and take 
precedence in resource consumption.

Composite aggregations are well suited for high cardinality data enabling 
pagination through results. If a circuit breaker memory
exception occurs when performing the composite aggregated search then we try
again reducing the number of buckets requested. This circuit breaker is
calculated based upon all activity within the cluster, not just activity from 
transforms, so it therefore may only be a temporary resource 
availability issue.

For a batch transform, the number of buckets requested is only ever adjusted 
downwards. The lowering of value may result in a longer duration for the 
transform checkpoint to complete. For {ctransforms}, the number of buckets 
requested is reset back to its default at the start of every checkpoint and it 
is possible for circuit breaker exceptions to occur repeatedly in the Elasticsearch logs. 

The transform retrieves data in batches which means it calculates several 
buckets at once. Per default this is 500 buckets per search/index operation. The 
default can be changed using `max_page_search_size` and the minimum value is 10. 
If failures still occur once the number of buckets requested has been reduced to 
its minimum, then the transform will be set to a failed state.

### Handling dynamic adjustments for many terms

For each checkpoint, entities are identified that have changed since the last 
time the check was performed. This list of changed entities is supplied as a 
terms query to the transform composite aggregation,
one page at a time. Then updates are applied to the destination index for each
page of entities.

The page `size` is defined by `max_page_search_size` which is also used to 
define the number of buckets returned by the composite aggregation search. The 
default value is 500, the minimum is 10.

The index setting `index.max_terms_count` defines 
the maximum number of terms that can be used in a terms query. The default value 
is 65536. If `max_page_search_size` exceeds `index.max_terms_count` the 
transform will fail. 

Using smaller values for `max_page_search_size` may result in a longer duration 
for the transform checkpoint to complete.

### Handling of failed transforms

Failed transforms remain as a persistent task and should be handled 
appropriately, either by deleting it or by resolving the root cause of the 
failure and re-starting.

When using the API to delete a failed transform, first stop it using 
`_stop?force=true`, then delete it.

### {ctransforms-cap} may give incorrect results if documents are not yet available to search

After a document is indexed, there is a very small delay until it is available 
to search.

A {ctransform} periodically checks for changed entities between the time since 
it last checked and `now` minus `sync.time.delay`. This time window moves 
without overlapping. If the timestamp of a recently indexed document falls 
within this time window but this document is not yet available to search then 
this entity will not be updated.

If using a `sync.time.field` that represents the data ingest time and using a 
zero second or very small `sync.time.delay`, then it is more likely that this 
issue will occur.

### Support for date nanoseconds data type

If your data uses the date nanosecond data type, aggregations
are nonetheless on millisecond resolution. This limitation also affects the
aggregations in your transforms.

### Data streams as destination indices are not supported

Transforms update data in the destination index which requires writing 
into the destination. data-streams are designed to be append-only, which 
means you cannot send update or delete requests directly to a data stream. For 
this reason, data streams are not supported as destination indices for 
transforms.

### ILM as destination index may cause duplicated documents

ILM is not recommended to use as a transform 
destination index. Transforms update documents in the current destination, 
and cannot delete documents in the indices previously used by ILM. This may lead 
to duplicated documents when you use transforms combined with ILM in case of a 
rollover.

If you use ILM to have time-based indices, please consider using the 
date-index-name-processor instead. The processor works without duplicated 
documents if your transform contains a `group_by` based on `date_histogram`.

## Limitations in Kibana

### Transforms are visible in all Kibana spaces

[Spaces](https://www.elastic.co/guide/en/kibana/8.19/xpack-spaces.html) enable you to organize your source and 
destination indices and other saved objects in Kibana and to see only the objects 
that belong to your space. However, a transform is a long running task which 
is managed on cluster level and therefore not limited in scope to certain 
spaces. Space awareness can be implemented for a {data-source} under 
**Stack Management > Kibana** which allows privileges to the transform 
destination index.

### Up to 1,000 transforms are listed in Kibana

The transforms management page in Kibana lists up to 1000 transforms.

### Kibana might not support every transform configuration option

There might be configuration options available via the transform APIs that are 
not supported in Kibana. For an exhaustive list of configuration options, refer 
to the documentation.
