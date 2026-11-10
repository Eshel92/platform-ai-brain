<!-- Converted from security/security-manual-configuration.asciidoc (AsciiDoc). Includes are inlined. -->

## Manually configure security

Security needs vary depending on whether you're developing locally on your
laptop or securing all communications in a production environment. Regardless
of where you're deploying the Elastic Stack ("ELK"), running a secure cluster is
incredibly important to protect your data. That's why security is
enabled and configured by default in Elasticsearch 8.0
and later.

If you want to enable security on an existing, unsecured cluster, use your own 
Certificate Authority (CA), or would rather manually configure security, the 
following scenarios provide steps for configuring TLS on the transport layer,
plus securing HTTPS traffic if you want it.

If you configure security manually _before_ starting your Elasticsearch nodes, the
auto-configuration process will respect your security configuration. You can
adjust your TLS configuration at any time, such as 
updating node certificates.

(Figure: images/elastic-security-overview.png)

### Minimal security (Elasticsearch Development)

If you've been working with Elasticsearch and want to enable security on your existing,
unsecured cluster, start here. You'll set passwords for the built-in users to prevent 
unauthorized access to your local cluster, and also configure password 
authentication for Kibana.

**Important:** The minimal security scenario is not sufficient for
production mode clusters. If your cluster has multiple
nodes, you must enable minimal security and then
configure Transport Layer Security (TLS) between
nodes.

Set up minimal security

### Basic security (Elasticsearch + Kibana)

This scenario configures TLS for communication between
nodes. This security layer requires that nodes verify security certificates,
which prevents unauthorized nodes from joining your Elasticsearch cluster.

Your external HTTP traffic between Elasticsearch and Kibana won't be encrypted, but
internode communication will be secured.

Set up basic security

### Basic security plus secured HTTPS traffic (Elastic Stack)

This scenario builds on the one for basic security and secures all HTTP
traffic with TLS. In addition to configuring TLS on the transport interface of
your Elasticsearch cluster, you configure TLS on the HTTP interface for both
Elasticsearch and Kibana.

**Note:** If you need mutual (bidirectional) TLS on the HTTP layer, then you'll
need to configure mutual authenticated encryption.

You then configure Kibana and Beats to communicate with
Elasticsearch using TLS so that all communications are encrypted. This level
of security is strong, and ensures that any communications in and out of your
cluster are secure.

Set up basic security plus HTTPS traffic

(See `security/securing-communications/security-minimal-setup.md`)
(See `security/securing-communications/security-basic-setup.md`)
(See `security/securing-communications/security-basic-setup-https.md`)
(See `security/securing-communications/change-passwords-native-users.md`)
(See `security/securing-communications/enabling-cipher-suites.md`)
(See `security/securing-communications/tls-versions-jdk.md`)
(See `security/reference/files.md`)
(See `security/fips-140-compliance.md`)
