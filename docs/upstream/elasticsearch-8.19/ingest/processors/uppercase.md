<!-- Converted from ingest/processors/uppercase.asciidoc (AsciiDoc). Includes are inlined. -->

### Uppercase processor

Converts a string to its uppercase equivalent. If the field is an array of strings, all members of the array will be converted.

**Uppercase Options**
|======
| Name             | Required  | Default  | Description
| `field`          | yes       | -        | The field to make uppercase
| `target_field`   | no        | `field`  | The field to assign the converted value to, by default `field` is updated in-place
| `ignore_missing` | no        | `false`  | If `true` and `field` does not exist or is `null`, the processor quietly exits without modifying the document
| `description`     | no      | -        | Description of the processor. Useful for describing the purpose of the processor or its configuration.
| `if`             | no       | -        | Conditionally execute the processor. See conditionally-run-processor.
| `ignore_failure` | no       | `false`  | Ignore failures for the processor. See handling-pipeline-failures.
| `on_failure`     | no       | -        | Handle failures for the processor. See handling-pipeline-failures.
| `tag`            | no       | -        | Identifier for the processor. Useful for debugging and metrics.
|======

```js
{
  "uppercase": {
    "field": "foo"
  }
}
```
