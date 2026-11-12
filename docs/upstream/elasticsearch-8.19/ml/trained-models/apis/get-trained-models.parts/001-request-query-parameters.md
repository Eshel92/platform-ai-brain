<!-- Part 1 of 4 of ml/trained-models/apis/get-trained-models.md (split because the page is big). -->

## Request

`GET _ml/trained_models/` +

`GET _ml/trained_models/<model_id>` +

`GET _ml/trained_models/_all` +

`GET _ml/trained_models/<model_id1>,<model_id2>` +

`GET _ml/trained_models/<model_id_pattern*>`


## Prerequisites

Requires the `monitor_ml` cluster privilege. This privilege is included in the
`machine_learning_user` built-in role.


## Path parameters

`<model_id>`::
(Optional, string)
The unique identifier of the trained model or a model alias.
You can get information for multiple trained models in a single API request by
using a comma-separated list of model IDs or a wildcard expression.


## Query parameters

`allow_no_match`::
(Optional, Boolean)
Specifies what to do when the request:
* Contains wildcard expressions and there are no models that match.
* Contains the `_all` string or no identifiers and there are no matches.
* Contains wildcard expressions and there are only partial matches.

The default value is `true`, which returns an empty array when there are no
matches and the subset of results when there are partial matches. If this
parameter is `false`, the request returns a `404` status code when there are no
matches or only partial matches.
`decompress_definition`::
(Optional, Boolean)
Specifies whether the included model definition should be returned as a JSON map
(`true`) or in a custom compressed format (`false`). Defaults to `true`.

`exclude_generated`::
(Optional, Boolean)
Indicates if certain fields should be removed from the configuration on
retrieval. This allows the configuration to be in an acceptable format to be retrieved
and then added to another cluster. Default is false.
`from`::
(Optional, integer)
Skips the specified number of models. The default value is `0`.
`include`::
(Optional, string)
A comma delimited string of optional fields to include in the response body. The
default value is empty, indicating no optional fields are included. Valid
options are:
 - `definition`: Includes the model definition.
 - `feature_importance_baseline`: Includes the baseline for {feat-imp} values.
 - `hyperparameters`: Includes the information about hyperparameters used to
    train the model. This information consists of the value, the absolute and
    relative importance of the hyperparameter as well as an indicator of whether
    it was specified by the user or tuned during hyperparameter optimization.
 - `total_feature_importance`: Includes the total {feat-imp} for the training
   data set.
 - `definition_status`: Includes the field `fully_defined` indicating if the
full model definition is present.
The baseline and total {feat-imp} values are returned in the `metadata` field
in the response body.

`size`::
(Optional, integer)
Specifies the maximum number of models to obtain. The default value
is `100`.
`tags`::
(Optional, string)
A comma delimited string of tags. A trained model can have many tags, or none.
When supplied, only trained models that contain all the supplied tags are
returned.
