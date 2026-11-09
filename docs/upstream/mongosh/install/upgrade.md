<!-- Converted from install/upgrade.txt (reStructuredText). Includes are inlined. -->

# Upgrade mongosh

To upgrade to the latest version of mongosh, select your operating
system and installation method at the top of the page and follow the
corresponding instructions.

This section describes how to upgrade `mongosh` on Windows
through the MSI installer.

## Steps

**Step 1: (Optional) Remove any existing mongosh binaries from your system**

If you skip this step, overwrite the existing `mongosh`
binary when you install the new version.

**Step 2: Open the MongoDB Shell download page**

Open the [MongoDB Download Center](https://www.mongodb.com/try/download/shell).

**Step 3: Select your platform and package**

a. In the Platform dropdown, select Windows x64.
b. In the Package dropdown, select msi.

**Step 4: Click Download**

**Step 5: Double-click the installer file**

**Step 6: Follow the installation prompts**

**Step 7: Ensure that the new mongosh binary is in your system PATH**

To confirm that you successfully installed the new version of
`mongosh`, run the following command:

```sh
mongosh --build-info
```

This section describes how to upgrade `mongosh` on Windows
through a downloaded zip file.

## Steps

**Step 1: (Optional) Remove any existing mongosh binaries from your system**

If you skip this step, overwrite the existing `mongosh`
binary when you install the new version.

**Step 2: Open the MongoDB Shell download page**

Open the [MongoDB Download Center](https://www.mongodb.com/try/download/shell).

**Step 3: Select your platform and package**

a. In the Platform dropdown, select your Linux distribution.
b. In the Package dropdown, select tgz.

**Step 4: Click Download**

**Step 5: Extract the files from the downloaded archive**

The archive contains a `bin` folder with the following binaries:

- `mongosh`
- `mongosh_crypt`

**Step 6: Add the path to the extracted bin folder to your system PATH**

**Step 7: Verify the installation**

To confirm that you successfully installed the new version of
`mongosh`, run the following command:

```sh
mongosh --build-info
```

This section describes how to upgrade `mongosh` on macOS with
Homebrew.

## Steps

**Step 1: Update package information**

```sh
brew update
```

**Step 2: Upgrade mongosh**

```sh
brew upgrade mongosh
```

**Step 3: Verify the installation**

To confirm that you successfully installed the new version of
`mongosh`, run the following command:

```sh
mongosh --build-info
```

## Steps

**Step 1: (Optional) Remove any existing mongosh binaries from your system**

If you skip this step, overwrite the existing `mongosh`
binary when you install the new version.

**Step 2: Open the MongoDB Shell download page**

Open the [MongoDB Download Center](https://www.mongodb.com/try/download/shell).

**Step 3: Select your platform and package**

a. In the Platform dropdown, select your Linux distribution.
b. In the Package dropdown, select tgz.

**Step 4: Click Download**

**Step 5: Extract the files from the downloaded archive**

The archive contains a `bin` folder with the following binaries:

- `mongosh`
- `mongosh_crypt`

**Step 6: Add the path to the extracted bin folder to your system PATH**

**Step 7: Verify the installation**

To confirm that you successfully installed the new version of
`mongosh`, run the following command:

```sh
mongosh --build-info
```

This section describes how to upgrade `mongosh` on Ubuntu Linux.

## Steps

**Step 1: Update package information**

```sh
sudo apt-get update
```

**Step 2: Upgrade the mongosh package**

```sh
sudo apt-get install --only-upgrade mongodb-mongosh
```

**Step 3: Verify the installation**

To confirm that you successfully installed the new version of
`mongosh`, run the following command:

```sh
mongosh --build-info
```

This section describes how to upgrade `mongosh` on Debian Linux.

## Steps

**Step 1: Update package information**

```sh
sudo apt-get update
```

**Step 2: Upgrade the mongosh package**

```sh
sudo apt-get install --only-upgrade mongodb-mongosh
```

**Step 3: Verify the installation**

To confirm that you successfully installed the new version of
`mongosh`, run the following command:

```sh
mongosh --build-info
```

This section describes how to upgrade `mongosh` on Red Hat
Enterprise Linux 9 and Oracle Linux 9.

## Steps

**Step 1: Upgrade the mongosh package**

```sh
sudo yum update mongodb-mongosh
```

**Step 2: Verify the installation**

To confirm that you successfully installed the new version of
`mongosh`, run the following command:

```sh
mongosh --build-info
```

This section describes how to upgrade `mongosh` on Amazon Linux.

## Steps

**Step 1: Upgrade the mongosh package**

```sh
sudo yum update mongodb-mongosh
```

**Step 2: Verify the installation**

To confirm that you successfully installed the new version of
`mongosh`, run the following command:

```sh
mongosh --build-info
```

This section describes how to upgrade `mongosh` on Linux
distributions using a `.tgz` archive.

## Steps

**Step 1: (Optional) Remove any existing mongosh binaries from your system**

If you skip this step, overwrite the existing `mongosh`
binary when you install the new version.

**Step 2: Open the MongoDB Shell download page**

Open the [MongoDB Download Center](https://www.mongodb.com/try/download/shell).

**Step 3: Select your platform and package**

a. In the Platform dropdown, select your Linux distribution.
b. In the Package dropdown, select tgz.

**Step 4: Click Download**

**Step 5: Extract the files from the downloaded archive**

The archive contains a `bin` folder with the following binaries:

- `mongosh`
- `mongosh_crypt`

**Step 6: Add the path to the extracted bin folder to your system PATH**

**Step 7: Verify the installation**

To confirm that you successfully installed the new version of
`mongosh`, run the following command:

```sh
mongosh --build-info
```
