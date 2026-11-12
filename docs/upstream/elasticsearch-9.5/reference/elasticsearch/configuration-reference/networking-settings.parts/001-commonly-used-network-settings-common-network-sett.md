<!-- Part 1 of 4 of reference/elasticsearch/configuration-reference/networking-settings.md (split because the page is big). -->

## Commonly used network settings [common-network-settings]

Most users will need to configure only the following network settings.

`network.host`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), string) Sets the address of this node for both HTTP and transport traffic. The node will bind to this address and will also use it as its publish address. Accepts an IP address, a hostname, or a [special value](#network-interface-values).

    Defaults to `_local_`. However, note that [security auto-configuration](docs-content://deploy-manage/deploy/self-managed/installing-elasticsearch.md) will add `http.host: 0.0.0.0` to your `elasticsearch.yml` configuration file, which overrides this default for HTTP traffic.


`http.port`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), integer) The port to bind for HTTP client communication. Accepts a single value or a range. If a range is specified, the node will bind to the first available port in the range.

    Defaults to `9200-9300`.


`transport.port`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), integer) The port to bind for communication between nodes. Accepts a single value or a range. If a range is specified, the node will bind to the first available port in the range. Set this setting to a single port, not a range, on every master-eligible node.

    Defaults to `9300-9400`.


$$$remote_cluster.port$$$

`remote_cluster.port`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), integer) The port to bind for remote cluster client communication. Accepts a single value.

    Defaults to `9443`.




## Special values for network addresses [network-interface-values]

You can configure Elasticsearch to automatically determine its addresses by using the following special values. Use these values when configuring `network.host`, `network.bind_host`, `network.publish_host`, and the corresponding settings for the HTTP and transport interfaces.

`_local_`
:   Any loopback addresses on the system, for example `127.0.0.1`.

`_site_`
:   Any site-local addresses on the system, for example `192.168.0.1`.

`_global_`
:   Any globally-scoped addresses on the system, for example `8.8.8.8`.

`_[networkInterface]_`
:   Use the addresses of the network interface called `[networkInterface]`. For example if you wish to use the addresses of an interface called `en0` then set `network.host: _en0_`.

`0.0.0.0`
:   The addresses of all available network interfaces.

::::{note}
In some systems these special values resolve to multiple addresses. If so, Elasticsearch will select one of them as its publish address and may change its selection on each node restart. Ensure your node is accessible at every possible address.
::::


::::{note}
Any values containing a `:` (e.g. an IPv6 address or some of the [special values](#network-interface-values)) must be quoted because `:` is a special character in YAML.
::::


### IPv4 vs IPv6 [network-interface-values-ipv4-vs-ipv6]

These special values yield both IPv4 and IPv6 addresses by default, but you can also add an `:ipv4` or `:ipv6` suffix to limit them to just IPv4 or IPv6 addresses respectively. For example, `network.host: "_en0:ipv4_"` would set this node’s addresses to the IPv4 addresses of interface `en0`.

::::{admonition} Discovery in the Cloud
:class: tip

More special settings are available when running in the Cloud with either the [EC2 discovery plugin](/reference/elasticsearch-plugins/discovery-ec2.md) or the [Google Compute Engine discovery plugin](/reference/elasticsearch-plugins/discovery-gce-network-host.md) installed.

::::





## Binding and publishing [modules-network-binding-publishing]

Elasticsearch uses network addresses for two distinct purposes known as binding and publishing. Most nodes will use the same address for everything, but more complicated setups may need to configure different addresses for different purposes.

When an application such as Elasticsearch wishes to receive network communications, it must indicate to the operating system the address or addresses whose traffic it should receive. This is known as *binding* to those addresses. Elasticsearch can bind to more than one address if needed, but most nodes only bind to a single address. Elasticsearch can only bind to an address if it is running on a host that has a network interface with that address. If necessary, you can configure the transport and HTTP interfaces to bind to different addresses.

Each Elasticsearch node has an address at which clients and other nodes can contact it, known as its *publish address*. Each node has one publish address for its HTTP interface and one for its transport interface. These two addresses can be anything, and don’t need to be addresses of the network interfaces on the host. The only requirements are that each node must be:

* Accessible at its HTTP publish address by all clients that will discover it using sniffing.
* Accessible at its transport publish address by all other nodes in its cluster, and by any remote clusters that will discover it using [sniff mode](docs-content://deploy-manage/remote-clusters/remote-clusters-self-managed.md#sniff-mode).

Each node must have its own distinct publish address.

If you specify the transport publish address using a hostname then Elasticsearch will resolve this hostname to an IP address once during startup, and other nodes will use the resulting IP address instead of resolving the name again themselves. You must use a hostname such that all of the addresses to which it resolves are addresses at which the node is accessible from all other nodes. To avoid confusion, it is simplest to use a hostname which resolves to a single address.

If you specify the transport publish address using a [special value](#network-interface-values) then Elasticsearch will resolve this value to a single IP address during startup, and other nodes will use the resulting IP address instead of resolving the value again themselves. You must use a value such that all of the addresses to which it resolves are addresses at which the node is accessible from all other nodes. To avoid confusion, it is simplest to use a value which resolves to a single address. It is usually a mistake to use `0.0.0.0` as a publish address on hosts with more than one network interface.

### Using a single address [_using_a_single_address]

The most common configuration is for Elasticsearch to bind to a single address at which it is accessible to clients and other nodes. To use this configuration, set only `network.host` to the desired address. Do not separately set any bind or publish addresses. Do not separately specify the addresses for the HTTP or transport interfaces.


### Using multiple addresses [_using_multiple_addresses]

Use the [advanced network settings](#advanced-network-settings) if you wish to bind Elasticsearch to multiple addresses, or to publish a different address from the addresses to which you are binding. Set `network.bind_host` to the bind addresses, and `network.publish_host` to the address at which this node is exposed. In complex configurations, you can configure these addresses differently for the HTTP and transport interfaces.




## Advanced network settings [advanced-network-settings]

These advanced settings let you bind to multiple addresses, or to use different addresses for binding and publishing. They are not required in most cases and you should not use them if you can use the [commonly used settings](#common-network-settings) instead.

`network.bind_host`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), string) The network address(es) to which the node should bind in order to listen for incoming connections. Accepts a list of IP addresses, hostnames, and [special values](#network-interface-values). Defaults to the address given by `network.host`. Use this setting only if binding to multiple addresses or using different addresses for publishing and binding.

`network.publish_host`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), string) The network address that clients and other nodes can use to contact this node. Accepts an IP address, a hostname, or a [special value](#network-interface-values). Defaults to the address given by `network.host`. Use this setting only if binding to multiple addresses or using different addresses for publishing and binding.

::::{note}
You can specify a list of addresses for `network.host` and `network.publish_host`. You can also specify one or more hostnames or [special values](#network-interface-values) that resolve to multiple addresses. If you do this then Elasticsearch chooses one of the addresses for its publish address. This choice uses heuristics based on IPv4/IPv6 stack preference and reachability and may change when the node restarts. Ensure each node is accessible at all possible publish addresses.
::::


### Advanced TCP settings [tcp-settings]

Use the following settings to control the low-level parameters of the TCP connections used by the HTTP and transport interfaces.

`network.tcp.keep_alive`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), boolean) Configures the `SO_KEEPALIVE` option for network sockets, which determines whether each connection sends TCP keepalive probes. Defaults to `true`.

`network.tcp.keep_idle`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), integer) Configures the `TCP_KEEPIDLE` option for network sockets, which determines the time in seconds that a connection must be idle before starting to send TCP keepalive probes. Defaults to `-1`, which means to use the system default. This value cannot exceed `300` seconds. Only applicable on Linux and macOS.

`network.tcp.keep_interval`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), integer) Configures the `TCP_KEEPINTVL` option for network sockets, which determines the time in seconds between sending TCP keepalive probes. Defaults to `-1`, which means to use the system default. This value cannot exceed `300` seconds. Only applicable on Linux and macOS.

`network.tcp.keep_count`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), integer) Configures the `TCP_KEEPCNT` option for network sockets, which determines the number of unacknowledged TCP keepalive probes that may be sent on a connection before it is dropped. Defaults to `-1`, which means to use the system default. Only applicable on Linux and macOS.

`network.tcp.no_delay`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), boolean) Configures the `TCP_NODELAY` option on network sockets, which determines whether [TCP no delay](https://en.wikipedia.org/wiki/Nagle%27s_algorithm) is enabled. Defaults to `true`.

`network.tcp.reuse_address`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), boolean) Configures the `SO_REUSEADDR` option for network sockets, which determines whether the address can be reused or not. Defaults to `false` on Windows and `true` otherwise.

`network.tcp.send_buffer_size`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), [byte value](/reference/elasticsearch/rest-apis/api-conventions.md#byte-units)) Configures the size of the TCP send buffer for network sockets. Defaults to `-1` which means to use the system default.

`network.tcp.receive_buffer_size`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting), [byte value](/reference/elasticsearch/rest-apis/api-conventions.md#byte-units)) Configures the size of the TCP receive buffer. Defaults to `-1` which means to use the system default.
