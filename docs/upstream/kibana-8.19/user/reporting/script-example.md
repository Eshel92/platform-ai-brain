<!-- Converted from user/reporting/script-example.asciidoc (AsciiDoc). Includes are inlined. -->

To automatically generate reports from a script, make a request to the `POST` URL. The request returns a JSON and contains a `path` property with a
URL that you use to download the report. Use the `GET` method in the HTTP request to download the report.

To queue CSV report generation using the `POST` URL with cURL:

```curl
curl \
-XPOST \ <1>
-u elastic \ <2>
-H 'kbn-xsrf: true' \ <3>
'<KIBANA_HOST>:5601/api/reporting/generate/csv?jobParams=...' <4>
```

<1> The required `POST` method.
<2> The user credentials for a user with permission to access Kibana and {report-features}.
<3> The required `kbn-xsrf` header for all `POST` requests to Kibana. For more information, refer to API Request Headers.
<4> The POST URL. You can copy and paste the URL for any report.

An example response for a successfully queued report:

```js
{
  "path": "/api/reporting/jobs/download/jxzaofkc0ykpf4062305t068", <1>
  "job": {
    "id": "jxzaofkc0ykpf4062305t068",
    "index": ".reporting-2018.11.11",
    "jobtype": "csv",
    "created_by": "elastic",
    "payload": ..., <2>
    "timeout": 120000,
    "max_attempts": 3
  }
}
```

<1> The relative path on the Kibana host for downloading the report.
<2> (Not included in the example) Internal representation of the reporting job, as found in the `.reporting-*` storage.
