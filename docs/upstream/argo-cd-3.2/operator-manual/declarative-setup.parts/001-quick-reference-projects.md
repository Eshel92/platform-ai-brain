<!-- Part 1 of 4 of operator-manual/declarative-setup.md (split because the page is big). -->

## Quick Reference

All resources, including `Application` and `AppProject` specs, have to be installed in the Argo CD namespace (by default `argocd`).

### Atomic configuration

| Sample File                                                           | Resource Name                                                                      | Kind      | Description                                                                          |
|-----------------------------------------------------------------------|------------------------------------------------------------------------------------|-----------|--------------------------------------------------------------------------------------|
| [`argocd-cm.yaml`](argocd-cm-yaml.md)                                 | argocd-cm                                                                          | ConfigMap | General Argo CD configuration                                                        |
| [`argocd-repositories.yaml`](argocd-repositories-yaml.md)             | my-private-repo / istio-helm-repo / private-helm-repo / private-repo               | Secrets   | Sample repository connection details                                                 |
| [`argocd-repo-creds.yaml`](argocd-repo-creds-yaml.md)                    | argoproj-https-creds / argoproj-ssh-creds / github-creds / github-enterprise-creds | Secrets   | Sample repository credential templates                                               |
| [`argocd-cmd-params-cm.yaml`](argocd-cmd-params-cm-yaml.md)           | argocd-cmd-params-cm                                                               | ConfigMap | Argo CD env variables configuration                                                  |
| [`argocd-secret.yaml`](argocd-secret-yaml.md)                         | argocd-secret                                                                      | Secret    | User Passwords, Certificates (deprecated), Signing Key, Dex secrets, Webhook secrets |
| [`argocd-rbac-cm.yaml`](argocd-rbac-cm-yaml.md)                       | argocd-rbac-cm                                                                     | ConfigMap | RBAC Configuration                                                                   |
| [`argocd-tls-certs-cm.yaml`](argocd-tls-certs-cm-yaml.md)             | argocd-tls-certs-cm                                                                | ConfigMap | Custom TLS certificates for connecting Git repositories via HTTPS (v1.2 and later)   |
| [`argocd-ssh-known-hosts-cm.yaml`](argocd-ssh-known-hosts-cm-yaml.md) | argocd-ssh-known-hosts-cm                                                          | ConfigMap | SSH known hosts data for connecting Git repositories via SSH (v1.2 and later)        |

For each specific kind of ConfigMap and Secret resource, there is only a single supported resource name (as listed in the above table) - if you need to merge things you need to do it before creating them.

!!!warning "A note about ConfigMap resources"
    Be sure to annotate your ConfigMap resources using the label `app.kubernetes.io/part-of: argocd`, otherwise Argo CD will not be able to use them.

### Multiple configuration objects

| Sample File                                                      | Kind        | Description              |
|------------------------------------------------------------------|-------------|--------------------------|
| [`application.yaml`](../user-guide/application-specification.md) | Application | Example application spec |
| [`project.yaml`](./project-specification.md)                     | AppProject  | Example project spec     |
| [`argocd-repositories.yaml`](./argocd-repositories-yaml.md)                                                                | Secret      | Repository credentials   |

For `Application` and `AppProject` resources, the name of the resource equals the name of the application or project within Argo CD. This also means that application and project names are unique within a given Argo CD installation - you cannot have the same application name for two different applications.


## Applications

The Application CRD is the Kubernetes resource object representing a deployed application instance
in an environment. It is defined by two key pieces of information:

* `source` reference to the desired state in Git (repository, revision, path, environment)
* `destination` reference to the target cluster and namespace. For the cluster one of server or name can be used, but not both (which will result in an error). Under the hood when the server is missing, it is calculated based on the name and used for any operations.

A minimal Application spec is as follows:

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: guestbook
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/argoproj/argocd-example-apps.git
    targetRevision: HEAD
    path: guestbook
  destination:
    server: https://kubernetes.default.svc
    namespace: guestbook
```

See [application.yaml](application.yaml) for additional fields. As long as you have completed the first step of [Getting Started](../getting_started.md#1-install-argo-cd), you can apply this with `kubectl apply -n argocd -f application.yaml` and Argo CD will start deploying the guestbook application.

!!! note
    The namespace must match the namespace of your Argo CD instance - typically this is `argocd`.

!!! note
    When creating an application from a Helm repository, the `chart` attribute must be specified instead of the `path` attribute within `spec.source`.

```yaml
spec:
  project: default
  source:
    repoURL: https://argoproj.github.io/argo-helm
    chart: argo
```

!!! warning
    Without the `resources-finalizer.argocd.argoproj.io` finalizer, deleting an application will not delete the resources it manages. To perform a cascading delete, you must add the finalizer. See [App Deletion](../user-guide/app_deletion.md#about-the-deletion-finalizer).

```yaml
metadata:
  finalizers:
    - resources-finalizer.argocd.argoproj.io
```

### App of Apps

You can create an app that creates other apps, which in turn can create other apps.
This allows you to declaratively manage a group of apps that can be deployed and configured in concert.

See [cluster bootstrapping](cluster-bootstrapping.md).


## Projects

The AppProject CRD is the Kubernetes resource object representing a logical grouping of applications.
It is defined by the following key pieces of information:

* `sourceRepos` reference to the repositories that applications within the project can pull manifests from.
* `destinations` reference to clusters and namespaces that applications within the project can deploy into.
* `roles` list of entities with definitions of their access to resources within the project.

!!!warning "Projects which can deploy to the Argo CD namespace grant admin access"
    If a Project's `destinations` configuration allows deploying to the namespace in which Argo CD is installed, then
    Applications under that project have admin-level access. [RBAC access](https://argo-cd.readthedocs.io/en/stable/operator-manual/rbac/)
    to admin-level Projects should be carefully restricted, and push access to allowed `sourceRepos` should be limited
    to only admins.

An example spec is as follows:

```yaml
apiVersion: argoproj.io/v1alpha1
kind: AppProject
metadata:
  name: my-project
  namespace: argocd
  # Finalizer that ensures that project is not deleted until it is not referenced by any application
  finalizers:
    - resources-finalizer.argocd.argoproj.io
spec:
  description: Example Project
  # Allow manifests to deploy from any Git repos
  sourceRepos:
  - '*'
  # Only permit applications to deploy to the guestbook namespace in the same cluster
  destinations:
  - namespace: guestbook
    server: https://kubernetes.default.svc
  # Deny all cluster-scoped resources from being created, except for Namespace
  clusterResourceWhitelist:
  - group: ''
    kind: Namespace
  # Allow all namespaced-scoped resources to be created, except for ResourceQuota, LimitRange, NetworkPolicy
  namespaceResourceBlacklist:
  - group: ''
    kind: ResourceQuota
  - group: ''
    kind: LimitRange
  - group: ''
    kind: NetworkPolicy
  # Deny all namespaced-scoped resources from being created, except for Deployment and StatefulSet
  namespaceResourceWhitelist:
  - group: 'apps'
    kind: Deployment
  - group: 'apps'
    kind: StatefulSet
  roles:
  # A role which provides read-only access to all applications in the project
  - name: read-only
    description: Read-only privileges to my-project
    policies:
    - p, proj:my-project:read-only, applications, get, my-project/*, allow
    groups:
    - my-oidc-group
  # A role which provides sync privileges to only the guestbook-dev application, e.g. to provide
  # sync privileges to a CI system
  - name: ci-role
    description: Sync privileges for guestbook-dev
    policies:
    - p, proj:my-project:ci-role, applications, sync, my-project/guestbook-dev, allow
    # NOTE: JWT tokens can only be generated by the API server and the token is not persisted
    # anywhere by Argo CD. It can be prematurely revoked by removing the entry from this list.
    jwtTokens:
    - iat: 1535390316
```
