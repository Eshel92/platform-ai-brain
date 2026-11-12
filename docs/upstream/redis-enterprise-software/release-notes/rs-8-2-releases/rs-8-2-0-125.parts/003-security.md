<!-- Part 3 of 3 of release-notes/rs-8-2-releases/rs-8-2-0-125.md (split because the page is big). -->

## Security

#### Redis Open Source security fixes compatibility

As part of Redis's commitment to security, Redis Software implements the latest [security fixes](https://github.com/redis/redis/releases) available with [Redis Open Source](https://github.com/redis/redis). Redis Software has already included the fixes for the relevant CVEs.

Some CVEs announced for Redis Open Source do not affect Redis Software due to different or additional functionality available in Redis Software that is not available in Redis Open Source.

Redis Software 8.2.0-125 supports Redis Open Source 8.6, 8.4, 8.2, 8.0, 7.4, 7.2, and 6.2. Below is the list of Redis Open Source CVEs and other security vulnerabilities fixed by version.

{{< collapsible "Redis 8.6.x" >}}

- Memory corruption in `SLOT_INFO` handling may allow an unauthenticated user to potentially run their own code.

- A use-after-free in TLS pending-data processing may allow an authenticated user to cause a denial-of-service.

- A vulnerability in the `RESTORE` command and in RDB loading allows an authenticated user to trigger a use-after-free in stream consumer groups via a specially crafted serialized payload, potentially resulting in remote code execution.

- An ACL key-pattern bypass in `GEORADIUS` and `GEORADIUSBYMEMBER` may allow an authenticated user to write to keys outside their permitted key patterns.

- An out-of-bounds read during command key extraction may cause the server to crash.

- VSET: Missing `level` cap when loading a serialized HNSW graph may lead to resource exhaustion.

- VSET: Missing validation of the parameter count when loading a serialized vector set may lead to oversized allocation and resource exhaustion.

- Certificate common-name handling can allow an authentication bypass when `tls-auth-clients-user` is set to `CN`.

- (CVE-2026-62356) An authenticated user may trigger a heap out-of-bounds write in RedisBloom by loading a specially crafted Count-Min Sketch (`CMSketch`) object, for example via the `RESTORE` command or a crafted RDB file.

- RedisBloom: Out-of-bounds access in the `TopK` heap cleanup path.

- VSET: Large `VADD REDUCE` values can lead to out-of-memory crashes or buffer overflow.

- (CVE-2026-23479) When a blocked client is evicted while re-executing a blocked command, an authenticated user may trigger a use-after-free and potentially lead to remote code execution.

- (CVE‑2026‑25243) A vulnerability in the Redis `RESTORE` command allows an authenticated user to trigger an invalid memory access via a specially crafted serialized payload, potentially resulting in remote code execution.

- (CVE-2026-25588) A vulnerability in the `RESTORE` command, when used with the RedisTimeSeries module, allows an authenticated attacker to trigger invalid memory access via a specially crafted serialized payload, potentially resulting in remote code execution.

- (CVE‑2026‑25589) A vulnerability in the `RESTORE` command, when used with the RedisBloom module, allows an authenticated attacker to trigger invalid memory access via a specially crafted serialized payload, potentially resulting in remote code execution.

- (CVE-2026-23631) An authenticated user may exploit the synchronization mechanism of the master-replica and trigger a use-after-free vulnerability, potentially leading to remote code execution. The bug affects only replicas that are configured, or may be configured with `replica-read-only` disabled, and exists in all versions of Redis with Lua scripting.

- Insufficient sanitization of Lua script error messages can allow an authenticated user with `EVAL` permission to inject arbitrary RESP protocol responses, leading to denial of service, data manipulation, and connection pool poisoning.

- RedisBloom: Integer overflow in `TopK` RDB loading may lead to heap out-of-bounds access.

- RedisBloom: Missing validation in `td_histogram_t` RDB loading may lead to heap buffer overflow.

- RedisBloom: Missing validation in `CuckooFilter` RDB loading may lead to heap out-of-bounds access.

- RedisBloom: Missing validation in `SBChain` and `CMSketch` RDB loading may lead to heap out-of-bounds write.

- Added validation of limits during RDB load and data creation to avoid resource exhaustion and Denial-of-Service (DoS) vulnerabilities.

{{< /collapsible >}}

{{< collapsible "Redis 8.4.x" >}}

- Memory corruption in `SLOT_INFO` handling may allow an unauthenticated user to potentially run their own code.

- A use-after-free in TLS pending-data processing may allow an authenticated user to cause a denial-of-service.

- A vulnerability in the `RESTORE` command and in RDB loading allows an authenticated user to trigger a use-after-free in stream consumer groups via a specially crafted serialized payload, potentially resulting in remote code execution.

- An ACL key-pattern bypass in `GEORADIUS` and `GEORADIUSBYMEMBER` may allow an authenticated user to write to keys outside their permitted key patterns.

- An out-of-bounds read during command key extraction may cause the server to crash.

- VSET: Missing `level` cap when loading a serialized HNSW graph may lead to resource exhaustion.

- VSET: Missing validation of the parameter count when loading a serialized vector set may lead to oversized allocation and resource exhaustion.

- (CVE-2026-62356) An authenticated user may trigger a heap out-of-bounds write in RedisBloom by loading a specially crafted Count-Min Sketch (`CMSketch`) object, for example via the `RESTORE` command or a crafted RDB file.

- RedisBloom: Out-of-bounds access in the `TopK` heap cleanup path.

- VSET: Large `VADD REDUCE` values can lead to out-of-memory crashes or buffer overflow.

- (CVE-2026-23479) When a blocked client is evicted while re-executing a blocked command, an authenticated user may trigger a use-after-free and potentially lead to remote code execution.

- (CVE‑2026‑25243) A vulnerability in the Redis `RESTORE` command allows an authenticated user to trigger an invalid memory access via a specially crafted serialized payload, potentially resulting in remote code execution.

- (CVE-2026-25588) A vulnerability in the `RESTORE` command, when used with the RedisTimeSeries module, allows an authenticated attacker to trigger invalid memory access via a specially crafted serialized payload, potentially resulting in remote code execution.

- (CVE‑2026‑25589) A vulnerability in the `RESTORE` command, when used with the RedisBloom module, allows an authenticated attacker to trigger invalid memory access via a specially crafted serialized payload, potentially resulting in remote code execution.

- (CVE-2026-23631) An authenticated user may exploit the synchronization mechanism of the master-replica and trigger a use-after-free vulnerability, potentially leading to remote code execution. The bug affects only replicas that are configured, or may be configured with `replica-read-only` disabled, and exists in all versions of Redis with Lua scripting.

- Insufficient sanitization of Lua script error messages can allow an authenticated user with `EVAL` permission to inject arbitrary RESP protocol responses, leading to denial of service, data manipulation, and connection pool poisoning.

- RedisBloom: Integer overflow in `TopK` RDB loading may lead to heap out-of-bounds access.

- RedisBloom: Missing validation in `td_histogram_t` RDB loading may lead to heap buffer overflow.

- RedisBloom: Missing validation in `CuckooFilter` RDB loading may lead to heap out-of-bounds access.

- RedisBloom: Missing validation in `SBChain` and `CMSketch` RDB loading may lead to heap out-of-bounds write.

- Added validation of limits during RDB load and data creation to avoid resource exhaustion and Denial-of-Service (DoS) vulnerabilities.

{{< /collapsible >}}

{{< collapsible "Redis 8.2.x" >}}

- Memory corruption in `SLOT_INFO` handling may allow an unauthenticated user to potentially run their own code.

- A use-after-free in TLS pending-data processing may allow an authenticated user to cause a denial-of-service.

- A vulnerability in the `RESTORE` command and in RDB loading allows an authenticated user to trigger a use-after-free in stream consumer groups via a specially crafted serialized payload, potentially resulting in remote code execution.

- An ACL key-pattern bypass in `GEORADIUS` and `GEORADIUSBYMEMBER` may allow an authenticated user to write to keys outside their permitted key patterns.

- An out-of-bounds read during command key extraction may cause the server to crash.

- VSET: Missing `level` cap when loading a serialized HNSW graph may lead to resource exhaustion.

- VSET: Missing validation of the parameter count when loading a serialized vector set may lead to oversized allocation and resource exhaustion.

- (CVE-2026-62356) An authenticated user may trigger a heap out-of-bounds write in RedisBloom by loading a specially crafted Count-Min Sketch (`CMSketch`) object, for example via the `RESTORE` command or a crafted RDB file.

- RedisBloom: Out-of-bounds access in the `TopK` heap cleanup path.

- VSET: Large `VADD REDUCE` values can lead to out-of-memory crashes or buffer overflow.

- (CVE-2026-23479) When a blocked client is evicted while re-executing a blocked command, an authenticated user may trigger a use-after-free and potentially lead to remote code execution.

- (CVE‑2026‑25243) A vulnerability in the Redis `RESTORE` command allows an authenticated user to trigger an invalid memory access via a specially crafted serialized payload, potentially resulting in remote code execution.

- (CVE-2026-25588) A vulnerability in the `RESTORE` command, when used with the RedisTimeSeries module, allows an authenticated attacker to trigger invalid memory access via a specially crafted serialized payload, potentially resulting in remote code execution.

- (CVE‑2026‑25589) A vulnerability in the `RESTORE` command, when used with the RedisBloom module, allows an authenticated attacker to trigger invalid memory access via a specially crafted serialized payload, potentially resulting in remote code execution.

- (CVE-2026-23631) An authenticated user may exploit the synchronization mechanism of the master-replica and trigger a use-after-free vulnerability, potentially leading to remote code execution. The bug affects only replicas that are configured, or may be configured with `replica-read-only` disabled, and exists in all versions of Redis with Lua scripting.

- Insufficient sanitization of Lua script error messages can allow an authenticated user with `EVAL` permission to inject arbitrary RESP protocol responses, leading to denial of service, data manipulation, and connection pool poisoning.

- RedisBloom: Integer overflow in `TopK` RDB loading may lead to heap out-of-bounds access.

- RedisBloom: Missing validation in `td_histogram_t` RDB loading may lead to heap buffer overflow.

- RedisBloom: Missing validation in `CuckooFilter` RDB loading may lead to heap out-of-bounds access.

- RedisBloom: Missing validation in `SBChain` and `CMSketch` RDB loading may lead to heap out-of-bounds write.

- Added validation of limits during RDB load and data creation to avoid resource exhaustion and Denial-of-Service (DoS) vulnerabilities.

- RedisBloom: Restore invalid filter.

- (CVE-2025-62507) A user can run the `XACKDEL` command with multiple IDs and trigger a stack buffer overflow, which can potentially lead to remote code execution.

- The `HGETEX` command can lead to a buffer overflow.

- Integer overflow in `hllPatLen`.

- RedisBloom: Cuckoo filter counter overflow.

- RedisBloom: Invalid Bloom filters can cause arbitrary memory reads and writes.

- RedisBloom: Reachable assert in `TopK_Create`

- RedisBloom: Out-of-bounds access with empty Bloom chains.

- RedisBloom: Division by zero in Cuckoo filter insertion.

- (CVE-2025-46818) An authenticated user may use a specially crafted Lua script to manipulate different LUA objects and potentially run their own code in the context of another user.

- (CVE-2025-46819) An authenticated user may use a specially crafted LUA script to read out-of-bound data or crash the server and lead to subsequent denial of service.

- (CVE-2025-46817) An authenticated user may use a specially crafted Lua script to cause an integer overflow and potentially lead to remote code execution.

- (CVE-2025-49844) An authenticated user may use a specially crafted Lua script to manipulate the garbage collector, trigger a use-after-free, and potentially lead to remote code execution.

{{< /collapsible >}}

{{< collapsible "Redis 8.0.x" >}}

- Memory corruption in `SLOT_INFO` handling may allow an unauthenticated user to potentially run their own code.

- A use-after-free in TLS pending-data processing may allow an authenticated user to cause a denial-of-service.

- A vulnerability in the `RESTORE` command and in RDB loading allows an authenticated user to trigger a use-after-free in stream consumer groups via a specially crafted serialized payload, potentially resulting in remote code execution.

- An ACL key-pattern bypass in `GEORADIUS` and `GEORADIUSBYMEMBER` may allow an authenticated user to write to keys outside their permitted key patterns.

- An out-of-bounds read during command key extraction may cause the server to crash.

- (CVE-2026-62356) An authenticated user may trigger a heap out-of-bounds write in RedisBloom by loading a specially crafted Count-Min Sketch (`CMSketch`) object, for example via the `RESTORE` command or a crafted RDB file.

- RedisBloom: Out-of-bounds access in the `TopK` heap cleanup path.

- VSET: Large `VADD REDUCE` values can lead to out-of-memory crashes or buffer overflow.

- (CVE-2026-23479) When a blocked client is evicted while re-executing a blocked command, an authenticated user may trigger a use-after-free and potentially lead to remote code execution.

- (CVE‑2026‑25243) A vulnerability in the Redis `RESTORE` command allows an authenticated user to trigger an invalid memory access via a specially crafted serialized payload, potentially resulting in remote code execution.

- (CVE-2026-25588) A vulnerability in the `RESTORE` command, when used with the RedisTimeSeries module, allows an authenticated attacker to trigger invalid memory access via a specially crafted serialized payload, potentially resulting in remote code execution.

- (CVE‑2026‑25589) A vulnerability in the `RESTORE` command, when used with the RedisBloom module, allows an authenticated attacker to trigger invalid memory access via a specially crafted serialized payload, potentially resulting in remote code execution.

- (CVE-2026-23631) An authenticated user may exploit the synchronization mechanism of the master-replica and trigger a use-after-free vulnerability, potentially leading to remote code execution. The bug affects only replicas that are configured, or may be configured with `replica-read-only` disabled, and exists in all versions of Redis with Lua scripting.

- Insufficient sanitization of Lua script error messages can allow an authenticated user with `EVAL` permission to inject arbitrary RESP protocol responses, leading to denial of service, data manipulation, and connection pool poisoning.

- RedisBloom: Integer overflow in `TopK` RDB loading may lead to heap out-of-bounds access.

- RedisBloom: Missing validation in `td_histogram_t` RDB loading may lead to heap buffer overflow.

- RedisBloom: Missing validation in `CuckooFilter` RDB loading may lead to heap out-of-bounds access.

- RedisBloom: Missing validation in `SBChain` and `CMSketch` RDB loading may lead to heap out-of-bounds write.

- Added validation of limits during RDB load and data creation to avoid resource exhaustion and Denial-of-Service (DoS) vulnerabilities.

- RedisBloom: Restore invalid filter.

- The `HGETEX` command can lead to a buffer overflow.

- Integer overflow in `hllPatLen`.

- RedisBloom: Cuckoo filter counter overflow.

- RedisBloom: Invalid Bloom filters can cause arbitrary memory reads and writes.

- RedisBloom: Reachable assert in `TopK_Create`

- RedisBloom: Out-of-bounds access with empty Bloom chains.

- RedisBloom: Division by zero in Cuckoo filter insertion.

- (CVE-2025-46818) An authenticated user may use a specially crafted Lua script to manipulate different LUA objects and potentially run their own code in the context of another user.

- (CVE-2025-46819) An authenticated user may use a specially crafted LUA script to read out-of-bound data or crash the server and lead to subsequent denial of service.

- (CVE-2025-46817) An authenticated user may use a specially crafted Lua script to cause an integer overflow and potentially lead to remote code execution.

- (CVE-2025-49844) An authenticated user may use a specially crafted Lua script to manipulate the garbage collector, trigger a use-after-free, and potentially lead to remote code execution.

{{< /collapsible >}}

{{< collapsible "Redis 7.4.x" >}}

- Memory corruption in `SLOT_INFO` handling may allow an unauthenticated user to potentially run their own code.

- A use-after-free in TLS pending-data processing may allow an authenticated user to cause a denial-of-service.

- A vulnerability in the `RESTORE` command and in RDB loading allows an authenticated user to trigger a use-after-free in stream consumer groups via a specially crafted serialized payload, potentially resulting in remote code execution.

- An ACL key-pattern bypass in `GEORADIUS` and `GEORADIUSBYMEMBER` may allow an authenticated user to write to keys outside their permitted key patterns.

- An out-of-bounds read during command key extraction may cause the server to crash.

- (CVE-2026-62356) An authenticated user may trigger a heap out-of-bounds write in RedisBloom by loading a specially crafted Count-Min Sketch (`CMSketch`) object, for example via the `RESTORE` command or a crafted RDB file.

- RedisBloom: Out-of-bounds access in the `TopK` heap cleanup path.

- (CVE-2026-23479) When a blocked client is evicted while re-executing a blocked command, an authenticated user may trigger a use-after-free and potentially lead to remote code execution.

- (CVE‑2026‑25243) A vulnerability in the Redis `RESTORE` command allows an authenticated user to trigger an invalid memory access via a specially crafted serialized payload, potentially resulting in remote code execution.

- (CVE-2026-25588) A vulnerability in the `RESTORE` command, when used with the RedisTimeSeries module, allows an authenticated attacker to trigger invalid memory access via a specially crafted serialized payload, potentially resulting in remote code execution.

- (CVE‑2026‑25589) A vulnerability in the `RESTORE` command, when used with the RedisBloom module, allows an authenticated attacker to trigger invalid memory access via a specially crafted serialized payload, potentially resulting in remote code execution.

- (CVE-2026-23631) An authenticated user may exploit the synchronization mechanism of the master-replica and trigger a use-after-free vulnerability, potentially leading to remote code execution. The bug affects only replicas that are configured, or may be configured with `replica-read-only` disabled, and exists in all versions of Redis with Lua scripting.

- Insufficient sanitization of Lua script error messages can allow an authenticated user with `EVAL` permission to inject arbitrary RESP protocol responses, leading to denial of service, data manipulation, and connection pool poisoning.

- RedisBloom: Integer overflow in `TopK` RDB loading may lead to heap out-of-bounds access.

- RedisBloom: Missing validation in `td_histogram_t` RDB loading may lead to heap buffer overflow.

- RedisBloom: Missing validation in `CuckooFilter` RDB loading may lead to heap out-of-bounds access.

- RedisBloom: Missing validation in `SBChain` and `CMSketch` RDB loading may lead to heap out-of-bounds write.

- Added validation of limits during RDB load and data creation to avoid resource exhaustion and Denial-of-Service (DoS) vulnerabilities.

- RedisBloom: Restore invalid filter.

- Integer overflow in `hllPatLen`.

- RedisBloom: Cuckoo filter counter overflow.

- RedisBloom: Invalid Bloom filters can cause arbitrary memory reads and writes.

- RedisBloom: Reachable assert in `TopK_Create`

- RedisBloom: Out-of-bounds access with empty Bloom chains.

- RedisBloom: Division by zero in Cuckoo filter insertion.

- (CVE-2025-46818) An authenticated user may use a specially crafted Lua script to manipulate different LUA objects and potentially run their own code in the context of another user.

- (CVE-2025-46819) An authenticated user may use a specially crafted LUA script to read out-of-bound data or crash the server and lead to subsequent denial of service.

- (CVE-2025-46817) An authenticated user may use a specially crafted Lua script to cause an integer overflow and potentially lead to remote code execution.

- (CVE-2025-49844) An authenticated user may use a specially crafted Lua script to manipulate the garbage collector, trigger a use-after-free, and potentially lead to remote code execution.

- (CVE-2025-32023) An authenticated user can use a specially crafted string to trigger a stack/heap out-of-bounds write on HyperLogLog operations, which can lead to remote code execution.

- (CVE-2025-21605) An unauthenticated client can cause unlimited growth of output buffers until the server runs out of memory or is terminated, which can lead to denial-of-service.

{{< /collapsible >}}

{{< collapsible "Redis 7.2.x" >}}

- Memory corruption in `SLOT_INFO` handling may allow an unauthenticated user to potentially run their own code.

- A use-after-free in TLS pending-data processing may allow an authenticated user to cause a denial-of-service.

- A vulnerability in the `RESTORE` command and in RDB loading allows an authenticated user to trigger a use-after-free in stream consumer groups via a specially crafted serialized payload, potentially resulting in remote code execution.

- An ACL key-pattern bypass in `GEORADIUS` and `GEORADIUSBYMEMBER` may allow an authenticated user to write to keys outside their permitted key patterns.

- An out-of-bounds read during command key extraction may cause the server to crash.

- (CVE-2026-62356) An authenticated user may trigger a heap out-of-bounds write in RedisBloom by loading a specially crafted Count-Min Sketch (`CMSketch`) object, for example via the `RESTORE` command or a crafted RDB file.

- RedisBloom: Out-of-bounds access in the `TopK` heap cleanup path.

- (CVE-2026-23479) When a blocked client is evicted while re-executing a blocked command, an authenticated user may trigger a use-after-free and potentially lead to remote code execution.

- (CVE‑2026‑25243) A vulnerability in the Redis `RESTORE` command allows an authenticated user to trigger an invalid memory access via a specially crafted serialized payload, potentially resulting in remote code execution.

- (CVE-2026-25588) A vulnerability in the `RESTORE` command, when used with the RedisTimeSeries module, allows an authenticated attacker to trigger invalid memory access via a specially crafted serialized payload, potentially resulting in remote code execution.

- (CVE‑2026‑25589) A vulnerability in the `RESTORE` command, when used with the RedisBloom module, allows an authenticated attacker to trigger invalid memory access via a specially crafted serialized payload, potentially resulting in remote code execution.

- (CVE-2026-23631) An authenticated user may exploit the synchronization mechanism of the master-replica and trigger a use-after-free vulnerability, potentially leading to remote code execution. The bug affects only replicas that are configured, or may be configured with `replica-read-only` disabled, and exists in all versions of Redis with Lua scripting.

- Insufficient sanitization of Lua script error messages can allow an authenticated user with `EVAL` permission to inject arbitrary RESP protocol responses, leading to denial of service, data manipulation, and connection pool poisoning.

- RedisBloom: Integer overflow in `TopK` RDB loading may lead to heap out-of-bounds access.

- RedisBloom: Missing validation in `td_histogram_t` RDB loading may lead to heap buffer overflow.

- RedisBloom: Missing validation in `CuckooFilter` RDB loading may lead to heap out-of-bounds access.

- RedisBloom: Missing validation in `SBChain` and `CMSketch` RDB loading may lead to heap out-of-bounds write.

- Added validation of limits during RDB load and data creation to avoid resource exhaustion and Denial-of-Service (DoS) vulnerabilities.

- RedisBloom: Restore invalid filter.

- Integer overflow in `hllPatLen`.

- RedisBloom: Cuckoo filter counter overflow.

- RedisBloom: Invalid Bloom filters can cause arbitrary memory reads and writes.

- RedisBloom: Reachable assert in `TopK_Create`

- RedisBloom: Out-of-bounds access with empty Bloom chains.

- RedisBloom: Division by zero in Cuckoo filter insertion.

- (CVE-2025-46818) An authenticated user may use a specially crafted Lua script to manipulate different LUA objects and potentially run their own code in the context of another user.

- (CVE-2025-46819) An authenticated user may use a specially crafted LUA script to read out-of-bound data or crash the server and lead to subsequent denial of service.

- (CVE-2025-46817) An authenticated user may use a specially crafted Lua script to cause an integer overflow and potentially lead to remote code execution.

- (CVE-2025-49844) An authenticated user may use a specially crafted Lua script to manipulate the garbage collector, trigger a use-after-free, and potentially lead to remote code execution.

- (CVE-2025-32023) An authenticated user can use a specially crafted string to trigger a stack/heap out-of-bounds write on HyperLogLog operations, which can lead to remote code execution.

- (CVE-2025-21605) An unauthenticated client can cause unlimited growth of output buffers until the server runs out of memory or is terminated, which can lead to denial-of-service.

- (CVE-2024-31449) An authenticated user may use a specially crafted Lua script to trigger a stack buffer overflow in the bit library, which may potentially lead to remote code execution.

- (CVE-2024-31228) An authenticated user can trigger a denial-of-service by using specially crafted, long string match patterns on supported commands such as `KEYS`, `SCAN`, `PSUBSCRIBE`, `FUNCTION LIST`, `COMMAND LIST`, and ACL definitions. Matching of extremely long patterns may result in unbounded recursion, leading to stack overflow and process crashes.

- (CVE-2023-41056) In some cases, Redis may incorrectly handle resizing of memory buffers, which can result in incorrect accounting of buffer sizes and lead to heap overflow and potential remote code execution.

- (CVE-2023-41053) Redis does not correctly identify keys accessed by `SORT_RO` and, as a result, may grant users executing this command access to keys that are not explicitly authorized by the ACL configuration. (Redis 7.2.1)

{{< /collapsible >}}

{{< collapsible "Redis 7.0.x" >}}

- (CVE-2024-31449) An authenticated user may use a specially crafted Lua script to trigger a stack buffer overflow in the bit library, which may potentially lead to remote code execution.

- (CVE-2024-31228) An authenticated user can trigger a denial-of-service by using specially crafted, long string match patterns on supported commands such as `KEYS`, `SCAN`, `PSUBSCRIBE`, `FUNCTION LIST`, `COMMAND LIST`, and ACL definitions. Matching of extremely long patterns may result in unbounded recursion, leading to stack overflow and process crashes.

- (CVE-2023-41056) In some cases, Redis may incorrectly handle resizing of memory buffers, which can result in incorrect accounting of buffer sizes and lead to heap overflow and potential remote code execution.

- (CVE-2023-41053) Redis does not correctly identify keys accessed by `SORT_RO` and, as a result, may grant users executing this command access to keys that are not explicitly authorized by the ACL configuration. (Redis 7.0.13)

- (CVE-2023-36824) Extracting key names from a command and a list of arguments may, in some cases, trigger a heap overflow and result in reading random heap memory, heap corruption, and potentially remote code execution. Specifically: using `COMMAND GETKEYS*` and validation of key names in ACL rules. (Redis 7.0.12)

- (CVE-2023-28856) Authenticated users can use the `HINCRBYFLOAT` command to create an invalid hash field that will crash Redis on access. (Redis 7.0.11)

- (CVE-2023-28425) Specially crafted `MSETNX` commands can lead to assertion and denial-of-service. (Redis 7.0.10)

- (CVE-2023-25155) Specially crafted `SRANDMEMBER`, `ZRANDMEMBER`, and `HRANDFIELD` commands can trigger an integer overflow, resulting in a runtime assertion and termination of the Redis server process. (Redis 7.0.9)

- (CVE-2023-22458) Integer overflow in the Redis `HRANDFIELD` and `ZRANDMEMBER` commands can lead to denial-of-service. (Redis 7.0.8)

- (CVE-2022-36021) String matching commands (like `SCAN` or `KEYS`) with a specially crafted pattern to trigger a denial-of-service attack on Redis can cause it to hang and consume 100% CPU time. (Redis 7.0.9)

- (CVE-2022-35977) Integer overflow in the Redis `SETRANGE` and `SORT`/`SORT_RO` commands can drive Redis to OOM panic. (Redis 7.0.8)

- (CVE-2022-35951) Executing an `XAUTOCLAIM` command on a stream key in a specific state, with a specially crafted `COUNT` argument, may cause an integer overflow, a subsequent heap overflow, and potentially lead to remote code execution. The problem affects Redis versions 7.0.0 or newer. (Redis 7.0.5)

- (CVE-2022-31144) A specially crafted `XAUTOCLAIM` command on a stream key in a specific state may result in heap overflow and potentially remote code execution. The problem affects Redis versions 7.0.0 or newer. (Redis 7.0.4)

- (CVE-2022-24834) A specially crafted Lua script executing in Redis can trigger a heap overflow in the cjson and cmsgpack libraries, and result in heap corruption and potentially remote code execution. The problem exists in all versions of Redis with Lua scripting support, starting from 2.6, and affects only authenticated and authorized users. (Redis 7.0.12)

- (CVE-2022-24736) An attacker attempting to load a specially crafted Lua script can cause NULL pointer dereference which will result in a crash of the `redis-server` process. This issue affects all versions of Redis. (Redis 7.0.0)

- (CVE-2022-24735) By exploiting weaknesses in the Lua script execution environment, an attacker with access to Redis can inject Lua code that will execute with the (potentially higher) privileges of another Redis user. (Redis 7.0.0)

{{< /collapsible >}}

{{< collapsible "Redis 6.2.x" >}}

- Memory corruption in `SLOT_INFO` handling may allow an unauthenticated user to potentially run their own code.

- A use-after-free in TLS pending-data processing may allow an authenticated user to cause a denial-of-service.

- A vulnerability in the `RESTORE` command and in RDB loading allows an authenticated user to trigger a use-after-free in stream consumer groups via a specially crafted serialized payload, potentially resulting in remote code execution.

- An ACL key-pattern bypass in `GEORADIUS` and `GEORADIUSBYMEMBER` may allow an authenticated user to write to keys outside their permitted key patterns.

- An out-of-bounds read during command key extraction may cause the server to crash.

- (CVE-2026-62356) An authenticated user may trigger a heap out-of-bounds write in RedisBloom by loading a specially crafted Count-Min Sketch (`CMSketch`) object, for example via the `RESTORE` command or a crafted RDB file.

- RedisBloom: Out-of-bounds access in the `TopK` heap cleanup path.

- (CVE-2026-23479) When a blocked client is evicted while re-executing a blocked command, an authenticated user may trigger a use-after-free and potentially lead to remote code execution.

- (CVE‑2026‑25243) A vulnerability in the Redis `RESTORE` command allows an authenticated user to trigger an invalid memory access via a specially crafted serialized payload, potentially resulting in remote code execution.

- (CVE-2026-25588) A vulnerability in the `RESTORE` command, when used with the RedisTimeSeries module, allows an authenticated attacker to trigger invalid memory access via a specially crafted serialized payload, potentially resulting in remote code execution.

- (CVE‑2026‑25589) A vulnerability in the `RESTORE` command, when used with the RedisBloom module, allows an authenticated attacker to trigger invalid memory access via a specially crafted serialized payload, potentially resulting in remote code execution.

- (CVE-2026-23631) An authenticated user may exploit the synchronization mechanism of the master-replica and trigger a use-after-free vulnerability, potentially leading to remote code execution. The bug affects only replicas that are configured, or may be configured with `replica-read-only` disabled, and exists in all versions of Redis with Lua scripting.

- Insufficient sanitization of Lua script error messages can allow an authenticated user with `EVAL` permission to inject arbitrary RESP protocol responses, leading to denial of service, data manipulation, and connection pool poisoning.

- RedisBloom: Integer overflow in `TopK` RDB loading may lead to heap out-of-bounds access.

- RedisBloom: Missing validation in `td_histogram_t` RDB loading may lead to heap buffer overflow.

- RedisBloom: Missing validation in `CuckooFilter` RDB loading may lead to heap out-of-bounds access.

- RedisBloom: Missing validation in `SBChain` and `CMSketch` RDB loading may lead to heap out-of-bounds write.

- Added validation of limits during RDB load and data creation to avoid resource exhaustion and Denial-of-Service (DoS) vulnerabilities.

- RedisBloom: Restore invalid filter.

- Integer overflow in `hllPatLen`.

- RedisBloom: Cuckoo filter counter overflow.

- RedisBloom: Invalid Bloom filters can cause arbitrary memory reads and writes.

- RedisBloom: Reachable assert in `TopK_Create`

- RedisBloom: Out-of-bounds access with empty Bloom chains.

- RedisBloom: Division by zero in Cuckoo filter insertion.

- (CVE-2025-46818) An authenticated user may use a specially crafted Lua script to manipulate different LUA objects and potentially run their own code in the context of another user.

- (CVE-2025-46819) An authenticated user may use a specially crafted LUA script to read out-of-bound data or crash the server and lead to subsequent denial of service.

- (CVE-2025-46817) An authenticated user may use a specially crafted Lua script to cause an integer overflow and potentially lead to remote code execution.

- (CVE-2025-49844) An authenticated user may use a specially crafted Lua script to manipulate the garbage collector, trigger a use-after-free, and potentially lead to remote code execution.

- (CVE-2025-32023) An authenticated user can use a specially crafted string to trigger a stack/heap out-of-bounds write on HyperLogLog operations, which can lead to remote code execution.

- (CVE-2025-21605) An unauthenticated client can cause unlimited growth of output buffers until the server runs out of memory or is terminated, which can lead to denial-of-service.

- (CVE-2024-31449) An authenticated user may use a specially crafted Lua script to trigger a stack buffer overflow in the bit library, which may potentially lead to remote code execution.

- (CVE-2024-31228) An authenticated user can trigger a denial-of-service by using specially crafted, long string match patterns on supported commands such as `KEYS`, `SCAN`, `PSUBSCRIBE`, `FUNCTION LIST`, `COMMAND LIST`, and ACL definitions. Matching of extremely long patterns may result in unbounded recursion, leading to stack overflow and process crashes.

- (CVE-2023-28856) Authenticated users can use the `HINCRBYFLOAT` command to create an invalid hash field that will crash Redis on access. (Redis 6.2.12)

- (CVE-2023-25155) Specially crafted `SRANDMEMBER`, `ZRANDMEMBER`, and `HRANDFIELD` commands can trigger an integer overflow, resulting in a runtime assertion and termination of the Redis server process. (Redis 6.2.11)

- (CVE-2023-22458) Integer overflow in the Redis `HRANDFIELD` and `ZRANDMEMBER` commands can lead to denial-of-service. (Redis 6.2.9)

- (CVE-2022-36021) String matching commands (like `SCAN` or `KEYS`) with a specially crafted pattern to trigger a denial-of-service attack on Redis can cause it to hang and consume 100% CPU time. (Redis 6.2.11)

- (CVE-2022-35977) Integer overflow in the Redis `SETRANGE` and `SORT`/`SORT_RO` commands can drive Redis to OOM panic. (Redis 6.2.9)

- (CVE-2022-24834) A specially crafted Lua script executing in Redis can trigger a heap overflow in the cjson and cmsgpack libraries, and result in heap corruption and potentially remote code execution. The problem exists in all versions of Redis with Lua scripting support, starting from 2.6, and affects only authenticated and authorized users. (Redis 6.2.13)

- (CVE-2022-24736) An attacker attempting to load a specially crafted Lua script can cause NULL pointer dereference which will result in a crash of the `redis-server` process. This issue affects all versions of Redis. (Redis 6.2.7)

- (CVE-2022-24735) By exploiting weaknesses in the Lua script execution environment, an attacker with access to Redis can inject Lua code that will execute with the (potentially higher) privileges of another Redis user. (Redis 6.2.7)

- (CVE-2021-41099) Integer to heap buffer overflow handling certain string commands and network payloads, when `proto-max-bulk-len` is manually configured to a non-default, very large value. (Redis 6.2.6)

- (CVE-2021-32762) Integer to heap buffer overflow issue in `redis-cli` and `redis-sentinel` parsing large multi-bulk replies on some older and less common platforms. (Redis 6.2.6)

- (CVE-2021-32761) An integer overflow bug in Redis version 2.2 or newer can be exploited using the `BITFIELD` command to corrupt the heap and potentially result with remote code execution. (Redis 6.2.5)

- (CVE-2021-32687) Integer to heap buffer overflow with intsets, when `set-max-intset-entries` is manually configured to a non-default, very large value. (Redis 6.2.6)

- (CVE-2021-32675) Denial Of Service when processing RESP request payloads with a large number of elements on many connections. (Redis 6.2.6)

- (CVE-2021-32672) Random heap reading issue with Lua Debugger. (Redis 6.2.6)

- (CVE-2021-32628) Integer to heap buffer overflow handling ziplist-encoded data types, when configuring a large, non-default value for `hash-max-ziplist-entries`, `hash-max-ziplist-value`, `zset-max-ziplist-entries` or `zset-max-ziplist-value`. (Redis 6.2.6)

- (CVE-2021-32627) Integer to heap buffer overflow issue with streams, when configuring a non-default, large value for `proto-max-bulk-len` and `client-query-buffer-limit`. (Redis 6.2.6)

- (CVE-2021-32626) Specially crafted Lua scripts may result with Heap buffer overflow. (Redis 6.2.6)

- (CVE-2021-32625) An integer overflow bug in Redis version 6.0 or newer can be exploited using the STRALGO LCS command to corrupt the heap and potentially result with remote code execution. This is a result of an incomplete fix by CVE-2021-29477. (Redis 6.2.4)

- (CVE-2021-29478) An integer overflow bug in Redis 6.2 could be exploited to corrupt the heap and potentially result with remote code execution. The vulnerability involves changing the default set-max-intset-entries configuration value, creating a large set key that consists of integer values and using the COPY command to duplicate it. The integer overflow bug exists in all versions of Redis starting with 2.6, where it could result with a corrupted RDB or DUMP payload, but not exploited through COPY (which did not exist before 6.2). (Redis 6.2.3)

- (CVE-2021-29477) An integer overflow bug in Redis version 6.0 or newer could be exploited using the STRALGO LCS command to corrupt the heap and potentially result in remote code execution. The integer overflow bug exists in all versions of Redis starting with 6.0. (Redis 6.2.3)

{{< /collapsible >}}
