<!-- Converted from core/databases-and-collections.txt (reStructuredText). Includes are inlined. -->

# Databases and Collections in MongoDB

MongoDB stores data records as documents
(BSON documents) in
collections. A database
holds one or more collections.

You can manage databases and
collections using the Atlas UI,
`mongosh`, or MongoDB Compass. This page covers Atlas UI
procedures. For self-managed deployments, use
`mongosh` or MongoDB Compass.

Select your client:

**atlas:**

**mongosh:**

The MongoDB Shell, `mongosh`, is a JavaScript and
Node.js REPL (Read Eval Print Loop) environment for
interacting with MongoDB deployments. To learn more, see
`mongosh`.

**compass:**

MongoDB Compass is a powerful GUI for querying, aggregating,
and analyzing your MongoDB data in a visual environment. To
learn more, see `MongoDB Compass`.

## Databases

**atlas:**

Log in to Atlas and go to the Data Explorer
page for your project.

**Step 1: Select your organization and project**

a. If it's not already displayed, select the
   organization that contains your project from
   the `office` Organizations menu in the navigation bar.

#. If it's not already displayed, select your
   project from the Projects menu
   in the navigation bar.

**Step 2: Open the Data Explorer**

In the sidebar, click Data Explorer
under the Database heading.

The Data Explorer displays.

**mongosh:**

Issue the `use <db>` statement:

```javascript
      use myDB

.. tab:: MongoDB Compass
   :tabid: compass

   .. procedure::
      :style: normal

      .. step:: Start MongoDB Compass and connect to your cluster.

         To learn more, see :compass:`Connect to MongoDB
         </connect/>`.

      .. step:: Select :guilabel:`Databases`.

         The :guilabel:`Databases` tab lists the existing
         databases for your deployment.
```

### Create a Database

**atlas:**

(Text shared from another MongoDB docs repo, not available offline: cet/atlas/data-explorer/steps-atlas-ui-create-database.rst)

**mongosh:**

MongoDB creates the database when you first store data
for it. Switch to a non-existent database and run:

```javascript
use myNewDB

db.myNewCollection1.insertOne( { x: 1 } )

   :method:`~db.collection.insertOne()` creates both the
   database ``myNewDB`` and the collection
   ``myNewCollection1`` if they do not already exist. Be
   sure that both names follow MongoDB
   :ref:`restrictions-on-db-names`.

.. tab:: MongoDB Compass
   :tabid: compass

   .. procedure::
      :style: normal

      .. step:: Open the :guilabel:`Databases` tab.

      .. step:: Click :guilabel:`Create database`.

      .. step:: Enter the database and collection names.

      .. step:: Click :guilabel:`Create Database`.
```

## Collections

MongoDB stores documents in collections. Collections are
analogous to tables in relational databases.

(Figure: /images/crud-annotated-collection.bakedsvg.svg)

### Create a Collection

If a collection does not exist, MongoDB creates the collection
when you first store data for that collection.

**atlas:**

(Text shared from another MongoDB docs repo, not available offline: cet/atlas/data-explorer/steps-atlas-ui-create-collection.rst)

**mongosh:**

```javascript
db.myNewCollection2.insertOne( { x: 1 } )
db.myNewCollection3.createIndex( { y: 1 } )

   Both :method:`~db.collection.insertOne()` and
   :method:`~db.collection.createIndex()` create their
   respective collection if it does not already exist.
   Be sure the collection name follows MongoDB
   :ref:`restrictions-on-db-names`.

.. tab:: MongoDB Compass
   :tabid: compass

   .. procedure::
      :style: normal

      .. step:: In the left navigation, click the database name.

      .. step:: Click :guilabel:`+` next to the database name.

      .. step:: Enter a name in :guilabel:`Create Collection`.

      .. step:: Click :guilabel:`Create Collection`.
```

**atlas:**

**mongosh:**

#### Explicit Creation

Use `db.createCollection()` to explicitly
create a collection with options such as maximum size
or validation rules. Without these options, MongoDB
automatically creates collections when you first store
data.

To modify these collection options, see
`collMod`.

**compass:**

#### Explicit creation

**Step 1: In the left navigation, click the database name.**

**Step 2: Click Create collection.**

**Step 3: Enter the collection name and optional preferences.**

**Step 4: Click Create Collection.**

MongoDB Compass supports the following additional
preferences:

- `Create a Capped Collection`
- `Create a Clustered Collection`
- `Create a Collection with Collation`
- `Create a Collection with Encrypted Field`
- `Create a Time Series Collection`

### Schema Validation

By default, documents in a collection do not share a schema.
Fields and data types can vary across documents.

You can enforce schema validation rules during insert and update
operations.

For MongoDB Atlas deployments, the Performance Advisor and the MongoDB Atlas UI detect common
schema design issues and suggest modifications that follow
MongoDB best practices. To learn more, see
Schema Suggestions.

### Modifying Document Structure

To add, remove, or retype fields in a collection's documents,
update the existing documents.

### Unique Identifiers

Collections are assigned an immutable
UUID (Universally unique identifier) that remains
consistent across all replica set members and shards.

**atlas:**

**mongosh:**

To retrieve the UUID for a collection, run either the
listCollections command or the
`db.getCollectionInfos()` method.

**compass:**
