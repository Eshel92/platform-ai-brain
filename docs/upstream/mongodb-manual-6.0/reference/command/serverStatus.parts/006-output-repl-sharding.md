<!-- Part 6 of 10 of reference/command/serverStatus.md (split because the page is big). -->

### repl

```javascript
repl : {
   hosts : [
         <string>,
         <string>,
         <string>
   ],
   setName : <string>,
   setVersion : <num>,
   isWritablePrimary : <boolean>,
   secondary : <boolean>,
   primary : <hostname>,
   me : <hostname>,
   electionId : ObjectId(""),
   primaryOnlyServices: {
      ReshardingRecipientService: { state: <string>, numInstances: <num> },
      RenameCollectionParticipantService: { state: <string>, numInstances: <num> },
      ShardingDDLCoordinator: { state: <string>, numInstances: <num> },
      ReshardingDonorService: { state: <string>, numInstances: <num> }
   },
   rbid : <num>,
   replicationProgress : [
         {
            rid : <ObjectId>,
            optime : { ts: <timestamp>, term: <num> },
            host : <hostname>,
            memberId : <num>
         },
        ...
   ]
}
```

**`repl`**

A document that reports on the replica set configuration.
`repl` only appear when the current host is a replica
set. See /replication for more information on replication.

**`repl.hosts`**

An array of the current replica set members' hostname and port
information (`"host:port"`).

**`repl.setName`**

A string with the name of the current replica set. This value
reflects the `--replSet` command line
argument, or `replSetName` value in the
configuration file.

**`repl.isWritablePrimary`**

A boolean that indicates whether the current node is the
primary of the replica set.

**`repl.secondary`**

A boolean that indicates whether the current node is a
secondary member of the replica set.

**`repl.primary`**

The hostname and port information (`"host:port"`) of the current
primary member of the replica set.

**`repl.me`**

The hostname and port information (`"host:port"`) for the current
member of the replica set.

**`repl.primaryOnlyServices`**

Document that contains the number and status of 
instances of each primary service active on the server. Primary 
services can only start when a server is primary but can continue running to 
completion after the server changes state.

**New in version:** 5.0

**`repl.primaryOnlyServices.ReshardingRecipientService`**

Document that contains the state and number of instances of the
`ReshardingRecipientService`.

Recipients are the shards,that would own the chunks after as a 
result of the resharding operation, according to the new 
shard key and 
zones.

The resharding coordinator instructs each donor and recipient shard 
primary, to rename the temporary sharded collection.
The temporary collection becomes the new resharded collection.

**New in version:** 5.0

**`repl.primaryOnlyServices.RenameCollectionParticipantService`**

Document that contains the state and number of instances of the
`RenameCollectionParticipantService`.

The `RenameCollectionParticipantService` ensures that, after a shard 
receives a 
renameCollection
request, the shard is able to resume the local rename in case of 
system failure.

**New in version:** 5.0

**`repl.primaryOnlyServices.ShardingDDLCoordinator`**

Document that contains the state and number of instances of the
`ShardingDDLCoordinator`.

The `ShardingDDLCoordinator` service manages DDL operations for 
primary
databases such as:
create database,
drop database,
renameCollection. 

The `ShardingDDLCoordinator` ensures that one DDL operation for
each database can happen at any one specific point in time within a 
sharded cluster. 

**New in version:** 5.0

**`repl.primaryOnlyServices.ReshardingDonorService`**

Document that contains the state and number of instances of the
`ReshardingDonorService`.

Donors are the shards that own chunks of the sharded collection
before the rename operation completes.

The resharding coordinator instructs each donor and recipient shard 
primary, to rename the temporary sharded collection.
The temporary collection becomes the new resharded collection.

**New in version:** 5.0

**`repl.rbid`**

Rollback identifier. Used to determine if a rollback has
happened for this `mongod` instance.

**`repl.replicationProgress`**

An array with one document for each member of the replica set that
reports replication process to this member. Typically this is the
primary, or secondaries if using chained replication.

To include this output, you must pass the `repl` option to the
`serverStatus`, as in the following:

```javascript
db.serverStatus({ "repl": 1 })
db.runCommand({ "serverStatus": 1, "repl": 1 })
```

The content of the `repl.replicationProgress` section
depends on the source of each member's replication. This section
supports internal operation and is for internal and diagnostic use only.

**`repl.replicationProgress[n].rid`**

An ObjectId used as an ID for the members of the replica
set. For internal use only.

**`repl.replicationProgress[n].optime`**

Information regarding the last operation from the oplog that
the member applied, as reported from this member.

**`repl.replicationProgress[n].host`**

The name of the host in `[hostname]:[port]` format for the member
of the replica set.

**`repl.replicationProgress[n].memberID`**

The integer identifier for this member of the replica set.


### security

```javascript
security : {
   authentication : {
      saslSupportedMechsReceived : <num>,
      mechanisms : {
         MONGODB-X509 : {
            speculativeAuthenticate : {
               received : Long("<num>"),
               successful : Long("<num>")
            },
            authenticate : {
               received : Long("<num>"),
               successful : Long("<num>")
            }
         },
         SCRAM-SHA-1 : {
            speculativeAuthenticate : {
               received : Long("<num>"),
               successful : Long("<num>")
            },
            authenticate : {
               received : Long("<num>"),
               successful : Long("<num>")
            }
         },
         SCRAM-SHA-256 : {
            speculativeAuthenticate : {
               received : Long("<num>"),
               successful : Long("<num>")
            },
            authenticate : {
               received : Long("<num>"),
               successful : Long("<num>")
            }
          }
       }
     },
     SSLServerSubjectName: <string>,
     SSLServerHasCertificateAuthority: <boolean>,
     SSLServerCertificateExpirationDate: <date>
},
```

**`security`**

A document that reports on:

- The number of times a given authentication mechanism has been used
  to authenticate against the `mongod` or
  `mongos` instance.

- The `mongod` / `mongos` instance's TLS/SSL
  certificate. (Only appears for `mongod` or
  `mongos` instance with support for TLS)

**`security.authentication.saslSupportedMechsReceived`**

**New in version:** 5.0

The number of times a `hello` request includes a valid
`hello.saslSupportedMechs` field.

**`security.authentication.mechanisms`**

A document that reports on the number of times a given
authentication mechanism has been used to authenticate against the
`mongod` or `mongos` instance. The
values in the document distinguish standard authentication and
speculative authentication. [#speculative-auth]_

**Note:**

The fields in the `mechanisms` document depend on the
configuration of the `authenticationMechanisms`
parameter. The `mechanisms` document includes a field for
each authentication mechanism supported by your
`mongod` or `mongos` instance.

The following example shows the shape of the `mechanisms`
document for a deployment that only supports X.509 authentication.

**`security.authentication.mechanisms.MONGODB-X509`**

A document that reports on the number of times
X.509 has been used to
authenticate against the
`mongod` or `mongos` instance.

Includes total number of `X.509` authentication attempts and the
subset of those attempts which were speculative.
[#speculative-auth]_

**`security.authentication.mechanisms.MONGODB-X509.speculativeAuthenticate.received`**

Number of speculative authentication attempts received using
X.509. Includes both successful and
failed speculative authentication attempts. [#speculative-auth]_

**`security.authentication.mechanisms.MONGODB-X509.speculativeAuthenticate.successful`**

Number of successful speculative authentication attempts received
using X.509. [#speculative-auth]_

**`security.authentication.mechanisms.MONGODB-X509.authenticate.received`**

Number of successful and failed authentication attempts
received using X.509.  This value includes speculative 
authentication attempts received using X.509.

**`security.authentication.mechanisms.MONGODB-X509.authenticate.successful`**

Number of successful authentication attempts received using
x.508. This value includes successful speculative authentication 
attempts which used X.509.

**`security.SSLServerSubjectName`**

The subject name associated with the
`mongod` / `mongos` instance's TLS/SSL
certificate.

**`security.SSLServerHasCertificateAuthority`**

A boolean that is:

- `true` when the `mongod` / `mongos`
  instance's TLS/SSL certificate is associated with a certificate
  authority.

- `false` when the TLS/SSL certificate is self-signed.

**`security.SSLServerCertificateExpirationDate`**

The expiration date and time of the
`mongod` / `mongos` instance's TLS/SSL
certificate.


### sharding

```javascript
{
   configsvrConnectionString : 'csRS/cfg1.example.net:27019,cfg2.example.net:27019,cfg2.example.net:27019',
   lastSeenConfigServerOpTime : {
      ts : <timestamp>,
      t : Long("<num>")
   },
   maxChunkSizeInBytes : Long("<num>")
}
```

**`sharding`**

A document with data regarding the sharded cluster. The
`lastSeenConfigServerOpTime` is present only
for a `mongos` or a shard member, not for a config
server.

**`sharding.configsvrConnectionString`**

The connection string for the config servers.

**`sharding.lastSeenConfigServerOpTime`**

The latest optime of the CSRS primary that the `mongos` or
the shard member has seen. The optime document includes:

- `ts`, the Timestamp of
  the operation.

- `t`, the `term` in which the
  operation was originally generated on the primary.

The `lastSeenConfigServerOpTime` is present
only if the sharded cluster uses CSRS.

**`sharding.maxChunkSizeInBytes`**

The maximum size limit for a range to
migrate. If this value has been updated recently on the config 
server, the `maxChunkSizeInBytes` may not 
reflect the most recent value.
