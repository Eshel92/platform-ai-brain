<!-- Converted from tutorial/plan-k8s-op-prerequisites.txt (reStructuredText). Includes are inlined. -->

# Kubernetes Operator Prerequisites

## Procedure

To install the MongoDB Kubernetes Operator, you must:

**Step 1: Have a Kubernetes solution available to use, and verify hardware architecture support.**

If you need a Kubernetes solution, see the Kubernetes
`documentation on picking the right solution`.
Review supported hardware architectures.

**Step 2: Clone the MongoDB Controllers for Kubernetes Operator repository and check out the tag for the current release.**

```sh
git clone https://github.com/mongodb/mongodb-kubernetes.git
cd mongodb-kubernetes
git checkout 1.7.0
```

**Note:**

You can use [Helm](https://helm.sh/) to install the
Kubernetes Operator. To learn how to install Helm, see its
documentation on GitHub.

**Step 3: Create a [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) for your Kubernetes deployment.**

By default, The Kubernetes Operator uses the `mongodb` namespace. To
simplify your installation, consider creating a namespace labeled
`mongodb` using the following [kubectl](https://kubernetes.io/docs/reference/kubectl/kubectl/) command:

```sh
kubectl create namespace mongodb
```

If you do not want to use the `mongodb` namespace, you can label
your namespace anything you like:

```sh
kubectl create namespace <namespaceName>
```

**See also:**

k8s-deployment-scopes

**Step 4: Have a running `Ops Manager`.**

If you don't deploy an Ops Manager resource with the
Kubernetes Operator, you must have an Ops Manager running outside of your
Kubernetes cluster. If you will deploy an Ops Manager resource in Kubernetes with
the Kubernetes Operator, skip this prerequisite.

**Important:**

Your Ops Manager installation must run an active NTP (Network Time Protocol) service. If
the Ops Manager host's clock falls out of sync, that host can't
communicate with the Kubernetes Operator. 

To learn how to check your NTP (Network Time Protocol) service for your Ops Manager
host, see the documentation for [RHEL](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/s1-checking_the_status_of_ntp).
