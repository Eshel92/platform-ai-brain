<!-- Converted from reference/method/db.createView.txt (reStructuredText). Includes are inlined. -->

# db.createView()

   

**`db.createView()`**

**Note:** Disambiguation

This page discusses standard views. For discussion of on-demand
materialized views, see manual-materialized-views.

To understand the differences between the view types, see
view-materialized-view-compare.

Creates a view as the result of the applying
the specified aggregation pipeline to
the source collection or view. Views act as read-only collections,
and are computed on demand during read operations. You must create
views in the same database as the source collection. MongoDB
executes read operations on views as part of the underlying
aggregation pipeline.

A view definition `pipeline` cannot include the `$out` or
the `$merge` stage. This restriction also applies to
embedded pipelines, such as pipelines used in `$lookup` or
`$facet` stages.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

`db.createView` has the following syntax:

```javascript
db.createView(<view>, <source>, <pipeline>, <collation>)
```

The method accepts the following parameters:

* - Parameter

  - Type

  - Description

* - `view`

  - string

  - The name of the view to create.

* - `source`

  - string

  - The name of the source collection or view from which to create
    the view. The name does not include the database name and implies
    the same database as the view to create; it is not the full
    namespace of the collection or view. You must create views in the
    same database as the source collection.

* - `pipeline`

  - array

  - An array that consists of the aggregation pipeline stage(s).  `db.createView` creates the view by
    applying the specified `pipeline` to the `source` collection or view.

    A view definition `pipeline` cannot include the `$out` or
    the `$merge` stage. This restriction also applies to
    embedded pipelines, such as pipelines used in `$lookup` or
    `$facet` stages.

    The view definition is public; i.e. `db.getCollectionInfos()`
    and `explain` operations on the view will include the pipeline that
    defines the view. As such, avoid referring directly to sensitive fields
    and values in view definitions.

* - `collation`

  - document

  - Optional. Specifies the default collation for the view.

    Collation allows users to specify
    language-specific rules for string comparison, such as rules for
    lettercase and accent marks.

    If the underlying `source` is a collection, the view does not
    inherit the collection's collation settings. 

    If no collation is specified, the view's default collation is the
    "simple" binary comparison collator.

    If the underlying `source` is another view, the view must specify
    the same collation settings.

    The collation option has the following syntax:

    ```none
    collation: {
       locale: <string>,
       caseLevel: <boolean>,
       caseFirst: <string>,
       strength: <int>,
       numericOrdering: <boolean>,
       alternate: <string>,
       maxVariable: <string>,
       backwards: <boolean>
    }
    ```

    When specifying collation, the `locale` field is mandatory; all
    other collation fields are optional. For descriptions of the fields,
    see collation-document-fields.

The `db.createView()` method wraps the following
`create` command operation:

```javascript
db.runCommand( { create: <view>, viewOn: <source>, pipeline: <pipeline>, collation: <collation> } )
```

   

**Important:** View Names are Included in Collection List Output

Operations that list collections, such as
`db.getCollectionInfos()` and `db.getCollectionNames()`,
include views in their outputs.

The view definition is public; i.e. `db.getCollectionInfos()`
and `explain` operations on the view will include the pipeline that
defines the view. As such, avoid referring directly to sensitive fields
and values in view definitions.

## Examples

To see examples of creating a view, see the following pages:

- manual-views-create

- manual-views-lookup

- manual-views-collation

## Behavior

To see behavioral details of views, see manual-views-behavior.
