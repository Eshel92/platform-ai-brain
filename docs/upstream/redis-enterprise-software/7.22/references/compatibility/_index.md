---
Title: Redis Enterprise compatibility with Redis Open Source
alwaysopen: false
categories:
- docs
- operate
- rs
- rc
description: Redis Enterprise compatibility with Redis Open Source.
hideListLinks: true
linkTitle: Redis Open Source compatibility
weight: $weight
tocEmbedHeaders: true
url: '/operate/rs/7.22/references/compatibility/'
---
Both Redis Enterprise Software and [Redis Cloud](/content/operate/rc/_index.md) are compatible with Redis Open Source. 

Redis contributes extensively to the Redis project and uses it inside of Redis Software and Redis Cloud. As a rule, we adhere to the project's specifications and update both products with the latest version of Redis.

## Redis commands

See [Compatibility with Redis commands]({{< relref "/operate/rs/references/compatibility/commands" >}}) to learn which Redis commands are compatible with Redis Software and Redis Cloud.

## Configuration settings

[Compatibility with Redis configuration settings]({{< relref "/operate/rs/references/compatibility/config-settings" >}}) lists the Redis configuration settings supported by Redis Software and Redis Cloud.

## Redis clients

You can use any standard [Redis client]({{< relref "/develop/clients" >}}) with Redis Software and Redis Cloud.

## RESP compatibility

Redis Enterprise Software and Redis Cloud support RESP2 and RESP3. See [RESP compatibility with Redis Enterprise](/content/operate/rs/7.22/references/compatibility/resp.md) for more information.

## Client-side caching compatibility

Redis Software and Redis Cloud support [client-side caching](/content/develop/clients/client-side-caching.md) for databases with Redis versions 7.4 or later. See [Client-side caching compatibility with Redis Software and Redis Cloud](/content/operate/rs/7.22/references/compatibility/client-side-caching.md) for more information about compatibility and configuration options.

## Compatibility with open source Redis Cluster API

Redis Enterprise supports [Redis OSS Cluster API](/content/operate/rs/7.22/clusters/optimize/oss-cluster-api.md) if it is enabled for a database. For more information, see [Enable OSS Cluster API](/content/operate/rs/7.22/databases/configure/oss-cluster-api.md).
