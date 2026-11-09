<!-- Converted from reference/api/hosts.txt (reStructuredText). Includes are inlined. -->

# Hosts

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

The `hosts` resource defines the `mongod` and `mongos` processes
in your deployment. Each process is identified by a unique hostname and
port combination. When you add a `mongod` or `mongos` to Ops Manager,
Ops Manager automatically discovers various valid hostname and port
combinations for the process. DNS records the names you can use to
access a given host. Ops Manager ranks the hostnames to choose a "primary"
hostname. Hostnames with the most periods rank highest, while the
loopback address (`127.0.0.1`) and `localhost` lowest. Ops Manager treats
the "losing" hostnames as host aliases.

When Ops Manager receives a ping from the Monitoring, the algorithm for
assigning a primary hostname repeats. As a result, the primary hostname
may change over time. You can also
specify preferred hostnames in Ops Manager's
project settings to override the hostname algorithm.

## Endpoints

The following endpoints are available for `hosts`.

| Method | Endpoint | Description |
|---|---|---|
| GET | /groups/{PROJECT-ID}/hosts | Get all MongoDB processes in a project. |
| GET | /groups/{PROJECT-ID}/hosts/{HOST-ID} | Get one MongoDB process by host ID. |
| GET | /groups/{PROJECT-ID}/hosts/byName/{HOSTNAME:PORT} | Get one MongoDB process by its hostname and port. |
| POST | /groups/{PROJECT-ID}/hosts | Start monitoring one new MongoDB process. |
| PATCH | /groups/{PROJECT-ID}/hosts/{HOST-ID} | Update configuration of one monitored MongoDB process. |
| DELETE | /groups/{PROJECT-ID}/hosts/{HOST-ID} | Stop monitoring one MongoDB process. |
