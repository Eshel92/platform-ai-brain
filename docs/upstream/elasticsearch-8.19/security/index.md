<!-- Converted from security/index.asciidoc (AsciiDoc). Includes are inlined. -->

# Secure the Elastic Stack

The Elastic Stack is comprised of many moving parts. There are the Elasticsearch
nodes that form the cluster, plus Logstash instances, Kibana instances, Beats
agents, and clients all communicating with the cluster. To keep your cluster
safe, adhere to the Elasticsearch security principles.

The first principle is to run Elasticsearch with security enabled. Configuring security
can be complicated, so we made it easy to
start the Elastic Stack with security enabled and configured.
For any new clusters, just start Elasticsearch to automatically enable password protection, 
secure internode communication with Transport Layer Security (TLS), and encrypt
connections between Elasticsearch and Kibana.

If you have an existing, unsecured cluster (or prefer to manage security on your
own), you can
manually enable and configure security to secure
Elasticsearch clusters and any clients that communicate with your clusters. You can also
implement additional security measures, such as role-based access control, IP
filtering, and auditing.

Enabling security protects Elasticsearch clusters by:

* Preventing unauthorized access
  with password protection, role-based access control, and IP filtering.
* Preserving the integrity of your data
  with SSL/TLS encryption.
* Maintaining an audit trail
  so you know who's doing what to your cluster and the data it stores.

**Tip:** If you plan to run Elasticsearch in a Federal Information Processing Standard (FIPS)
140-2 enabled JVM, see fips-140-compliance.

## Preventing unauthorized access

To prevent unauthorized access to your Elasticsearch cluster, you need a way to
_authenticate_ users in order to validate that a user is who they claim to be. For
example, making sure that only the person named _Kelsey Andorra_ can sign
in as the user `kandorra`. The {es-security-features} provide a standalone
authentication mechanism that enables you to quickly password-protect your
cluster.

If you're already using LDAP, Active Directory, or PKI to manage users in your
organization, the security features integrate with those systems to perform
user authentication.

In many cases, authenticating users isn't enough. You also need a way to
control what data users can access and what tasks they can perform. By enabling
the {es-security-features}, you can _authorize_ users by assigning access
privileges to roles and assigning those roles to users. Using this role-based
access control mechanism (RBAC), you can limit the user `kandorra` to only
perform read operations on the `events` index restrict access to all other
indices.

The security features also enable you to restrict the nodes and clients that
can connect to the cluster based on IP filters. You can
block and allow specific IP addresses, subnets, or DNS domains to
control network-level access to a cluster.

See User authentication and
User authorization.

## Preserving data integrity and confidentiality

A critical part of security is keeping confidential data secured.
Elasticsearch has built-in protections against accidental data loss and
corruption. However, there's nothing to stop deliberate tampering or data
interception. The {stack-security-features} use TLS to preserve the _integrity_
of your data against tampering, while also providing _confidentiality_ by
encrypting communications to, from, and within the cluster. For even	greater
protection, you can increase the encryption strength.

See Configure security for the Elastic Stack.

## Maintaining an audit trail

Keeping a system secure takes vigilance. By using {stack-security-features} to
maintain an audit trail, you can easily see who is accessing your cluster and
what they're doing. You can configure the audit level, which accounts for the
type of events that are logged. These events include failed authentication
attempts, user access denied, node connection denied, and more. By analyzing
access patterns and failed attempts to access your cluster, you can gain
insights into attempted attacks and data breaches. Keeping an auditable log of
the activity in your cluster can also help diagnose operational issues.

See Enable audit logging.

(See `security/es-security-principles.md`)
(See `security/configuring-stack-security.md`)
(See `security/security-manual-configuration.md`)
(See `security/securing-communications/update-tls-certificates.md`)
(See `security/authentication/overview.md`)
(See `security/authorization/overview.md`)
(See `security/auditing/enable-audit-logging.md`)
(See `security/auditing/event-types.md`)
(See `security/auditing/output-logfile.md`)
(See `security/auditing/ignore-policy.md`)
(See `security/auditing/auditing-search-queries.md`)
(See `security/using-ip-filtering.md`)
(See `security/ccs-clients-integrations/index.md`)
(See `security/operator-privileges/index.md`)
(See `security/troubleshooting.md`)
(See `security/limitations.md`)
