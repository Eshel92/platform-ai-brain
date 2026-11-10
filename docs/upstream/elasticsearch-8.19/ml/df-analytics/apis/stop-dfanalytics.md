<!-- Converted from ml/df-analytics/apis/stop-dfanalytics.asciidoc (AsciiDoc). Includes are inlined. -->

# Stop {dfanalytics-jobs} API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  {dfanalytics} APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-data-frame).

Stops one or more {dfanalytics-jobs}.

## Request

`POST _ml/data_frame/analytics/<data_frame_analytics_id>/_stop` +

`POST _ml/data_frame/analytics/<data_frame_analytics_id>,<data_frame_analytics_id>/_stop` +

`POST _ml/data_frame/analytics/_all/_stop`

## Prerequisites

Requires the `manage_ml` cluster privilege. This privilege is included in the 
`machine_learning_admin` built-in role.

## Description

A {dfanalytics-job} can be started and stopped multiple times throughout its 
lifecycle.

You can stop multiple {dfanalytics-jobs} in a single API request by using a 
comma-separated list of {dfanalytics-jobs} or a wildcard expression. You can 
stop all {dfanalytics-job} by using _all or by specifying * as the 
<data_frame_analytics_id>.

## Path parameters

`<data_frame_analytics_id>`::
(Required, string)
Identifier for the {dfanalytics-job}. This identifier can contain lowercase
alphanumeric characters (a-z and 0-9), hyphens, and underscores. It must start
and end with alphanumeric characters.

## Query parameters  

  
`allow_no_match`::
(Optional, Boolean) 
 Specifies what to do when the request:
* Contains wildcard expressions and there are no {dfanalytics-jobs} that match.
* Contains the `_all` string or no identifiers and there are no matches.
* Contains wildcard expressions and there are only partial matches.

The default value is `true`, which returns an empty `data_frame_analytics` array
when there are no matches and the subset of results when there are partial
matches. If this parameter is `false`, the request returns a `404` status code
when there are no matches or only partial matches.
`force`::
  (Optional, Boolean) If true, the {dfanalytics-job} is stopped forcefully.
  
`timeout`::
(Optional, time units) 
Controls the amount of time to wait until the {dfanalytics-job} stops. Defaults
to 20 seconds.

## Examples

The following example stops the `loganalytics` {dfanalytics-job}:

```console
POST _ml/data_frame/analytics/loganalytics/_stop
```

When the {dfanalytics-job} stops, you receive the following results:

```console-result
{
  "stopped" : true
}
```
