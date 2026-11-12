<!-- Part 2 of 6 of victoriametrics/vmauth.md (split because the page is big). -->

## Use cases

* [Simple HTTP proxy](#simple-http-proxy)
* [Generic HTTP proxy for different backends](#generic-http-proxy-for-different-backends)
* [Generic HTTP load balancer](#generic-http-load-balancer)
* [Load balancer for vmagent](#load-balancer-for-vmagent)
* [Load balancer for VictoriaMetrics cluster](#load-balancer-for-victoriametrics-cluster)
* [High availability](#high-availability)
* [TLS termination proxy](#tls-termination-proxy)
* [Basic Auth proxy](#basic-auth-proxy)
* [Bearer Token auth proxy](#bearer-token-auth-proxy)
* [JWT Token auth proxy](#jwt-token-auth-proxy)
* [Per-tenant authorization](#per-tenant-authorization)
* [mTLS-based request routing](#mtls-based-request-routing)
* [Enforcing query args](#enforcing-query-args)
* [OIDC discovery](#oidc-discovery)

### Simple HTTP proxy

The following [`-auth.config`](#auth-config) instructs `vmauth` to proxy all the incoming requests to the given backend.
For example, requests to `http://vmauth:8427/foo/bar` are proxied to `http://backend/foo/bar`:

```yaml
unauthorized_user:
  url_prefix: "http://backend/"
```

`vmauth` can balance load among multiple backends - see [these docs](#load-balancing) for details.

See also [authorization](#authorization) and [routing](#routing) docs.

### Generic HTTP proxy for different backends

`vmauth` can proxy requests to different backends depending on the requested path, [query args](https://en.wikipedia.org/wiki/Query_string), and any HTTP request header.

For example, the following [`-auth.config`](#auth-config) instructs `vmauth` to make the following:

* Requests starting with `/app1/` are proxied to `http://app1-backend/`, while the `/app1/` path prefix is dropped according to [`drop_src_path_prefix_parts`](#dropping-request-path-prefix).
  For example, the request to `http://vmauth:8427/app1/foo/bar?baz=qwe` is proxied to `http://app1-backend/foo/bar?baz=qwe`.
* Requests starting with `/app2/` are proxied to `http://app2-backend/`, while the `/app2/` path prefix is dropped according to [`drop_src_path_prefix_parts`](#dropping-request-path-prefix).
  For example, the request to `http://vmauth:8427/app2/index.html` is proxied to `http://app2-backend/index.html`.
* Other requests are proxied to `http://default-backed/`.

```yaml
unauthorized_user:
  url_map:
  - src_paths:
    - "/app1/.*"
    drop_src_path_prefix_parts: 1
    url_prefix: "http://app1-backend/"
  - src_paths:
    - "/app2/.*"
    drop_src_path_prefix_parts: 1
    url_prefix: "http://app2-backend/"
  url_prefix: "http://default-backed/"
```

Sometimes it is necessary to proxy all requests that do not match `url_map` to a special `404` page, which could count as invalid requests.
Use `default_url` for this case. For example, the following [`-auth.config`](#auth-config) instructs `vmauth` to send all the requests,
which do not match `url_map`, to the `http://some-backend/404-page.html` page. The requested path is passed via the `request_path` query arg.
For example, the request to `http://vmauth:8427/foo/bar?baz=qwe` is proxied to `http://some-backend/404-page.html?request_path=%2Ffoo%2Fbar%3Fbaz%3Dqwe`.

```yaml
unauthorized_user:
  url_map:
  - src_paths:
    - "/app1/.*"
    drop_src_path_prefix_parts: 1
    url_prefix: "http://app1-backend/"
  - src_paths:
    - "/app2/.*"
    drop_src_path_prefix_parts: 1
    url_prefix: "http://app2-backend/"
  default_url: "http://some-backend/404-page.html"
```

See [routing docs](#routing) for details.

See also [authorization](#authorization) and [load balancing](#load-balancing) docs.

### Generic HTTP load balancer

`vmauth` can balance load across multiple HTTP backends using least-loaded round-robin.
For example, the following [`-auth.config`](#auth-config) instructs `vmauth` to spread load among multiple application instances:

```yaml
unauthorized_user:
  url_prefix:
  - "http://app-instance-1/"
  - "http://app-instance-2/"
  - "http://app-instance-3/"
```

See [load balancing docs](#load-balancing) for more details.

See also [authorization](#authorization) and [routing](#routing) docs.

### Load balancer for vmagent

If [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/) is used for processing [data push requests](https://docs.victoriametrics.com/victoriametrics/vmagent/#how-to-push-data-to-vmagent), then it is possible to scale the performance of data processing at `vmagent` by spreading the load among multiple identically configured `vmagent` instances.
This can be done with the following [config](#auth-config) for `vmauth`:

```yaml
unauthorized_user:
  url_map:
  - src_paths:
    - "/prometheus/api/v1/write"
    - "/influx/write"
    - "/api/v1/import"
    - "/api/v1/import/.*"
    url_prefix:
    - "http://vmagent-1:8429/"
    - "http://vmagent-2:8429/"
    - "http://vmagent-3:8429/"
```

See [load balancing docs](#load-balancing) for more details.

See also [authorization](#authorization) and [routing](#routing) docs.

### Load balancer for VictoriaMetrics cluster

[VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/) accepts incoming data via `vminsert` nodes and processes incoming requests via `vmselect` nodes according to [these docs](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#architecture-overview).
`vmauth` can be used for balancing both `insert` and `select` requests among `vminsert` and `vmselect` nodes, when the following [`-auth.config`](#auth-config) is used:

```yaml
unauthorized_user:
  url_map:
  - src_paths:
    - "/insert/.*"
    url_prefix:
    - "http://vminsert-1:8480/"
    - "http://vminsert-2:8480/"
    - "http://vminsert-3:8480/"
  - src_paths:
    - "/select/.*"
    - "/admin/.*"
    url_prefix:
    - "http://vmselect-1:8481/"
    - "http://vmselect-2:8481/"
```

See [load balancing docs](#load-balancing) for more details.

See also [authorization](#authorization) and [routing](#routing) docs.

### High availability

`vmauth` automatically switches from a temporarily unavailable backend to other hot standby backends listed in `url_prefix`
if it runs with the `-loadBalancingPolicy=first_available` command-line flag. The load balancing policy can be overridden at `user` and `url_map` sections of [`-auth.config`](#auth-config) via `load_balancing_policy` option.
For example, the following config instructs `vmauth` to proxy requests to `http://victoria-metrics-main:8428/` backend.
If this backend becomes unavailable, then `vmauth` starts proxying requests to `http://victoria-metrics-standby1:8428/`.
If this backend also becomes unavailable, then requests are proxied to the last specified backend - `http://victoria-metrics-standby2:8428/`:

If all backends are marked as unavailable, requests are proxied to the first configured backend `http://victoria-metrics-main:8428/` instead of failing immediately.
```yaml
unauthorized_user:
  url_prefix:
  - "http://victoria-metrics-main:8428/"
  - "http://victoria-metrics-standby1:8428/"
  - "http://victoria-metrics-standby2:8428/"
  load_balancing_policy: first_available
```

See [load-balancing docs](#load-balancing) for more details.

See also [authorization](#authorization) and [routing](#routing) docs.

### TLS termination proxy

`vmauth` can terminate HTTPS requests to backend services when it runs with the following command-line flags:

```sh
/path/to/vmauth -tls -tlsKeyFile=/path/to/tls_key_file -tlsCertFile=/path/to/tls_cert_file -httpListenAddr=0.0.0.0:443
```

* `-httpListenAddr` sets the address to listen for incoming HTTPS requests
* `-tls` enables accepting TLS connections at `-httpListenAddr`
* `-tlsKeyFile` sets the path to the TLS certificate key file
* `-tlsCertFile` sets the path to the TLS certificate file

See also [automatic issuing of TLS certificates](#automatic-issuing-of-tls-certificates).

See also [security](#security), [routing](#routing) and [load balancing](#load-balancing) docs.

### Basic Auth proxy

`vmauth` can authorize access to backends depending on the provided [Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication) request headers.
For example, the following [config](#auth-config) proxies requests to [single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/)
if they contain Basic Auth header with the given `username` and `password`:

```yaml
users:
- username: foo
  password: bar
  url_prefix: "http://victoria-metrics:8428/"
```

See also [authorization](#authorization), [security](#security), [routing](#routing) and [load balancing](#load-balancing) docs.

### Bearer Token auth proxy

`vmauth` can authorize access to backends depending on the provided `Bearer Token` request headers.
For example, the following [config](#auth-config) proxies requests to [single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/)
if they contain the given `bearer_token`:

```yaml
users:
- bearer_token: ABCDEF
  url_prefix: "http://victoria-metrics:8428/"
```

See also [authorization](#authorization), [security](#security), [routing](#routing) and [load balancing](#load-balancing) docs.

### JWT Token auth proxy

`vmauth` can authorize access{{% available_from "v1.137.0" %}} to backends depending on the provided [JWT token](https://www.jwt.io/) in `Authorization` request header. 
JWT tokens are verified using RSA or ECDSA public keys. The following auth config proxies requests to [single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/) if they contain a valid JWT token:

```yaml
users:
- jwt:
    public_keys:
    - |
      -----BEGIN PUBLIC KEY-----
      MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...
      -----END PUBLIC KEY-----
  url_prefix: "http://victoria-metrics:8428/"
```

The `vm_access` claim is optional starting from {{% available_from "v1.147.0" %}}: when present it is used for [request templating](https://docs.victoriametrics.com/victoriametrics/vmauth/#jwt-claim-based-request-templating), and when absent the default tenant `0:0` is assumed for any `vm_access`-based placeholders. Routing can rely solely on other token claims via [JWT claim matching](https://docs.victoriametrics.com/victoriametrics/vmauth/#jwt-claim-matching).

For testing, skip signature verification with `skip_verify: true` (not recommended for production).

```yaml
users:
- jwt:
    skip_verify: true
  url_prefix: "http://victoria-metrics:8428"
```

JWT authentication cannot be combined with other auth methods (`bearer_token`, `username`, `password`) in the same `users` config.


#### OIDC Discovery

Instead of specifying public keys manually, `vmauth` can automatically fetch{{% available_from "v1.138.0" %}} 
and rotate public keys from an [OpenID Connect (OIDC)](https://openid.net/connect/) provider via its [Discovery endpoint](https://openid.net/specs/openid-connect-discovery-1_0.html).
This is useful when integrating with identity providers such as Keycloak, Auth0, Okta, or Google.

Set `oidc.issuer` to the base URL of the OIDC provider. `vmauth` will:
1. Fetch `{issuer}/.well-known/openid-configuration` to discover the `jwks_uri`.
2. Download the JSON Web Key Set (JWKS) from the `jwks_uri` to obtain the public keys used to verify JWT signatures.
   Only `RSA` and `EC` (`P-256`, `P-384`, `P-521`) keys are supported. Keys of other types, such as `OKP` (Ed25519), and keys with missing or invalid members are skipped with a warning.
3. Automatically refresh the keys every 5 minutes to handle key rotation.

JWT tokens must contain an `iss` claim that matches the configured `issuer` value exactly.

```yaml
users:
- jwt:
    oidc:
      issuer: "https://your-identity-provider.example.com"
    match_claims:
      # The OIDC spec requires verifying that the `aud` claim contains the client ID.
      # See https://openid.net/specs/openid-connect-core-1_0.html#IDTokenValidation
      aud: "theClientID"
  url_prefix: "http://victoria-metrics:8428/"
```

The `oidc` option cannot be combined with `public_keys`, `public_key_files`, or `skip_verify`.

If the OIDC provider is temporarily unavailable during a key refresh, `vmauth` continues using the previously fetched keys until the next successful refresh.
If no keys have been fetched yet (e.g., on startup when the provider is unreachable), the config section is skipped during authentication.


#### JWT claim matching

`vmauth` can route requests to different backends depending on the claims contained
in the provided [JWT token](https://www.jwt.io/) based on `match_claims`{{% available_from "v1.138.0" %}} field.

This enables RBAC-style setups where tokens carrying different roles
(e.g. `admin`, `viewer`, `writer`) are mapped to different users — each with its own
`url_prefix` or `url_map` configuration — all authenticated against the same public key.

Claim matching is configured via the `match_claims` field inside the `jwt` user section.
A user is selected only if:

1. All configured `match_claims` entries evaluate successfully (logical AND).
2. The token signature is cryptographically valid.

If `match_claims` is not set or is empty, the user matches any valid JWT token
signed with the configured public key.

Claim names support dot-notation for traversal of nested JSON objects
(a simplified JSONPath-style approach), for example `vm_access.metrics_account_id` matches `{"vm_access": {"metrics_account_id": 1}}` and
`security.permissions.0.read` matches `{"security": {"permissions": [{"read": 1}]}}.
Claim names must point to a **leaf value** or an **array**. The supported leaf types are string, integer, float and boolean.
If the claim value is an array, each scalar element is compared against the match value - the claim matches if any element matches. Objects and nested arrays inside the array are skipped.
All configured claims must match and the values use regular expression syntax.

For example, the following config routes requests based on the `role` claim in the JWT token:

```yaml
users:
- jwt:
    oidc:
      issuer: "https://your-identity-provider.example.com"
  url_prefix: "http://victoria-metrics:8428/"
    public_keys:
    - |
      -----BEGIN PUBLIC KEY-----
      MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...
      -----END PUBLIC KEY-----
    match_claims:
      role: admin
  url_prefix: "http://victoria-metrics-admin:8428/"
- jwt:
    public_keys:
    - |
      -----BEGIN PUBLIC KEY-----
      MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...
      -----END PUBLIC KEY-----
    match_claims:
      role: viewer
  url_prefix: "http://victoria-metrics-readonly:8428/"
```

The following config demonstrates matching on nested claims using dot-notation:

```yaml
users:
- jwt:
    public_keys:
    - |
      -----BEGIN PUBLIC KEY-----
      MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...
      -----END PUBLIC KEY-----
    match_claims:
      vm_access.metrics_account_id: 1
  url_prefix: "http://victoria-metrics-tenant-1:8428/"
- jwt:
    public_keys:
    - |
      -----BEGIN PUBLIC KEY-----
      MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...
      -----END PUBLIC KEY-----
    match_claims:
      foo.bar: baz
  url_prefix: "http://victoria-metrics-tenant-2:8428/"
```

The following config matches against array claim values.
The first user matches a token with claim `{"roles": ["admin"]}`, while the second matches a token with claim `{"roles": ["read"]}` or `{"roles": ["write"]}`.

```yaml
users:
- jwt:
    public_keys:
    - |
      -----BEGIN PUBLIC KEY-----
      MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...
      -----END PUBLIC KEY-----
    match_claims:
      roles: admin
  url_prefix: "http://victoria-metrics-admin:8428/"
- jwt:
    public_keys:
    - |
      -----BEGIN PUBLIC KEY-----
      MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...
      -----END PUBLIC KEY-----
    match_claims:
      roles: "read|write"
  url_prefix: "http://victoria-metrics-readonly:8428/"
```

The following config matches any valid token (no claim filtering),
equivalent to the behavior when `match_claims` is omitted:

```yaml
users:
- jwt:
    public_keys:
    - |
      -----BEGIN PUBLIC KEY-----
      MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...
      -----END PUBLIC KEY-----
    match_claims: {}
  url_prefix: "http://victoria-metrics:8428/"
```

The following config demonstrates matching on nested claims using dot-notation and regex value match for multiple tenants access:

```yaml
users:
- jwt:
    public_keys:
    - |
      -----BEGIN PUBLIC KEY-----
      MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...
      -----END PUBLIC KEY-----
    match_claims:
      vm_access.metrics_account_id: "0|1|2"
  url_prefix: "http://victoria-metrics-vmselect-1:8481/select/multitenant?extra_filters={vm_account_id=~\"(0|1|2)\"}"
- jwt:
    public_keys:
    - |
      -----BEGIN PUBLIC KEY-----
      MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...
      -----END PUBLIC KEY-----
    match_claims:
      vm_access.metrics_account_id: "3|4|5"
  url_prefix: "http://victoria-metrics-vmselect-1:8481/select/multitenant?extra_filters={vm_account_id=~\"(3|4|5)\"}"
```


#### JWT claim matching. Conflict resolution

When multiple users have `match_claims` entries that all match the incoming token,
`vmauth` selects the user whose `match_claims` map contains the **greatest number of entries**.
A more specific match (more claim constraints) always takes priority over a less specific one.

For example, given the following config and a token containing both `role=admin` and `iss=foo`:

```yaml
users:
- jwt:
    match_claims:
      iss: foo
  url_prefix: "http://victoria-metrics-default:8428/"
- jwt:
    match_claims:
      iss: foo
      role: admin
  url_prefix: "http://victoria-metrics-admin:8428/"
```

The second user is selected because it has two matching claim entries compared to one,
and requests are proxied to `http://victoria-metrics-admin:8428/`.

If two users match with the **same number** of `match_claims` entries,
the selection becomes non-deterministic. To avoid ambiguity, ensure that
claim match conditions across users with the same number of entries are mutually exclusive.

For example, the following config is ambiguous when a token contains both `role=foo` and `team=platform`:

```yaml
users:
- jwt:
    match_claims:
      role: foo
  url_prefix: "http://backend-a:8428/"
- jwt:
    match_claims:
      team: platform
  url_prefix: "http://backend-b:8428/"
```

Both users have one claim entry each, so if the token satisfies both,
neither takes priority. Resolve this by adding the same match claim keys to both users:

```yaml
users:
- jwt:
    match_claims:
      team: ops
      role: foo
  url_prefix: "http://backend-a:8428/"
- jwt:
    match_claims:
      team: platform
      role: admin
  url_prefix: "http://backend-b:8428/"

```

JWT claim-based matching can be combined with
[JWT claim-based request templating](/victoriametrics/vmauth/#jwt-claim-based-request-templating)
for dynamic URL rewriting based on `vm_access` claim fields.

#### JWT claim-based request templating

`vmauth` can dynamically rewrite{{% available_from "v1.137.0" %}} upstream URLs and request headers using values from the JWT `vm_access` claim. 
This enables routing different users to different backends or tenants based solely on the JWT token, 
without maintaining separate user configs per tenant. In addition `vm_access` claim could be defined at `jwt` section with `default_vm_access_claim` {{% available_from "v1.147.0" %}}.
In this case, if JWT token doesn't have `vm_access` claim defined, value from `default_vm_access_claim` will be used for templaing.

Example: minimal valid JWT. If vm_access is empty, tenant `0:0` is assumed and no additional filters are applied.
```json
{
  "exp": 2770832322,
  "vm_access": {}
}
```

Example: complete JWT with `vm_access` claim defining explicit access rules for metrics and logs.

```json
{
  "exp": 1771953418,
  "vm_access": {
    "metrics_account_id": 1,
    "metrics_project_id": 2,
    "metrics_extra_labels": ["dev=team","env=prod"],
    "metrics_extra_filters": ["{env=~\"prod|dev\",team!=\"test\"}"],

    "logs_account_id": 2,
    "logs_project_id": 3,
    "logs_extra_filters": ["{\"namespace\":\"my-app\",\"env\":\"prod\"}"],
    "logs_extra_stream_filters": []
  }
}
```

Placeholders are written directly into `url_prefix` and `headers` values in the auth config. 
At request time each placeholder is replaced with the corresponding value from the `vm_access` claim of the incoming JWT token.

The following placeholders are supported:

| Placeholder                   | JWT claim field                                         |
|-------------------------------|---------------------------------------------------------|
| `{{.MetricsAccountID}}`       | `metrics_account_id` int                                |
| `{{.MetricsProjectID}}`       | `metrics_project_id` int                                |
| `{{.MetricsTenant}}` -> `0:0` | `metrics_account_id` int, <br/>`metrics_project_id` int |
| `{{.MetricsExtraLabels}}`     | `metrics_extra_labels` string array                     |
| `{{.MetricsExtraFilters}}`    | `metrics_extra_filters` string array                    |
| `{{.LogsAccountID}}`          | `logs_account_id` int                                   |
| `{{.LogsProjectID}}`          | `logs_project_id` int                                   |
| `{{.LogsExtraFilters}}`       | `logs_extra_filters` string array                       |
| `{{.LogsExtraStreamFilters}}` | `logs_extra_stream_filters` string array                |

Placeholders are supported in the following locations:

- **URL path** — only `{{.MetricsTenant}}`, `{{.LogsAccountID}}` and `{{.LogsProjectID}}` are allowed in path segments.
- **URL query parameters** — any placeholder may be used as the full value of a query parameter (e.g. `?extra_filters={{.MetricsExtraFilters}}`).
- **Request headers** — any placeholder may be used as the full value of a request header (e.g. `AccountID: {{.LogsAccountID}}`).

Placeholders are **not** supported in response headers. 
They are also only valid for JWT-authenticated users — using them in configs for `username`/`password` or `bearer_token` users causes a configuration error.

Example: default `vm_access` claim:

```yaml
users:
- jwt:
    default_vm_access_claim:
      metrics_account_id: 10
      metrics_project_id: 10
      metrics_extra_filters:
      - '{instance="sandbox"}'
      metrics_extra_labels:
      - team=dev
      - env=dev
    public_keys:
    - |
      -----BEGIN PUBLIC KEY-----
      MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...
      -----END PUBLIC KEY-----
  url_prefix: "http://vminsert:8480/insert/{{.MetricsAccountID}}:{{.MetricsProjectID}}/prometheus/?extra_filters={{.MetricsExtraFilters}}&extra_label={{.MetricsExtraLabels}}"
```


Example: route requests to the VictoriaMetrics single-node:

```yaml
users:
- jwt:
    public_keys:
    - |
      -----BEGIN PUBLIC KEY-----
      MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...
      -----END PUBLIC KEY-----
  url_prefix: "http://vminsert:8480/prometheus/?extra_filters={{.MetricsExtraFilters}}&extra_label={{.MetricsExtraLabels}}"
```

Example: route requests to the VictoriaMetrics cluster:

```yaml
users:
- jwt:
    public_keys:
    - |
      -----BEGIN PUBLIC KEY-----
      MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...
      -----END PUBLIC KEY-----
  url_map:
  - src_paths:
    - "/api/v1/write"
    url_prefix: "http://vminsert:8480/insert/{{.MetricsTenant}}/prometheus/"
  - src_paths:
    - "/api/v1/query"
    - "/api/v1/query_range"
    url_prefix: "http://vmselect:8481/select/{{.MetricsTenant}}/prometheus/"
```

Example: route requests to the VictoriaLogs cluster:

```yaml
users:
- jwt:
    public_keys:
      - |
        -----BEGIN PUBLIC KEY-----
        MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...
        -----END PUBLIC KEY-----
  headers:
  - "AccountID: {{.LogsAccountID}}"
  - "ProjectID: {{.LogsProjectID}}"
  url_map:
  - src_paths:
      - "/select/.*"
    url_prefix:
      - http://vlselect:9428
  - src_paths:
      - "/insert/.*"
    url_prefix:
      - http://vlinsert:9428
```

See also [Single sign-on (SSO)](#single-sign-on-sso), [authorization](#authorization), [security](#security), [routing](#routing) and [load balancing](#load-balancing) docs.

### Single sign-on (SSO)

`vmauth` supports [Single sign-on (SSO)](https://en.wikipedia.org/wiki/Single_sign-on){{% available_from "v1.153.0" %}}.
It works with any [OIDC-compliant](https://openid.net/developers/how-connect-works/) Identity Provider (IdP) such as Keycloak, Auth0, Okta, Google, Azure AD, etc.
It implements the [Authorization Code Flow](https://openid.net/specs/openid-connect-core-1_0.html#CodeFlowAuth):
when an unauthenticated browser request arrives `vmauth` shows a login page, redirects to the IdP,
receives an authorization code on callback, exchanges it for an ID token, and sets it as a session cookie.
Subsequent requests carry the cookie and are authorized by [JWT Token auth proxy](https://docs.victoriametrics.com/victoriametrics/vmauth/#jwt-token-auth-proxy).

Only `GET`/`HEAD` requests trigger the login page; other methods receive `401`.

The config has two parts: a top-level `sso` section for the login flow, and `users` entries with `jwt` for authorization:

```yaml
sso:
  - src_host: 'sso\.example\.com'
    oidc:
      issuer: 'https://identity-provider.com/realms/master'
      client_id: 'sso.example.com'
      client_secret: 'theClientSecret'
      scopes: ['openid', 'profile', 'email']
      cookie_secret: 'theCookieSecret1234567890'
      session_duration: '1h'
      # insecure: true  # set only for local dev over plain HTTP

users:
  - jwt:
      match_claims:
        iss: 'https://identity-provider.com/realms/master'
        aud: 'sso.example.com'
      oidc:
        issuer: 'https://identity-provider.com/realms/master'
    url_map:
      - src_paths:
          - "/.*"
        src_hosts:
          - 'sso\.example\.com'
        url_prefix: "http://vmsingle:8428"
```

The `sso` section fields:

- `src_host` — a regex matching the request hostname. SSO activates only for matching hosts. First match wins when multiple entries are defined.
- `oidc.issuer` — the OIDC provider issuer URL. `vmauth` fetches `{issuer}/.well-known/openid-configuration` for endpoint discovery. Must use HTTPS in production.
- `oidc.client_id` — the OAuth2 client ID registered with the IdP.
- `oidc.client_secret` — the OAuth2 client secret.
- `oidc.cookie_secret` — the secret (≥16 chars) for HMAC-signing the CSRF cookie. Generate with `openssl rand -base64 32`.
- `oidc.scopes` — the OAuth2 scopes. The `openid` scope is always included.
- `oidc.session_duration` — this caps session cookie lifetime. Actual `MaxAge` = min(`session_duration`, token `exp`). Go duration syntax, e.g., `10m`, `1h`. Defaults to `10m`.
- `oidc.default_redirect_url` — the redirect target after login if the original URL fails validation. Defaults to `/`.
- `oidc.auth_params` - additional query parameters for the [authentication request](https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest) sent to the IdP. See [SSO authentication request parameters](https://docs.victoriametrics.com/victoriametrics/vmauth/#sso-authentication-request-parameters).
- `oidc.insecure` — disables `Secure` cookie flag and uses HTTP callback URIs. Used for local dev only; when `vmauth` runs behind a TLS-terminating proxy, keep this `false`.

Register the following URL in your IdP as the Authorized redirect URI:

- `https://<vmauth-host>/_vmauth/sso/callback`

If vmauth runs with `-http.pathPrefix`, insert the prefix before `/_vmauth`. For example, `-http.pathPrefix=/metrics` gives:

- `https://<vmauth-host>/metrics/_vmauth/sso/callback`

The URI must match exactly, including scheme, host, port and path. For local development over HTTP, register the `http://` form instead.

After login, the ID token works as a standard JWT — all [JWT claim matching](https://docs.victoriametrics.com/victoriametrics/vmauth/#jwt-claim-matching) features apply. The `match_claims` must verify that the `aud` claim matches the SSO `client_id`. The JWT token is stored in the `_vmauth_sso` cookie in plain text.
If a user authenticates but no `users` entry matches their token claims, `vmauth` shows the login page with an "Access Denied" error message.

By default, the cookie token is not proxied to backends. To forward the ID token as an `Authorization: Bearer` header, set `proxy_cookie_authorization_token: Authorization` in the `jwt` user config.

#### SSO authentication request parameters

The `oidc.auth_params` map adds provider-specific query parameters to the authentication request sent to the IdP,
such as `prompt`, `login_hint` or the provider extensions listed below.
Parameters set by `vmauth` (`response_type`, `client_id`, `redirect_uri`, `scope`, `nonce` and `state`) can't be overridden.

These parameters are sent via the browser, so the user can modify or remove them. Use them to streamline the login page,
not to restrict access. Restrict access with `match_claims` on claims of the signed ID token instead.

[Google](https://developers.google.com/identity/openid-connect/openid-connect#authenticationuriparameters) - `hd` limits the account chooser
to accounts of the given Google Workspace domain. The `hd` claim of the ID token contains the user's domain:

```yaml
sso:
  - src_host: 'sso\.example\.com'
    oidc:
      issuer: 'https://accounts.google.com'
      client_id: 'theClientID.apps.googleusercontent.com'
      client_secret: 'theClientSecret'
      scopes: ['openid', 'email']
      cookie_secret: 'theCookieSecret1234567890'
      auth_params:
        hd: 'example.com'
        prompt: 'select_account'

users:
  - jwt:
      match_claims:
        iss: 'https://accounts.google.com'
        aud: 'theClientID.apps.googleusercontent.com'
        hd: 'example.com'
      oidc:
        issuer: 'https://accounts.google.com'
    url_prefix: "http://vmsingle:8428"
```

[Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols-oidc#send-the-sign-in-request) - `domain_hint` skips
the email-based discovery on the sign-in page and redirects federated users to their home realm.
Restrict sign-in to a single tenant by using the tenant-specific issuer, since `vmauth` verifies the `iss` claim:

```yaml
sso:
  - src_host: 'sso\.example\.com'
    oidc:
      issuer: 'https://login.microsoftonline.com/<tenant-id>/v2.0'
      # ...
      auth_params:
        domain_hint: 'example.com'
```

[Keycloak](https://www.keycloak.org/docs/latest/server_admin/index.html) - `kc_idp_hint` skips the Keycloak login page
and redirects the user to the identity provider with the given alias:

```yaml
sso:
  - src_host: 'sso\.example\.com'
    oidc:
      issuer: 'https://keycloak.example.com/realms/master'
      # ...
      auth_params:
        kc_idp_hint: 'github'
```

[Auth0](https://auth0.com/docs/api/authentication/authorization-code-flow/authorize-application) - `connection` sends the user directly
to the given connection, and `organization` selects the organization to log in to:

```yaml
sso:
  - src_host: 'sso\.example\.com'
    oidc:
      issuer: 'https://example.auth0.com/'
      # ...
      auth_params:
        connection: 'google-oauth2'
```

See also [authorization](#authorization), [security](#security), [routing](#routing) and [load balancing](#load-balancing) docs.

### Per-tenant authorization

The following [`-auth.config`](#auth-config) instructs proxying `insert` and `select` requests from the [Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication) user `tenant1` to the [tenant](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#multitenancy) `1`, while requests from the user `tenant2` are sent to tenant `2`:

```yaml
users:
- username: tenant1
  password: "***"
  url_map:
  - src_paths:
    - "/api/v1/write"
    url_prefix: "http://vminsert-backend:8480/insert/1/prometheus/"
  - src_paths:
    - "/api/v1/query"
    - "/api/v1/query_range"
    - "/api/v1/series"
    - "/api/v1/labels"
    - "/api/v1/label/.+/values"
    url_prefix: "http://vmselect-backend:8481/select/1/prometheus/"
- username: tenant2
  password: "***"
  url_map:
  - src_paths:
    - "/api/v1/write"
    url_prefix: "http://vminsert-backend:8480/insert/2/prometheus/"
  - src_paths:
    - "/api/v1/query"
    - "/api/v1/query_range"
    - "/api/v1/series"
    - "/api/v1/labels"
    - "/api/v1/label/.+/values"
    url_prefix: "http://vmselect-backend:8481/select/2/prometheus/"
```

See also [authorization](#authorization), [security](#security), [routing](#routing) and [load balancing](#load-balancing) docs.

### mTLS-based request routing

[Enterprise version of `vmauth`](https://docs.victoriametrics.com/victoriametrics/enterprise/) can be configured for routing requests
to different backends depending on the following [subject fields](https://en.wikipedia.org/wiki/Public_key_certificate#Common_fields) in the TLS certificate provided by client:

* `organizational_unit` aka `OU`
* `organization` aka `O`
* `common_name` aka `CN`

For example, the following [`-auth.config`](#auth-config) routes requests from clients with `organizational_unit: finance` TLS certificates to `http://victoriametrics-finance:8428` backend, while requests from clients with `organizational_unit: devops` TLS certificates are routed to `http://victoriametrics-devops:8428` backend:

```yaml
users:
- mtls:
    organizational_unit: finance
  url_prefix: "http://victoriametrics-finance:8428"
- mtls:
    organizational_unit: devops
  url_prefix: "http://victoriametrics-devops:8428"
```

[mTLS protection](#mtls-protection) must be enabled for mTLS-based routing.

See also [authorization](#authorization), [security](#security), [routing](#routing) and [load balancing](#load-balancing) docs.

### Enforcing query args

`vmauth` can be configured to add mandatory query arguments before proxying requests to backends.
For example, the following [config](#auth-config) adds [`extra_label`](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#prometheus-querying-api-enhancements) to all the requests, which are proxied to [single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/):

```yaml
unauthorized_user:
  url_prefix: "http://victoria-metrics:8428/?extra_label=foo=bar"
```

See also [authorization](#authorization), [security](#security), [routing](#routing) and [load balancing](#load-balancing) docs.
