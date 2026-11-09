<!-- Converted from tutorial/retrieve-debug-diagnostics.txt (reStructuredText). Includes are inlined. -->

# Download Diagnostic Archives

**Warning:**

Don't add passwords or secrets to JVM (Java Virtual Machine) arguments in the `mms.conf`
file. Ops Manager exposes them as plain text in the diagnostic archives.

MongoDB engineers may request that Ops Manager administrators provide
diagnostic archives for one or all projects for debugging and
troubleshooting. Project diagnostic archives also contain global system
information about Ops Manager. Use the following procedures to locate and
download these archives when requested.

## Considerations

To access this feature, you must either:

- Belong to the project, or

- Have the Global Monitoring Admin role or the Global Owner role.

## Download the Diagnostic Archive for a Project

**Step 1: Navigate to the Projects Admin page.**

a. Click the Admin link at the top right of the page.

b. Click the Projects tab.

**Step 2: Download the compressed archive of diagnostic data.**

From the `ellipsis` menu in the Actions column,
select one of the following options depending on your desired
compression type:

- Download TAR Diagnostic Archive
- Download ZIP Diagnostic Archive

The archive downloads to your local host.

## Download the Diagnostic Archive for All Projects

**Step 1: Navigate to the System Overview Admin page.**

Click the Admin link at the top right of the page. Ops Manager
displays the System Overview Admin page.

**Step 2: Download the compressed archive of diagnostic data.**

From the Diagnostic Archive section in the summary table,
select one of the following options depending on your desired
compression type:

- .tar
- .zip

The archive downloads to your local host.

## Download the Resource Usage Archive for a Project

**Step 1: Navigate to the Projects Admin page.**

a. Click the Admin link at the top right of the page.

b. Click the Projects tab.

**Step 2: Download the compressed archive of Resource Usage data.**

From the `ellipsis` menu in the Actions column,
select Download ZIP Resource Usage Archive.

The archive downloads to your local host.
