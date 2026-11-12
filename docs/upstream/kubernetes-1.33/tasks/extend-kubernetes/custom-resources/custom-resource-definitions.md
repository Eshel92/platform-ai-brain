---
title: Extend the Kubernetes API with CustomResourceDefinitions
reviewers:
- deads2k
- jpbetz
- liggitt
- roycaihw
- sttts
content_type: task
min-kubernetes-server-version: 1.16
weight: 20
---

<!-- overview -->
This page shows how to install a
[custom resource](/docs/concepts/extend-kubernetes/api-extension/custom-resources/)
into the Kubernetes API by creating a
[CustomResourceDefinition](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#customresourcedefinition-v1-apiextensions-k8s-io).

<!-- This page was over 60 KB, so its sections are separate files. -->

## Sections (in `custom-resource-definitions.parts/`)

- `001-heading-prerequisites-serving-multiple-versions-of.md`: {{% heading "prerequisites" %}} … Serving multiple versions of a CRD
- `002-advanced-topics.md`: Advanced topics
- `003-heading-whatsnext.md`: {{% heading "whatsnext" %}}
