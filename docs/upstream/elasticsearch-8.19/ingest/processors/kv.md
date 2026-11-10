<!-- Converted from ingest/processors/kv.asciidoc (AsciiDoc). Includes are inlined. -->

### KV processor

This processor helps automatically parse messages (or specific event fields) which are of the `foo=bar` variety.

For example, if you have a log message which contains `ip=1.2.3.4 error=REFUSED`, you can parse those fields automatically by configuring:

```js
{
  "kv": {
    "field": "message",
    "field_split": " ",
    "value_split": "="
  }
}
```

**Tip:** Using the KV Processor can result in field names that you cannot control. Consider using the flattened data type instead, which maps an entire object as a single field and allows for simple searches over its contents.

**KV Options**
|======
| Name             | Required  | Default  | Description
| `field`          | yes       | -        | The field to be parsed. Supports template snippets.
| `field_split`    | yes       | -        | Regex pattern to use for splitting key-value pairs
| `value_split`    | yes       | -        | Regex pattern to use for splitting the key from the value within a key-value pair
| `target_field`   | no        | `null`   | The field to insert the extracted keys into. Defaults to the root of the document. Supports template snippets.
| `include_keys`   | no        | `null`   | List of keys to filter and insert into document. Defaults to including all keys
| `exclude_keys`   | no        | `null`   | List of keys to exclude from document
| `ignore_missing` | no        | `false`  | If `true` and `field` does not exist or is `null`, the processor quietly exits without modifying the document
| `prefix`         | no        | `null`   | Prefix to be added to extracted keys
| `trim_key`       | no        | `null`   | String of characters to trim from extracted keys
| `trim_value`     | no        | `null`   | String of characters to trim from extracted values
| `strip_brackets` | no        | `false`  | If `true` strip brackets `()`, `<>`, `[]` as well as quotes `'` and `"` from extracted values
| `description`     | no      | -        | Description of the processor. Useful for describing the purpose of the processor or its configuration.
| `if`             | no       | -        | Conditionally execute the processor. See conditionally-run-processor.
| `ignore_failure` | no       | `false`  | Ignore failures for the processor. See handling-pipeline-failures.
| `on_failure`     | no       | -        | Handle failures for the processor. See handling-pipeline-failures.
| `tag`            | no       | -        | Identifier for the processor. Useful for debugging and metrics.
|======
