<!-- Converted from migration.txt (reStructuredText). Includes are inlined. -->

# Migrate Deployments

**Important:** Live Migration (push) Deprecated or Not Supported for Source Deployments Managed or Monitored by Ops Manager

- For source deployments running any MongoDB 6.0.+ versions, where the
  deployments are managed or monitored by Ops Manager, live migration (push)
  is not supported.
- For source deployments running any MongoDB 5.0 and earlier versions,
  where the deployments are managed or monitored by Ops Manager, live
  migration (push) is deprecated.
- For source deployments running MongoDB 6.0.+, where the deployments
  are monitored by Cloud Manager, live migration (push) is supported.
  To learn more, see Live Migrate Your MongoDB Cluster Monitored by Cloud Manager to Atlas.

## MongoDB 6.0.17+ or 7.0.13+: Live Migrate to Atlas

If both the source and the destination clusters are running MongoDB 6.0.17+
or 7.0.13+, you can migrate your data from a source cluster into a destination
MongoDB cluster in Atlas using one of the following types of
guided live migration in the MongoDB Atlas UI:

- Live migration (push). For instructions, see Live Migrate Your MongoDB Cluster Monitored by Cloud Manager to Atlas.
- Live migration (pull). For instructions, see Live Migrate (Pull) a MongoDB Cluster into Atlas.

The choice between push and pull live migrations depends on whether the
network for your deployment allows flexibility in ingress rules and allows
access through the firewall.

In addition, you can use these migration methods for MongoDB 6.0.17+ or 7.0.13+
deployments:

- If your data is in a MongoDB deployment and you don't have access to the oplog,
  You can use `mongorestore` to run a self-managed migration.
  To learn more, see Seed with mongorestore.

## Earlier MongoDB Versions: Live Migrate to Atlas

If you are migrating MongoDB versions earlier than 6.0.17, use one of the
following migration methods, depending on your deployment's requirements
and configuration.

| Deployment Configuration | Migration Strategy |
|---|---|
| Your data is in a cluster running MongoDB earlier than 6.0.17, is managed or monitored by Ops Manager and your network allows flexibility in ingress rules. | Pull data into Atlas from Ops Manager. In this type of live migration, MongoDB Atlas requires access to the source deployment in Ops Manager through the deployment's firewall. |
| Your data is in a cluster running MongoDB earlier than 6.0.17, your cluster is managed or monitored by Ops Manager, and your network doesn't allow flexibility in ingress rules. | Push your data into Atlas from Ops Manager. In this type of live migration, Atlas receives data from Ops Manager without requiring access through the firewall. |
| Your data is in a MongoDB Community cluster running MongoDB earlier than 6.0.17, and your network doesn't allow flexibility in ingress rules. | Push your MongoDB Community data into Atlas after adding your Community deployment to Cloud Manager for monitoring. In this type of live migration, Atlas receives data from Ops Manager without requiring access through the firewall. |
| Your data is in a MongoDB deployment and you don't have access to the oplog. | Use `mongorestore` to run a self-managed migration. To learn more, see Seed with mongorestore. |

You can also migrate a MongoDB deployment from one Ops Manager project to
another project. To learn more, see Migrate a MongoDB Deployment to a New Project.
