<!-- Converted from reference/api/backup/update-one-snapshot-schedule-by-cluster-id.txt (reStructuredText). Includes are inlined. -->

# Update the Snapshot Schedule

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

## Resource

```http
PATCH /groups/{PROJECT-ID}/backupConfigs/{CLUSTER-ID}/snapshotSchedule
```

## Request Parameters

### Request Path Parameters

| Parameter | Type | Necessity | Description |
|---|---|---|---|
| `PROJECT-ID` | string | Required | Unique identifier for the project that holds the cluster with the snapshot schedule you want to update. |
| `CLUSTER-ID` | string | Required | Unique identifier of the cluster whose snapshot schedule you want to update. |

### Request Query Parameters

The following query parameters are optional:

* - Name
  - Type
  - Necessity
  - Description
  - Default

* - pretty
  - boolean
  - Optional
  - Flag indicating whether the response body should be in a
    prettyprint format.
  - `false`

* - envelope
  - boolean
  - Optional
  - Flag that indicates whether or not to wrap the response in an
    envelope.

    Some API (Application Programming Interface) clients cannot access the HTTP (Hypertext Transfer Protocol) response headers or
    status code. To remediate this, set **envelope=true** in the
    query.

    For endpoints that return one result, the response body
    includes:

    | Name | Description |
    |---|---|
    | status | HTTP (Hypertext Transfer Protocol) response code |
    | envelope | Expected response body |

  - `false`

### Request Body Parameters

* - Name
  - Type
  - Necessity
  - Description

* - `clusterCheckpointIntervalMin`
  - number
  - Optional
  - Number of minutes between successive cluster checkpoints. This
    only applies to sharded clusters. This number determines the
    granularity of point-in-time restores for sharded clusters.
    You can set a value of `15`, `30`, or `60`.

    **Important:**

    You may use checkpoints for clusters that run MongoDB with
    Feature Compatibility Version of 4.0 or earlier. Checkpoints were removed from
    MongoDB instances with FCV (Feature Compatibility Version) of 4.2 or later.

* - `clusterId`
  - string
  - Optional
  - Unique identifier of the cluster to which this backup
    configuration applies.

* - `dailySnapshotRetentionDays`
  - number
  - Optional
  - Number of days to retain daily snapshots. Accepted values are: 
    `0`, `3`, `4`, `5`, `6`, `7`, `15`, `30`, `60`, 
    `90`, `120`, `180`, `360`.

    **Note:**

    Setting `dailySnapshotRetentionDays` to `0` disables this
    rule.

* - `fullIncrementalDayOfWeek`
  - string
  - Optional
  - Day of the week when Ops Manager takes a full snapshot. This
    ensures a recent complete backup. Ops Manager sets the  default
    value to SUNDAY.

* - `groupId`
  - string
  - Optional
  - Unique identifier of the project that owns the backup
    configuration.

* - `links`
  - object array
  - Optional
  - .. include:: /includes/api/links-explanation.rst

* - `monthlySnapshotRetentionMonths`
  - number
  - Optional
  - Number of months to retain monthly snapshots. You can set a
    value between `1` and `36`, inclusive.

    **Note:**

    Setting `monthlySnapshotRetentionMonths` to `0` disables this rule.

* - `pointInTimeWindowHours`
  - number
  - Optional
  - Number of hours in the past for which a point-in-time snapshot
    can be created.

* - `referenceHourOfDay`
  - number
  - Optional
  - Hour of the day to schedule snapshots using a 24 hour clock.
    You can set a value between `0` and `23`, inclusive.

* - `referenceMinuteOfHour`
  - number
  - Optional
  - Minute of the hour to schedule snapshots. You can set a value
    between `0` and `59`, inclusive.

* - `referenceTimeZoneOffset`
  - string
  - Optional
  - The ISO-8601 timezone offset where the Ops Manager host resides. To
    avoid problems with daylight saving time, use UTC (Coordinated Universal Time). The
    default is `+0000`, which is equivalent to UTC (Coordinated Universal Time). `Z` is
    also a supported value and equivalent to UTC (Coordinated Universal Time).

    Ops Manager converts any offset other than `+0000` to 
    `+0000` before storing it, and adjusts the 
    `referenceHourOfDay` value accordingly.

    **Example:**

    You pass in a request with a `referenceHourOfDay` of `5`
    and a `referenceTimeZoneOffset` of ``"+0200". Ops Manager
    stores a `referenceHourOfDay` of `3` and a 
    `referenceTimeZoneOffset` of `"+0000"`.

* - `snapshotIntervalHours`
  - number
  - Optional
  - Number of hours between snapshots. You can set a value of `6`,
    `8`, `12`, or `24`.

* - `snapshotRetentionDays`
  - number
  - Optional
  - Number of days to keep recent snapshots. You can set a value
    between `2` and `5`, inclusive.

* - `weeklySnapshotRetentionWeeks`
  - number
  - Optional
  - Number of weeks to retain weekly snapshots. You can set a value
    between `1` and `52`, inclusive.

    **Note:**

    Setting `weeklySnapshotRetentionWeeks` to `0` disables
    this rule.

## Response

* - Name
  - Type
  - Description

* - `clusterCheckpointIntervalMin`
  - number
  - Number of minutes between successive cluster checkpoints. This
    only applies to sharded clusters. This number determines the
    granularity of point-in-time restores for sharded clusters.
    Ops Manager may return values of `15`, `30`, or `60`.

    **Important:**

    You may use checkpoints for clusters that run MongoDB with
    Feature Compatibility Version of 4.0 or earlier. Checkpoints were removed from
    MongoDB instances with FCV (Feature Compatibility Version) of 4.2 or later.

* - `clusterId`
  - string
  - Unique identifier of the cluster to which this backup
    configuration applies.

* - `dailySnapshotRetentionDays`
  - number
  - Number of days to retain daily snapshots. Ops Manager may return
    values between `1` and `365`, inclusive.

    **Note:**

    Setting `dailySnapshotRetentionDays` to `0` disables this
    rule.

* - `fullIncrementalDayOfWeek`
  - string
  - Day of the week when Ops Manager takes a full snapshot. This
    ensures a recent complete backup. Ops Manager sets the  default
    value to SUNDAY.

* - `groupId`
  - string
  - Unique identifier of the project that owns the backup
    configuration.

* - `links`
  - object array
  - .. include:: /includes/api/links-explanation.rst

* - `monthlySnapshotRetentionMonths`
  - number
  - Number of months to retain monthly snapshots. Ops Manager may return
    values between `1` and `36`, inclusive.

    **Note:**

    Setting `monthlySnapshotRetentionMonths` to `0` disables this rule.

* - `pointInTimeWindowHours`
  - number
  - Number of hours in the past for which a point-in-time snapshot
    can be created.

* - `referenceHourOfDay`
  - number
  - Hour of the day to schedule snapshots using a 24 hour clock.
    Ops Manager may return values between `0` and `23`, inclusive.

* - `referenceMinuteOfHour`
  - number
  - Minute of the hour to schedule snapshots. Ops Manager may return
    values between `0` and `59`, inclusive.

* - `referenceTimeZoneOffset`
  - string
  - The ISO-8601 timezone offset where the Ops Manager host resides. To
    avoid problems with daylight saving time, use UTC (Coordinated Universal Time). The
    default is `+0000`, which is equivalent to UTC (Coordinated Universal Time). `Z` is
    also a supported value and equivalent to UTC (Coordinated Universal Time).

    Ops Manager converts any offset other than `+0000` to 
    `+0000` before storing it, and adjusts the 
    `referenceHourOfDay` value accordingly.

    **Example:**

    You pass in a request with a `referenceHourOfDay` of `5`
    and a `referenceTimeZoneOffset` of ``"+0200". Ops Manager
    stores a `referenceHourOfDay` of `3` and a 
    `referenceTimeZoneOffset` of `"+0000"`.

* - `snapshotIntervalHours`
  - number
  - Number of hours between snapshots. Ops Manager may return values of
    `6`, `8`, `12`, or `24`.

* - `snapshotRetentionDays`
  - number
  - Number of days to keep recent snapshots. Ops Manager may return values
    between `2` and `5`, inclusive.

* - `weeklySnapshotRetentionWeeks`
  - number
  - Number of weeks to retain weekly snapshots. Ops Manager may return
    values between `1` and `52`, inclusive.

    **Note:**

    Setting `weeklySnapshotRetentionWeeks` to `0` disables
    this rule.

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --header "Accept: application/json" \
     --header "Content-Type: application/json" \
     --include \
     --request PATCH "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/backupConfigs/{CLUSTER-ID}/snapshotSchedule" \
     --data '
       {
         "fullIncrementalDayOfWeek":"TUESDAY"
         "snapshotIntervalHours": 8,
         "dailySnapshotRetentionDays": 15,
         "monthlySnapshotRetentionMonths": 6
       }'
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
  "clusterId" : "{CLUSTER-ID}",
  "dailySnapshotRetentionDays" : 15,
  "fullIncrementalDayOfWeek":"TUESDAY",
  "groupId" : "{PROJECT-ID}",
  "links" : [],
  "monthlySnapshotRetentionMonths" : 6,
  "pointInTimeWindowHours": 24,
  "snapshotIntervalHours" : 8,
  "snapshotRetentionDays" : 2,
  "weeklySnapshotRetentionWeeks" : 4
}
```
