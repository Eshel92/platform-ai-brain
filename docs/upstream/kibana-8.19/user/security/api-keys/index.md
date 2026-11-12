<!-- Converted from user/security/api-keys/index.asciidoc (AsciiDoc). Includes are inlined. -->

### API Keys

API keys are security mechanisms used to authenticate and authorize access to Elasticsearch resources. They ensure that only authorized users or applications interact with Elasticsearch.

For example, if you extract data from an Elasticsearch cluster on a daily basis, you might create an API key tied to your credentials, configure it with minimum access, and then put the API credentials into a cron job. Or you might create API keys to automate ingestion of new data from remote sources, without a live user interaction.

You can use Kibana to manage your different API keys:

* User API key: allows external services to access the Elastic Stack on behalf of a user.
* Cross-cluster API key: allows other clusters to connect to this cluster.
* Managed API key: created and managed by Kibana to run background tasks.

To manage API keys, go to the *API Keys* management page using the navigation menu or the 
global search field.

image:images/api-keys.png["API Keys UI"]

### Security privileges

* To use API keys in Kibana, you must have the `manage_security`, `manage_api_key`, or the `manage_own_api_key` cluster privileges.
* To delete API keys, you must have the `manage_api_key` or `manage_own_api_key` privileges.
* To create or update a *user API key*, you must have the `manage_api_key` or the `manage_own_api_key` privilege.
* To create or update a *cross-cluster API key*, you must have the `manage_security` privilege and an Enterprise license.
* To have a read-only view on the API keys, you must have access to the page and the `read_security` cluster privilege.

To manage roles, go to the *Roles* management page using the navigation menu or the 
global search field, or use the [role APIs](https://www.elastic.co/docs/api/doc/kibana/group/endpoint-roles).

### Create an API key

To create an API key, go to the *API Keys* management page using the navigation menu or the 
global search field, and select *Create API key*.

image:images/create-ccr-api-key.png["Create API Key UI"]

Refer to the [create API key](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/security-api-create-api-key.html) documentation to learn more about creating user API keys.

Refer to the [create cross-cluster API key](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/security-api-create-cross-cluster-api-key.html) documentation to learn more about creating cross-cluster API keys.

### Update an API key

To update an API key, go to the *API Keys* management page using the navigation menu or the 
global search field, and then click on the name of the key. You cannot update the name or the type of API key.

Refer to the [update API key](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/security-api-update-api-key.html) documentation to learn more about updating user API keys.

Refer to the [update cross-cluster API key](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/security-api-update-cross-cluster-api-key.html) documentation to learn more about updating cross-cluster API keys.

### View and delete API keys

The *API Keys* feature in Kibana lists your API keys, including the name, date created, and status. If an API key expires, its status changes from `Active` to `Expired`.

If you have `manage_security` or `manage_api_key` permissions, you can view the API keys of all users, and see which API key was created by which user in which realm.
If you have only the `manage_own_api_key` permission, you see only a list of your own keys.

You can delete API keys individually or in bulk, but you need the `manage_api_keys` or `manage_own_api_key` privileges.
