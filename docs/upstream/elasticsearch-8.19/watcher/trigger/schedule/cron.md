<!-- Converted from watcher/trigger/schedule/cron.asciidoc (AsciiDoc). Includes are inlined. -->

#### Watcher cron schedule

Defines a `schedule` using a cron expression
that specifiues when to execute a watch.

**Tip:** While cron expressions are powerful, a regularly occurring schedule
is easier to configure with the other schedule types.
If you must use a cron schedule, make sure you verify it with
`elasticsearch-croneval` .

##### Configure a cron schedule with one time

To configure a `cron` schedule, you simply specify the cron expression as a
string value. For example, the following snippet configures a `cron` schedule
that triggers every day at noon:

```js
{
  ...
  "trigger" : {
    "schedule" : {
      "cron" : "0 0 12 * * ?"
    }
  }
  ...
}
```

##### Configure a cron schedule with multiple times

To configure a `cron` schedule that triggers multiple times, you can
specify an array of cron expressions. For example, the following `cron`
schedule triggers every even minute during weekdays and every uneven
minute during the weekend:

```js
{
  ...
  "trigger" : {
    "schedule" : {
      "cron" : [
        "0 0/2 * ? * MON-FRI",
        "0 1-59/2 * ? * SAT-SUN"
      ]
    }
  }
  ...
}
```

#### Use a different time zone for a cron schedule

By default, cron expressions are evaluated in the UTC time zone. To use a different time zone,
you can specify the `timezone` parameter in the schedule. For example, the following
`cron` schedule triggers at 6:00 AM and 6:00 PM during weekends in the `America/Los_Angeles` time zone:

```js
{
  ...
  "trigger" : {
    "schedule" : {
      "timezone" : "America/Los_Angeles",
      "cron" : [
        "0 6,18 * * * SAT-SUN",
      ]
    }
  }
  ...
}
```

##### Use croneval to validate cron expressions

Elasticsearch provides a `elasticsearch-croneval` command line tool
in the `$ES_HOME/bin` directory that you can use to check that your cron expressions
are valid and produce the expected results.

To validate a cron expression, pass it in as a parameter to `elasticsearch-croneval`:

```bash
bin/elasticsearch-croneval "0 0/1 * * * ?"
```
