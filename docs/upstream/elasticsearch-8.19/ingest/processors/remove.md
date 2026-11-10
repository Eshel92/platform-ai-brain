<!-- Converted from ingest/processors/remove.asciidoc (AsciiDoc). Includes are inlined. -->

### Remove processor

Removes existing fields. If one field doesn't exist, an exception will be thrown.

**Remove Options**
|======
| Name             | Required  | Default  | Description
| `field`          | yes       | -        | Fields to be removed. Supports template snippets.
| `ignore_missing` | no        | `false`  | If `true` and `field` does not exist or is `null`, the processor quietly exits without modifying the document
| `keep`           | no        | -        | Fields to be kept. When set, all fields other than those specified are removed.
| `description`     | no      | -        | Description of the processor. Useful for describing the purpose of the processor or its configuration.
| `if`             | no       | -        | Conditionally execute the processor. See conditionally-run-processor.
| `ignore_failure` | no       | `false`  | Ignore failures for the processor. See handling-pipeline-failures.
| `on_failure`     | no       | -        | Handle failures for the processor. See handling-pipeline-failures.
| `tag`            | no       | -        | Identifier for the processor. Useful for debugging and metrics.
|======

Here is an example to remove a single field:

```js
{
  "remove": {
    "field": "user_agent"
  }
}
```

To remove multiple fields, you can use the following query:

```js
{
  "remove": {
    "field": ["user_agent", "url"]
  }
}
```

You can also choose to remove all fields other than a specified list:

```js
{
  "remove": {
    "keep": ["url"]
  }
}
```
