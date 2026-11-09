<!-- Converted from reference/aggregation-variables.txt (reStructuredText). Includes are inlined. -->

# Variables in Aggregation Expressions

Aggregation expressions can use both
user-defined and system variables.

Variables can hold any BSON type data.
To access the value of the variable, prefix the variable name with
double dollar signs (`$$`); i.e. `"$$<variable>"`.

If the variable references an object, to access a specific field in the
object, use the dot notation; i.e. `"$$<variable>.<field>"`.

## User Variables

User variable names can contain the ascii characters `[_a-zA-Z0-9]`
and any non-ascii character.

User variable names must begin with a lowercase ascii letter `[a-z]`
or a non-ascii character.

## System Variables

MongoDB offers the following system variables:

* - Variable

  - Description

* - .. variable:: NOW

  - A variable that returns the current datetime value.
    `NOW` returns the same value for all members of the
    deployment and remains the same throughout all stages of the
    aggregation pipeline.

* - .. variable:: CLUSTER_TIME

  - A variable that returns the current timestamp value.

    `CLUSTER_TIME` is only available on replica sets and
    sharded clusters.

    `CLUSTER_TIME` returns the same value for all members
    of the deployment and remains the same throughout all stages of
    the pipeline.

* - .. variable:: ROOT

  - References the root document, i.e. the top-level document, currently
    being processed in the aggregation pipeline stage.

* - .. variable:: CURRENT

  - References the start of the field path being processed in the
    aggregation pipeline stage. Unless documented otherwise, all
    stages start with `CURRENT` the same as
    `ROOT`.

    `CURRENT` is modifiable. However, since `$<field>`
    is equivalent to `$$CURRENT.<field>`, rebinding
    `CURRENT` changes the meaning of `$` accesses.

* - .. variable:: REMOVE

  - A variable which evaluates to the missing value. Allows for the
    exclusion of fields in `$addFields` and
    `$project` stages.

    For examples that use `$$REMOVE`, see:

    - addFields-remove-example
    - remove-example

* - .. variable:: DESCEND

  - One of the allowed results of a `$redact` expression.

* - .. variable:: PRUNE

  - One of the allowed results of a `$redact` expression.

* - .. variable:: KEEP

  - One of the allowed results of a `$redact` expression.

* - .. variable:: SEARCH_META 

  - A variable that stores the metadata results of an Atlas 
    Search query. In all supported aggregation 
    pipeline stages, a field set to the variable 
    `$$SEARCH_META` returns the metadata results
    for the query.

    For an example of its usage, see Atlas Search facet 
    and count.

**See also:**

- `$let`
- `$redact`
- `$map`
