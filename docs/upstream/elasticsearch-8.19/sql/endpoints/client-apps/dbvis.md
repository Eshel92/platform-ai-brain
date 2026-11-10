<!-- Converted from sql/endpoints/client-apps/dbvis.asciidoc (AsciiDoc). Includes are inlined. -->

### DbVisualizer

You can use the Elasticsearch JDBC driver to access Elasticsearch data from DbVisualizer.

**Important:** Elastic does not endorse, promote or provide support for this application.

#### Prerequisites

* [DbVisualizer](https://www.dbvis.com/) 13.0 or higher
* {es-sql} JDBC driver

Note::
Pre 13.0 versions of DbVisualizer can still connect to Elasticsearch by having the JDBC driver set up from the generic *Custom* template.

#### Setup the Elasticsearch JDBC driver

Setup the Elasticsearch JDBC driver through *Tools* > *Driver Manager*:

image:images/sql/client-apps/dbvis-1-driver-manager.png[]

Select *Elasticsearch* driver template from the left sidebar to create a new user driver:

image:images/sql/client-apps/dbvis-2-driver-manager-elasticsearch.png[]

Download the driver locally:

image:images/sql/client-apps/dbvis-3-driver-manager-download.png[]

and check its availability status:

image:images/sql/client-apps/dbvis-4-driver-manager-ready.png[]

#### Create a new connection

Once the Elasticsearch driver is in place, create a new connection:

image:images/sql/client-apps/dbvis-5-new-conn.png[]

by double-clicking the Elasticsearch entry in the list of available drivers:

image:images/sql/client-apps/dbvis-6-new-conn-elasticsearch.png[]

Enter the connection details, then press *Connect* and the driver version (as that of the cluster) should show up under *Connection Message*.

image:images/sql/client-apps/dbvis-7-new-conn-connect.png[]

#### Execute SQL queries

The setup is done. DbVisualizer can be used to run queries against Elasticsearch and explore its content:

image:images/sql/client-apps/dbvis-8-data.png[]
