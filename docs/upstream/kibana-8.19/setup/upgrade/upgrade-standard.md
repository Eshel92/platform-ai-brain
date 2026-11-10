<!-- Converted from setup/upgrade/upgrade-standard.asciidoc (AsciiDoc). Includes are inlined. -->

### Standard upgrade

**Note:** Kibana includes an Upgrade Assistant to help you prepare for an upgrade. To access the assistant, go to *{stack-manage-app} > Upgrade Assistant*.

===========================================
If you've saved and/or exported objects in Kibana that rely on the
Elasticsearch Query DSL, make sure to check the Elasticsearch
[breaking changes](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/breaking-changes.html) documentation and take the
necessary remediation steps as per those instructions.
===========================================

#### Upgrading multiple Kibana instances

**Note:** Kibana does not support rolling upgrades. If you're running multiple Kibana instances, all instances should be stopped before upgrading.

Different versions of Kibana running against the same Elasticsearch index, such as during a rolling upgrade, can cause data loss. This is because older instances will continue to write saved objects in a different format than the newer instances. To prevent this from happening ensure that all old Kibana instances are shutdown before starting up instances on a newer version.

#### Upgrade using a `deb` or `rpm` package

. Stop the existing Kibana process using the appropriate command for your
  system. If you have multiple Kibana instances connecting to the same Elasticsearch
  cluster ensure that all instances are stopped before proceeding to the next
  step to avoid data loss.
. Use `rpm` or `dpkg` to install the new package. All files should be placed in
  their proper locations and config files should not be overwritten.

Make sure you remove or update any configurations
that are indicated in the breaking changes documentation
otherwise Kibana will fail to start.
. Upgrade any plugins by removing the existing plugin and reinstalling the
  appropriate version using the `kibana-plugin` script. Check out the
  plugins documentation for more information.
. Start the new Kibana process using the appropriate command for your system.

#### Upgrade using a `zip` or `tar.gz` archive

. Extract the `zip` or `tar.gz` archive to a new directory to be sure that you
  don't overwrite the `config` or `data` directories. +
**Important:** If you use {monitor-features}, you must re-use the data directory when you upgrade Kibana. Otherwise, the Kibana instance is assigned a new persistent UUID
and becomes a new instance in the monitoring data.

. Copy the files from the `config` directory from your old installation to your
  new installation. Make sure you remove or update any configurations that are
  indicated in the breaking changes documentation
  otherwise Kibana will fail to start.
. Copy the files from the `data` directory from your old installation to your
  new installation.
. Install the appropriate versions of all your plugins for your new
  installation using the `kibana-plugin` script. Check out the
  plugins documentation for more information.
. Stop the old Kibana process. If you have multiple Kibana instances connecting
  to the same Elasticsearch cluster ensure that all instances are stopped before
  proceeding to the next step to avoid data loss.
. Start the new Kibana process.
