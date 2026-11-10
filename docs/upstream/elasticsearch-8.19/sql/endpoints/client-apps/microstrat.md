<!-- Converted from sql/endpoints/client-apps/microstrat.asciidoc (AsciiDoc). Includes are inlined. -->

### MicroStrategy Desktop

You can use the Elasticsearch ODBC driver to access Elasticsearch data from MicroStrategy Desktop.

**Important:** Elastic does not endorse, promote or provide support for this application; for native Elasticsearch integration in this product, please reach out to its vendor.

#### Prerequisites

* [MicroStrategy Desktop](https://www.microstrategy.com/us/get-started/desktop) 11 or higher
* {es-sql} ODBC driver
* A preconfigured User or System DSN (see Configuration section on how to configure a DSN).

#### Data loading

To use the {odbc} to load data into MicroStrategy Desktop perform the following steps in sequence.

. Create a New Dossier
Once the application is launched, you'll first need to create a _New Dossier_:
image:images/sql/odbc/apps_microstrat_newdossier.png[]
. New Data
To import into the _New Dossier_ just opened, press on the _New Data_ button in the _DATASETS_ column:
image:images/sql/odbc/apps_microstrat_newdata.png[]
. Access data from Tables
This opens a new window that allows to choose the source to load data from. Click on the _Databases_ icon:
image:images/sql/odbc/apps_microstrat_databases.png[]
. New Data Source
In the newly opened _Import from Table - Select_ window, click on the *+* button to the right of _DATA SOURCES_ item:
image:images/sql/odbc/apps_microstrat_newds.png[]
. Data Source
In the _Data Source_ window, tick the radio button for _DSN Data Sources_. In the _DSN_ drop-down box, choose the name of the DSN that you
have previously configured. For the _Version_, chose _Generic DBMS_.
Input a user name and password in the provided fields.
Note that the application requires them irrespective of the fact that they might already be part of the previously configured DSN and the
new input will take precedence over those.
Finally, give a name to the application-specific data source you're just configuring:
image:images/sql/odbc/apps_microstrat_dsn.png[]
. Select Import Options
Choosing an import methodology follows. You can pick any of the options; we'll exemplify the _Select Tables_ option:
image:images/sql/odbc/apps_microstrat_tables.png[]
. Import from Table - Select
The data source you've named two steps before is now listed in the _DATA SOURCES_ column. Clicking on its name triggers the
application to query the Elasticsearch instance configured in the DSN and list the tables available within:
image:images/sql/odbc/apps_microstrat_loadtable.png[]
. Data Access Mode
Choose a table to load data from and press the _Finish_ button. When doing so, the application offers to choose a loading methodology.
You can choose whichever, we'll exemplify the _Connect Live_ way:
image:images/sql/odbc/apps_microstrat_live.png[]
. Visualize the data
From the _DATASETS_ column you can choose what table columns (or index fields) to visualize:
image:images/sql/odbc/apps_microstrat_visualize.png[]
