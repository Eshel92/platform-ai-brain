<!-- Converted from logs/retention/file-count.txt (reStructuredText). Includes are inlined. -->

# Modify Maximum Log File Count

You can specify the maximum number of log files that the MongoDB Shell
retains. After the MongoDB Shell reaches the maximum log file count, it
starts deleting the oldest log files until the count is below the
threshold.

The MongoDB Shell stores one log file for each session. By default, the
MongoDB Shell stores up to 100 log files.

## About this Task

You can specify multiple criteria for log retention. For example, you
can specify a maximum duration for log files of 60 days and a maximum
log storage size of 2GB. Logs are deleted when any retention criterion
is met, starting with the oldest logs.

## Before you Begin

To check the current maximum log file count, run the following command:

```javascript
config.get("logMaxFileCount")
```

## Steps

To modify the maximum log file count, set the `logMaxFileCount`
configuration option. You can set configuration options in the
configuration API or a
configuration file.

### Modify Maximum Log File Count with the Configuration API

The following command uses the config API to set the maximum log file
count to 200:

```javascript
config.set("logMaxFileCount", 200)
```

Output:

```javascript
Setting "logMaxFileCount" has been changed
```

### Modify Maximum Log File Count with a Configuration File

The following configuration file sets the maximum log file count to 200:

```yaml
mongosh:
  logMaxFileCount: 200
```

### Disable Maximum Log File Limit

To disable the maximum log file limit, set `logMaxFileCount` to
`Infinity`. You can perform this action through the config API or
configuration file. For example:

```javascript
config.set("logMaxFileCount", Infinity)
```

**Important:**

To prevent log storage from growing too large, always specify at
least one log retention criterion.
