<!-- Converted from reference/api/automation-config.txt (reStructuredText). Includes are inlined. -->

# Automation Configuration Resource

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

The API provides the `automationConfig` resource to let you manage your project’s
automation configuration.
The configuration defines the various MongoDB clusters, replica sets
and standalones in the deployment and defines how each process runs.
Automation builds the deployment according to the goals specified. Each
MongoDB Agent using Automation is responsible for the MongoDB processes
that run on its host. The configuration also specifies settings for the
deployment's MongoDB Agents.

When a running MongoDB process matches its defined configuration, the
process is in "goal state". When all processes on all hosts are in goal
state, the deployment itself is in goal state.

To update the automation configuration, you must issue the request from
an IP address on your user account's
access list.

## Additional Copies of the Automation Configuration

The MongoDB Agent stores a copy of the configuration in the
`mms-cluster-config-backup.json` file. Automation stores the most
recent version of configuration *with which Automation was able to
reach goal state*. If an Agent is not able to process configuration
changes, it continues to store an older version of the configuration.

Users with global roles can view Ops Manager's
internal representation of the deployment configuration, which is
much larger than the automation configuration and includes
additional fields used only internally. *Never* use this
representation to update the automation configuration. The
representation is called the `Raw AutomationConfig` is viewable
through the Deployment page.

## Automation Configuration Parameters

The Automation Configuration contains a large amount of information
about your Ops Manager instance, agents, clusters, and security. With this
complexity, these parameters can be found as their own
reference page.

To review an example of a complete automation configuration file, see
/reference/api/automation-config/automation-config-example.

## Endpoints

The following lists the endpoints available for the automation
configuration resource.

| Method | Endpoint | Description |
|---|---|---|
| `GET` | /groups/{PROJECT-ID}/automationConfig | Retrieve the current automation configuration IMPORTANT: The automation configuration might contain sensitive information, such as passwords or key values. Use the /groups/{PROJECT-ID}/automationConfig/noSecrets endpoint to get the automation configuration with sensitive information redacted. |
| `GET` | /groups/{PROJECT-ID}/automationConfig/noSecrets | Retrieve the current automation configuration with sensitive information redacted |
| `PUT` | /groups/{PROJECT-ID}/automationConfig | Replace the current automation configuration IMPORTANT: The automation configuration might contain sensitive information, such as passwords or key values. To update the automation configuration without updating any fields that contain sensitive information, use the /groups/{PROJECT-ID}/automationConfig/noSecrets endpoint. |
| `PUT` | /groups/{PROJECT-ID}/automationConfig/noSecrets | Replace the current automation configuration without updating any fields that contain sensitive information |
| `POST` | /groups/{PROJECT-ID}/automationConfig/updateAgentVersions | Update the MongoDB Agent |
| `GET` | /groups/{PROJECT-ID}/automationConfig/backupAgentConfig | Retrieve the current backup log settings |
| `PUT` | /groups/{PROJECT-ID}/automationConfig/backupAgentConfig | Update the current backup log settings |
| `GET` | /groups/{PROJECT-ID}/automationConfig/monitoringAgentConfig | Retrieve the current monitoring log settings |
| `PUT` | /groups/{PROJECT-ID}/automationConfig/monitoringAgentConfig | Update the current monitoring log settings |
