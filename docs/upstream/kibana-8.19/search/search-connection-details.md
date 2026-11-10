<!-- Converted from search/search-connection-details.asciidoc (AsciiDoc). Includes are inlined. -->

## Find your connection details

To connect to your Elasticsearch deployment, you need either a Cloud ID or an Elasticsearch endpoint, depending on the
deployment type you use. For secure connections, it’s recommended to use an API key for authentication.

* Learn how to find your Cloud ID for Elastic Cloud or self-hosted deployments.
* Learn how to create an API key for Elastic Cloud or self-hosted deployments.  
* Learn how to find your Elasticsearch endpoint or Cloud ID for a serverless deployment.  
* Learn how to create an API key for a serverless deployment.

### Elastic Cloud and self-hosted deployments

#### Find your Cloud ID

. Navigate to the Elastic Cloud home page.
. In the main menu, click *Manage this deployment*.
(Figure: manage-deployment.png)
. The Cloud ID is displayed on the right side of the page.
(Figure: cloud-id.png)

#### Create an API key

. To navigate to *API keys*, use the *global search bar*.
(Figure: api-keys-search-bar.png)
. Click *Create API key*.
(Figure: click-create-api-key.png)
. Enter the API key details, and click *Create API key*.
. Copy and securely store the API key, as it will not be shown again.

### Serverless deployments

#### Find your Elasticsearch endpoint

. Navigate to the serverless project's home page.
. Scroll down to the *Copy your connection details* section, and copy the *Elasticsearch endpoint*.
(Figure: serverless-connection-details.png)

**Note:**
The *Cloud ID* is also displayed in the Copy your connection details section, which you can use with specific client libraries and connectors.

#### Create an API key

. Navigate to the serverless project's home page.
. Scroll down to the *Add an API Key* section, and click *New*.
(Figure: serverless-create-an-api-key.png)
. Enter the API key details, and click *Create API key*.
. Copy and securely store the API key, as it will not be shown again.
