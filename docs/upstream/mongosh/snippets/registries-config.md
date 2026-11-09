<!-- Converted from snippets/registries-config.txt (reStructuredText). Includes are inlined. -->

# Registries and Registry Configuration

**Warning:** Experimental feature

This feature is experimental. MongoDB does not provide support for
Snippets. This feature may be changed or removed at any time without
prior notice.

Bugs are not expected, however should you encounter one, please open an
issue in the
[GitHub repository](https://github.com/mongodb-labs/mongosh-snippets/issues)
for this project.

This page discusses different registries and how to configure your
system to use them. 

## Types of Registry Configuration

The snippets feature uses the
[npm package manager](https://www.npmjs.com/package/npm) to install
snippets from a pre-specified registry. You can configure your local
`mongosh` to use one or more registries: 

- The [community registry](https://github.com/mongodb-labs/mongosh-snippets/tree/main/snippets)
  that is maintained by MongoDB
- A private registry that you maintain
- Multiple registries used together

### Using the MongoDB Registry

This is a public, [community registry](https://github.com/mongodb-labs/mongosh-snippets/tree/main/snippets)
that is maintained by MongoDB.

The community registry is the default registry. It provides several
useful snippets which can help you to get started. The snippets in the
community registry are also [good examples](https://github.com/mongodb-labs/mongosh-snippets/tree/main/snippets)
to use when you are ready to create your own snippets.

MongoDB users are encouraged to contribute to this public registry. To
learn how to share your code with other MongoDB users, see
snip-contribute-a-package.

### Using Private Snippet Registries

You can share code internally using a private registry.

If your snippets reveal proprietary or sensitive information, you can
store them in a private, local registry instead of the public
registry.

To create a private registry, see snip-define-a-registry.

### Using Multiple Registries

A private registry can also be used in conjunction with the
community registry and other private registries. Using multiple
registries allows you to benefit from snippets maintained by MongoDB or
third parties while also maintaining control over code you don't want
to share externally.

To configure multiple registries, see snip-multiple-urls.

## How to Configure a Registry

To use a private registry or multiple registries: 

- snip-define-a-registry.
- Create a registry index file.
- Update `snippetIndexSourceURLs` to contain a link to your registry
  index file.
- Update `snippetRegistryURL` to point to your registry host
  (optional).

### Define a New Registry

The [npm public registry](https://registry.npmjs.org/) hosts the
MongoDB snippets community registry. You can use npm to host your own
public or private registry as well. 

**Step 1: Create A GitHub Repository.**

You will push snippet packages from your GitHub repository to your
npm registry.

Follow the [GitHub documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)
to create a repository.

**Step 2: Create An npm Registry.**

Follow the [npm registry documentation](https://docs.npmjs.com/cli/v7/using-npm/registry) to create a
registry.

**Step 3: Update `snippetIndexSourceURLs`.**

To make the new registry available to your local
`mongosh` installation, update the
`snippetIndexSourceURLs` configuration settings.

```
config.set('snippetIndexSourceURLs', 
'https://github.com/YOUR_COMPANY/PATH_TO_YOUR_REPOSITORY/index.bson.br;'
+ config.get('snippetIndexSourceURLs') )
```

**Step 4: Update `snippetRegistryURL`.**

If you created a registry that is hosted outside npm, update 
`snippetRegistryURL` to point to the new registry.

### Connecting to Registries

You can use a private registry in addition to, or instead of, the
community MongoDB registry. 

`snippetIndexSourceURLs` ia a list of URLs. Each URL defines a path
to an index file that contains metadata for the snippets in that
registry. 

Configure an additional registry by adding a URL to
`snippetIndexSourceURLs`. 

```shell
config.set('snippetIndexSourceURLs', 
  'https://github.com/YOUR_COMPANY/PATH_TO_YOUR_REPOSITORY/index.bson.br;'
  + config.get('snippetIndexSourceURLs')
)
```

Restart `mongosh` for the update to take effect.

**Important:**

If two snippets with the same name appear in multiple registries,
local system updates will be based on the entry in the first
registry in the `snippetIndexSourceURLs` list.

Do not reuse snippet names to avoid potential conflicts.
