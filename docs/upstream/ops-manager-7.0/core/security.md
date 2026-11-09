<!-- Converted from core/security.txt (reStructuredText). Includes are inlined. -->

# Security Overview

To ensure the security of your MongoDB Agents, Ops Manager hosts,
and MongoDB deployments, Ops Manager supports the following security
options.

## TLS (Transport Layer Security) for Encrypted Connections

Ops Manager supports encrypted connections using TLS (Transport Layer Security) server or
client certificates. Client certificates identify the *user* while
server certificates identifies the *host*.

- The MongoDB Agent uses TLS (Transport Layer Security) server or client certificate that the
  legacy Automation Agent used.

  - If the legacy Monitoring Agent used its own TLS (Transport Layer Security) server or
    client certificate before the update to the MongoDB Agent,
    Monitoring continues to use that certificate.

  - If the legacy Backup Agent used its own TLS (Transport Layer Security) server or client
    certificate before the update to the MongoDB Agent, Backup
    continues to use that certificate.

- Ops Manager can
  connect to its backing databases
  using TLS (Transport Layer Security) server or client certificates.

- Ops Manager users can connect to the Ops Manager console or API (Application Programming Interface) using
  TLS (Transport Layer Security) server certificates.

## Authentication Mechanisms

### Authenticate with Deployments

Ops Manager supports these mechanisms to authenticate the Ops Manager Application
and its Agents with your MongoDB processes:

| From | To | MONGODB-CR | SCRAM-SHA-1 | SCRAM-SHA-256 | x.509 | Kerberos | LDAP |
|---|---|---|---|---|---|---|---|
| Ops Manager | Backing Database | check-circle | check-circle | check-circle | check-circle | check-circle | check-circle |
| MongoDB Agent | MongoDB Processes | check-circle | check-circle | check-circle | check-circle | check-circle | check-circle |
| Your Application Clients | MongoDB Processes | check-circle | check-circle | check-circle | check-circle | check-circle | check-circle |

**Note:**

Kerberos and LDAP (Lightweight Directory Access Protocol) authentication is available with
`MongoDB Enterprise` only.

### Authenticate with Ops Manager

Ops Manager supports these mechanisms to authenticate with
Ops Manager Application:

| From | To | Ops Manager DB | LDAP | SAML |
|---|---|---|---|---|
| Ops Manager User | Ops Manager | check-circle | check-circle | check-circle |
