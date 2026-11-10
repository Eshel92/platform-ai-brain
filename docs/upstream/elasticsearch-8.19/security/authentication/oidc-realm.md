<!-- Converted from security/authentication/oidc-realm.asciidoc (AsciiDoc). Includes are inlined. -->

### OpenID Connect authentication

The OpenID Connect realm enables Elasticsearch to serve as an OpenID Connect Relying
Party (RP) and provides single sign-on (SSO) support in Kibana. 

It is specifically designed to support authentication via an interactive web
browser, so it does not operate as a standard authentication realm. Instead,
there are Kibana and Elasticsearch security features that work together to enable
interactive OpenID Connect sessions.

This means that the OpenID Connect realm is not suitable for use by standard
REST clients. If you configure an OpenID Connect realm for use in Kibana, you
should also configure another realm, such as the native realm
in your authentication chain.

In order to simplify the process of configuring OpenID Connect authentication
within the Elastic Stack, there is a step-by-step guide: oidc-guide.
