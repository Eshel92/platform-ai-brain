<!-- Converted from snippets/registry-index.txt (reStructuredText). Includes are inlined. -->

# Create a Registry Index File Manually

**Warning:** Experimental feature

This feature is experimental. MongoDB does not provide support for
Snippets. This feature may be changed or removed at any time without
prior notice.

Bugs are not expected, however should you encounter one, please open an
issue in the
[GitHub repository](https://github.com/mongodb-labs/mongosh-snippets/issues)
for this project.

This page discusses how to manually create a registry index file. To
generate the registry index file using a script, see Create a
Registry Index File. 

To create the registry index file:

#. Copy the following TypeScript template and save it as `make-index.ts`:

   ```typescript
   import bson from 'bson';
   import zlib from 'zlib';

   interface ErrorMatcher {
      // Add additional information to shell errors matching one of the regular.
      // expressions. The message can point to a snippet helping solve that error.
      matches: RegExp[];
      message: string;
   }

   interface SnippetDescription {
      // The *npm* package name. Users do not interact with this.
      name: string;

      // The snippet name. This is what users interact with.
      snippetName: string;

      // An optional install specifier that can be used to point npm towards
      // packages that are not uploaded to the registry. For example,
      // this could be an URL to a git repository or a tarball.
      installSpec?: string;

      // A version field. Users do not interact with this, as currently, `snippet`
      // always installs the latest versions of snippets.
      version: string;
      description: string;
      readme: string;

      // License should be a SPDX license identifier.
      license: string;
      errorMatchers?: ErrorMatcher[];
   }

   interface SnippetIndexFile {
      // This must be 1 currently.
      indexFileVersion: 1;
      index: SnippetDescription[];
      metadata: { homepage: string };
   }

   const indexFileContents: SnippetIndexFile = {
      indexFileVersion: 1,
      index: [ /* ... */ ],
      metadata: { homepage: 'https://example.com' }
   };

   // Serialize, compress and store the index file:
   fs.writeFileSync('index.bson.br',
      zlib.brotliCompressSync(
      bson.serialize(indexFileContents)));
   ```

#. Edit `make-index.ts` as needed for your snippet package. Use the
   comments as a guide to filling out the required information.
#. Run `ts-node make-index.ts` to create the `index.bson.br file`.
#. Upload `index.bson.br` to your GitHub repository.
#. Update `snippetIndexSourceURLs` to include a URL that references
   your `index.bson.br`.
