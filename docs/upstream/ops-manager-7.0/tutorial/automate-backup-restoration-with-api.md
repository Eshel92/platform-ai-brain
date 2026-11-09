<!-- Converted from tutorial/automate-backup-restoration-with-api.txt (reStructuredText). Includes are inlined. -->

# Automate Backup Restoration through the API

To restore a snapshot using the API (Application Programming Interface):

1. Find the ID of the snapshot that you want to restore.
2. Create a restore job using that snapshot ID.

## Prerequisites

You must have API (Application Programming Interface) access. To learn how to get access, see
/tutorial/configure-public-api-access.

To find and download the snapshot, your API (Application Programming Interface) Key needs read access to
snapshots in the desired project. Grant the API Key the
`Project Read Only` role on the Project that relates to that
snapshot.

## Variables for Automated Restore API Resources

The API resources use one or more of these variables. Replace these
variables with your desired values before calling these API resources.

| Name | Type | Description |
|---|---|---|
| `PUBLIC-KEY` | string | Your public API Key for your API (Application Programming Interface) credentials. |
| `PRIVATE-KEY` | string | Your private API Key for your API (Application Programming Interface) credentials. |
| `<OpsManagerHost>:<Port>` | string | URL (Uniform Resource Locator) of your Ops Manager instance. |
| `GROUP-ID` | string | Unique identifier of your project that contains the source cluster for the restore job. You can find this value in the Project Settings of that project. |
| `CLUSTER-ID` | string | Unique identifier of your source cluster for the restore job. |
| `TARGET-GROUP-ID` | string | Unique identifier of your project that contains the target cluster for the restore job. |
| `TARGET-CLUSTER-ID` | string | Unique identifier of your target cluster for the restore job. |
| `SNAPSHOT-ID` | string | Unique identifier of the snapshot you want to restore. |

## Procedure

**Step 1: Retrieve the snapshot ID.**

Call the Get All Snapshots resource to find the ID for the desired snapshot.

Invoke the following command:

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --header "Accept: application/json" \
     --header "Content-Type: application/json" \
     --request GET "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/snapshots?pretty=true"
```

**Step 2: Create a restore job for the snapshot.**

Call the
Create One Restore Job
resource to request a snapshot restore.

Invoke the following command:

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --header "Accept: application/json" \
     --header "Content-Type: application/json" \
     --request POST "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs?pretty=true" \
     --data '
       {
         "delivery" : {
           "methodName" : "AUTOMATED_RESTORE",
           "targetGroupId" : "{TARGET-PROJECT-ID}",
           "targetClusterId" : "{TARGET-CLUSTER-ID}"
         },
         "snapshotId": "{SNAPSHOT-ID}"
       }'
```

**Note:**

To learn more about restoring snapshots with additional examples,
see the
Create One Restore Job for One Cluster
API (Application Programming Interface) resource page.
