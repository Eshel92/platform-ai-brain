<!-- Converted from scripting.asciidoc (AsciiDoc). Includes are inlined. -->

# Scripting

With scripting, you can evaluate custom expressions in Elasticsearch. For example, you
can use a script to return a computed value as a field or evaluate a custom
score for a query.

The default scripting language is Painless.
Additional `lang` plugins are available to run scripts written in other
languages. You can specify the language of the script anywhere that scripts run.

## Available scripting languages

Painless is purpose-built for Elasticsearch, can be used for any purpose in the
scripting APIs, and provides the most flexibility. The other languages are less
flexible, but can be useful for specific purposes.

|========
|Language
    |Sandboxed
    |Required plugin
    |Purpose

|`painless`
    |✓
    |Built-in
    |Purpose-built for Elasticsearch

|`expression`
    |✓
    |Built-in
    |Fast custom ranking and sorting

|`mustache`
    |✓
    |Built-in
    |Templates

|`java`
    |✗
    |You write it!
    |Expert API
|========

(See `scripting/painless.md`)
(See `scripting/using.md`)
(See `scripting/access-fields.md`)
(See `scripting/common-script-uses.md`)
(See `scripting/fields.md`)
(See `scripting/security.md`)
(See `scripting/expression.md`)
(See `scripting/engine.md`)
