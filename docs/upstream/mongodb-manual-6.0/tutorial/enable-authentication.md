<!-- Converted from tutorial/enable-authentication.txt (reStructuredText). Includes are inlined. -->

# Enable Access Control on Self-Managed Deployments

Enabling access control on a MongoDB deployment enforces authentication.
With access control enabled, users are required to identify themselves
and can only perform actions that adhere to the permissions granted by
the roles assigned to their user.

You can configure authentication in the UI for deployments hosted in [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server).

**Note:**

You can't disable access control in MongoDB Atlas.

## Access Control Resources

If you would like to enable access control for a standalone MongoDB
instance, please refer to one of the following resources:

- /tutorial/configure-scram-client-authentication
- /tutorial/configure-x509-client-authentication
- /tutorial/control-access-to-mongodb-with-kerberos-authentication
- /tutorial/control-access-to-mongodb-windows-with-kerberos-authentication
- /tutorial/kerberos-auth-activedirectory-authz
- /tutorial/configure-ldap-sasl-activedirectory
- /tutorial/configure-ldap-sasl-openldap
- /tutorial/authenticate-nativeldap-activedirectory

If you would like to enable access control for a replica set or a sharded cluster, please refer to
one of the following resources:

- /tutorial/deploy-replica-set-with-keyfile-access-control
- /tutorial/enforce-keyfile-access-control-in-existing-replica-set
- /tutorial/enforce-keyfile-access-control-in-existing-replica-set-without-downtime
- /tutorial/deploy-sharded-cluster-with-keyfile-access-control
- /tutorial/enforce-keyfile-access-control-in-existing-sharded-cluster
- /tutorial/enforce-keyfile-access-control-in-existing-sharded-cluster-no-downtime
- /tutorial/control-access-to-mongodb-with-kerberos-authentication
- /tutorial/control-access-to-mongodb-windows-with-kerberos-authentication
- /tutorial/kerberos-auth-activedirectory-authz
- /tutorial/configure-ldap-sasl-activedirectory
- /tutorial/configure-ldap-sasl-openldap
- /tutorial/authenticate-nativeldap-activedirectory

## Next Steps

To create additional users, see /tutorial/create-users.

To manage users, assign roles, and create custom roles, see
/tutorial/manage-users-and-roles.
