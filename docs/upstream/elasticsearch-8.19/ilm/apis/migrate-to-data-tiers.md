<!-- Converted from ilm/apis/migrate-to-data-tiers.asciidoc (AsciiDoc). Includes are inlined. -->

### Migrate to data tiers routing API

**New API reference**
For the most up-to-date API details, refer to [Index lifecycle management APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ilm).

Switches the indices, ILM policies, and legacy, composable and component templates from using custom node attributes and
attribute-based allocation filters to using data tiers, and
optionally deletes one legacy index template.
Using node roles enables ILM to automatically move the indices between
data tiers.

Migrating away from custom node attributes routing can be manually performed
as indicated in the <<migrate-index-allocation-filters, Migrate index allocation
filters to node roles>> page.

This API provides an automated way of executing three out of the four manual steps listed
in the migration guide:

. Stop setting the custom hot attribute on new indices
. Remove custom allocation settings from existing ILM policies
. Replace custom allocation settings from existing indices with the corresponding tier preference

#### Request

`POST /_ilm/migrate_to_data_tiers`

The API accepts an optional body that allows you to specify:

- The legacy index template name to delete. Defaults to none.
- The name of the custom node attribute used for the indices and ILM policies allocation filtering.
Defaults to `data`.

#### Prerequisites

* ILM must be stopped before performing the migration. Use the stop ILM API
to stop ILM and get status API to wait until the
reported operation mode is `STOPPED`.

#### Query parameters

`dry_run`::
(Optional, Boolean)
If `true`, simulates the migration from node attributes based allocation filters to data tiers, but does
not perform the migration. This provides a way to retrieve the indices and ILM policies that need to be
migrated.
Defaults to `false`.

**Note:** When simulating a migration (ie. `dry_run` is `true`) ILM doesn't need to be stopped.

#### Examples

The following example migrates the indices, ILM policies, legacy templates,
composable, and component templates away from defining custom allocation filtering
using the `custom_attribute_name` node attribute, and deletes the legacy template
with name `global-template` if it exists in the system.

```console
POST /_ilm/migrate_to_data_tiers
{
  "legacy_template_to_delete": "global-template",
  "node_attribute": "custom_attribute_name"
}
```

If the request succeeds, a response like the following will be received:

```console-result
{
  "dry_run": false,
  "removed_legacy_template":"global-template", <1>
  "migrated_ilm_policies":["policy_with_allocate_action"], <2>
  "migrated_indices":["warm-index-to-migrate-000001"], <3>
  "migrated_legacy_templates":["a-legacy-template"], <4>
  "migrated_composable_templates":["a-composable-template"], <5>
  "migrated_component_templates":["a-component-template"] <6>
}
```

<1> Shows the name of the legacy index template that was deleted. This will be missing
if no legacy index template was deleted.
<2> The ILM policies that were updated.
<3> The indices that were migrated to tier preference routing.
<4> The legacy index templates that were updated to not contain custom routing settings for the
provided data attribute.
<5> The composable index templates that were updated to not contain custom routing settings for the
provided data attribute.
<6> The component templates that were updated to not contain custom routing settings for the
provided data attribute.
