<!-- Converted from tutorial/deploy-prometheus.txt (reStructuredText). Includes are inlined. -->

# Deploy a Resource to Use with Prometheus

You can use the mongodb-prometheus-sample.yaml file to deploy a MongoDB resource in your
Kubernetes cluster, with a ServiceMonitor
to indicate to Prometheus how to consume metrics data from 
it.

The sample specifies a simple MongoDB resource with one user,
and the `spec.prometheus` attribute with basic HTTP 
authentication and no TLS (Transport Layer Security). The sample lets you test
the metrics that MongoDB sends to Prometheus.

**Note:**

You can't use Prometheus with a multi-Kubernetes-cluster deployment.

## Quick Start

We tested this setup with version 0.54 of the 
Prometheus Operator.

### Prerequisites

* Kubernetes 1.16+
* Helm 3+

### Install the Prometheus Operator

You can install the Prometheus Operator using Helm. To learn 
more, see the installation instructions.

To install the Prometheus Operator using Helm, run the 
following commands:

```sh
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
```

```sh
helm repo update
```

```sh
helm install prometheus prometheus-community/kube-prometheus-stack \ 
  --namespace <prometheus-system> \   
  --create-namespace
```

### Install the MongoDB Controllers for Kubernetes Operator

Run the following command to install the Kubernetes Operator and create a 
namespace to contain the Kubernetes Operator and resources:

```sh
helm install mongodb-kubernetes-operator mongodb/mongodb-kubernetes \ 
  --namespace <mongodb> --create-namespace
```

To learn more, see install-k8s.

## Create a MongoDB Resource

You can use the mongodb-prometheus-sample.yaml file to deploy a MongoDB resource in your
Kubernetes cluster, with a ServiceMonitor
to indicate to Prometheus how to consume metrics data from 
it.

You can apply the sample directly with the following command:

**Note:**

Specify the full path to the mongodb-prometheus-sample.yaml file. Ensure you specify 
`spec.credentials` and 
`spec.cloudManager.configMapRef.name`.

```sh
kubectl apply -f <mongodb-prometheus-sample.yaml>
```

This command creates two [secrets](https://kubernetes.io/docs/concepts/configuration/secret/) that contain authentication 
for a new MongoDB user and basic HTTP authentication for the 
Prometheus endpoint. The command creates both [secrets](https://kubernetes.io/docs/concepts/configuration/secret/) in the 
`mongodb` namespace.

This command also creates a ServiceMonitor that 
configures Prometheus to consume this resource's metrics. This command 
creates the `ServiceMonitor` in the `prometheus-system`
namespace.

## Optional: Enable TLS on the Prometheus Endpoint

### Install Cert-Manager

1. To install [cert-manager](https://cert-manager.io/) using Helm, 
   see the [cert-manager installation documentation](https://cert-manager.io/docs/installation/helm/).

#. To create a cert-manager `Issuer`, see the 
   [cert-manager configuration documentation](https://cert-manager.io/docs/configuration/)
   
#. To create a certificate, see the [cert-manager usage documentation](https://cert-manager.io/docs/usage/).

### Enable TLS on the MongoDB CRD

**Important:**

Do **NOT** use this configuration in Production 
environments! A security expert should advise you about how to 
configure TLS (Transport Layer Security).

To enable TLS (Transport Layer Security), you must add a new entry to the
`spec.prometheus` section of the MongoDB custom resource. Run 
the following `patch`
operation to add the needed entry.

**Note:**

`tlsSecretKeyRef.name` points at a [secret](https://kubernetes.io/docs/concepts/configuration/secret/) of type 
`kubernetes.io/tls` that holds a **Server certificate**.

```sh
kubectl patch mdbc mongodb --type='json' \
  -p='[{"op": "add", "path": "/spec/prometheus/tlsSecretKeyRef", "value":{"name": "prometheus-target-cert"}}]' \
  --namespace mongodb
```

The following response appears:

```sh
mongodbenterprise.mongodbenterprise.mongodb.com/mongodb patched
```

After a few minutes, the MongoDB resource should return to the 
Running phase. Now you must configure the Prometheus 
ServiceMonitor
to point to the HTTPS endpoint.

### Update ServiceMonitor

To update the ServiceMonitor, run 
the following command to patch the resource again:

```sh
kubectl patch servicemonitors mongodb-sm --type='json' \
    -p='
[
    {"op": "replace", "path": "/spec/endpoints/0/scheme", "value": "https"},
    {"op": "add",     "path": "/spec/endpoints/0/tlsConfig", "value": {"insecureSkipVerify": true}}
]
' \
    --namespace mongodb
```

The following reponse appears:

```sh
servicemonitor.monitoring.coreos.com/mongodb-sm patched
```

With these changes, the new ServiceMonitor 
points to the HTTPS endpoint (defined in 
`/spec/endpoints/0/scheme`). You also set 
`spec/endpoints/0/tlsConfig/insecureSkipVerify` to `true`, 
so that Prometheus doesn't verify the TLS (Transport Layer Security) certificates on 
MongoDB's end.

Prometheus should now be able to scrape the MongoDB target 
using HTTPS.

## `mongodb-prometheus-sample.yaml`

Create the following `mongodb-prometheus-sample.yaml` file to deploy 
a MongoDB resource in your Kubernetes cluster, with a 
ServiceMonitor
to indicate to Prometheus how to consume metrics data from 
it.

This sample file specifies a simple MongoDB resource with one user,
and the `spec.prometheus` attribute with basic HTTP 
authentication and no TLS (Transport Layer Security). The sample lets you test
the metrics that MongoDB sends to Prometheus.

To learn more, see prometheus-settings.

```sh
---
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: my-replica-set
spec:
  members: 3
  version: 8.0.0

  cloudManager:
    configMapRef:
      name: <project-configmap>

  credentials: <credentials-secret>
  type: ReplicaSet

  persistent: true

  prometheus:
    passwordSecretRef:
      # SecretRef to a Secret with a 'password' entry on it.
      name: metrics-endpoint-password

    # change this value to your Prometheus username
    username: prometheus-username

    # Enables HTTPS on the prometheus scrapping endpoint
    # This should be a reference to a Secret type kuberentes.io/tls
    # tlsSecretKeyRef:
    #   name: <prometheus-tls-cert-secret>

    # Port for Prometheus, default is 9216
    # port: 9216
    #
    # Metrics path for Prometheus, default is /metrics
    # metricsPath: '/metrics'

---
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:

  # This needs to match `spec.ServiceMonitorSelector.matchLabels` from your
  # `prometheuses.monitoring.coreos.com` resouce.
  labels:
    release: prometheus

  name: mongodb-sm

  # Make sure this namespace is the same as in `spec.namespaceSelector`.
  namespace: mongodb
spec:
  endpoints:

  # Configuring a Prometheus Endpoint with basic Auth.
  # `prom-secret` is a Secret containing a `username` and `password` entries.
  - basicAuth:
      password:
        key: password
        name: metrics-endpoint-creds
      username:
        key: username
        name: metrics-endpoint-creds

    # This port matches what we created in our MongoDB Service.
    port: prometheus

    # If using HTTPS enabled endpoint, change scheme to https
    scheme: http

    # Configure different TLS related settings. For more information, see:
    # https://github.com/prometheus-operator/prometheus-operator/blob/v0.94.1/pkg/apis/monitoring/v1/tls_types.go#L36-L39
    # tlsConfig:
    #    insecureSkipVerify: true

  # What namespace to watch
  namespaceSelector:
    matchNames:
    # Change this to the namespace the MongoDB resource was deployed.
    - mongodb

  # Service labels to match
  selector:
    matchLabels:
      app: my-replica-set-svc

---
apiVersion: v1
kind: Secret
metadata:
  name: metrics-endpoint-creds
  namespace: mongodb
type: Opaque
stringData:
  password: 'Not-So-Secure!'
  username: prometheus-username

...
```

## Examples

The following examples show the resource definitions required to use 
Prometheus with your MongoDB resource.

### MongoDB Resource with Prometheus

To learn more, see prometheus-settings.

```sh
---
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: my-replica-set
spec:
  members: 3
  version: 8.0.0 
  cloudManager:
    configMapRef:
      name: <project-configmap>
  credentials: <credentials-secret>
  type: ReplicaSet
  persistent: true
  prometheus:
    passwordSecretRef:
      name: metrics-endpoint-password
    username: prometheus-username

...
```

### ServiceMonitor

```sh
---
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  labels:
    release: prometheus
  name: mongodb-sm
  namespace: mongodb
spec:
  endpoints:
  - basicAuth:
      password:
        key: password
        name: metrics-endpoint-creds
      username:
        key: username
        name: metrics-endpoint-creds
    port: prometheus
    scheme: http
  namespaceSelector:
    matchNames:
    - mongodb
  selector:
    matchLabels:
      app: my-replica-set-svc

...
```

### Endpoint Credentials

```sh
---
apiVersion: v1
kind: Secret
metadata:
  name: metrics-endpoint-creds
  namespace: mongodb
type: Opaque
stringData:
  password: 'Not-So-Secure!'
  username: prometheus-username

...
```
