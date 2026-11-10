<!-- Converted from management/connectors/action-types/cases-action-type.asciidoc (AsciiDoc). Includes are inlined. -->

## Cases connector and action

The Cases connector creates cases in Kibana when alerts occur.

### Create connectors in Kibana

To use this connector you must have `All` Kibana privileges for the *Cases* feature.
Depending on the type of rule you want to create and its role visibility, you must have privileges for *Management* or *Observability* case features.
For more details, refer to kibana-privileges.

You cannot manage this connector in *{stack-manage-app} > {connectors-ui}* or by using APIs.
You also cannot create a Cases preconfigured connector.
It is available only when you're creating a rule in Kibana.
For example:

(Figure: management/connectors/images/cases-action.png)

**Note:** You can have only one Cases action in each rule.

#### Connector configuration

Cases connectors have the following configuration properties:

Group by alert field::
By default, all alerts are attached to the same case.
You can optionally choose a field to use for grouping the alerts; a unique case is created for each group.

Time window::
By default, alerts are added to an existing case only if they occur within a 7 day time window.

Template name::
Select a specific case template to apply when the Cases action is triggered (optional).

Reopen when the case is closed::
If this option is enabled, closed cases are re-opened when an alert occurs.

### Test connectors

You cannot test or edit these connectors in Kibana or by using APIs.
