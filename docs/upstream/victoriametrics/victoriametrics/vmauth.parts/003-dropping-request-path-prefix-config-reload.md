<!-- Part 3 of 6 of victoriametrics/vmauth.md (split because the page is big). -->

## Dropping request path prefix

By default, `vmauth` doesn't strip the path prefix from the original request when proxying it to the matching backend.
Sometimes it is needed to drop the path prefix before proxying the request to the backend. This can be done by specifying the number of `/`-delimited prefix parts to drop from the request path via `drop_src_path_prefix_parts` option at `url_map` level or at `user` level or [`-auth.config`](#auth-config).

For example, if you need to serve requests to [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/) at `/vmalert/` path prefix, while serving requests to [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/) at `/vmagent/` path prefix,
then the following [-auth.config](#auth-config) can be used:

```yaml
unauthorized_user:
  url_map:

    # proxy all the requests, which start with `/vmagent/`, to the vmagent backend
  - src_paths:
    - "/vmagent/.*"

    # drop /vmagent/ path prefix from the original request before proxying it to url_prefix.
    drop_src_path_prefix_parts: 1
    url_prefix: "http://vmagent-backend:8429/"

    # proxy all the requests, which start with `/vmalert`, to the vmalert backend
  - src_paths:
    - "/vmalert/.*"

    # drop /vmalert/ path prefix from the original request before proxying it to url_prefix.
    drop_src_path_prefix_parts: 1
    url_prefix: "http://vmalert-backend:8880/"
```


## Authorization

`vmauth` supports the following authorization mechanisms:

* [No authorization](https://docs.victoriametrics.com/victoriametrics/vmauth/#simple-http-proxy)
* [Basic Auth](https://docs.victoriametrics.com/victoriametrics/vmauth/#basic-auth-proxy)
* [Bearer token](https://docs.victoriametrics.com/victoriametrics/vmauth/#bearer-token-auth-proxy)
* [JWT token](https://docs.victoriametrics.com/victoriametrics/vmauth/#jwt-token-auth-proxy)
* [Client TLS certificate verification aka mTLS](https://docs.victoriametrics.com/victoriametrics/vmauth/#mtls-based-request-routing)
* [Auth tokens via Arbitrary HTTP request headers](https://docs.victoriametrics.com/victoriametrics/vmauth/#reading-auth-tokens-from-other-http-headers)

See also [authorization](#authorization), [security](#security), [routing](#routing) and [load balancing](#load-balancing) docs.


## Routing

`vmauth` can proxy requests to different backends depending on the following parts of the HTTP request:

* [Request path](#routing-by-path)
* [Request host](#routing-by-host)
* [Request query arg](#routing-by-query-arg)
* [HTTP request header](#routing-by-header)
* [Multiple parts](#routing-by-multiple-parts)

See also [authorization](#authorization) and [load balancing](#load-balancing).
For debug purposes, extra logging for failed requests can be enabled by setting `dump_request_on_errors: true` {{% available_from "v1.107.0" %}} on the user level. Please note that such logging may expose sensitive information and should be used only for debugging.

### Routing by path

`src_paths` option can be specified inside `url_map` in order to route requests by path.

The following [`-auth.config`](#auth-config) routes requests to paths starting with `/app1/` to `http://app1-backend`,
while requests with paths starting with `/app2` are routed to `http://app2-backend`, and the rest of the requests
are routed to `http://some-backend/404-page.html`:

```yaml
unauthorized_user:
  url_map:
  - src_paths:
    - "/app1/.*"
    url_prefix: "http://app1-backend/"
  - src_paths:
    - "/app2/.*"
    url_prefix: "http://app2-backend/"
  default_url: http://some-backend/404-page.html
```

`src_paths` accepts a list of [regular expressions](https://github.com/google/re2/wiki/Syntax). The incoming request is routed to the given `url_prefix` if **the whole** requested path matches at least one `src_paths` entry.

See also [how to drop request path prefix](#dropping-request-path-prefix).

### Denying paths

`deny_paths` inside `url_map` rejects a subset of paths matched by `src_paths` (or the other `src_*` options) so you don't have to enumerate every allowed path:

```yaml
unauthorized_user:
  url_map:
  - src_paths:
    - "/select/.*"
    deny_paths:
    - "/select/[^/]+/prometheus/api/v1/status/active_queries"
    - "/select/[^/]+/prometheus/api/v1/status/active_queries/"
    url_prefix: "http://vmselect:8481"
```

A request matching `deny_paths` is rejected with `403 Forbidden` (or `401 Unauthorized` for anonymous requests). It can't be used on its own, it needs at least one of `src_paths`, `src_hosts`, `src_query_args` or `src_headers` in the same `url_map` entry.

### Routing by host

`src_hosts` option can be specified inside `url_map` in order to route requests by host header.

The following [`-auth.config`](#auth-config) routes requests to `app1.my-host.com` host to `http://app1-backend`, while routing requests to `app2.my-host.com` host to `http://app2-backend`, and the rest of the requests are routed to `http://some-backend/404-page.html`:

```yaml
unauthorized_user:
  url_map:
  - src_hosts:
    - "app1\\.my-host\\.com"
    url_prefix: "http://app1-backend/"
  - src_hosts:
    - "app2\\.my-host\\.com"
    url_prefix: "http://app2-backend/"
  default_url: http://some-backend/404-page.html
```

`src_hosts` accepts a list of [regular expressions](https://github.com/google/re2/wiki/Syntax). The incoming request is routed to the given `url_prefix` if **the whole** request host matches at least one `src_hosts` entry.

### Routing by query arg

`src_query_args` option can be specified inside `url_map` in order to route requests by the given [query arg](https://en.wikipedia.org/wiki/Query_string).

For example, the following [`-auth.config`](#auth-config) routes requests to `http://app1-backend/` if `db=foo` query arg is present in the request, while routing requests with `db` query arg starting with `bar` to `http://app2-backend`, and the rest of the requests are routed to `http://some-backend/404-page.html`:

```yaml
unauthorized_user:
  url_map:
  - src_query_args: ["db=foo"]
    url_prefix: "http://app1-backend/"
  - src_query_args: ["db=~bar.*"]
    url_prefix: "http://app2-backend/"
  default_url: http://some-backend/404-page.html
```

`src_query_args` accepts a list of strings in the format `arg=value` or `arg=~regex`.
The `arg=value` format means exact matching of **the whole** `arg` query arg value to the given `value`.
The `arg=~regex` format means regex matching of **the whole** `arg` query arg value to the given `regex`.
If at least a single query arg in the request matches at least one `src_query_args` entry, then the request is routed to the given `url_prefix`.

### Routing by header

`src_headers` option can be specified inside `url_map` in order to route requests by the given HTTP request header.

For example, the following [`-auth.config`](#auth-config) routes requests to `http://app1-backend` if `TenantID` request header equals to `42`, while routing requests to `http://app2-backend` if `TenantID` request header equals to `123:456`, and the rest of the requests are routed to `http://some-backend/404-page.html`:

```yaml
unauthorized_user:
  url_map:
  - src_headers: ["TenantID: 42"]
    url_prefix: "http://app1-backend/"
  - src_headers: ["TenantID: 123:456"]
    url_prefix: "http://app2-backend/"
  default_url: http://some-backend/404-page.html
```

If `src_headers` contains multiple entries, then it is enough to match only a single entry in order to route the request to the given `url_prefix`.

### Routing by multiple parts

Any subset of [`src_paths`](#routing-by-path), [`src_hosts`](#routing-by-host), [`src_query_args`](#routing-by-query-arg) and [`src_headers`](#routing-by-header) options can be specified simultaneously in a single `url_map` entry. In this case, the request is routed to the given `url_prefix` if the request matches all the provided configs **simultaneously**.

For example, the following [`-auth.config`](#auth-config) routes requests to `http://app1-backend` if all the conditions mentioned below are simultaneously met:

* the request path starts with `/app/`
* the requested hostname ends with `.bar.baz`
* the request contains `db=abc` query arg
* the `TenantID` request header equals `42`

```yaml
unauthorized_user:
  url_map:
  - src_paths: ["/app/.*"]
    src_hosts: [".+\\.bar\\.baz"]
    src_query_args: ["db=abc"]
    src_headers: ["TenantID: 42"]
    url_prefix: "http://app1-backend/"
```


## Load balancing

Each `url_prefix` in the [-auth.config](#auth-config) can be specified in the following forms:

* A single URL. For example:

  ```yaml
  unauthorized_user:
    url_prefix: 'http://vminsert:8480/insert/0/prometheus/`
  ```

  In this case, `vmauth` proxies requests to the specified URL.

* A list of URLs. For example:

  ```yaml
  unauthorized_user:
    url_prefix:
    - 'http://vminsert-1:8480/insert/0/prometheus/'
    - 'http://vminsert-2:8480/insert/0/prometheus/'
    - 'http://vminsert-3:8480/insert/0/prometheus/'
  ```

  In this case, `vmauth` spreads requests among the specified URLs using the least-loaded round-robin policy.
  This guarantees that incoming load is shared uniformly among the specified backends.
  See also [discovering backend IPs](#discovering-backend-ips).

  `vmauth` automatically detects temporarily unavailable backends and spreads incoming requests among the remaining available backends.
  This allows restarting and performing maintenance on backends without removing them from the `url_prefix` list.
  If all backends are marked as unavailable, requests are proxied to the first configured backend in the list instead of failing immediately.

  By default, `vmauth` returns backend responses with all the HTTP status codes to the client. It is possible to configure automatic retry of requests at other backends if the backend responds with a status code specified in the `-retryStatusCodes` command-line flag.
  It is possible to customize the list of HTTP response status codes to retry via the `retry_status_codes` list at the `user` and `url_map` level of [`-auth.config`](#auth-config).
  For example, the following config retries requests on other backends if the current backend returns a response with `500` or `502` HTTP status code:

  ```yaml
  unauthorized_user:
    url_prefix:
    - http://vmselect1:8481/
    - http://vmselect2:8481/
    - http://vmselect3:8481/
    retry_status_codes: [500, 502]
  ```

  By default, `vmauth` uses the `least_loaded` policy to distribute incoming requests across available backends.
  The policy can be changed to `first_available` via the `-loadBalancingPolicy` command-line flag. In this case, `vmauth` sends all the requests to the first specified backend while it is available. `vmauth` starts sending requests to the next specified backend when the first backend is temporarily unavailable.
  It is possible to customize the load-balancing policy at the `user` and `url_map` levels.
  For example, the following config specifies a `first_available` load balancing policy for unauthorized requests:

  ```yaml
  unauthorized_user:
    url_prefix:
    - http://victoria-metrics-main:8428/
    - http://victoria-metrics-standby:8428/
    load_balancing_policy: first_available
  ```

The load balancing feature can be used in the following cases:

* Balancing the load among multiple `vmselect` and/or `vminsert` nodes in [VictoriaMetrics cluster](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/).
  The following [`-auth.config`](#auth-config) can be used to spread incoming requests among 3 vmselect nodes and retrying failed requests or requests with 500 and 502 response status codes:

  ```yaml
  unauthorized_user:
    url_prefix:
    - http://vmselect1:8481/
    - http://vmselect2:8481/
    - http://vmselect3:8481/
    retry_status_codes: [500, 502]
  ```

* Sending select queries to the closest availability zone (AZ), while falling back to other AZs with identical data if the closest AZ is unavailable.
  For example, the following [`-auth.config`](#auth-config) sends select queries to `https://vmselect-az1/` and uses the `https://vmselect-az2/` as a fallback when `https://vmselect-az1/` is temporarily unavailable or cannot return full responses.
  See [these docs](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#cluster-availability) for details about the `deny_partial_response` query arg, which is added to requests before they are proxied to backends.

  ```yaml
  unauthorized_user:
    url_prefix:
    - https://vmselect-az1/?deny_partial_response=1
    - https://vmselect-az2/?deny_partial_response=1
    retry_status_codes: [500, 502, 503]
    load_balancing_policy: first_available
  ```

Load balancing can be configured independently for each `user` entry and for each `url_map` entry. See [auth config docs](#auth-config) for more details.

See also [discovering backend IPs](#discovering-backend-ips), [authorization](#authorization) and [routing](#routing).


## Discovering backend IPs

By default, `vmauth` distributes load across the backends listed under `url_prefix`, as described in the [load balancing docs](#load-balancing).
Sometimes multiple backend instances can be hidden behind a single hostname. For example, `vmselect-service` hostname
may point to a cluster of `vmselect` instances in [VictoriaMetrics cluster setup](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#architecture-overview).
So the following config may fail to spread load among available `vmselect` instances, since `vmauth` will send all the requests to the same URL, which may end up with a single backend instance:

```yaml
unauthorized_user:
  url_prefix: http://vmselect-service/select/0/prometheus/
```

There are the following solutions for this issue:

* To enumerate every `vmselect` hostname or IP in the `url_prefix` list:

  ```yaml
  unauthorized_user:
    url_prefix:
    - http://vmselect-1:8481/select/0/prometheus/
    - http://vmselect-2:8481/select/0/prometheus/
    - http://vmselect-3:8481/select/0/prometheus/
  ```

  This scheme works great, but it requires manual updating of the [`-auth.config`](#auth-config) whenever `vmselect` services are restarted, downscaled, or upscaled.

* To set `discover_backend_ips: true` option, so `vmauth` automatically discovers IPs behind the given hostname and then spreads load among the discovered IPs:

  ```yaml
  unauthorized_user:
    url_prefix: http://vmselect-service:8481/select/0/prometheus/
    discover_backend_ips: true
  ```

  If the `url_prefix` contains a hostname with `srv+` prefix, then the hostname without `srv+` prefix is automatically resolved via [DNS SRV](https://en.wikipedia.org/wiki/SRV_record) to the list of hostnames with TCP ports, and `vmauth` balances load among the discovered TCP addresses:

  ```yaml
  unauthorized_user:
    url_prefix: "http://srv+vmselect/select/0/prometheus"
    discover_backend_ips: true
  ```

  This functionality is useful for balancing load across backend instances running on different TCP ports, since DNS SRV records include TCP ports.

  The `discover_backend_ips` option can be specified at `user` and `url_map` level in the [`-auth.config`](#auth-config). It can also be enabled globally via the `-discoverBackendIPs` command-line flag.

See also [load balancing docs](#load-balancing).


## SRV URLs

If `url_prefix` contains a URL with the hostname starting with `srv+` prefix, then `vmauth` uses [DNS SRV](https://en.wikipedia.org/wiki/SRV_record) lookup for the hostname without the `srv+` prefix and selects a random TCP address (e.g., hostname plus TCP port) from the resolved results.

For example, if `some-addr` [DNS SRV](https://en.wikipedia.org/wiki/SRV_record) record contains `some-host:12345` TCP address,
then `url_prefix: http://srv+some-addr/some/path` is automatically resolved into `url_prefix: http://some-host:12345/some/path`.
DNS SRV resolution is performed whenever a new connection to the `url_prefix` backend is established.

See also [discovering backend addresses](#discovering-backend-ips).


## Modifying HTTP headers

`vmauth` supports setting and removing HTTP request headers before sending requests to backends.
This is done via the `headers` option. For example, the following [`-auth.config`](#auth-config) sets `TenantID: foobar` header to requests proxied to `http://backend:1234/`. It also overrides the `X-Forwarded-For` request header with an empty value. This effectively removes the `X-Forwarded-For` header from requests proxied to `http://backend:1234/`:

```yaml
unauthorized_user:
  url_prefix: "http://backend:1234/"
  headers:
  - "TenantID: foobar"
  - "X-Forwarded-For:"

users:
  - username: "foo"
    password: "bar"
    # dump request details on errors (can contain sensitive information)
    dump_request_on_errors: true
    url_map:
      - src_paths: ["/select/.*"]
        headers:
          - "AccountID: 1"
          - "ProjectID: 0"
        url_prefix:
          - "http://backend:9428/"
```

`vmauth` also supports setting and removing HTTP response headers before returning the response from the backend to the client.
This is done via the `response_headers` option. For example, the following [`-auth.config`](#auth-config) sets `Foo: bar` response header
and removes the `Server` response header before returning the response to the client:

```yaml
unauthorized_user:
  url_prefix: "http://backend:1234/"
  response_headers:
  - "Foo: bar"
  - "Server:"
```

See also [`Host` header docs](#host-http-header).


## Host HTTP header

By default, `vmauth` sets the `Host` HTTP header to the backend hostname when proxying requests to the corresponding backend.
Sometimes it is needed to keep the original `Host` header from the client request sent to `vmauth`. For example, if backends use host-based routing.
In this case, set `keep_original_host: true`. For example, the following config instructs to use the original `Host` header from client requests when proxying requests to the `backend:1234`:

```yaml
unauthorized_user:
  url_prefix: "http://backend:1234/"
  keep_original_host: true
```

It is also possible to set the `Host` header to an arbitrary value when proxying the request to the configured backend, via [`headers` option](#modifying-http-headers):

```yaml
unauthorized_user:
  url_prefix: "http://backend:1234/"
  headers:
  - "Host: foobar"
```


## Config reload

`vmauth` supports dynamic reload of [`-auth.config`](#auth-config) via the following ways:

* By sending `SIGHUP` signal to `vmauth` process:

  ```sh
  kill -HUP `pidof vmauth`
  ```

* By sending an HTTP GET request to the `/-/reload` endpoint. We recommend protecting it with `-reloadAuthKey`. See [security](#security) for details.
* By passing the interval for config check to the `-configCheckInterval` command-line flag.
