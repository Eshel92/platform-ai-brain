<!-- Part 4 of 4 of ml/trained-models/apis/get-trained-models.md (split because the page is big). -->

## Response codes

`400`::
  If `include_model_definition` is `true`, this code indicates that more than
  one models match the ID pattern.

`404` (Missing resources)::
  If `allow_no_match` is `false`, this code indicates that there are no
  resources that match the request or only partial matches for the request.


## Examples

The following example gets configuration information for all the trained models:

```console
GET _ml/trained_models/
```
