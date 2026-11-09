<!-- Converted from tutorial/remove-monitored-process-api.txt (reStructuredText). Includes are inlined. -->

# Stop Monitoring a Process

This tutorial shows you how to stop monitoring a process. Once you
stop monitoring a process, Ops Manager stops displaying its status and tracking its
metrics.

## Understand the Objectives

Learn how to use the Ops Manager Administration API to:

- Find the host ID for the process.
- Stop monitoring the process that matches the host ID.
- Verify that Ops Manager no longer monitors the process.

## Complete the Prerequisites

Complete these prerequisites before you complete the tutorial.

- Configure your access to the Ops Manager Administration API.
- Get the permissions needed to change monitoring settings. You need one of
  the following roles:

  - `Project Monitoring Admin`
  - `Project Owner`
- Terminate the backups for the process before you
  stop monitoring it.

## Follow These Steps

Complete all the following steps to use the API to stop monitoring a process.
 
**Step 1: Find the host ID for the process.**

Use the /reference/api/hosts/get-one-host-by-hostname-port
resource to find the process and retrieve the `id` value.

### Learn What This Step Does

The /reference/api/hosts/get-one-host-by-hostname-port
resource uses the hostname and port you specify to find the process. Then, it
returns information about this process. You can find the `id` needed for the
next step in the response.

### Issue This Command

Copy the following curl command. Paste it into your preferred terminal or
console. Replace the displayed placeholders with these values:

| Placeholder | Description |
|---|---|
| `{PUBLIC-KEY}` | .. include:: /includes/api/list-tables/tutorials/list-rows/list-table-placeholders-public-key.rst |
| `{PRIVATE-KEY}` | .. include:: /includes/api/list-tables/tutorials/list-rows/list-table-placeholders-private-key.rst |
| `{PROJECT-ID}` | .. include:: /includes/api/list-tables/tutorials/list-rows/list-table-placeholders-project-id.rst |
| `{HOSTNAME}` | Primary hostname that Ops Manager uses to connect to the instance. This may be a hostname, an FQDN (fully qualified domain name), an IPv4 (Internet Protocol version 4) address, or an IPv6 (Internet Protocol version 6) address. |
| `{PORT}` | Port on which the process listens. |

Replace the placeholders in the command, then execute it.

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --request GET "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/hosts/byName/{HOSTNAME}:{PORT}"
```

### Copy the Host's ID

In the response body, copy the value returned in the `id` field. You need the
value for the next step.

**Example:**

```json
{
  "alertsEnabled" : true,
  "aliases": [ "server1.example.com:27017", "203.0.113.3:27017" ],
  "authMechanismName" : "SCRAM-SHA-1",
  "clusterId" : "<cluster-ID-1>",
  "created" : "2021-04-22T19:56:50Z",
  "groupId" : "<project-ID-1>",
  "hasStartupWarnings" : false,
  "hidden" : false,
  "hostEnabled" : true,
  "hostname" : "server1.example.com",
  "id" : "{HOST-ID}",
  "ipAddress": "203.0.113.3",
}
```

**Step 2: Stop monitoring the process that matches the host ID.**

Use the /reference/api/hosts/delete-one-host resource
to stop monitoring the host.

### Learn What This Step Does

The /reference/api/hosts/delete-one-host resource
doesn't actually delete the host.
The resource deletes the host from the list of hosts that Ops Manager monitors. This
removes the process from monitoring.

### Issue This Command

Copy the following curl command. Paste it into your preferred terminal or
console. Replace the displayed placeholders with these values:

| Placeholder | Description |
|---|---|
| `{PUBLIC-KEY}` | .. include:: /includes/api/list-tables/tutorials/list-rows/list-table-placeholders-public-key.rst |
| `{PRIVATE-KEY}` | .. include:: /includes/api/list-tables/tutorials/list-rows/list-table-placeholders-private-key.rst |
| `{PROJECT-ID}` | .. include:: /includes/api/list-tables/tutorials/list-rows/list-table-placeholders-project-id.rst |
| `{HOST-ID}` | Unique identifier of the host for the process. Use the `id` from step 1. |

Replace the placeholders in the command, then execute it.

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --request DELETE "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/hosts/{HOST-ID}"
```

**Step 3: Verify that Ops Manager no longer monitors the process.**

Use the /reference/api/hosts/get-one-host-by-hostname-port
resource again to attempt to find the process using its hostname and port. Then, verify
that `details` returns ``No host with hostname
and port {HOSTNAME}:{PORT} exists in group {PROJECT-ID}``.

### Learn What This Step Does

The /reference/api/hosts/get-one-host-by-hostname-port
resource uses the hostname and port you specify to find the process. Then, it
returns information about this process. You can tell that Ops Manager doesn't monitor
the process if the `details` value in the response is ``No host with hostname
and port {HOSTNAME}:{PORT} exists in group {PROJECT-ID}``.
This means that Ops Manager can't find the host in the
list of processes that it monitors.

### Issue This Command

Copy the following curl command. Paste it into your preferred terminal or
console. Replace the displayed placeholders with these values:

| Placeholder | Description |
|---|---|
| `{PUBLIC-KEY}` | .. include:: /includes/api/list-tables/tutorials/list-rows/list-table-placeholders-public-key.rst |
| `{PRIVATE-KEY}` | .. include:: /includes/api/list-tables/tutorials/list-rows/list-table-placeholders-private-key.rst |
| `{PROJECT-ID}` | .. include:: /includes/api/list-tables/tutorials/list-rows/list-table-placeholders-project-id.rst |
| `{HOSTNAME}` | Primary hostname that Ops Manager uses to connect to this instance. This may be a hostname, an FQDN, an IPv4 address, or an IPv6 address. |
| `{PORT}` | Port on which the process listens. |

Replace the placeholders in the command, then execute it.

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --request GET "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/hosts/byName/{HOSTNAME}:{PORT}"
```

### Check the Response Details

In the response body, check the value returned in the `details` field. If
`details` returns ``No host with hostname
and port {HOSTNAME}:{PORT} exists in group {PROJECT-ID}``, you succeeded. Ops Manager no longer monitors the process.
