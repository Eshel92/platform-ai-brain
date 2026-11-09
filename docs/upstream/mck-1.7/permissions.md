<!-- Converted from permissions.txt (reStructuredText). Includes are inlined. -->

# Verify Permissions

Objects in the Kubernetes Operator configuration use
default permissions. These are the minimum
permissions for the Kubernetes Operator to deploy and manage Ops Manager
and MongoDB resources in a Kubernetes cluster.

## Default Permissions for Kubernetes Operator Objects

Use the following chart to verify that the
objects in your Kubernetes Operator configuration have access to the
required Kubernetes `API verbs`:

* - Kubernetes Resources
  - API Verbs

* - Configmaps
  - Require the following permissions:

    - `get`, `list`, `watch`. The Kubernetes Operator reads the organization
      and project data from the specified `configmap`.

    - `create`, `update`. The Kubernetes Operator creates and updates `configmap`
      objects for configuring the appdb-om-arch instances.

    - `delete`. The Kubernetes Operator needs the `delete` `configmap` permission
      to support its [older versions](https://www.mongodb.com/legal/support-policy/software).
      This permission will be deleted when older versions reach their
      End of Life Date.

* - Secrets
  - Require the following permissions:

    - `get`, `list`, `watch`. The Kubernetes Operator reads secret objects to
      retrieve sensitive data, such as TLS or
      X.509 access information. For example, it
      reads the credentials from a secret object to connect to the Ops Manager.

    - `create`, `update`. The Kubernetes Operator creates secret
      objects holding TLS or
      X.509 access information.

    - `delete`. The Kubernetes Operator deletes secret objects (containing passwords)
      related to the appdb-om-arch.

* - Services
  - Require the following permissions:

    - `get`, `list`, `watch`. The Kubernetes Operator reads and watches
      MongoDB services. For example, to communicate with the Ops Manager service,
      the Kubernetes Operator needs `get`, `list` and `watch`
      permissions to use the Ops Manager service's URL.

    - `create`, `update`. To communicate with services, the Kubernetes Operator
      creates and updates service objects corresponding to Ops Manager
      and MongoDB custom resources.

* - StatefulSets
  - Require the following permissions:

    - `get`, `list`, `watch`. The Kubernetes Operator reacts to the changes in the
      StatefulSets it creates for the MongoDB custom resources. It also reads
      the fields of  the StatefulSets it manages.

    - `create`, `update`. The Kubernetes Operator creates and updates StatefulSets
      corresponding to the mongoDB custom resources.

    - `delete`. The Kubernetes Operator needs permissions to delete the StatefulSets
      when you delete the MongoDB custom resource.

* - Pods
  - Require the following permissions:

    - `get`, `list`, `watch`. The Kubernetes Operator queries the
      Application Database Pods to get information about its state.

* - Namespaces
  - Require the following permissions:

    - `list`, `watch`. When you run the Kubernetes Operator in the cluster-wide mode,
      it needs `list` and `watch` permissions to all namespaces
      for the MongoDB custom resources.
