<!-- Converted from search/search-your-data/search-application-overview.asciidoc (AsciiDoc). Includes are inlined. -->

## Elastic Search Applications

_Search Applications_ enable users to build search-powered applications that leverage the full power of Elasticsearch and its Query DSL, with a simplified user experience.
Create search applications based on your Elasticsearch indices, build queries using search templates, and easily preview your results directly in the Kibana Search UI.

You can also interact with your search applications using the search-application-apis.
Search Applications are designed to simplify building unified search experiences across a range of enterprise search use cases, using the Elastic platform.

**Search Applications documentation**
****
Documentation for the Search Applications feature lives in two places:

* The documentation in this section covers the basics of Search Applications, information about working with Search Applications in the Kibana UI, and use case examples.
* The Elasticsearch API documentation contains the API references for working with Search Applications programmatically.
Jump there if you're only interested in the APIs.
****

### Availability and prerequisites

The Search Applications feature was introduced in Elastic version *8.8.0*.

**Note:**
Search Applications is a beta feature.
Beta features are subject to change and are not covered by the support SLA of general release (GA) features.
Elastic plans to promote this feature to GA in a future release.

This feature is available to all *Elastic Cloud* deployments.

This feature is also available to *self-managed* deployments when Elastic subscription requirements are satisfied.
View the requirements for this feature under the *Elastic Search* section of the [Elastic Stack subscriptions^](https://www.elastic.co/subscriptions) page.

Your deployment must include the Elasticsearch and Kibana services.

Managing search applications requires the `manage_search_application` cluster privilege, and also requires the `manage` index privilege on all indices associated with the search application.

### Overview

The Elasticsearch Query DSL is powerful and flexible, but it comes with a steep learning curve.
Complex queries are verbose and hard to understand for non-experts.
We've designed search applications to be easier to search over, but with the flexibility of working with an Elasticsearch index.

Search Applications use search templates to simplify the process of building queries.
Templates are defined when creating a search application, and can be customized according to your needs.
Read search-application-api for the details.

### Get started

#### Option 1: Get started in the UI

You can create build, and manage your search applications directly in the Kibana UI under *Search*.
Make sure you have at least one Elasticsearch index to work with on your deployment.
The indices underlying your search application are searched together, similar to how an alias searches over multiple indices.

To create a new search application in Kibana:

. Go to *Search > Search Applications*.
. Select *Create*.
. Select the Elasticsearch indices you want to use for your search application.
. Name your search application.
. Select *Create*.

Your search application should now be available in the list of search applications.

Once created, you can explore the documents in your search application under *Search > Search Applications >* _your-search-application_ > *Docs Explorer*.
From there, you can expand a matching Elasticsearch document to see its full contents.

#### Option 2: Get started with the API

Use the Elasticsearch Put Search Application API to create a search application.

The following example creates a search application named `my_search_application` that searches over the `my_search_index1` and `my_search_index2` indices, along with defining a simple search template (Refer to search-application-api-default-template).

```console
PUT /_application/search_application/my_search_application
{
  "indices": [ "my_search_index1", "my_search_index2" ],
  "template": {
    "script": {
      "source": {
        "query": {
          "query_string": {
            "query": "{{query_string}}",
            "default_field": "{{default_field}}"
          }
        }
      },
      "params": {
        "query_string": "*",
        "default_field": "*"
      }
    }
  }
}
```

#### Search templates

Search templates are the heart of your search applications.
The default template created for a search application is very minimal, and you'll want to customize it to suit your needs.
search-application-api contains a number of examples to get you started, including the default template, as well as templates for text search, semantic search and hybrid search.

(See `search/search-your-data/search-application-api.md`)
(See `search/search-your-data/search-application-security.md`)
(See `search/search-your-data/search-application-client.md`)
