<!-- Converted from settings/audit-settings.asciidoc (AsciiDoc). Includes are inlined. -->

### Auditing security settings

You can use audit logging to record security-related
events, such as authentication failures, refused connections, and data-access
events. In addition, changes via the APIs to the security configuration, such
as creating, updating and removing native and
built-in users, roles,
role mappings and
API keys are also recorded.
**Tip:** Audit logs are only available on certain subscription levels.
For more information, see {subscriptions}.

If configured, auditing settings must be set on every node in the cluster.
Static settings, such as `xpack.security.audit.enabled`, must be configured in
`elasticsearch.yml` on each node. For dynamic auditing settings, use the
cluster update settings API to ensure the setting is
the same on all nodes.

#### General Auditing Settings

`xpack.security.audit.enabled`::
(Static)
Set to `true` to enable auditing on the node. The default value is `false`. This
puts the auditing events in a dedicated file named `<clustername>_audit.json` on
each node.
If enabled, this setting must be configured in `elasticsearch.yml` on all nodes
in the cluster.

#### Audited Event Settings

The events and some other information about what gets logged can be controlled
by using the following settings:

`xpack.security.audit.logfile.events.include`::
(Dynamic)
Specifies the kind of events to print in the auditing output.
In addition, `_all` can be used to exhaustively audit all the events, but this is usually
discouraged since it will get very verbose.
The default list value contains:
`access_denied, access_granted, anonymous_access_denied, authentication_failed,
connection_denied, tampered_request, run_as_denied, run_as_granted,
security_config_change`.

`xpack.security.audit.logfile.events.exclude`::
(Dynamic)
Excludes the specified kind of events from the include list.
This is useful in the case where the `events.include` setting contains the special value `_all`.
The default is the empty list.

`xpack.security.audit.logfile.events.emit_request_body`::
(Dynamic)
Specifies whether to include the full request body from REST requests as an
attribute of certain kinds of audit events. This setting can be used to
audit search queries.
The default value is `false`, so request bodies are not printed.
**Important:** Be advised that sensitive data may be audited in plain text when including
the request body in audit events, even though all the security APIs, such as those that
change the user's password, have the credentials filtered out when audited.

#### Local Node Info Settings

`xpack.security.audit.logfile.emit_node_name`::
(Dynamic)
Specifies whether to include the node name as a field in
each audit event. The default value is `false`.

`xpack.security.audit.logfile.emit_node_host_address`::
(Dynamic)
Specifies whether to include the node's IP address as a field in each audit event.
The default value is `false`.

`xpack.security.audit.logfile.emit_node_host_name`::
(Dynamic)
Specifies whether to include the node's host name as a field in each audit event.
The default value is `false`.

`xpack.security.audit.logfile.emit_node_id`::
(Dynamic)
Specifies whether to include the node id as a field in each audit event.
Unlike node name, whose value might change if the administrator
changes the setting in the config file, the node id will persist across cluster
restarts and the administrator cannot change it.
The default value is `true`.

#### Audit Logfile Event Ignore Policies

The following settings affect the ignore policies
that enable fine-grained control over which audit events are printed to the log file.
All of the settings with the same policy name combine to form a single policy.
If an event matches all the conditions of any policy, it is ignored and not printed.
Most audit events are subject to the ignore policies. The sole exception are
events of the `security_config_change` type, which cannot be filtered out, unless
excluded altogether.

`xpack.security.audit.logfile.events.ignore_filters.<policy_name>.users`::
(Dynamic)
A list of user names or wildcards. The specified policy will
not print audit events for users matching these values.

`xpack.security.audit.logfile.events.ignore_filters.<policy_name>.realms`::
(Dynamic)
A list of authentication realm names or wildcards. The specified policy will
not print audit events for users in these realms.

`xpack.security.audit.logfile.events.ignore_filters.<policy_name>.actions`::
(Dynamic)
A list of action names or wildcards. Action name can be found in the `action`
field of the audit event. The specified policy will not print audit events
for actions matching these values.

`xpack.security.audit.logfile.events.ignore_filters.<policy_name>.roles`::
(Dynamic)
A list of role names or wildcards. The specified policy will
not print audit events for users that have these roles. If the user has several
roles, some of which are *not* covered by the policy, the policy will
*not* cover this event.

`xpack.security.audit.logfile.events.ignore_filters.<policy_name>.indices`::
(Dynamic)
A list of index names or wildcards. The specified policy will
not print audit events when all the indices in the event match
these values. If the event concerns several indices, some of which are
*not* covered by the policy, the policy will *not* cover this event.
