<!-- Converted from tutorial/configure-available-mongodb-version.txt (reStructuredText). Includes are inlined. -->

# Add a Custom MongoDB Build

You can add custom-built versions of MongoDB for Ops Manager to download.
Automation downloads these MongoDB versions "lazily": downloading
binaries for a version of MongoDB when a MongoDB process uses that
version on a managed host.

**Warning:** Serving Custom Builds when Ops Manager runs without Internet access

If you want to download a Custom Build from your Ops Manager host:

1. Run Ops Manager and its MongoDB Agents without
   access to the Internet.

#. Upload the Custom Build binary to the
   `Versions Directory` folder on the Ops Manager host.

#. Provide the full URL (Uniform Resource Locator) to the Custom Build in the
   Ops Manager Application per the "Complete the Add Custom Build form" step
   in this procedure.

Ops Manager can't serve your Custom Build binaries if it or its
Agents have Internet access. When Ops Manager, the Agents, or both
have Internet access, they download the Custom Build binaries
direct from the source over the Internet. These Custom Build
binaries aren't stored on the Ops Manager host in this scenario.

Ops Manager can't backup deployments that use third-party custom
builds. It does support custom builds that MongoDB provides.

## Add a Custom Build

The existing versions of MongoDB may not meet your immediate needs.
You can provide other versions of MongoDB through the
Custom Builds functionality.

**Step 1: Click Deployment, then the More drop-down list, then Custom Builds.**

**Step 2: Click Add Custom Build.**

**Step 3: Complete the Add Custom Build form.**

* - Parameter
  - Description

* - Platform
  - The platform on which this build can be installed.

    Accepted values are:

    - `Linux (amd64)` (64-bit Intel architecture Linux)
    - `Linux (ppc64le)` (64-bit PowerPC architecture Linux)
    - `Mac OS X (amd64)` (64-bit Intel architecture macOS)

* - Version Name
  - Your label for this build. It must begin with a valid MongoDB
    version number.

    **Example:**

    ```sh
    3.6.2-myCustomBuild
    ```

* - Download URL (Uniform Resource Locator)
  - URL (Uniform Resource Locator) from which the MongoDB Agent can download this build.
    This URL (Uniform Resource Locator) must:

    - Be accessible to from your network. It doesn't need to be Internet accessible.
    - Point to a host running an HTTP (Hypertext Transfer Protocol)\-compatible web server.
    - Point to the Custom Build binary file.

    **Important:**

    The Ops Manager Application does not check if this URL (Uniform Resource Locator) exists, only
    that it is [a complete URL](https://www.w3.org/Addressing/URL/url-spec.html).

* - Git Version
  - The complete 40-character `git` SHA-1 checksum (or *hash*)
    for this build.

    **Example:**

    ```sh
    f3fa18bc6d8a749b7a526d83d2ad969fae1236c7
    ```

* - Modules
  - If your Custom Build included any add-on modules, enter them
    into this combo box.

    Accepted values are:

    - None
    - `subscription`
    - `enterprise`

Click Add Custom Build.

**Step 4: **

The new Custom Build appears on the Custom Builds page.

**Note:**

After you create a Custom Build, you cannot edit it. You can click
the Remove link to delete it.
