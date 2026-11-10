<!-- Converted from tab-widgets/troubleshooting/snapshot/corrupt-repository.asciidoc (AsciiDoc). Includes are inlined. -->

Fixing the corrupted repository will entail making changes in multiple deployments
that write to the same snapshot repository.
Only one deployment must be writing to a repository. The deployment 
that will keep writing to the repository will be called the "primary" deployment (the current cluster), 
and the other one(s) where we'll mark the repository read-only as the "secondary" 
deployments.

First mark the repository as read-only on the secondary deployments:

**Use Kibana**

. Log in to the {ess-console}[Elastic Cloud console].

. On the **Elasticsearch Service** panel, click the name of your deployment. 

**Note:** If the name of your deployment is disabled your Kibana instances might be
unhealthy, in which case please contact [Elastic Support](https://support.elastic.co).
If your deployment doesn't include Kibana, all you need to do is 
{cloud}/ec-access-kibana.html[enable it first].

. Open your deployment's side navigation menu (placed under the Elastic logo in the upper left corner)
and go to **Stack Management > Snapshot and Restore > Repositories**.
(Figure: images/repositories.png)

. The repositories table should now be visible. Click on the pencil icon at the 
right side of the repository to be marked as read-only. On the Edit page that opened 
scroll down and check "Read-only repository". Click "Save".
Alternatively if deleting the repository altogether is preferable, select the checkbox
at the left of the repository name in the repositories table and click the 
"Remove repository" red button at the top left of the table.

At this point, it's only the primary (current) deployment that has the repository marked
as writeable.
Elasticsearch sees it as corrupt, so the repository needs to be removed and added back so that 
Elasticsearch can resume using it:

Note that we're now configuring the primary (current) deployment.

. Open the primary deployment's side navigation menu (placed under the Elastic logo in the upper left corner)
and go to **Stack Management > Snapshot and Restore > Repositories**.
(Figure: images/repositories.png)

. Click on the pencil icon at the right side of the repository. On the Edit page that opened
scroll down and click "Save", without making any changes to the existing settings.

Fixing the corrupted repository will entail making changes in multiple clusters
that write to the same snapshot repository.
Only one cluster must be writing to a repository. Let's call the cluster 
we want to keep writing to the repository the "primary" cluster (the current cluster), 
and the other one(s) where we'll mark the repository as read-only the "secondary" 
clusters.

Let's first work on the secondary clusters:

. Get the configuration of the repository:
```console
GET _snapshot/my-repo
```
The response will look like this:
```console-result
{
  "my-repo": { <1>
    "type": "s3",
    "settings": {
      "bucket": "repo-bucket",
      "client": "elastic-internal-71bcd3",
      "base_path": "myrepo"
    }
  }
}
```
<1> Represents the current configuration for the repository.

. Using the settings retrieved above, add the `readonly: true` option to mark
it as read-only:
```console
PUT _snapshot/my-repo
{
    "type": "s3",
    "settings": {
      "bucket": "repo-bucket",
      "client": "elastic-internal-71bcd3",
      "base_path": "myrepo",
      "readonly": true <1>
    }
}
```
<1> Marks the repository as read-only.

. Alternatively, deleting the repository is an option using:
```console
DELETE _snapshot/my-repo
```
The response will look like this:
```console-result
{
  "acknowledged": true
}
```

At this point, it's only the primary (current) cluster that has the repository marked
as writeable.
Elasticsearch sees it as corrupt though so let's recreate it so that Elasticsearch can resume using it.
Note that now we're configuring the primary (current) cluster:

. Get the configuration of the repository and save its configuration as we'll use it
to recreate the repository:
```console
GET _snapshot/my-repo
```
. Using the configuration we obtained above, let's recreate the repository:
```console
PUT _snapshot/my-repo
{
  "type": "s3",
  "settings": {
    "bucket": "repo-bucket",
    "client": "elastic-internal-71bcd3",
    "base_path": "myrepo"
  }
}
```
The response will look like this:
```console-result
{
  "acknowledged": true
}
```
