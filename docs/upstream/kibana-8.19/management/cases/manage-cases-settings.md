<!-- Converted from management/cases/manage-cases-settings.asciidoc (AsciiDoc). Includes are inlined. -->

## Configure case settings

To change case closure options and add custom fields, templates, and connectors for external incident management systems, go to *{stack-manage-app} > Cases* and click *Settings*.

To perform these tasks, you must have full access to the appropriate case and connector features in Kibana.

(Figure: images/cases-settings.png)

### Case closures

If you close cases in your external incident management system, they will remain open in *Cases* until you close them manually.

To change whether cases are automatically closed after they are sent to an external system, update the case closure options.

### External incident management systems

You can add connectors to cases to push information to these external incident
management systems:

* {ibm-r}
* {jira}
* {sn-itsm}
* {sn-sir}
* {swimlane}
* {hive}
* {webhook-cm}

**Note:** To create connectors and send cases to external systems, you must have the
appropriate Kibana feature privileges. Refer to setup-cases.

You can create connectors in *{stack-manage-app} > {connectors-ui}*, as described in action-types.
Alternatively, you can create them in *{stack-manage-app} > Cases > Settings*:

. From the *Incident management system* list, select *Add new connector*.

. Select an external incident management system.

. Enter your required settings. Refer to resilient-action-type,
jira-action-type, servicenow-action-type, servicenow-sir-action-type,
swimlane-action-type, thehive-action-type, or cases-webhook-action-type for connector
configuration details.

You can subsequently choose the connector when you create cases and use it in case templates.
To change the default connector for new cases, select the connector from the
*Incident management system* list.

To update a connector, click *Update <connector name>* and edit the connector fields as required.

### Custom fields

You can add optional and required fields for customized case collaboration. added:[8.15.0]

To create a custom field:

. In the *Custom fields* section, click *Add field*.
(Figure: images/cases-custom-fields-add.png)

. You must provide a field label and type (text or toggle).
  You can optionally designate it as a required field and provide a default value.

When you create a custom field, it's added to all new and existing cases.
Existing cases have null values for new text fields until you set them in each case.

You can subsequently remove or edit custom fields on the *Settings* page.

### Templates

preview::[]

You can make the case creation process faster and more consistent by adding templates.
A template defines values for one or all of the case fields (such as severity, tags, description, and title) as well as any custom fields.

To create a template:

. In the *Templates* section, click *Add template*.
(Figure: images/cases-templates-add.png)

. You must provide a template name and case severity.
  You can optionally add template tags and a description, values for each case field, and a case connector.

When users create cases, they can optionally select a template and use its values or override them.

**Note:** If you update or delete templates, existing cases are unaffected.
