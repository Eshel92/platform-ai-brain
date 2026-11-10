<!-- Converted from troubleshooting/data/source-mode-setting.asciidoc (AsciiDoc). Includes are inlined. -->

## Configuring source mode in mappings is deprecated and replaced by an index setting

Index source mode was previously configured in mappings as follows:

```js
"mappings": {
    "source": {
        "mode": "synthetic"
    },
    "foo": {
        "type": "keyword"
    },
    "bar": {
        "type": "keyword"
    }
}
```

Starting with version 8.18, this method for configuring the source mode is considered
deprecated and replaced by index setting `index.mapping.source.mode` that accepts the
same values: `stored`, `synthetic` and `disabled`. The index setting can be
used as follows:

```js
"settings": {
    "index.mapping.source.mode": "synthetic"
}
"mappings": {
    "foo": {
        "type": "keyword"
    },
    "bar": {
        "type": "keyword"
    }
}
```

Existing indexes using the deprecated method for configuring the source mode are not
affected, but creating new indexes raises warnings and will not be supported in a future
release. This can be an issue for data streams and other indexes that get regularly
generated using component templates. To avoid these problems, identify all affected
component templates, as shown in the deprecation info API,
and update them to use setting `index.mapping.source.mode` instead of
`mappings.source.mode`, according to the examples above.
