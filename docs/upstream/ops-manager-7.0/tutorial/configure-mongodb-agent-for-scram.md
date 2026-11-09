<!-- Converted from tutorial/configure-mongodb-agent-for-scram.txt (reStructuredText). Includes are inlined. -->

# Configure MongoDB Agent for Authentication

MongoDB supports the following authentication mechanisms depending on your MongoDB version:

| MongoDB Version | Default Authentication Mechanism |
|---|---|
| 4.0 or later | SCRAM authentication mechanisms with the `SHA-256` and `SHA-1` hash functions. `SCRAM-SHA-1` (RFC 5802) and `SCRAM-SHA-256` (RFC 7677) are IETF (Internet Engineering Task Force) standards that define best practice methods for implementation of challenge-response mechanisms for authenticating users with passwords. |
| 3.0 to 3.6 | SCRAM authentication mechanism with`SHA-1` hash function. |
| 2.6 or earlier | MongoDB Challenge and Response (`MONGODB-CR`). `MONGODB-CR` is a challenge-response mechanism that authenticates users through passwords. |

## Prerequisites

### Configure Deployments to Use Authentication

The MongoDB Agent interacts with the MongoDB databases in your
deployment as a MongoDB user would. As a result, you must configure
your MongoDB deployment and the MongoDB Agent to support authentication.

You can specify the deployment's authentication mechanisms when
adding the
deployment, or you can edit the settings for an existing
deployment. At minimum, the deployment must enable the authentication
mechanism you want the MongoDB Agent to use. The MongoDB Agent can use
any supported authentication mechanism.

## Configure the MongoDB Agent for Authentication

The MongoDB Agent can use `SCRAM-SHA-1` or `SCRAM-SHA-256`
to authenticate to hosts that enforce access control.

**Note:**

With Automation, Ops Manager manages MongoDB Agent authentication for
you. To learn more about authentication, see /tutorial/enable-mongodbcr-authentication-for-group.

**automation:**

When you install the MongoDB Agent with Automation, Ops Manager creates a
user to authenticate on the MongoDB database. Ops Manager create this
MongoDB user (`mms-automation`) in the `admin` database with
the correct privileges for each MongoDB Agent function.

Configure these credentials in Ops Manager.

1. Navigate to Deployment arrow-right
   Security arrow-right
   Settings

2. Continue through the modal until you see the
   Configure Ops Manager Agents page

3. Add the appropriate credentials:

   | Setting | Value |
   |---|---|
   | MongoDB Agent Username | Enter the MongoDB Agent username. |
   | MongoDB Agent Password | Enter the password for the MongoDB Agent username. |

**monitoring-backup-only:**

Each MongoDB Agent function uses a different set of 
MongoDB shell (`mongosh`) commands to configure a user with the 
appropriate roles and privileges.

**backup:**

User creation commands vary depending on the version of
MongoDB that you use:

**backup-fcv4.2:**

To back up MongoDB instances running FCV 4.2
and later, create a user in the `admin` database.
Assign this user the roles provided in the following
example.

Use the following `mongosh` command to create the
user:

```javascript
db.getSiblingDB("admin").createUser(
   {
      user: "<username>",
      pwd: "<password>",
      roles: [ { 
        role: "clusterAdmin", db: "admin"
      } ]
   }
)
```

To learn more about the required access, see
Required Access for MongoDB Agent Backup

**backup-fcv4.0:**

To back up MongoDB instances running FCV 4.0 or
earlier, create a user in the `admin` database.
Assign this user the roles provided in the following
example.

Use the following `mongosh` command to create the
user:

```javascript
db.getSiblingDB("admin").createUser(
  {
    user: "<username>",
    pwd: "<password>",
    roles: [ {
      role: "backup", db: "admin"
    } ]
  }
)
```

To learn more about the required access, see
Required Access for MongoDB Agent Backup

**Configure Backup Credentials**

After you create the user for the Backup function, add
the credentials to the Backup Settings.

1. Navigate to Backup arrow-right
   backup-deployment arrow-right
   `ellipsis` arrow-right
   Edit Credentials.

2. Click Credentials.

3. Add the appropriate credentials:

   | Setting | Value |
   |---|---|
   | Backup Username | Enter the Backup username. |
   | Backup Password | Enter the password for the Backup username. |

**monitoring:**

To monitor MongoDB 4.0 or later instances that use SCRAM
authentication, add a user to the `admin` database in
MongoDB. Assign this user the roles provided in the
following example.

```javascript
db.getSiblingDB("admin").createUser(
   {
      user: "<username>",
      pwd: "<password>",
      roles: [ {
        role: "clusterMonitor", db: "admin"
      } ]
   }
)
```

To learn what roles this function requires, see
Monitoring settings.

**Configure Monitoring Credentials**

After you create the user for the Monitoring function, add
the credentials to the Monitoring Settings.

1. Navigate to Deployment
   arrow-right deployment
   arrow-right `ellipsis`
   arrow-right Monitoring Settings.

2. Click Credentials.

3. Add the appropriate credentials:

   | Setting | Value |
   |---|---|
   | Monitoring Username | Enter the Monitoring username. |
   | Monitoring Password | Enter the password for the Monitoring username. |
