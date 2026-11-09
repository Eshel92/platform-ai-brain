<!-- Converted from security.txt (reStructuredText). Includes are inlined. -->

# Security

  

MongoDB provides various features, such as authentication, access
control, encryption, to secure your MongoDB deployments. Some key
security features include:

| Authentication | Authorization | TLS/SSL | Enterprise Only | Encryption |
|---|---|---|---|---|
| /core/authentication /reference/database-users /core/security-scram /core/security-x.509 | /core/authorization /tutorial/enable-authentication /tutorial/manage-users-and-roles | /core/security-transport-encryption /tutorial/configure-ssl configure-client-tls-tutorial | /core/kerberos /core/security-ldap /core/oidc/security-oidc /core/auditing log-message-log-redaction | qe-manual-feature-qe manual-csfle-feature security-encryption-at-rest transport-encryption |

## Secure Your MongoDB Atlas Deployments

MongoDB Atlas, the fully managed service for MongoDB deployments 
in the cloud, comes preconfigured with secure default settings.
Atlas also provides the following key security features:

| Security Feature | Description |
|---|---|
| Authentication and Authorization | In Atlas, you configure database users to access your deployments. Atlas provides various ways to perform user authentication and authorization, including LDAP, OIDC, and X.509. To learn more, see Configure Authentication and Authorization. |
| Encryption | By default, Atlas encrypts all data stored in your deployments and uses TLS/SSL to encrypt the connections to your databases. To add another layer of security, you can configure Encryption at Rest using Customer Key Management. |
| IP Access List | Atlas allows connections only from addresses specified in the IP access list. To learn how to manage client connections in Atlas, see Configure IP Access List Entries. |
| Cloud Provider Support | Atlas supports network peering connections and private endpoints to secure your deployments hosted on AWS, Azure, and Google Cloud. To learn more, see Set Up a Network Peering Connection and Configure Private Endpoints. |

For a full list of security features in Atlas, see 
Security Features for Clusters.

## Report Suspected Security Bugs

If you suspect you have [identified a security bug](https://www.mongodb.com/company/contact/mongodb-vulnerability-disclosure-policy) 
on any MongoDB products, please submit the issue using our 
[Security Bug Submission Form](https://www.mongodb.com/bug-submission-form).
