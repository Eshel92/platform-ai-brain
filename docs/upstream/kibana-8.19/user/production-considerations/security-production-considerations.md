<!-- Converted from user/production-considerations/security-production-considerations.asciidoc (AsciiDoc). Includes are inlined. -->

## Security production considerations

To secure your Kibana installation in production, consider these high-priority topics to ensure
that only authorized users can access Kibana.
For more information on Kibana's security controls, see Configure security.

### Enable SSL/TLS

You should use SSL/TLS encryption to ensure that traffic between browsers and the Kibana server cannot be viewed or tampered with by third
parties. See 
[encrypt HTTP client communications for Kibana](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/security-basic-setup-https.html#encrypt-kibana-http).

encrypt-kibana-http

### Use Elastic Stack security features

You can use Elastic Stack security features to control what Elasticsearch data users can
access through Kibana.

When security features are enabled, Kibana users have to log in. They must
have a role granting Kibana privileges and access
to the indices that they will be working with in Kibana.

If a user loads a Kibana dashboard that accesses data in an index that they
are not authorized to view, they get an error that indicates the index does
not exist.

For more information on granting access to Kibana, see xpack-security-authorization.

### Use secure HTTP headers

The Kibana server can instruct browsers to enable additional security controls using HTTP headers.

1. Enable HTTP Strict-Transport-Security.
Use `strictTransportSecurity` to ensure that browsers will only attempt
to access Kibana with SSL/TLS encryption. This is designed to prevent manipulator-in-the-middle attacks.
To configure this with a lifetime of one
year in your `kibana.yml`:
```js
server.securityResponseHeaders.strictTransportSecurity: "max-age=31536000"
```
**Warning:** This header will block unencrypted connections for the entire domain. If you host more than one web application on the same domain
using different ports or paths, all of them will be affected.

2. Disable embedding.
Use `disableEmbedding` to ensure
that Kibana cannot be embedded in other websites.
To configure this in your `kibana.yml`:
```js
server.securityResponseHeaders.disableEmbedding: true
```

### Require a Content Security Policy

Kibana uses a Content Security Policy (CSP) to prevent the browser from allowing
unsafe scripting, but older browsers will silently ignore this policy. If your
organization does not need to support very old
versions of our supported browsers, we recommend that you enable Kibana's
`strict` mode for the CSP. This will block access to Kibana
for any browser that does not enforce even a rudimentary set of CSP
protections.

To do this, set `csp.strict` to `true` in your `kibana.yml`:

```js
csp.strict: true
```
