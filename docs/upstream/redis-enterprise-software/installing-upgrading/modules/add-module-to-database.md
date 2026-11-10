---
Title: Enable a module for a database
aliases:
- /operate/oss_and_stack/stack-with-enterprise/install/add-module-to-database/
alwaysopen: false
categories:
- docs
- operate
- rs
description: null
linkTitle: Enable for a database
toc: 'true'
weight: 30
---

Modules add additional functionality to Redis databases for specific use cases. You can enable modules when you create a database.

## Automatically enabled capabilities in Redis 8

Databases created with or upgraded to Redis version 8 or later automatically enable the capabilities (modules) bundled with Redis Software as follows:

| Database type | Automatically enabled capabilities |
|---------------|------------------------------------|
| RAM-only | [Redis Search]({{<relref "/operate/oss_and_stack/stack-with-enterprise/search">}})<br />[JSON]({{<relref "/operate/oss_and_stack/stack-with-enterprise/json">}})<br />[Time series]({{<relref "/operate/oss_and_stack/stack-with-enterprise/timeseries">}})<br />[Probabilistic]({{<relref "/operate/oss_and_stack/stack-with-enterprise/bloom">}})  |
| Flash-enabled ([Redis Flex]({{<relref "/operate/rs/databases/flash">}})) | [JSON]({{<relref "/operate/oss_and_stack/stack-with-enterprise/json">}})<br />[Probabilistic]({{<relref "/operate/oss_and_stack/stack-with-enterprise/bloom">}}) |
| [Active-Active]({{<relref "/operate/rs/databases/active-active">}})<sup>[1](#enabled-modules-table-note-1)</sup> | [Redis Search]({{<relref "/operate/oss_and_stack/stack-with-enterprise/search/search-active-active">}})<br />[JSON]({{<relref "/operate/oss_and_stack/stack-with-enterprise/json">}}) |

1. <a name="enabled-modules-table-note-1"></a>Upgrading existing Active-Active databases to Redis version 8 does not automatically enable these capabilities. Only new Active-Active databases created with Redis version 8 enable these capabilities by default.

## Create a database with a module

You can only add modules to a database when you first create it. You cannot add modules to an existing database.

### Prerequisites

- [Installed the module on the cluster](/content/operate/rs/installing-upgrading/modules/add-module-to-cluster.md)
- [Upgraded the module](/content/operate/rs/installing-upgrading/modules/upgrade-module.md) to the latest version

### Create a database and enable capabilities

In the Redis Software Cluster Manager UI, follow these steps to add modules to a database:

1. From the **Databases** screen, select **Quick database** or **Create database**.

1. In the **Capabilities** section, select one or more capabilities:

    ![Select which capabilities to add to your database.](/images/rs/screenshots/databases/quick-db-capabilities-7-8-2.png)

    > [!NOTE]
    > You cannot use RediSearch 1.x and RediSearch 2.x in the same database.
    >     

1. To use custom configuration for capabilities:

    1. Select **Parameters**.
    
    1. Enter the [configuration options](#module-configuration-options).
    
    1. Select **Done**.

1. Configure additional database settings.

    > [!NOTE]
    > Depending on the [features supported by an enabled module](/content/operate/oss_and_stack/stack-with-enterprise/enterprise-capabilities.md#module-feature-support), certain database configuration fields may not be available.
    >     

1. Select **Create**.

## Module configuration options

- [Redis Search configuration options](/content/operate/oss_and_stack/stack-with-enterprise/search/config.md)

- [RedisTimeSeries configuration options](/content/operate/oss_and_stack/stack-with-enterprise/timeseries/config.md)

- [RedisBloom configuration options](/content/operate/oss_and_stack/stack-with-enterprise/bloom/config.md)