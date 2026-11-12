<!-- Part 1 of 4 of reference/access-authn-authz/authentication.md (split because the page is big). -->

## Users in Kubernetes

All Kubernetes clusters have two categories of users: service accounts managed
by Kubernetes, and normal users.

It is assumed that a cluster-independent service manages normal users in the following ways:

- an administrator distributing private keys
- a user store like Keystone or Google Accounts
- a file with a list of usernames and passwords

In this regard, _Kubernetes does not have objects which represent normal user accounts._
Normal users cannot be added to a cluster through an API call.

Even though a normal user cannot be added via an API call, any user that
presents a valid certificate signed by the cluster's certificate authority
(CA) is considered authenticated. In this configuration, Kubernetes determines
the username from the common name field in the 'subject' of the cert (e.g.,
"/CN=bob"). From there, the role based access control (RBAC) sub-system would
determine whether the user is authorized to perform a specific operation on a
resource.

In contrast, service accounts are users managed by the Kubernetes API. They are
bound to specific namespaces, and created automatically by the API server or
manually through API calls. Service accounts are tied to a set of credentials
stored as `Secrets`, which are mounted into pods allowing in-cluster processes
to talk to the Kubernetes API.

API requests are tied to either a normal user or a service account, or are treated
as [anonymous requests](#anonymous-requests). This means every process inside or outside the cluster, from
a human user typing `kubectl` on a workstation, to `kubelets` on nodes, to members
of the control plane, must authenticate when making requests to the API server,
or be treated as an anonymous user.
