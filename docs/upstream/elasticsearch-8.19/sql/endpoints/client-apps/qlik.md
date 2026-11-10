<!-- Converted from sql/endpoints/client-apps/qlik.asciidoc (AsciiDoc). Includes are inlined. -->

### Qlik Sense Desktop

You can use the Elasticsearch ODBC driver to access Elasticsearch data from Qlik Sense Desktop.

**Important:** Elastic does not endorse, promote or provide support for this application; for native Elasticsearch integration in this product, please reach out to its vendor.

#### Prerequisites

* [Qlik Sense Desktop](https://www.qlik.com/us/try-or-buy/download-qlik-sense) November 2018 or higher
* {es-sql} ODBC driver
* A preconfigured User or System DSN (see Configuration section on how to configure a DSN).

#### Data loading

To use the {odbc} to load data into Qlik Sense Desktop perform the following steps in sequence.

. Create new app
Once the application is launched, you'll first need to click on the _Create new app_ button:
image:images/sql/odbc/apps_qlik_newapp.png[]
. Name app
...then give it a name,
image:images/sql/odbc/apps_qlik_create.png[]
. Open app
...and then open it:
image:images/sql/odbc/apps_qlik_open.png[]
. Add data to your app
Start configuring the source to load data from in the newly created app:
image:images/sql/odbc/apps_qlik_adddata.png[]
. Load from ODBC
You'll be given a choice of sources to select. Click on the _ODBC_ icon:
image:images/sql/odbc/apps_qlik_odbc.png[]
. Choose DSN
In the _Create new connection (ODBC)_ dialog, click on the DSN name that you have previously configured for your Elasticsearch instance:
image:images/sql/odbc/apps_qlik_dsn.png[]
Provide a username and password in the respective fields, if authentication is enabled on your instance and if these are not already part
of the DSN. Press the _Create_ button.
. Select source table
The application will now connect to the Elasticsearch instance and query the catalog information, presenting you with a list of tables that you can
load data from:
image:images/sql/odbc/apps_qlik_selecttable.png[]
. Visualize the data
Press on the _Add data_ button and customize your data visualization:
image:images/sql/odbc/apps_qlik_visualize.png[]
