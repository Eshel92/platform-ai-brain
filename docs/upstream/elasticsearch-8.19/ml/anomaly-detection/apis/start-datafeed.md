<!-- Converted from ml/anomaly-detection/apis/start-datafeed.asciidoc (AsciiDoc). Includes are inlined. -->

# Start datafeeds API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Starts one or more datafeeds.

## Request

`POST _ml/datafeeds/<feed_id>/_start`

## Prerequisites

* Before you can start a datafeed, the anomaly detection job must be open. Otherwise, an
error occurs.
* Requires the `manage_ml` cluster privilege. This privilege is included in the 
`machine_learning_admin` built-in role.

## Description

A datafeed must be started in order to retrieve data from Elasticsearch.
A datafeed can be started and stopped multiple times throughout its lifecycle.

If you restart a stopped datafeed, by default it continues processing input data
from the next millisecond after it was stopped. If new data was indexed for that
exact millisecond between stopping and starting, it will be ignored.

**Important:** When Elasticsearch security features are enabled, your datafeed remembers
which roles the last user to create or update it had at the time of
creation/update and runs the query using those same roles. If you provided
secondary authorization headers when
you created or updated the datafeed, those credentials are used instead.

## Path parameters

`<feed_id>`::
(Required, string)
A numerical character string that uniquely identifies the
datafeed. This identifier can contain lowercase alphanumeric characters (a-z
and 0-9), hyphens, and underscores. It must start and end with alphanumeric
characters.

## Query parameters

`end`::
(Optional, string) The time that the datafeed should end, which can be
specified by using one of the following formats:
* ISO 8601 format with milliseconds, for example `2017-01-22T06:00:00.000Z`
* ISO 8601 format without milliseconds, for example `2017-01-22T06:00:00+00:00`
* Milliseconds since the epoch, for example `1485061200000`
 
Date-time arguments using either of the ISO 8601 formats must have a time zone
designator, where `Z` is accepted as an abbreviation for UTC time.
  
**Note:** When a URL is expected (for example, in browsers), the `+` used in time
zone designators must be encoded as `%2B`.
  
This value is exclusive. If you do not specify an end time, the datafeed runs
continuously.

`start`::
(Optional, string) The time that the datafeed should begin, which can be
specified by using the same formats as the `end` parameter. This value is
inclusive.
If you do not specify a start time and the datafeed is associated with a new
anomaly detection job, the analysis starts from the earliest time for which data is
available.
If you restart a stopped datafeed and specify a `start` value that is earlier
than the timestamp of the latest processed record, the datafeed continues from
1 millisecond after the timestamp of the latest processed record.

`timeout`::
(Optional, time) Specifies the amount of time to wait until a datafeed starts.
The default value is 20 seconds.

## Request body

You can also specify the query parameters (such as `end` and `start`)
in the request body.

## Response body

`node`::
  (string) The ID of the node that the datafeed was started on. If the datafeed is
  allowed to open lazily and has not yet been assigned to a node, this value is
  an empty string.

`started`::
  (Boolean) For a successful response, this value is always `true`. On failure, an
  exception is returned instead.

## Examples

```console
POST _ml/datafeeds/datafeed-low_request_rate/_start
{
  "start": "2019-04-07T18:22:16Z"
}
```

When the datafeed starts, you receive the following results:

```console-result
{
  "started" : true,
  "node" : "node-1"
}
```
