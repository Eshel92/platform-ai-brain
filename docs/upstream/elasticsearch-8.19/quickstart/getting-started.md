<!-- Converted from quickstart/getting-started.asciidoc (AsciiDoc). Includes are inlined. -->

## Index and search data using Elasticsearch APIs

This quick start guide is a hands-on introduction to the fundamental concepts of Elasticsearch: indices, documents and field type mappings.

You'll learn how to create an index, add data as documents, work with dynamic and explicit mappings, and perform your first basic searches.

**Tip:**
The code examples in this tutorial are in [Console](https://www.elastic.co/guide/en/kibana/8.19/console-kibana.html) syntax by default.
You can [convert into other programming languages](https://www.elastic.co/guide/en/kibana/8.19/console-kibana.html#import-export-console-requests) in the Console UI.

### Requirements

You'll need a running Elasticsearch cluster, together with Kibana to use the Dev Tools API Console.
Run the following command in your terminal to set up a single-node local cluster in Docker:

```sh
curl -fsSL https://elastic.co/start-local | sh
```

### Step 1: Create an index

Create a new index named `books`:

```console
PUT /books
```

The following response indicates the index was created successfully.

**Example response**
===============
```console-result
{
  "acknowledged": true,
  "shards_acknowledged": true,
  "index": "books"
}
```
===============

### Step 2: Add data to your index

**Tip:**
This tutorial uses Elasticsearch APIs, but there are many other ways to
add data to Elasticsearch.

You add data to Elasticsearch as JSON objects called documents.
Elasticsearch stores these
documents in searchable indices.

#### Add a single document

Submit the following indexing request to add a single document to the
`books` index.

**Tip:**
If the index didn't already exist, this request would automatically create it.

```console
POST books/_doc
{
  "name": "Snow Crash",
  "author": "Neal Stephenson",
  "release_date": "1992-06-01",
  "page_count": 470
}
```

The response includes metadata that Elasticsearch generates for the document, including a unique `_id` for the document within the index.

**Example response**
===============
```console-result
{
  "_index": "books", <1>
  "_id": "O0lG2IsBaSa7VYx_rEia", <2>
  "_version": 1, <3>
  "result": "created", <4>
  "_shards": { <5>
    "total": 2, <6>
    "successful": 2, <7>
    "failed": 0 <8>
  },
  "_seq_no": 0, <9>
  "_primary_term": 1 <10>
}
```
<1> The `_index` field indicates the index the document was added to.
<2> The `_id` field is the unique identifier for the document.
<3> The `_version` field indicates the version of the document.
<4> The `result` field indicates the result of the indexing operation.
<5> The `_shards` field contains information about the number of shards that the indexing operation was executed on and the number that succeeded.
<6> The `total` field indicates the total number of shards for the index.
<7> The `successful` field indicates the number of shards that the indexing operation was executed on.
<8> The `failed` field indicates the number of shards that failed during the indexing operation. '0' indicates no failures.
<9> The `_seq_no` field holds a monotonically increasing number incremented for each indexing operation on a shard.
<10> The `_primary_term` field is a monotonically increasing number incremented each time a primary shard is assigned to a different node.
===============

#### Add multiple documents

Use the `_bulk` endpoint to add multiple documents in one request. Bulk data
must be formatted as newline-delimited JSON (NDJSON).

```console
POST /_bulk
{ "index" : { "_index" : "books" } }
{"name": "Revelation Space", "author": "Alastair Reynolds", "release_date": "2000-03-15", "page_count": 585}
{ "index" : { "_index" : "books" } }
{"name": "1984", "author": "George Orwell", "release_date": "1985-06-01", "page_count": 328}
{ "index" : { "_index" : "books" } }
{"name": "Fahrenheit 451", "author": "Ray Bradbury", "release_date": "1953-10-15", "page_count": 227}
{ "index" : { "_index" : "books" } }
{"name": "Brave New World", "author": "Aldous Huxley", "release_date": "1932-06-01", "page_count": 268}
{ "index" : { "_index" : "books" } }
{"name": "The Handmaids Tale", "author": "Margaret Atwood", "release_date": "1985-06-01", "page_count": 311}
```

You should receive a response indicating there were no errors.

**Example response**
===============
```console-result
{
  "errors": false,
  "took": 29,
  "items": [
    {
      "index": {
        "_index": "books",
        "_id": "QklI2IsBaSa7VYx_Qkh-",
        "_version": 1,
        "result": "created",
        "_shards": {
          "total": 2,
          "successful": 2,
          "failed": 0
        },
        "_seq_no": 1,
        "_primary_term": 1,
        "status": 201
      }
    },
    {
      "index": {
        "_index": "books",
        "_id": "Q0lI2IsBaSa7VYx_Qkh-",
        "_version": 1,
        "result": "created",
        "_shards": {
          "total": 2,
          "successful": 2,
          "failed": 0
        },
        "_seq_no": 2,
        "_primary_term": 1,
        "status": 201
      }
    },
    {
      "index": {
        "_index": "books",
        "_id": "RElI2IsBaSa7VYx_Qkh-",
        "_version": 1,
        "result": "created",
        "_shards": {
          "total": 2,
          "successful": 2,
          "failed": 0
        },
        "_seq_no": 3,
        "_primary_term": 1,
        "status": 201
      }
    },
    {
      "index": {
        "_index": "books",
        "_id": "RUlI2IsBaSa7VYx_Qkh-",
        "_version": 1,
        "result": "created",
        "_shards": {
          "total": 2,
          "successful": 2,
          "failed": 0
        },
        "_seq_no": 4,
        "_primary_term": 1,
        "status": 201
      }
    },
    {
      "index": {
        "_index": "books",
        "_id": "RklI2IsBaSa7VYx_Qkh-",
        "_version": 1,
        "result": "created",
        "_shards": {
          "total": 2,
          "successful": 2,
          "failed": 0
        },
        "_seq_no": 5,
        "_primary_term": 1,
        "status": 201
      }
    }
  ]
}
```
===============

### Step 3: Define mappings and data types

Mappings define how data is stored and indexed in Elasticsearch, like a schema in a relational database.

#### Use dynamic mapping

When using dynamic mapping, Elasticsearch automatically creates mappings for new fields by default.
The documents we've added so far have used dynamic mapping, because we didn't specify a mapping when creating the index.

To see how dynamic mapping works, add a new document to the `books` index with a field that doesn't appear in the existing documents.

```console
POST /books/_doc
{
  "name": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "release_date": "1925-04-10",
  "page_count": 180,
  "language": "EN" <1>
}
```
<1> The new field.

View the mapping for the `books` index with the Get mapping API. The new field `language` has been added to the mapping with a `text` data type.

```console
GET /books/_mapping
```

**Example response**
===============
```console-result
{
  "books": {
    "mappings": {
      "properties": {
        "author": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "name": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "language": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "page_count": {
          "type": "long"
        },
        "release_date": {
          "type": "date"
        }
      }
    }
  }
}
```
===============

#### Define explicit mapping

Create an index named `my-explicit-mappings-books` with explicit mappings.
Pass each field's properties as a JSON object. This object should contain the field data type and any additional mapping parameters.

```console
PUT /my-explicit-mappings-books
{
  "mappings": {
    "dynamic": false,  <1>
    "properties": {  <2>
      "name": { "type": "text" },
      "author": { "type": "text" },
      "release_date": { "type": "date", "format": "yyyy-MM-dd" },
      "page_count": { "type": "integer" }
    }
  }
}
```
<1> Disables dynamic mapping for the index. Documents containing fields not defined in the mapping will be rejected.
<2> The `properties` object defines the fields and their data types for documents in this index.

**Example response**
===============
```console-result
{
  "acknowledged": true,
  "shards_acknowledged": true,
  "index": "my-explicit-mappings-books"
}
```
===============

#### Combine dynamic and explicit mappings

Explicit mappings are defined at index creation, and documents must conform to these mappings.
You can also use the Update mapping API.
When an index has the `dynamic` flag set to `true`, you can add new fields to documents without updating the mapping.

This allows you to combine explicit and dynamic mappings.
Learn more about managing and updating mappings.

### Step 4: Search your index

Indexed documents are available for search in near real-time, using the `_search` API.

#### Search all documents

Run the following command to search the `books` index for all documents:

```console
GET books/_search
```

**Example response**
===============
```console-result
{
  "took": 2, <1>
  "timed_out": false, <2>
  "_shards": { <3>
    "total": 5,
    "successful": 5,
    "skipped": 0,
    "failed": 0
  },
  "hits": { <4>
    "total": { <5>
      "value": 7,
      "relation": "eq"
    },
    "max_score": 1, <6>
    "hits": [
      {
        "_index": "books", <7>
        "_id": "CwICQpIBO6vvGGiC_3Ls", <8>
        "_score": 1, <9>
        "_source": { <10>
          "name": "Brave New World",
          "author": "Aldous Huxley",
          "release_date": "1932-06-01",
          "page_count": 268
        }
      },
      ... (truncated)
    ]
  }
}
```
<1> The `took` field indicates the time in milliseconds for Elasticsearch to execute the search
<2> The `timed_out` field indicates whether the search timed out
<3> The `_shards` field contains information about the number of shards that the search was executed on and the number that succeeded
<4> The `hits` object contains the search results
<5> The `total` object provides information about the total number of matching documents
<6> The `max_score` field indicates the highest relevance score among all matching documents
<7> The `_index` field indicates the index the document belongs to
<8> The `_id` field is the document's unique identifier
<9> The `_score` field indicates the relevance score of the document
<10> The `_source` field contains the original JSON object submitted during indexing
===============

#### `match` query

You can use the `match` query to search for documents that contain a specific value in a specific field.
This is the standard query for full-text searches.

Run the following command to search the `books` index for documents containing `brave` in the `name` field:

```console
GET books/_search
{
  "query": {
    "match": {
      "name": "brave"
    }
  }
}
```

**Example response**
===============
```console-result
{
  "took": 9,
  "timed_out": false,
  "_shards": {
    "total": 5,
    "successful": 5,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 1,
      "relation": "eq"
    },
    "max_score": 0.6931471, <1>
    "hits": [
      {
        "_index": "books",
        "_id": "CwICQpIBO6vvGGiC_3Ls",
        "_score": 0.6931471,
        "_source": {
          "name": "Brave New World",
          "author": "Aldous Huxley",
          "release_date": "1932-06-01",
          "page_count": 268
        }
      }
    ]
  }
}
```
<1> The `max_score` is the score of the highest-scoring document in the results. In this case, there is only one matching document, so the `max_score` is the score of that document.
===============

### Step 5: Delete your indices (optional)

When following along with examples, you might want to delete an index to start from scratch.
You can delete indices using the Delete index API.

For example, run the following command to delete the indices created in this tutorial:

```console
DELETE /books
DELETE /my-explicit-mappings-books
```

**Caution:**
Deleting an index permanently deletes its documents, shards, and metadata.
