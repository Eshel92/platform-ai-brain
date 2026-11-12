<!-- Part 7 of 7 of victoriametrics/sd_configs.md (split because the page is big). -->

## HTTP API client options

The following additional options can be specified in the [scrape_configs](#scrape_configs)
and in the majority of [supported service discovery configs](#supported-service-discovery-configs):

```yaml
    # authorization is an optional `Authorization` header configuration.
    #
    # authorization:
    #   type: "..."  # default: Bearer
    #   credentials: "..."
    #   credentials_file: "..."

    # basic_auth is an optional HTTP basic authentication configuration.
    #
    # basic_auth:
    #   username: "..."      # optional
    #   username_file: "..."  # optional, is mutually-exclusive with username
    #   password: "..."
    #   password_file: "..."  # is mutually-exclusive with password

    # bearer_token is an optional Bearer token to send in every HTTP API request during service discovery.
    #
    # bearer_token: "..."

    # bearer_token_file is an optional path to file with Bearer token to send
    # in every HTTP API request during service discovery.
    # The file is re-read every second, so its contents can be updated without the need to restart the service discovery.
    #
    # bearer_token_file: "..."

    # oauth2 is an optional OAuth 2.0 configuration.
    # See https://prometheus.io/docs/prometheus/latest/configuration/configuration/#oauth2
    # Additionally, `headers` field is supported for sending custom HTTP headers to `token_url`.
    #
    # oauth2:
    #   ...
    #   headers:
    #   - "X-Tenant-ID: my-tenant"

    # tls_config is an optional TLS configuration.
    # See https://prometheus.io/docs/prometheus/latest/configuration/configuration/#tls_config
    #
    # tls_config:
    #   ...

    # headers is an optional HTTP headers to pass with each request.
    #
    # headers:
    # - "HeaderName1: HeaderValue"
    # - "HeaderNameN: HeaderValueN"

    # proxy_url is an optional URL for the proxy to use for HTTP API queries during service discovery.
    #
    # proxy_url: "..."

    # proxy_authorization is an optional `Authorization` header config for the proxy_url.
    #
    # proxy_authorization:
    #   type: "..."  # default: Bearer
    #   credentials: "..."
    #   credentials_file: "..."

    # proxy_basic_auth is an optional HTTP basic authentication configuration for the proxy_url.
    #
    # proxy_basic_auth:
    #   username: "..."
    #   username_file: "..."  # is mutually-exclusive with username
    #   password: "..."
    #   password_file: "..."  # is mutually-exclusive with password

    # proxy_bearer_token is an optional Bearer token to send to proxy_url.
    #
    # proxy_bearer_token: "..."

    # proxy_bearer_token_file is an optional path to file with Bearer token to send to proxy_url.
    # The file is re-read every second, so its contents can be updated without the need to restart the service discovery.
    #
    # proxy_bearer_token_file: "..."

    # proxy_oauth2 is an optional OAuth 2.0 configuration for the proxy_url.
    # See https://prometheus.io/docs/prometheus/latest/configuration/configuration/#oauth2
    #
    # proxy_oauth2:
    #   ...

    # proxy_tls_config is an optional TLS configuration for the proxy_url.
    # See https://prometheus.io/docs/prometheus/latest/configuration/configuration/#tls_config
    #
    # proxy_tls_config:
    #   ...

    # proxy_headers is an optional HTTP headers to pass to the proxy_url.
    #
    # proxy_headers:
    # - "HeaderName1: HeaderValue"
    # - "HeaderNameN: HeaderValueN"

    # follow_redirects can be used for disallowing HTTP redirects.
    # By default HTTP redirects are followed.
    #
    # follow_redirects: false
```
