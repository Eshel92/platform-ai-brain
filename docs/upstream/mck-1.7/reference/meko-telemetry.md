<!-- Converted from reference/meko-telemetry.txt (reStructuredText). Includes are inlined. -->

# Configure Kubernetes Operator Telemetry

MongoDB Controllers for Kubernetes Operator's telemetry collects aggregate usage data to
help MongoDB identify improvements with the greatest impact to customers. The 
Kubernetes Operator enables telemetry by default. 

This telemetry data helps MongoDB:

* Improve product reliability and stability.
* Optimize performance based on real-world cluster configurations.
* Ensure smooth upgrades and simplified issue resolution.

Kubernetes Operator telemetry is separate from the data collected by the MongoDB Agent
and does not depend on Ops Manager.

## Learn What the Kubernetes Operator Tracks

Kubernetes Operator telemetry tracking includes but is
not limited to the following information:

**Note:**

This list is kept up to date in alignment with iterations to the telemetry data sent, 
but might not be exhaustive or include full detail. For full insight into the telemetry 
sent to MongoDB for analysis, see view-meko-telemetry.

* - Data
  - Example Value

* - Kubernetes Operator version number
  - `1.0.0`

* - Kubernetes cluster version
  - `v1.22.0`

* - Kubernetes cluster provider
  - `gke`, `eks`, `aks`

* - Kubernetes UUID. This is the same as the UID of the `kube-system` namespace. 
    To learn more, see the [OpenTelemetry documentation](https://opentelemetry.io/docs/specs/semconv/attributes-registry/k8s/).
  - `f47ac10b-58cc-4372-a567-0e02b2c3d479` 

* - `mongodb` CRD (Custom Resource Definition) deployments and resource types. Kubernetes Operator telemetry 
    does *not* track custom deployment names.
  - Example values:

    - Architecture: `static`, `non-static` 
    - Multi-Cluster: `true`, `false` 
    - Deployment Type: `ReplicaSet`

* - Self-generated Kubernetes Operator UUID. Kubernetes Operator telemetry 
    does *not* track custom names. 
  - `d2d2c3e0-6666-4e83-1234-abcd5678efgh`

* - Telemetry send timestamps
  - `2025-02-14T15:45:34.27814598Z`

## Learn What the Kubernetes Operator Doesn't Track

Kubernetes Operator telemetry *doesn't* track:

| Data | Example |
|---|---|
| All self-set, free-text fields such as custom names or database user names. | `--clusterName MyCluster` |
| Data that could uniquely identify the company using the Kubernetes Operator. | `<hostname>:<port>` |
| API (Application Programming Interface) key values or Atlas login credentials. | `private_api_key abcdefghi123456789` |

## Required RBAC for MongoDB

MongoDB requires specific `role-based access control (RBAC)` permissions to collect telemetry.
*Do not disable these permissions*. These permissions allow MongoDB to:

* Retrieve the Kubernetes cluster UID.
* Access information for a single node to determine the cloud provider, such as EKS, GKE, or AKS.
* Query the `/version` endpoint to detect the Kubernetes server version and ensure compatibility.

Disabling these RBAC roles might lead to degraded functionality, compatibility issues, 
and reduced support effectiveness. To maintain full functionality and receive the best 
support experience, these permissions must remain enabled.

## View Your Telemetry

To review the telemetry collected by your Kubernetes Operator before it sends 
your data to MongoDB for analysis, follow these steps:

**Step 1: (Optional) Disable telemetry transmission.**

To prevent the Kubernetes Operator from sending telemetry to MongoDB before you review it, 
set mdb-operator-telemetry-send-enabled to `false`. 

Alternatively, if you use [Helm](https://helm.sh/), set operator.telemetry.send.enabled to `false`.

**Step 2: View your telemetry.**

Your telemetry is collected in a ConfigMap named `mongodb-kubernetes-operator-telemetry`. 
To view this ConfigMap, replace `<namespace>` and run:

```sh
 kubectl get configmap mongodb-kubernetes-operator-telemetry -n <namespace> -o yaml
```

Output:

```sh
- apiVersion: v1
  data:
   lastSendPayloadClusters: '[{"timestamp":"2025-02-14T15:45:34.27814598Z","source":"Clusters","properties":              {"kubernetesAPIVersion":"v1.30.4","kubernetesClusterID":"80b25668-6732-4463-93fb-61ae0487c3e8",              "kubernetesFlavour":"Unknown"}},{"timestamp":"2025-02-14T15:45:34.278149016Z","source":"Clusters","properties":              {"kubernetesAPIVersion":"v1.30.4","kubernetesClusterID":"80b25668-6732-4463-93fb-61ae0487c3e8",              "kubernetesFlavour":"Unknown"}}]'
     lastSendPayloadDeployments: '[{"timestamp":"2025-02-14T15:45:34.280318302Z","source":"Deployments","properties":              {"architecture":"non-static","deploymentUID":"ff43ecfb-d244-4639-bca9-9cbbb9fbaa56","isMultiCluster":false,              "operatorID":"4ae3880d-4bc5-495c-b5ea-ff9c9fc0bb34","type":"ReplicaSet"}}]'
     lastSendPayloadOperators: '[{"timestamp":"2025-02-14T15:45:34.270025096Z","source":"Operators","properties":              {"kubernetesClusterID":"80b25668-6732-4463-93fb-61ae0487c3e8","kubernetesClusterIDs":              ["80b25668-6732-4463-93fb-61ae0487c3e8"],"operatorID":"4ae3880d-4bc5-495c-b5ea-ff9c9fc0bb34","operatorType":"MEKO",              "operatorVersion":"67af61832ac9680007bb966b"}}]'
     lastSendTimestampClusters: Initial-Value
     lastSendTimestampDeployments: "1739377730"
     lastSendTimestampOperators: "1739377728"
     Operator-UUID: 9cc0fb41-5142-419d-b440-baae616f66d4
   kind: ConfigMap
   metadata:
     name: mongodb-kubernetes-operator-telemetry
```

**Note:**

* `lastSendPayload<type>` is the most recently collected data 
  for a cluster, deployment, or Kubernetes Operator instance.
* `lastSendTimestamp<type>` is the date and time when the Kubernetes Operator last
  sent `lastSendPayload<type>` to MongoDB for analysis. If the value is 
  `Initial-Value`, no telemetry has yet been sent to MongoDB. If you 
  disable telemetry, `Initial-Value` never changes.

## Disable Telemetry for the Kubernetes Operator

The Kubernetes Operator enables telemetry by default. You can disable Kubernetes Operator telemetry 
in the following ways:

- Add the environment variable MDB_OPERATOR_TELEMETRY_ENABLED to your Kubernetes Operator deployment 
  configuration and set to `false`. 
  

  ```yaml
  spec:
    template:
      spec:
        serviceAccountName: mongodb-kubernetes-operator
        containers:
        - name: mongodb-kubernetes-operator
          env:
          - name: MDB_OPERATOR_TELEMETRY_ENABLED
            value: "false"    
  ```

- Alternatively, if you use [Helm](https://helm.sh/), set operator.telemetry.enabled to `false`.

  ```sh
  helm template operator helm_chart --set operator.telemetry.enabled=false
  ```

## Enable Telemetry for the Kubernetes Operator

The Kubernetes Operator enables telemetry by default. If telemetry is
currently disabled, you can enable telemetry by setting the following environment variables 
to `true`, or removing the values entirely, which then defaults the settings to `true`.

- Set the environment variables `MDB_OPERATOR_TELEMETRY_ENABLED` and 
  `MDB_OPERATOR_TELEMETRY_SEND_ENABLED` in your Kubernetes Operator deployment 
  configuration to `true` or remove the values entirely, which then defaults the settings 
  to `true`. To learn more, see mdb-operator-telemetry-enabled.
  

  ```yaml
  spec:
    template:
      spec:
        serviceAccountName: mongodb-kubernetes-operator
        containers:
        - name: mongodb-kubernetes-operator
          env:
          - name: MDB_OPERATOR_TELEMETRY_ENABLED
            value: "true"
          - name: MDB_OPERATOR_TELEMETRY_SEND_ENABLED
            value: "true"     
  ```

- Alternatively, if you use [Helm](https://helm.sh/), set the following settings to `true` or remove 
  the values entirely, which then defaults the settings to `true`.
  To learn more, see helm-meko-telemetry.

  ```yaml
  operator:
    telemetry:
      # Enables telemetry. Setting this to "false" will stop all telemetry.
      enabled: true
      # Adds RBAC clusterRole for kube-system UID detection for the Kubernetes cluster UID.
      # Adds RBAC clusterRole for RBAC for nodes. We are listing exactly one node to detect the cluster provider (for example, eks).
      # Adds RBAC clusterRole for /version query for detecting Kubernetes server version. 
      installClusterRole: true
      collection:
        # Controls how often the Kubernetes Operator collects and saves the data to the telemetry ConfigMap. It doesn't control whether this data is sent to MongoDB for analysis.
        # Valid time units for frequency are "m", or "h". Anything less than one minute defaults to 1h.
        frequency: 1h
        # Enables the Kubernetes Operator to collect and send cluster-level telemetry.
        # Note: the cluster UUID is unique but random and MongoDB has no way to map this to a customer.
        clusters:
          enabled: true
        # Enables the Kubernetes Operator to collect and send deployment-level telemetry.
        deployments:
          enabled: true
        # Enables the Kubernetes Operator to collect and send Kubernetes Operator-level telemetry.
        operators:
          enabled: true
      # Enables sending the collected telemetry to MongoDB.
      send:
        enabled: true
        # Controls how often the Kubernetes Operator sends the collected the data to MongoDB for analysis.
        # Valid time units are "h". Anything less than one hour defaults to 168h, which is one week.
        frequency: 168h
  ```
