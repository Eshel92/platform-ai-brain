<!-- Converted from rest-api/security/enroll-kibana.asciidoc (AsciiDoc). Includes are inlined. -->

### Enroll Kibana API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Enables a Kibana instance to configure itself for communication with a secured Elasticsearch cluster.

**Note:** This API is currently intended for internal use only by Kibana.

#### Request

`GET /_security/enroll/kibana`

#### Description

Kibana uses this API internally to configure itself for communications with an
Elasticsearch cluster that already has security features enabled.

#### Examples

The following example shows how to enroll a Kibana instance.

```console
GET /_security/enroll/kibana
```

The API returns the following response:

```console_result
{
  "token" : {
    "name" : "enroll-process-token-1629123923000", <1>
    "value": "AAEAAWVsYXN0aWM...vZmxlZXQtc2VydmVyL3Rva2VuMTo3TFdaSDZ" <2>
  },
  "http_ca" : "MIIJlAIBAzVoGCSqGSIb3...vsDfsA3UZBAjEPfhubpQysAICAA=", <3>
}
```
<1> The name of the bearer token for the `elastic/kibana` service account.
<2> The value of the bearer token for the `elastic/kibana` service account.
Use this value to [authenticate the service account](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/service-accounts.html#authenticate-with-service-account-token) with Elasticsearch.
<3> The CA certificate used to sign the node certificates that Elasticsearch uses for TLS
on the HTTP layer. The certificate is returned as a Base64 encoded string of the
ASN.1 DER encoding of the certificate.
