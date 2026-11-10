<!-- Converted from search/search-your-data/behavioral-analytics/behavioral-analytics-event.asciidoc (AsciiDoc). Includes are inlined. -->

### View Behavioral Analytics events

**Tip:**
Refer to behavioral-analytics-event-reference for a complete list of the fields logged by events.

Once you've started *tracking events* using the [Behavioral Analytics Tracker^](https://github.com/elastic/behavioral-analytics-tracker/tree/main#readme), you can view them on a pre-built dashboard in Kibana.

#### View events in the Overview dashboard

The *Overview* dashboard provides a quick overview of the following:

* Searches
* No results
* Clicks
* Sessions

This allows you to quickly check both absolute numbers and trends (tracked in percentage changes) about these events.
Find this dashboard under *Search > Behavioral Analytics>* _your-collection_ *> Overview*.

The following screenshot shows an example *Overview* dashboard:

(Figure: images/analytics-overview-dashboard.png)

#### View events in the Explorer dashboard

The *Explorer* dashboard provides a more detailed view of your events.
Find this dashboard under *Search > Behavioral Analytics>* _your-collection_ *> Explorer*.

Here you can find and search over the following:

* Search terms
* Top clicked results
* No results
* Locations
* Referrers

You can also easily sort in ascending or descending order by clicking on the header arrows.

The following screenshot shows the *Locations* tab of an *Explorer* dashboard, with a list of top locations in descending order:

(Figure: images/analytics-explorer-dashboard.png)

#### Discover and Lens

For more detailed analysis, you can view events in the Kibana [Discover^](https://www.elastic.co/guide/en/kibana/8.19/discover.html) app.
The Behavioral Analytics UI will guide you here from the *Explorer* dashboard.
You can dig into the details using Discover and then generate visualizations using [Lens^](https://www.elastic.co/guide/en/kibana/8.19/lens.html).

Discover works with [data views^](https://www.elastic.co/guide/en/kibana/8.19/data-views.html).
You'll find a data view automatically created for your collection, named `behavioral_analytics.events-<your-collection>`.
This data view will be pre-selected in the data view dropdown menu.
Use this menu to switch between data views for different collections.

The following screenshot shows you where to find the data view dropdown menu in Discover:

(Figure: images/discover-data-view-analytics.png)

Discover has a lot of options, but here's a quick overview of how to get started:

* Filter your data by searching for terms, such as `search`, `page_view`, and `search_click`.
You'll see a time series of hits that match your search.
* Search for "event" in the field name search bar.
For example:
** Select `event.action`.
You'll find a list of all the events you've sent and their frequency distribution.
* Search for `search.query` to find all search queries.
* Select *Visualize* to create a Lens visualization.

The following screenshot shows a Lens visualization of an `event.action` distribution:
(Figure: images/discover-lens-analytics.png)

##### Learn more

Read the [Discover documentation^](https://www.elastic.co/guide/en/kibana/8.19/discover.html).

Read the [Lens documentation^](https://www.elastic.co/guide/en/kibana/8.19/lens.html).
