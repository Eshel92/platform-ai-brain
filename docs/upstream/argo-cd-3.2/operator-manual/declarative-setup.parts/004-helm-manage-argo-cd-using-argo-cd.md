<!-- Part 4 of 4 of operator-manual/declarative-setup.md (split because the page is big). -->

## Helm

Helm charts can be sourced from a Helm repository or OCI registry.

This is an example of a Helm chart being sourced from a Helm repository. The `releaseName` property is used to customize the name of the Helm _release_.

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: sealed-secrets
  namespace: argocd
spec:
  project: default
  source:
    chart: sealed-secrets
    repoURL: https://bitnami-labs.github.io/sealed-secrets
    targetRevision: 1.16.1
    helm:
      releaseName: sealed-secrets
  destination:
    server: "https://kubernetes.default.svc"
    namespace: kubeseal
```

Another example using a public OCI helm chart:

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: nginx
spec:
  project: default
  source:
    chart: nginx
    repoURL: registry-1.docker.io/bitnamicharts  # note: the oci:// syntax is not included.
    targetRevision: 15.9.0
  destination:
    name: "in-cluster"
    namespace: nginx
```

Helm charts located in sources that require additional configuration, such as authentication or TLS connection details, are defined within a _repository_ Secret. Each Secret must specify the `url`, `type` and `name` fields. Additional fields including `username`, `password`, `tlsClientCertData` and `tlsClientCertKey` can be specified as desired.

Helm Chart Repository:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: argo-helm
  namespace: argocd
  labels:
    argocd.argoproj.io/secret-type: repository
stringData:
  name: argo
  url: https://argoproj.github.io/argo-helm
  type: helm
  username: my-username
  password: my-password
  tlsClientCertData: ...
  tlsClientCertKey: ...
```

Helm charts sourced from OCI registries should utilize the fields described previously as well as set the `enableOCI` field as `true`.

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: oci-helm-chart
  namespace: oci-helm-chart
  labels:
    argocd.argoproj.io/secret-type: repository
stringData:
  name: oci-helm-chart
  url: myregistry.example.com
  type: helm
  enableOCI: "true"
```


## Resource Exclusion/Inclusion

Resources can be excluded from discovery and sync so that Argo CD is unaware of them. For example, the apiGroup/kind `events.k8s.io/*`, `metrics.k8s.io/*` and `coordination.k8s.io/Lease` are always excluded. Use cases:

* You have temporal issues and you want to exclude problematic resources.
* There are many of a kind of resources that impacts Argo CD's performance.
* Restrict Argo CD's access to certain kinds of resources, e.g. secrets. See [security.md#cluster-rbac](security.md#cluster-rbac).

To configure this, edit the `argocd-cm` config map:

```shell
kubectl edit configmap argocd-cm -n argocd
```

Add `resource.exclusions`, e.g.:

```yaml
apiVersion: v1
data:
  resource.exclusions: |
    - apiGroups:
      - "*"
      kinds:
      - "*"
      clusters:
      - https://192.168.0.20
kind: ConfigMap
```

The `resource.exclusions` node is a list of objects. Each object can have:

* `apiGroups` A list of globs to match the API group.
* `kinds` A list of kinds to match. Can be `"*"` to match all.
* `clusters` A list of globs to match the cluster.

If all three match, then the resource is ignored.

In addition to exclusions, you might configure the list of included resources using the `resource.inclusions` setting.
By default, all resource group/kinds are included. The `resource.inclusions` setting allows customizing the list of included group/kinds:

```yaml
apiVersion: v1
data:
  resource.inclusions: |
    - apiGroups:
      - "*"
      kinds:
      - Deployment
      clusters:
      - https://192.168.0.20
kind: ConfigMap
```

The `resource.inclusions` and `resource.exclusions` might be used together. The final list of resources includes group/kinds specified in `resource.inclusions` minus group/kinds
specified in `resource.exclusions` setting.

Notes:

* Quote globs in your YAML to avoid parsing errors.
* Invalid globs result in the whole rule being ignored.
* If you add a rule that matches existing resources, these will appear in the interface as `OutOfSync`.
* Some excluded objects may already be in the controller cache. A restart of the controller will be necessary to remove them from the Application View.


## Mask sensitive Annotations on Secrets

An optional comma-separated list of `metadata.annotations` keys can be configured with `resource.sensitive.mask.annotations` to mask their values in UI/CLI on Secrets.

```yaml
  resource.sensitive.mask.annotations: openshift.io/token-secret.value, api-key
```


## Auto respect RBAC for controller

Argo CD controller can be restricted from discovering/syncing specific resources using just controller RBAC, without having to manually configure resource exclusions.
This feature can be enabled by setting `resource.respectRBAC` key in argocd cm, once it is set the controller will automatically stop watching for resources 
that it does not have the permission to list/access. Possible values for `resource.respectRBAC` are:
    - `strict` : This setting checks whether the list call made by controller is forbidden/unauthorized and if it is, it will cross-check the permission by making a `SelfSubjectAccessReview` call for the resource.
    - `normal` : This will only check whether the list call response is forbidden/unauthorized and skip `SelfSubjectAccessReview` call, to minimize any extra api-server calls.
    - unset/empty (default) : This will disable the feature and controller will continue to monitor all resources.

Users who are comfortable with an increase in kube api-server calls can opt for `strict` option while users who are concerned with higher api calls and are willing to compromise on the accuracy can opt for the `normal` option.

Notes:

* When set to use `strict` mode controller must have RBAC permission to `create` a `SelfSubjectAccessReview` resource 
* The `SelfSubjectAccessReview` request will be only made for the `list` verb, it is assumed that if `list` is allowed for a resource then all other permissions are also available to the controller.

Example argocd cm with `resource.respectRBAC` set to `strict`:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: argocd-cm
data:
  resource.respectRBAC: "strict"
```


## Resource Custom Labels

Custom Labels configured with `resource.customLabels` (comma separated string) will be displayed in the UI (for any resource that defines them).


## Labels on Application Events

An optional comma-separated list of `metadata.labels` keys can be configured with `resource.includeEventLabelKeys` to add to Kubernetes events generated for Argo CD Applications. When events are generated for Applications containing the specified labels, the controller adds the matching labels to the event. This establishes an easy link between the event and the application, allowing for filtering using labels. In case of conflict between labels on the Application and AppProject, the Application label values are prioritized and added to the event.

```yaml
  resource.includeEventLabelKeys: team,env*
```

To exclude certain labels from events, use the `resource.excludeEventLabelKeys` key, which takes a comma-separated list of `metadata.labels` keys.

```yaml
  resource.excludeEventLabelKeys: environment,bu
```

Both `resource.includeEventLabelKeys` and `resource.excludeEventLabelKeys` support wildcards.


## SSO & RBAC

* SSO configuration details: [SSO](./user-management/index.md)
* RBAC configuration details: [RBAC](./rbac.md)


## Manage Argo CD Using Argo CD

Argo CD is able to manage itself since all settings are represented by Kubernetes manifests. The suggested way is to create [Kustomize](https://github.com/kubernetes-sigs/kustomize)
based application which uses base Argo CD manifests from [https://github.com/argoproj/argo-cd](https://github.com/argoproj/argo-cd/tree/stable/manifests) and apply required changes on top.

Example of `kustomization.yaml`:

```yaml
# additional resources like ingress rules, cluster and repository secrets.
resources:
- github.com/argoproj/argo-cd//manifests/cluster-install?ref=stable
- clusters-secrets.yaml
- repos-secrets.yaml

# changes to config maps
patches:
- path: overlays/argo-cd-cm.yaml
```

The live example of self managed Argo CD config is available at [https://cd.apps.argoproj.io](https://cd.apps.argoproj.io) and with configuration
stored at [argoproj/argoproj-deployments](https://github.com/argoproj/argoproj-deployments/tree/master/argocd).

!!! note
    You will need to sign-in using your GitHub account to get access to [https://cd.apps.argoproj.io](https://cd.apps.argoproj.io)
