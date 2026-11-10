<!-- Converted from sql/endpoints/client-apps/excel.asciidoc (AsciiDoc). Includes are inlined. -->

### Microsoft Excel

You can use the Elasticsearch ODBC driver to access Elasticsearch data from Microsoft Excel.

**Important:** Elastic does not endorse, promote or provide support for this application; for native Elasticsearch integration in this product, please reach out to its vendor.

#### Prerequisites

* [Microsoft Office](https://products.office.com/en/excel) 2016 or higher
* {es-sql} ODBC driver
* A preconfigured User or System DSN (see Configuration section on how to configure a DSN).

#### Load data into a spreadsheet

First, you'll need to choose ODBC as the source to load data from. To do so, click on the _Data_ tab, then _New Query_ button, in the
drop-down menu expand _From Other Sources_, then choose _From ODBC_:

**ODBC as data source**
image:images/sql/odbc/apps_excel_fromodbc.png[]

This will open a new window with a drop down menu populated with the DSNs that Excel found on the system. Choose a DSN configured to
connect to your Elasticsearch instance and press the _OK_ button:

**Choose a DSN**
image:images/sql/odbc/apps_excel_dsn.png[]

This will lead to a new window, allowing the user to input the connection credentials.

A username might be required by Excel even if the Elasticsearch instance has no security enabled. Providing a bogus username with no password in
this case will not hinder the connectivity. Note however that Excel will cache these credentials (so in case you do have security enabled,
you won't be prompted for the credentials a second time).

Fill in the username and the password and press
_Connect_.

**Provide connection credentials**
image:images/sql/odbc/apps_excel_cred.png[]

Once connected, Excel will read Elasticsearch's catalog and offer the user a choice of tables (indices) to load data from. Clicking on one of the
tables will load a preview of the data within:

**Pick table to load**
image:images/sql/odbc/apps_excel_picktable.png[]

Now click the _Load_ button, which will have Excel load all the data from the table into a spreadsheet:

**Data loaded in spreadsheet**
image:images/sql/odbc/apps_excel_loaded.png[]
