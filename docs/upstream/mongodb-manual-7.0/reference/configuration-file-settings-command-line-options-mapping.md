<!-- Converted from reference/configuration-file-settings-command-line-options-mapping.txt (reStructuredText). Includes are inlined. -->

# Map Configuration File Settings to Command-Line Options

The following table maps the configuration file settings and the related `mongod`
and `mongos` command-line options.

| Configuration File Setting | `mongod` and `mongos` Command-Line Options |
|---|---|
| `auditLog.auditEncryptionKeyIdentifier` | \| `mongod --auditEncryptionKeyUID` \| `mongos --auditEncryptionKeyUID` |
| `auditLog.compressionMode` | \| `mongod --auditCompressionMode` \| `mongos --auditCompressionMode` |
| `auditLog.destination` | \| `mongod --auditDestination` \| `mongos --auditDestination` |
| `auditLog.filter` | \| `mongod --auditFilter` \| `mongos --auditFilter` |
| `auditLog.format` | \| `mongod --auditFormat` \| `mongos --auditFormat` |
| `auditLog.localAuditKeyFile` | \| `mongod --auditLocalKeyFile` \| `mongos --auditLocalKeyFile` |
| `auditLog.path` | \| `mongod --auditPath` \| `mongos --auditPath` |
| `net.bindIp` | \| `mongod --bind_ip` \| `mongos --bind_ip` |
| `net.bindIpAll` | \| `mongod --bind_ip_all` \| `mongos --bind_ip_all` |
| `net.compression.compressors` | \| `mongod --networkMessageCompressors` \| `mongos --networkMessageCompressors` |
| `net.ipv6` | \| `mongod --ipv6` \| `mongos --ipv6` |
| `net.maxIncomingConnections` | \| `mongod --maxConns` \| `mongos --maxConns` |
| `net.port` | \| `mongod --port` \| `mongos --port` |
| `net.tls.allowConnectionsWithoutCertificates` | \| `mongod --tlsAllowConnectionsWithoutCertificates` \| `mongos --tlsAllowConnectionsWithoutCertificates` |
| `net.tls.allowInvalidCertificates` | \| `mongod --tlsAllowInvalidCertificates` \| `mongos --tlsAllowInvalidCertificates` |
| `net.tls.allowInvalidHostnames` | \| `mongod --tlsAllowInvalidHostnames` \| `mongos --tlsAllowInvalidHostnames` |
| `net.tls.CAFile` | \| `mongod --tlsCAFile` \| `mongos --tlsCAFile` |
| `net.tls.clusterCAFile` | \| `mongod --tlsClusterCAFile` \| `mongos --tlsClusterCAFile` |
| `net.tls.certificateSelector` | \| `mongod --tlsCertificateSelector` \| `mongos --tlsCertificateSelector` |
| `net.tls.clusterCertificateSelector` | \| `mongod --tlsClusterCertificateSelector` \| `mongos --tlsClusterCertificateSelector` |
| `net.tls.clusterFile` | \| `mongod --tlsClusterFile` \| `mongos --tlsClusterFile` |
| `net.tls.clusterPassword` | \| `mongod --tlsClusterPassword` \| `mongos --tlsClusterPassword` |
| `net.tls.CRLFile` | \| `mongod --tlsCRLFile` \| `mongos --tlsCRLFile` |
| `net.tls.disabledProtocols` | \| `mongod --tlsDisabledProtocols` \| `mongos --tlsDisabledProtocols` |
| `net.tls.FIPSMode` | \| `mongod --tlsFIPSMode` \| `mongos --tlsFIPSMode` |
| `net.tls.mode` | \| `mongod --tlsMode` \| `mongos --tlsMode` |
| `net.tls.certificateKeyFile` | \| `mongod --tlsCertificateKeyFile` \| `mongos --tlsCertificateKeyFile` |
| `net.tls.certificateKeyFilePassword` | \| `mongod --tlsCertificateKeyFilePassword` \| `mongos --tlsCertificateKeyFilePassword` |
| `net.ssl.sslOnNormalPorts` | \| `--sslOnNormalPorts` \| `--sslOnNormalPorts` |
| `net.unixDomainSocket.enabled` | \| `mongod --nounixsocket` \| `mongos --nounixsocket` |
| `net.unixDomainSocket.filePermissions` | \| `mongod --filePermissions` \| `mongos --filePermissions` |
| `net.unixDomainSocket.pathPrefix` | \| `mongod --unixSocketPrefix` \| `mongos --unixSocketPrefix` |
| `net.wireObjectCheck` |  |
| `operationProfiling.mode` | \| `mongod --profile` |
| `operationProfiling.slowOpSampleRate` | \| `mongod --slowOpSampleRate` \| `mongos --slowOpSampleRate` |
| `operationProfiling.slowOpThresholdMs` | \| `mongod --slowms` \| `mongos --slowms` |
| `processManagement.fork` | \| `mongod --fork` \| `mongos --fork` |
| `processManagement.pidFilePath` | \| `mongod --pidfilepath` \| `mongos --pidfilepath` |
| `processManagement.timeZoneInfo` | \| `mongod --timeZoneInfo` \| `mongos --timeZoneInfo` |
| `processManagement.windowsService.description` | \| `mongod.exe --serviceDescription` \| `mongos.exe --serviceDescription` |
| `processManagement.windowsService.displayName` | \| `mongod.exe --serviceDisplayName` \| `mongos.exe --serviceDisplayName` |
| `processManagement.windowsService.serviceName` | \| `mongod.exe --serviceName` \| `mongos.exe --serviceName` |
| `processManagement.windowsService.servicePassword` | \| `mongod.exe --servicePassword` \| `mongos.exe --servicePassword` |
| `processManagement.windowsService.serviceUser` | \| `mongod.exe --serviceUser` \| `mongos.exe --serviceUser` |
| `replication.enableMajorityReadConcern` | \| `mongod --enableMajorityReadConcern` |
| `replication.localPingThresholdMs` | \| `mongos --localThreshold` |
| `replication.oplogSizeMB` | \| `mongod --oplogSize` |
| `replication.replSetName` | \| `mongod --replSet` |
| `security.authorization` | \| `mongod --auth` \| `mongod --noauth` |
| `security.clusterAuthMode` | \| `mongod --clusterAuthMode` \| `mongos --clusterAuthMode` |
| `security.enableEncryption` | \| `mongod --enableEncryption` |
| `security.encryptionCipherMode` | \| `mongod --encryptionCipherMode` |
| `security.encryptionKeyFile` | \| `mongod --encryptionKeyFile` |
| `security.javascriptEnabled` | \| `mongod --noscripting` \| `mongos --noscripting` |
| `security.keyFile` | \| `mongod --keyFile` \| `mongos --keyFile` |
| `security.kmip.clientCertificateFile` | \| `mongod --kmipClientCertificateFile` |
| `security.kmip.clientCertificatePassword` | \| `mongod --kmipClientCertificatePassword` |
| `security.kmip.clientCertificateSelector` | \| `mongod --kmipClientCertificateSelector` |
| `security.kmip.connectRetries` | \| `mongod --kmipConnectRetries` |
| `security.kmip.connectTimeoutMS` | \| `mongod --kmipConnectTimeoutMS` |
| `security.kmip.keyIdentifier` | \| `mongod --kmipKeyIdentifier` |
| `security.kmip.port` | \| `mongod --kmipPort` |
| `security.kmip.rotateMasterKey` | \| `mongod --kmipRotateMasterKey` |
| `security.kmip.serverCAFile` | \| `mongod --kmipServerCAFile` |
| `security.kmip.serverName` | \| `mongod --kmipServerName` |
| `security.kmip.activateKeys` | \| `mongod --kmipActivateKeys` |
| `security.kmip.keyStatePollingSeconds` | \| `mongod --kmipKeyStatePollingSeconds` |
| `security.ldap.authz.queryTemplate` | \| `mongod --ldapAuthzQueryTemplate` |
| `security.ldap.bind.method` | \| `mongod --ldapBindMethod` \| `mongos --ldapBindMethod` |
| `security.ldap.bind.queryPassword` | \| `mongod --ldapQueryPassword` \| `mongos --ldapQueryPassword` |
| `security.ldap.bind.queryUser` | \| `mongod --ldapQueryUser` \| `mongos --ldapQueryUser` |
| `security.ldap.bind.saslMechanisms` | \| `mongod --ldapBindSaslMechanisms` \| `mongos --ldapBindSaslMechanisms` |
| `security.ldap.bind.useOSDefaults` | \| `mongod --ldapBindWithOSDefaults` \| `mongos --ldapBindWithOSDefaults` |
| `security.ldap.retryCount` | \| `mongod --ldapRetryCount` \| `mongos --ldapRetryCount` |
| `security.ldap.servers` | \| `mongod --ldapServers` \| `mongos --ldapServers` |
| `security.ldap.timeoutMS` | \| `mongod --ldapTimeoutMS` \| `mongos --ldapTimeoutMS` |
| `security.ldap.transportSecurity` | \| `mongod --ldapTransportSecurity` \| `mongos --ldapTransportSecurity` |
| `security.ldap.userToDNMapping` | \| `mongod --ldapUserToDNMapping` \| `mongos --ldapUserToDNMapping` |
| `security.redactClientLogData` | \| `mongod --redactClientLogData` \| `mongos --redactClientLogData` |
| `security.sasl.hostName` | \| `mongod --setParameter saslHostName=...` \| `mongos --setParameter saslHostName=...` |
| `security.sasl.saslauthdSocketPath` | \| `mongod --setParameter saslauthdPath=...` \| `mongos --setParameter saslauthdPath=...` |
| `security.sasl.serviceName` | \| `mongod --setParameter saslServiceName=...` \| `mongos --setParameter saslServiceName=...` |
| `security.transitionToAuth` | \| `mongod --transitionToAuth` \| `mongos --transitionToAuth` |
| `setParameter` | \| `mongod --setParameter` \| `mongos --setParameter` |
| `sharding.archiveMovedChunks` | \| `mongod --moveParanoia` \| `mongod --noMoveParanoia` |
| `sharding.clusterRole` | \| `mongod --shardsvr` \| `mongod --configsvr` |
| `sharding.configDB` | \| `mongos --configdb` |
| `storage.dbPath` | \| `mongod --dbpath` |
| `storage.directoryPerDB` | \| `mongod --directoryperdb` |
| `storage.engine` | \| `mongod --storageEngine` |
| `storage.inMemory.engineConfig.inMemorySizeGB` | \| `mongod --inMemorySizeGB` |
| `storage.journal.commitIntervalMs` | \| `mongod --journalCommitInterval` |
| `storage.syncPeriodSecs` | \| `mongod --syncdelay` |
| `storage.wiredTiger.collectionConfig.blockCompressor` | \| `mongod --wiredTigerCollectionBlockCompressor` |
| `storage.wiredTiger.engineConfig.cacheSizeGB` | \| `mongod --wiredTigerCacheSizeGB` |
| `storage.wiredTiger.engineConfig.directoryForIndexes` | \| `mongod --wiredTigerDirectoryForIndexes` |
| `storage.wiredTiger.engineConfig.journalCompressor` | \| `mongod --wiredTigerJournalCompressor` |
| `storage.wiredTiger.indexConfig.prefixCompression` | \| `mongod --wiredTigerIndexPrefixCompression` |
| `systemLog.component.accessControl.verbosity` | \| `mongod --setParameter "logComponentVerbosity={accessControl: ... }"` \| `mongos --setParameter "logComponentVerbosity={accessControl: ... }"` |
| `systemLog.component.command.verbosity` | \| `mongod --setParameter "logComponentVerbosity={command: ... }"` \| `mongos --setParameter "logComponentVerbosity={command: ... }"` |
| `systemLog.component.control.verbosity` | \| `mongod --setParameter "logComponentVerbosity={control: ... }"` \| `mongos --setParameter "logComponentVerbosity={control: ... }"` |
| `systemLog.component.ftdc.verbosity` | \| `mongod --setParameter "logComponentVerbosity={ftdc: ... }"` \| `mongos --setParameter "logComponentVerbosity={ftdc: ... }"` |
| `systemLog.component.geo.verbosity` | \| `mongod --setParameter "logComponentVerbosity={geo: ... }"` \| `mongos --setParameter "logComponentVerbosity={geo: ... }"` |
| `systemLog.component.index.verbosity` | \| `mongod --setParameter "logComponentVerbosity={index: ... }"` \| `mongos --setParameter "logComponentVerbosity={index: ... }"` |
| `systemLog.component.network.verbosity` | \| `mongod --setParameter "logComponentVerbosity={network: ... }"` \| `mongos --setParameter "logComponentVerbosity={network: ... }"` |
| `systemLog.component.query.verbosity` | \| `mongod --setParameter "logComponentVerbosity={query: ... }"` \| `mongos --setParameter "logComponentVerbosity={query: ... }"` |
| `systemLog.component.replication.heartbeats.verbosity` | \| `mongod --setParameter "logComponentVerbosity={replication: {heartbeats: ... }}"` \| `mongos --setParameter "logComponentVerbosity={replication: {heartbeats: ... }}"` |
| `systemLog.component.replication.rollback.verbosity` | \| `mongod --setParameter "logComponentVerbosity={replication: {rollback: ... }}"` \| `mongos --setParameter "logComponentVerbosity={replication: {rollback: ... }}"` |
| `systemLog.component.replication.verbosity` | \| `mongod --setParameter "logComponentVerbosity={replication: ... }"` \| `mongos --setParameter "logComponentVerbosity={replication: ... }"` |
| `systemLog.component.sharding.verbosity` | \| `mongod --setParameter "logComponentVerbosity={sharding: ... }"` \| `mongos --setParameter "logComponentVerbosity={sharding: ... }"` |
| `systemLog.component.storage.journal.verbosity` | \| `mongod --setParameter "logComponentVerbosity={storage: {journal: ... }}"` \| `mongos --setParameter "logComponentVerbosity={storage: {journal: ... }}"` |
| `systemLog.component.storage.recovery.verbosity` | \| `mongod --setParameter "logComponentVerbosity={storage: {recovery: ... }}"` \| `mongos --setParameter "logComponentVerbosity={storage: {recovery: ... }}"` |
| `systemLog.component.storage.verbosity` | \| `mongod --setParameter "logComponentVerbosity={storage: ... }"` \| `mongos --setParameter "logComponentVerbosity={storage: ... }"` |
| `systemLog.component.write.verbosity` | \| `mongod --setParameter "logComponentVerbosity={write: ... }"` \| `mongos --setParameter "logComponentVerbosity={write: ... }"` |
| `systemLog.destination` | \| `mongod --logpath` \| `mongos --logpath` \| `mongod --syslog` \| `mongos --syslog` |
| `systemLog.logAppend` | \| `mongod --logappend` \| `mongos --logappend` |
| `systemLog.logRotate` | \| `mongod --logRotate` \| `mongos --logRotate` |
| `systemLog.path` | \| `mongod --logpath` \| `mongos --logpath` |
| `systemLog.quiet` | \| `mongod --quiet` \| `mongos --quiet` |
| `systemLog.syslogFacility` | \| `mongod --syslogFacility` \| `mongos --syslogFacility` |
| `systemLog.timeStampFormat` | \| `mongod --timeStampFormat` \| `mongos --timeStampFormat` |
| `systemLog.traceAllExceptions` | \| `mongod --traceExceptions` |
| `systemLog.verbosity` | \| `mongod --verbose` \| `mongos --verbose` |

## ChangeLog

Starting in version 6.1:
  MongoDB always enables journaling. As a result, MongoDB removes the 
  `storage.journal.enabled` option and the corresponding `--journal` and 
  `--nojournal` command-line options.

  
Starting in version 5.0:
  MongoDB removes the `--serviceExecutor` command-line option and the
  corresponding `net.serviceExecutor` configuration option.

  For earlier versions of MongoDB, refer to the [legacy documentation](https://www.mongodb.com/docs/legacy/).
