<!-- Converted from opa-gatekeeper.txt (reStructuredText). Includes are inlined. -->

# Apply OPA Gatekeeper Policies

To control, audit, and debug your production deployments, you can use policies
for the [Gatekeeper](https://github.com/open-policy-agent/gatekeeper)
Open Policy Agent (OPA). Gatekeeper contains [CustomResourceDefinitions](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/) for creating and extending
deployment constraints through the
[constraint templates](https://open-policy-agent.github.io/gatekeeper/website/docs/constrainttemplates/).

## Control Your Deployments with Gatekeeper Policies

The Kubernetes Operator offers a list of Gatekeeper policies
that you can customize and apply to your deployments.

Each Gatekeeper policy consists of:

- `<policy_name>.yaml` file
- `constraints.yaml` file that is based on the [constraint template](https://open-policy-agent.github.io/gatekeeper/website/docs/constrainttemplates/)

You can use binary and configurable Gatekeeper policies:

- Binary policies allow or prevent specific configurations, such as
  preventing deployments that don't use TLS, or deploying only specific
  MongoDB or Ops Manager versions.

- Configurable policies allow you to specify configurations, such as the
  total number of replica sets that will be deployed for a specific
  MongoDB or Ops Manager custom resource.

To use and apply Gatekeeper sample policies with the Kubernetes Operator:

1. [Install the OPA Gatekeeper](https://open-policy-agent.github.io/gatekeeper/website/docs/install/) on your Kubernetes cluster.

2. Review the list of available constraint templates and constraints:

   ```sh
   kubectl get constrainttemplates
   kubectl get constraints
   ```

3. Navigate to the policy directory, select a policy from the list and
   apply it and its constraints file:

   ```sh
   cd <policy_directory>
   kubectl apply -f <policy_name>.yaml
   kubectl apply -f constraints.yaml
   ```

4. Review the Gatekeeper policies that are currently applied:

   ```sh
   kubectl get constrainttemplates
   kubectl get contstraints
   ```

### List of Sample OPA Gatekeeper Policies

The Kubernetes Operator offers the following sample policies in this
OPA examples
GitHub directory:

| Location | Policy Description |
|---|---|
| Debugging | Blocks all MongoDB and Ops Manager resources. This allows you to use the log output to craft your own policies. To learn more, see [Gatekeeper Debugging](https://open-policy-agent.github.io/gatekeeper/website/docs/debug/). |
| mongodb_allow_replicaset | Allows deploying only replica sets for MongoDB resources and prevents deploying sharded clusters. |
| mongodb_allowed_versions | Allows deploying only specific MongoDB versions. |
| ops_manager_allowed_versions | Allows deploying only specific Ops Manager versions. |
| mongodb_strict_tls | Allows using strict TLS mode for MongoDB deployments. |
| ops_manager_replica_members | Allows deploying a specified number of Ops Manager replica set and Application Database members. |
| ops_manager_wizardless | Allows installing Ops Manager in a non-interactive mode. |
