---
title: Kubernetes API Concepts
reviewers:
- smarterclayton
- lavalamp
- liggitt
content_type: concept
weight: 20
---

<!-- overview -->
The Kubernetes API is a resource-based (RESTful) programmatic interface
provided via HTTP. It supports retrieving, creating, updating, and deleting
primary resources via the standard HTTP verbs (POST, PUT, PATCH, DELETE,
GET).

For some resources, the API includes additional subresources that allow
fine-grained authorization (such as separate views for Pod details and
log retrievals), and can accept and serve those resources in different
representations for convenience or efficiency.

Kubernetes supports efficient change notifications on resources via
_watches_:
{{< glossary_definition prepend="in the Kubernetes API, watch is" term_id="watch" length="short" >}}
Kubernetes also provides consistent list operations so that API clients can
effectively cache, track, and synchronize the state of resources.

You can view the [API reference](/docs/reference/kubernetes-api/) online,
or read on to learn about the API in general.

<!-- body -->

<!-- This page was over 60 KB, so its sections are separate files. -->

## Sections (in `api-concepts.parts/`)

- `001-kubernetes-api-terminology-standard-api-terminolog.md`: Kubernetes API terminology {#standard-api-terminology} … Efficient detection of changes
- `002-streaming-lists-single-resource-api.md`: Streaming lists … Single resource API
- `003-field-validation-updates-to-existing-resources-pat.md`: Field validation … Updates to existing resources {#patch-and-apply}
- `004-resource-versions.md`: Resource versions
