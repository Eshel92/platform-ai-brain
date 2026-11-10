<!-- Converted from transform/apis/get-transform.asciidoc (AsciiDoc). Includes are inlined. -->

# Get transforms API

**New API reference**
For the most up-to-date API details, refer to [Transform APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-transform).

Retrieves configuration information for transforms.

## Request

`GET _transform/<transform_id>` +

`GET _transform/<transform_id>,<transform_id>` +

`GET _transform/` +

`GET _transform/_all` +

`GET _transform/*`

## Prerequisites

Requires the `monitor_transform` cluster privilege. This privilege is included
in the `transform_user` built-in role.

## Description

You can get information for multiple transforms in a single API
request by using a comma-separated list of identifiers or a wildcard expression.
You can get information for all transforms by using `_all`, by
specifying `*` as the `<transform_id>`, or by omitting the `<transform_id>`.

## Path parameters

`<transform_id>`::
(Optional, string)
Identifier for the transform. It can be a transform identifier or a wildcard
expression. If you do not specify one of these options, the API returns
information for all transforms.

## Query parameters

`allow_no_match`::
(Optional, Boolean)
Specifies what to do when the request:
* Contains wildcard expressions and there are no transforms that match.
* Contains the `_all` string or no identifiers and there are no matches.
* Contains wildcard expressions and there are only partial matches.

The default value is `true`, which returns an empty `transforms` array when
there are no matches and the subset of results when there are partial matches.

If this parameter is `false`, the request returns a `404` status code when there
are no matches or only partial matches.
`exclude_generated`::
(Optional, Boolean)
Excludes fields that were automatically added when creating the transform.
This allows the configuration to be in an acceptable format to be retrieved
and then added to another cluster. Default is false.

`from`::
(Optional, integer)
Skips the specified number of transforms. The default value is `0`.
`size`::
(Optional, integer)
Specifies the maximum number of transforms to obtain. The default value is
`100`.

## Response body

The API returns an array of transform resources, which are sorted by the `id`
value in ascending order. For the full list of properties, see
Create transform API.

`create_time`::
(string) The time the transform was created. For example, `1576094542936`.
This property is informational; you cannot change its value.

`version`::
(string) The transform configuration version number at which the trained model was created.

**Note:** From Elasticsearch 8.10.0,  a new version number is used to
track the configuration and state changes in the transform plugin. This new
version number is decoupled from the product version and will increment
independently. The `version` value represents the new version number.

## Response codes

`404` (Missing resources)::
  If `allow_no_match` is `false`, this code indicates that there are no
  resources that match the request or only partial matches for the request.

## Examples

The following example retrieves information about a maximum of ten transforms:

```console
GET _transform?size=10
```

The following example gets configuration information for the
`ecommerce_transform1` transform:

```console
GET _transform/ecommerce_transform1
```

The API returns the following results:

```console-result
{
  "count" : 1,
  "transforms" : [
    {
      "id" : "ecommerce_transform1",
      "authorization" : {
        "roles" : [
          "superuser"
        ]
      },
      "version" : "8.4.0",
      "create_time" : 1656023416565,
      "source" : {
        "index" : [
          "kibana_sample_data_ecommerce"
        ],
        "query" : {
          "term" : {
            "geoip.continent_name" : {
              "value" : "Asia"
            }
          }
        }
      },
      "dest" : {
        "index" : "kibana_sample_data_ecommerce_transform1",
        "pipeline" : "add_timestamp_pipeline"
      },
      "frequency" : "5m",
      "sync" : {
        "time" : {
          "field" : "order_date",
          "delay" : "60s"
        }
      },
      "pivot" : {
        "group_by" : {
          "customer_id" : {
            "terms" : {
              "field" : "customer_id"
            }
          }
        },
        "aggregations" : {
          "max_price" : {
            "max" : {
              "field" : "taxful_total_price"
            }
          }
        }
      },
      "description" : "Maximum priced ecommerce data by customer_id in Asia",
      "settings" : { },
      "retention_policy" : {
        "time" : {
          "field" : "order_date",
          "max_age" : "30d"
        }
      }
    }
  ]
}
```
