<!-- Converted from tutorial/update-version-manifest.txt (reStructuredText). Includes are inlined. -->

# Update Version Manifest Manually

You can use Automation to install and upgrade MongoDB instances in your
deployment. You need to give Ops Manager a list of which versions can be
installed. The complete list of all possible MongoDB editions and
versions is called the `version manifest`.

If you configure the MongoDB Agent to use remote or hybrid downloads,
Ops Manager updates the version manifest automatically.

If you configure the MongoDB Agent to use local downloads, you must 
update the version manifest manually.

To learn more about **Remote Mode**, **Hybrid Mode**, and **Local 
Mode**, see om-modes.

**Step 1: Open the Ops Manager Application.**

From a computer that can access the Internet and the Ops Manager
hosts, open the Ops Manager Application.

**Step 2: Navigate to the Version Manifest page.**

a. Click Admin in the upper right corner.
b. Click the General tab.
c. Click Version Manifest.

**Step 3: Click Update MongoDB Version Manifest from MongoDB, Inc.**

- If the version manifest update succeeds, the last updated note
  changes to the current date and time.

  **Example:**

  The following output is for a successful update. 

  The current manifest has a last updated time of
  01/23/2023 - 00:00.

  You can stop this procedure at this step.

- If the version manifest update fails, a warning describing the
  failure displays with a text box beneath it. 

  **Example:**

  The following output is for an Internet Access Error:

  Auto Update failed. It does not appear your web browser has
  access to the internet. To update the manifest you must place
  the contents the file located at [https://opsmanager.mongodb.com/static/version_manifest/7.0.json](https://opsmanager.mongodb.com/static/version_manifest/7.0.json) into the box below.

  You need to continue to the next step.

**Step 4: Copy the version manifest contents.**

a. Open the manifest JSON file at [https://opsmanager.mongodb.com/static/version_manifest/7.0.json](https://opsmanager.mongodb.com/static/version_manifest/7.0.json) in your browser.
b. Select all of the manifest contents.
c. Copy the contents.

**Step 5: Return to the Version Manifest page in the Ops Manager Application.**

**Step 6: Paste the version manifest contents into the Ops Manager Application.**

a. Paste the `version manifest` into the text box beneath the
   warning.
b. Click Submit MongoDB Version Manifest.
