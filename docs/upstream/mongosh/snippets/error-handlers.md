<!-- Converted from snippets/error-handlers.txt (reStructuredText). Includes are inlined. -->

# Error Handlers

**Warning:**

This feature is experimental. MongoDB does not provide support for
Snippets. This feature may be changed or removed at any time without
prior notice.

Bugs are not expected, however should you encounter one, please open an
issue in the
[GitHub repository](https://github.com/mongodb-labs/mongosh-snippets/issues)
for this project.

Error handlers allow you to specify regular expressions to catch
runtime errors and display custom error messages.

To use an error matcher, add a line to your package.json file like the highlighted line in this
excerpt from a snippet in the community [GitHub repository](https://github.com/mongodb-labs/mongosh-snippets/blob/main/snippets/mongocompat/package.json). 

```shell
...
"description": "mongo compatibility script for mongosh",
"main": "index.js",
"errorMatchers": "error-matchers.js",
"license": "SSPL",
...
```

For an example of error matching code, see the [mongocompat](https://github.com/mongodb-labs/mongosh-snippets/blob/main/snippets/mongocompat/error-matchers.js)
snippet.
