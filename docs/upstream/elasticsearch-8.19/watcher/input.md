<!-- Converted from watcher/input.asciidoc (AsciiDoc). Includes are inlined. -->

## Watcher inputs

When a watch is triggered, its _input_ loads data into the execution 
context. This payload is accessible during the subsequent watch execution 
phases. For example, you can base a watch's condition on the data loaded by its
input.

Watcher supports four input types: 

* `simple`: load static data into the execution context.
* `search`: load the results of a search into the execution 
context.
* `http`: load the results of an HTTP request into the execution
context.
* `chain`: use a series of inputs to load data into the 
execution context.

**Note:** If you don't define an input for a watch, an empty payload is loaded
      into the execution context.

(See `watcher/input/simple.md`)
(See `watcher/input/search.md`)
(See `watcher/input/http.md`)
(See `watcher/input/chain.md`)
