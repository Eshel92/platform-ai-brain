<!-- Converted from watcher/condition/always.asciidoc (AsciiDoc). Includes are inlined. -->

### Watcher always condition

Use the `always` condition to perform the watch actions whenever the watch is triggered, unless they are
throttled.

The `always` condition enables you to perform watch actions on a fixed schedule,
such as, _"Every Friday at noon, send a status report email to
sys.admin@example.com."_

#### Using the always condition

This is the default if you omit the condition definition from a watch.

There are no attributes to specify for the `always` condition. To explicitly
use this condition, specify the condition type and associate it with an empty
object:

```js
"condition" : {
  "always" : {}
}
```
