<!-- Converted from ingest/processors/registered-domain.asciidoc (AsciiDoc). Includes are inlined. -->

### Registered domain processor

Extracts the registered domain (also known as the effective top-level domain or
eTLD), sub-domain, and top-level domain from a fully qualified domain name
(FQDN). Uses the registered domains defined in the
[Mozilla Public Suffix List](https://publicsuffix.org/).

**Registered Domain Options**
|======
| Name               | Required | Default | Description
| `field`            | yes      |         | Field containing the source FQDN.
| `target_field`     | no       | `<empty string>` | Object field containing
extracted domain components. If an `<empty string>`, the processor adds
components to the document's root.
| `ignore_missing`   | no       | `true`  | If `true` and any required fields
are missing, the processor quietly exits without modifying the document.

| `description`     | no      | -        | Description of the processor. Useful for describing the purpose of the processor or its configuration.
| `if`             | no       | -        | Conditionally execute the processor. See conditionally-run-processor.
| `ignore_failure` | no       | `false`  | Ignore failures for the processor. See handling-pipeline-failures.
| `on_failure`     | no       | -        | Handle failures for the processor. See handling-pipeline-failures.
| `tag`            | no       | -        | Identifier for the processor. Useful for debugging and metrics.
|======

##### Examples

The following example illustrates the use of the registered domain processor:

```console
POST _ingest/pipeline/_simulate
{
  "pipeline": {
    "processors": [
      {
        "registered_domain": {
          "field": "fqdn",
          "target_field": "url"
        }
      }
    ]
  },
  "docs": [
    {
      "_source": {
        "fqdn": "www.example.ac.uk"
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
          "fqdn": "www.example.ac.uk",
          "url": {
            "subdomain": "www",
            "registered_domain": "example.ac.uk",
            "top_level_domain": "ac.uk",
            "domain": "www.example.ac.uk"
          }
        }
      }
    }
  ]
}
```
