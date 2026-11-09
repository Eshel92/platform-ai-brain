<!-- Converted from data-explorer/databases-collections.txt (reStructuredText). Includes are inlined. -->

# Manage Databases and Collections in Data Explorer

You can use the Data Explorer to manage your cluster's
databases and collections.

To interact with data in the Ops Manager UI:

1. Click Deployment in the left navigation.

#. Select the desired MongoDB deployment.

#. Select the Data tab.

## Required Roles

### View Databases and Collections

To view databases and collections, through
the Data Explorer you must have been granted at least the
`Project Data Access Read Only` role.

### Create Databases and Collections

To create databases and
collections through the
Data Explorer, you must have been granted access through
one of the following roles:

- `Project Owner` or `Organization Owner`

- `Project Data Access Admin`

- `Project Data Access Read/Write`

### Drop Databases and Collections

To drop databases and
collections through the
Data Explorer, you must have been granted access through
one of the following roles:

- `Project Owner`

- `Project Data Access Admin`

## View Databases and Collections

From the Collections tab, you can view the databases and
collections in the deployment. Ops Manager shows the databases in the
left pane of the Data Explorer:

(Figure: /images/data-explorer-dbs.png)

To view the collections in a particular database, click on the
name of the database.

## Create a Database

To create a database through the Data Explorer:

**Step 1: Click Create Database.**

**Step 2: Enter the Database Name and the Collection Name.**

Enter the Database Name and the Collection
Name to create the database and its first collection. 

For more information on MongoDB database names and collection names,
see restrictions-on-db-names.

**Step 3: Optional. Specify a capped collection.**

Select whether the collection is a capped collection. If you select to create a capped
collection, specify the maximum size in bytes.

**Step 4: Click Create.**

Upon successful creation, the database and the collection appears in
the Data Explorer.

## Create a Collection

**Tip:**

To create the first collection in a new database, see
de-create-a-db.

To create a collection in an existing database through the Data
Explorer:

**Step 1: Click on the plus sign `+` icon for a database.**

Either select or hover over the database to drop and click on the
plus sign `+` icon.

**Step 2: Enter the Collection Name.**

For more information on MongoDB collection names, see
restrictions-on-db-names.

**Step 3: Optional. Specify a capped collection.**

Select whether the collection is a capped collection. If you select to create a capped
collection, specify the maximum size in bytes.

**Step 4: Click Create.**

Upon successful creation, the collection appears underneath the
database in the Data Explorer.

## Drop a Database

To drop a database, including all its collections, through the
Data Explorer:

**Step 1: Drop the database.**

Either select or hover of the database to drop and click on its
trash can icon.

**Step 2: Confirm action.**

Confirm by typing the name of the database, and click Drop.

## Drop a Collection

To drop a collection, including its documents and indexes, through the
Data Explorer:

**Step 1: Drop the collection.**

Either select or hover of the collection to drop and click on its
trash can icon.

**Step 2: Confirm action.**

Confirm by typing the name of the collection, and click Drop.
