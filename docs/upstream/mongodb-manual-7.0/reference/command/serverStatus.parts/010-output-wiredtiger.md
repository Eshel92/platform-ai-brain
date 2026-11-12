<!-- Part 10 of 11 of reference/command/serverStatus.md (split because the page is big). -->

### wiredTiger

`wiredTiger` information only appears if using the
WiredTiger storage engine. Some of the statistics roll up for the server.

```javascript
{
   uri : 'statistics:',
   async : {
      current work queue length : <num>,
      maximum work queue length : <num>,
      number of allocation state races : <num>,
      number of flush calls : <num>,
      number of operation slots viewed for allocation : <num>,
      number of times operation allocation failed : <num>,
      number of times worker found no work : <num>,
      total allocations : <num>,
      total compact calls : <num>,
      total insert calls : <num>,
      total remove calls : <num>,
      total search calls : <num>,
      total update calls : <num>
   },
   block-manager : {
      blocks pre-loaded : <num>,
      blocks read : <num>,
      blocks written : <num>,
      bytes read : <num>,
      bytes written : <num>,
      bytes written for checkpoint : <num>,
      mapped blocks read : <num>,
      mapped bytes read : <num>
   },
   cache : {
      application threads page read from disk to cache count : <num>,
      application threads page read from disk to cache time (usecs) : <num>,
      application threads page write from cache to disk count : <num>,
      application threads page write from cache to disk time (usecs) : <num>,
      bytes belonging to page images in the cache : <num>,
      bytes belonging to the cache overflow table in the cache : <num>,
      bytes currently in the cache : <num>,
      bytes dirty in the cache cumulative : <num>,
      bytes not belonging to page images in the cache : <num>,
      bytes read into cache : <num>,
      bytes written from cache : <num>,
      cache overflow cursor application thread wait time (usecs) : <num>,
      cache overflow cursor internal thread wait time (usecs) : <num>,
      cache overflow score : <num>,
      cache overflow table entries : <num>,
      cache overflow table insert calls : <num>,
      cache overflow table max on-disk size : <num>,
      cache overflow table on-disk size : <num>,
      cache overflow table remove calls : <num>,
      checkpoint blocked page eviction : <num>,
      eviction calls to get a page : <num>,
      eviction calls to get a page found queue empty : <num>,
      eviction calls to get a page found queue empty after locking : <num>,
      eviction currently operating in aggressive mode : <num>,
      eviction empty score : <num>,
      eviction passes of a file : <num>,
      eviction server candidate queue empty when topping up : <num>,
      eviction server candidate queue not empty when topping up : <num>,
      eviction server evicting pages : <num>,
      eviction server slept, because we did not make progress with eviction : <num>,
      eviction server unable to reach eviction goal : <num>,
      eviction server waiting for a leaf page : <num>,
      eviction server waiting for an internal page sleep (usec) : <num>,
      eviction server waiting for an internal page yields : <num>,
      eviction state : <num>,
      eviction walk target pages histogram - 0-9 : <num>,
      eviction walk target pages histogram - 10-31 : <num>,
      eviction walk target pages histogram - 128 and higher : <num>,
      eviction walk target pages histogram - 32-63 : <num>,
      eviction walk target pages histogram - 64-128 : <num>,
      eviction walks abandoned : <num>,
      eviction walks gave up because they restarted their walk twice : <num>,
      eviction walks gave up because they saw too many pages and found no candidates : <num>,
      eviction walks gave up because they saw too many pages and found too few candidates : <num>,
      eviction walks reached end of tree : <num>,
      eviction walks started from root of tree : <num>,
      eviction walks started from saved location in tree : <num>,
      eviction worker thread active : <num>,
      eviction worker thread created : <num>,
      eviction worker thread evicting pages : <num>,
      eviction worker thread removed : <num>,
      eviction worker thread stable number : <num>,
      files with active eviction walks : <num>,
      files with new eviction walks started : <num>,
      force re-tuning of eviction workers once in a while : <num>,
      forced eviction - pages evicted that were clean count : <num>,
      forced eviction - pages evicted that were clean time (usecs) : <num>,
      forced eviction - pages evicted that were dirty count : <num>,
      forced eviction - pages evicted that were dirty time (usecs) : <num>,
      forced eviction - pages selected because of too many deleted items count : <num>,
      forced eviction - pages selected count : <num>,
      forced eviction - pages selected unable to be evicted count : <num>,
      forced eviction - pages selected unable to be evicted time : <num>,
      hazard pointer blocked page eviction : <num>,
      hazard pointer check calls : <num>,
      hazard pointer check entries walked : <num>,
      hazard pointer maximum array length : <num>,
      in-memory page passed criteria to be split : <num>,
      in-memory page splits : <num>,
      internal pages evicted : <num>,
      internal pages split during eviction : <num>,
      leaf pages split during eviction : <num>,
      maximum bytes configured : <num>,
      maximum page size at eviction : <num>,
      modified pages evicted : <num>,
      modified pages evicted by application threads : <num>,
      operations timed out waiting for space in cache : <num>,
      overflow pages read into cache : <num>,
      page split during eviction deepened the tree : <num>,
      page written requiring cache overflow records : <num>,
      pages currently held in the cache : <num>,
      pages evicted by application threads : <num>,
      pages queued for eviction : <num>,
      pages queued for eviction post lru sorting : <num>,
      pages queued for urgent eviction : <num>,
      pages queued for urgent eviction during walk : <num>,
      pages read into cache : <num>,
      pages read into cache after truncate : <num>,
      pages read into cache after truncate in prepare state : <num>,
      pages read into cache requiring cache overflow entries : <num>,
      pages read into cache requiring cache overflow for checkpoint : <num>,
      pages read into cache skipping older cache overflow entries : <num>,
      pages read into cache with skipped cache overflow entries needed later : <num>,
      pages read into cache with skipped cache overflow entries needed later by checkpoint : <num>,
      pages requested from the cache : <num>,
      pages seen by eviction walk : <num>,
      pages selected for eviction unable to be evicted : <num>,
      pages walked for eviction : <num>,
      pages written from cache : <num>,
      pages written requiring in-memory restoration : <num>,
      percentage overhead : <num>,
      tracked bytes belonging to internal pages in the cache : <num>,
      tracked bytes belonging to leaf pages in the cache : <num>,
      tracked dirty bytes in the cache : <num>,
      tracked dirty pages in the cache : <num>,
      unmodified pages evicted : <num>
   },
   capacity : {
      background fsync file handles considered : <num>,
      background fsync file handles synced : <num>,
      background fsync time (msecs) : <num>,
      bytes read : <num>,
      bytes written for checkpoint : <num>,
      bytes written for eviction : <num>,
      bytes written for log : <num>,
      bytes written total : <num>,
      threshold to call fsync : <num>,
      time waiting due to total capacity (usecs) : <num>,
      time waiting during checkpoint (usecs) : <num>,
      time waiting during eviction (usecs) : <num>,
      time waiting during logging (usecs) : <num>,
      time waiting during read (usecs) : <num>
   },
   connection : {
      auto adjusting condition resets : <num>,
      auto adjusting condition wait calls : <num>,
      detected system time went backwards : <num>,
      files currently open : <num>,
      memory allocations : <num>,
      memory frees : <num>,
      memory re-allocations : <num>,
      pthread mutex condition wait calls : <num>,
      pthread mutex shared lock read-lock calls : <num>,
      pthread mutex shared lock write-lock calls : <num>,
      total fsync I/Os : <num>,
      total read I/Os : <num>,
      total write I/Os : <num>
   },
   cursor : {
      cached cursor count : <num>,
      cursor bulk loaded cursor insert calls : <num>,
      cursor close calls that result in cache : <num>,
      cursor create calls : <num>,
      cursor insert calls : <num>,
      cursor insert key and value bytes : <num>,
      cursor modify calls : <num>,
      cursor modify key and value bytes affected : <num>,
      cursor modify value bytes modified : <num>,
      cursor next calls : <num>,
      cursor operation restarted : <num>,
      cursor prev calls : <num>,
      cursor remove calls : <num>,
      cursor remove key bytes removed : <num>,
      cursor reserve calls : <num>,
      cursor reset calls : <num>,
      cursor search calls : <num>,
      cursor search near calls : <num>,
      cursor sweep buckets : <num>,
      cursor sweep cursors closed : <num>,
      cursor sweep cursors examined : <num>,
      cursor sweeps : <num>,
      cursor truncate calls : <num>,
      cursor update calls : <num>,
      cursor update key and value bytes : <num>,
      cursor update value size change : <num>,
      cursors reused from cache : <num>,
      open cursor count : <num>
   },
   data-handle : {
      connection data handle size : <num>,
      connection data handles currently active : <num>,
      connection sweep candidate became referenced : <num>,
      connection sweep dhandles closed : <num>,
      connection sweep dhandles removed from hash list : <num>,
      connection sweep time-of-death sets : <num>,
      connection sweeps : <num>,
      session dhandles swept : <num>,
      session sweep attempts : <num>
   },
   lock : {
      checkpoint lock acquisitions : <num>,
      checkpoint lock application thread wait time (usecs) : <num>,
      checkpoint lock internal thread wait time (usecs) : <num>,
      dhandle lock application thread time waiting (usecs) : <num>,
      dhandle lock internal thread time waiting (usecs) : <num>,
      dhandle read lock acquisitions : <num>,
      dhandle write lock acquisitions : <num>,
      durable timestamp queue lock application thread time waiting (usecs) : <num>,
      durable timestamp queue lock internal thread time waiting (usecs) : <num>,
      durable timestamp queue read lock acquisitions : <num>,
      durable timestamp queue write lock acquisitions : <num>,
      metadata lock acquisitions : <num>,
      metadata lock application thread wait time (usecs) : <num>,
      metadata lock internal thread wait time (usecs) : <num>,
      read timestamp queue lock application thread time waiting (usecs) : <num>,
      read timestamp queue lock internal thread time waiting (usecs) : <num>,
      read timestamp queue read lock acquisitions : <num>,
      read timestamp queue write lock acquisitions : <num>,
      schema lock acquisitions : <num>,
      schema lock application thread wait time (usecs) : <num>,
      schema lock internal thread wait time (usecs) : <num>,
      table lock application thread time waiting for the table lock (usecs) : <num>,
      table lock internal thread time waiting for the table lock (usecs) : <num>,
      table read lock acquisitions : <num>,
      table write lock acquisitions : <num>,
      txn global lock application thread time waiting (usecs) : <num>,
      txn global lock internal thread time waiting (usecs) : <num>,
      txn global read lock acquisitions : <num>,
      txn global write lock acquisitions : <num>
   },
   log : {
      busy returns attempting to switch slots : <num>,
      force archive time sleeping (usecs) : <num>,
      log bytes of payload data : <num>,
      log bytes written : <num>,
      log files manually zero-filled : <num>,
      log flush operations : <num>,
      log force write operations : <num>,
      log force write operations skipped : <num>,
      log records compressed : <num>,
      log records not compressed : <num>,
      log records too small to compress : <num>,
      log release advances write LSN : <num>,
      log scan operations : <num>,
      log scan records requiring two reads : <num>,
      log server thread advances write LSN : <num>,
      log server thread write LSN walk skipped : <num>,
      log sync operations : <num>,
      log sync time duration (usecs) : <num>,
      log sync_dir operations : <num>,
      log sync_dir time duration (usecs) : <num>,
      log write operations : <num>,
      logging bytes consolidated : <num>,
      maximum log file size : <num>,
      number of pre-allocated log files to create : <num>,
      pre-allocated log files not ready and missed : <num>,
      pre-allocated log files prepared : <num>,
      pre-allocated log files used : <num>,
      records processed by log scan : <num>,
      slot close lost race : <num>,
      slot close unbuffered waits : <num>,
      slot closures : <num>,
      slot join atomic update races : <num>,
      slot join calls atomic updates raced : <num>,
      slot join calls did not yield : <num>,
      slot join calls found active slot closed : <num>,
      slot join calls slept : <num>,
      slot join calls yielded : <num>,
      slot join found active slot closed : <num>,
      slot joins yield time (usecs) : <num>,
      slot transitions unable to find free slot : <num>,
      slot unbuffered writes : <num>,
      total in-memory size of compressed records : <num>,
      total log buffer size : <num>,
      total size of compressed records : <num>,
      written slots coalesced : <num>,
      yields waiting for previous log file close : <num>
   },
   perf : {
      file system read latency histogram (bucket 1) - 10-49ms : <num>,
      file system read latency histogram (bucket 2) - 50-99ms : <num>,
      file system read latency histogram (bucket 3) - 100-249ms : <num>,
      file system read latency histogram (bucket 4) - 250-499ms : <num>,
      file system read latency histogram (bucket 5) - 500-999ms : <num>,
      file system read latency histogram (bucket 6) - 1000ms+ : <num>,
      file system write latency histogram (bucket 1) - 10-49ms : <num>,
      file system write latency histogram (bucket 2) - 50-99ms : <num>,
      file system write latency histogram (bucket 3) - 100-249ms : <num>,
      file system write latency histogram (bucket 4) - 250-499ms : <num>,
      file system write latency histogram (bucket 5) - 500-999ms : <num>,
      file system write latency histogram (bucket 6) - 1000ms+ : <num>,
      operation read latency histogram (bucket 1) - 100-249us : <num>,
      operation read latency histogram (bucket 2) - 250-499us : <num>,
      operation read latency histogram (bucket 3) - 500-999us : <num>,
      operation read latency histogram (bucket 4) - 1000-9999us : <num>,
      operation read latency histogram (bucket 5) - 10000us+ : <num>,
      operation write latency histogram (bucket 1) - 100-249us : <num>,
      operation write latency histogram (bucket 2) - 250-499us : <num>,
      operation write latency histogram (bucket 3) - 500-999us : <num>,
      operation write latency histogram (bucket 4) - 1000-9999us : <num>,
      operation write latency histogram (bucket 5) - 10000us+ : <num>
   },
   reconciliation : {
      fast-path pages deleted : <num>,
      page reconciliation calls : <num>,
      page reconciliation calls for eviction : <num>,
      pages deleted : <num>,
      split bytes currently awaiting free : <num>,
      split objects currently awaiting free : <num>
   },
   session : {
      open session count : <num>,
      session query timestamp calls : <num>,
      table alter failed calls : <num>,
      table alter successful calls : <num>,
      table alter unchanged and skipped : <num>,
      table compact failed calls : <num>,
      table compact successful calls : <num>,
      table create failed calls : <num>,
      table create successful calls : <num>,
      table drop failed calls : <num>,
      table drop successful calls : <num>,
      table import failed calls : <num>,
      table import successful calls : <num>,
      table rebalance failed calls : <num>,
      table rebalance successful calls : <num>,
      table rename failed calls : <num>,
      table rename successful calls : <num>,
      table salvage failed calls : <num>,
      table salvage successful calls : <num>,
      table truncate failed calls : <num>,
      table truncate successful calls : <num>,
      table verify failed calls : <num>,
      table verify successful calls : <num>
   },
   thread-state : {
      active filesystem fsync calls : <num>,
      active filesystem read calls : <num>,
      active filesystem write calls : <num>
   },
   thread-yield : {
      application thread time evicting (usecs) : <num>,
      application thread time waiting for cache (usecs) : <num>,
      connection close blocked waiting for transaction state stabilization : <num>,
      connection close yielded for lsm manager shutdown : <num>,
      data handle lock yielded : <num>,
      get reference for page index and slot time sleeping (usecs) : <num>,
      log server sync yielded for log write : <num>,
      page access yielded due to prepare state change : <num>,
      page acquire busy blocked : <num>,
      page acquire eviction blocked : <num>,
      page acquire locked blocked : <num>,
      page acquire read blocked : <num>,
      page acquire time sleeping (usecs) : <num>,
      page delete rollback time sleeping for state change (usecs) : <num>,
      page reconciliation yielded due to child modification : <num>
   },
   transaction : {
      Number of prepared updates : <num>,
      Number of prepared updates added to cache overflow : <num>,
      Number of prepared updates resolved : <num>,
      durable timestamp queue entries walked : <num>,
      durable timestamp queue insert to empty : <num>,
      durable timestamp queue inserts to head : <num>,
      durable timestamp queue inserts total : <num>,
      durable timestamp queue length : <num>,
      number of named snapshots created : <num>,
      number of named snapshots dropped : <num>,
      prepared transactions : <num>,
      prepared transactions committed : <num>,
      prepared transactions currently active : <num>,
      prepared transactions rolled back : <num>,
      query timestamp calls : <num>,
      read timestamp queue entries walked : <num>,
      read timestamp queue insert to empty : <num>,
      read timestamp queue inserts to head : <num>,
      read timestamp queue inserts total : <num>,
      read timestamp queue length : <num>,
      rollback to stable calls : <num>,
      rollback to stable updates aborted : <num>,
      rollback to stable updates removed from cache overflow : <num>,
      set timestamp calls : <num>,
      set timestamp durable calls : <num>,
      set timestamp durable updates : <num>,
      set timestamp oldest calls : <num>,
      set timestamp oldest updates : <num>,
      set timestamp stable calls : <num>,
      set timestamp stable updates : <num>,
      transaction begins : <num>,
      transaction checkpoint currently running : <num>,
      transaction checkpoint generation : <num>,
      transaction checkpoint max time (msecs) : <num>,
      transaction checkpoint min time (msecs) : <num>,
      transaction checkpoint most recent time (msecs) : <num>,
      transaction checkpoint scrub dirty target : <num>,
      transaction checkpoint scrub time (msecs) : <num>,
      transaction checkpoint total time (msecs) : <num>,
      transaction checkpoints : <num>,
      transaction checkpoints skipped because database was clean : <num>,
      transaction failures due to cache overflow : <num>,
      transaction fsync calls for checkpoint after allocating the transaction ID : <num>,
      transaction fsync duration for checkpoint after allocating the transaction ID (usecs) : <num>,
      transaction range of IDs currently pinned : <num>,
      transaction range of IDs currently pinned by a checkpoint : <num>,
      transaction range of IDs currently pinned by named snapshots : <num>,
      transaction range of timestamps currently pinned : <num>,
      transaction range of timestamps pinned by a checkpoint : <num>,
      transaction range of timestamps pinned by the oldest active read timestamp : <num>,
      transaction range of timestamps pinned by the oldest timestamp : <num>,
      transaction read timestamp of the oldest active reader : <num>,
      transaction sync calls : <num>,
      transactions committed : <num>,
      transactions rolled back : <num>,
      update conflicts : <num>
   },
   concurrentTransactions : {
      write : {
         out : <num>,
         available : <num>,
         totalTickets : <num>
      },
      read : {
         out : <num>,
         available : <num>,
         totalTickets : <num>
      },
      monitor : { 
         timesDecreased: <num>, 
         timesIncreased: <num>, 
         totalAmountDecreased: <num>, 
         totalAmountIncreased: <num>
      }
   },
   snapshot-window-settings : {
      total number of SnapshotTooOld errors : <num>,
      max target available snapshots window size in seconds : <num>,
      target available snapshots window size in seconds : <num>,
      current available snapshots window size in seconds : <num>,
      latest majority snapshot timestamp available : <string>,
      oldest majority snapshot timestamp available : <string>
   }
}
```

**Note:**

The following is not an exhaustive list.

**`wiredTiger.uri`**

A string. For internal use by MongoDB.

**`wiredTiger.async`**

A document that returns statistics related to the asynchronous
operations API. This is unused by MongoDB.

**`wiredTiger.block-manager`**

A document that returns statistics on the block manager operations.

**`wiredTiger.cache`**

A document that returns statistics on the cache and page evictions
from the cache.

The following describes some of the key
`wiredTiger.cache` statistics:

**`wiredTiger.cache.maximum bytes configured`**

Maximum cache size.

**`wiredTiger.cache.bytes currently in the cache`**

Size in bytes of the data currently in cache. This value should
not be greater than the `maximum bytes configured` value.

**`wiredTiger.cache.unmodified pages evicted`**

Main statistics for page eviction.

**`wiredTiger.cache.tracked dirty bytes in the cache`**

Size in bytes of the dirty data in the cache. This value should
be less than the `bytes currently in the cache` value.

**`wiredTiger.cache.pages read into cache`**

Number of pages read into the cache.
`wiredTiger.cache.pages read into cache` with
the `wiredTiger.cache.pages written from
cache` can provide an overview of the I/O activity.

**`wiredTiger.cache.pages written from cache`**

Number of pages written from the cache.
`wiredTiger.cache.pages written from cache`
with the `wiredTiger.cache.pages read into
cache` can provide an overview of the I/O activity.

To adjust the size of the WiredTiger internal cache, see
`storage.wiredTiger.engineConfig.cacheSizeGB` and
`--wiredTigerCacheSizeGB`. Avoid increasing the WiredTiger
internal cache size above its default value.

**`wiredTiger.connection`**

A document that returns statistics related to WiredTiger connections.

**`wiredTiger.cursor`**

A document that returns statistics on WiredTiger cursor.

**`wiredTiger.data-handle`**

A document that returns statistics on the data handles and sweeps.

**`wiredTiger.log`**

A document that returns statistics on WiredTiger's write ahead log
(that is, the journal).

**See also:**

journaling-wiredTiger

**`wiredTiger.reconciliation`**

A document that returns statistics on the reconciliation process.

**`wiredTiger.session`**

A document that returns the open cursor count and open session count
for the session.

**`wiredTiger.thread-yield`**

A document that returns statistics on yields during page
acquisitions.

**`wiredTiger.transaction`**

A document that returns statistics on transaction checkpoints and
operations.

**`wiredTiger.transaction.transaction checkpoint most recent time (msecs)`**

Amount of time, in milliseconds, to create the most recent
checkpoint. An increase in this value under stead write load may
indicate saturation on the I/O subsystem.

**`wiredTiger.concurrentTransactions`**

**Changed in version:** 7.0

A document that returns information about: 

- The number of concurrent read transactions (read tickets) allowed 
  into the WiredTiger storage engine.
- The number of concurrent write transactions (write tickets) allowed 
  into the WiredTiger storage engine. 
- Any adjustments that the system has made to the number
  of allowed concurrent transactions (tickets).

These settings are MongoDB-specific. To change the settings for 
concurrent reads and write transactions (read and write tickets), see
`storageEngineConcurrentReadTransactions` and
`storageEngineConcurrentWriteTransactions`.

**Important:**

Starting in version 7.0, MongoDB uses a default algorithm to dynamically
adjust the maximum number of concurrent storage engine transactions
(including both read and write tickets) to optimize database throughput
during overload.

The following table summarizes how to identify overload scenarios for MongoDB 
7.0 and prior releases:

| Version | Diagnosing Overload Scenarios |
|---|---|
| 7.0 | A large number of queued operations that persists for a prolonged period of time likely indicates an overload. A concurrent storage engine transaction (ticket) availability of 0 for a prolonged period of time **does not** indicate an overload. |
| 6.0 and prior | A large number of queued operations that persists for a prolonged period of time likely indicates an overload. A concurrent storage engine transaction (ticket) availibility of 0 for a prolonged period of time likely indicates an overload. |
