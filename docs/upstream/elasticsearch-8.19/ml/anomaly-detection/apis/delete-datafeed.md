<!-- Converted from ml/anomaly-detection/apis/delete-datafeed.asciidoc (AsciiDoc). Includes are inlined. -->

# Delete datafeeds API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Deletes an existing datafeed.

## Request

`DELETE _ml/datafeeds/<feed_id>`

## Prerequisites

* Requires the `manage_ml` cluster privilege. This privilege is included in the 
`machine_learning_admin` built-in role.
* Unless you use the `force` parameter, you must stop the datafeed before you
can delete it.

## Path parameters

`<feed_id>`::
(Required, string)
A numerical character string that uniquely identifies the
datafeed. This identifier can contain lowercase alphanumeric characters (a-z
and 0-9), hyphens, and underscores. It must start and end with alphanumeric
characters.

## Query parameters

`force`::
(Optional, Boolean) Use to forcefully delete a started datafeed; this method is
quicker than stopping and deleting the datafeed.

## Examples

```console
DELETE _ml/datafeeds/datafeed-total-requests
```

When the datafeed is deleted, you receive the following results:

```console-result
{
  "acknowledged": true
}
```
