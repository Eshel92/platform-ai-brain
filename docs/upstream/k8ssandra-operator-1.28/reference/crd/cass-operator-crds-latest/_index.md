---
title: "cass-operator CRDs latest build"
linkTitle: "cass-operator CRDs latest build"
weight: 5
description: >
  Configuration reference for the CRDs used with cass-operator latest build.  
---

Packages:

- [cassandra.datastax.com/v1beta1](#cassandradatastaxcomv1beta1)
- [control.k8ssandra.io/v1alpha1](#controlk8ssandraiov1alpha1)

<!-- This page was over 60 KB, so its sections are separate files. -->

## Sections (in `_index.parts/`)

- `001-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 … CassandraDatacenter.spec.storageConfig.additionalVolumes[index]
- `002-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.storageConfig.additionalVolumes[index].pvcSpec … CassandraDatacenter.spec.storageC
- `003-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.storageConfig.additionalVolumes[index].volumeSource … CassandraDatacenter.spec.sto
- `004-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.storageConfig.additionalVolumes[index].volumeSource.azureDisk … CassandraDatacente
- `005-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.storageConfig.additionalVolumes[index].volumeSource.downwardAPI.items[index] … Cas
- `006-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.storageConfig.additionalVolumes[index].volumeSource.ephemeral.volumeClaimTemplate.
- `007-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.storageConfig.additionalVolumes[index].volumeSource.glusterfs … CassandraDatacente
- `008-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.storageConfig.additionalVolumes[index].volumeSource.projected.sources[index] … Cas
- `009-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.storageConfig.additionalVolumes[index].volumeSource.projected.sources[index].secre
- `010-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.storageConfig.additionalVolumes[index].volumeSource.storageos … CassandraDatacente
- `011-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.storageConfig.cassandraDataVolumeClaimSpec.selector.matchExpressions[index] … Cass
- `012-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.podTemplateSpec.spec
- `013-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.podTemplateSpec.spec.containers[index] … CassandraDatacenter.spec.podTemplateSpec.
- `014-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.podTemplateSpec.spec.containers[index].env[index].valueFrom.secretKeyRef … Cassand
- `015-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.podTemplateSpec.spec.containers[index].lifecycle.preStop.httpGet.httpHeaders[index
- `016-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.podTemplateSpec.spec.containers[index].readinessProbe.exec … CassandraDatacenter.s
- `017-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.podTemplateSpec.spec.containers[index].securityContext.seccompProfile … CassandraD
- `018-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.podTemplateSpec.spec.affinity.nodeAffinity … CassandraDatacenter.spec.podTemplateS
- `019-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.podTemplateSpec.spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringEx
- `020-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.podTemplateSpec.spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExe
- `021-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.podTemplateSpec.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDurin
- `022-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.podTemplateSpec.spec.ephemeralContainers[index].env[index] … CassandraDatacenter.s
- `023-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.podTemplateSpec.spec.ephemeralContainers[index].lifecycle.postStart.httpGet.httpHe
- `024-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.podTemplateSpec.spec.ephemeralContainers[index].livenessProbe.tcpSocket … Cassandr
- `025-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.podTemplateSpec.spec.ephemeralContainers[index].securityContext … CassandraDatacen
- `026-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.podTemplateSpec.spec.ephemeralContainers[index].startupProbe.grpc … CassandraDatac
- `027-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.podTemplateSpec.spec.initContainers[index] … CassandraDatacenter.spec.podTemplateS
- `028-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.podTemplateSpec.spec.initContainers[index].env[index].valueFrom.secretKeyRef … Cas
- `029-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.podTemplateSpec.spec.initContainers[index].lifecycle.preStop.httpGet.httpHeaders[i
- `030-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.podTemplateSpec.spec.initContainers[index].readinessProbe.exec … CassandraDatacent
- `031-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.podTemplateSpec.spec.initContainers[index].securityContext.seccompProfile … Cassan
- `032-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.podTemplateSpec.spec.os … CassandraDatacenter.spec.podTemplateSpec.spec.securityCo
- `033-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.podTemplateSpec.spec.securityContext.seLinuxOptions … CassandraDatacenter.spec.pod
- `034-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.podTemplateSpec.spec.volumes[index] … CassandraDatacenter.spec.podTemplateSpec.spe
- `035-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.podTemplateSpec.spec.volumes[index].azureFile … CassandraDatacenter.spec.podTempla
- `036-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.podTemplateSpec.spec.volumes[index].downwardAPI.items[index].resourceFieldRef … Ca
- `037-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.podTemplateSpec.spec.volumes[index].ephemeral.volumeClaimTemplate.spec.resources …
- `038-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.podTemplateSpec.spec.volumes[index].image … CassandraDatacenter.spec.podTemplateSp
- `039-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.podTemplateSpec.spec.volumes[index].projected.sources[index].clusterTrustBundle.la
- `040-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.podTemplateSpec.spec.volumes[index].rbd … CassandraDatacenter.spec.racks[index]
- `041-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.racks[index].affinity … CassandraDatacenter.spec.racks[index].affinity.podAffinity
- `042-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.racks[index].affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution[
- `043-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.racks[index].affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution[i
- `044-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.spec.racks[index].affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecuti
- `045-cassandra-datastax-com-v1beta1-cassandradatacenter.md`: cassandra.datastax.com/v1beta1 › CassandraDatacenter.status.trackedTasks[index]
- `046-control-k8ssandra-io-v1alpha1.md`: control.k8ssandra.io/v1alpha1
