<!-- Converted from search/search-your-data/behavioral-analytics/behavioral-analytics-cors.asciidoc (AsciiDoc). Includes are inlined. -->

### Set up CORS for Behavioral Analytics

Behavioral Analytics sends events directly to the Elasticsearch API.
This means that the browser makes requests to the Elasticsearch API directly.
Elasticsearch supports [Cross-Origin Resource Sharing (CORS)^](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS), but this feature is disabled by default.
Therefore the browser will block these requests.

There are two workarounds for this:

* Enable CORS on Elasticsearch
* Proxy the request through a server that supports CORS

#### Enable CORS on Elasticsearch

This is the simplest option.
Enable CORS on Elasticsearch by adding the following to your `elasticsearch.yml` file:

```yaml
http.cors.allow-origin: "*" # Only use unrestricted value for local development
# Use a specific origin value in production, like `http.cors.allow-origin: "https://<my-website-domain.example>"`
http.cors.enabled: true
http.cors.allow-credentials: true
http.cors.allow-methods: OPTIONS, POST
http.cors.allow-headers: X-Requested-With, X-Auth-Token, Content-Type, Content-Length, Authorization, Access-Control-Allow-Headers, Accept
```

On Elastic Cloud, you can do this by {cloud}/ec-add-user-settings.html#ec-add-user-settings[editing your Elasticsearch user settings].

. From your deployment menu, go to the *Edit* page.
. In the *Elasticsearch* section, select *Manage user settings and extensions*.
. Update the user settings with the configuration above.
. Select *Save changes*.

#### Proxy the request through a server that supports CORS

If you are unable to enable CORS on Elasticsearch, you can proxy the request through a server that supports CORS.
This is more complicated, but is a viable option.
