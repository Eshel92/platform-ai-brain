<!-- Converted from user/alerting/rule-types.asciidoc (AsciiDoc). Includes are inlined. -->

## Rule types

A rule is a set of conditions, schedules, and actions that enable notifications. Kibana provides rules built into the Elastic Stack and rules registered by one of the Kibana apps.
You can create most rules types in <<create-and-manage-rules,{stack-manage-app} > {rules-ui}>>.
Security rules must be defined in the Security app. For more information, refer to the documentation about {security-guide}/rules-ui-create.html[creating a detection rule].

==============================================
Some rule types are subscription features, while others are free features.
For a comparison of the Elastic subscription levels,
see {subscriptions}[the subscription page].
==============================================

### Stack rules

Stack rules are built into Kibana. To access the *Stack Rules* feature and create and edit rules, users require the `all` privilege. See feature privileges for more information.

|===

| rule-type-es-query
| Run a user-configured Elasticsearch query, compare the number of matches to a configured threshold, and schedule actions to run when the threshold condition is met.

| rule-type-index-threshold
| Aggregate field values from documents using Elasticsearch queries, compare them to threshold values, and schedule actions to run when the thresholds are met.

| [Transform rules](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/transform-alerts.html)
| beta:[] Run scheduled checks on a {ctransform} to check its health. If a {ctransform} meets the conditions, an alert is created and the associated action is triggered.

| Tracking containment
| Run an Elasticsearch query to determine if any documents are currently contained in any boundaries from a specified boundary index and generate alerts when a rule's conditions are met.

|===

### Observability rules

Observability rules detect complex conditions in your observability data and create alerts when a rule's conditions are met. For example, you can create a rule that detects when the value of a metric exceeds a specified threshold or when an anomaly occurs on a system or service you are monitoring. For more information, refer to {observability-guide}/create-alerts.html[Alerting].

==============================================
If you create a rule in the Observability app, its alerts are not visible in
*{stack-manage-app} > {rules-ui}*. They are visible only in the Observability app.
==============================================

### Machine learning rules

beta:[] {ml-docs}/ml-configuring-alerts.html[Machine learning rules] run scheduled checks on an anomaly detection job to detect anomalies with certain conditions. If an anomaly meets the conditions, an alert is created and the associated action is triggered.

### Security rules

Security rules detect suspicious source events with pre-built or custom rules and create alerts when a rule's conditions are met. For more information, refer to {security-guide}/prebuilt-rules.html[Security rules].

==============================================
Alerts associated with security rules are visible only in the {security-app};
they are not visible in *{stack-manage-app} > {rules-ui}*.
==============================================

(See `user/alerting/rule-types/index-threshold.md`)
(See `user/alerting/rule-types/es-query.md`)
(See `user/alerting/rule-types/geo-rule-types.md`)
