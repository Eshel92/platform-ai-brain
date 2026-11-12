<!-- Part 5 of 7 of reference/k8s-operator-specification.md (split because the page is big). -->

## Prometheus Settings

You can use Prometheus with your replica sets or sharded clusters.
Prometheus monitoring is not supported for standalone resources. To
monitor a single-node deployment with Prometheus, deploy a
single-member replica set instead. To learn more, see
deploy-prometheus. To view an example, see
mdb-resource-prometheus.

The following settings apply when you use Prometheus 
with your MongoDB resource:

**`spec.prometheus`**

*Type*: array

*Optional*

List that contains the parameters for exposing metrics to Prometheus.

**`spec.prometheus.metricsPath`**

*Type*: string

*Optional*

*Default*: `"/metrics"`

Human-readable string that indicates the path to the metrics 
endpoint. If you don't specify this setting, the default applies.

**`spec.prometheus.passwordSecretRef`**

*Type*: object

*Conditional*

Object that contains the details of the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) for 
basic HTTP authentication. If you want to use Prometheus with your 
MongoDB resource, you must specify this setting.

**`spec.prometheus.passwordSecretRef.key`**

*Type*: string

*Optional*

*Default*: `"password"`

Human-readable string that indentifies the key in the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) 
that stores the password for basic HTTP authentication. If you don't 
specify this setting, the default applies.

**`spec.prometheus.passwordSecretRef.name`**

*Type*: string

*Conditional*

Human-readable label that identifies the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that contains 
the password for basic HTTP authentication. If you want to use 
Prometheus with your MongoDB resource, you must specify this setting.

**`spec.prometheus.port`**

*Type*: integer

*Optional*

*Default:* 9216

Number that identifies the port that the metrics endpoint will 
bind to. If you don't specify this setting, the default applies.

**`spec.prometheus.tlseSecretKeyRef`**

*Type*: object

*Optional*

Object that contains the details of the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) for TLS (Transport Layer Security) 
authentication.

**`spec.prometheus.tlseSecretKeyRef.key`**

*Type*: string

*Optional*

*Default*: `"password"`

Human-readable string that indentifies the key in the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) 
that stores the password for TLS (Transport Layer Security) authentication. If you don't 
specify this setting, the default applies.

**`spec.prometheus.tlseSecretKeyRef.name`**

*Type*: string

*Conditional*

Human-readable label that identifies the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that contains 
the password for TLS (Transport Layer Security) authentication. If you want to use 
Prometheus with your MongoDB resource and you want to use TLS (Transport Layer Security) 
authentication, you must specify this setting.

**`spec.prometheus.username`**

*Type*: string

*Conditional*

Human-readable label that identifies the user for basic HTTP 
authentication. If you want to use Prometheus with your MongoDB 
resource, you must specify this setting.
