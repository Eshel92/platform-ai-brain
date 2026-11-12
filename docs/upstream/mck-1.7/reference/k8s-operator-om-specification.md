<!-- Converted from reference/k8s-operator-om-specification.txt (reStructuredText). Includes are inlined. -->

# Ops Manager Resource Specification

The MongoDB Controllers for Kubernetes Operator
creates a containerized Ops Manager deployment from specification files
that you write.

After you create or update an Ops Manager resource specification, you
direct MongoDB Controllers for Kubernetes Operator to apply this specification to your Kubernetes
environment. Kubernetes Operator creates the services and custom Kubernetes
resources that Ops Manager requires, then deploys Ops Manager and its backing
Application Database in containers in your Kubernetes environment.

Each Ops Manager resource uses an [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) specification in YAML (Yet Another Markup Language) to
define the characteristics and settings of the deployment.

<!-- This page was over 60 KB, so its sections are separate files. -->

## Sections (in `k8s-operator-om-specification.parts/`)

- `001-examples-ops-manager-required-settings.md`: Examples … Ops Manager Required Settings
- `002-ops-manager-optional-settings.md`: Ops Manager Optional Settings
- `003-application-database-required-settings.md`: Application Database Required Settings
- `004-application-database-optional-settings.md`: Application Database Optional Settings
- `005-multi-cluster-settings.md`: Multi-Cluster Settings
