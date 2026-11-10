<!-- Converted from sql/endpoints/client-apps/tableau-desktop.asciidoc (AsciiDoc). Includes are inlined. -->

### Tableau Desktop

Use the Elasticsearch JDBC driver and dedicated Elasticsearch Tableau Connector to access Elasticsearch data from Tableau Desktop.

**Important:** Elastic does not endorse, promote or provide support for this application; for native Elasticsearch integration in this
product, please reach out to its vendor.

#### Prerequisites

* [Tableau Desktop](https://www.tableau.com/products/desktop) 2019.4 or later
* {es-sql} JDBC driver
* [Elasticsearch Connector for Tableau](https://www.elastic.co/downloads/tableau-connector)

#### Load data

First, move or download the JDBC driver to the Tableau Desktop drivers directory:

* Windows: `C:\Program Files\Tableau\Drivers`
* Mac: `/Users/[user]/Library/Tableau/Drivers`

Move the Elasticsearch Connector for Tableau to the Tableau Desktop connectors directory:

* Windows: `C:\Users\[Windows User]\Documents\My Tableau Repository\Connectors`
* Mac: `/Users/[user]/Documents/My Tableau Repository/Connectors`

Launch Tableau Desktop. In the menu, click **More...** and select **Elasticsearch by Elastic** as the data source.

image:images/sql/client-apps/apps_tableau_desktop_from_connector.png[Select Elasticsearch by Elastic as the data source]

In the **New connection** modal, enter the information for your Elasticsearch instance, and click **Sign In**.

image:images/sql/client-apps/apps_tableau_desktop_connect.png[Sign in]

In the main window, select your Elasticsearch instance as the **Database**. Then select a table to load.

image:images/sql/client-apps/apps_tableau_desktop_prepare.png[Select a table to load]

Finally, generate a report.

image:images/sql/client-apps/apps_tableau_desktop_report.png[Generate a report]
