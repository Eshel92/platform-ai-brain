<!-- Converted from management/maintenance-windows/maintenance-windows.asciidoc (AsciiDoc). Includes are inlined. -->

## Maintenance windows

preview::[]

You can schedule single or recurring maintenance windows to temporarily reduce rule notifications.
For example, a maintenance window prevents false alarms during planned outages.

By default, a maintenance window affects all rules in all Kibana apps within its space.
You can refine the scope of a maintenance window by adding filters and rule categories.

Alerts continue to be generated, however notifications are suppressed as follows:

- When an alert occurs during a maintenance window, there are no notifications.
When the alert recovers, there are no notifications--even if the recovery occurs after the maintenance window ends.
- When an alert occurs before a maintenance window and recovers during or after the maintenance window, notifications are sent as usual.

## Configure access to maintenance windows

To use maintenance windows, you must have the appropriate {subscriptions}[subscription] and Kibana feature privileges.

- To have full access to maintenance windows, you must have `All` privileges for the *Management > Maintenance Windows* feature.
- To have view-only access to maintenance windows, you must have `Read` privileges for the *Management > Maintenance Windows* feature.

For more details, refer to kibana-privileges.

## Create and manange maintenance windows

In *Management > {stack-manage-app} > Maintenance Windows*, you can create, edit, cancel, archive, and delete maintenance windows. Be aware that you can't recover maintenance windows once you delete them.

When you create a maintenance window, you must provide a name and a schedule.
You can optionally configure it to repeat daily, monthly, yearly, or on a custom interval.

(Figure: images/create-maintenance-window.png)

By default, maintenance windows affect all categories of rules.
The category-specific maintenance window options alter this behavior.
For the definitive list of rule types in each category, refer to the [get rule types API](https://www.elastic.co/docs/api/doc/kibana/group/endpoint-alerting).

If you turn on *Filter alerts*, you can use KQL to filter the alerts affected by the maintenance window:

(Figure: images/create-maintenance-window-filter.png)

**Note:** You can select only a single category when you turn on filters.

A maintenance window can have any one of the following statuses:

- `Upcoming`: It will run at the scheduled date and time.
- `Running`: It is running.
- `Finished`: It ended and does not have a repeat schedule.
- `Archived`: It is archived. In a future release, archived maintenance windows will be queued for deletion.

When you view alert details in Kibana, each alert shows unique identifiers for maintenance windows that affected it.
