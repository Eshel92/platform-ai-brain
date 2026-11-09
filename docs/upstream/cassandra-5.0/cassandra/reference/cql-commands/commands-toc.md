<!-- Converted from modules/cassandra/pages/reference/cql-commands/commands-toc.adoc (AsciiDoc). Includes are inlined. -->

# CQL Commands

This section describes the Cassandra Query Language (CQL) commands supported by the {product} database.

'''
ALTER KEYSPACE ::
Changes keyspace replication strategy and enables or disables commit log.

ALTER MATERIALIZED VIEW ::
Changes the table properties of a materialized view.

ALTER ROLE ::
Changes password and sets superuser or login options.

ALTER TABLE ::
Modifies the columns and properties of a table, or modify

ALTER TYPE ::
Modifies an existing user-defined type (UDT).

ALTER USER (Deprecated) ::
Deprecated. Alter existing user options.

BATCH ::
Applies multiple data modification language (DML) statements with atomicity and/or in isolation.

CREATE AGGREGATE ::
Defines a user-defined aggregate.
CREATE CUSTOM INDEX ::
Creates a storage-attached index.

CREATE FUNCTION ::
Creates custom function to execute user provided code.

CREATE INDEX ::
Defines a new index for a single column of a table.

CREATE KEYSPACE ::

CREATE MATERIALIZED VIEW ::
Optimizes read requests and eliminates the need for multiple write requests by duplicating data from a base table.

CREATE ROLE ::
Creates a cluster wide database object used for access control.

CREATE TABLE ::
Creates a new table.

CREATE TYPE ::
Creates a custom data type in the keyspace that contains one or more fields of related information.

CREATE USER (Deprecated) ::
Deprecated. Creates a new user.

DELETE ::
Removes data from one or more columns or removes the entire row

DROP AGGREGATE ::
Deletes a user-defined aggregate from a keyspace.

DROP FUNCTION ::
Deletes a user-defined function (UDF) from a keyspace.

DROP INDEX ::
Removes an index from a table.

DROP KEYSPACE ::
Removes the keyspace.

DROP MATERIALIZED VIEW ::
Removes the named materialized view.

DROP ROLE ::
Removes a role.

DROP TABLE ::
Removes the table.

DROP TYPE ::
Drop a user-defined type.

DROP USER (Deprecated) ::
Removes a user.

GRANT ::
Allow access to database resources.

INSERT ::
Inserts an entire row or upserts data into existing rows.

LIST PERMISSIONS ::
Lists permissions on resources.

LIST ROLES ::
Lists roles and shows superuser and login status.

LIST USERS (Deprecated) ::
Lists existing internal authentication users and their superuser status.

RESTRICT ::
Denies the permission on a resource, even if the role is directly granted or inherits permissions.

RESTRICT ROWS ::
Configures the column used for row-level access control.

REVOKE ::
Removes privileges on database objects from roles.

SELECT ::
Returns data from a table.

TRUNCATE ::
Removes all data from a table.

UNRESTRICT ::
Removes a restriction from a role. 

UNRESTRICT ROWS ::
Removes the column definition for row-level access control. 

UPDATE ::
Modifies one or more column values to a row in a table.

USE ::
Selects the keyspace for the current client session.
