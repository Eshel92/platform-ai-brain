<!-- Converted from reference/alerts/host-down.txt (reStructuredText). Includes are inlined. -->

# Fix Down Host

At time `T`, the Monitoring on host `X` had not detected a 
mongod process running on host `Y` port `Z` for `A` 
minutes.

## Alert Conditions

You can configure alert conditions in the project-level 
alert settings page to trigger alerts.

To learn more about the alert condition, see 
Host is down.

## Common Triggers

- The mongod process could not be reached because of a 
  network issue.

- The mongod process is not running.

- The host is powered off.

## Fix the Immediate Problem

- Verify network communication between the host running the Monitoring 
  and the host that is listed as down. One way to do this is through 
  `mongosh`:

  ```sh
  mongosh <hostname>:<port>
  ```

  If connecting from `mongosh` fails, try a basic 
  ping test:

  ```sh
  ping <hostname>
  ```

- Verify the mongod process is running:

  If the process was installed from `deb` or `rpm` package, query 
  the service manager for the status:

  ```sh
  sudo service mongod status
  ```

  Alternatively, you can use `ps`:

  ```sh
  ps aux | grep mongo
  ```

**Note:**

The `Host is down` alert should not be used to detect all 
occurrences of a host reboot. The alert is triggered only if the 
host is seen as down at the instant that the Monitoring runs the 
check. The interval between checks can vary from 1 to 3 minutes.

## Implement a Long-Term Solution

Keep your host powered on and the mongod process running. 
Work to prevent any network issues.

## Monitor Your Progress

View the following chart to monitor your progress:

- Network
  
  Monitor network metrics to track network performance.

To learn more, see 
View Deployment Metrics.
