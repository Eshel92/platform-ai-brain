<!-- Converted from sql/endpoints/client-apps/ps1.asciidoc (AsciiDoc). Includes are inlined. -->

### Microsoft PowerShell

You can use the Elasticsearch ODBC driver to access Elasticsearch data from Microsoft PowerShell.

**Important:** Elastic does not endorse, promote or provide support for this application; for native Elasticsearch integration in this product, please reach out to its vendor.

#### Prerequisites

* [Microsoft PowerShell](https://docs.microsoft.com/en-us/powershell/)
* {es-sql} ODBC driver
* A preconfigured User or System DSN (see Configuration section on how to configure a DSN).

#### Writing a script

While putting the following instructions into a script file is not an absolute requirement, doing so will make it easier to extend and
reuse. The following instructions exemplify how to execute a simple SELECT query from an existing index in your Elasticsearch instance, using a DSN
configured in advance. Open a new file, `select.ps1`, and place the following instructions in it:

```
$connectstring = "DSN=Local Elasticsearch;"
$sql = "SELECT * FROM library"

$conn = New-Object System.Data.Odbc.OdbcConnection($connectstring)
$conn.open()
$cmd = New-Object system.Data.Odbc.OdbcCommand($sql,$conn)
$da = New-Object system.Data.Odbc.OdbcDataAdapter($cmd)
$dt = New-Object system.Data.datatable
$null = $da.fill($dt)
$conn.close()
$dt
```

Now open a PowerShell shell and simply execute the script:

**Run SQL in PowerShell**
image:images/sql/odbc/apps_ps_exed.png[]
