<!-- Converted from tutorial/manage-alerts-and-events.txt (reStructuredText). Includes are inlined. -->

# Manage Alerts

## Overview

Ops Manager issues alerts for the database and server conditions
configured in your alert settings. When a 
condition triggers an alert, you receive the alert at regular
intervals until the alert resolves or Ops Manager cancels it. You should fix 
the immediate problem, implement a long-term solution, and 
view metrics to monitor 
your progress.

**org:**

**project:**

## View Alerts

hidden: true

tabs:
  - id: org
    name: Organization Alerts
    content: |

      You can view all alerts, alert settings, and deleted alerts on 
      the Organization Alerts page. To learn more, see 
      alerts-workflow.

      **Step 1: Navigate to the Alerts page for your organization.**

      a. If it is not already displayed, select your desired organization
         from the `office` Organizations menu in the
         navigation bar.

      #. Click Alerts in the sidebar.

      **Step 2: If it is not already displayed, click the All Alerts tab.**

  - id: project
    name: Project Alerts
    content: |

      You can view open alerts, closed alerts, and alert 
      settings on the Project Alerts page. 
      MongoDB Atlas sends notifications for all alerts 
      that appear on the Open tab. To learn more, 
      see alerts-workflow.

      **Step 1: Navigate to the Alerts page for your project.**

      a. If it is not already displayed, select the organization that
         contains your desired project from the `office` Organizations menu in the
         navigation bar.

      #. If it is not already displayed, select your desired project
         from the Projects menu in the navigation bar.

      #. Click the `bell` Project Alerts icon in the
         navigation bar, or click Alerts in the sidebar.

      **Step 2: Click the tab that corresponds to the status of the alerts you want to view.**

      - To view open alerts, click the Open Alerts tab if it is
        not already displayed.
      - To view closed alerts, click the Closed Alerts tab.

## View All Activity

tabs:
  - id: org
    name: Organization Activity
    content: |

      **Step 1: Navigate to the Activity Feed page for your organization.**

      a. If it is not already displayed, select your desired organization
         from the `office` Organizations menu in the
         navigation bar.

      #. Click Activity Feed in the sidebar.

      **Step 2: Filter the activity feed.**

      You can filter the organization activity feed by event type and time
      range. You can combine filtering methods together for greater control
      over the activity feed output.

      Filter by event
        Select the event categories or specific events you want to see from
        the activity feed. To exclude specific categories or events from the
        activity feed, click Select all categories and events,
        then deselect the categories and events you want to exclude.

        You can filter events based on the following categories:

        | Category | Description |
        |---|---|
        | Access | Events related to Ops Manager users. |
        | Alerts | Events related to alert configuration and monitoring. |
        | Billing | Events related to payments and payment methods. |
        | Others | Miscellaneous events, including log retrieval and mLab events. |
        | Organization | Events related to your Ops Manager organization. |
        | Projects | Events related to Ops Manager projects. |

      Filter by time range
        Select a Start Date and End Date to
        view events from within a specified time range. Once you have
        configured a time range, click Apply Dates to
        update the activity feed with the specified range.

  - id: project
    name: Project Activity
    content: |

      **Step 1: Navigate to the Activity Feed page for your project.**

      a. If it is not already displayed, select the organization that
         contains your desired project from the `office` Organizations menu in the
         navigation bar.

      #. If it is not already displayed, select your desired project
         from the Projects menu in the navigation bar.

      #. Click the Project Activity Feed icon in the navigation
         bar, or click Activity Feed in the sidebar.

      **Step 2: Filter the activity feed.**

      You can filter the project activity feed by event type, cluster, and
      time range. You can combine filtering methods together for greater
      control over the activity feed output.

      Filter by event
        Select the event categories or specific events you want to see from
        the activity feed. To exclude specific categories or events from the
        activity feed, click Select all categories and events,
        then deselect the categories and events you want to exclude.

        You can filter events based on the following categories:

        | Category | Description |
        |---|---|
        | Access | Events related to Ops Manager users. |
        | Alerts | Events related to alert configuration and monitoring. |
        | Billing | Events related to payments and payment methods. |
        | Others | Miscellaneous events, including log retrieval and mLab events. |
        | Organization | Events related to your Ops Manager organization. |
        | Projects | Events related to Ops Manager projects. |

      Filter by time range
        Select a Start Date and End Date to
        view events from within a specified time range. Once you have
        configured a time range, click Apply Dates to
        update the activity feed with the specified range.

## Retrieve the Activity Feed

You can retrieve events for a specified organization or project using
the /reference/api/events/ API (Application Programming Interface) resource.

## Acknowledge an Alert

When you acknowledge the alert, Ops Manager sends no further notifications to
the alert's distribution list until the acknowledgment period has
passed or until you resolve the alert. The distribution list
receives *no* notification of the acknowledgment.

If the alert condition ends during the acknowledgment period, Ops Manager
sends a notification of the resolution.

If you configure an alert with PagerDuty, a third-party incident
management service, you can only acknowledge the alert on your
PagerDuty dashboard.

hidden: true

tabs:
  - id: org
    name: Organization Alerts
    content: |

      **Step 1: Navigate to the Alerts page for your organization.**

      a. If it is not already displayed, select your desired organization
         from the `office` Organizations menu in the
         navigation bar.

      #. Click Alerts in the sidebar.

      **Step 2: Acknowledge alerts**

      To acknowledge a single alert, on the line item for the alert, click 
      Acknowledge.

      To acknowledge multiple, but not all, alerts:

      a. Check the checkbox to the left of each alert to acknowledge.

      #. Click Mark Acknowledge above the table.

      To acknowledge all alerts: 

      a. Select the checkbox in the table header to select every alert.

      #. Click Mark Acknowledge above the table.

      **Step 3: Select the time period for which to acknowledge the alert.**

      Click the time frame for which you no longer wish to receive alerts.

      Ops Manager sends no further alert messages for the period of time you
      select.

      **Step 4: If all Alerts were checked, select All Visible or All Open Alerts.**

      If all alerts are checked, then another set of radio buttons appear:

      - Click Acknowledge all visible checked alerts to 
        acknowledge all alerts that were loaded onto the page.

      - Click Acknowledge all open alerts to acknowledge all 
        alerts: checked, unchecked, visible and not visible on the current 
        page.

      **Step 5: Click Acknowledge to confirm.**

  - id: project
    name: Project Alerts
    content: |

      **Step 1: Navigate to the Open Alerts tab.**

      a. If it is not already displayed, select the organization that
         contains your desired project from the `office` Organizations menu in the
         navigation bar.

      #. If it is not already displayed, select your desired project
         from the Projects menu in the navigation bar.

      #. Click the `bell` Project Alerts icon in the
         navigation bar, or click Alerts in the sidebar.

      #. If it is not already displayed, click the Open Alerts 
         tab.

      **Step 2: Acknowledge alerts**

      To acknowledge a single alert, on the line item for the alert, click 
      Acknowledge.

      To acknowledge multiple, but not all, alerts:

      a. Check the checkbox to the left of each alert to acknowledge.

      #. Click Mark Acknowledge above the table.

      To acknowledge all alerts: 

      a. Select the checkbox in the table header to select every alert.

      #. Click Mark Acknowledge above the table.

      **Step 3: Select the time period for which to acknowledge the alert.**

      Click the time frame for which you no longer wish to receive alerts.

      Ops Manager sends no further alert messages for the period of time you
      select.

      **Step 4: If all Alerts were checked, select All Visible or All Open Alerts.**

      If all alerts are checked, then another set of radio buttons appear:

      - Click Acknowledge all visible checked alerts to 
        acknowledge all alerts that were loaded onto the page.

      - Click Acknowledge all open alerts to acknowledge all 
        alerts: checked, unchecked, visible and not visible on the current 
        page.

      **Step 5: Click Acknowledge to confirm.**

## Unacknowledge an Alert

You can undo an acknowledgment and again receive notifications if the
alert condition still applies.

hidden: true

tabs:
  - id: org
    name: Organization Alerts
    content: |

      **Step 1: Navigate to the Alerts page for your organization.**

      a. If it is not already displayed, select your desired organization
         from the `office` Organizations menu in the
         navigation bar.

      #. Click Alerts in the sidebar.

      **Step 2: On the line item for the alert, click Unacknowledge.**

      **Step 3: Click Confirm.**

      If the alert condition continues to exist, Ops Manager resends the alerts.

  - id: project
    name: Project Alerts
    content: |

      **Step 1: Navigate to the Open Alerts tab.**

      a. If it is not already displayed, select the organization that
         contains your desired project from the `office` Organizations menu in the
         navigation bar.

      #. If it is not already displayed, select your desired project
         from the Projects menu in the navigation bar.

      #. Click the `bell` Project Alerts icon in the
         navigation bar, or click Alerts in the sidebar.

      #. If it is not already displayed, click the Open Alerts 
         tab.

      **Step 2: On the line item for the alert, click Unacknowledge.**

      **Step 3: Click Confirm.**

      If the alert condition continues to exist, Ops Manager resends the alerts.

## Disable Alerts for a Specific Process

You can turn off alerts for a given process. This might be useful, for
example, if you want to temporarily disable the process but do not want
it hidden from monitoring. Use the following procedure both to turn
alerts off or on.

**Step 1: Navigate to the Clusters view for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Clusters view.

**Step 2: On the line listing the process, click the ellipsis icon and select Monitoring Settings.**

**Step 3: Select Alert Status and then modify the alert settings.**

## Suspend Alerts by Adding a Maintenance Window

Specify maintenance windows to temporarily turn off alert notifications
for a given resource while you perform maintenance.

**Important:**

Maintenance windows have a cache TTL of 5 minutes. When you create or
update a maintenance window, it might take up to 5 minutes to take
effect. You might receive alerts during this initial 5-minute period.

To view maintenance windows:

**Step 1: Navigate to the Alert Settings tab.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. Click the `bell` Project Alerts icon in the
   navigation bar, or click Alerts in the sidebar.

#. Click the Alert Settings tab.

**Step 2: Click the Maintenance Windows filter.**

### Add or Edit a Maintenance Window

**Step 1: Navigate to the Alert Settings tab.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. Click the `bell` Project Alerts icon in the
   navigation bar, or click Alerts in the sidebar.

#. Click the Alert Settings tab.

**Step 2: Add or edit a maintenance window.**

- **To add a maintenance window:** Click the Add button and
  select New Maintenance Window.

- **To edit a maintenance window:** Click the Maintenance
  Windows filter, then click the ellipsis icon for a
  mainenance window and select Edit.

**Step 3: Select the target components for which to suspend alerts.**

Note that selecting the Host target selects both `HOST`
and `HOST_METRIC` alert configurations returned through the
alertConfigs endpoint.

**Step 4: Select the time period for which to suspend alerts.**

**Step 5: Enter an optional description for the maintenance window.**

**Step 6: Click Save.**

### Delete a Maintenance Window

**Step 1: Navigate to the Alert Settings tab.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. Click the `bell` Project Alerts icon in the
   navigation bar, or click Alerts in the sidebar.

#. Click the Alert Settings tab.

**Step 2: Click the Maintenance Windows filter.**

**Step 3: For the window to delete, click the ellipsis icon and select Delete.**

**Step 4: Click Confirm.**
