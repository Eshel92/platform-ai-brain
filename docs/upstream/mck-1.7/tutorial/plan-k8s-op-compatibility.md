<!-- Converted from tutorial/plan-k8s-op-compatibility.txt (reStructuredText). Includes are inlined. -->

# MongoDB Controllers for Kubernetes Operator Compatibility

**Note:**

The Kubernetes Operator doesn't support Kubernetes versions that have reached 
End of Life (EOL).

## Kubernetes and OpenShift Versions

The Kubernetes Operator is compatible with the following Kubernetes and OpenShift
versions. Unless otherwise noted, each Kubernetes Operator version listed
spans the full release series starting from the listed version.

| Kubernetes Operator Release Series | Release Date | Kubernetes Version | OpenShift Version |
|---|---|---|---|
| 1.7.0 | February 10, 2026 | 1.33, 1.34, 1.35 | 4.20, 4.21, 4.22 |
| 1.6.1 | December 16, 2025 | 1.32, 1.33, 1.34 | 4.19, 4.20, 4.21 |
| 1.6.0 | November 17, 2025 | 1.32, 1.33, 1.34 | 4.19, 4.20, 4.21 |
| 1.5.0 | November 15, 2025 | 1.32, 1.33, 1.34 | 4.19, 4.20, 4.21 |
| 1.4.0 | September 17, 2025 | 1.31, 1.32, 1.33 | 4.18, 4.19, 4.20 |
| 1.3.0 | September 4, 2025 | 1.31, 1.32, 1.33 | 4.18, 4.19, 4.20 |
| 1.2.0 | July 10, 2025 | 1.29, 1.30, 1.31 | 4.16, 4.17, 4.18 |
| 1.1.0 | May 23, 2025 | 1.29, 1.30, 1.31 | 4.16, 4.17, 4.18 |
| 1.0.1 | May 14, 2025 | 1.29, 1.30, 1.31 | 4.16, 4.17, 4.18 |
| 1.0.0 | May 6, 2025 | 1.29, 1.30, 1.31 | 4.16, 4.17, 4.18 |

## Supported Kubernetes Cluster Naming Conventions

The Kubernetes Operator supports only Kubernetes cluster names that consist of 
alphanumeric characters, dashes, underscores, and periods. 

If your cluster name contains unsupported characters, you must [rename your cluster](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/kubectl_config_rename-context/) 
to a supported name. For example, if you are deploying the Kubernetes Operator in an AWS (Amazon Web Services) 
[EKS](https://docs.aws.amazon.com/eks/latest/userguide/clusters.html) cluster, you must rename the 
cluster as the default name contains unsupported characters.

## Other Distributions of Kubernetes

The Kubernetes Operator is also compatible with all
[CNCF-certified distributions](https://www.cncf.io/certification/software-conformance/)
of Kubernetes and core Kubernetes features. The distribution version 
must match one of the base Kubernetes versions supported by the Kubernetes Operator.

To learn which Kubernetes versions are supported by your Kubernetes Operator series,
see the preceding OpenShift versions table.

## Supported Platforms and MongoDB Versions

The Kubernetes Operator is compatible with different versions of MongoDB
depending on the base image of the MongoDB database resource.

The Kubernetes Operator is compatible with actively supported versions of
MongoDB.

The Kubernetes Operator isn't compatible with MongoDB versions that
have reached end of life, or that are listed on the [MongoDB Alerts](https://www.mongodb.com/alerts) page. To learn more about
which MongoDB versions your base image supports, see
Platform Support
in the MongoDB Manual.

Unless otherwise noted, each Kubernetes Operator version listed spans the
full release series starting from the listed version.

| Kubernetes Operator Release Series | Base Image |
|---|---|
| 1.0.0, 1.1.0, 1.2.0, 1.3.0, 1.4.0, 1.5.0, 1.6.0 | Red Hat UBI 9 Base Image |

## Supported Hardware Architectures

Kubernetes nodes must be running processors with the following hardware architectures:

**Important:**

While the Kubernetes Operator supports the hardware architectures listed below,
some container images have limitations for specific architectures.
To learn more, see k8s-container-images. 

- x86-64/AMD64
- ARM64
- IBM ZSeries (s390x)
- IBM Power (ppc64le)

## Cloud Manager and Ops Manager Versions

The Kubernetes Operator is compatible with Cloud Manager and with the
following Ops Manager versions. To learn about MongoDB Agent compatibility,
see ops-manager-agent-compatibility.

Unless otherwise noted, each Kubernetes Operator
version listed spans the full release series starting from the listed
version.

| Kubernetes Operator Release Series | Ops Manager Version |
|---|---|
| 1.0.0, 1.1.0, 1.2.0, 1.3.0, 1.4.0, 1.5.0, 1.6.0, 1.7.0 | 7.0, 8.0 |

**See also:**

[End of Life (EOL) dates for the MongoDB Kubernetes Operator](https://www.mongodb.com/legal/support-policy/lifecycles/).
