<!-- Converted from management/cases/manage-cases.asciidoc (AsciiDoc). Includes are inlined. -->

## Open and manage cases

To perform these tasks, you must have full access to the appropriate case features in Kibana.

### Open a new case

Open a new case to keep track of issues and share their details with colleagues.

. Go to *Management > {stack-manage-app} > Cases*, then click *Create case*.
(Figure: images/cases-create.png)

. If you defined templates, you can optionally select one to use its default field values. preview:[]

. Give the case a name, severity, and description.
**Tip:** In the `Description` area, you can use
[Markdown](https://www.markdownguide.org/cheat-sheet) syntax to create formatted
text.

. Optionally, add a category, assignees, and tags.
You can add users only if they meet the necessary prerequisites.

. If you defined any custom fields, they appear in the *Additional fields* section. added:[8.15.0]

. For the *External incident management system*, select a connector. For more
information, refer to case-connectors.

. After you've completed all of the required fields, click *Create case*.

preview:[] Alternatively, you can configure your rules to automatically create cases by using case actions.
By default, the rule adds all of the alerts within a specified time window to a single case.
You can optionally choose a field to group the alerts and create separate cases for each group.
You can also choose whether you want the rule to reopen cases or open new ones when the time window elapses.

### Add email notifications

You can configure email notifications that occur when users are assigned to
cases.

For hosted Kibana on Elasticsearch Service:

. Add the email domains to the {cloud}/ec-organizations-notifications-domain-allowlist.html[notifications domain allowlist].
You do not need to take any more steps to configure an email connector or update
Kibana user settings, since the preconfigured Elastic-Cloud-SMTP connector is
used by default.

For self-managed Kibana:

. Create a preconfigured email connector.
**Note:** At this time, email notifications support only preconfigured connectors,
which are defined in the `kibana.yml` file.
For examples, refer to preconfigured-email-configuration and configuring-email.
. Set the `notifications.connectors.default.email` Kibana setting in kibana.yml to the name of
your email connector.
```js
notifications.connectors.default.email: ‘mail-dev’

xpack.actions.preconfigured:
  mail-dev:
    name: preconfigured-email-notification-maildev
    actionTypeId: .email
    config:
      service: other
      from: from address
      host: host name
      port: port number
      secure: true/false
      hasAuth: true/false
```

. If you want the email notifications to contain links back to the case, you
must configure the server.publicBaseUrl setting.

When you subsequently add assignees to cases, they receive an email.

### Add files

After you create a case, you can upload and manage files on the *Files* tab:

(Figure: images/cases-files.png)

The acceptable file types and sizes are affected by your case settings.

To download or delete the file or copy the file hash to your clipboard, open the action menu (…).
The available hash functions are MD5, SHA-1, and SHA-256.

When you upload a file, a comment is added to the case activity log.
To view images, click their name in the activity or file list.

============================================================================
Uploaded files are also accessible in *{stack-manage-app} > Files*.
When you export cases as saved objects, the case files are not exported.
============================================================================

### Add visualizations

You can also optionally add visualizations.
For example, you can portray event and alert data through charts and graphs.

(Figure: images/cases-visualization.png)

To add a visualization to a comment within your case:

. Click the *Visualization* button. The *Add visualization* dialog appears.

. Select an existing visualization from your Visualize Library or create a new
visualization.
**Important:** Set an absolute time range for your visualization. This ensures your
visualization doesn't change over time after you save it to your case and
provides important context for viewers.

. After you've finished creating your visualization, click *Save and return* to
go back to your case.

. Click *Preview* to see how the visualization will appear in the case comment.

. Click *Add Comment* to add the visualization to your case.

Alternatively, while viewing a dashboard you can open a panel's menu then click *More > Add to existing case* or *More > Add to new case*.

After a visualization has been added to a case, you can modify or interact with it by clicking the *Open Visualization* option in the case's comment menu.

### Manage cases

In *Management > {stack-manage-app} > Cases*, you can search cases and filter
them by attributes such as assignees, categories, severity, status, and tags. You can also
select multiple cases and use bulk actions to delete cases or change their
attributes.

To view a case, click on its name. You can then:

* Add a new comment.
* Edit existing comments and the description.
* Add or remove assignees.
* Add a connector.
* Send updates to external systems (if external connections are configured).
* Edit the category and tags.
* Refresh the case to retrieve the latest updates.
* Change the status.
* Change the severity.
* Close or delete the case.
* Reopen a closed case.
