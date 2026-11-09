<!-- Converted from reference/deployment-advanced-options.txt (reStructuredText). Includes are inlined. -->

# Advanced Options for MongoDB Deployments

The following mongod and mongos configuration
options are available through the Ops Manager
Advanced Configuration Options field when you deploy
MongoDB. You select advanced options when deploying:

- replica sets
- sharded clusters
- standalone instances

The Ops Manager Advanced Configuration Options map to the MongoDB
configuration options and parameters described as follows.

**Warning:** Limited to Listed Options

If a MongoDB option isn't listed on this page, you may use
setParameter to add the setting.
Settings added in this way apply to MongoDB instances that Ops Manager
manages when those instances start up.

## Procedure

To edit Advanced Options, complete the following steps.
   
**Step 1: Navigate to the Deployment page for your project.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

**Step 2: Navigate to the Processes tab for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. Click Processes in the sidebar.

**Step 3: Click MODIFY next to the deployment that you wish to edit.**

**Step 4: Scroll to Advanced Configuration Options and click Add Option.**

**Step 5: Select the desired option and click Add.**

             

## Audit Log

| Ops Manager Interface | MongoDB Option |
|---|---|
| auditEncryptionKeyIdentifier | `auditLog.auditEncryptionKeyIdentifier` |
| compressionMode | `auditLog.compressionMode` |
| auditDestination | `auditLog.destination` |
| auditFilter | `auditLog.filter` |
| auditFormat | `auditLog.format` |
| localAuditKeyFile | `auditLog.localAuditKeyFile` |
| auditPath | `auditLog.path` |

You can add these audit log parameters with a `setParameter`
option in the Advanced Configuration Options section.

To encrypt the audit log, before you start MongoDB instances that
Ops Manager manages, add the `auditEncryptKeyWithKMIPGet` and `auditEncryptionHeaderMetadataFile` parameters in the
Advanced Configuration Options section.

## Basis Tech

| Ops Manager Interface | MongoDB Option |
|---|---|
| basisTechRootDirectory | `basisTech.rootDirectory` |

## Kerberos

| Ops Manager Interface | MongoDB Option |
|---|---|
| kerberosKeytab | `kerberos.keytab` |

## Net

| Ops Manager Interface | MongoDB Option |
|---|---|
| bind_ip | `net.bindIp` |
| httpinterface | `net.http.enabled` |
| ipv6 | `net.ipv6` |
| jsonp | `net.http.JSONPEnabled` |
| maxConns | `net.maxIncomingConnections` |
| rest | `net.http.RESTInterfaceEnabled` |
| tlsClusterFile | `net.tls.clusterFile` |
| tlsClusterPassword | `net.tls.clusterPassword` |
| tlsCRLFile | `net.tls.CRLFile` |
| tlsDisabledProtocols | `net.tls.disabledProtocols` |
| tlsLogVersions | `net.tls.logVersions` |

## Numactl

| Ops Manager Interface | MongoDB Option |
|---|---|
| numCores | `numactl.numCores` |

## Operation Profiling

| Ops Manager Interface | MongoDB Option |
|---|---|
| profile | `operationProfiling.mode` |
| slowms | `operationProfiling.slowOpThresholdMs` |
| slowOpSampleRate | `operationProfiling.slowOpSampleRate` |

## Process Management

| Ops Manager Interface | MongoDB Option |
|---|---|
| pidfilepath | `processManagement.pidFilePath` |

## Replication

| Ops Manager Interface | MongoDB Option |
|---|---|
| enableMajorityReadConcern | `replication.enableMajorityReadConcern` |
| oplogSize | `replication.oplogSizeMB` |

## Security

**Warning:**

Ops Manager doesn't support transitioning from local key encryption 
to KMIP (Key Management Interoperability) server-based encryption.

| Ops Manager Interface | MongoDB Option |
|---|---|
| clusterAuthMode | `security.clusterAuthMode` |
| enableEncryption | `security.enableEncryption` |
| encryptionCipherMode | `security.encryptionCipherMode` |
| encryptionKeyFile | `security.encryptionKeyFile` |
| javascriptEnabled | `security.javascriptEnabled` |
| kmipClientCertificateFile | `security.kmip.clientCertificateFile` |
| kmipClientCertificatePassword | `security.kmip.clientCertificatePassword` |
| kmipKeyIdentifier | `security.kmip.keyIdentifier` |
| kmipPort | `security.kmip.port` |
| kmipServerCAFile | `security.kmip.serverCAFile` |
| kmipServerName | `security.kmip.serverName` |
| saslauthdSocketPath | `security.sasl.saslauthdSocketPath` |
| saslHostname | `security.sasl.hostName` |

## Sharding

| Ops Manager Interface | MongoDB Option |
|---|---|
| autoSplit | `sharding.autoSplit` |
| chunkSize | `sharding.chunkSize` |

## Storage

| Ops Manager Interface | MongoDB Option |
|---|---|
| directoryperdb | `storage.directoryPerDB` |
| engine | `storage.engine` |
| inMemorySizeGB | `storage.inMemory.engineConfig.inMemorySizeGB` |
| journal | `storage.journal.enabled` |
| journalCommitInterval | `storage.journal.commitIntervalMs` |
| nssize | `storage.nsSize` |
| prealloc | `storage.preallocDataFiles` |
| quota | `storage.quota.enforced` |
| quotaFiles | `storage.quota.maxFilesPerDB` |
| repairpath | `storage.repairPath` |
| smallfiles | `storage.smallFiles` |
| syncdelay | `storage.syncPeriodSecs` |
| wiredTigerCacheSizeGB | `storage.wiredTiger.engineConfig.cacheSizeGB` |
| wiredTigerCollectionBlockCompressor | `storage.wiredTiger.collectionConfig.blockCompressor` |
| wiredTigerCollectionConfigString | `storage.wiredTiger.collectionConfig.configString` |
| wiredTigerDirectoryForIndexes | `storage.wiredTiger.engineConfig.directoryForIndexes` |
| wiredTigerEngineConfigString | `storage.wiredTiger.engineConfig.configString` |
| wiredTigerIndexConfigString | `storage.wiredTiger.indexConfig.configString` |
| wiredTigerIndexPrefixCompression | `storage.wiredTiger.indexConfig.prefixCompression` |
| wiredTigerJournalCompressor | `storage.wiredTiger.engineConfig.journalCompressor` |
| wiredTigerStatisticsLogDelaySecs | `storage.wiredTiger.engineConfig.statisticsLogDelaySecs` |

## System Log

| Ops Manager Interface | MongoDB Option |
|---|---|
| logappend | `systemLog.logAppend` |
| logRotate | `systemLog.logRotate` |
| quiet | `systemLog.quiet` |
| syslogDestination | `systemLog.destination` |
| syslogFacility | `systemLog.syslogFacility` |
| timeStampFormat | `systemLog.timeStampFormat` |
| verbosity | `systemLog.verbosity` |

## TLS

| Ops Manager Interface | MongoDB Option |
|---|---|
| tlsCertificateKeyFile | `net.tls.certificateKeyFile` |
| tlsCertificateKeyFilePassword | `net.tls.certificateKeyFilePassword` |
| tlsFIPSMode | `net.tls.FIPSMode` |
| tlsMode | `net.tls.mode` |

## Set Parameter

**Important:**

Ops Manager does not check to see if the parameters you provide are
valid. Check the
MongoDB Server Manual for
accepted parameters and values.

| Ops Manager Interface | MongoDB Option |
|---|---|
| [setParameter] | `setParameter.name` You can add any value from Server Parameters as a `setParameter`. |

For supported MongoDB versions and MongoDB Agent versions, you can set
certain `setParameter` parameters without a `rolling restart`.
To determine whether you can set a  `setParameter` parameter during
runtime or upon startup, retrieve details
on that parameter. For complex `setParameter` parameters, you must set
the parameter values in the same format as in the process configuration
file or in the `--setParameter` command line option.

**Note:**

If you set the watchdogPeriodSeconds
parameter, MongoDB Agent triggers a rolling restart.

If you delete or remove a parameter, MongoDB Agent keeps the parameter's
current value until you make another change to that parameter. To reset
the parameter to its default value, you must manually set the value or
trigger a rolling restart.

If you attempt to set a parameter that MongoDB Agent can't set at startup,
MongoDB Agent triggers a `rolling restart` and fails to start up a
`mongod` instance.
