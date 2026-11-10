<!-- Converted from sql/endpoints/client-apps/powerbi.asciidoc (AsciiDoc). Includes are inlined. -->

### Microsoft Power BI Desktop

You can use the Elasticsearch ODBC driver to access Elasticsearch data from Microsoft Power BI Desktop.

**Important:** Elastic does not endorse, promote or provide support for this application; for native Elasticsearch integration in this product, please reach out to its vendor.

#### Prerequisites

* [Microsoft Power BI Desktop](https://powerbi.microsoft.com/en-us/desktop/) 2.63 or higher
* {es-sql} ODBC driver
* A preconfigured User or System DSN (see Configuration section on how to configure a DSN).

#### Data loading

First, you'll need to choose ODBC as the source to load data from. Once launched, click on the _Get Data_ button (under _Home_ tab), then
on the _More..._ button at the bottom of the list:

**Get Data / More...**
image:images/sql/odbc/apps_pbi_fromodbc1.png[]

In the new opened window scroll at the bottom of the _All_ list and select the _ODBC_ entry, then click on the _Connect_ button:

**ODBC / Connect**
image:images/sql/odbc/apps_pbi_fromodbc2.png[]

This will replace current window with a new _From ODBC_ one, where you'll have to select a previously configured DSN:

**Choose a DSN**
image:images/sql/odbc/apps_pbi_dsn.png[]

Once connected Power BI will read Elasticsearch's catalog and offer the user a choice of tables (indices) to load data from. Clicking on one of the
tables will load a preview of the data within:

**Pick table to load**
image:images/sql/odbc/apps_pbi_picktable.png[]

Now tick the chosen table and click on the _Load_ button. Power BI will now load and analyze the data, populating a list with the available
columns. These can now be used to build the desired visualisation:

**Visualize the data**
image:images/sql/odbc/apps_pbi_loaded.png[]
