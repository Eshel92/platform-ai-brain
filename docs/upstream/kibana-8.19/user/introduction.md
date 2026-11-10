<!-- Converted from user/introduction.asciidoc (AsciiDoc). Includes are inlined. -->

## Kibana&mdash;your window into Elastic

Kibana enables you to give
shape to your data and navigate the Elastic Stack.  With Kibana, you can:

* *Search, observe, and protect your data.*
From discovering documents to analyzing logs to finding security vulnerabilities,
Kibana is your portal for accessing these capabilities and more.

* *Analyze your data.*
Search for hidden insights, visualize what you've found in charts, gauges,
maps, graphs, and more, and combine them in a dashboard.

* *Manage, monitor, and secure the Elastic Stack.*
Manage your data, monitor the health of your
Elastic Stack cluster, and control which users have access to
which features.

(Figure: images/analytics-home-page.png)

*Kibana is for administrators, analysts, and business users.*
As an admin, your role is to manage the Elastic Stack, from creating your
deployment to getting Elasticsearch data into Kibana, and then
managing the data.  As an analyst, you're looking to discover insights
in the data, visualize your data on dashboards, and share your findings.  As a business user,
you want to view existing dashboards and drill down into details.

*Kibana works with all types of data.* Your data can be structured or unstructured text,
numerical data, time series data, geospatial data, logs, metrics, security events,
and more.
No matter your data, Kibana can help you uncover patterns and relationships and visualize the results.

### Search, observe, and protect

Being able to search, observe, and protect your data is a requirement for any analyst.
Kibana provides solutions for each of these use cases.

* [*Enterprise Search*](https://www.elastic.co/guide/en/enterprise-search/current/index.html) enables you to create a search experience for your app, workplace, and website.

* {observability-guide}/observability-introduction.html[*Elastic Observability*] enables you to monitor and apply analytics in real time
to events happening across all your environments. You can analyze log events, monitor the performance metrics for the host or container
that it ran in, trace the transaction, and check the overall service availability.

* Designed for security analysts, {security-guide}/es-overview.html[*Elastic Security*] provides an overview of
the events and alerts from your environment.  Elastic Security helps you defend
your organization from threats before damage and loss occur.

### Analyze

With Kibana *Analytics*, you can quickly search through large amounts
of data, explore fields and values,
and then use the drag-and-drop interface to rapidly build charts, tables, metrics, and more.

(Figure: images/visualization-journey.png)

|===

| *1*
| *Add data.* The best way to add data to the Elastic Stack is to use one of our many integrations.
On the **Integrations** page, you can also find options to add sample data sets or to upload a file.

| *2*
| *Explore.* With *Discover*, you can search your data for hidden
insights and relationships. Ask your questions, and then filter the results to just the data you want.
You can limit your results to the most recent documents added to Elasticsearch.

| *3*
| *Visualize.* Kibana provides many options to create visualizations of your data, from
aggregation-based data to time series data to geo data.
*Dashboard* is your starting point to create visualizations,
and then pulling them together to show your data from multiple perspectives.
Use *Canvas*,
to give your data
the “wow” factor for display on a big screen. Use *Graph* to explore patterns and relationships.

| *4*
| *Model data behavior.*
Use *Machine learning* to model the behavior of your data&mdash;forecast unusual behavior and
perform outlier detection, regression, and classification analysis.

| *5*
| *Share.* Ready to share your findings with a larger audience? Kibana offers many options&mdash;embed
a dashboard, share a link, export to PDF, and more.
|===

### Manage your data

Kibana helps you perform your data management tasks from the convenience of a UI. You can:

* Refresh, flush, and clear the cache of your indices.
* Define the lifecycle of an index as it ages.
* Define a policy for taking snapshots of your cluster.
* Roll up data from one or more indices into a new, compact index.
* Replicate indices on a remote cluster and copy them to a local cluster.

For a full list of data management UIs, refer to *Stack Management*.

(Figure: images/stack-management.png)

### Alert and take action

Detecting and acting on significant shifts and signals in your data is a need
that exists in almost every use case. Alerting allows you to
detect conditions in different Kibana apps and trigger actions when those conditions are met.
For example, you might trigger an alert when a shift occurs in your business critical KPIs or when
memory, CPU, or disk space take a dip.
When the alert triggers, you can send a notification to a system that is part of your daily workflow:
email, Slack, PagerDuty, ServiceNow, and other third party integrations.

A dedicated view for creating, searching,
and editing rules is in *{rules-ui}*.

### Organize content

You might be managing tens, hundreds, or even thousands of dashboards, visualizations, and other Kibana assets.
Kibana has several features for keeping your content organized.

#### Collect related items in a space

Kibana provides spaces for organizing your visualizations, dashboards, {data-sources}, and more.
Think of a space as its own mini Kibana installation&mdash;it’s isolated from all other spaces,
so you can tailor it to your specific needs without impacting others.

(Figure: images/select-your-space.png)

#### Organize your content with tags

Tags are keywords or labels that you assign to saved objects,
such as dashboards and visualizations, so you can classify them in a way that is meaningful to you.
For example, if you tag objects with “design”, you can search and
filter on the tag to see all related objects.
Tags are also good for grouping content into categories within a space.

Don’t worry if you have hundreds of dashboards that need to be tagged. Use *Tags*
in *Stack Management* to create your tags, then assign and delete
them in bulk operations.

### Secure Kibana

Kibana offers a range of security features for you to control who has access to what.
[Security is enabled automatically](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/configuring-stack-security.html) when you enroll Kibana with a secured Elasticsearch cluster.
For a description of all available configuration options,
refer to Security settings in Kibana.

#### Log in

Kibana supports several authentication providers,
allowing you to login using Elasticsearch’s built-in realms, or with your own single sign-on provider.

(Figure: security/images/kibana-login.png)

#### Secure access

Kibana provides roles and privileges for controlling which users can
view and manage Kibana features. Privileges grant permission to view an application
or perform a specific action and are assigned to roles. Roles allow you to describe
a “template” of capabilities that you can grant to many users,
without having to redefine what each user should be able to do.

When you create a role, you can scope the assigned Kibana privileges to specific spaces.
This makes it possible to grant users different access levels in different spaces,
or even give users their very own private space. For example, power users might
have privileges to create and edit visualizations and dashboards,
while analysts or executives might have *Dashboard* and *Canvas* with read-only privileges.

The Kibana role management interface allows you to describe these various access
levels, or you can automate role creation by using [role APIs](https://www.elastic.co/docs/api/doc/kibana/group/endpoint-roles).

(Figure: spaces/images/spaces-roles.png)

#### Audit access

Once you have your users and roles configured, you might want to maintain a
record of who did what, when. The Kibana audit log will record this information for you,
which can then be correlated with Elasticsearch audit logs to gain more insights into your
users’ behavior. For more information, see Kibana audit logging.

### Find apps and objects

To quickly find apps and the objects you create, use the search field in the global header.
Search suggestions include deep links into applications,
allowing you to directly navigate to the views you need most.

(Figure: images/app-navigation-search.png)

You can search for objects by type, name, and tag.
To get the most from the search feature, follow these tips:

* Use the keyboard shortcut&mdash;Ctrl/ on Windows and Linux, Command/ on MacOS&mdash;to focus on the input at any time.

* Use the provided syntax keywords.
|===
|Search by type
|`type:dashboard`

Available types: `application`, `canvas-workpad`, `dashboard`, `data-view`, `lens`, `maps`, `query`, `search`, `visualization`

|Search by tag
|`tag:mytagname` +
`tag:"tag name with spaces"`

|Search by type and name
|`type:dashboard my_dashboard_title`

|Advanced&nbsp;searches
|`tag:(tagname1 or tagname2) my_dashboard_title` +
`type:lens tag:(tagname1 or tagname2)` +
`type:(dashboard or canvas-workpad) logs` +
|===

This example searches for visualizations with the tag `design` .

(Figure: images/tags-search.png)

### View all Kibana has to offer

To view the full list of apps and features, go to [Kibana features](https://www.elastic.co/kibana/features).

### Get help

Click image:images/intro-help-icon.png[Help icon in navigation bar]
for help with questions or to provide feedback.

To keep up with what’s new and changed in Elastic, click the celebration icon in the global header.
