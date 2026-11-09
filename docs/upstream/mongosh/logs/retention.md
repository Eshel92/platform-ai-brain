<!-- Converted from logs/retention.txt (reStructuredText). Includes are inlined. -->

# Log Retention

You can customize how MongoDB Shell logs are retained. By default, the
system retains 100 log files for 30 days. You can choose to retain logs
based on a combination of time, storage size, and number of log files.

## Get Started

To customize log retention, see these pages:

- mongosh-log-file-duration
- mongosh-log-retention-gb
- mongosh-log-file-count

## Details

You can specify multiple criteria for log retention. For example, you
can specify a maximum duration for log files of 60 days and a maximum
log storage size of 2GB. Logs are deleted when any retention criterion
is met, starting with the oldest logs.
