<!-- Converted from management/connectors/action-types/servicenow-itom.asciidoc (AsciiDoc). Includes are inlined. -->

## {sn-itom} connector and action

The {sn-itom} connector uses the
[event API](https://docs.servicenow.com/bundle/rome-it-operations-management/page/product/event-management/task/send-events-via-web-service.html)
to create {sn} events. You can use the connector for rule actions.

### Create connectors in Kibana

You can create connectors in *{stack-manage-app} > {connectors-ui}*
or as needed when you're creating a rule. You must choose whether to use OAuth for authentication.

(Figure: management/connectors/images/servicenow-itom-connector-basic.png)

(Figure: management/connectors/images/servicenow-itom-connector-oauth.png)

#### Connector configuration

{sn-itom} connectors have the following configuration properties:

Client ID::
The client identifier assigned to your OAuth application.
Client secret:: 
The client secret assigned to your OAuth application.
JWT verifier key ID::
The key identifier assigned to the JWT verifier map of your OAuth application.
Password::
The password for HTTP basic authentication.
Private key::
The RSA private key that you created for use in ServiceNow.
Private key password::
The password for the RSA private key.
This value is required when you set a password for your private key.
{sn} instance URL::
The full URL for the {sn} instance.
Use OAuth authentication::
By default, basic authentication is used instead of open authorization (OAuth).
User identifier::
The identifier to use for OAuth type authentication.
This identifier should be the user field you selected when you created an OAuth JWT API endpoint for external clients in your ServiceNow instance.
For example, if the selected user field is `Email`, the user identifier should be the user's email address.
Username::
The username for HTTP basic authentication.

### Test connectors

You can test connectors as you're creating or editing the connector in Kibana. For example:

(Figure: management/connectors/images/servicenow-itom-params-test.png)

{sn-itom} actions have the following configuration properties.

Description::
The details about the event.
Message key::
All actions sharing this key are associated with the same {sn} alert. The default value is `{{rule.id}}:{{alert.id}}`.
Metric name::
The name of the metric.
Node::
The host that the event was triggered for.
Resource::
The name of the resource.
Severity::
The severity of the event.
Source::
The name of the event source type.
Source instance::
A specific instance of the source.
Type::
The type of event.

Refer to [{sn} documentation](https://docs.servicenow.com/bundle/rome-it-operations-management/page/product/event-management/task/send-events-via-web-service.html) for more information about the properties.

### Connector networking configuration

Use the Action configuration settings to customize connector networking configurations, such as proxies, certificates, or TLS settings. You can set configurations that apply to all your connectors or use `xpack.actions.customHostSettings` to set per-host configurations.

### Configure {sn-itom}

{sn} offers free [Personal Developer Instances](https://developer.servicenow.com/dev.do#!/guides/madrid/now-platform/pdi-guide/obtaining-a-pdi), which you can use to test incidents.

#### Prerequisites

. Create a {sn} integration user and assign it the appropriate roles.
. If you use open authorization (OAuth), you must also:
.. Create an RSA keypair and add an X.509 Certificate.
.. Create an OAuth JWT API endpoint for external clients with a JWT Verifiers Map.

#### Create a {sn} integration user

To ensure authenticated communication between Elastic and {sn}, create a {sn} integration user and assign it the appropriate roles.

. In your {sn} instance, go to *System Security -> Users and Groups -> Users*.
. Click *New*.
. Complete the form, then right-click on the menu bar and click *Save*.
. Go to the *Roles* tab and click *Edit*.
. Assign the integration user the following roles:
* `personalize_choices`: Allows the user to retrieve Choice element options, such as Severity.
* `evt_mgmt_integration`: Enables integration with external event sources by allowing the user to create events.
. Click *Save*.

#### Create an RSA keypair and add an X.509 Certificate

This step is required to use OAuth for authentication between Elastic and {sn}.

*Create an RSA keypair:*

. Use [OpenSSL](https://www.openssl.org/docs/man1.0.2/man1/genrsa.html) to generate an RSA private key.
** To create a private key with a password, use the `passout` option. For example:
```sh
openssl genrsa -passout pass:foobar -out example-private-key-with-password.pem 3072
```
** To create a private key without a password, omit the `passout` option. For example:
```sh
openssl genrsa -out example-private-key.pem 3072
```

. Use [OpenSSL](https://www.openssl.org/docs/man1.0.2/man1/req.html) to generate the matching public key:
```sh
openssl req -new -x509 -key example-private-key.pem -out example-sn-cert.pem -days 360
```
*Add an X.509 certificate to ServiceNow:*

. In your {sn} instance, go to *Certificates* and select *New*.
. Configure the certificate as follows:
* *Name*: Name the certificate.
* *PEM Certificate*: Copy the generated public key into this text field.

(Figure: management/connectors/images/servicenow-new-certificate.png)

. Click *Submit* to create the certificate.

#### Create an OAuth JWT API endpoint for external clients with a JWT Verifiers Map

This step is required to use OAuth for authentication between Elastic and {sn}.

. In your {sn} instance, go to *Application Registry* and select *New*.
. Select *Create an OAuth JWT API endpoint for external clients* from the list of options.
(Figure: management/connectors/images/servicenow-jwt-endpoint.png)

. Configure the application as follows:
* *Name*: Name the application.
* *User field*: Select the field to use as the user identifier.

(Figure: management/connectors/images/servicenow-new-application.png)

**Important:** Remember the selected user field. You will use this as the *User Identifier Value* when creating the connector. For example, if you selected *Email* for *User field*, you will use the user's email for the *User Identifier Value*.

. Click *Submit* to create the application. You will be redirected to the list of applications.
. Select the application you just created.
. Find the *Jwt Verifier Maps* tab and click *New*.
. Configure the new record as follows:
* *Name*: Name the JWT Verifier Map.
* *Sys certificate*: Click the search icon and select the name of the certificate created in the previous step.

(Figure: management/connectors/images/servicenow-new-jwt-verifier-map.png)

. Click *Submit* to create the verifier map.
. Note the *Client ID*, *Client Secret* and *JWT Key ID*. You will need these values to create your {sn} connector.
(Figure: management/connectors/images/servicenow-oauth-values.png)
