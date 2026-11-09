<!-- Converted from snippets/commands.txt (reStructuredText). Includes are inlined. -->

# Snippet Commands

**Warning:**

This feature is experimental. MongoDB does not provide support for
Snippets. This feature may be changed or removed at any time without
prior notice.

Bugs are not expected, however should you encounter one, please open an
issue in the
[GitHub repository](https://github.com/mongodb-labs/mongosh-snippets/issues)
for this project.

This document provides an overview of the commands that are available
to work with snippets.

## Commands

* - Command
  - Description

* - `help`
  - Show the help text or information about a specific snippet. See
    an example.

    ```shell
    snippet help
    snippet help <snippet-name>
    ```

* - `info`
  - Show information about configured snippet repositories. See an
    example.

    ```shell
    snippet info
    ```

* - `install`
  - Install a new snippet. See an example.

    ```shell
    snippet install <snippet-name>
    ```

* - `ls`
  - List name and version of installed snippets. See an
    example

    ```shell
    snippet ls
    ```

* - `load-all`
  - Load all installed snippets into the current environment. 

    ```shell
    snippet load-all
    ```

* - `outdated`
  - List snippets that have updated registry versions. 

    ```shell
    snippet outdated
    ```

* - `refresh`
  - Clear and refresh the snippet metadata cache. See an
    example.

    ```shell
    snippet refresh
    ```

* - `search`
  - List available snippets, their version, and a brief description.
    See an example.

    ```shell
    snippet search
    ```

* - `uninstall`
  - Remove an installed snippet. See an example.

    ```shell
    snippet uninstall <snippet-name>
    ```

* - `update`
  - Get the latest versions of installed snippets

    ```shell
    snippet update
    ```
