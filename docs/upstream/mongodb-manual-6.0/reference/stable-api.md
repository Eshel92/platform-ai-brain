<!-- Converted from reference/stable-api.txt (reStructuredText). Includes are inlined. -->

# Stable API

   

## What is the Stable API, and Should You Use It?

The MongoDB Stable API (previously labeled the Versioned API) lets you 
upgrade your MongoDB server at will, and ensure that behavior changes 
between MongoDB versions do not break your application.

MongoDB 5.0 introduces the Stable API for applications 
communicating with MongoDB server products. The Stable API allows 
you to specify which version of the MongoDB API your application 
runs against.

The Stable API provides long-term API stability for applications 
and supports more frequent releases and automatic server upgrades. This 
allows your applications to take advantage of rapidly released 
features without risking backwards-breaking changes.

The default behavior for your driver connection will continue to 
function as expected, even if you do not explicitly specify
an apiVersion.

The Stable API encompasses the 
subset of MongoDB commands that 
applications use to read and write data, create collections 
and indexes, and perform other common tasks. 

**Note:**

Starting in February 2022, the "Versioned API" terminology was 
changed to "Stable API". All concepts and features remain the same 
with this naming change.

## Backward Compatibility Guarantee

Your application will not experience significant behavior changes 
resulting from server upgrades. This guarantee holds as long as the 
new server supports your specified API version.

To guarantee backward compatibility, your application must:

- Declare an API version
- Only use commands and features supported in your specified API version
- Deploy with a supported version of an official driver

## Declare the API Version

----------

→ Use the **Select your language** drop-down menu in the
upper-right to set the language of the examples on this page.

----------

To use the Stable API, upgrade to the latest driver and create your 
application's MongoClient:

**shell:**

```javascript
mongosh --apiVersion 1
```

**python:**

(Code example not available offline: /driver-examples/test_examples.py)

**php:**

(Code example not available offline: /driver-examples/DocumentationExamplesTest.php)

**c:**

(Code example not available offline: /driver-examples/test-mongoc-sample-commands.c)

**go:**

(Code example not available offline: /driver-examples/go_examples.go)

**csharp:**

(Code example not available offline: /driver-examples/VersionedApiExamples.cs)

**nodejs:**

(Code example not available offline: /driver-examples/node_versioned_api.js)

**java-sync:**

```java-sync
MongoClient client = MongoClients.create(
        MongoClientSettings.builder()
        .applyConnectionString(new ConnectionString(<connection string>))
        .serverApi(
                ServerApi.builder()
                .version(ServerApiVersion.V1)
                .build()
                ).build()
        );

return client;
```

**motor:**

(Code example not available offline: /driver-examples/test_examples_motor.py)

**rust:**

(Code example not available offline: /driver-examples/mod.rs)

**ruby:**

(Code example not available offline: /driver-examples/versioned_api_examples_spec.rb)

**cpp:**

(Code example not available offline: /driver-examples/cpp-versioned_api.cpp)

**swift-sync:**

(Code example not available offline: /driver-examples/swiftSync.swift)

**swift-async:**

(Code example not available offline: /driver-examples/swiftAsync.swift)

`"1"` is currently the only API version available. 

By default, clients are *non-strict*. A non-strict client allows you
to run any command, regardless of whether or not it belongs to the 
Stable API.

## Checking Client API Versions

Use the `serverStatus` command to check for your 
application's configured API version. For each application connected to 
your MongoDB instance, an `appname` appears in the `apiVersions` 
document.

See metrics.apiVersions for more 
information.

```javascript
db.runCommand( { serverStatus: 1 } ).metrics.apiVersions
```

## Create a Strict Client

A *strict* client rejects all commands outside of the Stable API.
Attempts to use commands outside of the Stable API will receive the 
APIVersionError response.

A strict client also ignores 
unsupported index types during 
query planning and 
execution.

Use the sample code to create a *strict* client:

**shell:**

```javascript
mongosh --apiVersion 1 --apiStrict
```

**python:**

(Code example not available offline: /driver-examples/test_examples.py)

**php:**

(Code example not available offline: /driver-examples/DocumentationExamplesTest.php)

**c:**

(Code example not available offline: /driver-examples/test-mongoc-sample-commands.c)

**go:**

(Code example not available offline: /driver-examples/go_examples.go)

**csharp:**

(Code example not available offline: /driver-examples/VersionedApiExamples.cs)

**nodejs:**

(Code example not available offline: /driver-examples/node_versioned_api.js)

**java-sync:**

```java-sync
MongoClient client = MongoClients.create(
        MongoClientSettings.builder()
        .applyConnectionString(new ConnectionString(<connection string>))
        .serverApi(
                ServerApi.builder()
                .version(ServerApiVersion.V1)
                .strict(true)
                .build()
                ).build()
        );

return client;
```

**motor:**

(Code example not available offline: /driver-examples/test_examples_motor.py)

**rust:**

(Code example not available offline: /driver-examples/mod.rs)

**ruby:**

(Code example not available offline: /driver-examples/versioned_api_examples_spec.rb)

**cpp:**

(Code example not available offline: /driver-examples/cpp-versioned_api.cpp)

**swift-sync:**

(Code example not available offline: /driver-examples/swiftSync.swift)

**swift-async:**

(Code example not available offline: /driver-examples/swiftAsync.swift)

## Migrate To Stable API Commands

To migrate your application to use the Stable API, you must:

#. Run your application's test suite with the new MongoClient options.
#. Determine which commands and features you're using that are outside 
   of the Stable API.
#. Migrate to alternative commands and features in the Stable API.

Once your application uses only commands and features defined in the 
Stable API, you can redeploy it with the new MongoClient options 
and be confident that future server upgrades won't negatively
impact your application.

## How To Use Commands and Features Outside of the Stable API

To use commands and features outside of the Stable API, you can 
connect to your deployment with a *non-strict* client. By default,
clients are *non-strict*.

To create a *non-strict* client, use the following sample code:

**shell:**

```javascript
mongosh --apiVersion 1
```

**python:**

(Code example not available offline: /driver-examples/test_examples.py)

**php:**

(Code example not available offline: /driver-examples/DocumentationExamplesTest.php)

**c:**

(Code example not available offline: /driver-examples/test-mongoc-sample-commands.c)

**go:**

(Code example not available offline: /driver-examples/go_examples.go)

**csharp:**

(Code example not available offline: /driver-examples/VersionedApiExamples.cs)

**nodejs:**

(Code example not available offline: /driver-examples/node_versioned_api.js)

**java-sync:**

```java-sync
MongoClient client = MongoClients.create(
        MongoClientSettings.builder()
        .applyConnectionString(new ConnectionString(<connection string>))
        .serverApi(
                ServerApi.builder()
                .version(ServerApiVersion.V1)
                .strict(false)
                .build()
                ).build()
        );
```

**motor:**

(Code example not available offline: /driver-examples/test_examples_motor.py)

**rust:**

(Code example not available offline: /driver-examples/mod.rs)

**ruby:**

(Code example not available offline: /driver-examples/versioned_api_examples_spec.rb)

**cpp:**

(Code example not available offline: /driver-examples/cpp-versioned_api.cpp)

**swift-sync:**

(Code example not available offline: /driver-examples/swiftSync.swift)

**swift-async:**

(Code example not available offline: /driver-examples/swiftAsync.swift)

Using this non-strict client allows you to run commands outside of the
Stable API. For example, this non-strict client allows you to run the
`createUser` command.

**Important:**

Commands and features outside of the Stable API do not have the same 
backward compatibility guarantees as versioned alternatives.

## Stable API Commands

The database commands included in Stable API V1 depend on the MongoDB
version you are using. To view the database commands included in the
Stable API and the MongoDB version they were introduced, see
stable-api-changelog.

## Parameters

You can specify the following optional parameters for Stable API in 
your application's MongoDB driver connection code. Check the MongoDB 
driver documentation for the driver you use in your application for 
more information:

* - Parameter
  - Type
  - Description

* - apiVersion
  - string
  - Specifies the API Version. `"1"` is
    currently the only supported version.

* - apiStrict
  - boolean 
  - If `true`:
       - Using a command that is not part of the declared API 
         version returns an APIStrictError 
         error.

       - Indexes that are unsupported 
         by the Stable API are ignored by the 
         query planner.

    If you specify apiStrict, you must also specify apiVersion.  

    If not specified, defaults to `false`. 

* - apiDeprecationErrors
  - boolean
  - If `true`, using a command or behavior that is deprecated 
    in the specified API version returns an 
    APIDeprecationError. If you specify
    apiDeprecationErrors, you must also specify apiVersion.

    If not specified, defaults to `false`. 
  
       

## Behavior

### Parameter Validation

Starting in MongoDB 5.0, API V1 database commands raise an error if 
passed a parameter not explicitly accepted by the command. 

## Stable API Error Responses

This table shows error responses for problematic Stable API requests.

| Server Response | Request |
|---|---|
| APIDeprecationError | .. _api-deprecation-resp: Specifies `{ apiDeprecationErrors: true }` with API version `V` and uses a behavior deprecated in `V`. |
| APIStrictError | .. _api-strict-resp: Specifies `{ apiStrict: true }` with API version `V`, but uses a behavior not in version `V`. |
| APIVersionError | .. _api-vers-resp: Specifies an apiVersion that the server does not support. |
| InvalidOptions | .. _api-invalid-opts-resp: Specifies `{ apiStrict: true }` or `{ apiDeprecationErrors: true }` but omits apiVersion. |
