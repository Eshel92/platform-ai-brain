<!-- Converted from management/managing-licenses.asciidoc (AsciiDoc). Includes are inlined. -->

## License Management

By default, new installations have a Basic license that never expires. 
For the full list of features available at the Free and Open Basic subscription level, 
refer to {subscriptions}.

To explore all of the available solutions and features, start a 30-day free trial.
You can activate a trial subscription once per major product version. 
If you need more than 30 days to complete your evaluation, 
request an extended trial at {extendtrial}.

To view the status of your license, start a trial, or install a new
license, go to the *License Management* page using the navigation menu or the 
global search field.

### Required permissions

The `manage` cluster privilege is required to access *License Management*.

To add the privilege, go to the *Roles* management page using the navigation menu or the 
global search field.

### License expiration

Licenses are valid for a specific time period. 
30 days before the license expiration date, Elasticsearch starts logging expiration warnings.
If monitoring is enabled, expiration warnings are displayed prominently in Kibana.

If your license expires, your subscription level reverts to Basic and
you will no longer be able to use [Platinum or Enterprise features](https://www.elastic.co/subscriptions).

### Update your license

Licenses are provided as a _JSON_ file and have an effective date and an expiration date.  
You cannot install a new license before its effective date.
License updates take effect immediately and do not require restarting Elasticsearch.

You can update your license from *Stack Management > License Management* or through the
[update license API](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/update-license.html).
