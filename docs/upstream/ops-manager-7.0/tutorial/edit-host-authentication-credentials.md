<!-- Converted from tutorial/edit-host-authentication-credentials.txt (reStructuredText). Includes are inlined. -->

# Configure MongoDB Authentication and Authorization

Your MongoDB deployments can use the access control mechanisms described
on this page. You specify the authentication settings when
adding the deployment.
You can edit the security settings after adding a deployment.

If a deployment uses access control, the MongoDB Agent must
authenticate to the deployment as MongoDB users with appropriate access.
Enable and configure authentication through the Ops Manager Application.

## Considerations

With access control enabled, you must
create MongoDB users so that
clients can access your databases.

Ops Manager automatically creates a user for the MongoDB Agent when you enable access
control. The MongoDB Agent can administrate and manage other users. 
As such, the first user you create can have any role.

When you select an Authentication Mechanism for your Ops Manager group, this
enables access control for all the deployments in your Ops Manager group.

**Note:** Recommendation

To avoid inconsistencies, use the Ops Manager interface to manage users
and roles for MongoDB deployments.

**See also:**

To learn more about MongoDB access control, see the
Authentication and
Authorization pages in the MongoDB
manual.

## Access Control Mechanisms

### `SCRAM-SHA-1` and `SCRAM-SHA-256`

MongoDB supports the following implementations of challenge-response
mechanisms for authenticating users with passwords.

In the following table, the default authentication mechanism for the
release series is marked with check-square and acceptable
authentication mechanisms are marked with check-circle.

| MongoDB Release Series | :v3.6:`MONGODB-CR </core/security-mongodb-cr>` | SCRAM-SHA-1 | SCRAM-SHA-256 |
|---|---|---|---|
| 5.x.x |  | check-circle | check-square |
| 4.4.x |  | check-circle | check-square |
| 4.2.x |  | check-circle | check-square |
| 4.0.x |  | check-circle | check-square |
| 3.6.x | check-circle | check-square |  |
| 3.4.x | check-circle | check-square |  |

To enable `SCRAM-SHA-1` or `SCRAM-SHA-256` for your Ops Manager project, 
complete the following tasks:

1. /tutorial/enable-mongodbcr-authentication-for-group.
2. /tutorial/configure-mongodb-agent-for-scram.

### LDAP (Lightweight Directory Access Protocol)

`MongoDB Enterprise` supports proxy
authentication of users. This allows administrators to configure a
MongoDB cluster to authenticate users by proxying authentication
requests to a specified LDAP (Lightweight Directory Access Protocol) service.

To enable LDAP (Lightweight Directory Access Protocol) for your Ops Manager project, complete the following tasks:

1. /tutorial/enable-ldap-authentication-for-group.
2. /tutorial/configure-mongodb-agent-for-ldap.

### Kerberos

`MongoDB Enterprise` supports
authentication using a Kerberos service. Kerberos is an IETF (Internet Engineering Task Force)
(RFC 4120) standard authentication protocol for large
client/server systems.

To use MongoDB with Kerberos, you must have a properly configured
Kerberos deployment, configure *Kerberos service principals* for
MongoDB, and add the *Kerberos user principal*.

To enable Kerberos for your Ops Manager project, complete the following tasks:

1. /tutorial/enable-kerberos-authentication-for-group
2. /tutorial/configure-mongodb-agent-for-kerberos.

Specify Kerberos as the MongoDB process's authentication mechanism when
adding or
editing the deployment.

### X.509

MongoDB supports X.509 certificate authentication for use with a secure
TLS connection. The
X.509 client authentication allows clients to authenticate to servers
with certificates rather than with a username and password.

To enable X.509 authentication for your Ops Manager project, complete the
following tasks:

1. /tutorial/enable-x509-authentication-for-group.
2. /tutorial/configure-mongodb-agent-for-x509.

You can also use X.509 certificates for membership authentication
for the processes that Ops Manager monitors.

## Edit Host Credentials

You can configure the deployment to use the authentication mechanism
from the Ops Manager interface. The
/tutorial/nav/access-control-mongodb tutorials describe how to
configure an existing deployment to use each authentication mechanism.
