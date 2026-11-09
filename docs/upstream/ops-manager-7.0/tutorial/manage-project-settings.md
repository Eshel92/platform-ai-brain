<!-- Converted from tutorial/manage-project-settings.txt (reStructuredText). Includes are inlined. -->

# Edit Project Settings

You can configure project-specific settings from the project's
Settings page.

**See also:**

- /tutorial/manage-users

- /tutorial/manage-agent-api-key.

**Step 1: Navigate to the Settings page for your project.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. Next to the Projects menu, expand the
   Options menu, then click Project Settings.

**Step 2: View or modify project settings.**

Project Settings displays the configurable settings.
See group-settings-page to view the setting descriptions.

If you access Ops Manager as a user with the `Global Owner` 
role, you can also update Admin Project Settings under 
the Global Admin Only section. See
admin-only-group-settings to view the
administrative setting descriptions.

## Project Settings

Project Settings apply to all the users in the project.

* - Setting

  - Description

* - Project

  - Sets your project's name.

    Only users with `Project Owner` access for the
    project can edit the project name.

* - Project Time Zone

  - Sets your project's time zone.

    Only users with `Project Owner` access for the
    project can edit the project time zone.

* - Collect Logs For All Hosts

  - Activates or deactivates the collection of log data for all
    hosts. This overwrites the statuses set on the individual hosts.

* - Collect Profiling Information for All Hosts

  - Activates or deactivates Ops Manager collection of data from the
    MongoDB database profilers
    running on your mongod instances. A mongod
    instance must have its profiler enabled in order for Ops Manager to
    collect data from it.

    When you change this setting, Ops Manager applies the change globally
    to all mongod processes in the project. For example,
    if you disable this setting, Ops Manager disables the collection of
    profiling data for all the project's processes. This setting
    does not affect whether the profiler is enabled on a given
    mongod process, only whether Ops Manager collects profiling
    data.

    To enable the collection of profiling data on a
    process-by-process basis, see /tutorial/profile-database.

    When profiling is enabled, Ops Manager collects data from MongoDB’s
    profiler to provide statistics about performance and database
    operations. Ensure exposing profile data to Ops Manager is consistent
    with your information security practices. Also be aware the
    profiler can consume resources which may adversely affect
    MongoDB performance.

    For more information, see /tutorial/profile-database.

* - Collect Database Specific Statistics

  - Allows you to enable or disable the collection of database
    statistics. For more information, see
    /tutorial/profile-database.

* - Default Project Server Type

  - Sets the default server type for all hosts added to this
    project. This does *not* modify the default server type of existing hosts.

    * - Server Intention
      - Environment Purpose
      - License Requirement

    * - Production Server
      - Hosts your application to your internal or external end users.

        If an end user might use an environment, it functions as a
        Production environment. This applies whether the environment
        also provides testing, quality assurance, evaluation, or
        development capabilities.

      - One license per server

    * - Test/QA Server
      - This type of environment can be used to:

        |  |  |
        |---|---|
        | Test | Exercises your application to verify that it works as designed and expected. The platform configuration might be a less performant version of Production in compute, network, and storage capability. |
        | Assure system quality | Validates your application against a combination of data, hardware, and software configured to simulate Production. The platform configuration should be a smaller scale of Production in compute, network, and storage capability. |
        | Stage | Simulates the Production environment including performance testing and release candidate approval. The platform configuration should mirror Production in compute, network, and storage capability. |

      - One license per server

    * - Development Server
      - Hosts in progress design, code, debugging or some combination
        thereof for your application. Used to evaluate if the current
        state of your application can be promoted to another
        environment.
      - None

    * - RAM Pool
      - Provides any combination of servers for any environment purpose.
      - One license for any number of servers up to the maximum of
        the total GB of RAM you purchased across these servers.

    |  |  |  |
    |---|---|---|
    | Backing Database | Hosts your Ops Manager backing database. enable-application-database-monitoring to enable this option. | None |

* - Reset Duplicates

  - Allows you to reset and remove all detected duplicate hosts.
    This is useful if your server environment has drastically
    changed and you believe a host is incorrectly marked as a
    duplicate.

* - Preferred Hostnames

  - Allows you to specify resolvable hostnames or IP (Internet Protocol) addresses
    for your deployment's host. Ops Manager keeps a list of the multiple
    ways to which each host is referred (hostname, FQDN (fully qualified domain name), IPv4 (Internet Protocol version 4)
    address, IPv6 (Internet Protocol version 6) address) and uses heuristics to determine the
    best choice. Specify a preferred hostname to make sure Ops Manager
    uses a hostname that can resolve to a host. The method you
    choose becomes the method used to display the hosts in Ops Manager.

    To specify a preferred hostname, click Add and do
    one of the following:

    - To specify hostnames that end with a particular string, click
      the Ends With button and enter the string.

    - To specify hostnames that match a pattern, click the
      Regex button and enter a regular expression. An
      expression that uses "starts with" behavior must have `.*`
      at the end in order to correctly match. 

      For example, to specify hostnames that start with `acme-`, enter the following regular expression:

      ```none
      ^acme-.*
      ```

* - Suppress Mongos Automatic Discovery

  - Suppresses automatic discovery of all mongos
    processes in your deployment's sharded clusters.

* - Real Time Performance Panel

  - Enables the collection and display of real time metrics from
    your MongoDB databases in the
    Real-Time Performance Panel

    If you toggle Real-Time Performance Panel to
    `Off`, you disable this feature for every user in the Project.

    You might see some PII (Personally identifiable information) if you have permission to use this
    feature.

* - Data Explorer

  - Enables the ability to query of your MongoDB databases from
    Ops Manager.

    If you toggle Data Explorer to `Off`, you disable
    this feature for every user in the Project.

    You might see some PII (Personally identifiable information) if you have permission to use this
    feature.

* - Performance Advisor

  - Enables the ability to analyze the logs of your MongoDB database
    to recommend performance improvements.

    If you toggle Performance Advisor to `Off`, you
    disable this feature for every user in the Project.

    You might see some PII (Personally identifiable information) if you have permission to use this
    feature.

* - Delete Project

  - Click Delete to remove the project from Ops Manager. The
    Delete Project modal displays. Click
    Delete Project to confirm your decision.

## Admin Project Settings

The following project settings in the Global Admin Only
section of Settings could, in certain situations, affect
more than the project. For example, setting logging to a high
verbosity would cause system logs to roll over faster. Only users
with the `Global Owner` role can edit these settings:

| Setting | Description |
|---|---|
| Mongos Deactivation Threshold | Change the amount of time before Ops Manager removes an unreachable mongos process from the Deployment tab view. By default, Ops Manager waits 30 days before removing an unreachable mongos. Set this to the amount of time in seconds to wait before removal. This setting applies only if the mongos is not managed by Ops Manager Automation. |
| Monitoring Agent Log Level | Change the verbosity of the Monitoring log. |
| Automation Agent Log Level | Change the verbosity of the Automation log. |
