<!-- Converted from rest-api/security/enroll-node.asciidoc (AsciiDoc). Includes are inlined. -->

### Enroll Node API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Allows a new node to join an existing cluster with security features enabled.

#### Request

`GET /_security/enroll/node`

#### Description

The purpose of the enroll node API is to allow a new node to join an existing cluster
where security is enabled. The enroll node API response contains all the necessary information
for the joining node to bootstrap discovery and security related settings so that it
can successfully join the cluster.

**Note:** The response contains key and certificate material that allows the
caller to generate valid signed certificates for the HTTP layer of all nodes in the cluster.

#### Examples

```console
GET /security/enroll/node
```
The API returns a response such as

```console-result
{
  "http_ca_key" : "MIIJlAIBAzCCCVoGCSqGSIb3DQEHAaCCCUsEgglHMIIJQzCCA98GCSqGSIb3DQ....vsDfsA3UZBAjEPfhubpQysAICCAA=", <1>
  "http_ca_cert" : "MIIJlAIBAzCCCVoGCSqGSIb3DQEHAaCCCUsEgglHMIIJQzCCA98GCSqGSIb3DQ....vsDfsA3UZBAjEPfhubpQysAICCAA=", <2>
  "transport_ca_cert" : "MIIJlAIBAzCCCVoGCSqGSIb3DQEHAaCCCUsEgglHMIIJQzCCA98GCSqG....vsDfsA3UZBAjEPfhubpQysAICCAA=", <3>
  "transport_key" : "MIIEJgIBAzCCA98GCSqGSIb3DQEHAaCCA9AEggPMMIIDyDCCA8QGCSqGSIb3....YuEiOXvqZ6jxuVSQ0CAwGGoA==", <4>
  "transport_cert" : "MIIEJgIBAzCCA98GCSqGSIb3DQEHAaCCA9AEggPMMIIDyDCCA8QGCSqGSIb3....YuEiOXvqZ6jxuVSQ0CAwGGoA==", <5>
  "nodes_addresses" : [                          <6>
    "192.168.1.2:9300"
  ]
}
```
<1> The CA private key that can be used by the new node in order to sign its certificate
    for the HTTP layer, as a Base64 encoded string of the ASN.1 DER encoding of the key.
<2> The CA certificate that can be used by the new node in order to sign its certificate
    for the HTTP layer, as a Base64 encoded string of the ASN.1 DER encoding of the certificate.
<3> The CA certificate that is used to sign the TLS certificate for the transport layer, as
    a Base64 encoded string of the ASN.1 DER encoding of the certificate.
<4> The private key that the node can use for TLS for its transport layer, as a Base64 encoded
    string of the ASN.1 DER encoding of the key.
<5> The certificate that the node can use for TLS for its transport layer, as a Base64 encoded
    string of the ASN.1 DER encoding of the certificate.
<6> A list of transport addresses in the form of `host:port` for the nodes that are already
    members of the cluster.
