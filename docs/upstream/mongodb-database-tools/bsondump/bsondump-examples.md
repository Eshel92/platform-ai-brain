<!-- Converted from bsondump/bsondump-examples.txt (reStructuredText). Includes are inlined. -->

# bsondump Examples

**`bsondump`**

This page shows examples for `bsondump`.

Run `bsondump` from the system command line, not the `mongo` shell.

By default, `bsondump` outputs data to standard output. To
create corresponding JSON files, you can use the 
`--outFile` option:

```sh
bsondump --outFile=collection.json collection.bson
```

Use the following command (at the system shell) to produce debugging
output for a BSON file:

```sh
bsondump --type=debug collection.bson
```

## Learn More

- bsondump
- bsondump-compatibility-and-installation
