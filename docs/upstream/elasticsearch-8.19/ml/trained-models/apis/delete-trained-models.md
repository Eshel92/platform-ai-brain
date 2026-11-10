<!-- Converted from ml/trained-models/apis/delete-trained-models.asciidoc (AsciiDoc). Includes are inlined. -->

# Delete trained models API

**New API reference**
For the most up-to-date API details, refer to [Machine learning trained model APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-trained-model).

Deletes an existing trained inference model.

## Request

`DELETE _ml/trained_models/<model_id>`

## Prerequisites

Requires the `manage_ml` cluster privilege. This privilege is included in the 
`machine_learning_admin` built-in role.

## Path parameters

`<model_id>`::
(Optional, string)
The unique identifier of the trained model.

## Query parameters

`force`::
  (Optional, Boolean) Use to forcefully delete a trained model that is referenced
  by ingest pipelines or has a started deployment.

## Response codes

`409`::
  The code indicates that the trained model is referenced by an ingest pipeline
  and cannot be deleted.

## Examples

The following example deletes the `regression-job-one-1574775307356` trained
model:

```console
DELETE _ml/trained_models/regression-job-one-1574775307356
```

The API returns the following result:

```console-result
{
  "acknowledged" : true
}
```
