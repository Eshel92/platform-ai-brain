<!-- Converted from rest-api/security/saml-sp-metadata.asciidoc (AsciiDoc). Includes are inlined. -->

### SAML service provider metadata API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Generate SAML metadata for a SAML 2.0 Service Provider.

#### Request

`GET /_security/saml/metadata/<realm_name>`

#### Description

The SAML 2.0 specification provides a mechanism for Service Providers to
describe their capabilities and configuration using a metadata file. This API
generates Service Provider metadata, based on the configuration of a SAML realm
in Elasticsearch.

#### Path parameters

`<realm_name>`::
  (Required, string) The name of the SAML realm in Elasticsearch.

#### Response body

`metadata`::
(string) An XML string that contains a SAML Service Provider's metadata for the realm.

#### Examples

The following example generates Service Provider metadata for
SAML realm `saml1`:

```console
GET /_security/saml/metadata/saml1
```
The API returns the following response containing the SAML metadata as an XML string:

```console-result
{
    "metadata" : "<?xml version=\"1.0\" encoding=\"UTF-8\"?><md:EntityDescriptor xmlns:md=\"urn:oasis:names:tc:SAML:2.0:metadata\" entityID=\"https://kibana.org\"><md:SPSSODescriptor AuthnRequestsSigned=\"false\" WantAssertionsSigned=\"true\" protocolSupportEnumeration=\"urn:oasis:names:tc:SAML:2.0:protocol\"><md:SingleLogoutService Binding=\"urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect\" Location=\"https://kibana.org/logout\"/><md:AssertionConsumerService Binding=\"urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST\" Location=\"https://kibana.org/api/security/saml/callback\" index=\"1\" isDefault=\"true\"/></md:SPSSODescriptor></md:EntityDescriptor>"
}
```
