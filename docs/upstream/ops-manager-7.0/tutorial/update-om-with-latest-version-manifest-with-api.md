<!-- Converted from tutorial/update-om-with-latest-version-manifest-with-api.txt (reStructuredText). Includes are inlined. -->

# Upload the Latest Version Manifest to Ops Manager with the API

For Ops Manager deployments with limited internet access, the 
`version manifest` that Ops Manager uses might not match the latest 
version manifest that MongoDB provides.

You can download the latest version manifest from MongoDB, then upload
it to Ops Manager with the API.

## Variables for API Resources to Update the Version Manifest

The API resources use one or more of these variables. Replace these 
variables with your desired values before calling these API resources.

| Name | Type | Description |
|---|---|---|
| `{PUBLIC-KEY}` | string | Public API key for your API (Application Programming Interface) credentials. |
| `{PRIVATE-KEY}` | string | Private API Key for your API (Application Programming Interface) credentials. |
| `<OpsManagerHost>:<Port>` | string | URL (Uniform Resource Locator) of your Ops Manager instance. |
| `{OPS-MANAGER-VERSION}` | string | Major and minor version of your Ops Manager instance. For example, `4.2`. |

## Prerequisite

Your API (Application Programming Interface) key must have the `Global Automation Admin` or the
`Global Owner` role.

## Procedure

To update your Ops Manager version to use the latest version manifest:

**Step 1: Retrieve the current version manifest from MongoDB.**

From a machine that can access the public internet, run the following 
command to retrieve the latest version manifest for
your Ops Manager version from MongoDB:

**Tip:**

Replace `{OPS-MANAGER-VERSION}` with your Ops Manager major and minor
version.

For example, `4.2`. 

```sh
curl --request GET "https://opsmanager.mongodb.com/static/version_manifest/{OPS-MANAGER-VERSION}.json" \
     --header "Accept: application/json" \
     --output {OPS-MANAGER-VERSION}.json
```

The JSON (Javascript Object Notation) file you receive in response includes all data that your 
Ops Manager instance needs. This covers all versions and variants
of MongoDB that your version of Ops Manager supports.

The parameters and values in this file -- as well as how they are
structured -- can change without notice.

**Step 2: Transfer the version manifest JSON (Javascript Object Notation) file to a host that can access your Ops Manager instance.**

**Step 3: Upload the version manifest JSON (Javascript Object Notation) file to your Ops Manager instance.**

From a host that can access your Ops Manager instance, use the 
Update the Version Manifest endpoint to
upload the latest version manifest to Ops Manager.

Run the following command, replacing the placeholders with the version-manifest-api-tutorial-vars:

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --header "Accept: application/json" \
     --header "Content-Type: application/json" \
     --include \
     --request PUT "https://<OpsManagerHost>:<Port>/api/public/v1.0/versionManifest?pretty=true" \
     --data @{OPS-MANAGER-VERSION}.json
```

**Step 4: Confirm that Ops Manager uses the latest version manifest.**

From a host that can access your Ops Manager instance, use the 
Retrieve the Ops Manager Version Manifest endpoint to
confirm that Ops Manager uses the latest version manifest. You *can* call  
this endpoint without having an API 
key.

Run the following command, replacing the placeholders with the
version-manifest-api-tutorial-vars:

```sh
curl --include --header "Accept: application/json" \
     --request GET "https://<OpsManagerHost>:<Port>/api/public/v1.0/unauth/versionManifest?pretty=true"  
```

The response should match the version manifest you downloaded from
MongoDB and uploaded to your Ops Manager instance.
