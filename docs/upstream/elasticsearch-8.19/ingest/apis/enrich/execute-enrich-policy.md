<!-- Converted from ingest/apis/enrich/execute-enrich-policy.asciidoc (AsciiDoc). Includes are inlined. -->

### Execute enrich policy API

**New API reference**
For the most up-to-date API details, refer to [Enrich APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-enrich).

Executes an existing enrich policy.

```console
PUT /_enrich/policy/my-policy/_execute?wait_for_completion=false
```

#### Request

`PUT /_enrich/policy/<enrich-policy>/_execute`

`POST /_enrich/policy/<enrich-policy>/_execute`

#### Prerequisites

To use enrich policies, you must have:

* `read` index privileges for any indices used
* The `enrich_user` built-in role

#### Description

Use the execute enrich policy API
to create the enrich index for an existing enrich policy.

The _enrich index_ contains documents from the policy's source indices.
Enrich indices always begin with `.enrich-*`,
are read-only,
and are force merged.

**Warning:**
Enrich indices should only be used by the enrich processor
or the ES|QL `ENRICH` command. Avoid using enrich indices for
other purposes.

Once created, you cannot update 
or index documents to an enrich index.
Instead, update your source indices
and execute the enrich policy again.
This creates a new enrich index from your updated source indices. 
The previous enrich index will deleted with a delayed maintenance job. 
By default this is done every 15 minutes. 

By default, this API is synchronous: It returns when a policy has been executed.
Because executing a policy performs several operations, it may take a while to
return a response, especially when the source indices are large. This can lead
to timeouts. To prevent timeouts, set the `wait_for_completion` parameter to
`false`. This runs the request asynchronously in the background, and returns a
task ID. You can use the task ID to manage the request with the <<tasks,task
management API>>.

#### Path parameters

`<enrich-policy>`::
(Required, string)
Enrich policy to execute.

#### Query parameters

`wait_for_completion`::
(Optional, Boolean)
If `true`, the request blocks until execution is complete. If `false`, the
request returns immediately and execution runs asynchronously in the background.
Defaults to `true`.
