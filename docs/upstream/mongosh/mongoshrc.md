<!-- Converted from mongoshrc.txt (reStructuredText). Includes are inlined. -->

# `.mongoshrc` Configuration File

..
   COMMENT This file might be expanded later. For now the content is
   same here and in run-commands.

On startup, `mongosh` checks your `HOME` directory for a
JavaScript file named .mongoshrc.js. If this file is found,
`mongosh` reads the content of .mongoshrc.js before
displaying the prompt for the first time.

If you use `mongosh` to evaluate a JavaScript file or
expression, either by using the `--eval` option
on the command line or by specifying a .js file, `mongosh` reads .mongoshrc.js
*after* the JavaScript has finished processing. You can prevent
.mongoshrc.js from being loaded by using the `--norc` option.

**Note:** Legacy Shell Configuration

The legacy `mongo` shell uses a configuration file named
`.mongorc.js`.

If `mongosh` finds `.mongorc.js` on startup but doesn't find
`.mongoshrc.js`, `mongosh` doesn't load the legacy `.mongorc.js`
file and states you should rename `.mongorc.js` to `.mongoshrc.js`.

## Example Usage

You can use the .mongoshrc file to customize `mongosh` startup
behavior and add scripted functionality. For examples, see
mongosh-write-scripts-config-file.
