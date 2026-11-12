<!-- Part 12 of 193 of reference/crd/k8ssandra-operator-crds-latest/_index.md (split because the page is big). -->

#### K8ssandraCluster.spec.cassandra.datacenters[index].config.jvmOptions
<sup><sup>[↩ Parent](#k8ssandraclusterspeccassandradatacentersindexconfig)</sup></sup>





<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>additionalJvm11ServerOptions</b></td>
        <td>[]string</td>
        <td>
          Jvm11ServerOptions are additional options that will be passed on to the jvm11-server-options file.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>additionalJvm8ServerOptions</b></td>
        <td>[]string</td>
        <td>
          Jvm8ServerOptions are additional options that will be passed on to the jvm8-server-options file.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>additionalJvmServerOptions</b></td>
        <td>[]string</td>
        <td>
          JvmServerOptions are additional options that will be passed on to the jvm-server-options file.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>additionalOptions</b></td>
        <td>[]string</td>
        <td>
          Additional, arbitrary JVM options which are written into the cassandra-env.sh file.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>cassandra_available_processors</b></td>
        <td>integer</td>
        <td>
          Available CPU processors.
Disabled by default.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -Dcassandra.available_processors.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>cassandra_disable_auth_caches_remote_configuration</b></td>
        <td>boolean</td>
        <td>
          Disable remote configuration via JMX of auth caches.
Disabled by default.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -Dcassandra.disable_auth_caches_remote_configuration.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>cassandra_expiration_date_overflow_policy</b></td>
        <td>string</td>
        <td>
          Defines how to handle INSERT requests with TTL exceeding the maximum supported expiration
date.
Possible values include `REJECT`, `CAP`, `CAP_NOWARN`.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -Dcassandra.expiration_date_overflow_policy.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>cassandra_force_3_0_protocol_version</b></td>
        <td>boolean</td>
        <td>
          Disabled by default.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Corresponds to: -Dcassandra.force_3_0_protocol_version=true.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>cassandra_force_default_indexing_page_size</b></td>
        <td>boolean</td>
        <td>
          Disable dynamic calculation of the page size used when indexing an entire partition (during
initial index build/rebuild).
Disabled by default.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -Dcassandra.force_default_indexing_page_size.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>cassandra_max_hint_ttl_seconds</b></td>
        <td>integer</td>
        <td>
          Imposes an upper bound on hint lifetime below the normal min gc_grace_seconds.
Disabled by default.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -Dcassandra.maxHintTTL.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>cassandra_metrics_reporter_config_file</b></td>
        <td>string</td>
        <td>
          Enable pluggable metrics reporter.
Disabled by default.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -Dcassandra.metricsReporterConfigFile.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>cassandra_ring_delay_ms</b></td>
        <td>integer</td>
        <td>
          Amount of time in milliseconds that a node waits before joining the ring.
Disabled by default.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -Dcassandra.ring_delay_ms.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>cassandra_triggers_directory</b></td>
        <td>string</td>
        <td>
          Default location for the trigger JARs.
Disabled by default.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -Dcassandra.triggers_dir.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>cassandra_write_survey</b></td>
        <td>boolean</td>
        <td>
          For testing new compaction and compression strategies.
Disabled by default.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -Dcassandra.write_survey.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>debug_disable_contended_annotations</b></td>
        <td>boolean</td>
        <td>
          Disable honoring user code @Contended annotations.
Enabled by default.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -XX:-RestrictContended.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>debug_enable_flight_recorder</b></td>
        <td>boolean</td>
        <td>
          Enable Flight Recorder (Use in production is subject to Oracle licensing).
Disabled by default.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -XX:+FlightRecorder.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>debug_listen_remote_debuggers</b></td>
        <td>boolean</td>
        <td>
          Listen for JVM remote debuggers on port 1414.
Disabled by default.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=1414".<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>debug_log_compilation</b></td>
        <td>boolean</td>
        <td>
          Make Cassandra JVM log internal method compilation (developers only).
Disabled by default.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -XX:+LogCompilation.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>debug_non_safepoints</b></td>
        <td>boolean</td>
        <td>
          Whether the compiler should generate the necessary metadata for the parts of the code not at
safe points as well. For use with Flight Recorder.
Enabled by default.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -XX:+DebugNonSafepoints.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>debug_preserve_frame_pointer</b></td>
        <td>boolean</td>
        <td>
          Preserve Frame Pointer.
Enabled by default.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -XX:+PreserveFramePointer.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>debug_unlock_commercial_features</b></td>
        <td>boolean</td>
        <td>
          Unlock commercial features.
Disabled by default.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -XX:+UnlockCommercialFeatures.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>debug_unlock_diagnostic_vm_options</b></td>
        <td>boolean</td>
        <td>
          Enabled by default.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -XX:+UnlockDiagnosticVMOptions.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>gc</b></td>
        <td>enum</td>
        <td>
          The name of the garbage collector to use. Depending on the Cassandra version, not all values
are supported: Cassandra 3.11 supports only G1GC and CMS; Cassandra 4.0 supports G1GC, ZGC,
Shenandoah and Graal. This option will unlock the corresponding garbage collector with a
default configuration; to further tune the GC settings, use the additional JVM options field.
Use the special value Custom if you intend to use non-standard garbage collectors.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Cass Config Builder: supported for Cassandra 4.0 in jvm11-server.options.<br/>
          <br/>
            <i>Enum</i>: G1GC, CMS, ZGC, Shenandoah, Graal, Custom<br/>
            <i>Default</i>: G1GC<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>gc_cms_heap_size_young_generation</b></td>
        <td>int or string</td>
        <td>
          Disabled by default. Can only be used when CMS garbage collector is used.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Corresponds to: -Xmn.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>gc_cms_initiating_occupancy_fraction</b></td>
        <td>integer</td>
        <td>
          Defaults to 75. Can only be used when CMS garbage collector is used.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Corresponds to: -XX:CMSInitiatingOccupancyFraction.<br/>
          <br/>
            <i>Minimum</i>: 0<br/>
            <i>Maximum</i>: 100<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>gc_cms_max_tenuring_threshold</b></td>
        <td>integer</td>
        <td>
          Defaults to 1. Can only be used when CMS garbage collector is used.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Corresponds to: -XX:MaxTenuringThreshold.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>gc_cms_survivor_ratio</b></td>
        <td>integer</td>
        <td>
          Defaults to 8. Can only be used when CMS garbage collector is used.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Corresponds to: -XX:SurvivorRatio.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>gc_cms_wait_duration_ms</b></td>
        <td>integer</td>
        <td>
          Defaults to 10000. Can only be used when CMS garbage collector is used.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Corresponds to: -XX:CMSWaitDuration.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>gc_g1_conc_threads</b></td>
        <td>integer</td>
        <td>
          Concurrent GC Threads. Can only be used when G1 garbage collector is used.
Disabled by default.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Cass Config Builder: supported for Cassandra 4.0 in jvm11-server.options.
Corresponds to: -XX:ConcGCThreads.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>gc_g1_initiating_heap_occupancy_percent</b></td>
        <td>integer</td>
        <td>
          Initiating Heap Occupancy Percentage. Can only be used when G1 garbage collector is used.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Cass Config Builder: supported for Cassandra 4.0 in jvm11-server.options.
Corresponds to: -XX:InitiatingHeapOccupancyPercent.<br/>
          <br/>
            <i>Minimum</i>: 0<br/>
            <i>Maximum</i>: 100<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>gc_g1_max_gc_pause_ms</b></td>
        <td>integer</td>
        <td>
          G1GC Max GC Pause in milliseconds. Defaults to 500. Can only be used when G1 garbage collector is used.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Cass Config Builder: supported for Cassandra 4.0 in jvm11-server.options.
Corresponds to: -XX:MaxGCPauseMillis.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>gc_g1_parallel_threads</b></td>
        <td>integer</td>
        <td>
          Parallel GC Threads. Can only be used when G1 garbage collector is used.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Cass Config Builder: supported for Cassandra 4.0 in jvm11-server.options.
Corresponds to: -XX:ParallelGCThreads.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>gc_g1_rset_updating_pause_time_percent</b></td>
        <td>integer</td>
        <td>
          G1GC Updating Pause Time Percentage. Defaults to 5. Can only be used when G1 garbage collector is used.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Cass Config Builder: supported for Cassandra 4.0 in jvm11-server.options.
Corresponds to: -XX:G1RSetUpdatingPauseTimePercent.<br/>
          <br/>
            <i>Minimum</i>: 0<br/>
            <i>Maximum</i>: 100<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>gc_print_application_stopped_time</b></td>
        <td>boolean</td>
        <td>
          Print GC Application Stopped Time.
Disabled by default.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Corresponds to: -XX:+PrintGCApplicationStoppedTime.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>gc_print_date_stamps</b></td>
        <td>boolean</td>
        <td>
          Print GC Date Stamps. Disabled by default.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Corresponds to: -XX:+PrintGCDateStamps.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>gc_print_details</b></td>
        <td>boolean</td>
        <td>
          Print GC details.
Disabled by default.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Corresponds to: -XX:+PrintGCDetails.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>gc_print_flss_statistics</b></td>
        <td>boolean</td>
        <td>
          Print FLSS Statistics.
Disabled by default.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Corresponds to: -XX:PrintFLSStatistics=1.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>gc_print_heap</b></td>
        <td>boolean</td>
        <td>
          Print Heap at GC.
Disabled by default.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Corresponds to: -XX:+PrintHeapAtGC.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>gc_print_log_file_size</b></td>
        <td>int or string</td>
        <td>
          Size of each log file.
Disabled by default.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Corresponds to: -XX:GCLogFileSize.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>gc_print_number_of_log_files</b></td>
        <td>integer</td>
        <td>
          Number of GC log files.
Disabled by default. Can only be used when the G1 garbage collector is used.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Corresponds to: -XX:NumberOfGCLogFiles.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>gc_print_promotion_failure</b></td>
        <td>boolean</td>
        <td>
          Print promotion failure.
Disabled by default.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Corresponds to: -XX:+PrintPromotionFailure.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>gc_print_tenuring_distribution</b></td>
        <td>boolean</td>
        <td>
          Print tenuring distribution.
Defaults to false.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Corresponds to: -XX:+PrintTenuringDistribution.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>gc_print_use_log_file</b></td>
        <td>boolean</td>
        <td>
          Whether to print GC logs to /var/log/cassandra/gc.log.
Disabled by default.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Corresponds to: -Xloggc:/var/log/cassandra/gc.log.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>gc_print_use_log_file_rotation</b></td>
        <td>boolean</td>
        <td>
          Use GC Log File Rotation.
Disabled by default.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Corresponds to: -XX:+UseGCLogFileRotation.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>heapNewGenSize</b></td>
        <td>int or string</td>
        <td>
          Deprecated. Use gc_cms_heap_size_young_generation instead.
Valid for CMS garbage collector only + Cassandra 3.11.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>heapSize</b></td>
        <td>int or string</td>
        <td>
          Deprecated. Use heap_initial_size and heap_max_size instead. If this field is defined,
it applies to both max_heap_size and initial_heap_size.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>heap_initial_size</b></td>
        <td>int or string</td>
        <td>
          Disabled by default.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -Xms.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>heap_max_size</b></td>
        <td>int or string</td>
        <td>
          Disabled by default.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -Xmx.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>jdk_allow_attach_self</b></td>
        <td>boolean</td>
        <td>
          Allow the current VM to attach to itself.
Defaults to true.
Cass Config Builder: supported for Cassandra 4.0 in jvm11-server.options.
Corresponds to: -Djdk.attach.allowAttachSelf=true.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>jmx_connection_type</b></td>
        <td>string</td>
        <td>
          Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Possible values for 3.11 include `local-no-auth`, `remote-no-auth`, and `remote-dse-unified-auth`. Defaults to `local-no-auth`.
Possible values for 4.0 include `local-no-auth`, `remote-no-auth`. Defaults to `local-no-auth`.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>jmx_port</b></td>
        <td>integer</td>
        <td>
          Disabled by default. Defaults to 7199.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>jmx_remote_ssl</b></td>
        <td>boolean</td>
        <td>
          Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Defaults to false.
Valid only when JmxConnectionType is "remote-no-auth", "remote-dse-unified-auth".<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>jmx_remote_ssl_opts</b></td>
        <td>string</td>
        <td>
          Remote SSL options.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>jmx_remote_ssl_require_client_auth</b></td>
        <td>boolean</td>
        <td>
          Require Client Authentication for remote SSL? Defaults to false.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>netty_eventloop_maxpendingtasks</b></td>
        <td>integer</td>
        <td>
          Defaults to 65536.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -Dio.netty.eventLoop.maxPendingTasks.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>netty_try_reflection_set_accessible</b></td>
        <td>boolean</td>
        <td>
          Netty setting `io.netty.tryReflectionSetAccessible`.
Defaults to true.
Cass Config Builder: supported for Cassandra 4.0 in jvm11-server.options.
Corresponds to: -Dio.netty.tryReflectionSetAccessible=true.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>nio_align_direct_memory</b></td>
        <td>boolean</td>
        <td>
          Align direct memory allocations on page boundaries.
Enabled by default.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -Dsun.nio.PageAlignDirectMemory=true.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>nio_maxcachedbuffersize</b></td>
        <td>int or string</td>
        <td>
          Defaults to 1048576.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -Djdk.nio.maxCachedBufferSize.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>vm_always_pre_touch</b></td>
        <td>boolean</td>
        <td>
          Ensure all memory is faulted and zeroed on startup.
Enabled by default.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -XX:+AlwaysPreTouch.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>vm_crash_on_out_of_memory_error</b></td>
        <td>boolean</td>
        <td>
          Disabled by default. Requires `exit_on_out_of_memory_error` to be disabled..
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -XX:+CrashOnOutOfMemoryError.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>vm_disable_biased_locking</b></td>
        <td>boolean</td>
        <td>
          Disable biased locking to avoid biased lock revocation pauses.
Disabled by default.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -XX:-UseBiasedLocking.
Note: the Cass Config Builder option is named use_biased_locking, but setting it to true
disables biased locking.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>vm_disable_perf_shared_mem</b></td>
        <td>boolean</td>
        <td>
          Disable hsperfdata mmap'ed file.
Enabled by default.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -XX:+PerfDisableSharedMem.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>vm_enable_assertions</b></td>
        <td>boolean</td>
        <td>
          Enable assertions.
Enabled by default.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -ea.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>vm_enable_non_root_thread_priority</b></td>
        <td>boolean</td>
        <td>
          Enable lowering thread priority without being root on linux.
See CASSANDRA-1181 for details.
Enabled by default.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Corresponds to: -XX:ThreadPriorityPolicy=42.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>vm_enable_thread_priorities</b></td>
        <td>boolean</td>
        <td>
          Enable thread priorities.
Enabled by default.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -XX:+UseThreadPriorities.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>vm_exit_on_out_of_memory_error</b></td>
        <td>boolean</td>
        <td>
          Disabled by default.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -XX:+ExitOnOutOfMemoryError.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>vm_guaranteed_safepoint_interval_ms</b></td>
        <td>integer</td>
        <td>
          Defaults to 300000 milliseconds.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -XX:GuaranteedSafepointInterval.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>vm_heap_dump_on_out_of_memory_error</b></td>
        <td>boolean</td>
        <td>
          Enabled by default.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -XX:+HeapDumpOnOutOfMemoryError.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>vm_per_thread_stack_size</b></td>
        <td>int or string</td>
        <td>
          Per-thread stack size.
Defaults to 256Ki.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -Xss.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>vm_prefer_ipv4</b></td>
        <td>boolean</td>
        <td>
          Prefer binding to IPv4 network interfaces.
Enabled by default.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -Djava.net.preferIPv4Stack=true.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>vm_print_heap_histogram_on_out_of_memory_error</b></td>
        <td>boolean</td>
        <td>
          Disabled by default.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -Dcassandra.printHeapHistogramOnOutOfMemoryError.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>vm_resize_tlab</b></td>
        <td>boolean</td>
        <td>
          Allow resizing of thread-local allocation blocks.
Enabled by default.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -XX:+ResizeTLAB.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>vm_string_table_size</b></td>
        <td>int or string</td>
        <td>
          The size of interned string table. Larger sizes are beneficial to gossip.
Defaults to 1000003.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -XX:StringTableSize.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>vm_use_numa</b></td>
        <td>boolean</td>
        <td>
          Enabled by default.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -XX:+UseNUMA.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>vm_use_tlab</b></td>
        <td>boolean</td>
        <td>
          Enable thread-local allocation blocks.
Enabled by default.
Cass Config Builder: supported for Cassandra 3.11 in jvm.options.
Cass Config Builder: supported for Cassandra 4.0 in jvm-server.options.
Corresponds to: -XX:+UseTLAB.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>
