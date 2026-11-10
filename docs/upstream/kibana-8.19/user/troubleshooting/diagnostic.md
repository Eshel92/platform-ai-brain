<!-- Converted from user/troubleshooting/diagnostic.asciidoc (AsciiDoc). Includes are inlined. -->

### Capturing diagnostics

The Kibana [Support Diagnostic](https://github.com/elastic/support-diagnostics) 
tool captures a point-in-time snapshot of Kibana and its Task Manager health. 
It works on Kibana versions 7.11.0 and above. 

You can use the information captured by the tool to troubleshoot problems with Kibana instances. 
Check the 
https://www.elastic.co/blog/troubleshooting-kibana-health[Troubleshooting 
Kibana Health blog] for examples.

You can generate diagnostic information using this tool before you contact 
[Elastic Support](https://support.elastic.co) or 
[Elastic Discuss](https://discuss.elastic.co) to help get a timely answer. 

#### Requirements

-  Java Runtime Environment or Java Development Kit v1.8 or higher.

#### Access the tool

The Support Diagnostic tool is included out-of-the-box as a sub-library in: 

* Elastic Cloud Enterprise - Find the tool under **Elastic Cloud Enterprise** > **Deployment** > **Operations** > 
**Prepare Bundle** > **Kibana**. 
* Elastic Cloud on Kubernetes - Run the tool with [`eck-diagnostics`](https://www.elastic.co/guide/en/cloud-on-k8s/current/k8s-take-eck-dump.html).

You can also get the latest version of the tool by downloading the `diagnostics-X.X.X-dist.zip` file from 
https://github.com/elastic/support-diagnostics/releases/latest[the 
`support-diagnostic` repo].

#### Capture diagnostic information

To run a Kibana diagnostic: 

. In a terminal, verify that your network and user permissions are sufficient 
to connect by polling Kibana's Task Manager health.
For example, with the parameters `host:localhost`, `port:5601`, and 
`username:elastic`, you'd use the following curl request. Adapt these parameters to your context.
```sh
curl -X GET -k -H 'kbn-xsrf: true' -u elastic -p https://localhost:5601/api/task_manager/_health
```
If you receive an HTTP 200 `OK` response, you can proceed to the 
next step. If you receive a different response code, you must 
diagnose the issue before proceeding.

. Using the same environment parameters, run the diagnostic tool script. 
For information about the parameters that you can pass to the tool, refer 
to the https://github.com/elastic/support-diagnostics#standard-options[diagnostic 
parameter reference]. 
The following command options are recommended:
**Unix-based systems**
```sh
sudo ./diagnostics.sh --type kibana-local --host localhost --port 5601 -u elastic -p --bypassDiagVerify --ssl --noVerify
```
**Windows**
```sh
sudo .\diagnostics.bat --type kibana-local --host localhost --port 5601 -u elastic -p --bypassDiagVerify --ssl --noVerify
```
**Script execution modes**

**Tip:**
You can execute the script in three [modes](https://github.com/elastic/support-diagnostics#diagnostic-types): 

* `kibana-local` (default, recommended): Polls the Kibana API, 
gathers operating system info, and captures cluster and garbage collection (GC) logs. 

* `kibana-remote`: Establishes an SSH session 
to the applicable target server to pull the same information as `kibana-local`.

* `kibana-api`: Polls the Kibana API. All other data must be 
collected manually.

. When the script has completed, verify that no errors were logged to 
`diagnostic.log`. If the log file contains errors, refer to 
Diagnose errors in `diagnostic.log`.

. If the script completed without errors, an archive with the 
format `<diagnostic type>-diagnostics-<DateTimeStamp>.zip` is created in 
the working directory or the output directory that you have specified. You can 
review or share the diagnostic archive as needed.

#### Diagnose a non-200 response

When you poll your Task Manager health, if you receive any response other 
than `200 0K`, then the diagnostic tool might not work as intended. Check the possible resolutions based on the error code that you get:

HTTP 401 `UNAUTHENTICATED`::
Additional information in the error will usually indicate 
that your `username:password` pair is invalid, or that your Elasticsearch `.security` 
index is unavailable and you need to setup a temporary Elasticsearch
[file-based realm](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/file-realm.html) user with `role:superuser` to authenticate.

HTTP 403 `UNAUTHORIZED`::
Your `username` is recognized but has insufficient permissions to run the 
diagnostic. Either use a different username or increase the user's privileges.

HTTP 429 `TOO_MANY_REQUESTS` (for example, `circuit_breaking_exception`)::
The authentication and authorization were successful, but the Elasticsearch cluster isn't  
responding to requests. This issue is usually intermittent and can happen 
when the cluster is overwhelmed. In this case, resolve Elasticsearch's health first before 
returning to Kibana. 

HTTP 504 `BAD_GATEWAY`::
Your network has trouble reaching Kibana. You might be using 
a proxy or firewall. Consider running the diagnostic tool from a different 
location, confirming your port, or using an IP instead of a URL domain. 

#### Diagnose errors in `diagnostic.log`

The following are common errors that you might encounter when running 
the diagnostic tool:

* `Error: Could not find or load main class com.elastic.support.diagnostics.DiagnosticApp`
This indicates that you accidentally downloaded the source code file 
instead of `diagnostics-X.X.X-dist.zip` from the releases page.

* A `security_exception` that includes `is unauthorized for user`:
The provided user has insufficient admin permissions to run the diagnostic 
tool. Use another user, or grant the user `role:superuser` privileges.

* `Kibana Server is not Ready yet`
This indicates issues with Kibana's dependencies blocking full start-up. 
To investigate, check Troubleshoot Kibana UI error.
