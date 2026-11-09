<!-- Converted from reference/api/log-collection.txt (reStructuredText). Includes are inlined. -->

# Log Collection Jobs

You can use the Ops Manager API (Application Programming Interface) to download Ops Manager deployment logs. Once a
log collection request has been made, Ops Manager downloads the logs in a
background job. Use the following endpoints to create, modify, and
retrieve Ops Manager log collection jobs.

To use the Log Collection resources, you must be an Ops Manager user with
at least one of the following project roles:

- `Group Automation Admin`
- `Group Backup Admin`
- `Group Monitoring Admin`

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Endpoints

The following lists the endpoints available for the log collection jobs
resource.

| Method | Endpoint | Description |
|---|---|---|
| `GET` | /groups/{PROJECT-ID}/logCollectionJobs | Retrieves all available log collection jobs in the specified project. |
| `GET` | /groups/{PROJECT-ID}/logCollectionJobs/{JOB-ID} | Retrieves a single log collection job as specified by the `jobId`. |
| `GET` | /groups/{PROJECT-ID}/logCollectionJobs/{JOB-ID}/download | Downloads the logs from a single log collection job. |
| `POST` | /groups/{PROJECT-ID}/logCollectionJobs | Create a new log collection job for a given resource. |
| `PATCH` | /groups/{PROJECT-ID}/logCollectionJobs/{JOB-ID} | Extend the expiry date of a specified log collection job. |
| `PUT` | /groups/{PROJECT-ID}/logCollectionJobs/{JOB-ID}/retry | Retry a failed log collection job. |
| `DELETE` | /groups/{PROJECT-ID}/logCollectionJobs/{JOB-ID} | Delete a specified log collection job. |
