<!-- Converted from security/authentication/built-in-users.asciidoc (AsciiDoc). Includes are inlined. -->

### Built-in users

The {stack-security-features} provide built-in user credentials to help you get
up and running. These users have a fixed set of privileges and cannot be
authenticated until their passwords have been set. The `elastic` user can be
used to set all of the built-in user passwords.

**Create users with minimum privileges**
****
The built-in users serve specific purposes and are not intended for general
use. In particular, do not use the `elastic` superuser unless full access to
the cluster is absolutely required. On self-managed deployments, use the
`elastic` user to create users that have the minimum necessary roles or 
privileges for their activities.
****

**Note:**
On Elastic Cloud, [operator privileges](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/operator-privileges.html) are enabled.
These privileges restrict some infrastructure functionality, even if a role
would otherwise permit a user to complete an administrative task.

`elastic`:: A built-in superuser.
**Important:** Anyone who can log in as the `elastic` user has direct read-only
access to restricted indices, such as `.security`. This user also has the ability
to manage security and create roles with unlimited privileges.

`kibana_system`:: The user Kibana uses to connect and communicate with Elasticsearch.
`logstash_system`:: The user Logstash uses when storing monitoring information in Elasticsearch.
`beats_system`:: The user the Beats use when storing monitoring information in Elasticsearch.
`apm_system`:: The user the APM server uses when storing monitoring information in Elasticsearch.
`remote_monitoring_user`:: The user {metricbeat} uses when collecting and
storing monitoring information in Elasticsearch. It has the `remote_monitoring_agent` and
`remote_monitoring_collector` built-in roles.

#### How the built-in users work

These built-in users are stored in a special `.security` index, which is managed
by Elasticsearch. If a built-in user is disabled or its password
changes, the change is automatically reflected on each node in the cluster. If
your `.security` index is deleted or restored from a snapshot, however, any
changes you have applied are lost.

Although they share the same API, the built-in users are separate and distinct
from users managed by the native realm. Disabling the native
realm will not have any effect on the built-in users. The built-in users can
be disabled individually, using the
disable users API.

#### The Elastic bootstrap password

When you install Elasticsearch, if the `elastic` user does not already have a password,
it uses a default bootstrap password. The bootstrap password is a transient
password that enables you to run the tools that set all the built-in user passwords.

By default, the bootstrap password is derived from a randomized `keystore.seed`
setting, which is added to the keystore during installation. You do not need
to know or change this bootstrap password. If you have defined a
`bootstrap.password` setting in the keystore, however, that value is used instead.
For more information about interacting with the keystore, see
secure-settings.

**Note:** After you set passwords for the built-in users,
in particular for the `elastic` user, there is no further use for the bootstrap
password.

#### Setting built-in user passwords

You must set the passwords for all built-in users.

The elasticsearch-setup-passwords tool is the simplest method to set the
built-in users' passwords for the first time. It uses the `elastic` user's
bootstrap password to run user management API requests. For example, you can run
the command in an "interactive" mode, which prompts you to enter new passwords
for the `elastic`, `kibana_system`, `logstash_system`, `beats_system`, `apm_system`,
and `remote_monitoring_user` users:

```shell
bin/elasticsearch-setup-passwords interactive
```

For more information about the command options, see
elasticsearch-setup-passwords.

**Important:** After you set a password for the `elastic` user, the bootstrap
password is no longer valid; you cannot run the `elasticsearch-setup-passwords`
command a second time.

Alternatively, you can set the initial passwords for the built-in users by using
the *Management > Users* page in Kibana or the
change password API. These methods are
more complex. You must supply the `elastic` user and its bootstrap password to
log in to Kibana or run the API. This requirement means that you cannot use the
default bootstrap password that is derived from the `keystore.seed` setting.
Instead, you must explicitly set a `bootstrap.password` setting in the keystore
before you start Elasticsearch. For example, the following command prompts you to enter a
new bootstrap password:

```shell
bin/elasticsearch-keystore add "bootstrap.password"
```

You can then start Elasticsearch and Kibana and use the `elastic` user and bootstrap
password to log in to Kibana and change the passwords. Alternatively, you can
submit Change Password API requests for each built-in user. These methods are
better suited for changing your passwords after the initial setup is complete,
since at that point the bootstrap password is no longer required.

#### Adding built-in user passwords to Kibana

After the `kibana_system` user password is set, you need to update the Kibana server
with the new password by setting `elasticsearch.password` in the `kibana.yml`
configuration file:

```yaml
elasticsearch.password: kibanapassword
```

See [Configuring security in Kibana](https://www.elastic.co/guide/en/kibana/8.19/using-kibana-with-security.html).

#### Adding built-in user passwords to Logstash

The `logstash_system` user is used internally within Logstash when
monitoring is enabled for Logstash.

To enable this feature in Logstash, you need to update the Logstash
configuration with the new password by setting `xpack.monitoring.elasticsearch.password` in
the `logstash.yml` configuration file:

```yaml
xpack.monitoring.elasticsearch.password: logstashpassword
```

If you have upgraded from an older version of Elasticsearch, the `logstash_system` user
may have defaulted to _disabled_ for security reasons. Once the password has
been changed, you can enable the user via the following API call:

```console
PUT _security/user/logstash_system/_enable
```

See {logstash-ref}/ls-security.html#ls-monitoring-user[Configuring credentials for Logstash monitoring].

#### Adding built-in user passwords to Beats

The `beats_system` user is used internally within Beats when monitoring is
enabled for Beats.

To enable this feature in Beats, you need to update the configuration for each
of your beats to reference the correct username and password. For example:

```yaml
xpack.monitoring.elasticsearch.username: beats_system
xpack.monitoring.elasticsearch.password: beatspassword
```

For example, see {metricbeat-ref}/monitoring.html[Monitoring {metricbeat}].

The `remote_monitoring_user` is used when {metricbeat} collects and stores
monitoring data for the Elastic Stack. See monitoring-production.

If you have upgraded from an older version of Elasticsearch, then you may not have set a
password for the `beats_system` or `remote_monitoring_user` users. If this is
the case, then you should use the *Management > Users* page in Kibana or the
change password API to set a password
for these users.

#### Adding built-in user passwords to APM

The `apm_system` user is used internally within APM when monitoring is enabled.

To enable this feature in APM, you need to update the
`apm-server.yml` configuration file to
reference the correct username and password. For example:

```yaml
xpack.monitoring.elasticsearch.username: apm_system
xpack.monitoring.elasticsearch.password: apmserverpassword
```

If you have upgraded from an older version of Elasticsearch, then you may not have set a
password for the `apm_system` user. If this is the case,
then you should use the *Management > Users* page in Kibana or the
change password API to set a password
for these users.

#### Disabling default password functionality

=============================================================================
This setting is deprecated. The elastic user no longer has a default password.
The password must be set before the user can be used.
See bootstrap-elastic-passwords.
=============================================================================
