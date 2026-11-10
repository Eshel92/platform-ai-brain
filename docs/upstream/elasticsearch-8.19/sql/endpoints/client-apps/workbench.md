<!-- Converted from sql/endpoints/client-apps/workbench.asciidoc (AsciiDoc). Includes are inlined. -->

### SQL Workbench/J

You can use the Elasticsearch JDBC driver to access Elasticsearch data from SQL Workbench/J.

**Important:** Elastic does not endorse, promote or provide support for this application; for native Elasticsearch integration in this product, please reach out to its vendor.

#### Prerequisites

* [SQL Workbench/J](https://www.sql-workbench.eu/) build 125 or higher
* {es-sql} JDBC driver

#### Add Elasticsearch JDBC driver

Add the Elasticsearch JDBC driver to SQL Workbench/J through *Manage Drivers* either from the main windows in the *File* menu or from the *Connect* window:

image:images/sql/client-apps/workbench-1-manage-drivers.png[]

Select *Elasticsearch* profile from the left-hand side (if it is missing check the SQL Workbench/J version or add a new entry to the list through the blank page button in the upper left corner):

image:images/sql/client-apps/workbench-2-select-driver.png[]

Add the JDBC jar (if the driver name hasn't been picked up already,  click on the magnifier button):

image:images/sql/client-apps/workbench-3-add-jar.png[]

#### Create a new connection profile

With the driver configured, create a new connection profile through *File* > *Connect Window* (or Alt+C shortcut):

image:images/sql/client-apps/workbench-4-connection.png[]

Select the previously configured driver and set the URL of your cluster using the JDBC syntax.
Verify the connection through the *Test* button - a confirmation window should appear that everything is properly configured.

The setup is complete.

#### Execute SQL queries

SQL Workbench/J is ready to talk to Elasticsearch through SQL: click on the profile created to execute statements or explore the data:

image:images/sql/client-apps/workbench-5-data.png[]
