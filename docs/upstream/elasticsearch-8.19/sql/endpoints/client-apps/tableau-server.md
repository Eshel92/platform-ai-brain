<!-- Converted from sql/endpoints/client-apps/tableau-server.asciidoc (AsciiDoc). Includes are inlined. -->

### Tableau Server

Use the Elasticsearch JDBC driver and dedicated Elasticsearch Tableau Connector to access Elasticsearch data from Tableau Server.

**Important:** Elastic does not endorse, promote or provide support for this application; for native Elasticsearch integration in this
product, please reach out to its vendor.

#### Prerequisites

* [Tableau Server](https://www.tableau.com/products/server) 2019.4 or later
* {es-sql} JDBC driver
* [Elasticsearch Connector for Tableau](https://www.elastic.co/downloads/tableau-connector)

#### Load data

First, move or download the JDBC driver to the Tableau Server drivers directory:

* Windows: `C:\Program Files\Tableau\Drivers`
* Mac: `/Users/[user]/Library/Tableau/Drivers`

Move the Elasticsearch Connector for Tableau to the Tableau Server connectors
directory. To find the location of this directory, refer to Tableau Server
documentation or use the TSM command line interface.

Restart Tableau Server.

To load data into a workbook, add a **New Data Source** from the **Data** menu or using the icon. In the **Connectors** tab of the **Connect to Data** modal, select **Elasticsearch by Elastic**.

image:images/sql/client-apps/apps_tableau_server_from_connector.png[Select Elasticsearch as the data source]

Enter the information for your Elasticsearch instance, and click **Sign In**.

image:images/sql/client-apps/apps_tableau_server_connect.png[Sign in]

In the main window, select your Elasticsearch instance as the **Database**. Then select a table to load.

image:images/sql/client-apps/apps_tableau_server_prepare.png[Select a table to load]

Finally, generate a report.

image:images/sql/client-apps/apps_tableau_server_report.png[Generate a report]
