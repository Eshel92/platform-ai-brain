<!-- Converted from reference/cluster-configuration-process-options.txt (reStructuredText). Includes are inlined. -->

# MongoDB Settings and Automation Support

The `processes.<args>` object in an
automation configuration file
specifies the configuration options for each MongoDB instance. The
supported settings depend on the version of MongoDB.

The `processes.args2_6` object accepts most MongoDB settings and parameters for MongoDB versions 2.6 and later. Format this object using YAML (Yet Another Markup Language). To review examples of the MongoDB configuration YAML (Yet Another Markup Language),
see the Configuration File Options
in the MongoDB manual.

**Warning:**

Ops Manager automation doesn't support or validate the following settings. Using them
could cause deployment failure or downtime.

- net.unixDomainSocket options such as
  `net.unixDomainSocket.enabled`, `net.unixDomainSocket.pathPrefix`,
  and `net.unixDomainSocket.filePermissions`.

- Ops Manager automation rejects deployments that contain internal settings such as
  `__exec` and `__rest`.

If you require these settings, you must manage the deployment manually without Ops Manager.

**Important:**

Specific security-related settings, such as LDAP settings, TLS 
settings related to the Certificate Authority, and Authentication 
settings, are managed at the project level and may be overridden 
upon import into Automation.
