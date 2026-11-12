<!-- Part 1 of 6 of victoriametrics/vmauth.md (split because the page is big). -->

## Quick start

Just download the `vmutils-*` archive from [releases page](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest), unpack it, and pass the following flag to the `vmauth` binary in order to start authorizing and proxying requests:

```sh
/path/to/vmauth -auth.config=/path/to/auth/config.yml
```

The `-auth.config` command-line flag must point to a valid [config](#auth-config). See [use cases](#use-cases) with typical `-auth.config` examples.

`vmauth` accepts HTTP requests on port `8427` and proxies them according to the provided [-auth.config](#auth-config).
The port can be modified via the `-httpListenAddr` command-line flag.

See [how to reload config without restart](#config-reload).

Docker images for `vmauth` are available at [Docker Hub](https://hub.docker.com/r/victoriametrics/vmauth/tags) and [Quay](https://quay.io/repository/victoriametrics/vmauth?tab=tags).
See how `vmauth` is used in [docker-compose environment](https://github.com/VictoriaMetrics/VictoriaMetrics/blob/master/deployment/docker/README.md#victoriametrics-cluster).

Pass `-help` to `vmauth` in order to see all the supported command-line flags with their descriptions.

Feel free to [contact us](mailto:info@victoriametrics.com) if you need a customized auth proxy for VictoriaMetrics with the support of LDAP, SSO, RBAC, SAML, accounting, and rate limiting, such as [vmgateway](https://docs.victoriametrics.com/victoriametrics/vmgateway/).

> [VictoriaMetrics Cloud](https://console.victoriametrics.cloud/signUp?utm_source=website&utm_campaign=docs_vm_vmauth_access)
> provides built-in access control with organization-level roles, and lets you create and revoke read, write, or read/write access tokens with a couple of clicks from the UI, without the need of additional proxies.
> See the [VictoriaMetrics Cloud documentation](https://docs.victoriametrics.com/victoriametrics-cloud/) to get started.
