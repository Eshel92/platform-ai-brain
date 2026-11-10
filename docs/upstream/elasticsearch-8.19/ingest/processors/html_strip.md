<!-- Converted from ingest/processors/html_strip.asciidoc (AsciiDoc). Includes are inlined. -->

### HTML strip processor

Removes HTML tags from the field. If the field is an array of strings, HTML tags will be removed from all members of the array.

**Note:** Each HTML tag is replaced with a `\n` character.

**HTML Strip Options**
|======
| Name              | Required  | Default  | Description
| `field`           | yes       | -        | The string-valued field to remove HTML tags from
| `target_field`    | no        | `field`  | The field to assign the value to, by default `field` is updated in-place
| `ignore_missing`  | no        | `false`  | If `true` and `field` does not exist, the processor quietly exits without modifying the document
| `description`     | no      | -        | Description of the processor. Useful for describing the purpose of the processor or its configuration.
| `if`             | no       | -        | Conditionally execute the processor. See conditionally-run-processor.
| `ignore_failure` | no       | `false`  | Ignore failures for the processor. See handling-pipeline-failures.
| `on_failure`     | no       | -        | Handle failures for the processor. See handling-pipeline-failures.
| `tag`            | no       | -        | Identifier for the processor. Useful for debugging and metrics.
|======

```js
{
  "html_strip": {
    "field": "foo"
  }
}
```
