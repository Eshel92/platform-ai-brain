<!-- Converted from ingest/processors/rename.asciidoc (AsciiDoc). Includes are inlined. -->

### Rename processor

Renames an existing field. If the field doesn't exist or the new name is already used, an exception will be thrown.

**Rename Options**
|======
| Name              | Required  | Default  | Description
| `field`           | yes       | -        | The field to be renamed. Supports template snippets.
| `target_field`    | yes       | -        | The new name of the field. Supports template snippets.
| `ignore_missing`  | no        | `false`  | If `true` and `field` does not exist, the processor quietly exits without modifying the document.
| `override`        | no        | `false`  | If `true`, the processor will update pre-existing non-null-valued fields. When set to `false`, such fields will not be touched.
| `description`     | no      | -        | Description of the processor. Useful for describing the purpose of the processor or its configuration.
| `if`             | no       | -        | Conditionally execute the processor. See conditionally-run-processor.
| `ignore_failure` | no       | `false`  | Ignore failures for the processor. See handling-pipeline-failures.
| `on_failure`     | no       | -        | Handle failures for the processor. See handling-pipeline-failures.
| `tag`            | no       | -        | Identifier for the processor. Useful for debugging and metrics.
|======

```js
{
  "rename": {
    "field": "provider",
    "target_field": "cloud.provider"
  }
}
```
