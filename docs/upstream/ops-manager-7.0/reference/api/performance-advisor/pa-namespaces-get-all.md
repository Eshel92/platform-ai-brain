<!-- Converted from reference/api/performance-advisor/pa-namespaces-get-all.txt (reStructuredText). Includes are inlined. -->

# Get Namespaces for a Project

Retrieve namespaces for collections experiencing slow queries
on a specified host. Namespaces appear in the following format:
`{database}.{collection}`.

**Note:**

If you specify a secondary member of a replica set
that has not received any database read operations, the endpoint
does not return any namespaces.

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```none
GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/performanceAdvisor/namespaces
```

### Request Path Parameters

| Path Element | Description |
|---|---|
| `PROJECT-ID` | The unique identifier for the project where the the MongoDB host resides. |
| `HOST-ID` | The unique identifier for the host of a MongoDB process. For information about retrieving host ids, see Get All Hosts in One Project. |

### Request Query Parameters

| Field | Optional/Required | Type | Description |
|---|---|---|---|
| `since` | Optional | number | Point in time, specified as milliseconds since the [Unix Epoch](https://en.wikipedia.org/wiki/Unix_time), from which you want to receive results. If you do not also specify the `duration` parameter, the endpoint returns results from `since` until the current time. |
| `duration` | Optional | number | Length of time from the `since` parameter, in milliseconds, for which you want to receive results. If you do not also specify the `since` parameter, the endpoint returns results from the number of milliseconds specified by `duration` before the current time until now. |
| `envelope` | Optional | boolean | Specifies whether or not to wrap the response in an envelope. The default is `false`. |
| `pretty` | Optional | boolean | Indicates whether the response body should be in a [prettyprint](https://en.wikipedia.org/w/index.php?title=Unix_time&oldid=856146990) format. The default value is `false`. |

### Request Body Parameters

This endpoint doesn't use HTTP request body parameters.

## Response Elements

| Name | Type | Description |
|---|---|---|
| `namespaces` | array | Each element in the array represents one namespace on the specified host that is experiencing slow queries. Namespaces appear in the following format: `{database.collection}` |
| `namespaces[i].namespace` | string | A namespace on the specified host. |
| `namespaces[i].type` | string | The type of namespace. |

## Example Request

```shell
curl --digest -i -u "{PUBLIC-KEY}:{PRIVATE-KEY}" \
   "https://cloud.mongodb.com/api/atlas/v1.0/groups/{PROJECT-ID}/hosts/cluster0-shard-00-00-mnswc.mongodb-dev.net:27017/performanceAdvisor/namespaces?pretty=true"
```

## Example Response

```javascript
{
  "namespaces" : [ {
    "namespace" : "data.zips",
    "type" : "COLLECTION"
  }, {
    "namespace" : "data.stocks",
    "type" : "COLLECTION"
  } ]
}
```
