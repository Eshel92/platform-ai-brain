<!-- Converted from administration/full-time-diagnostic-data-capture.txt (reStructuredText). Includes are inlined. -->

# Full Time Diagnostic Data Capture

To help MongoDB engineers analyze server behavior, `mongod` and
`mongos` processes include a Full Time Diagnostic Data
Capture (FTDC) mechanism. FTDC is enabled by default. Due to its
importance in debugging deployments, FTDC thread failures are fatal and
stop the parent `mongod` or `mongos` process.

## Behavior

**Note:** FTDC User Permissions on Windows

On Windows, to collect system data such as disk, CPU, and memory, FTDC 
requires Microsoft access permissions from the following groups:

- Performance Monitor Users

- Performance Log Users

If the user running `mongod` and `mongos` is not an administrator, add them to these groups to log
FTDC data. For more information, see the [Microsoft documentation](https://learn.microsoft.com/en-us/windows/win32/perfctrs/restricting-access-to-performance-extension--dlls).

FTDC periodically collects statistics produced by the following 
commands:

- `serverStatus`
- `replSetGetStatus` (`mongod` only)
- `collStats` for the `local.oplog.rs` collection (`mongod` only)
- `connPoolStats` (`mongos` only)

Depending on the host operating system, the diagnostic data may include
one or more of the following utilization statistics:

- CPU utilization
- Memory utilization
- Disk utilization related to performance. FTDC does not include
  data related to storage capacity.
- Network performance statistics. FTDC only captures metadata and
  does not capture or inspect any network packets.

**Note:**

If the `mongod` process runs in a container, FTDC 
reports utilization statistics from the perspective of the container 
instead of the host operating system. For example, if a the 
`mongod` runs in a container that is configured with RAM 
restrictions, FTDC calculates memory utilization against the container's 
RAM limit, as opposed to the host operating system's RAM limit.

FTDC collects statistics produced by the following commands on
file rotation or startup:

- `getCmdLineOpts`
- `buildInfo`
- `hostInfo`

### FTDC Data Files

`mongod` processes store FTDC data files in a 
`diagnostic.data` directory under the instances 
`storage.dbPath`. All diagnostic data files are stored
under this directory. For example, given a `dbPath`
of `/data/db`, the diagnostic data directory would be
`/data/db/diagnostic.data`. 

`mongos` processes store FTDC data files in a 
diagnostic directory relative to the `systemLog.path` log 
path setting. MongoDB truncates the logpath's file extension and 
concatenates `diagnostic.data` to the remaining name. For example, 
given a `path` setting of
`/var/log/mongodb/mongos.log`, the diagnostic data directory would be 
`/var/log/mongodb/mongos.diagnostic.data`.

### FTDC Privacy

FTDC data files are compressed and not human-readable. They inherit
the same file access permissions as the MongoDB data files. Only
users with access to FTDC data files can transmit the FTDC data.

MongoDB engineers cannot access FTDC data without explicit
permission and assistance from system owners or operators.

FTDC data **never** contains any of the following information:

- Samples of queries, query predicates, or query results
- Data sampled from any end-user collection or index
- System or MongoDB user credentials or security certificates

FTDC data contains certain host machine information such as
hostnames, operating system information, and the options or settings
used to start the `mongod` or 
`mongos`. This information may be
considered protected or confidential by some organizations or
regulatory bodies. For clusters where these fields are
configured with protected, confidential, or PII data, please notify
MongoDB engineers before sending FTDC data to coordinate
appropriate security measures.

## Details

You can view the FTDC source code on the
[MongoDB Github Repository](https://github.com/mongodb/mongo/tree/master/src/mongo/db/ftdc).
The `ftdc_system_stats_*.ccp` files specifically define any
system-specific diagnostic data captured.

### FTDC Defaults

FTDC runs with the following defaults:

- Data capture every 1 second
- 200MB maximum `diagnostic.data` folder size. 

These defaults provide useful data to MongoDB engineers with minimal
impact on performance or storage size. Modify these values only if
requested by MongoDB engineers for specific diagnostic purposes.

**Important:**

MongoDB overwrites older data as the folder approaches its
size limit. To ensure critical diagnostic information is
preserved, capture the `diagnostic.data` directory at the
time of an incident. Once MongoDB purges FTDC data, it is no
longer available for diagnostic analysis.

### Data Retention in On-Premises Environments

MongoDB stores FTDC data only on the local host. You cannot use
FTDC data forwarded by OTel or other log shipping pipelines for
diagnostic purposes.

In on-premises environments that use ephemeral storage or
automation tools such as Terraform, FTDC data is lost when a host
is terminated or rebuilt. To improve the availability of FTDC data
for diagnostic investigations, consider one or both of the
following actions:

- Store the `diagnostic.data` directory on persistent storage.
- Periodically copy the `diagnostic.data` directory to a
  persistent external location.

MongoDB engineers rely on FTDC data for accurate diagnosis.

### Disable FTDC

**Warning:**

Not recommended for production environments.

To disable FTDC, start up the `mongod` or 
`mongos` with the 
`diagnosticDataCollectionEnabled: false` option in the 
`setParameter` settings of your configuration file:

```yaml
setParameter:
  diagnosticDataCollectionEnabled: false
```

Disabling FTDC may increase the time or resources required when 
analyzing or debugging issues with support from MongoDB engineers. 
For information on MongoDB Support, visit [Get Started With MongoDB Support](https://www.mongodb.com/support/get-started).
