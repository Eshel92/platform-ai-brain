<!-- Converted from core/timeseries/timeseries-quick-start.txt (reStructuredText). Includes are inlined. -->

# Time Series Quick Start

Configure, create, and query a time series collection with MongoDB
Atlas or a self-managed deployment.

*Time required: 30 minutes*

**Step 1: Set up your Atlas cluster.**

a. [Create a free Atlas account or sign in to an existing account](https://account.mongodb.com/account/register).

#. If you don't yet have an Atlas cluster, [create a free M0 cluster](https://cloud.mongodb.com/go?l=https%3A%2F%2Fcloud.mongodb.com%2Fv2%2F%3Cproject%3E%23clusters%2Fedit%3Ffrom%3DctaClusterHeader).
   To learn more about creating an Atlas cluster, see Create a Cluster.

   **Note:**

   If you are working with an existing cluster, you must have
   `Project Data Access Admin` or higher access to your
   Atlas project.

   If you create a new cluster, you have the necessary permissions by default.

   You can create only one `M0` Free cluster per project.

#. In the left sidebar, click [Overview](https://cloud.mongodb.com/go?l=https%3A%2F%2Fcloud.mongodb.com%2Fv2%2F%3Cproject%3E%23%2Foverview).
   Choose your cluster and click Connect.

**Step 2: Get .NET/C# Driver connection details.**

a. Under Connect to your application, click Driver.
   Select C#.

   If you haven't already, follow the steps provided to download and
   install the `.NET/C# Driver`.

#. Copy your connection string and click Done.

**Step 3: Copy the template app and connect to your deployment.**

a. Paste the following code into a new `.cs` file.

#. Replace `"<connection-string>"` with your copied connection string.

As you work with time series code examples, add them between the
`// start example code here` and `// end example code here` comments.

```csharp
using MongoDB.Driver;

// Replace the placeholder with your connection string.
var uri = "<connection string>";

try
{
    var client = new MongoClient(uri);
    // start example code here

    // end example code here
}
catch (MongoException me)
{
    Console.Error.WriteLine(me.Message);
}
```

**Step 4: Create a data model.**

**Note:**

This exercise uses stock ticker sample data. The `date` field stores time data, and
the `ticker` field identifies the individual stock.

Create a C# class to model the data in the `stocks` collection:

```csharp
public class Stocks
{
    [BsonId]
    public ObjectId Id { get; set; }

    [BsonElement("ticker")]
    public string Ticker { get; set; } = "";

    [BsonElement("date")]
    public DateTime Date { get; set; }

    [BsonElement("close")]
    public double Close { get; set; }

    [BsonElement("volume")]
    public double Volume { get; set; }
}
```

**Step 5: Access the database.**

```csharp
var db = client.GetDatabase("timeseriesdb");
```

This creates a reference to an empty "timeseries" database.

**Step 6: Create an empty time series collection.**

a. Set the `timeField`, `metaField`, and `granularity`:

   ```csharp
   var timeSeriesOptions = new TimeSeriesOptions(
       timeField: "date",
       metaField: "ticker",
       TimeSeriesGranularity.Seconds
   );

   var options = new CreateCollectionOptions
   {
       TimeSeriesOptions = timeSeriesOptions
   };
   ```

#. Create the collection using the `db.createCollection()` method:

   ```csharp
   db.CreateCollection("stocks", options);
   ```

   This creates an empty time series collection named `stocks`.

**Step 7: Add sample documents.**

Use the `db.collection.insertMany()` method to add the
following sample documents to the collection:

```csharp
var stocks = db.GetCollection<Stocks>("stocks");

stocks.InsertMany(new List<Stocks>
{
    new Stocks()
    {
        Ticker = "MDB",
        Date = DateTime.Parse("2021-12-18T15:59:00Z"),
        Close = 252.47,
        Volume = 55046.0
    },
    new Stocks()
    {
        Ticker = "MDB",
        Date = DateTime.Parse("2021-12-18T15:58:00Z"),
        Close = 252.94,
        Volume = 44042.0
    },
    new Stocks()
    {
        Ticker = "MDB",
        Date = DateTime.Parse("2021-12-18T15:57:00Z"),
        Close = 253.62,
        Volume = 40182.0
    },
    new Stocks()
    {
        Ticker = "MDB",
        Date = DateTime.Parse("2021-12-18T15:56:00Z"),
        Close = 253.63,
        Volume = 27890.0
    },
    new Stocks()
    {
        Ticker = "MDB",
        Date = DateTime.Parse("2021-12-18T15:55:00Z"),
        Close = 254.03,
        Volume = 40270.0
    }
});
```

If you are running MongoDB on Atlas, you can click
Browse collections to view the sample data.

**Step 8: Query the data.**

You query a time series collection like any other MongoDB collection. For
more information, see About Querying Time Series Data.

Common queries for time series data are querying the `metaField`
to get data for a single time series, or using a range query on the
`timeField` to get data for a given time span.

To query the `metaField` for a single time series:

```csharp
```

Output:

```text
```

To query the `timeField` for a time span:

```csharp
```

Output:

```text
```

**Step 1: Install local deployment dependencies.**

For detailed instructions, see `Prerequisites`.

a. Install the `Atlas CLI`.

   If you use [Homebrew](https://brew.sh/#install), you can
   run the following command in your terminal:

   ```
   brew install mongodb-atlas
   ```

   For installation instructions on other operating systems,
   see `Install the Atlas CLI`

#. Install [Docker](https://www.docker.com/).

   Docker requires a network connection for pulling and caching
   MongoDB images.

   - For MacOS or Windows, install [Docker Desktop v4.31+](https://docs.docker.com/desktop/release-notes/#4310).
   - For Linux, install [Docker Engine v27.0+](https://docs.docker.com/engine/release-notes/27/).
   - For RHEL, you can also use [Podman v5.0+](https://podman.io).

**Step 2: Set up your local Atlas deployment.**

a. If you don't have an existing Atlas account, run `atlas setup` in your terminal
   or [create a new account](https://account.mongodb.com/account/register).

#. Run `atlas deployments setup` and follow the prompts to create a
   local deployment. When prompted to connect to the deployment,
   select `skip`.

   For detailed instructions, see `Create a Local Atlas Deployment`.

**Step 3: Install the .NET/C# driver.**

Follow the directions on the [.NET/C# Driver Get Started](https://www.mongodb.com/docs/drivers/csharp/current/get-started/)
page to create a new project and install driver dependencies.

**Step 4: Copy the template app and connect to your deployment.**

a. Paste the following code into a new `.cs` file.

#. Replace `"<connection-string>"` with your copied connection string.

As you work with time series code examples, add them between the
`// start example code here` and `// end example code here` comments.

```csharp
using MongoDB.Driver;

// Replace the placeholder with your connection string.
var uri = "<connection string>";

try
{
    var client = new MongoClient(uri);
    // start example code here

    // end example code here
}
catch (MongoException me)
{
    Console.Error.WriteLine(me.Message);
}
```

**Step 5: Create a data model.**

**Note:**

This exercise uses stock ticker sample data. The `date` field stores time data, and
the `ticker` field identifies the individual stock.

Create a C# class to model the data in the `stocks` collection:

```csharp
public class Stocks
{
    [BsonId]
    public ObjectId Id { get; set; }

    [BsonElement("ticker")]
    public string Ticker { get; set; } = "";

    [BsonElement("date")]
    public DateTime Date { get; set; }

    [BsonElement("close")]
    public double Close { get; set; }

    [BsonElement("volume")]
    public double Volume { get; set; }
}
```

**Step 6: Access the database.**

```csharp
var db = client.GetDatabase("timeseriesdb");
```

This creates a reference to an empty "timeseries" database.

**Step 7: Create an empty time series collection.**

a. Set the `timeField`, `metaField`, and `granularity`:

   ```csharp
   var timeSeriesOptions = new TimeSeriesOptions(
       timeField: "date",
       metaField: "ticker",
       TimeSeriesGranularity.Seconds
   );

   var options = new CreateCollectionOptions
   {
       TimeSeriesOptions = timeSeriesOptions
   };
   ```

#. Create the collection using the `db.createCollection()` method:

   ```csharp
   db.CreateCollection("stocks", options);
   ```

   This creates an empty time series collection named `stocks`.

**Step 8: Add sample documents.**

Use the `db.collection.insertMany()` method to add the
following sample documents to the collection:

```csharp
var stocks = db.GetCollection<Stocks>("stocks");

stocks.InsertMany(new List<Stocks>
{
    new Stocks()
    {
        Ticker = "MDB",
        Date = DateTime.Parse("2021-12-18T15:59:00Z"),
        Close = 252.47,
        Volume = 55046.0
    },
    new Stocks()
    {
        Ticker = "MDB",
        Date = DateTime.Parse("2021-12-18T15:58:00Z"),
        Close = 252.94,
        Volume = 44042.0
    },
    new Stocks()
    {
        Ticker = "MDB",
        Date = DateTime.Parse("2021-12-18T15:57:00Z"),
        Close = 253.62,
        Volume = 40182.0
    },
    new Stocks()
    {
        Ticker = "MDB",
        Date = DateTime.Parse("2021-12-18T15:56:00Z"),
        Close = 253.63,
        Volume = 27890.0
    },
    new Stocks()
    {
        Ticker = "MDB",
        Date = DateTime.Parse("2021-12-18T15:55:00Z"),
        Close = 254.03,
        Volume = 40270.0
    }
});
```

If you are running MongoDB on Atlas, you can click
Browse collections to view the sample data.

**Step 9: Query the data.**

You query a time series collection like any other MongoDB collection. For
more information, see About Querying Time Series Data.

Common queries for time series data are querying the `metaField`
to get data for a single time series, or using a range query on the
`timeField` to get data for a given time span.

To query the `metaField` for a single time series:

```csharp
```

Output:

```text
```

To query the `timeField` for a time span:

```csharp
```

Output:

```text
```

**Step 1: Install MongoDB and local deployment dependencies.**

If you're running a self-managed deployment, follow the
installation instructions for your
MongoDB version, edition, and platform.

**Step 2: Install the .NET/C# driver.**

Follow the directions on the [.NET/C# Driver Get Started](https://www.mongodb.com/docs/drivers/csharp/current/get-started/)
page to create a new project and install driver dependencies.

**Step 3: Copy the template app and connect to your deployment.**

a. Paste the following code into a new `.cs` file.

#. Replace `"<connection-string>"` with your copied connection string.

As you work with time series code examples, add them between the
`// start example code here` and `// end example code here` comments.

```csharp
using MongoDB.Driver;

// Replace the placeholder with your connection string.
var uri = "<connection string>";

try
{
    var client = new MongoClient(uri);
    // start example code here

    // end example code here
}
catch (MongoException me)
{
    Console.Error.WriteLine(me.Message);
}
```

**Step 4: Create a data model.**

**Note:**

This exercise uses stock ticker sample data. The `date` field stores time data, and
the `ticker` field identifies the individual stock.

Create a C# class to model the data in the `stocks` collection:

```csharp
public class Stocks
{
    [BsonId]
    public ObjectId Id { get; set; }

    [BsonElement("ticker")]
    public string Ticker { get; set; } = "";

    [BsonElement("date")]
    public DateTime Date { get; set; }

    [BsonElement("close")]
    public double Close { get; set; }

    [BsonElement("volume")]
    public double Volume { get; set; }
}
```

**Step 5: Access the database.**

```csharp
var db = client.GetDatabase("timeseriesdb");
```

This creates a reference to an empty "timeseries" database.

**Step 6: Create an empty time series collection.**

a. Set the `timeField`, `metaField`, and `granularity`:

   ```csharp
   var timeSeriesOptions = new TimeSeriesOptions(
       timeField: "date",
       metaField: "ticker",
       TimeSeriesGranularity.Seconds
   );

   var options = new CreateCollectionOptions
   {
       TimeSeriesOptions = timeSeriesOptions
   };
   ```

#. Create the collection using the `db.createCollection()` method:

   ```csharp
   db.CreateCollection("stocks", options);
   ```

   This creates an empty time series collection named `stocks`.

**Step 7: Add sample documents.**

Use the `db.collection.insertMany()` method to add the
following sample documents to the collection:

```csharp
var stocks = db.GetCollection<Stocks>("stocks");

stocks.InsertMany(new List<Stocks>
{
    new Stocks()
    {
        Ticker = "MDB",
        Date = DateTime.Parse("2021-12-18T15:59:00Z"),
        Close = 252.47,
        Volume = 55046.0
    },
    new Stocks()
    {
        Ticker = "MDB",
        Date = DateTime.Parse("2021-12-18T15:58:00Z"),
        Close = 252.94,
        Volume = 44042.0
    },
    new Stocks()
    {
        Ticker = "MDB",
        Date = DateTime.Parse("2021-12-18T15:57:00Z"),
        Close = 253.62,
        Volume = 40182.0
    },
    new Stocks()
    {
        Ticker = "MDB",
        Date = DateTime.Parse("2021-12-18T15:56:00Z"),
        Close = 253.63,
        Volume = 27890.0
    },
    new Stocks()
    {
        Ticker = "MDB",
        Date = DateTime.Parse("2021-12-18T15:55:00Z"),
        Close = 254.03,
        Volume = 40270.0
    }
});
```

If you are running MongoDB on Atlas, you can click
Browse collections to view the sample data.

**Step 8: Query the data.**

You query a time series collection like any other MongoDB collection. For
more information, see About Querying Time Series Data.

Common queries for time series data are querying the `metaField`
to get data for a single time series, or using a range query on the
`timeField` to get data for a given time span.

To query the `metaField` for a single time series:

```csharp
```

Output:

```text
```

To query the `timeField` for a time span:

```csharp
```

Output:

```text
```

**Step 1: Set up your Atlas cluster.**

a. [Create a free Atlas account or sign in to an existing account](https://account.mongodb.com/account/register).

#. If you don't yet have an Atlas cluster, [create a free M0 cluster](https://cloud.mongodb.com/go?l=https%3A%2F%2Fcloud.mongodb.com%2Fv2%2F%3Cproject%3E%23clusters%2Fedit%3Ffrom%3DctaClusterHeader).
   To learn more about creating an Atlas cluster, see Create a Cluster.

   **Note:**

   If you are working with an existing cluster, you must have
   `Project Data Access Admin` or higher access to your
   Atlas project.

   If you create a new cluster, you have the necessary permissions by default.

   You can create only one `M0` Free cluster per project.

#. In the left sidebar, click [Overview](https://cloud.mongodb.com/go?l=https%3A%2F%2Fcloud.mongodb.com%2Fv2%2F%3Cproject%3E%23%2Foverview).
   Choose your cluster and click Connect.

**Step 2: Get Java Sync Driver connection details.**

a. Under Connect to your application, click Driver.
   Select Java (Sync).

   If you haven't already, follow the steps provided to download and
   install the `Java Sync Driver`.

#. Copy your connection string and click Done.

**Step 3: Copy the template app and connect to your deployment.**

a. Paste the following code into a new `.java` file.

#. Replace `"<connection-string>"` with your copied connection string.

As you work with time series code examples, add them between the
`// start example code here` and `// end example code here` comments.

```java
package org.example;

// Modify imports for each tutorial as needed.
import com.mongodb.MongoException;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;

public class SampleApp {
    public static void main(String[] args) {
        // Replace the placeholder with your connection string.
        String uri = "<connection string>";

        try (MongoClient mongoClient = MongoClients.create(uri)) {
            // start example code here

            // end example code here
        } catch (MongoException me) {
            System.err.println(me.getMessage());
        }
    }
}
```

**Step 4: Add the required imports.**

Add these imports to the top of your sample app file:

```java
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import com.mongodb.client.FindIterable;
import com.mongodb.client.model.CreateCollectionOptions;
import com.mongodb.client.model.TimeSeriesGranularity;
import com.mongodb.client.model.TimeSeriesOptions;
import org.bson.Document;

import java.time.Instant;
import java.util.Arrays;
import java.util.Date;
```

**Step 5: Access the database.**

```java
MongoDatabase db = mongoClient.getDatabase("timeseries_db");
```

This creates a reference to an empty "timeseries" database.

**Step 6: Create an empty time series collection.**

**Note:**

This exercise uses stock ticker sample data. The `date` field stores time data, and
the `ticker` field identifies the individual stock.

a. Set the `timeField`, `metaField`, and `granularity`:

   ```java
   // Specify the time series options to configure the collection
   TimeSeriesOptions timeSeriesOptions = new TimeSeriesOptions("date")
           .metaField("ticker")
           .granularity(TimeSeriesGranularity.SECONDS);

   CreateCollectionOptions options = new CreateCollectionOptions()
           .timeSeriesOptions(timeSeriesOptions);
   ```

#. Create the collection using the `db.createCollection()` method:

   ```java
   db.createCollection("stocks", options);
   ```

   This creates an empty time series collection named `stocks`.

**Step 7: Add sample documents.**

Use the `db.collection.insertMany()` method to add the
following sample documents to the collection:

```java
MongoCollection<Document> stocks = db.getCollection("stocks");

stocks.insertMany(
        Arrays.asList(
                new Document("ticker", "MDB")
                        .append("date", Date.from(Instant.parse("2021-12-18T15:59:00Z")))
                        .append("close", 252.47)
                        .append("volume", 55046.0),

                new Document("ticker", "MDB")
                        .append("date", Date.from(Instant.parse("2021-12-18T15:58:00Z")))
                        .append("close", 252.93)
                        .append("volume", 44042.0),

                new Document("ticker", "MDB")
                        .append("date", Date.from(Instant.parse("2021-12-18T15:57:00Z")))
                        .append("close", 253.61)
                        .append("volume", 40182.0),

                new Document("ticker", "MDB")
                        .append("date", Date.from(Instant.parse("2021-12-18T15:56:00Z")))
                        .append("close", 253.63)
                        .append("volume", 27890.0),

                new Document("ticker", "MDB")
                        .append("date", Date.from(Instant.parse("2021-12-18T15:55:00Z")))
                        .append("close", 254.03)
                        .append("volume", 40270.0)
        )
);
```

If you are running MongoDB on Atlas, you can click
Browse collections to view the sample data.

**Step 8: Query the data.**

You query a time series collection like any other MongoDB collection. For
more information, see About Querying Time Series Data.

Common queries for time series data are querying the `metaField`
to get data for a single time series, or using a range query on the
`timeField` to get data for a given time span.

To query the `metaField` for a single time series:

```java
```

Output:

```text
```

To query the `timeField` for a time span:

```java
```

Output:

```text
```

**Step 1: Install local deployment dependencies.**

For detailed instructions, see `Prerequisites`.

a. Install the `Atlas CLI`.

   If you use [Homebrew](https://brew.sh/#install), you can
   run the following command in your terminal:

   ```
   brew install mongodb-atlas
   ```

   For installation instructions on other operating systems,
   see `Install the Atlas CLI`

#. Install [Docker](https://www.docker.com/).

   Docker requires a network connection for pulling and caching
   MongoDB images.

   - For MacOS or Windows, install [Docker Desktop v4.31+](https://docs.docker.com/desktop/release-notes/#4310).
   - For Linux, install [Docker Engine v27.0+](https://docs.docker.com/engine/release-notes/27/).
   - For RHEL, you can also use [Podman v5.0+](https://podman.io).

**Step 2: Set up your local Atlas deployment.**

a. If you don't have an existing Atlas account, run `atlas setup` in your terminal
   or [create a new account](https://account.mongodb.com/account/register).

#. Run `atlas deployments setup` and follow the prompts to create a
   local deployment. When prompted to connect to the deployment,
   select `skip`.

   For detailed instructions, see `Create a Local Atlas Deployment`.

**Step 3: Install the Java Sync Driver.**

Follow the directions on the [Java Sync Driver Get Started](https://www.mongodb.com/docs/drivers/java/sync/current/get-started/)
page to create a new project and install driver dependencies.

**Step 4: Copy the template app and connect to your deployment.**

a. Paste the following code into a new `.java` file.

#. Replace `"<connection-string>"` with your copied connection string.

As you work with time series code examples, add them between the
`// start example code here` and `// end example code here` comments.

```java
package org.example;

// Modify imports for each tutorial as needed.
import com.mongodb.MongoException;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;

public class SampleApp {
    public static void main(String[] args) {
        // Replace the placeholder with your connection string.
        String uri = "<connection string>";

        try (MongoClient mongoClient = MongoClients.create(uri)) {
            // start example code here

            // end example code here
        } catch (MongoException me) {
            System.err.println(me.getMessage());
        }
    }
}
```

**Step 5: Add the required imports.**

Add these imports to the top of your sample app file:

```java
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import com.mongodb.client.FindIterable;
import com.mongodb.client.model.CreateCollectionOptions;
import com.mongodb.client.model.TimeSeriesGranularity;
import com.mongodb.client.model.TimeSeriesOptions;
import org.bson.Document;

import java.time.Instant;
import java.util.Arrays;
import java.util.Date;
```

**Step 6: Access the database.**

```java
MongoDatabase db = mongoClient.getDatabase("timeseries_db");
```

This creates a reference to an empty "timeseries" database.

**Step 7: Create an empty time series collection.**

**Note:**

This exercise uses stock ticker sample data. The `date` field stores time data, and
the `ticker` field identifies the individual stock.

a. Set the `timeField`, `metaField`, and `granularity`:

   ```java
   // Specify the time series options to configure the collection
   TimeSeriesOptions timeSeriesOptions = new TimeSeriesOptions("date")
           .metaField("ticker")
           .granularity(TimeSeriesGranularity.SECONDS);

   CreateCollectionOptions options = new CreateCollectionOptions()
           .timeSeriesOptions(timeSeriesOptions);
   ```

#. Create the collection using the `db.createCollection()` method:

   ```java
   db.createCollection("stocks", options);
   ```

   This creates an empty time series collection named `stocks`.

**Step 8: Add sample documents.**

Use the `db.collection.insertMany()` method to add the
following sample documents to the collection:

```java
MongoCollection<Document> stocks = db.getCollection("stocks");

stocks.insertMany(
        Arrays.asList(
                new Document("ticker", "MDB")
                        .append("date", Date.from(Instant.parse("2021-12-18T15:59:00Z")))
                        .append("close", 252.47)
                        .append("volume", 55046.0),

                new Document("ticker", "MDB")
                        .append("date", Date.from(Instant.parse("2021-12-18T15:58:00Z")))
                        .append("close", 252.93)
                        .append("volume", 44042.0),

                new Document("ticker", "MDB")
                        .append("date", Date.from(Instant.parse("2021-12-18T15:57:00Z")))
                        .append("close", 253.61)
                        .append("volume", 40182.0),

                new Document("ticker", "MDB")
                        .append("date", Date.from(Instant.parse("2021-12-18T15:56:00Z")))
                        .append("close", 253.63)
                        .append("volume", 27890.0),

                new Document("ticker", "MDB")
                        .append("date", Date.from(Instant.parse("2021-12-18T15:55:00Z")))
                        .append("close", 254.03)
                        .append("volume", 40270.0)
        )
);
```

If you are running MongoDB on Atlas, you can click
Browse collections to view the sample data.

**Step 9: Query the data.**

You query a time series collection like any other MongoDB collection. For
more information, see About Querying Time Series Data.

Common queries for time series data are querying the `metaField`
to get data for a single time series, or using a range query on the
`timeField` to get data for a given time span.

To query the `metaField` for a single time series:

```java
```

Output:

```text
```

To query the `timeField` for a time span:

```java
```

Output:

```text
```

**Step 1: Install MongoDB and local deployment dependencies.**

If you're running a self-managed deployment, follow the
installation instructions for your
MongoDB version, edition, and platform.

**Step 2: Install the Java Sync Driver.**

Follow the directions on the [Java Sync Driver Get Started](https://www.mongodb.com/docs/drivers/java/sync/current/get-started/)
page to create a new project and install driver dependencies.

**Step 3: Copy the template app and connect to your deployment.**

a. Paste the following code into a new `.java` file.

#. Replace `"<connection-string>"` with your copied connection string.

As you work with time series code examples, add them between the
`// start example code here` and `// end example code here` comments.

```java
package org.example;

// Modify imports for each tutorial as needed.
import com.mongodb.MongoException;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;

public class SampleApp {
    public static void main(String[] args) {
        // Replace the placeholder with your connection string.
        String uri = "<connection string>";

        try (MongoClient mongoClient = MongoClients.create(uri)) {
            // start example code here

            // end example code here
        } catch (MongoException me) {
            System.err.println(me.getMessage());
        }
    }
}
```

**Step 4: Add the required imports.**

Add these imports to the top of your sample app file:

```java
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import com.mongodb.client.FindIterable;
import com.mongodb.client.model.CreateCollectionOptions;
import com.mongodb.client.model.TimeSeriesGranularity;
import com.mongodb.client.model.TimeSeriesOptions;
import org.bson.Document;

import java.time.Instant;
import java.util.Arrays;
import java.util.Date;
```

**Step 5: Access the database.**

```java
MongoDatabase db = mongoClient.getDatabase("timeseries_db");
```

This creates a reference to an empty "timeseries" database.

**Step 6: Create an empty time series collection.**

**Note:**

This exercise uses stock ticker sample data. The `date` field stores time data, and
the `ticker` field identifies the individual stock.

a. Set the `timeField`, `metaField`, and `granularity`:

   ```java
   // Specify the time series options to configure the collection
   TimeSeriesOptions timeSeriesOptions = new TimeSeriesOptions("date")
           .metaField("ticker")
           .granularity(TimeSeriesGranularity.SECONDS);

   CreateCollectionOptions options = new CreateCollectionOptions()
           .timeSeriesOptions(timeSeriesOptions);
   ```

#. Create the collection using the `db.createCollection()` method:

   ```java
   db.createCollection("stocks", options);
   ```

   This creates an empty time series collection named `stocks`.

**Step 7: Add sample documents.**

Use the `db.collection.insertMany()` method to add the
following sample documents to the collection:

```java
MongoCollection<Document> stocks = db.getCollection("stocks");

stocks.insertMany(
        Arrays.asList(
                new Document("ticker", "MDB")
                        .append("date", Date.from(Instant.parse("2021-12-18T15:59:00Z")))
                        .append("close", 252.47)
                        .append("volume", 55046.0),

                new Document("ticker", "MDB")
                        .append("date", Date.from(Instant.parse("2021-12-18T15:58:00Z")))
                        .append("close", 252.93)
                        .append("volume", 44042.0),

                new Document("ticker", "MDB")
                        .append("date", Date.from(Instant.parse("2021-12-18T15:57:00Z")))
                        .append("close", 253.61)
                        .append("volume", 40182.0),

                new Document("ticker", "MDB")
                        .append("date", Date.from(Instant.parse("2021-12-18T15:56:00Z")))
                        .append("close", 253.63)
                        .append("volume", 27890.0),

                new Document("ticker", "MDB")
                        .append("date", Date.from(Instant.parse("2021-12-18T15:55:00Z")))
                        .append("close", 254.03)
                        .append("volume", 40270.0)
        )
);
```

If you are running MongoDB on Atlas, you can click
Browse collections to view the sample data.

**Step 8: Query the data.**

You query a time series collection like any other MongoDB collection. For
more information, see About Querying Time Series Data.

Common queries for time series data are querying the `metaField`
to get data for a single time series, or using a range query on the
`timeField` to get data for a given time span.

To query the `metaField` for a single time series:

```java
```

Output:

```text
```

To query the `timeField` for a time span:

```java
```

Output:

```text
```

**Step 1: Set up your Atlas cluster.**

a. [Create a free Atlas account or sign in to an existing account](https://account.mongodb.com/account/register).

#. If you don't yet have an Atlas cluster, [create a free M0 cluster](https://cloud.mongodb.com/go?l=https%3A%2F%2Fcloud.mongodb.com%2Fv2%2F%3Cproject%3E%23clusters%2Fedit%3Ffrom%3DctaClusterHeader).
   To learn more about creating an Atlas cluster, see Create a Cluster.

   **Note:**

   If you are working with an existing cluster, you must have
   `Project Data Access Admin` or higher access to your
   Atlas project.

   If you create a new cluster, you have the necessary permissions by default.

   You can create only one `M0` Free cluster per project.

#. In the left sidebar, click [Overview](https://cloud.mongodb.com/go?l=https%3A%2F%2Fcloud.mongodb.com%2Fv2%2F%3Cproject%3E%23%2Foverview).
   Choose your cluster and click Connect.

**Step 2: Get mongosh connection details.**

a. Under Access your data through tools, click Shell.

   If you haven't already, follow the steps provided to download and
   install `mongosh`.

#. Copy your connection string and click Done.

**Step 3: Open a new terminal window and connect to your deployment.**

Use `mongosh` to connect to your self-managed or Atlas deployment. 
For example:

```bash
mongosh "mongodb+srv://my-test-cluster.1twap.mongodb.net/" --apiVersion 1
--username <user>
```

**Step 4: Create a new database.**

```bash
use timeseries
```

This creates and switches to an empty "timeseries" database.

**Step 5: Create an empty time series collection.**

**Note:**

This exercise uses stock ticker sample data. The `date` field stores time data, and
the `ticker` field identifies the individual stock.

a. Set the `timeField`, `metaField`, and `granularity`:

   ```javascript
   timeseries: {
      timeField: "date",
      metaField: "ticker",
      granularity: "seconds"
   }
   ```

#. Create the collection using the `db.createCollection()` method:

   ```bash
   db.createCollection(
      "stocks",
      {
         timeseries: {
            timeField: "date",
            metaField: "ticker",
            granularity: "seconds"
         }
      })
   ```

   This creates an empty time series collection named `stocks`.

**Step 6: Add sample documents.**

Run the `db.collection.insertMany()` method to add the
following sample documents to the collection:

```bash
db.stocks.insertMany([
   { ticker: "MDB", date: ISODate("2021-12-18T15:59:00.000Z"), close: 252.47, volume: 55046.00}, 
   { ticker: "MDB", date: ISODate("2021-12-18T15:58:00.000Z"), close: 252.93, volume: 44042.00}, 
   { ticker: "MDB", date: ISODate("2021-12-18T15:57:00.000Z"), close: 253.61, volume: 40182.00}, 
   { ticker: "MDB", date: ISODate("2021-12-18T15:56:00.000Z"), close: 253.63, volume: 27890.00}, 
   { ticker: "MDB", date: ISODate("2021-12-18T15:55:00.000Z"), close: 254.03, volume: 40270.00}
])
```

If you are running MongoDB on Atlas, you can click 
Browse collections to view the sample data.

**Step 7: Query the data.**

You query a time series collection like any other MongoDB collection. For
more information, see About Querying Time Series Data.

Common queries for time series data are querying the `metaField`
to get data for a single time series, or using a range query on the
`timeField` to get data for a given time span. 

To query the `metaField` for a single time series:

```bash
db.stocks.find( { ticker: "MDB" } )
```

To query the `timeField` for a time span:

```bash
db.stocks.find({ date : {
   $gte : ISODate("2021-12-18T15:50:00.000Z"), 
   $lte : ISODate("2021-12-18T15:56:00.000Z")}
});
```

**Step 1: Install local deployment dependencies.**

For detailed instructions, see `Prerequisites`.

a. Install the `Atlas CLI`.

   If you use [Homebrew](https://brew.sh/#install), you can
   run the following command in your terminal:

   ```
   brew install mongodb-atlas
   ```

   For installation instructions on other operating systems,
   see `Install the Atlas CLI`

#. Install [Docker](https://www.docker.com/).

   Docker requires a network connection for pulling and caching
   MongoDB images.

   - For MacOS or Windows, install [Docker Desktop v4.31+](https://docs.docker.com/desktop/release-notes/#4310).
   - For Linux, install [Docker Engine v27.0+](https://docs.docker.com/engine/release-notes/27/).
   - For RHEL, you can also use [Podman v5.0+](https://podman.io).

**Step 2: Set up your local Atlas deployment.**

a. If you don't have an existing Atlas account, run `atlas setup` in your terminal
   or [create a new account](https://account.mongodb.com/account/register).

#. Run `atlas deployments setup` and follow the prompts to create a
   local deployment. When prompted to connect to the deployment,
   select `skip`.

   For detailed instructions, see `Create a Local Atlas Deployment`.

**Step 3: Install mongosh.**

Go to the `mongosh` page and click
Download mongosh. Check that the platform matches
your system and click Download.

**Step 4: Open a new terminal window and connect to your deployment.**

Use `mongosh` to connect to your self-managed or Atlas deployment. 
For example:

```bash
mongosh "mongodb+srv://my-test-cluster.1twap.mongodb.net/" --apiVersion 1
--username <user>
```

**Step 5: Create a new database.**

```bash
use timeseries
```

This creates and switches to an empty "timeseries" database.

**Step 6: Create an empty time series collection.**

**Note:**

This exercise uses stock ticker sample data. The `date` field stores time data, and
the `ticker` field identifies the individual stock.

a. Set the `timeField`, `metaField`, and `granularity`:

   ```javascript
   timeseries: {
      timeField: "date",
      metaField: "ticker",
      granularity: "seconds"
   }
   ```

#. Create the collection using the `db.createCollection()` method:

   ```bash
   db.createCollection(
      "stocks",
      {
         timeseries: {
            timeField: "date",
            metaField: "ticker",
            granularity: "seconds"
         }
      })
   ```

   This creates an empty time series collection named `stocks`.

**Step 7: Add sample documents.**

Run the `db.collection.insertMany()` method to add the
following sample documents to the collection:

```bash
db.stocks.insertMany([
   { ticker: "MDB", date: ISODate("2021-12-18T15:59:00.000Z"), close: 252.47, volume: 55046.00}, 
   { ticker: "MDB", date: ISODate("2021-12-18T15:58:00.000Z"), close: 252.93, volume: 44042.00}, 
   { ticker: "MDB", date: ISODate("2021-12-18T15:57:00.000Z"), close: 253.61, volume: 40182.00}, 
   { ticker: "MDB", date: ISODate("2021-12-18T15:56:00.000Z"), close: 253.63, volume: 27890.00}, 
   { ticker: "MDB", date: ISODate("2021-12-18T15:55:00.000Z"), close: 254.03, volume: 40270.00}
])
```

If you are running MongoDB on Atlas, you can click 
Browse collections to view the sample data.

**Step 8: Query the data.**

You query a time series collection like any other MongoDB collection. For
more information, see About Querying Time Series Data.

Common queries for time series data are querying the `metaField`
to get data for a single time series, or using a range query on the
`timeField` to get data for a given time span. 

To query the `metaField` for a single time series:

```bash
db.stocks.find( { ticker: "MDB" } )
```

To query the `timeField` for a time span:

```bash
db.stocks.find({ date : {
   $gte : ISODate("2021-12-18T15:50:00.000Z"), 
   $lte : ISODate("2021-12-18T15:56:00.000Z")}
});
```

**Step 1: Install MongoDB and local deployment dependencies.**

If you're running a self-managed deployment, follow the
installation instructions for your
MongoDB version, edition, and platform.

**Step 2: Install mongosh.**

Go to the `mongosh` page and click
Download mongosh. Check that the platform matches
your system and click Download.

**Step 3: Open a new terminal window and connect to your deployment.**

Use `mongosh` to connect to your self-managed or Atlas deployment. 
For example:

```bash
mongosh "mongodb+srv://my-test-cluster.1twap.mongodb.net/" --apiVersion 1
--username <user>
```

**Step 4: Create a new database.**

```bash
use timeseries
```

This creates and switches to an empty "timeseries" database.

**Step 5: Create an empty time series collection.**

**Note:**

This exercise uses stock ticker sample data. The `date` field stores time data, and
the `ticker` field identifies the individual stock.

a. Set the `timeField`, `metaField`, and `granularity`:

   ```javascript
   timeseries: {
      timeField: "date",
      metaField: "ticker",
      granularity: "seconds"
   }
   ```

#. Create the collection using the `db.createCollection()` method:

   ```bash
   db.createCollection(
      "stocks",
      {
         timeseries: {
            timeField: "date",
            metaField: "ticker",
            granularity: "seconds"
         }
      })
   ```

   This creates an empty time series collection named `stocks`.

**Step 6: Add sample documents.**

Run the `db.collection.insertMany()` method to add the
following sample documents to the collection:

```bash
db.stocks.insertMany([
   { ticker: "MDB", date: ISODate("2021-12-18T15:59:00.000Z"), close: 252.47, volume: 55046.00}, 
   { ticker: "MDB", date: ISODate("2021-12-18T15:58:00.000Z"), close: 252.93, volume: 44042.00}, 
   { ticker: "MDB", date: ISODate("2021-12-18T15:57:00.000Z"), close: 253.61, volume: 40182.00}, 
   { ticker: "MDB", date: ISODate("2021-12-18T15:56:00.000Z"), close: 253.63, volume: 27890.00}, 
   { ticker: "MDB", date: ISODate("2021-12-18T15:55:00.000Z"), close: 254.03, volume: 40270.00}
])
```

If you are running MongoDB on Atlas, you can click 
Browse collections to view the sample data.

**Step 7: Query the data.**

You query a time series collection like any other MongoDB collection. For
more information, see About Querying Time Series Data.

Common queries for time series data are querying the `metaField`
to get data for a single time series, or using a range query on the
`timeField` to get data for a given time span. 

To query the `metaField` for a single time series:

```bash
db.stocks.find( { ticker: "MDB" } )
```

To query the `timeField` for a time span:

```bash
db.stocks.find({ date : {
   $gte : ISODate("2021-12-18T15:50:00.000Z"), 
   $lte : ISODate("2021-12-18T15:56:00.000Z")}
});
```

**Step 1: Set up your Atlas cluster.**

a. [Create a free Atlas account or sign in to an existing account](https://account.mongodb.com/account/register).

#. If you don't yet have an Atlas cluster, [create a free M0 cluster](https://cloud.mongodb.com/go?l=https%3A%2F%2Fcloud.mongodb.com%2Fv2%2F%3Cproject%3E%23clusters%2Fedit%3Ffrom%3DctaClusterHeader).
   To learn more about creating an Atlas cluster, see Create a Cluster.

   **Note:**

   If you are working with an existing cluster, you must have
   `Project Data Access Admin` or higher access to your
   Atlas project.

   If you create a new cluster, you have the necessary permissions by default.

   You can create only one `M0` Free cluster per project.

#. In the left sidebar, click [Overview](https://cloud.mongodb.com/go?l=https%3A%2F%2Fcloud.mongodb.com%2Fv2%2F%3Cproject%3E%23%2Foverview).
   Choose your cluster and click Connect.

**Step 2: Get Node.js Driver connection details.**

a. Under Connect to your application, click Driver.
   Select Node.js.

   If you haven't already, follow the steps provided to download and
   install the `Node.js Driver`.

#. Copy your connection string and click Done.

**Step 3: Copy the template app and connect to your deployment.**

a. Paste the following code into a new `.js` file.

#. Replace `"<connection-string>"` with your copied connection string.

As you work with time series code examples, add them between the
`// start example code here` and `// end example code here` comments.

```javascript
import { MongoClient } from 'mongodb';

// Replace the placeholder with your connection string.
const uri = '<connection-string>';
const client = new MongoClient(uri);

export async function runApp() {
  try {
    // start example code here
    // end example code here
  } finally {
    await client.close();
  }
}

runApp().catch(console.dir);
```

**Step 4: Create a new database.**

```javascript
const timeSeriesDB = client.db('timeseries');
```

This creates a reference to an empty "timeseries" database.

**Step 5: Create an empty time series collection.**

**Note:**

This exercise uses stock ticker sample data. The `date` field stores time data, and
the `ticker` field identifies the individual stock.

a. Set the `timeField`, `metaField`, and `granularity`:

   ```javascript
   const options = {
     timeseries: {
       timeField: 'date',
       metaField: 'ticker',
       granularity: 'seconds',
     },
   };
   ```

#. Create the collection using the `db.createCollection()` method:

   ```javascript
   const stocks = await timeSeriesDB.createCollection('stocks', options);
   ```

   This creates an empty time series collection named `stocks`.

**Step 6: Add sample documents.**

Use the `db.collection.insertMany()` method to add the
following sample documents to the collection:

```javascript
const sampleDocuments = [
  {
    ticker: 'MDB',
    date: new Date(2021, 11, 18, 15, 59, 0, 0),
    close: 252.47,
    volume: 55046.0,
  },
  {
    ticker: 'MDB',
    date: new Date(2021, 11, 18, 15, 58, 0, 0),
    close: 252.93,
    volume: 44042.0,
  },
  {
    ticker: 'MDB',
    date: new Date(2021, 11, 18, 15, 57, 0, 0),
    close: 253.61,
    volume: 40182.0,
  },
  {
    ticker: 'MDB',
    date: new Date(2021, 11, 18, 15, 56, 0, 0),
    close: 253.63,
    volume: 27890.0,
  },
  {
    ticker: 'MDB',
    date: new Date(2021, 11, 18, 15, 55, 0, 0),
    close: 254.03,
    volume: 40270.0,
  },
];

const result = await stocks.insertMany(sampleDocuments);
```

If you are running MongoDB on Atlas, you can click
Browse collections to view the sample data.

**Step 7: Query the data.**

You query a time series collection like any other MongoDB collection. For
more information, see About Querying Time Series Data.

Common queries for time series data are querying the `metaField`
to get data for a single time series, or using a range query on the
`timeField` to get data for a given time span.

To query the `metaField` for a single time series:

```javascript
```

Output:

```shell
```

To query the `timeField` for a time span:

```javascript
```

Output:

```shell
```

**Step 1: Install local deployment dependencies.**

For detailed instructions, see `Prerequisites`.

a. Install the `Atlas CLI`.

   If you use [Homebrew](https://brew.sh/#install), you can
   run the following command in your terminal:

   ```
   brew install mongodb-atlas
   ```

   For installation instructions on other operating systems,
   see `Install the Atlas CLI`

#. Install [Docker](https://www.docker.com/).

   Docker requires a network connection for pulling and caching
   MongoDB images.

   - For MacOS or Windows, install [Docker Desktop v4.31+](https://docs.docker.com/desktop/release-notes/#4310).
   - For Linux, install [Docker Engine v27.0+](https://docs.docker.com/engine/release-notes/27/).
   - For RHEL, you can also use [Podman v5.0+](https://podman.io).

**Step 2: Set up your local Atlas deployment.**

a. If you don't have an existing Atlas account, run `atlas setup` in your terminal
   or [create a new account](https://account.mongodb.com/account/register).

#. Run `atlas deployments setup` and follow the prompts to create a
   local deployment. When prompted to connect to the deployment,
   select `skip`.

   For detailed instructions, see `Create a Local Atlas Deployment`.

**Step 3: Install the Node.js Driver.**

Follow the directions on the [Node.js Get Started](https://www.mongodb.com/docs/drivers/node/current/get-started/)
page to create a new project directory and install driver dependencies.

**Step 4: Copy the template app and connect to your deployment.**

a. Paste the following code into a new `.js` file.

#. Replace `"<connection-string>"` with your copied connection string.

As you work with time series code examples, add them between the
`// start example code here` and `// end example code here` comments.

```javascript
import { MongoClient } from 'mongodb';

// Replace the placeholder with your connection string.
const uri = '<connection-string>';
const client = new MongoClient(uri);

export async function runApp() {
  try {
    // start example code here
    // end example code here
  } finally {
    await client.close();
  }
}

runApp().catch(console.dir);
```

**Step 5: Create a new database.**

```javascript
const timeSeriesDB = client.db('timeseries');
```

This creates a reference to an empty "timeseries" database.

**Step 6: Create an empty time series collection.**

**Note:**

This exercise uses stock ticker sample data. The `date` field stores time data, and
the `ticker` field identifies the individual stock.

a. Set the `timeField`, `metaField`, and `granularity`:

   ```javascript
   const options = {
     timeseries: {
       timeField: 'date',
       metaField: 'ticker',
       granularity: 'seconds',
     },
   };
   ```

#. Create the collection using the `db.createCollection()` method:

   ```javascript
   const stocks = await timeSeriesDB.createCollection('stocks', options);
   ```

   This creates an empty time series collection named `stocks`.

**Step 7: Add sample documents.**

Use the `db.collection.insertMany()` method to add the
following sample documents to the collection:

```javascript
const sampleDocuments = [
  {
    ticker: 'MDB',
    date: new Date(2021, 11, 18, 15, 59, 0, 0),
    close: 252.47,
    volume: 55046.0,
  },
  {
    ticker: 'MDB',
    date: new Date(2021, 11, 18, 15, 58, 0, 0),
    close: 252.93,
    volume: 44042.0,
  },
  {
    ticker: 'MDB',
    date: new Date(2021, 11, 18, 15, 57, 0, 0),
    close: 253.61,
    volume: 40182.0,
  },
  {
    ticker: 'MDB',
    date: new Date(2021, 11, 18, 15, 56, 0, 0),
    close: 253.63,
    volume: 27890.0,
  },
  {
    ticker: 'MDB',
    date: new Date(2021, 11, 18, 15, 55, 0, 0),
    close: 254.03,
    volume: 40270.0,
  },
];

const result = await stocks.insertMany(sampleDocuments);
```

If you are running MongoDB on Atlas, you can click
Browse collections to view the sample data.

**Step 8: Query the data.**

You query a time series collection like any other MongoDB collection. For
more information, see About Querying Time Series Data.

Common queries for time series data are querying the `metaField`
to get data for a single time series, or using a range query on the
`timeField` to get data for a given time span.

To query the `metaField` for a single time series:

```javascript
```

Output:

```shell
```

To query the `timeField` for a time span:

```javascript
```

Output:

```shell
```

**Step 1: Install MongoDB and local deployment dependencies.**

If you're running a self-managed deployment, follow the
installation instructions for your
MongoDB version, edition, and platform.

**Step 2: Install the Node.js Driver.**

Follow the directions on the [Node.js Get Started](https://www.mongodb.com/docs/drivers/node/current/get-started/)
page to create a new project directory and install driver dependencies.

**Step 3: Copy the template app and connect to your deployment.**

a. Paste the following code into a new `.js` file.

#. Replace `"<connection-string>"` with your copied connection string.

As you work with time series code examples, add them between the
`// start example code here` and `// end example code here` comments.

```javascript
import { MongoClient } from 'mongodb';

// Replace the placeholder with your connection string.
const uri = '<connection-string>';
const client = new MongoClient(uri);

export async function runApp() {
  try {
    // start example code here
    // end example code here
  } finally {
    await client.close();
  }
}

runApp().catch(console.dir);
```

**Step 4: Create a new database.**

```javascript
const timeSeriesDB = client.db('timeseries');
```

This creates a reference to an empty "timeseries" database.

**Step 5: Create an empty time series collection.**

**Note:**

This exercise uses stock ticker sample data. The `date` field stores time data, and
the `ticker` field identifies the individual stock.

a. Set the `timeField`, `metaField`, and `granularity`:

   ```javascript
   const options = {
     timeseries: {
       timeField: 'date',
       metaField: 'ticker',
       granularity: 'seconds',
     },
   };
   ```

#. Create the collection using the `db.createCollection()` method:

   ```javascript
   const stocks = await timeSeriesDB.createCollection('stocks', options);
   ```

   This creates an empty time series collection named `stocks`.

**Step 6: Add sample documents.**

Use the `db.collection.insertMany()` method to add the
following sample documents to the collection:

```javascript
const sampleDocuments = [
  {
    ticker: 'MDB',
    date: new Date(2021, 11, 18, 15, 59, 0, 0),
    close: 252.47,
    volume: 55046.0,
  },
  {
    ticker: 'MDB',
    date: new Date(2021, 11, 18, 15, 58, 0, 0),
    close: 252.93,
    volume: 44042.0,
  },
  {
    ticker: 'MDB',
    date: new Date(2021, 11, 18, 15, 57, 0, 0),
    close: 253.61,
    volume: 40182.0,
  },
  {
    ticker: 'MDB',
    date: new Date(2021, 11, 18, 15, 56, 0, 0),
    close: 253.63,
    volume: 27890.0,
  },
  {
    ticker: 'MDB',
    date: new Date(2021, 11, 18, 15, 55, 0, 0),
    close: 254.03,
    volume: 40270.0,
  },
];

const result = await stocks.insertMany(sampleDocuments);
```

If you are running MongoDB on Atlas, you can click
Browse collections to view the sample data.

**Step 7: Query the data.**

You query a time series collection like any other MongoDB collection. For
more information, see About Querying Time Series Data.

Common queries for time series data are querying the `metaField`
to get data for a single time series, or using a range query on the
`timeField` to get data for a given time span.

To query the `metaField` for a single time series:

```javascript
```

Output:

```shell
```

To query the `timeField` for a time span:

```javascript
```

Output:

```shell
```

**Step 1: Set up your Atlas cluster.**

a. [Create a free Atlas account or sign in to an existing account](https://account.mongodb.com/account/register).

#. If you don't yet have an Atlas cluster, [create a free M0 cluster](https://cloud.mongodb.com/go?l=https%3A%2F%2Fcloud.mongodb.com%2Fv2%2F%3Cproject%3E%23clusters%2Fedit%3Ffrom%3DctaClusterHeader).
   To learn more about creating an Atlas cluster, see Create a Cluster.

   **Note:**

   If you are working with an existing cluster, you must have
   `Project Data Access Admin` or higher access to your
   Atlas project.

   If you create a new cluster, you have the necessary permissions by default.

   You can create only one `M0` Free cluster per project.

#. In the left sidebar, click [Overview](https://cloud.mongodb.com/go?l=https%3A%2F%2Fcloud.mongodb.com%2Fv2%2F%3Cproject%3E%23%2Foverview).
   Choose your cluster and click Connect.

**Step 2: Get PyMongo connection details.**

a. Under Connect to your application, click Driver.
   Select Python.

   If you haven't already, follow the steps provided to download and
   install the `PyMongo Driver`.

#. Copy your connection string and click Done.

**Step 3: Copy the template app and connect to your deployment.**

a. Paste the following code into a new `.py` file.

#. Replace `"<connection-string>"` with your copied connection string.

As you work with time series code examples, add them between the
`# start example code here` and `# end example code here` comments.

```python
from datetime import datetime
from pymongo import MongoClient

try:
    uri = "<connection-string>"
    client = MongoClient(uri)

    # start example code here

    # end example code here

    client.close()

except Exception as e:
    raise Exception("The following error occurred: ", e)
```

**Step 4: Create a new database.**

```python
timeseries_db = client["timeseries"]
```

This creates a reference to an empty "timeseries" database.

**Step 5: Create an empty time series collection.**

**Note:**

This exercise uses stock ticker sample data. The `date` field stores time data, and
the `ticker` field identifies the individual stock.

a. Set the `timeField`, `metaField`, and `granularity`:

   ```python
   time_series_options = {
       "timeField": "date",
       "metaField": "ticker",
       "granularity": "seconds",
   }
   ```

#. Create the collection using the `db.create_collection()` method:

   ```python
   timeseries_db.create_collection("stocks", timeseries=time_series_options)
   ```

   This creates an empty time series collection named `stocks`.

**Step 6: Add sample documents.**

Use the `db.collection.insert_many()` method to add the
following sample documents to the collection:

```python
stocks_coll = timeseries_db["stocks"]

sample_documents = [
    {
        "ticker": "MDB",
        "date": datetime(2021, 12, 18, 15, 59, 0, 0),
        "close": 252.47,
        "volume": 55046.00,
    },
    {
        "ticker": "MDB",
        "date": datetime(2021, 12, 18, 15, 58, 0, 0),
        "close": 252.93,
        "volume": 44042.00,
    },
    {
        "ticker": "MDB",
        "date": datetime(2021, 12, 18, 15, 57, 0, 0),
        "close": 253.61,
        "volume": 40182.00,
    },
    {
        "ticker": "MDB",
        "date": datetime(2021, 12, 18, 15, 56, 0, 0),
        "close": 253.63,
        "volume": 27890.00,
    },
    {
        "ticker": "MDB",
        "date": datetime(2021, 12, 18, 15, 55, 0, 0),
        "close": 254.03,
        "volume": 40270.00,
    },
]

stocks_coll.insert_many(sample_documents)
```

If you are running MongoDB on Atlas, you can click
Browse collections to view the sample data.

**Step 7: Query the data.**

You query a time series collection like any other MongoDB collection. For
more information, see About Querying Time Series Data.

Common queries for time series data are querying the `metaField`
to get data for a single time series, or using a range query on the
`timeField` to get data for a given time span.

To query the `metaField` for a single time series:

```python
```

Output:

```text
```

To query the `timeField` for a time span:

```python
```

Output:

```text
```

**Step 1: Install local deployment dependencies.**

For detailed instructions, see `Prerequisites`.

a. Install the `Atlas CLI`.

   If you use [Homebrew](https://brew.sh/#install), you can
   run the following command in your terminal:

   ```
   brew install mongodb-atlas
   ```

   For installation instructions on other operating systems,
   see `Install the Atlas CLI`

#. Install [Docker](https://www.docker.com/).

   Docker requires a network connection for pulling and caching
   MongoDB images.

   - For MacOS or Windows, install [Docker Desktop v4.31+](https://docs.docker.com/desktop/release-notes/#4310).
   - For Linux, install [Docker Engine v27.0+](https://docs.docker.com/engine/release-notes/27/).
   - For RHEL, you can also use [Podman v5.0+](https://podman.io).

**Step 2: Set up your local Atlas deployment.**

a. If you don't have an existing Atlas account, run `atlas setup` in your terminal
   or [create a new account](https://account.mongodb.com/account/register).

#. Run `atlas deployments setup` and follow the prompts to create a
   local deployment. When prompted to connect to the deployment,
   select `skip`.

   For detailed instructions, see `Create a Local Atlas Deployment`.

**Step 3: Install the PyMongo Driver.**

Follow the directions on the [PyMongo Get Started](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/get-started/)
page to create a new project directory and install driver dependencies.

**Step 4: Copy the template app and connect to your deployment.**

a. Paste the following code into a new `.py` file.

#. Replace `"<connection-string>"` with your copied connection string.

As you work with time series code examples, add them between the
`# start example code here` and `# end example code here` comments.

```python
from datetime import datetime
from pymongo import MongoClient

try:
    uri = "<connection-string>"
    client = MongoClient(uri)

    # start example code here

    # end example code here

    client.close()

except Exception as e:
    raise Exception("The following error occurred: ", e)
```

**Step 5: Create a new database.**

```python
timeseries_db = client["timeseries"]
```

This creates a reference to an empty "timeseries" database.

**Step 6: Create an empty time series collection.**

**Note:**

This exercise uses stock ticker sample data. The `date` field stores time data, and
the `ticker` field identifies the individual stock.

a. Set the `timeField`, `metaField`, and `granularity`:

   ```python
   time_series_options = {
       "timeField": "date",
       "metaField": "ticker",
       "granularity": "seconds",
   }
   ```

#. Create the collection using the `db.create_collection()` method:

   ```python
   timeseries_db.create_collection("stocks", timeseries=time_series_options)
   ```

   This creates an empty time series collection named `stocks`.

**Step 7: Add sample documents.**

Use the `db.collection.insert_many()` method to add the
following sample documents to the collection:

```python
stocks_coll = timeseries_db["stocks"]

sample_documents = [
    {
        "ticker": "MDB",
        "date": datetime(2021, 12, 18, 15, 59, 0, 0),
        "close": 252.47,
        "volume": 55046.00,
    },
    {
        "ticker": "MDB",
        "date": datetime(2021, 12, 18, 15, 58, 0, 0),
        "close": 252.93,
        "volume": 44042.00,
    },
    {
        "ticker": "MDB",
        "date": datetime(2021, 12, 18, 15, 57, 0, 0),
        "close": 253.61,
        "volume": 40182.00,
    },
    {
        "ticker": "MDB",
        "date": datetime(2021, 12, 18, 15, 56, 0, 0),
        "close": 253.63,
        "volume": 27890.00,
    },
    {
        "ticker": "MDB",
        "date": datetime(2021, 12, 18, 15, 55, 0, 0),
        "close": 254.03,
        "volume": 40270.00,
    },
]

stocks_coll.insert_many(sample_documents)
```

If you are running MongoDB on Atlas, you can click
Browse collections to view the sample data.

**Step 8: Query the data.**

You query a time series collection like any other MongoDB collection. For
more information, see About Querying Time Series Data.

Common queries for time series data are querying the `metaField`
to get data for a single time series, or using a range query on the
`timeField` to get data for a given time span.

To query the `metaField` for a single time series:

```python
```

Output:

```text
```

To query the `timeField` for a time span:

```python
```

Output:

```text
```

**Step 1: Install MongoDB and local deployment dependencies.**

If you're running a self-managed deployment, follow the
installation instructions for your
MongoDB version, edition, and platform.

**Step 2: Install the PyMongo Driver.**

Follow the directions on the [PyMongo Get Started](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/get-started/)
page to create a new project directory and install driver dependencies.

**Step 3: Copy the template app and connect to your deployment.**

a. Paste the following code into a new `.py` file.

#. Replace `"<connection-string>"` with your copied connection string.

As you work with time series code examples, add them between the
`# start example code here` and `# end example code here` comments.

```python
from datetime import datetime
from pymongo import MongoClient

try:
    uri = "<connection-string>"
    client = MongoClient(uri)

    # start example code here

    # end example code here

    client.close()

except Exception as e:
    raise Exception("The following error occurred: ", e)
```

**Step 4: Create a new database.**

```python
timeseries_db = client["timeseries"]
```

This creates a reference to an empty "timeseries" database.

**Step 5: Create an empty time series collection.**

**Note:**

This exercise uses stock ticker sample data. The `date` field stores time data, and
the `ticker` field identifies the individual stock.

a. Set the `timeField`, `metaField`, and `granularity`:

   ```python
   time_series_options = {
       "timeField": "date",
       "metaField": "ticker",
       "granularity": "seconds",
   }
   ```

#. Create the collection using the `db.create_collection()` method:

   ```python
   timeseries_db.create_collection("stocks", timeseries=time_series_options)
   ```

   This creates an empty time series collection named `stocks`.

**Step 6: Add sample documents.**

Use the `db.collection.insert_many()` method to add the
following sample documents to the collection:

```python
stocks_coll = timeseries_db["stocks"]

sample_documents = [
    {
        "ticker": "MDB",
        "date": datetime(2021, 12, 18, 15, 59, 0, 0),
        "close": 252.47,
        "volume": 55046.00,
    },
    {
        "ticker": "MDB",
        "date": datetime(2021, 12, 18, 15, 58, 0, 0),
        "close": 252.93,
        "volume": 44042.00,
    },
    {
        "ticker": "MDB",
        "date": datetime(2021, 12, 18, 15, 57, 0, 0),
        "close": 253.61,
        "volume": 40182.00,
    },
    {
        "ticker": "MDB",
        "date": datetime(2021, 12, 18, 15, 56, 0, 0),
        "close": 253.63,
        "volume": 27890.00,
    },
    {
        "ticker": "MDB",
        "date": datetime(2021, 12, 18, 15, 55, 0, 0),
        "close": 254.03,
        "volume": 40270.00,
    },
]

stocks_coll.insert_many(sample_documents)
```

If you are running MongoDB on Atlas, you can click
Browse collections to view the sample data.

**Step 7: Query the data.**

You query a time series collection like any other MongoDB collection. For
more information, see About Querying Time Series Data.

Common queries for time series data are querying the `metaField`
to get data for a single time series, or using a range query on the
`timeField` to get data for a given time span.

To query the `metaField` for a single time series:

```python
```

Output:

```text
```

To query the `timeField` for a time span:

```python
```

Output:

```text
```

## Sample Data

The following example shows the `stocks` time series collection
structure used in this quick start.

```javascript
{
   _id: ObjectId(...),
   ticker: <string>,
   date: ISODate(...),
   close: <double>,
   volume: <double>
}
```

## Learning Summary

Time series collections are optimized for time data, so performance
depends heavily on how you configure them at creation. For more
information, see Time Series Collection Considerations.

## Next Steps

* To migrate existing data into a time series collection, see Migrate
  Data into a Time Series Collection.

* To shard a time series collection, see Shard a Time Series Collection.

* For aggregation and query behaviors specific to time series
  collections, see Aggregation and Operator Considerations.

## Learn More

* To learn how MongoDB stores time series data internally, see
  About Time Series Data.

* To learn about custom bucketing parameters in MongoDB 6.3 and later,
  see Using Custom Bucketing Parameters.
