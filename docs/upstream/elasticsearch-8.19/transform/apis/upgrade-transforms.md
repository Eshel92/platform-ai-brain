<!-- Converted from transform/apis/upgrade-transforms.asciidoc (AsciiDoc). Includes are inlined. -->

# Upgrade transforms API

**New API reference**
For the most up-to-date API details, refer to [Transform APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-transform).

Upgrades all transforms.

## Request

`POST _transform/_upgrade`

## Prerequisites

Requires the following privileges:

* cluster: `manage_transform` (the `transform_admin` built-in role grants this
  privilege)

## Description

Transforms are compatible across minor versions and between supported
major versions. However, over time, the format of transform configuration
information may change. This API identifies transforms which have a legacy
configuration format and upgrades them to the latest version; including clean up
of the internal data structures that store transform state and checkpoints.
Transform upgrade does not affect the source and destination indices.

**Note:** From Elasticsearch 8.10.0,  a new version number is used to
track the configuration and state changes in the transform plugin. This new
version number is decoupled from the product version and will increment
independently.

If a transform upgrade step fails, the upgrade stops, and an error is returned
about the underlying issue. Resolve the issue then re-run the process again. A
summary is returned when the upgrade is finished.

To ensure {ctransforms} remain running during a major version upgrade of the
cluster – for example, from 7.16 to 8.0 – it is recommended to upgrade
transforms before upgrading the cluster. You may want to perform a recent
cluster backup prior to the upgrade.

**Important:**

* When Elasticsearch security features are enabled, your transform remembers the
roles of the user who created or updated it last. In contrast to
update transform, a transform upgrade does not change the
stored roles, therefore the role used to read source data and write to the
destination index remains unchanged.

## Query parameters

`dry_run`::
(Optional, Boolean) When `true`, only checks for updates but does not execute
them. Defaults to `false`.

`timeout`::
(Optional, time)
Period to wait for a response. If no response is received before the timeout
expires, the request fails and returns an error. Defaults to `30s`.

## Response body

`needs_update`::
  (integer) The number of transforms that need to be upgraded.

`no_action`::
  (integer) The number of transforms that don't require upgrading.

`updated`::
  (integer) The number of transforms that have been upgraded.

## Examples

To upgrade the legacy transforms to the latest configuration format, perform
the following API call:

```console
POST _transform/_upgrade
```

When all transforms are upgraded, you receive a summary:

```console-result
{
  "needs_update": 0,
  "updated": 2,
  "no_action": 1
}
```
