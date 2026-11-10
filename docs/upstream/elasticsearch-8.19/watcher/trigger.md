<!-- Converted from watcher/trigger.asciidoc (AsciiDoc). Includes are inlined. -->

## Watcher triggers

Every watch must have a `trigger` that defines when the watch execution process
should start. When you create a watch, its trigger is registered with the
appropriate _Trigger Engine_. The trigger engine is responsible for evaluating
the trigger and triggering the watch when needed.

Watcher is designed to support different types of triggers, but only time-based
`schedule` triggers are currently available.

(See `watcher/trigger/schedule.md`)
