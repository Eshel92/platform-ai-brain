<!-- Converted from ingest/apis/enrich/get-enrich-policy.asciidoc (AsciiDoc). Includes are inlined. -->

### Get enrich policy API

**New API reference**
For the most up-to-date API details, refer to [Enrich APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-enrich).

Returns information about an enrich policy.

```console
GET /_enrich/policy/my-policy
```

#### Request

`GET /_enrich/policy/<name>`

`GET /_enrich/policy`

`GET /_enrich/policy/policy1,policy2`

#### Prerequisites

To use enrich policies, you must have:

* `read` index privileges for any indices used
* The `enrich_user` built-in role

#### Path parameters

`<name>`::
(Optional, string)
Comma-separated list of enrich policy names
used to limit the request.

To return information for all enrich policies,
omit this parameter.

#### Examples

##### Get a single policy

```console
GET /_enrich/policy/my-policy
```

The API returns the following response:

```console-result
{
  "policies": [
    {
      "config": {
        "match": {
          "name": "my-policy",
          "indices": [ "users" ],
          "match_field": "email",
          "enrich_fields": [
            "first_name",
            "last_name",
            "city",
            "zip",
            "state"
          ]
        }
      }
    }
  ]
}
```

##### Get multiple policies

```console
GET /_enrich/policy/my-policy,other-policy
```

The API returns the following response:

```console-result
{
  "policies": [
    {
      "config": {
        "match": {
          "name": "my-policy",
          "indices": [ "users" ],
          "match_field": "email",
          "enrich_fields": [
            "first_name",
            "last_name",
            "city",
            "zip",
            "state"
          ]
        }
      }
    },
    {
      "config": {
        "match": {
          "name": "other-policy",
          "indices": [ "users" ],
          "match_field": "email",
          "enrich_fields": [
            "first_name",
            "last_name",
            "city",
            "zip",
            "state"
          ]
        }
      }
    }
  ]
}
```

##### Get all policies

```console
GET /_enrich/policy
```

The API returns the following response:

```console-result
{
  "policies": [
    {
      "config": {
        "match": {
          "name": "my-policy",
          "indices": [ "users" ],
          "match_field": "email",
          "enrich_fields": [
            "first_name",
            "last_name",
            "city",
            "zip",
            "state"
          ]
        }
      }
    },
    {
      "config": {
        "match": {
          "name": "other-policy",
          "indices": [ "users" ],
          "match_field": "email",
          "enrich_fields": [
            "first_name",
            "last_name",
            "city",
            "zip",
            "state"
          ]
        }
      }
    }
  ]
}
```
