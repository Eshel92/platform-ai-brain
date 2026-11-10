<!-- Converted from ingest/processors/fingerprint.asciidoc (AsciiDoc). Includes are inlined. -->

### Fingerprint processor

Computes a hash of the document's content. You can use this hash for
[content fingerprinting](https://en.wikipedia.org/wiki/Fingerprint_(computing)).

**Fingerprint Options**
|======
| Name               | Required | Default       | Description
| `fields`           | yes      | n/a           | Array of fields to include in
the fingerprint. For objects, the processor hashes both the field key and
value. For other fields, the processor hashes only the field value.
| `target_field`     | no       | `fingerprint` | Output field for the fingerprint.
| `salt`             | no       | <none>        |
[Salt value](https://en.wikipedia.org/wiki/Salt_(cryptography)) for the hash function.
| `method`           | no       | `SHA-1`       | The hash method used to
compute the fingerprint. Must be one of `MD5`, `SHA-1`, `SHA-256`, `SHA-512`, or
`MurmurHash3`.
| `ignore_missing`   | no       | `false`       | If `true`, the processor
ignores any missing `fields`. If all fields are missing, the processor silently
exits without modifying the document.

| `description`     | no      | -        | Description of the processor. Useful for describing the purpose of the processor or its configuration.
| `if`             | no       | -        | Conditionally execute the processor. See conditionally-run-processor.
| `ignore_failure` | no       | `false`  | Ignore failures for the processor. See handling-pipeline-failures.
| `on_failure`     | no       | -        | Handle failures for the processor. See handling-pipeline-failures.
| `tag`            | no       | -        | Identifier for the processor. Useful for debugging and metrics.
|======

##### Example

The following example illustrates the use of the fingerprint processor:

```console
POST _ingest/pipeline/_simulate
{
  "pipeline": {
    "processors": [
      {
        "fingerprint": {
          "fields": ["user"]
        }
      }
    ]
  },
  "docs": [
    {
      "_source": {
        "user": {
          "last_name": "Smith",
          "first_name": "John",
          "date_of_birth": "1980-01-15",
          "is_active": true
        }
      }
    }
  ]
}
```

Which produces the following result:

```console-result
{
  "docs": [
    {
      "doc": {
        ...
        "_source": {
          "fingerprint" : "WbSUPW4zY1PBPehh2AA/sSxiRjw=",
          "user" : {
            "last_name" : "Smith",
            "first_name" : "John",
            "date_of_birth" : "1980-01-15",
            "is_active" : true
          }
        }
      }
    }
  ]
}
```
