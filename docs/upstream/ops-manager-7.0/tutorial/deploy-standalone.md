<!-- Converted from tutorial/deploy-standalone.txt (reStructuredText). Includes are inlined. -->

# Deploy a Standalone MongoDB Instance

You can deploy a standalone MongoDB instance for Ops Manager to 
manage. Use standalone instances for testing and development.
**Do not** use these deployments for production systems as they lack 
replication and high availability. For all production deployments
use replica sets. To learn about replica sets, see 
/tutorial/deploy-replica-set.

**Note:** Added in Ops Manager 4.0

You can use Kubernetes to deploy MongoDB instances with
Ops Manager version 4.0 or later. 

To learn how to deploy a standalone using a Kubernetes object, see
`Deploy a Standalone` in the
MongoDB Enterprise Kubernetes Operator documentation.

## Prerequisites

You must provision a server
before deploying a standalone MongoDB instance. For testing purposes,
you can use your localhost.

## Procedure

**Step 1: Navigate to the Processes tab for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. Click Processes in the sidebar.

**Step 2: Choose New Standalone.**

a. Click the Add dropdown menu.
b. Select New Standalone.

**Step 3: Configure the standalone MongoDB instance.**

In the Process Configuration section, complete the
following fields.

|  |  |
|---|---|
| Name | Type the name for your standalone MongoDB deployment. |
| Version | Select the MongoDB version for your standalone MongoDB deployment. Ops Manager lists only the MongoDB versions that are available for your deployment. To disable this filtering, see `automation.versions.download.baseUrl.allowOnlyAvailableBuilds`. |
| Auth Schema Version | Select the schema for storing the user data for your deployment. MongoDB 3.0 uses a different schema for user data than previous versions. |
| Feature Compatibility (Optional) | Select the feature compatibility set. This field appears if your deployment MongoDB version is `3.4` or later. |
| Hostname | Type the resolvable address for the host serving your MongoDB deployment. This can be a hostname, an FQDN (fully qualified domain name), an IPv4 (Internet Protocol version 4) address, or an IPv6 (Internet Protocol version 6) address. |
| Port | Type the IANA (Internet Assigned Numbers Authority) port number for your MongoDB deployment. The default for MongoDB deployments is `27017`. |
| DB Directory Path | Type the system path to the `database directory` for this deployment. The default is `/data/myProcess`. |
| Log File Path | Type the system path to the `log file` setting for this deployment. The default is `/data/myProcess/mongodb.log`. |

**Step 4: Set any Advanced Configuration options for the standalone MongoDB instance.**

In the Advanced Configuration Options section, add any
additional runtime options you want to set for your MongoDB 
deployment.

To add an option:

a. Click Add Option.
b. Select a Startup Option.
c. Set an acceptable value for that Startup Option.

For descriptions of Advanced Configuration Options, see
/reference/deployment-advanced-options.

**Step 4: Click Apply.**

**Step 5: Click Review & Deploy to review your changes.**

**Step 6: Click Confirm & Deploy to deploy your changes.**

Otherwise, click Cancel and you can make
additional changes.
