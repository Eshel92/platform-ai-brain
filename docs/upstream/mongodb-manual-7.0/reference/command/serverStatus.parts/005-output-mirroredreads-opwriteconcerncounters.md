<!-- Part 5 of 11 of reference/command/serverStatus.md (split because the page is big). -->

### mirroredReads

*Available on mongod only.*

```javascript
"mirroredReads" : {
      "seen" : <num>,
      "sent" : <num>
},
```

**`mirroredReads`**

*Available on mongod only.*

A document that reports on mirrored reads.
To return `mirroredReads` information, you must
explicitly specify the inclusion:

```javascript
db.runCommand( { serverStatus: 1, mirroredReads: 1 } )
```

**`mirroredReads.processedAsSecondary`**

**New in version:** 6.2

The number of mirrored reads processed by this member while a secondary.

**See also:**

`mirrorReads` Parameter

**`mirroredReads.seen`**

The number of operations that support mirroring received by this member.

**See also:**

`mirrorReads` Parameter

**`mirroredReads.sent`**

The number of mirrored reads sent by this member when primary.
For example, if a read is mirrored and sent to two secondaries,
the number of mirrored reads is `2`.

**See also:**

`mirrorReads` Parameter


### network

```javascript
network : {
   bytesIn : Long("<num>"),
   bytesOut : Long("<num>"),
   physicalBytesIn : Long("<num>"),
   physicalBytesOut : Long("<num>"),
   numSlowDNSOperations : Long("<num>"),
   numSlowSSLOperations : Long("<num>"),
   numRequests : Long("<num>"),
   tcpFastOpen : {
      kernelSetting : Long("<num>"),
      serverSupported : <bool>,
      clientSupported : <bool>,
      accepted : Long("<num>")
   },
   compression : {
      snappy : {
         compressor : { bytesIn : Long("<num>"), bytesOut : Long("<num>") },
         decompressor : { bytesIn : Long("<num>"), bytesOut : Long("<num>") }
      }, 
      zstd : { 
         compressor : { bytesIn : Long("<num>"), bytesOut : Long("<num>") },
         decompressor : { bytesIn : Long("<num>"), bytesOut : Long("<num>") }
      },
      zlib : {
         compressor : { bytesIn : Long("<num>"), bytesOut : Long("<num>") },
         decompressor : { bytesIn : Long("<num>"), bytesOut : Long("<num>") }
      }
   },
   serviceExecutors : {
      passthrough : {
         threadsRunning : <num>,
         clientsInTotal : <num>,
         clientsRunning : <num>,
         clientsWaitingForData : <num>
      },
      fixed : {
         threadsRunning : <num>,
         clientsInTotal : <num>,
         clientsRunning : <num>,
         clientsWaitingForData : <num>
      }
   },
   listenerProcessingTime : { durationMicros : <num> }  // Added in MongoDB 6.3
}
```

**`network`**

A document that reports data on MongoDB's network use. These
statistics measure *ingress connections* only, specifically the
traffic seen by the `mongod` or `mongos`
over network connections initiated by clients or other
`mongod` or `mongos` instances. Traffic
from network connections initiated by this `mongod` or
`mongos` instance (specifically, *egress connections*)
is *not* measured in these statistics.

**`network.bytesIn`**

The total number of logical bytes that the server has *received* over 
network connections initiated by clients or other `mongod` or
`mongos` instances. Logical bytes are the exact number of bytes
that a given file contains.

**`network.bytesOut`**

The total number of logical bytes that the server has *sent* over 
network connections initiated by clients or other `mongod` or
`mongos` instances. Logical bytes correspond to the number of 
bytes that a given file contains.

**`network.physicalBytesIn`**

The total number of physical bytes that the server has *received* 
over network connections initiated by clients or other `mongod` or
`mongos` instances. Physical bytes are the number of bytes that 
actually reside on disk.

**`network.physicalBytesOut`**

The total number of physical bytes that the server has *sent* over 
network connections initiated by clients or other `mongod` or
`mongos` instances. Physical bytes are the number of bytes that 
actually reside on disk.

**`network.numSlowDNSOperations`**

The total number of DNS resolution operations which took longer than
1 second.
  

**`network.numSlowSSLOperations`**

The total number of SSL handshake operations which took longer than
1 second.

**`network.numRequests`**

The total number of distinct requests that the server has received.
Use this value to provide context for the
`network.bytesIn` and `network.bytesOut`
values to ensure that MongoDB's network utilization is consistent
with expectations and application use.

**`network.tcpFastOpen`**

A document that reports data on MongoDB's support and use of 
TCP Fast Open (TFO) connections.

**`network.tcpFastOpen.kernelSetting`**

*Linux only* 

Returns the value of `/proc/sys/net/ipv4/tcp_fastopen`:

- `0` - TCP Fast Open is disabled on the system.

- `1` - TCP Fast Open is enabled for outgoing connections.

- `2` - TCP Fast Open is enabled for incoming connections.

- `3` - TCP Fast Open is enabled for incoming and outgoing 
  connections. 

**`network.tcpFastOpen.serverSupported`**

- Returns `true` if the host operating system supports inbound
  TCP Fast Open (TFO) connections.

- Returns `false` if the host operating system does *not* support
  inbound TCP Fast Open (TFO) connections.

**`network.tcpFastOpen.clientSupported`**

- Returns `true` if the host operating system supports outbound
  TCP Fast Open (TFO) connections.

- Returns `false` if the host operating system does *not* support
  outbound TCP Fast Open (TFO) connections.

**`network.tcpFastOpen.accepted`**

The total number of accepted incoming TCP Fast Open (TFO) connections
to the `mongod` or `mongos` since the 
`mongod` or `mongos` last started.

**`network.compression`**

A document that reports on the amount of data compressed and decompressed by 
each network compressor library.

**`network.compression.snappy`**

A document that returns statistics on the number of bytes that have been 
compressed and decompressed with the snappy library.

**`network.compression.zstd`**

A document that returns statistics on the number of bytes that have been 
compressed and decompressed with the zstd library.

**`network.compression.zlib`**

A document that returns statistics on the number of bytes that have been 
compressed and decompressed with the zlib library.

**`network.serviceExecutors`**

**New in version:** 5.0

A document that reports data on the service executors, which run
operations for client requests.

**`network.serviceExecutors.passthrough`**

**New in version:** 5.0

A document that reports data about the threads and clients for the
`passthrough` service executor. The `passthrough` service
executor creates a new thread for each client and destroys the thread
after the client ends.

**`network.serviceExecutors.passthrough.threadsRunning`**

**New in version:** 5.0

Number of threads running in the `passthrough` service executor.

**`network.serviceExecutors.passthrough.clientsInTotal`**

**New in version:** 5.0

Total number of clients allocated to the `passthrough` service
executor. A client can be allocated to the `passthrough` service
executor and not currently running requests.

**`network.serviceExecutors.passthrough.clientsRunning`**

**New in version:** 5.0

Number of clients currently using the `passthrough` service
executor to run requests.

**`network.serviceExecutors.passthrough.clientsWaitingForData`**

**New in version:** 5.0

Number of clients using the `passthrough` service executor that are
waiting for incoming data from the network.

**`network.serviceExecutors.fixed`**

**New in version:** 5.0

A document that reports data about the threads and clients for the
`fixed` service executor. The `fixed` service executor has a
fixed number of threads. A thread is temporarily assigned to a client
and the thread is preserved after the client ends.

**`network.serviceExecutors.fixed.threadsRunning`**

**New in version:** 5.0

Number of threads running in the `fixed` service executor.

**`network.serviceExecutors.fixed.clientsInTotal`**

**New in version:** 5.0

Total number of clients allocated to the `fixed` service executor.
A client can be allocated to the `fixed` service executor and not
currently running requests.

**`network.serviceExecutors.fixed.clientsRunning`**

**New in version:** 5.0

Number of clients currently using the `fixed` service executor to
run requests.

**`network.serviceExecutors.fixed.clientsWaitingForData`**

**New in version:** 5.0

Number of clients using the `fixed` service executor that are
waiting for incoming data from the network.

**`network.listenerProcessingTime`**

**New in version:** 6.3

A document that reports the total time the database listener spends
allocating incoming database connection requests to dedicated
threads.

**`network.listenerProcessingTime.durationMicros`**

**New in version:** 6.3

Total time in microseconds the database listener spends allocating
incoming database connection requests to dedicated threads that
perform database operations.


### opLatencies

```javascript
opLatencies : {
   reads : <document>,
   writes : <document>,
   commands : <document>,
   transactions : <document>
},
```

**`opLatencies`**

A document containing operation latencies for the instance as a whole.
See latency-stats-document for an description of this document.

Starting in MongoDB 6.2, the `opLatencies` metric 
reports for both `mongod` and `mongos` 
instances. Latencies reported by `mongos` include operation latency
time and communication time between the `mongod` and `mongos` 
instances.

Starting in MongoDB 7.0, each category document includes
`queryableEncryptionLatencyMicros`, the total latency, in
microseconds, attributable to Queryable Encryption operations.

**`opLatencies.reads`**

Latency statistics for read requests.

**`opLatencies.writes`**

Latency statistics for write operations.

**`opLatencies.commands`**

Latency statistics for database commands.

**`opLatencies.transactions`**

Latency statistics for database transactions.


### opReadConcernCounters

**Warning:** Removed

Starting in version 5.0, `opReadConcernCounters` is
replaced by `readConcernCounters`.

*Only for mongod instances*

```javascript
opReadConcernCounters : {
   available : Long("<num>"),
   linearizable : Long("<num>"),
   local : Long("<num>"),
   majority : Long("<num>"),
   snapshot : Long("<num>"),
   none : Long("<num>")
}
```

**`opReadConcernCounters`**

*Removed in version 5.0*. Replaced by
`readConcernCounters`.

A document that reports on the read concern level specified by query operations to the
`mongod` instance since it last started.

| Specified `w` | Description |
|---|---|
| `"available"` | Number of query operations that specified read concern level `"available"`. |
| `"linearizable"` | Number of query operations that specified read concern level `"linearizable"`. |
| `"local"` | Number of query operations that specified read concern level `"local"`. |
| `"majority"` | Number of query operations that specified read concern level `"majority"`. |
| `"snapshot"` | Number of query operations that specified read concern level `"snapshot"`. |
| `"none"` | Number of query operations that did not specify a read concern level and instead used the default read concern level. |

The sum of the `opReadConcernCounters` equals
`opcounters.query`.


### opWriteConcernCounters

*Only for mongod instances*

```javascript
opWriteConcernCounters : {
   insert : {
      wmajority : Long("<num>"),
      wnum : {
         <num> :  Long("<num>"),
         ...
      },
      wtag : {
         <tag1> :  Long("<num>"),
         ...
      },
      none : Long("<num>"),
      noneInfo : {
         CWWC : {
            wmajority : Long("<num>"),
            wnum : {
               <num> :  Long("<num>"),
               ...
            },
            wtag : {
               <tag1> :  Long("<num>"),
               ...
            }
         },
         implicitDefault : {
            wmajority : Long("<num>")
            wnum : {
               <num> :  Long("<num>"),
               ...
            }
         }
      }
   },
   update : {
      wmajority : Long("<num>"),
      wnum : {
         <num> :  Long("<num>"),
         ...
      },
      wtag : {
         <tag1> :  Long("<num>"),
         ...
      },
      none : Long("<num>"),
      noneInfo : {
         CWWC : {
            wmajority : Long("<num>"),
            wnum : {
               <num> :  Long("<num>"),
               ...
            }
            wtag : {
               <tag1> :  Long("<num>"),
               ...
            }
         },
         implicitDefault : {
            wmajority : Long("<num>")
            wnum : {
               <num> :  Long("<num>"),
               ...
            }
         }
      }
   },
   delete : {
      wmajority :  Long("<num>")
      wnum : {
         <num> :  Long("<num>"),
         ...
      },
      wtag : {
         <tag1> :  Long("<num>"),
         ...
      },
      none : Long("<num>"),
      noneInfo : {
         CWWC : {
            wmajority : Long("<num>"),
            wnum : {
               <num> :  Long("<num>"),
               ...
            },
            wtag : {
               <tag1> :  Long("<num>"),
               ...
            }
         },
         implicitDefault : {
            wmajority : Long("<num>")
            wnum : {
               <num> :  Long("<num>"),
               ...
            }
         }
      }
   }
}
```

**`opWriteConcernCounters`**

A document that reports on the write concerns
specified by write operations to the
`mongod` instance since it last started.

More specifically, the `opWriteConcernCounters`
reports on the w: <value> specified by the write
operations. The journal flag option (`j`) and the timeout option
(`wtimeout`) of the write concerns does not affect the count. The
count is incremented even if the operation times out.

**Note:**

Only available when
`reportOpWriteConcernCountersInServerStatus` parameter is
set to `true` (`false` by default).

**`opWriteConcernCounters.insert`**

A document that reports on the w: <value> specified
by insert operations to the `mongod` instance since it
last started:

**Note:**

Only available when
`reportOpWriteConcernCountersInServerStatus` parameter is
set to `true` (`false` by default).

```javascript
insert : {
   wmajority : Long("<num>"),
   wnum : {
      <num> :  Long("<num>"),
      ...
   },
   wtag : {
      <tag1> :  Long("<num>"),
      ...
   },
   none : Long("<num>"),
   noneInfo : {
      CWWC : {
         wmajority : Long("<num>"),
         wnum : {},
         wtag : {}
      },
      implicitDefault : {
         wmajority : Long("<num>")
         wnum : {}
      }
   }
},
```

| Specified `w` | Description |
|---|---|
| `"wmajority"` | Number of insert operations that specified `w: "majority"`. |
| `"wnum"` | Number of insert operations that specified `w: <num> <`. The counts are grouped by the specific`<num>`. |
| `"wtag"` | Number of insert operations that specified `w: <tag> <`. The counts are grouped by the specific `<tag>`. |
| `"none"` | Number of insert operations that did not specify `w` value. These operations use the default `w` value of "majority". |
| `"noneInfo"` | .. include:: /includes/serverStatus/details-noneInfo.rst |

The sum of the `opWriteConcernCounters.insert` equals
`opcounters.insert`.

**`opWriteConcernCounters.update`**

A document that reports on the w: <value> specified
by update operations to the `mongod` instance since it
last started:

**Note:**

Only available when
`reportOpWriteConcernCountersInServerStatus` parameter is
set to `true` (`false` by default).

```javascript
update : {
   wmajority : Long("<num>"),
   wnum : {
      <num> :  Long("<num>"),
      ...
   },
   wtag : {
      <tag1> :  Long("<num>"),
      ...
   },
   none : Long("<num>"),
   noneInfo : {
      CWWC : {
         wmajority : Long("<num>"),
         wnum : {},
         wtag : {}
      },
      implicitDefault : {
         wmajority : Long("<num>")
         wnum : {}
      }
   }
},
```

| Specified `w` | Description |
|---|---|
| `"wmajority"` | Number of update operations that specified `w: "majority"`. |
| `"wnum"` | Number of update operations that specified `w: <num> <`. The counts are grouped by the specific `<num>`. |
| `"wtag"` | Number of update operations that specified `w: <tag> <`. The counts are grouped by the specific `<tag>`. |
| `"none"` | Number of update operations that did not specify `w` value. These operations use the default `w` value of `1`. |
| `"noneInfo"` | .. include:: /includes/serverStatus/details-noneInfo.rst |

The sum of the `opWriteConcernCounters.update` equals
`opcounters.update`.

**`opWriteConcernCounters.delete`**

A document that reports on the w: <value> specified
by delete operations to the `mongod` instance since it
last started:

**Note:**

Only available when
`reportOpWriteConcernCountersInServerStatus` parameter is
set to `true` (`false` by default).

```javascript
delete : {
   wmajority :  Long("<num>"),
   wnum : {
      <num> :  Long("<num>"),
      ...
   },
   wtag : {
      <tag1> :  Long("<num>"),
      ...
   },
   none : Long("<num>"),
   noneInfo : {
      CWWC : {
         wmajority : Long("<num>"),
         wnum : {},
         wtag : {}
      },
      implicitDefault : {
         wmajority : Long("<num>")
         wnum : {}
      }
   }
}
```

| Specified `w` | Description |
|---|---|
| `"wmajority"` | Number of delete operations that specified `w: "majority"`. |
| `"wnum"` | Number of delete operations that specified `w: <num> <`. The counts are grouped by the specific `<num>`. |
| `"wtag"` | Number of delete operations that specified `w: <tag> <`. The counts are grouped by the specific `<tag>`. |
| `"none"` | Number of delete operations that did not specify `w` value. These operations use the default `w` value of `1`. |
| `"noneInfo"` | .. include:: /includes/serverStatus/details-noneInfo.rst |

The sum of the `opWriteConcernCounters.delete` equals
`opcounters.delete`.
