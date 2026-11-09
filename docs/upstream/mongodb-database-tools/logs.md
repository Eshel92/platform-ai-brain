<!-- Converted from logs.txt (reStructuredText). Includes are inlined. -->

# Database Tools Logs

The MongoDB Database Tools print logs to stderr.

## Stderr Examples

The following examples show the results of `mongoexport`
operations and the information logged to stderr.

### Successful `mongoexport` Operation

Consider the following `mongoexport` operation that
produces a file called `cakeSales.json` from the contents
of the `test.cakeSales` collection:

```sh
mongoexport --db=test --collection=cakeSales --out=cakeSales.json
```

`mongoexport` logs the following information to stderr:

```none
2021-09-21T14:05:07.197-0400	connected to: mongodb://localhost/
2021-09-21T14:05:07.203-0400	exported 6 records
```

### Failed `mongoexport` Operation

Consider the following `mongoexport` operation that fails
because it cannot connect to the target deployment:

```sh
mongoexport --host=notRealHost.example.net --port=27017 --username=someUser --authenticationDatabase=admin --collection=contacts --db=marketing --out=mdb1-examplenet.json
```

   
`mongoexport` logs the following information to stderr:

```none
2021-09-21T14:35:30.125-0400	could not connect to server: server selection error: server selection timeout, current topology: { Type: Single, Servers: [{ Addr: notrealhost.example.net:27017, Type: Unknown, Last error: connection() error occurred during connection handshake: dial tcp: lookup notrealhost.example.net: no such host }, ] }
```

   

## Pipe Database Tools Logs to a File

You may want to output the contents of the stderr logs to a file
for easier viewing, or to save the results of Database Tools
operations.

To pipe the stderr output to a file, append `2> {fileName}`
to your command.

### Example

The following command writes the output of a `mongoexport`
operation to a file called `mongoexport.log`. In this example, the
`mongoexport.log` file is created in the same directory where the
command is run.

```sh
mongoexport --db=test --collection=cakeSales --out=cakeSales.json 2> mongoexport.log
```

   
To view the contents of `mongoexport.log`, open the file in a text
editor.
