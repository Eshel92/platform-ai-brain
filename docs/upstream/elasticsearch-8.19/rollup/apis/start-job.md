<!-- Converted from rollup/apis/start-job.asciidoc (AsciiDoc). Includes are inlined. -->

### Start {rollup-jobs} API

deprecated::[8.11.0,"Rollups will be removed in a future version. Use downsampling instead."]

**New API reference**
For the most up-to-date API details, refer to [Rollup APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-rollup).

Starts an existing, stopped {rollup-job}.

#### Request

`POST _rollup/job/<job_id>/_start`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have `manage` or
`manage_rollup` cluster privileges to use this API. For more information, see
security-privileges.

#### Description

If you try to start a job that does not exist, an exception occurs. If you try
to start a job that is already started, nothing happens.

#### Path parameters

`<job_id>`::
  (Required, string) Identifier for the {rollup-job}.

#### Response codes

 `404` (Missing resources)::
 This code indicates that there are no resources that match the request. It
 occurs if you try to start a job that doesn't exist.

#### Examples

If we have already created a {rollup-job} named `sensor`, it can be started with:

```console
POST _rollup/job/sensor/_start
```

Which will return the response:

```console-result
{
  "started": true
}
```
