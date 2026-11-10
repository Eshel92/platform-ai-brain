<!-- Converted from ml/anomaly-detection/apis/validate-detector.asciidoc (AsciiDoc). Includes are inlined. -->

# Validate detectors API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Validates detector configuration information.

## Request

`POST _ml/anomaly_detectors/_validate/detector`

## Prerequisites

Requires the `manage_ml` cluster privilege. This privilege is included in the 
`machine_learning_admin` built-in role.

## Description

This API enables you to validate the detector configuration
before you create an anomaly detection job.

## Request body

`by_field_name`::
(string)
The field used to split the data. In particular, this property is used for
analyzing the splits with respect to their own history. It is used for finding
unusual values in the context of the split.
`custom_rules`::
(array)
An array of custom rule objects, which enable you to customize the way detectors
operate. For example, a rule may dictate to the detector conditions under which
results should be skipped. Kibana refers to custom rules as _job rules_. For more
examples, see
{ml-docs}/ml-configuring-detector-custom-rules.html[Customizing detectors with custom rules].
`analysis_config`.`detectors`.`custom_rules`.`actions`:::
(array)
The set of actions to be triggered when the rule applies. If
more than one action is specified the effects of all actions are combined. The
available actions include:

* `skip_result`: The result will not be created. This is the default value.
Unless you also specify `skip_model_update`, the model will be updated as usual
with the corresponding series value.
* `skip_model_update`: The value for that series will not be used to update the
model. Unless you also specify `skip_result`, the results will be created as
usual. This action is suitable when certain values are expected to be
consistently anomalous and they affect the model in a way that negatively
impacts the rest of the results.
* `force_time_shift`: This action will shift the time inside the anomaly detector by a specified
amount. This is useful, e.g. to quickly adapt to the daylight saving time events that
are known beforehand. This action requires a `force_time_shift` parameter
in the `params` object.
`analysis_config`.`detectors`.`custom_rules`.`scope`:::
(object)
An optional scope of series where the rule applies. A rule must either
have a non-empty scope or at least one condition. By default, the scope includes
all series. Scoping is allowed for any of the fields that are also specified in
`by_field_name`, `over_field_name`, or `partition_field_name`. To add a scope
for a field, add the field name as a key in the scope object and set its value
to an object with the following properties:
`analysis_config`.`detectors`.`custom_rules`.`scope`.`filter_id`::::
(string)
The id of the filter to be used.
`analysis_config`.`detectors`.`custom_rules`.`scope`.`filter_type`::::
(string)
Either `include` (the rule applies for values in the filter) or `exclude` (the
rule applies for values not in the filter). Defaults to `include`.
`analysis_config`.`detectors`.`custom_rules`.`conditions`:::
(array)
An optional array of numeric conditions when the rule applies. A rule must
either have a non-empty scope or at least one condition. Multiple conditions are
combined together with a logical `AND`. A condition has the following
properties:
`analysis_config`.`detectors`.`custom_rules`.`conditions`.`applies_to`::::
(string)
Specifies the result property to which the condition applies. The available
options are `actual`, `typical`, `diff_from_typical`, `time`. If your detector
uses `lat_long`, `metric`, `rare`, or `freq_rare` functions, you can only
specify conditions that apply to `time`.
`analysis_config`.`detectors`.`custom_rules`.`conditions`.`operator`::::
(string)
Specifies the condition operator. The available options are `gt` (greater than),
`gte` (greater than or equals), `lt` (less than) and `lte` (less than or
equals).
`analysis_config`.`detectors`.`custom_rules`.`conditions`.`value`::::
(double)
The value that is compared against the `applies_to` field using the `operator`.

`detector_description`::
(string)
A description of the detector. For example, `Low event rate`.
`detector_index`::
(integer)
A unique identifier for the detector. This identifier is based on the order of
the detectors in the `analysis_config`, starting at zero.
`exclude_frequent`::
(string)
Contains one of the following values: `all`, `none`, `by`, or `over`. If set,
frequent entities are excluded from influencing the anomaly results. Entities
can be considered frequent over time or frequent in a population. If you are
working with both over and by fields, then you can set `exclude_frequent` to
`all` for both fields, or to `by` or `over` for those specific fields.
`field_name`::
(string)
The field that the detector uses in the function. If you use an event rate
function such as `count` or `rare`, do not specify this field.
**Note:** The `field_name` cannot contain double quotes or backslashes.

`function`::
(string)
The analysis function that is used. For example, `count`, `rare`, `mean`, `min`,
`max`, and `sum`. For more information, see
{ml-docs}/ml-functions.html[Function reference].
`over_field_name`::
(string)
The field used to split the data. In particular, this property is used for
analyzing the splits with respect to the history of all splits. It is used for
finding unusual values in the population of all splits. For more information,
see {ml-docs}/ml-configuring-populations.html[Performing population analysis].
`partition_field_name`::
(string)
The field used to segment the analysis. When you use this property, you have
completely independent baselines for each value of this field.
`use_null`::
(Boolean)
Defines whether a new series is used as the null series when there is no value
for the by or partition fields. The default value is `false`.

## Examples

```console
POST _ml/anomaly_detectors/_validate/detector
{
  "function": "metric",
  "field_name": "responsetime",
  "by_field_name": "airline"
}
```

When the validation completes, you receive the following results:

```console-result
{
  "acknowledged": true
}
```
