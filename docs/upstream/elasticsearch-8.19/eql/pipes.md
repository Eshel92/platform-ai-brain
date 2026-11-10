<!-- Converted from eql/pipes.asciidoc (AsciiDoc). Includes are inlined. -->

## EQL pipe reference

Elasticsearch supports the following EQL pipes.

### `head`

Returns up to a specified number of events or sequences, starting with the
earliest matches. Works similarly to the
[Unix head command](https://en.wikipedia.org/wiki/Head_(Unix)).

*Example*

The following EQL query returns up to three of the earliest powershell
commands.

```eql
process where process.name == "powershell.exe"
| head 3
```

*Syntax*
```txt
head <max>
```

*Parameters*

`<max>`::
(Required, integer)
Maximum number of matching events or sequences to return.

### `tail`

Returns up to a specified number of events or sequences, starting with the most
recent matches. Works similarly to the
[Unix tail command](https://en.wikipedia.org/wiki/Tail_(Unix)).

*Example*

The following EQL query returns up to five of the most recent `svchost.exe`
processes.

```eql
process where process.name == "svchost.exe"
| tail 5
```

*Syntax*
```txt
tail <max>
```

*Parameters*

`<max>`::
(Required, integer)
Maximum number of matching events or sequences to return.
