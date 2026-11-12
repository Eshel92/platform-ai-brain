<!-- Converted from security/operator-privileges/index.asciidoc (AsciiDoc). Includes are inlined. -->

## Operator privileges

**Note:** {cloud-only}

With a typical Elasticsearch deployment, people who administer the cluster also operate
the cluster at the infrastructure level. User authorization based on
role-based access control (RBAC) is effective and reliable for
this environment. However, in more managed environments, such as
{ess-trial}[Elasticsearch Service], there is a distinction between the operator of the cluster
infrastructure and the administrator of the cluster. 

Operator privileges limit some functionality to operator users _only_. Operator
users are just regular Elasticsearch users with access to specific
operator-only functionality. These
privileges are not available to cluster administrators, even if they log in as
a highly privileged user such as the `elastic` user or another user with the
`superuser` role. By limiting system access, operator privileges enhance the
Elasticsearch security model while safeguarding user capabilities.

Operator privileges are enabled on Elastic Cloud, which means that some 
infrastructure management functionality is restricted and cannot be accessed by
your administrative users. This capability protects your cluster from unintended 
infrastructure changes.

(See `security/operator-privileges/configure-operator-privileges.md`)
(See `security/operator-privileges/operator-only-functionality.md`)
(See `security/operator-privileges/operator-only-snapshot-and-restore.md`)
