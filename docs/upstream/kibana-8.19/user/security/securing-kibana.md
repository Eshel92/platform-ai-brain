<!-- Converted from user/security/securing-kibana.asciidoc (AsciiDoc). Includes are inlined. -->

## Configure security in Kibana

When you start Elasticsearch for the first time, {stack-security-features} are enabled on
your cluster and TLS is configured automatically. The security configuration
process generates a password for the `elastic` user and an enrollment token for
Kibana.
[Start the Elastic Stack with security enabled](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/configuring-stack-security.html)
and then enroll Kibana as part of the configuration process.

You can then log in to Kibana as the `elastic` user to create additional roles
and users.

**Note:** When a user is not authorized to view data in an index (such as an Elasticsearch
index), the entire index will be inaccessible and not display in Kibana.

### Configure security settings

Set an encryption key so that sessions are not invalidated. You can optionally
configure additional security settings and authentication.

. Set the `xpack.security.encryptionKey` property in the `kibana.yml`
configuration file. You can use any text string that is 32 characters or longer
as the encryption key. Refer to `xpack.security.encryptionKey`.
```yaml
xpack.security.encryptionKey: "something_at_least_32_characters"
```

Kibana's reporting and saved objects features also have encryption key settings.
Refer to `xpack.reporting.encryptionKey` and
`xpack.encryptedSavedObjects.encryptionKey`
respectively.

. Optional: Configure Kibana's session expiration settings.

. Optional: Configure Kibana to authenticate to Elasticsearch with a client certificate.

. Restart Kibana.

### Create roles and users

Configure roles for your Kibana users to control what data those users can
access.

. Temporarily log in to Kibana using the built-in `elastic` superuser so you can
create new users and assign roles. If you are running Kibana locally, go to
`https://localhost:5601` to view the login page.
**Note:** The password for the built-in `elastic` user is generated as part of the
security configuration process on Elasticsearch. If you need to reset the password for
the `elastic` user or other built-in users, run the
[`elasticsearch-reset-password`](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/reset-password.html) tool.

. [[kibana-roles]]Create roles and users to grant access to Kibana.
To manage privileges in Kibana, go to the *Roles* management page using the navigation menu or the 
global search field. The built-in `kibana_admin` role will grant
access to Kibana with administrator privileges. Alternatively, you can create additional roles that grant limited access to Kibana.

If you're using the default native realm with Basic Authentication, go to the *Users* management page using the navigation menu or the 
global search field to create
users and assign roles, or use the Elasticsearch [user management APIs](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/security-api.html#security-user-apis). For example, the following creates
a user named `jacknich` and assigns it the `kibana_admin` role:

```js
POST /_security/user/jacknich
{
  "password" : "t0pS3cr3t",
  "roles" : [ "kibana_admin" ]
}
```

**Tip:** For more information on Basic Authentication and additional methods of authenticating Kibana users, see kibana-authentication.

. Grant users access to the indices that they will be working with in Kibana.
**Tip:** You can define as many different roles for your Kibana users as you need.

For example, create roles that have `read` and `view_index_metadata` privileges
on specific data views. For more information, see
[User authorization](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/authorization.html).

. Log out of Kibana and verify that you can log in as a normal user. If you are running Kibana locally, go to `https://localhost:5601` and
enter the credentials for a user you've assigned a Kibana user role. For example, you could log in as the user `jacknich`.
**Note:** This must be a user who has been assigned Kibana privileges. Kibana server credentials (the built-in
`kibana_system` user) should only be used internally by the Kibana server.

(See `user/security/authentication/index.md`)
(See `user/security/securing-communications/elasticsearch-mutual-tls.md`)
(See `user/security/audit-logging.md`)
(See `user/security/access-agreement.md`)
(See `user/security/session-management.md`)
(See `user/security/secure-saved-objects.md`)
