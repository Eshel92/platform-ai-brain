<!-- Converted from ingest/processors/append.asciidoc (AsciiDoc). Includes are inlined. -->

### Append processor

Appends one or more values to an existing array if the field already exists and it is an array.
Converts a scalar to an array and appends one or more values to it if the field exists and it is a scalar.
Creates an array containing the provided values if the field doesn't exist.
Accepts a single value or an array of values.

**Append Options**
|======
| Name      | Required  | Default  | Description
| `field`   | yes       | -        | The field to be appended to. Supports template snippets.
| `value`   | yes       | -        | The value to be appended. Supports template snippets.
| `allow_duplicates` | no | true  | If `false`, the processor does not append
values already present in the field.
| `media_type` | no | `application/json` | The media type for encoding `value`. Applies only when `value` is a
template snippet. Must be one of `application/json`, `text/plain`, or
`application/x-www-form-urlencoded`.
| `description`     | no      | -        | Description of the processor. Useful for describing the purpose of the processor or its configuration.
| `if`             | no       | -        | Conditionally execute the processor. See conditionally-run-processor.
| `ignore_failure` | no       | `false`  | Ignore failures for the processor. See handling-pipeline-failures.
| `on_failure`     | no       | -        | Handle failures for the processor. See handling-pipeline-failures.
| `tag`            | no       | -        | Identifier for the processor. Useful for debugging and metrics.
|======

```js
{
  "append": {
    "field": "tags",
    "value": ["production", "{{{app}}}", "{{{owner}}}"]
  }
}
```
