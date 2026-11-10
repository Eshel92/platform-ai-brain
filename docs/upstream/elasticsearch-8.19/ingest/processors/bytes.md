<!-- Converted from ingest/processors/bytes.asciidoc (AsciiDoc). Includes are inlined. -->

### Bytes processor

Converts a human readable byte value (e.g. 1kb) to its value in bytes (e.g. 1024). If the field is an array of strings, all members of the array will be converted.

Supported human readable units are "b", "kb", "mb", "gb", "tb", "pb" case insensitive. An error will occur if
the field is not a supported format or resultant value exceeds 2^63.

**Bytes Options**
|======
| Name             | Required  | Default  | Description
| `field`          | yes       | -        | The field to convert
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
  "bytes": {
    "field": "file.size"
  }
}
```
