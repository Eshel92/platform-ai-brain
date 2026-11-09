<!-- Converted from reference/method/js-native.txt (reStructuredText). Includes are inlined. -->

# Native Methods in `mongosh`

The methods listed in this section are `mongosh` functional
replacements for the native methods that were available in the legacy 
`mongo` shell. These methods are not exact replacements: output 
formats and some functionality may differ from the corresponding 
legacy methods.

In addition to these methods, the [mongocompat snippet](https://github.com/mongodb-labs/mongosh-snippets/blob/main/snippets/mongocompat/index.js)
provides access to legacy `mongo` shell APIs.

**Note:**

In the following table `<path>` and `<filename>` are strings and
should be in quotes.

```javascript
// process.chdir( <path> )

process.chdir( "./data/incoming" )
```

* - Legacy Method Name
  - Replacement

* - `cat()`
  - Returns the contents of the specified file

    ```javascript
    fs.readFileSync( <filename>, 'utf8' )
    ```

    The legacy `useBinaryMode` option is not supported. Emulate 
    the `useBinaryMode = false` option with:

    ```javascript
    fs.readFileSync( <filename>, 'utf8' ).replace( /\r\n/g, '\n' )
    ```

* - `getHostName()`
  - Returns the hostname of the system running `mongosh`.

    ```javascript
    os.hostname()
    ```

* - `getMemInfo()`
  - Returns a document that reports memory used by the shell.

    ```javascript
    process.memoryUsage()
    ```

* - `hostname()`
  - Returns the hostname of the computer running the shell.

    ```javascript
    os.hostname()
    ```

* - `isInteractive()`
  - Returns a boolean indicating whether `mongosh` is
    running in interactive or script mode.

    ```
    isInteractive()
    ```

* - `listFiles()`
  - Returns an array of documents that give the name and type of
    each object in the directory.

    ```javascript
    fs.readdirSync( <path>, { withFileTypes: true } )
    ```

* - `load()`
  - Loads and runs a JavaScript file in the shell.

    `load()` is available in `mongosh`. See also
    load-and-require.

* - `ls()`
  - Returns a list of the files in the current directory.

    ```javascript
    fs.readdirSync( <path> )
    ```

* - `md5sumFile()`
  - Returns the md5 hash of the specified file.

    ```javascript
    crypto.createHash( 'md5' ).update( fs.readFileSync( <filename> ) ).digest( 'hex' )
    ```

* - `mkdir()`
  - Creates a directory at the specified path.

    ```javascript
    fs.mkdirSync( <path>, { recursive: true } )
    ```

* - `quit()`
  - Exits the current shell session.

    ```javascript
    quit()
    ```

* - `removeFile()`
  - Removes the specified file from the local file system.

    ```javascript
    fs.unlinkSync( <filename> )
    ```

* - `sleep()`
  - Sleep for the specified number of milliseconds.

    ```javascript
    sleep( <number> )
    ```

* - `version()`
  - Returns the current version of `mongosh` instance.

    ```javascript
    version()
    ```

* - `_isWindows()`
  - Returns `true` if the shell in running on Windows.

    ```javascript
    process.platform === 'win32'
    ```

* - `_rand()`
  - Returns a random number between `0` and `1`.                    

    ```javascript
    Math.random() 
    ```
