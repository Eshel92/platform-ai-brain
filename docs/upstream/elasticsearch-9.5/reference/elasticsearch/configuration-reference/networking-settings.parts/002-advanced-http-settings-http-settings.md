<!-- Part 2 of 4 of reference/elasticsearch/configuration-reference/networking-settings.md (split because the page is big). -->

## Advanced HTTP settings [http-settings]

Use the following advanced settings to configure the HTTP interface independently of the [transport interface](#transport-settings). You can also configure both interfaces together using the [network settings](#common-network-settings).

`http.host`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), string) Sets the address of this node for HTTP traffic. The node will bind to this address and will also use it as its HTTP publish address. Accepts an IP address, a hostname, or a [special value](#network-interface-values). Use this setting only if you require different configurations for the transport and HTTP interfaces.

    Defaults to the address given by `network.host`. However, note that [security auto-configuration](docs-content://deploy-manage/deploy/self-managed/installing-elasticsearch.md) will add `http.host: 0.0.0.0` to your `elasticsearch.yml` configuration file, which overrides this default.


`http.bind_host`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), string) The network address(es) to which the node should bind in order to listen for incoming HTTP connections. Accepts a list of IP addresses, hostnames, and [special values](#network-interface-values). Defaults to the address given by `http.host` or `network.bind_host`. Use this setting only if you require to bind to multiple addresses or to use different addresses for publishing and binding, and you also require different binding configurations for the transport and HTTP interfaces.

`http.publish_host`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), string) The network address for HTTP clients to contact the node using sniffing. Accepts an IP address, a hostname, or a [special value](#network-interface-values). Defaults to the address given by `http.host` or `network.publish_host`. Use this setting only if you require to bind to multiple addresses or to use different addresses for publishing and binding, and you also require different binding configurations for the transport and HTTP interfaces.

`http.publish_port`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), integer) The port of the [HTTP publish address](#modules-network-binding-publishing). Configure this setting only if you need the publish port to be different from `http.port`. Defaults to the port assigned via `http.port`.

`http.max_content_length`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), [byte value](/reference/elasticsearch/rest-apis/api-conventions.md#byte-units)) Maximum size of an HTTP request body. If the body is compressed, the limit applies to the HTTP request body size before compression. Defaults to `100mb`. Configuring this setting to greater than `100mb` can cause cluster instability and is not recommended. If you hit this limit when sending a request to the [Bulk](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-bulk) API, configure your client to send fewer documents in each bulk request. If you wish to index individual documents that exceed `100mb`, pre-process them into smaller documents before sending them to Elasticsearch. For instance, store the raw data in a system outside Elasticsearch and include a link to the raw data in the documents that Elasticsearch indexes.

`http.max_initial_line_length`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), [byte value](/reference/elasticsearch/rest-apis/api-conventions.md#byte-units)) Maximum size of an HTTP URL. Defaults to `4kb`.

`http.max_header_size`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), [byte value](/reference/elasticsearch/rest-apis/api-conventions.md#byte-units)) Maximum size of allowed headers. Defaults to `16kb`.

$$$http-compression$$$

`http.compression` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), boolean) Support for compression when possible (with Accept-Encoding). If HTTPS is enabled, defaults to `false`. Otherwise, defaults to `true`.

    Disabling compression for HTTPS mitigates potential security risks, such as a [BREACH attack](https://en.wikipedia.org/wiki/BREACH). To compress HTTPS traffic, you must explicitly set `http.compression` to `true`.


`http.compression_level`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), integer) Defines the compression level to use for HTTP responses. Valid values are in the range of 1 (minimum compression) and 9 (maximum compression). Defaults to `3`.

$$$http-cors-enabled$$$

`http.cors.enabled` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), boolean) Enable or disable cross-origin resource sharing, which determines whether a browser on another origin can execute requests against Elasticsearch. Set to `true` to enable Elasticsearch to process pre-flight [CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) requests. Elasticsearch will respond to those requests with the `Access-Control-Allow-Origin` header if the `Origin` sent in the request is permitted by the `http.cors.allow-origin` list. Set to `false` (the default) to make Elasticsearch ignore the `Origin` request header, effectively disabling CORS requests because Elasticsearch will never respond with the `Access-Control-Allow-Origin` response header.

    ::::{note}
    If the client does not send a pre-flight request with an `Origin` header or it does not check the response headers from the server to validate the `Access-Control-Allow-Origin` response header, then cross-origin security is compromised. If CORS is not enabled on Elasticsearch, the only way for the client to know is to send a pre-flight request and realize the required response headers are missing.
    ::::


$$$http-cors-allow-origin$$$

`http.cors.allow-origin` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), string) Which origins to allow. If you prepend and append a forward slash (`/`) to the value, this will be treated as a regular expression, allowing you to support HTTP and HTTPs. For example, using `/https?:\/\/localhost(:[0-9]+)?/` would return the request header appropriately in both cases. Defaults to no origins allowed.

    ::::{important}
    A wildcard (`*`) is a valid value but is considered a security risk, as your Elasticsearch instance is open to cross origin requests from **anywhere**.
    ::::


$$$http-cors-max-age$$$

`http.cors.max-age` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), integer) Browsers send a "preflight" OPTIONS-request to determine CORS settings. `max-age` defines for how long, in seconds, the result should be cached. Defaults to `1728000` (20 days).

$$$http-cors-allow-methods$$$

`http.cors.allow-methods` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), string) Which methods to allow. Defaults to `OPTIONS, HEAD, GET, POST, PUT, DELETE`.

$$$http-cors-allow-headers$$$

`http.cors.allow-headers` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), string) Which headers to allow. Defaults to `X-Requested-With, Content-Type, Content-Length, Authorization, Accept, User-Agent, X-Elastic-Client-Meta`.

$$$http-cors-expose-headers$$$

`http.cors.expose-headers` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Which response headers to expose in the client. Defaults to `X-elastic-product`.

$$$http-cors-allow-credentials$$$

`http.cors.allow-credentials` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), boolean) Whether the `Access-Control-Allow-Credentials` header should be returned. Defaults to `false`.

    ::::{note}
    This header is only returned when the setting is set to `true`.
    ::::


`http.detailed_errors.enabled`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), boolean) Configures whether detailed error reporting in HTTP responses is enabled. Defaults to `true`. When this option is set to `false`, only basic information is returned if an error occurs in the request, and requests with [`?error_trace` parameter](/reference/elasticsearch/rest-apis/common-options.md#common-options-error-options) set are rejected.

`http.pipelining.max_events`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), integer) The maximum number of events to be queued up in memory before an HTTP connection is closed, defaults to `10000`.

`http.max_warning_header_count`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), integer) The maximum number of warning headers in client HTTP responses. Defaults to `-1` which means the number of warning headers is unlimited.

`http.max_warning_header_size`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), [byte value](/reference/elasticsearch/rest-apis/api-conventions.md#byte-units)) The maximum total size of warning headers in client HTTP responses. Defaults to `-1` which means the size of the warning headers is unlimited.

`http.tcp.keep_alive`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), boolean) Configures the `SO_KEEPALIVE` option for this socket, which determines whether it sends TCP keepalive probes. Defaults to `network.tcp.keep_alive`.

`http.tcp.keep_idle`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), integer) Configures the `TCP_KEEPIDLE` option for HTTP sockets, which determines the time in seconds that a connection must be idle before starting to send TCP keepalive probes. Defaults to `network.tcp.keep_idle`, which uses the system default. This value cannot exceed `300` seconds. Only applicable on Linux and macOS.

`http.tcp.keep_interval`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), integer) Configures the `TCP_KEEPINTVL` option for HTTP sockets, which determines the time in seconds between sending TCP keepalive probes. Defaults to `network.tcp.keep_interval`, which uses the system default. This value cannot exceed `300` seconds. Only applicable on Linux and macOS.

`http.tcp.keep_count`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), integer) Configures the `TCP_KEEPCNT` option for HTTP sockets, which determines the number of unacknowledged TCP keepalive probes that may be sent on a connection before it is dropped. Defaults to `network.tcp.keep_count`, which uses the system default. Only applicable on Linux and macOS.

`http.tcp.no_delay`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), boolean) Configures the `TCP_NODELAY` option on HTTP sockets, which determines whether [TCP no delay](https://en.wikipedia.org/wiki/Nagle%27s_algorithm) is enabled. Defaults to `true`.

`http.tcp.reuse_address`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), boolean) Configures the `SO_REUSEADDR` option for HTTP sockets, which determines whether the address can be reused or not. Defaults to `false` on Windows and `true` otherwise.

`http.tcp.send_buffer_size`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), [byte value](/reference/elasticsearch/rest-apis/api-conventions.md#byte-units)) The size of the TCP send buffer for HTTP traffic. Defaults to `network.tcp.send_buffer_size`.

`http.tcp.receive_buffer_size`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), [byte value](/reference/elasticsearch/rest-apis/api-conventions.md#byte-units)) The size of the TCP receive buffer for HTTP traffic. Defaults to `network.tcp.receive_buffer_size`.

`http.client_stats.enabled`
:   ([Dynamic](docs-content://deploy-manage/stack-settings.md#dynamic-cluster-setting), boolean) Enable or disable collection of HTTP client stats. Defaults to `true`.

`http.client_stats.closed_channels.max_count`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), integer) When `http.client_stats.enabled` is `true`, sets the maximum number of closed HTTP channels for which Elasticsearch reports statistics. Defaults to `10000`.

`http.client_stats.closed_channels.max_age`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), [time value](/reference/elasticsearch/rest-apis/api-conventions.md#time-units)) When `http.client_stats.enabled` is `true`, sets the maximum length of time after closing a HTTP channel that Elasticsearch will report that channel’s statistics. Defaults to `5m`.

### HTTP client configuration [_http_client_configuration]

::::{include} _snippets/http-client-configuration.md
::::
