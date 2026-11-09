<!-- Converted from reference/api/measures/get-host-process-system-measurements.txt (reStructuredText). Includes are inlined. -->

# Get Host, Process, System Measurements

Host measurements provide data on the state of the MongoDB process.
The Monitoring collects host measurements through the MongoDB
serverStatus and
dbStats commands.

System and process measurements provide data on the CPU usage of the
hosts that run MongoDB. The Automation collects these
measurements. System and process measurements require Ops Manager Automation.

This endpoint returns these /reference/api/measures/measurement-types.

**Note:**

To calculate some metric series, Ops Manager takes the rate between every 
two adjacent points. For these metric series, the first data point 
has a null value because Ops Manager can't calculate a rate for the first 
data point given the query time range.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/measurements?granularity={ISO-8601-PERIOD}&period={ISO-8601-PERIOD}
```

### Request Path Parameters

| Name | Type | Description |
|---|---|---|
| PROJECT-ID | string | Unique identifier of the `project` that owns the host. |
| HOST-ID | string | Unique identifier of the host that serves the MongoDB process. |

### Request Query Parameters

#### Unique Query Parameters

This endpoint accepts the following query parameters to filter
returned measurements:

* - Name
  - Type
  - Description

* - | granularity
    | *Required*
  - string
  - Duration in ISO 8601 notation that specifies the interval between
    measurement data points.

    Measurement granularity can be expressed as days, hours, minutes, seconds and milliseconds using the following notation:

    `P` (for *period*) followed by:

    - `D` for *days* (if desired)
    - `T` for *time* (after *days*)
    - `H` for *hours*
    - `M` for *minutes*
    - `S` for *seconds*

    For example:

    | Notation | Duration |
    |---|---|
    | `PT30S` | 30 seconds |
    | `P1T12H` | 1 day, 12 hours |
    | `PT0.5S` | 500 milliseconds |

* - period
  - string
  - Duration in ISO 8601 notation that specifies how far back in the past to
    retrieve measurements.

    For example, to request the last 36 hours, include this query
    parameter: `period=P1DT12H`.

* - start
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) for the beginning of the period for which to
    retrieve measurements. If you specify `start` you must also
    specify `end`.

* - end
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) for the end of the period for which to retrieve
    measurements. If you specify `end` you must also specify
    `start`.

* - m
  - string
  - Measurements to return. If `m` is not specified, all
    measurements are returned.

    To specify multiple values for `m`, you must repeat the `m`
    parameter.

    For example:

    ```none
    ../measurements?m=CONNECTIONS&m=OPCOUNTER_CMD&m=OPCOUNTER_QUERY
    ```

    You must specify measurements that are valid for the host. Ops Manager
    returns an error if any specified measurements are invalid
    For available measurements, see /reference/api/measures/measurement-types.

**Note:**

Each measurement request must include either the
`period` query parameter
or both the `start` and `end` query parameters.

#### Common Query Parameters

This endpoint also accepts the query parameters common to all endpoints
that return a single response:

* - Name
  - Type
  - Description
  - Default

* - pageNum
  - integer
  - Page number (1-index based).
  - `1`

* - itemsPerPage
  - integer
  - Number of items to return per page, up to a maximum of 500.
  - `100`

* - pretty
  - boolean
  - Indicates whether the response body should be in a
    prettyprint format.
  - `false`

* - envelope
  - boolean
  - Indicates whether or not to wrap the response in an envelope.

    Some API (Application Programming Interface) clients cannot access the HTTP (Hypertext Transfer Protocol) response headers or
    status code. To remediate this, set `"envelope" : true` in the
    query.

    For endpoints that return one result, response body
    includes:

    | status | HTTP (Hypertext Transfer Protocol) response code |
    |---|---|
    | envelope | Expected response body |

    For endpoints that return a list of results, the `results`
    object is an envelope. Ops Manager adds the `status` field to the
    response body.
  - None

### Request Body Parameters

This endpoint doesn't use HTTP request body parameters.

## Response

* - Name
  - Type
  - Description

* - databaseName
  - string
  - Database to which the measurement applies. 

    Populated for Get Database Measurements only.

* - end
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) for the end of the period the returned
    measurements cover.

* - granularity
  - string
  - Duration in ISO 8601 notation that specifies the size of the interval that
    each data point covers.

    For example, `PT5M` specifies a 5-minute granularity.

* - groupId
  - string
  - Unique identifier of the project that owns the host.

* - hostId
  - string
  - Unique identifier of the host to which the measurements pertain.

* - measurements
  - object array
  - Each object in this array represents a measurement and the data
    points for that measurement.

* - measurements.dataPoints
  - object array
  - Each object represents a single data point. If there is no data
    point available for a particular moment in time, this `value`
    is set to `null`.

* - measurements.dataPoints.timestamp
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) for the beginning of the time interval this data
    point represents.

* - measurements.dataPoints.value
  - float
  - Value of this data point.

* - measurements.name
  - string
  - Name of the measurement. Accepted values are given in the
    /reference/api/measures/measurement-types page.

* - measurements.units
  - string
  - How this measurement is quantified. Accepted units are:

    - `PERCENT`
    - `MILLISECONDS`
    - `BYTES`
    - `GIGABYTES`
    - `BYTES_PER_SECOND`
    - `MEGABYTES_PER_SECOND`
    - `GIGABYTES_PER_HOUR`
    - `SCALAR_PER_SECOND`
    - `SCALAR`

* - partitionName
  - string
  - Name of the disk partition that stores the MongoDB process
    database.

    Populated for Get Disk Partition Measurements only.

* - processId
  - string
  - FQDN (fully qualified domain name) and port of the MongoDB process.

* - start
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) for the beginning of the period the returned
    measurements cover.

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --header "Accept: application/json" \
     --include \
     --request GET "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/hosts/{HOST-ID}/measurements?granularity={TIME-INCREMENT}&period={PERIOD}}&pretty=true"
```

## Example Response

### Response Header

```http
HTTP/1.1 401 Unauthorized
Content-Type: application/json;charset=ISO-8859-1
Date: {dateInUnixFormat}
WWW-Authenticate: Digest realm="MMS Public API", domain="", nonce="{nonce}", algorithm=MD5, op="auth", stale=false
Content-Length: {requestLengthInBytes}
Connection: keep-alive
```

```http
HTTP/1.1 200 OK
Vary: Accept-Encoding
Content-Type: application/json
Strict-Transport-Security: max-age=300
Date: {dateInUnixFormat}
Connection: keep-alive
Content-Length: {requestLengthInBytes}
X-MongoDB-Service-Version: gitHash={gitHash}; versionString={ApplicationVersion}
```

### Response Body

```json
{
  "end": "2022-05-12T18:28:19Z",
  "granularity": "{TIME-INCREMENT}",
  "groupId": "{PROJECT-ID}",
  "hostId": "{HOST-ID}",
  "links": [ ],
  "measurements": [{
    "dataPoints": [{
      "timestamp" : "2022-05-12T18:28:10Z",
      "value": 5.0
    }],
    "name": "CONNECTIONS",
    "units": "SCALAR"
  }, {
    "dataPoints": [{
      "timestamp": "2022-05-12T18:28:10Z",
      "value": 15.699934824278714
    }],
    "name": "NETWORK_BYTES_IN",
    "units": "BYTES_PER_SECOND"
  },

  .
  .
  .

  , {
    "dataPoints": [],
    "name": "SYSTEM_NORMALIZED_CPU_SOFTIRQ",
    "units": "PERCENT"
  }, {
    "dataPoints": [],
    "name": "SYSTEM_NORMALIZED_CPU_GUEST",
    "units": "PERCENT"
  }, {
    "dataPoints": [],
    "name": "SYSTEM_NORMALIZED_CPU_STEAL",
    "units": "PERCENT"
  }],
  "processId": "{MONGODB-PROCESS-FQDN}:{PORT}",
  "start": "2022-05-12T18:28:10Z"
}
```
