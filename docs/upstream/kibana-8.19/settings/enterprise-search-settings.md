<!-- Converted from settings/enterprise-search-settings.asciidoc (AsciiDoc). Includes are inlined. -->

### Enterprise Search settings in Kibana

On Elastic Cloud, you do not need to configure any settings to use Enterprise Search in Kibana. It is enabled by default. On self-managed installations, you must configure `enterpriseSearch.host`.

`enterpriseSearch.host`::
The http(s) URL of your Enterprise Search instance. For example, in a local self-managed setup,
set this to `http://localhost:3002`. Authentication between Kibana and the Enterprise Search host URL,
such as via OAuth, is not supported. You can also
{enterprise-search-ref}/configure-ssl-tls.html#configure-ssl-tls-in-kibana[configure Kibana to trust
your Enterprise Search TLS certificate authority].

`enterpriseSearch.accessCheckTimeout`::
When launching the Enterprise Search UI, the maximum number of milliseconds for Kibana to wait
for a response from Enterprise Search
before considering the attempt failed and logging a warning.
Default: 5000.

`enterpriseSearch.accessCheckTimeoutWarning`::
When launching the Enterprise Search UI, the maximum number of milliseconds for Kibana to wait for a response from
Enterprise Search before logging a warning. Default: 300.
