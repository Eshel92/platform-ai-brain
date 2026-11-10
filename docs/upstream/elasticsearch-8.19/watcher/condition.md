<!-- Converted from watcher/condition.asciidoc (AsciiDoc). Includes are inlined. -->

## Watcher conditions

When a watch is triggered, its condition determines whether or not to execute
the watch actions. Watcher supports the following condition types:

* `always`: The condition always evaluates to `true`, so the watch actions are always performed.
* `never`: The condition always evaluates to `false`, so the watch
actions are never executed.
* `compare`: perform simple comparisons against values
in the watch payload to determine whether or not to execute the watch actions.
* `array_compare`: compare an array of values in the
watch payload to a given value to determine whether or not to execute the watch
actions.
* `script`: use a script to determine whether or not to
execute the watch actions.

**Note:** If you omit the condition definition from a watch, the condition defaults
      to `always`.

When a condition is evaluated, it has full access to the watch execution context,
including the watch payload (`ctx.payload.*`). The script,
compare  and array_compare
conditions can use the payload data to determine whether or not the necessary
conditions are met.

In addition to the watch wide condition, you can also configure conditions
per action.

(See `watcher/condition/always.md`)
(See `watcher/condition/never.md`)
(See `watcher/condition/compare.md`)
(See `watcher/condition/array-compare.md`)
(See `watcher/condition/script.md`)
