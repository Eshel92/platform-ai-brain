<!-- Converted from ingest/apis/enrich/delete-enrich-policy.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete enrich policy API

**New API reference**
For the most up-to-date API details, refer to [Enrich APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-enrich).

Deletes an existing enrich policy and its
enrich index.

```console
DELETE /_enrich/policy/my-policy
```

#### Request

`DELETE /_enrich/policy/<enrich-policy>`

#### Prerequisites

To use enrich policies, you must have:

* `read` index privileges for any indices used
* The `enrich_user` built-in role

#### Description

Use the delete enrich policy API
to delete an existing enrich policy
and its enrich index.

**Important:**
You must remove an enrich policy
from any in-use ingest pipelines
before deletion.
You cannot remove in-use enrich policies.

#### Path parameters

`<enrich-policy>`::
(Required, string)
Enrich policy to delete.
