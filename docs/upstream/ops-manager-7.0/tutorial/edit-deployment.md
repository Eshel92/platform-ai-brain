<!-- Converted from tutorial/edit-deployment.txt (reStructuredText). Includes are inlined. -->

# Edit a Deployment's Configuration

You can modify a deployment's configuration and topology, including its
MongoDB versions, storage engines, and numbers of hosts or shards. You
can make modifications at all levels of a deployment's topology from a
top-level sharded cluster or
replica set to lower levels, such as a replica set within a
sharded cluster, or an individual process within a replica set. You can
also modify standalone processes.

tabs:
  - id: ui
    name: User Interface
    content: |

  - id: k8s
    name: Kubernetes
    content: |

## Considerations

hidden: true

tabs:
  - id: ui
    name: User Interface
    content: |

      Apply Changes to Cluster or Member
      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

      If you make configuration changes to an individual MongoDB
      process within a cluster, any future changes to the cluster no longer apply to the child process.

      **Example:**

      If you turn off journaling for a replica set member and
      then later change the journal commit interval for the
      replica set, the change does not apply to the member.

      MongoDB Version
      ~~~~~~~~~~~~~~~

      To choose which versions of MongoDB are available to Ops Manager, see
      /tutorial/configure-available-mongodb-version.

      - Check the following documents for any considerations or 
        compatibility issues before changing a deployment's MongoDB version:

        - The MongoDB Release Notes

          **Warning:** Upgrades from MongoDB 5.0 to 6.0

          When you upgrade a sharded cluster from MongoDB 5.0 to 6.0, you
          must use the procedure on the
          Upgrade a Sharded Cluster to 6.0 page of the MongoDB
          Manual to refresh the cached routing table for each `mongos`.

        - The documentation for your driver.

        - /reference/mongodb-compatibility

      - Plan the version change during a predefined maintenance window.

      - Change the MongoDB version on a staging environment before changing a
        production environment. Your staging environment should mirror your
        production environment. This can help avoid compatibility issues 
        that may result in downtime for your production deployment.

      - Follow the MongoDB release notes when 
        performing manual upgrades of replica sets and
        sharded clusters.

      **Note:** Downgrading Limitations

      You cannot downgrade a MongoDB deployment:

      - From version 5.0 to any version before 4.4.0
      - From version 4.4 to any version before 4.2.6

      Backup Considerations for MongoDB Versions
      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

      To learn more about backup considerations, see
      4.2-backup-considerations.

      Storage Engine
      ~~~~~~~~~~~~~~

      **Important:**

      MongoDB removed support for the MMAPv1 storage engine in MongoDB 4.2.
      If you
      edit your deployment's configuration
      to change your storage engine to storage-wiredtiger, Ops Manager
      restarts the MongoDB processes.

      If you run or upgrade to MongoDB 3.0 or later and modify the MongoDB
      storage engine, Ops Manager shuts down and restarts the MongoDB process. For
      a multi-member replica set, Ops Manager performs a rolling
      `initial sync` of each member.

      Ops Manager creates backup directories during the migration from one storage
      engine to the other if the host has adequate disk space. If disk space
      is insufficient, no backups are taken. Ops Manager *does not* delete the
      backup directories once the migration is complete. You can keep or
      delete the previous backup directories. The backup directories are
      located in  the mongod's data directory.

      **Example:**

      If the data directory was `/data/process`, the backup would be
      `/data/process.bak.UNIQUENAME`. The `UNIQUENAME` is a random
      string that Ops Manager generates.

      Before you can change the storage engine for a standalone
      instance or replica set, you must give the Automation write access to
      the MongoDB data directory's *parent* directory. The agent
      creates a temporary backup of the data in the parent directory when
      updating the storage engine. Storage engine changes on standalone 
      instances also require adequate disk space to perform a full `/mongodump` 
      and `/mongorestore`. This disk space is then restored to the 
      instance after the storage engine configuration change. Ops Manager *does not* 
      delete the backup directories. 

      You cannot change the storage engine on a config server. For
      more information on storage engines and the available options, see
      Storage in the MongoDB manual.

      Fixed Properties
      ~~~~~~~~~~~~~~~~

      You cannot modify the following settings after a deployment has been
      created:

      - `database path`
      - The hostname, `bind_ip` or
        `port` to which a MongoDB process is
        assigned

      You *can* modify the following deployment settings:

      - `log path` at the process level
      - advanced options

      Deployment Topology
      ~~~~~~~~~~~~~~~~~~~

      You can make modifications at all levels of a deployment's topology,
      including child processes.

      To modify the topology or processes, use this tutorial or one of the
      more specific tutorials:

      - /tutorial/migrate-member-to-new-hardware
      - /tutorial/convert-standalone-to-replica-set

      Project-Level Modifications
      ~~~~~~~~~~~~~~~~~~~~~~~~~~~

      Some modifications that affect a deployment occur at the project level.
      The following changes affect every MongoDB process in the project. For
      these changes, use the specified tutorials:

      - To enable TLS (Transport Layer Security) for the deployment, see
        /tutorial/enable-ssl-for-a-deployment.

      - To enable authentication for the deployment, see
        /tutorial/nav/security-enable-authentication.

      - To add or modify MongoDB users and roles for the deployment, see
        /tutorial/manage-mongodb-users.

      Multiple Modifications
      ~~~~~~~~~~~~~~~~~~~~~~

      You can combine multiple modifications into one deployment.

      **Example:**

      You could make all the following modifications before clicking the
      Review Changes button:

      - Add the latest stable version of MongoDB to the
        version-manager.

      - Enable TLS (Transport Layer Security) for the deployment's MongoDB processes.

      - Add a new sharded cluster running the latest stable version of
        MongoDB from above.

      When you click Review Changes, the review displays all the
      changes on one screen for you to confirm before deploying.

      Force Reconfigure
      ~~~~~~~~~~~~~~~~~

      *For Replica Sets and Sharded Clusters Only*

      The MongoDB Agent can force a replica set to accept a new configuration
      when you set the Force Reconfigure Replication Setting to
      `Yes`. Only force a reconfiguration to recover a replica set from a
      state in which a minority of its members are available.

      WARNING: Forcing a replica set reconfiguration might lead to a
      rollback of
      majority-committed writes.

      Proceed with caution. Contact [MongoDB Support](https://support.mongodb.com) if you have questions
      about the potential impacts of this operation.

      **See also:**

      Reconfigure a Replica Set with Unavailable Members in the MongoDB Manual.

      Removing a Shard
      ~~~~~~~~~~~~~~~~

      *For Sharded Clusters Only*

      When you remove a shard, any unsharded databases in that shard are 
      moved to a remaining shard using the 
      movePrimary command.

      All sharded collections remain online and available during the shard 
      removal process. However, read and write operations sent to unsharded 
      collections during the `movePrimary` operation can result in 
      unexpected behavior, including failure of the migration or loss of 
      data.

      We recommend moving the primary shard for any databases containing 
      unsharded collections before removing the shard.

      To learn more about removing shards, see 
      Remove Shards from an Existing Sharded Cluster.

      Removing Multiple Replica Set Members
      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

      You can remove or migrate multiple replica set members at once, but a majority of the
      voting members must remain. If you need to remove more voting members, remove
      them one at a time.

      **Example:** Example 1

      You have a four-node replica set. All nodes are voting members. You can
      remove only one node, which preserves the majority of three out of four
      voting nodes. You can remove another node from the remaining 
      three-node replica set afterward. This preserves the majority of the 
      remaining voting nodes.

      **Example:** Example 2

      You have a four-node replica set. Three nodes are voting members and 
      one node is a non-voting member. You can remove one voting member 
      and one non-voting member at the same time. This preserves the 
      majority of two out of three voting nodes.

      To learn more about voting, see Replica Set High Availability and Replica Set Elections.

  - id: k8s
    name: Kubernetes
    content: |

      **Warning:** Upgrades from MongoDB 5.0 to 6.0

      When you upgrade a sharded cluster from MongoDB 5.0 to 6.0, you
      must use the procedure on the
      Upgrade a Sharded Cluster to 6.0 page of the MongoDB
      Manual to refresh the cached routing table for each `mongos`.

      All Changes are Clusterwide
      ~~~~~~~~~~~~~~~~~~~~~~~~~~~

      Changes cannot be made to individual members of a replica
      set or sharded cluster, only to the whole set or cluster.

      Kubernetes Operator Overrides Some Ops Manager Settings
      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

      Some settings that you configure using Kubernetes Operator
      cannot be overridden in the Ops Manager Application. If you change
      one of these settings, the Kubernetes Operator reverts the
      settings each time you apply the resource specification.
      Settings that the Kubernetes Operator does not manage are
      accepted.

      The following list of settings are exclusive to Kubernetes. This
      list may change at a later date.

      These settings can be found on the Automation
      Configuration page.

      - `processes.args2_6.net.port`
      - `processes.args2_6.replication.replSetName`
      - `processes.args2_6.storage.dbPath`
      - `processes.args2_6.systemLog.path`
      - `processes.authSchemaVersion`
      - `processes.cluster` (mongos processes)
      - `processes.featureCompatibilityVersion`
      - `processes.hostname`
      - `processes.name`
      - `processes.version`
      - `replicaSets._id`
      - `replicaSets.members._id`
      - `replicaSets.members.host`
      - `replicaSets.members`
      - `replicaSets.version`
      - `sharding.clusterRole` (config server)
      - `sharding.configServerReplica`
      - `sharding.name`
      - `sharding.shards._id`
      - `sharding.shards.rs`

      **Example:**

      - Kubernetes Operator creates a replica set of 3 members.
      - You changed
        `storage.wiredTiger.engineConfig.cacheSizeGB`
        to `40`.
      - You then scale the replica set to 5 members.
      - The `storage.wiredTiger.engineConfig.cacheSizeGB` on the new members should be `40`.

      Changes not available in Kubernetes
      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

      If a setting is not available for a MongoDB Kubernetes
      resource, then the change must be made in the
      Ops Manager Application.

## Prerequisites

hidden: true

tabs:
  - id: ui
    name: User Interface
    content: |

      Your deployment must be running a version of the
      Automation that is compatible with Ops Manager. If
      your deployment is not running a compatible version of the
      agent, Ops Manager displays a banner prompting you to update your
      agents.

      You must have enough disk space in the parent directory to perform 
      backups before making storage engine changes on standalone processes.
      We recommend using replica sets instead of standalone processes, which 
      apply changes in a rolling fashion.

  - id: k8s
    name: Kubernetes
    content: |

      To update a MongoDB Kubernetes object, you need
      to meet the prerequisites for, and complete the procedures
      on, the
      `Install Kubernetes Operator`
      page.

## Procedure

hidden: true

tabs:
  - id: ui
    name: User Interface
    content: |

      Select the type of deployment you want to edit:

      tabs:
      - id: standalone
        name: "Standalone"
        content: |

          **Step 1: Navigate to the Deployment page for your project.**

          a. If it is not already displayed, select the organization that
             contains your desired project from the `office` Organizations menu in the
             navigation bar.

          #. If it is not already displayed, select your desired project
             from the Projects menu in the navigation bar.

          #. If it is not already displayed, click Deployment in 
             the sidebar.

          **Step 2: On the line listing the deployment item, click Modify.**

          **Step 3: Modify the Standalone Settings.**

          The Standalone Settings section contains the following
          configuration settings:

          | Setting | Description |
          |---|---|
          | Hostname | Hostname to which Ops Manager deploys the `mongod`. This hostname can be a hostname, an FQDN (fully qualified domain name), an IPv4 (Internet Protocol version 4) address, or an IPv6 (Internet Protocol version 6) address. You can only deploy to hosts under Ops Manager automation. For complete documentation on adding servers to Ops Manager automation, see /tutorial/add-servers-automation/. |
          | Port | .. include:: /includes/extracts/deploy-member-configuration-port.rst |
          | Version | .. include:: /includes/extracts/deploy-version.rst |
          | Auth Schema Version | .. include:: /includes/extracts/deploy-replica-set-auth-schema-version.rst |
          | Feature Compatibility Version | .. include:: /includes/extracts/deploy-replica-set-feature-compatibility-version.rst |
          | Log File | .. include:: /includes/extracts/deploy-log-file.rst |

          **Step 4: Modify Advanced Configuration Options.**

          The Advanced Configuration Options section allows you to
          set MongoDB runtime options for each MongoDB process
          in your deployment.

          To add an option:

          a. Click Add Option.

          #. Click Select a Startup Option and select the
             configuration option.

          #. Ops Manager displays a context-sensitive input for configuring an
             acceptable value for the selected option.

          #. Click Add to add the selected option and its
             corresponding value to the process.

          For descriptions of the available Advanced
          Configuration Options, see
          /reference/deployment-advanced-options.

          **Step 5: Click Save.**

          Ops Manager redirects you to the Deployment page, where you must
          review your changes before deploying the updated configuration.

          **Step 6: Click Review & Deploy to review your changes.**

          **Step 7: Click Confirm & Deploy to deploy your changes.**

          Otherwise, click Cancel and you can make
          additional changes.

      - id: replica-set
        name: "Replica Set"
        content: |

          **Step 1: Navigate to the Deployment page for your project.**

          a. If it is not already displayed, select the organization that
             contains your desired project from the `office` Organizations menu in the
             navigation bar.

          #. If it is not already displayed, select your desired project
             from the Projects menu in the navigation bar.

          #. If it is not already displayed, click Deployment in 
             the sidebar.

          **Step 2: On the line listing the deployment item, click Modify.**

          **Step 3: Modify Cluster-Wide Settings.**

          The Replica Set Configuration section contains the
          following cluster-wide configuration settings.

          | Setting | Description |
          |---|---|
          | Auth Schema Version | .. include:: /includes/extracts/deploy-replica-set-auth-schema-version.rst |
          | Feature Compatibility Version | .. include:: /includes/extracts/deploy-replica-set-feature-compatibility-version.rst |
          | Replica Set Settings | .. include:: /includes/extracts/deploy-replica-set-settings.rst |
          | Process Name | .. include:: /includes/extracts/deploy-process-name.rst |
          | Version | .. include:: /includes/extracts/deploy-version.rst |
          | Log File | .. include:: /includes/extracts/deploy-log-file.rst |

          **Step 4: Configure Each Replica Set Member.**

          Ops Manager lists each replica set member under the
          MongoD Settings heading of the
          Member Configuration section. Each replica set member
          has the following configurable options:

          | Setting | Description |
          |---|---|
          | Member | .. include:: /includes/extracts/deploy-member-configuration-member.rst |
          | Hostname | .. include:: /includes/extracts/deploy-member-configuration-hostname.rst |
          | Port | .. include:: /includes/extracts/deploy-member-configuration-port.rst |
          | Votes | .. include:: /includes/extracts/deploy-member-configuration-votes.rst |
          | Priority | .. include:: /includes/extracts/deploy-member-configuration-priority.rst |
          | Delay | .. include:: /includes/extracts/deploy-member-configuration-delay.rst |
          | Build Indexes | .. include:: /includes/extracts/deploy-member-configuration-build-indexes.rst |
          | Tags | .. include:: /includes/extracts/deploy-member-configuration-tags.rst |
          | Add a Mongod | .. include:: /includes/extracts/deploy-member-configuration-add-mongod.rst |

          **Step 5: Configure your Replication Settings.**

          The Replication Settings section contains the following
          configuration options for the replica set:

          | Setting | Description |
          |---|---|
          | Protocol Version | .. include:: /includes/extracts/deploy-member-replication-protocol-version.rst |
          | Chaining Allowed | .. include:: /includes/extracts/deploy-member-replication-chaining-allowed.rst |
          | Write Concern Majority Journal Default | .. include:: /includes/extracts/deploy-member-replication-write-concern-majority-journal-default.rst |
          | Heartbeat Timeout (secs) | .. include:: /includes/extracts/deploy-member-replication-heartbeat-timeouts.rst |
          | Election Timeout (ms) | .. include:: /includes/extracts/deploy-member-replication-election-timeout.rst |
          | CatchUp Timeout (ms) | .. include:: /includes/extracts/deploy-member-replication-catch-up-timeout.rst |
          | CatchUp Takeover Delay (ms) | .. include:: /includes/extracts/deploy-member-replication-catch-up-takeover-delay.rst |
          | Last Error Defaults | .. include:: /includes/extracts/deploy-member-replication-last-error-defaults.rst |
          | Force Reconfigure | .. include:: /includes/extracts/deploy-member-replication-force-reconfigure.rst |

          **Step 6: Modify Advanced Configuration Options.**

          The Advanced Configuration Options section allows you to 
          set MongoDB runtime options for each MongoDB process
          in your deployment.

          To add an option:

          a. Click Add Advanced Options.

          #. Click Select a Startup Option and select the
             configuration option.

          #. Ops Manager displays a context-sensitive input for configuring an
             acceptable value for the selected option.

          #. Click Add to add the selected option and its
             corresponding value to every process of the selected process type
             in the cluster.

          Ops Manager lists each process in the cluster grouped logically. Click
          the grey arrow to the left of the logical grouping to display
          its sub-groupings and processes. You can modify the advanced options
          for each process individually as necessary.

          For descriptions of the available Advanced Configuration 
          Options, see /reference/deployment-advanced-options.

          **Step 7: Click Save.**

          Ops Manager redirects you to the deployment page, where you must review
          your changes before deploying the updated configuration.

          **Step 8: Click Review & Deploy to review your changes.**

          **Step 9: Click Confirm & Deploy to deploy your changes.**

          Otherwise, click Cancel and you can make
          additional changes.

          Ops Manager displays the following message if you attempt to force
          reconfigure a replica set.

          (Figure: /images/force-reconfig-dialog.png)

          Before you click Confirm & Deploy, make sure that you
          understand the risks of force
          reconfiguring a replica set.

          **See also:**

          Reconfigure a Replica Set with Unavailable Members in the MongoDB Manual.

      - id: sharded-cluster
        name: "Sharded Cluster"
        content: |

          **Step 1: Navigate to the Deployment page for your project.**

          a. If it is not already displayed, select the organization that
             contains your desired project from the `office` Organizations menu in the
             navigation bar.

          #. If it is not already displayed, select your desired project
             from the Projects menu in the navigation bar.

          #. If it is not already displayed, click Deployment in 
             the sidebar.

          **Step 2: On the line listing the deployment item, click Modify.**

          **Step 3: Configure Cluster-Wide Settings.**

          The Cluster Configuration section contains the following
          cluster-wide configuration settings.

          | Setting | Description |
          |---|---|
          | Shard Name Prefix | .. include:: /includes/extracts/deploy-sharded-shard-name.rst |
          | Auth Schema Version | .. include:: /includes/extracts/deploy-replica-set-auth-schema-version.rst |
          | Feature Compatibility Version | .. include:: /includes/extracts/deploy-replica-set-feature-compatibility-version.rst |
          | Process Name | .. include:: /includes/extracts/deploy-sharded-process-name.rst |
          | Version | .. include:: /includes/extracts/deploy-sharded-version.rst |
          | Log File | .. include:: /includes/extracts/deploy-sharded-log-file.rst |

          **Step 4: Configure Each Shard in Your Cluster.**

          From the Member Configuration section, click
          Shard Settings to open the shard configuration
          options. Ops Manager lists each shard in the cluster and the `mongod`
          processes associated to that shard. Each shard process has the
          following options. You cannot modify options that are greyed out:

          | Setting | Description |
          |---|---|
          | Member | .. include:: /includes/extracts/deploy-member-configuration-member.rst |
          | Hostname | .. include:: /includes/extracts/deploy-member-configuration-hostname.rst |
          | Port | .. include:: /includes/extracts/deploy-member-configuration-port.rst |
          | Votes | .. include:: /includes/extracts/deploy-member-configuration-votes.rst |
          | Priority | .. include:: /includes/extracts/deploy-member-configuration-priority.rst |
          | Delay | .. include:: /includes/extracts/deploy-member-configuration-delay.rst |
          | Build Indexes | .. include:: /includes/extracts/deploy-member-configuration-build-indexes.rst |
          | Tags | .. include:: /includes/extracts/deploy-member-configuration-tags.rst |
          | Add a Mongod | .. include:: /includes/extracts/deploy-member-configuration-add-mongod.rst |

          To add additional shards to the cluster:

          a. Click Add a Shard.
          b. Under the Cluster Configuration section, set the
             following parameters for each `mongod` in the shard:

             - Version
             - Data Directory
             - Log File

          **Step 5: Configure Each Configuration Server in Your Cluster.**

          Ops Manager displays a different heading for your configuration server
          settings depending on the MongoDB version you selected for your
          configuration servers.

          MongoDB 3.2 or Later:
            From the Member Configuration section, click
            Config Server Replica Set Settings to open
            the CSRS configuration options. Each config server
            replica set member has the following options:

            | Setting | Description |
            |---|---|
            | Member | .. include:: /includes/extracts/deploy-member-configuration-member.rst |
            | Hostname | .. include:: /includes/extracts/deploy-member-configuration-hostname.rst |
            | Port | .. include:: /includes/extracts/deploy-member-configuration-port.rst |
            | Votes | .. include:: /includes/extracts/deploy-member-configuration-votes.rst |
            | Priority | .. include:: /includes/extracts/deploy-member-configuration-priority.rst |
            | Delay | .. include:: /includes/extracts/deploy-member-configuration-delay.rst |
            | Build Indexes | .. include:: /includes/extracts/deploy-member-configuration-build-indexes.rst |
            | Tags | .. include:: /includes/extracts/deploy-member-configuration-tags.rst |
            | Add a Mongod | .. include:: /includes/extracts/deploy-sharded-member-configuration-add-mongod.rst |

          MongoDB 3.0 or Earlier
            From the Member Configuration section, click
            Config Server Settings to open the configuration
            server options. Each configuration server has the following
            options:

            | Setting | Description |
            |---|---|
            | Hostname | .. include:: /includes/extracts/deploy-member-configuration-hostname.rst |
            | Port | .. include:: /includes/extracts/deploy-member-configuration-port.rst |

          **Step 6: Configure Each `mongos` in Your Cluster.**

          From the Member Configuration section, click
          Mongos Settings to open the `mongos`
          configuration options. Each `mongos` process has the
          following options. You cannot modify options that are greyed out:

          | Setting | Description |
          |---|---|
          | Hostname | .. include:: /includes/extracts/deploy-sharded-member-configuration-hostname.rst |
          | Port | .. include:: /includes/extracts/deploy-sharded-member-configuration-port.rst |
          | Add a Mongos | .. include:: /includes/extracts/deploy-sharded-member-configuration-add-mongos.rst |

          **Step 7: Configure Each Replica Set in your Cluster.**

          The Replication Settings section contains the following
          configuration options for each replica set in the cluster:

          | Setting | Description |
          |---|---|
          | Protocol Version | .. include:: /includes/extracts/deploy-member-replication-protocol-version.rst |
          | Chaining Allowed | .. include:: /includes/extracts/deploy-member-replication-chaining-allowed.rst |
          | Write Concern Majority Journal Default | .. include:: /includes/extracts/deploy-member-replication-write-concern-majority-journal-default.rst |
          | Heartbeat Timeout (secs) | .. include:: /includes/extracts/deploy-member-replication-heartbeat-timeouts.rst |
          | Election Timeout (ms) | .. include:: /includes/extracts/deploy-member-replication-election-timeout.rst |
          | CatchUp Timeout (ms) | .. include:: /includes/extracts/deploy-member-replication-catch-up-timeout.rst |
          | CatchUp Takeover Delay (ms) | .. include:: /includes/extracts/deploy-member-replication-catch-up-takeover-delay.rst |
          | Last Error Defaults | .. include:: /includes/extracts/deploy-member-replication-last-error-defaults.rst |
          | Force Reconfigure | .. include:: /includes/extracts/deploy-member-replication-force-reconfigure.rst |

          **Step 8: Modify Advanced Configuration Options.**

          The Advanced Configuration Options section allows you to 
          set MongoDB runtime options for each MongoDB process
          in your deployment.

          To add an option:

          a. Click Add Advanced Options.

          #. Click Select a Startup Option and select the
             configuration option.

          #. Ops Manager displays a context-sensitive input for configuring an
             acceptable value for the selected option.

          #. Click Add to add the selected option and its
             corresponding value to every process of the selected process type
             in the cluster.

          Ops Manager lists each process in the cluster grouped logically. Click
          the grey arrow to the left of the logical grouping to display
          its sub-groupings and processes. You can modify the advanced options
          for each process individually as necessary.

          For descriptions of the available Advanced Configuration 
          Options, see /reference/deployment-advanced-options.

          **Step 9: Click Save.**

          Ops Manager redirects you to the deployment page, where you must review
          your changes before deploying the updated configuration.

          **Step 10: Click Review & Deploy to review your changes.**

          **Step 11: Click Confirm & Deploy to deploy your changes.**

          Otherwise, click Cancel and you can make
          additional changes.

      - id: k8s
        name: Kubernetes
        content: |

          1. Edit the Kubernetes resource specification file.

          2. Modify or add any settings you need added or changed.

          3. Save your specification file.

          4. Invoke the following Kubernetes command to update your resource.

             ```sh
             kubectl apply -f <standalone-conf>.yaml
             ```
