<!-- Converted from tutorial/nav/security.txt (reStructuredText). Includes are inlined. -->

# Security

Security Options & Support Matrices
  Describes Ops Manager security features.

Configure Firewall to Access Ops Manager
  Describes the ports that Ops Manager components use.

/tutorial/manage-ports
  Describes how to change the default ports used by Ops Manager.

Secure Connections to Ops Manager
  Describes how to run Ops Manager over HTTPS (Hypertext Transfer Protocol Secure) and require users to
  have a valid certificate to connect to the Ops Manager console.

/tutorial/encrypt-user-credentials
  Describes how to encrypt user credentials to the application
  database and snapshot stores.

Secure Connections to Application Database
  Configure the connections to the MongoDB processes that host the
  application database.

Secure Connections to MongoDB Deployments
  Enable TLS for connections to your MongoDB deployments.

Configure LDAP for Ops Manager Users
  Configure Ops Manager to use LDAP to store user data and permissions.

Configure SAML for Ops Manager Users
  Configure Ops Manager to use SAML (Security Assertion Markup Language) to use an identity provider.

Secure MongoDB Deployments with Authentication
  Configure the Authentication Mechanisms used by your Ops Manager project
  for communication between the Ops Manager agents and your deployments.

Enable System-wide Two-Factor Authentication
  Configure two-factor authentication.

Encrypt Snapshots
  Configure Ops Manager to encrypt snapshots when stored in persistent
  storage.

/tutorial/rotate-master-kmip-keys
  Rotate master encryption keys.

/tutorial/configure-auditing
  Configure Ops Manager to audit various events on `mongod` and `mongos` instances.
