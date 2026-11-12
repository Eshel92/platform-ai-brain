<!-- Part 5 of 6 of victoriametrics/vmauth.md (split because the page is big). -->

## Auth config

`-auth.config` is represented in the following `yml` format:

```yaml
# An arbitrary number of usernames may be put here.
# It is possible to set multiple identical usernames with different passwords.
# Such usernames can be differentiated by the `name` option.

users:
  # Requests with the 'Authorization: Bearer XXXX' and 'Authorization: Token XXXX'
  # headers are proxied to http://localhost:8428 .
  # For example, http://vmauth:8427/api/v1/query is proxied to http://localhost:8428/api/v1/query
  # Requests with the Basic Auth username=XXXX are proxied to http://localhost:8428 as well.
- bearer_token: "XXXX"
  url_prefix: "http://localhost:8428"

  # Requests with the 'Authorization: Foo XXXX' header are proxied to http://localhosT:8428 .
  # For example, http://vmauth:8427/api/v1/query is proxied to http://localhost:8428/api/v1/query
- auth_token: "Foo XXXX"
  url_prefix: "http://localhost:8428"

  # Requests with the 'Authorization: Bearer YYY' header are proxied to http://localhost:8428 ,
  # The `X-Scope-OrgID: foobar` HTTP header is added to every proxied request.
  # The `X-Server-Hostname` http header is removed from the proxied response.
  # For example, http://vmauth:8427/api/v1/query is proxied to http://localhost:8428/api/v1/query
- bearer_token: "YYY"
  url_prefix: "http://localhost:8428"
  # extra headers to add to the request or remove from the request (if header value is empty)
  headers:
    - "X-Scope-OrgID: foobar"
  # extra headers to add to the response or remove from the response (if header value is empty)
  response_headers:
    - "X-Server-Hostname:" # empty value means the header will be removed from the response

  # All the requests to http://vmauth:8427 with the given Basic Auth (username:password)
  # are proxied to http://localhost:8428 .
  # For example, http://vmauth:8427/api/v1/query is proxied to http://localhost:8428/api/v1/query
  #
  # The given user can send a maximum of 10 concurrent requests according to the provided max_concurrent_requests.
  # Excess concurrent requests are rejected with 429 HTTP status code.
  # See also -maxConcurrentPerUserRequests and -maxConcurrentRequests command-line flags.
- username: "local-single-node"
  password: "***"
  url_prefix: "http://localhost:8428"
  max_concurrent_requests: 10

  # All the requests to http://vmauth:8427 with the given Basic Auth (username:password)
  # are proxied to http://localhost:8428 with extra_label=team=dev query arg.
  # For example, http://vmauth:8427/api/v1/query is proxied to http://localhost:8428/api/v1/query?extra_label=team=dev
- username: "local-single-node2"
  password: "***"
  url_prefix: "http://localhost:8428?extra_label=team=dev"

  # All the requests to http://vmauth:8427 with the given Basic Auth (username:password)
  # are proxied to https://localhost:8428.
  # For example, http://vmauth:8427/api/v1/query is proxied to https://localhost/api/v1/query
  # TLS verification is skipped for https://localhost.
- username: "local-single-node-with-tls"
  password: "***"
  url_prefix: "https://localhost"
  tls_insecure_skip_verify: true

  # All the requests to http://vmauth:8427 with the given Basic Auth (username:password)
  # are load-balanced among http://vmselect1:8481/select/123/prometheus and http://vmselect2:8481/select/123/prometheus
  # For example, http://vmauth:8427/api/v1/query is proxied to the following URLs in a round-robin manner:
  #   - http://vmselect1:8481/select/123/prometheus/api/v1/select
  #   - http://vmselect2:8481/select/123/prometheus/api/v1/select
- username: "cluster-select-account-123"
  password: "***"
  url_prefix:
  - "http://vmselect1:8481/select/123/prometheus"
  - "http://vmselect2:8481/select/123/prometheus"

  # All the requests to http://vmauth:8427 with the given Basic Auth (username:password)
  # are load-balanced between http://vminsert1:8480/insert/42/prometheus and http://vminsert2:8480/insert/42/prometheus
  # For example, http://vmauth:8427/api/v1/write is proxied to the following URLs in a round-robin manner:
  #   - http://vminsert1:8480/insert/42/prometheus/api/v1/write
  #   - http://vminsert2:8480/insert/42/prometheus/api/v1/write
- username: "cluster-insert-account-42"
  password: "***"
  url_prefix:
  - "http://vminsert1:8480/insert/42/prometheus"
  - "http://vminsert2:8480/insert/42/prometheus"

  # A single user for querying and inserting data:
  #
  # - Requests to http://vmauth:8427/api/v1/query, http://vmauth:8427/api/v1/query_range
  #   and http://vmauth:8427/api/v1/label/<label_name>/values are proxied to the following URLs in a round-robin manner:
  #     - http://vmselect1:8481/select/42/prometheus
  #     - http://vmselect2:8481/select/42/prometheus
  #   For example, http://vmauth:8427/api/v1/query is proxied to http://vmselect1:8480/select/42/prometheus/api/v1/query
  #   or to http://vmselect2:8480/select/42/prometheus/api/v1/query .
  #   Requests are retried at other url_prefix backends if response status codes match 500 or 502.
  #
  # - Requests to http://vmauth:8427/api/v1/write are proxied to http://vminsert:8480/insert/42/prometheus/api/v1/write .
  #   The "X-Scope-OrgID: abc" HTTP header is added to these requests.
  #   The "X-Server-Hostname" HTTP header is removed from the proxied response.
  #
  # Request which do not match `src_paths` from the `url_map` are proxied to the urls from `default_url`
  # in a round-robin manner. The original request path is passed in `request_path` query arg.
  # For example, request to http://vmauth:8427/non/existing/path are proxied:
  #  - to http://default1:8888/unsupported_url_handler?request_path=/non/existing/path
  #  - or http://default2:8888/unsupported_url_handler?request_path=/non/existing/path
  #
  # Regular expressions are allowed in `src_paths` and `src_hosts` entries.
- username: "foobar"
  # log requests that failed url_map rules in the following form:
  #   statusCode=<SC> remoteAddr: "<IP>, X-Forwarded-For: <IP>"; requestURI: <URI>; missing route for <URL>"(host: <HOST>; path: <PATH>; args: <ARGS>; headers: <HEADERS>)
  # May contain sensitive information and is recommended to use only for debugging purposes.
  dump_request_on_errors: true
  url_map:
  - src_paths:
    - "/api/v1/query"
    - "/api/v1/query_range"
    - "/api/v1/label/[^/]+/values"
    url_prefix:
    - "http://vmselect1:8481/select/42/prometheus"
    - "http://vmselect2:8481/select/42/prometheus"
    retry_status_codes: [500, 502]
  - src_paths: ["/api/v1/write"]
    url_prefix: "http://vminsert:8480/insert/42/prometheus"
    headers:
    - "X-Scope-OrgID: abc"
    response_headers:
    - "X-Server-Hostname:" # empty value means the header will be removed from the response
    ip_filters:
      deny_list: [127.0.0.1]
  default_url:
  - "http://default1:8888/unsupported_url_handler"
  - "http://default2:8888/unsupported_url_handler"

# Requests without an Authorization header are proxied according to the `unauthorized_user` section.
# Requests are proxied in round-robin fashion between `url_prefix` backends.
# The deny_partial_response query arg is added to all the proxied requests.
# The requests are retried if url_prefix backends send 500 or 503 response status codes.
# Note that the unauthorized_user section takes precedence when processing a route without credentials,
# even if such a route also exists in the users section (see https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5236).
unauthorized_user:
  url_prefix:
  - http://vmselect-az1/?deny_partial_response=1
  - http://vmselect-az2/?deny_partial_response=1
  retry_status_codes: [503, 500]

ip_filters:
  allow_list: ["1.2.3.0/24", "127.0.0.1"]
  deny_list:
  - 10.1.0.1
```

The config may contain `%{ENV_VAR}` placeholders, which are substituted by the corresponding `ENV_VAR` environment variable values.
This may be useful for passing secrets to the config.


## mTLS protection

By default, `vmauth` accepts HTTP requests at the `8427` port (this port can be changed via the `-httpListenAddr` command-line flag).
The [Enterprise version of vmauth](https://docs.victoriametrics.com/victoriametrics/enterprise/) supports the ability to accept [mTLS](https://en.wikipedia.org/wiki/Mutual_authentication) requests at this port, by specifying `-tls` and `-mtls` command-line flags. For example, the following command runs `vmauth`, which accepts only mTLS requests at port `8427`:

```sh
./vmauth -tls -mtls -auth.config=...
```

By default, system-wide [TLS Root CA](https://en.wikipedia.org/wiki/Root_certificate) is used to verify client certificates if the `-mtls` command-line flag is specified.
It is possible to specify a custom TLS Root CA via the `-mtlsCAFile` command-line flag.

See also [automatic issuing of TLS certificates](#automatic-issuing-of-tls-certificates) and [mTLS-based request routing](#mtls-based-request-routing).


## Security

1. All backend services behind `vmauth` must be in an isolated private network, accessible to external users only through `vmauth`.

1. Never send auth headers in plaintext over untrusted networks. Enable HTTPS on `-httpListenAddr` by passing the following `-tls*` command-line flags to `vmauth`:

    ```sh
      -tls
         Whether to enable TLS for incoming HTTP requests at -httpListenAddr (aka https). -tlsCertFile and -tlsKeyFile must be set if -tls is set
      -tlsCertFile string
         Path to file with TLS certificate. Used only if -tls is set. Prefer ECDSA certs instead of RSA certs, since RSA certs are slow
      -tlsKeyFile string
         Path to file with TLS key. Used only if -tls is set
    ```

    See also:
     - [Automatic issuing of TLS certificates](#automatic-issuing-of-tls-certificates).
     - [mTLS protection](https://docs.victoriametrics.com/victoriametrics/vmauth/#mtls-protection) for enabling [mutual TLS authentication](https://en.wikipedia.org/wiki/Mutual_authentication).
     - [TLS termination proxy](https://en.wikipedia.org/wiki/TLS_termination_proxy) may be put in front of `vmauth`.

1. We recommend protecting the following endpoints with authKeys:

    * `/-/reload` with `-reloadAuthKey` command-line flag, so external users cannot trigger config reload.
    * `/flags` with `-flagsAuthKey` command-line flag, so unauthorized users cannot read command-line flag values.
    * `/metrics` with `-metricsAuthKey` command-line flag, so unauthorized users cannot access [vmauth metrics](https://docs.victoriametrics.com/victoriametrics/vmauth/#monitoring).
    * `/debug/pprof` with `-pprofAuthKey` command-line flag, so unauthorized users cannot access [profiling information](#profiling).

1. Alternatively, serve internal API routes on a separate listen address via `-httpInternalListenAddr=127.0.0.1:8426`{{% available_from "v1.111.0" %}}.
To enable TLS on the public listener while keeping the internal listener non-TLS, configure multiple listeners as follows:

    ```
    /path/to/vmauth -httpInternalListenAddr=,localhost:8426 -httpListenAddr=0.0.0.0:443, -tls=true,false -tlsCertFile=a-cert.crt -tlsKeyFile=a-key.key
    ```

1. If you know the source IPs upfront, you can restrict access with [IP filters](https://docs.victoriametrics.com/victoriametrics/vmauth/#ip-filters). See also [concurrency limiting docs](https://docs.victoriametrics.com/victoriametrics/vmauth/#concurrency-limiting).

1. Authentication headers are proxied to backends by default. If this is undesirable, set an empty `Authorization` header in the `headers` section to strip it:

    ```yaml
    users:
      - username: "tester"
        password: "testpass"
        url_prefix: "http://127.0.0.1:9999/"
        headers:
          - "Authorization:"
    ```

1. [JWT authentication](https://docs.victoriametrics.com/victoriametrics/vmauth/#jwt-token-auth-proxy) verifies the signature, expiration, and `vm_access` claim. For OIDC setups, vmauth also verifies `iss` against the configured issuer; follow [ID Token Validation](https://openid.net/specs/openid-connect-core-1_0.html#IDTokenValidation) best practices and verify `aud` via `match_claims`:

    ```yaml
    users:
    - jwt:
        oidc:
          issuer: "https://accounts.example.com"
        match_claims:
          aud: "theClientID"
      url_prefix: "http://127.0.0.1:9999/"
    ```

1. When `vmauth` routes [multitenant](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#multitenant-reads) requests, you must explicitly set `extra_label`, `extra_filters`, and `extra_filters[]` in `url_prefix`. Without this, a client can supply its own `extra_filters` or `extra_filters[]` values and bypass the tenant restriction set via `extra_label`, because `vmselect` combines these filters with `OR` logic.

    ```yaml
    unauthorized_user:
        url_prefix: http://vmselect/select/multitenant?extra_filters[]=&extra_filters=&extra_label=vm_account_id=10&extra_label=vm_project_id=100
    ```

1. Review that `vmauth` `src_paths` are properly tenant-scoped for [multitenant](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#multitenant-reads) routing. Some APIs provide access across all tenants. They should be excluded from per-tenant access. Check the [Per-tenant authorization](https://docs.victoriametrics.com/victoriametrics/vmauth/#per-tenant-authorization) documentation and the available [API examples](https://docs.victoriametrics.com/victoriametrics/url-examples/) for the supported endpoint paths.

1. When backends use [multitenancy via headers](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#multitenancy-via-headers), clients can set `AccountID` and `ProjectID` headers to route requests to arbitrary tenants. To prevent this, explicitly override these headers in the `headers` section so the client-supplied values are ignored:

    ```yaml
    users:
      - username: "tenant2"
        password: "secret"
        url_prefix: "http://vmselect:8481/"
        headers:
          - "AccountID: 2"
          - "ProjectID: 0"
    ```

1. Clients can spoof HTTP headers, so when `vmauth` is internet-facing, take the following precautions:

    * Drop `X-Forwarded-For` headers at the internet-facing reverse proxy before traffic reaches `vmauth`.
    * Avoid using `-httpRealIPHeader` on internet-facing `vmauth` instances.
    * Set `removeXFFHTTPHeaderValue` on the internet-facing `vmauth` to replace the `X-Forwarded-For` value with the client's `remoteAddr`.

    See also [X-Forwarded-For security and privacy concerns](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For#security_and_privacy_concerns).


## Automatic issuing of TLS certificates

`vmauth` [Enterprise](https://docs.victoriametrics.com/victoriametrics/enterprise/) supports automatic issuing of TLS certificates via [Let's Encrypt service](https://letsencrypt.org/).
The following command-line flags must be set in order to enable automatic issuance of TLS certificates:

* `-httpListenAddr` must be set to listen on TCP port `443`. For example, `-httpListenAddr=:443`. This port must be accessible by the [Let's Encrypt service](https://letsencrypt.org/).
* `-tls` must be set to accept HTTPS requests at `-httpListenAddr`. Note that `-tlsCertFile` and `-tlsKeyFile` aren't needed when automatic TLS certificate issuing is enabled.
* `-tlsAutocertHosts` must be set to a comma-separated list of hosts, which can be reached via `-httpListenAddr`. TLS certificates are automatically issued for these hosts.
* `-tlsAutocertEmail` must be set to the contact email for the issued TLS certificates.
* `-tlsAutocertCacheDir` may be set to the directory path to persist the issued TLS certificates between `vmauth` restarts. If this flag isn't set, then TLS certificates are reissued on every restart.

This functionality can be evaluated for free according to [these docs](https://docs.victoriametrics.com/victoriametrics/enterprise/).

See also [security](#security).
