<!-- Part 5 of 5 of reference/configuration.md (split because the page is big). -->

## Web Server

**`mms.centralUrl`**

*Type*: string

FQDN (fully qualified domain name) and port number of the Ops Manager Application.

To use a port other than `8080`, see
/tutorial/manage-ports.

```ini
mms.centralUrl=http://mms.example.com:8080
```

Corresponds to `URL to Access Ops Manager`.

**Important:**

If you plan on accessing your Ops Manager Application using its IPv6 (Internet Protocol version 6)
address, you must enclose the IPv6 (Internet Protocol version 6) address in square brackets
(`[ ]`) to separate it from its port number.

For example: 

```ini
http://[2600:1f16:777:8700:93c2:b99c:a875:2b10]:8080
```

**`mms.https.PEMKeyFile`**

*Type*: string

Absolute path to the PEM file that contains the Ops Manager Application's
valid certificate and private key. The PEM file is required if the
Ops Manager Application uses HTTPS (Hypertext Transfer Protocol Secure) to encrypt connections between the
Ops Manager Application, the agents, and the web interface.

The default port for HTTPS (Hypertext Transfer Protocol Secure) access to the Ops Manager Application is
`8443`, as set in `<install_dir>/conf/mms.conf` file. If you
change this default, you must also change the port specified in the
`mms.centralUrl` setting.

Corresponds to `HTTPS PEM Key File`.

**`mms.https.PEMKeyFilePassword`**

*Type*: string

Password for the HTTPS (Hypertext Transfer Protocol Secure) PEM key file. You must include this setting
if the PEM (Privacy-Enhanced Mail) key file contains an encrypted private key.

Corresponds to `HTTPS PEM Key File Password`.

**`mms.https.ClientCertificateMode`**

*Type*: string

Specifies if Ops Manager requires clients to present valid TLS (Transport Layer Security)/SSL (Secure Sockets Layer)
client certificates when connecting to it. Accepted values are:

- `none`
- `agents_only`
- `required`

Corresponds to `Client Certificate Mode`.

**`mms.https.CAFile`**

*Type*: string

Required if:

- You are using a private certificate authority.
- You set `mms.https.ClientCertificateMode` to
  `agents_only` or `required`.
- You run Ops Manager in hybrid mode with TLS (Transport Layer Security) enabled.

Specifies the filesystem location of a private certificate authority
file containing the list of acceptable client certificates. The
Ops Manager Application authenticates HTTPS (Hypertext Transfer Protocol Secure) requests from clients bearing a
certificate described in this file.

```ini
mms.https.CAFile=/path/to/ca_file.pem
```

Corresponds to `CA File`.

**`mms.https.dualConnectors`**

*Type*: boolean

*Default*: False

Enables connections to Ops Manager using HTTP (Hypertext Transfer Protocol) and HTTPS (Hypertext Transfer Protocol Secure) concurrently.

You can use this setting temporarily while you upgrade Ops Manager and the
MongoDB Agent\s to use TLS (Transport Layer Security). To ensure zero downtime, set to
`true` and provide a value for `mms.http.bindhostname`.
After you configure Ops Manager and the MongoDB Agent\s, set to `false`.

**Important:**

Ops Manager is accessible using insecure connections while
`mms.https.dualConnectors` is `true`.

Set `mms.https.dualConnectors` to `false` to allow secure
connections only after you have updated the MongoDB Agent\s to use
TLS (Transport Layer Security) connections.

**`mms.http.bindhostname`**

*Type*: string

*Default*: 127.0.0.1

The hostname or IP (Internet Protocol) at which MongoDB Agent\s can connect to
Ops Manager using HTTP (Hypertext Transfer Protocol).

You can use this setting temporarily while you upgrade Ops Manager and the
MongoDB Agent\s to use TLS (Transport Layer Security). To ensure zero downtime, set a value and
set `mms.https.dualConnectors` to `true`. After you
configure Ops Manager and the MongoDB Agent\s, remove the value.

**`mms.remoteIp.header`**

*Type*: string

If you use a load balancer with the Ops Manager Application, set this to the
HTTP (Hypertext Transfer Protocol) header field the load balancer uses to identify the
originating client's IP address to the Ops Manager host. When you
specify `Load Balancer Remote IP Header`, do not allow
clients to connect directly to any Ops Manager host. A load
balancer placed in front of the Ops Manager hosts must not
return cached content.

Once `Load Balancer Remote IP Header` is set, Ops Manager
enables the following HTTP (Hypertext Transfer Protocol) headers:

| HTTP (Hypertext Transfer Protocol) Header | Forwards to Ops Manager |
|---|---|
| X-Forwarded-Host | Original host that the client requested in the Host HTTP (Hypertext Transfer Protocol) request header. |
| X-Forwarded-Proto | Protocol used to make the HTTP (Hypertext Transfer Protocol) request. |
| [X-Forwarded-Server](https://www.eclipse.org/jetty/javadoc/current/org/eclipse/jetty/server/ForwardedRequestCustomizer.html) | Hostname of the proxy server. |
| [X-Proxied-Https](https://www.eclipse.org/jetty/javadoc/current/org/eclipse/jetty/server/ForwardedRequestCustomizer.html) | HTTPS (Hypertext Transfer Protocol Secure) status of a request. |

To learn more, see
/tutorial/configure-application-high-availability.

Corresponds to `Load Balancer Remote IP Header`.

**`mms.minimumTLSVersion`**

*Type*: string

*Default*: `TLSv1.2`

Specifies the TLS (Transport Layer Security) version required for clients to connect to Ops Manager.
This property affects all clients, such as browsers used to connect
to the Ops Manager Admin interface and command-line tools, such
as `curl`, used to connect to the REST (Representational State Transfer) API (Application Programming Interface).

Ops Manager versions between 4.0.9 and 4.0.18 and earlier than 4.2.13 and 4.4.0
  Ops Manager supports `TLSv1.2` only. If you change this value to
  anything other than `TLSv1.2`, including a blank value, you can't
  connect to this Ops Manager.

Ops Manager versions 4.0.0 to 4.0.8, 4.0.18 or later, 4.2.13 or later, 4.4.0 or later
  Ops Manager supports `TLSv1.0`, `TLSv1.1` and `TLSv1.2`.

**Note:**

TLSv1.2 requires connecting clients to meet the following minimum
requirements:

* Browser supports TLS (Transport Layer Security) version 1.2

* `curl` version 7.34.0+

* OpenSSL version 1.0.1+

To set `minimum.TLSVersion`, follow the Modify a Custom
Setting procedure with the following
values:

|  |  |
|---|---|
| Key | `minimum.TLSVersion` |
| Value | `<tls-versions>` |

**`mms.disableCiphers`**

*Type*: string

*Default*: `SSL_DHE_DSS_WITH_3DES_EDE_CBC_SHA`,
`SSL_DHE_DSS_WITH_DES_CBC_SHA`,
`SSL_DHE_RSA_EXPORT_WITH_DES40_CBC_SHA`,
`SSL_DHE_RSA_WITH_3DES_EDE_CBC_SHA`, `SSL_DHE_RSA_WITH_DES_CBC_SHA`,
`SSL_RSA_EXPORT_WITH_DES40_CBC_SHA`,
`SSL_RSA_EXPORT_WITH_RC4_40_MD5`,
`TLS_DHE_DSS_WITH_AES_128_CBC_SHA256`,
`TLS_DHE_DSS_WITH_AES_128_CBC_SHA`,
`TLS_DHE_DSS_WITH_AES_256_CBC_SHA256`,
`TLS_DHE_DSS_WITH_AES_256_CBC_SHA`,
`TLS_DHE_RSA_WITH_AES_128_CBC_SHA256`,
`TLS_DHE_RSA_WITH_AES_128_CBC_SHA`,
`TLS_DHE_RSA_WITH_AES_128_GCM_SHA256`,
`TLS_DHE_RSA_WITH_AES_256_CBC_SHA256`,
`TLS_DHE_RSA_WITH_AES_256_CBC_SHA`,
`TLS_DHE_RSA_WITH_AES_256_GCM_SHA384`,
`TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`,
`TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384`

Specifies a list of TLS (Transport Layer Security) cipher suites which your instance of Ops Manager
can't accept when clients connect to the Ops Manager Application and API (Application Programming Interface).
Specify TLS (Transport Layer Security) cipher suite names as a comma-separated list, as in
the following example.

**Important:**

Cipher suite names used in Ops Manager must follow RFC 5246 naming conventions. Do not use the OpenSSL
naming convention. For convenience, Ops Manager logs a list of all
supported cipher suite names during startup. If Ops Manager does not
recognize a TLS (Transport Layer Security) cipher suite name, it logs the following
warning:

Your config lists the following as ciphers which should be
disabled as the JDK (Java Development Kit) does not recognize them. Please check the
format of the entries and list of enabled ciphers.
[*unrecognized_cipher_name*]

To change `mms.disableCiphers`, follow the Modify a Custom
Setting procedure with the following
values:

* - Key
  - `mms.disableCiphers`
* - Value
  - `<ciphers>`

    For example:

    ```ini
    TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA, TLS_DHE_RSA_WITH_AES_256_CBC_SHA256
    ```

**Warning:**

Setting `mms.disableCiphers` to a custom value could
re-enable one or more of these disabled ciphers.


## Webhook

**`mms.alerts.webhook.adminEndpoint`**

*Type*: string

Corresponds to `Webhook URL`.

**`mms.alerts.webhook.adminSecret`**

*Type*: string

Corresponds to `Webhook Secret`.
