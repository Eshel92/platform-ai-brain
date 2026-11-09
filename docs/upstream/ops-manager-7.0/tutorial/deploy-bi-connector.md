<!-- Converted from tutorial/deploy-bi-connector.txt (reStructuredText). Includes are inlined. -->

# Deploy a BI Connector

The MongoDB Connector for Business Intelligence allows you to query a 
MongoDB database using SQL commands to aid in data analysis. It 
translates SQL queries from data analysis tools to MongoDB aggregation 
pipelines on MongoDB database. To learn more about the 
BI Connector, see the [BI Connector manual](https://www.mongodb.com/docs/bi-connector/).

Use the following procedure to deploy a new MongoDB BI Connector
for Ops Manager to manage.

## Limitations

- The `BI Connector` allows only
  [read-only operations](https://www.mongodb.com/docs/bi-connector/current/supported-operations/) 
  on data served in MongoDB databases. To create, update, or delete 
  data you must use `mongosh` or any appropriate driver.

- MongoDB BI Connector for Ops Manager is not compatible with the 
  following authentication methods:

  - Kerberos

  - x.509

- The BI Connector cannot be deployed using Ops Manager
  if the automation agent authentication mechanism is 
  Kerberos (`GSSAPI`) authentication.

- The BI Connector skips field names that contain a period (.), such as `price.usd`.
  Such fields don't appear in the output schema. 

## Prerequisites

To deploy MongoDB clusters, you must
provision hosts to serve those
clusters. Ops Manager requires access to these hosts.

**Important:**

If you run `MongoDB Enterprise`
and provision your own Linux hosts, then you must manually install a
set of dependencies to each server **before installing MongoDB**.
The MongoDB manual provides the appropriate command to install the
dependencies.

To learn more about the specifics for an operating system, see the
following:

- Red Hat

- Ubuntu

- Debian

- SUSE

- Amazon AMI

             

## Procedure

**Step 1: Navigate to the Processes tab for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. Click Processes in the sidebar.

**Step 2: Choose New BI Connector.**

a. Click the Add New dropdown menu.
b. Click New BI Connector.

**Step 3: Configure the BI Connector instance.**

In the New BI Connector modal, configure the following
settings:

* - Choose Server
  - Select the host where this new BI Connector is installed.

* - Deployment Item
  - Select the deployment item (standalone, replica set, 
    or sharded cluster) to which this new BI connector 
    connects.

* - Port to Listen On
  - Type the IANA (Internet Assigned Numbers Authority) port number you want to use when connecting
    to this new BI Connector. The recommended port number is
    `3306`.

* - Read Preference
  - Select how the BI connector routes read operations to the 
    members of a replica set. Available values include:

    - `Primary`
    - `Primary Preferred`
    - `Secondary Only`
    - `Secondary Preferred`
    - `Nearest`

* - Included Namespace(s) *(Optional)* 
  - Type the name of a database and/or collection to limit what
    data the BI Connector can access.

    Leave this box blank to allow the BI Connector to use all 
    namespaces on the host.

    Click the + add another namespace link to add 
    another namespace to your list of included namespaces.

**Note:**

Ops Manager manages the BI Connector version. You cannot select a 
different version of the BI Connector.

**Step 4: Set any Additional settings for the BI Connector instance.**

If you need to use TLS (Transport Layer Security) to connect with the Deployment Item, 
configure these settings:

|  |  |
|---|---|
| TLs Mode | Select Disabled, Allow TLS, or Require TLS. |
| TLS PEM Key File Path | Type the path on the MongoDB host where the TLS PEM key file is stored. |
| TLS PEM Key Password *(Optional)* | If you encrypted the PEM file, type its password. |
| Minimum TLS Version | Select the minimum TLS (Transport Layer Security) version to connect to the `BI Connector`. Default value is `TLS1_0`. Accepted values are `TLS1_0`, `TLS1_1`, and `TLS1_2`. |
| MongoDB Minimum TLS Version | Select the minimum TLS (Transport Layer Security) version to connect to MongoDB. Default value is `TLS1_0`. Accepted values are `TLS1_0`, `TLS1_1`, and `TLS1_2`. |

|  |  |
|---|---|
| Linux Log File Path | *(Conditional: BI Connector is installed on a Linux platform)* Type the path to the BI Connector log on that host. |
| Windows Log File Path | *(Conditional: BI Connector is installed on a Windows platform)* Type the path to the BI Connector log on that host. |
| Log Verbosity | Select logging level for the BI Connector. Accepted values are `Lowest`, `Medium`, `Highest`. These values correspond to `log verbosity levels` of `0`, `1`, and `2`, respectively. |
| Log Rotation | Toggle to `ON` to enable. Default is `OFF`. If toggled to `ON`, the logs are rotated when the Size Threshold or Time Threshold is met. The next four settings require Log Rotation to be set to `ON`. |
| Size Threshold (MB) | *(Conditional:* Log Rotation *=* `ON` *)* Type the size the log file must reach in MB (Megabytes) before the BI Connector rotates it automatically. The default value is `1000.0` (about 1 GB (Gigabyte)). |
| Time Threshold (Hours) | *(Conditional:* Log Rotation *=* `ON` *)* Type the duration the log file must cover in hours before the BI Connector rotates it automatically. The default value is `24` hours. |
| Max Uncompressed Files | *(Conditional:* Log Rotation *=* `ON` *)* Type how many rotated log files may stay uncompressed in the log directory before they are archived and compressed. (The suggested number is `2`.) |
| Max Percent of Disk | *(Conditional:* Log Rotation *=* `ON` *)* Type the percentage of disk space on the host the log files may consume before older files are deleted. (The suggested number is `5`.) |

|  |  |
|---|---|
| Max Length for varChar Fields | Type the maximum number of characters that can exist in a `VARCHAR` field. |
| Refresh Interval (Seconds) | Type how much time must elapse in seconds before the `BI Connector` refreshes the schema. |
| Sample Size (# of Documents in Collection) | Type how many MongoDB documents are included in each sample the schema examines. To learn more on how the `BI Connector` performs sampling, see `Cached Sampling`. |
| Allow Schema Alterations from SQL Client | Toggle if the user can alter the schema using an `SQL client`. |

**Step 4: Click Create.**

**Step 5: Click Review & Deploy to review your changes.**

**Step 6: Click Confirm & Deploy to deploy your changes.**

Otherwise, click Cancel and you can make
additional changes.
