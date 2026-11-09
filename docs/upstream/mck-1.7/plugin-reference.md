<!-- Converted from plugin-reference.txt (reStructuredText). Includes are inlined. -->

# MongoDB Plugin Reference

Use the `kubectl mongodb` plugin to:

- Set up multi-Kubernetes-cluster Deployments
- Run automatic and manual disaster recovery

Before you begin, install the kubectl mongodb plugin.

The `kubectl mongodb` plugin has the following subcommands:

- kubectl-mongodb-mc-setup
- kubectl-mongodb-mc-recover

## setup Subcommand

The `kubectl mongodb multicluster setup` subcommand sets up the initial multi-Kubernetes cluster MongoDB deployment.
It performs the following actions:

- Creates a default ConfigMap named `mongodb-kubernetes-operator-member-list`
  that contains all the member clusters of the multi-Kubernetes cluster MongoDB deployment. This name is
  hard-coded and you can't change it. See Known Issues.
- Creates `ServiceAccounts`,
  `Roles, ClusterRoles`,
  `RoleBindings and ClusterRoleBindings`
  in the central cluster and
  each member cluster.
- Applies the correct permissions for service accounts.
- Uses the preceding settings to create your multi-Kubernetes cluster MongoDB deployment.

### setup Subcommand Options

The `setup` subcommand of the `kubectl mongodb` plugin has the following options:

| Option | Data Type | Description |
|---|---|---|
| `central-cluster` | string | .. include:: /includes/list-tables/plugin-central-cluster.rst |
| `central-cluster-namespace` | string | .. include:: /includes/list-tables/plugin-central-cluster-ns.rst |
| `cleanup` | boolean | .. include:: /includes/list-tables/plugin-cleanup.rst |
| `cluster-scoped` | boolean | .. include:: /includes/list-tables/plugin-cluster-scoped.rst |
| `create-service-account-secrets` | boolean | Optional. Flag that indicates whether to create secrets for the [service accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) in the [Kubernetes API server](https://kubernetes.io/docs/concepts/overview/components/#kube-apiserver). Default value is `false`. |
| `install-database-roles` | boolean | Optional. Flag that indicates whether to install the Service accounts and roles required for running MongoDB workloads on the member clusters. Default value is `false`. |
| `image-pull-secrets` | boolean | Optional. Flag that indicates whether the service accounts that the `kubectl mongodb` plugin creates should reference the secret you specified in the registry.imagePullSecrets setting. Default value is `false`. To learn more, see Helm installation settings. |
| `member-clusters` | string | Required. Comma-separated list that contains member clusters, such as: `-member-clusters="${MDB_CLUSTER_2_FULL_NAME}, ${MDB_CLUSTER_3_FULL_NAME}, ${MDB_CLUSTER_4_FULL_NAME}"`. |
| `member-cluster-namespace` | string | Required. Namespace that the member cluster resources will be deployed to, such as: `-member-cluster-namespace="mongodb"`. |
| `service-account` | string | Optional. Name of the service account for the Kubernetes Operator to use to communicate with the member clusters. Default value is `mongodb-kubernetes-operator-multi-cluster`. |

For a full example of the `kubectl mongodb` plugin `setup` subcommand's usage,
see the multi-Kubernetes-cluster quick start.

## recover Subcommand

The `kubectl mongodb multicluster` subcommand can automatically recover a
failed cluster topology in some cases. In other cases, you must
manually recover from a failure. To
learn more, see disaster-recovery-ref.

### recover Subcommand Options

The `recover` subcommand of the `kubectl mongodb` plugin has the following options:

| Option | Data Type | Description |
|---|---|---|
| `central-cluster` | string | .. include:: /includes/list-tables/plugin-central-cluster.rst |
| `central-cluster-namespace` | string | .. include:: /includes/list-tables/plugin-central-cluster-ns.rst |
| `cleanup` | boolean | .. include:: /includes/list-tables/plugin-cleanup.rst |
| `cluster-scoped` | boolean | .. include:: /includes/list-tables/plugin-cluster-scoped.rst |

For a full example of the `kubectl mongodb` plugin `recover` subcommand's usage,
see the manual disaster recovery procedure.
