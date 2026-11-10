<!-- Converted from transform/setup.asciidoc (AsciiDoc). Includes are inlined. -->

# Set up transforms

## Requirements overview

To use transforms, you must have:

* at least one transform node,
* management features visible in the Kibana space, and
* security privileges that:
* grant use of transforms, and
* grant access to source and destination indices

## Security privileges

Assigning security privileges affects how users access transforms. Consider
the two main categories:

* *transform-es-security-privileges*: uses an Elasticsearch client, cURL, or Kibana
**{dev-tools-app}** to access transforms via Elasticsearch APIs. This scenario requires
Elasticsearch security privileges.
* *transform-kib-security-privileges*: uses transforms in Kibana. This
scenario requires Kibana feature privileges _and_ Elasticsearch security privileges.

### Elasticsearch API user

To _manage_ transforms, you must meet all of the following requirements:

* `transform_admin` built-in role or `manage_transform` cluster privileges,
* `read` and `view_index_metadata` index privileges on source indices, and
* `create_index`, `index`, `manage`, and `read` index privileges on destination
indices. If a `retention_policy` is configured, `delete` index privilege is
also required on the destination index.

To view only the configuration and status of transforms, you must have:

* `transform_user` built-in role or `monitor_transform` cluster privileges

For more information about Elasticsearch roles and privileges, refer to
built-in-roles and security-privileges.

### Kibana user

Within a Kibana space, for full access to transforms, you must meet all of the
following requirements:

*  Management features visible in the Kibana space, including
`Data View Management` and `Stack Monitoring`,
* `monitoring_user` built-in role,
* `transform_admin` built-in role or `manage_transform` cluster privileges,
* `kibana_admin` built-in role or a custom role with `read` or `all` Kibana
privileges for the `Data View Management` feature (dependent on whether data
views already exist for your destination indices),
* data views for your source indices,
* `read` and `view_index_metadata` index privileges on source indices, and
* `create_index`, `index`, `manage`, and `read` index privileges on destination
indices. Additionally, when using a `retention_policy`, `delete` index privilege is required
on destination indices.
* `read_pipeline` cluster privileges, if the transform uses an ingest pipeline

Within a Kibana space, for read-only access to transforms, you must meet all of
the following requirements:

* Management features visible in the Kibana space, including `Stack Monitoring`,
* `monitoring_user` built-in role,
* `transform_user` built-in role or `monitor_transform` cluster privileges,
* `kibana_admin` built-in role or a custom role with `read` Kibana privileges
for at least one feature in the space,
* data views for your source and destination indices, and
* `read`, and `view_index_metadata` index privileges on source indices and
destination indices

For more information and Kibana security features, see
[Kibana role management](https://www.elastic.co/guide/en/kibana/8.19/kibana-role-management.html) and
[Kibana privileges](https://www.elastic.co/guide/en/kibana/8.19/kibana-privileges.html).

## Kibana spaces

[Spaces](https://www.elastic.co/guide/en/kibana/8.19/xpack-spaces.html) enable you to organize your source and
destination indices and other saved objects in Kibana and to see only the objects
that belong to your space. However, a transform is a long running task which 
is managed on cluster level and therefore not limited in scope to certain 
spaces. Space awareness can be implemented for a {data-source} under 
**Stack Management > Kibana** which allows privileges to the transform 
destination index.

To successfully create transforms in Kibana, you must be logged into a space
where the source indices are visible and the `Data View Management` and
`Stack Monitoring` features are visible.
