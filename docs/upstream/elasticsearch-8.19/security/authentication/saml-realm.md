<!-- Converted from security/authentication/saml-realm.asciidoc (AsciiDoc). Includes are inlined. -->

### SAML authentication

The Elastic Stack security features support user authentication using SAML
single sign-on (SSO). The security features provide this support using the Web
Browser SSO profile of the SAML 2.0 protocol.

This protocol is specifically designed to support authentication via an
interactive web browser, so it does not operate as a standard authentication
realm. Instead, there are Kibana and Elasticsearch security features that work
together to enable interactive SAML sessions.

This means that the SAML realm is not suitable for use by standard REST clients.
If you configure a SAML realm for use in Kibana, you should also configure
another realm, such as the native realm in your authentication
chain.

In order to simplify the process of configuring SAML authentication within the
Elastic Stack, there is a step-by-step guide to
Configuring SAML single-sign-on on the Elastic Stack.
