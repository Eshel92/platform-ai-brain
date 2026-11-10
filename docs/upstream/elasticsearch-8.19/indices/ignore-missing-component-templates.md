<!-- Converted from indices/ignore-missing-component-templates.asciidoc (AsciiDoc). Includes are inlined. -->

## Config ignore_missing_component_templates

The configuration option `ignore_missing_component_templates` can be used when an index template references a component template that might not exist. Every time a data stream is created based on the index template, the existence of the component template will be checked. If it exists, it will used to form the index's composite settings. If it does not exist, it is ignored.

### Usage example

In the following, one component template and an index template are created. The index template references two component templates, but only the `@package` one exists.

Create the component template `logs-foo_component1`. This has to be created before the index template as it is not optional:

```console
PUT _component_template/logs-foo_component1
{
  "template": {
    "mappings": {
      "properties": {
        "host.name": {
          "type": "keyword"
        }
      }
    }
  }
}
```

Next, the index template will be created and it references two component templates:

```JSON
  "composed_of": ["logs-foo_component1", "logs-foo_component2"]
```

Before, only the `logs-foo_component1` compontent template was created, meaning the `logs-foo_component2` is missing. Because of this the following entry was added to the config:

```JSON
  "ignore_missing_component_templates": ["logs-foo_component2"],
```

During creation of the template, it will not validate that `logs-foo_component2` exists:

```console
PUT _index_template/logs-foo
{
  "index_patterns": ["logs-foo-*"],
  "data_stream": { },
  "composed_of": ["logs-foo_component1", "logs-foo_component2"],
  "ignore_missing_component_templates": ["logs-foo_component2"],
  "priority": 500
}
```

The index template `logs-foo` was successfully created. A data stream can be created based on this template:

```console
PUT _data_stream/logs-foo-bar
```

Looking at the mappings of the data stream, it will contain the `host.name` field.

At a later stage, the missing component template might be added:

```console
PUT _component_template/logs-foo_component2
{
  "template": {
    "mappings": {
      "properties": {
        "host.ip": {
          "type": "ip"
        }
      }
    }
  }
}
```

This will not have an immediate effect on the data stream. The mapping `host.ip` will only show up in the data stream mappings when the data stream is rolled over automatically next time or a manual rollover is triggered:

```console
POST logs-foo-bar/_rollover
```
