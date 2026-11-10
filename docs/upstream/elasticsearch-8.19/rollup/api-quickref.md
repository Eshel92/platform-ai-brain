<!-- Converted from rollup/api-quickref.asciidoc (AsciiDoc). Includes are inlined. -->

### {rollup-cap} API quick reference

deprecated::[8.11.0,"Rollups will be removed in a future version. Please migrate to downsampling instead."]

Most rollup endpoints have the following base:

```js
/_rollup/
```

#### /job/

* [PUT /_rollup/job/<job_id+>+](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rollup-put-job.html): Create a {rollup-job}
* [GET /_rollup/job](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rollup-get-job.html): List {rollup-jobs}
* [GET /_rollup/job/<job_id+>+](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rollup-get-job.html): Get {rollup-job} details
* [POST /_rollup/job/<job_id>/_start](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rollup-start-job.html): Start a {rollup-job}
* [POST /_rollup/job/<job_id>/_stop](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rollup-stop-job.html): Stop a {rollup-job}
* [DELETE /_rollup/job/<job_id+>+](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rollup-delete-job.html): Delete a {rollup-job}

#### /data/

* [GET /_rollup/data/<index_pattern+>/_rollup_caps+](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rollup-get-rollup-caps.html): Get Rollup Capabilities
* [GET /<index_name+>/_rollup/data/+](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rollup-get-rollup-index-caps.html): Get Rollup Index Capabilities

#### /<index_name>/

* [GET /<index_name>/_rollup_search](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rollup-search.html): Search rollup data
