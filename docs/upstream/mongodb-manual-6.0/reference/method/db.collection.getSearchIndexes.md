<!-- Converted from reference/method/db.collection.getSearchIndexes.txt (reStructuredText). Includes are inlined. -->

# db.collection.getSearchIndexes()

## Definition

**`db.collection.getSearchIndexes()`**

**New in version:** 6.0.7

Returns information about existing Atlas Search indexes or Atlas Vector Search indexes on a specified
collection. 

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in serverless instances. For more information, 
see Unsupported Commands.

## Syntax

Command syntax:

```javascript
db.<collection>.getSearchIndexes(<indexName>)
```

## Command Fields

`getSearchIndexes()` takes this field:

| Field | Type | Necessity | Description |
|---|---|---|---|
| `indexName` | string | Optional | Name of the index to return information about. If you omit the `indexName` field, `getSearchIndexes()` returns information about all Atlas Search indexes on the collection. |

## Access Control

If your deployment enforces access control, the user running
`getSearchIndexes()` must have the `listSearchIndexes` privilege
action on the database or collection:

```javascript
{
   resource: {
      db : <database>,
      collection: <collection>
   },
   actions: [ "listSearchIndexes" ]
}
```

The built-in `read` role provides the the
`listSearchIndexes` privilege. The following example grants the
`read` role on the `qa` database:

```javascript
db.grantRolesToUser(
   "<user>",
   [ { role: "read", db: "qa" } ]
)
```

## Output

`getSearchIndexes()` returns an array of documents. Each document in the array
contains the following fields:

* - Field
  - Type
  - Description

* - `id`
  - string
  - Unique identifier for the index.

* - `name`
  - string
  - Name of the index.

* - `status`
  - string
  - Status of the index. For more information, see search-index-status.

* - `queryable`
  - boolean
  - Indicates whether the index is ready to be queried.

* - `latestDefinitionVersion`
  - document
  - Describes the version of the index.

* - `latestDefinitionVersion.version`
  - integer
  - Version number associated with the index definition. When you
    update an index definition, the version number increments
    automatically.

* - `latestDefinitionVersion.createdAt`
  - date
  - Time when the current index definition was created.

* - `latestDefinition`
  - document
  - The most recent definition for the index. For more information,
    see search-index-definition-create.

* - `statusDetail`
  - array of documents
  - Contains the status of the index on each search host
    (`mongot`).

* - `statusDetail.[n].hostname`
  - string
  - Hostname of the corresponding `mongot`.

* - `statusDetail.[n].status`
  - string
  - Status of the index on the corresponding `mongot`.

* - `statusDetail.[n].queryable`
  - boolean
  - Indicates whether the index is ready to be queried on the
    corresponding `mongot`.

* - `statusDetail.[n].mainIndex`
  - document
  - Contains status information about the active index on the
    corresponding `mongot`.

    For details, see search-index-details.

* - `statusDetail.[n].stagedIndex`
  - document
  - Contains status information about an index being built in the
    background on the corresponding `mongot`. This field only
    appears if you are building a new index to update an existing
    active index.

    For details, see search-index-details.

* - `synonymMappingStatus`
  - string
  - Status of the index's synonym mappings.
    This field only appears if the index has synonyms defined. Can be
    one of the following values:

    - `BUILDING`
    - `FAILED`
    - `READY`

    The returned status is a summary of the synonym mappings on each
    individual `mongot`.

* - `synonymMappingStatusDetail`
  - array of documents
  - Contains the status of the index's synonym mappings on each
    search host (`mongot`). This field (and its subfields) only
    appear if the index has synonyms defined.

* - `synonymMappingStatusDetail.[n].status`
  - string
  - Status for the corresponding synonym mapping across all
    `mongot` processes.

* - `synonymMappingStatusDetail.[n].queryable`
  - boolean
  - Indicates whether the corresponding synonym mapping can support
    queries across all `mongot` processes.

* - `message`
  - string
  - Describes an error for the synonym mapping, if applicable. Only
    appears if the `status` for this synonym mapping is `FAILED`.

### Index Status Details

The following table describes the embedded fields of the following
documents:
- `statusDetail.[mongot].mainIndex`
- `statusDetail.[mongot].stagedIndex`

The fields describe the index status on a specific `mongot`.

| Field | Type | Description |
|---|---|---|
| `status` | string | The state of the index generation on the corresponding `mongot`. |
| `queryable` | boolean | Indicates whether the index generation is ready to be queried on the corresponding `mongot`. |
| `synonymMappingStatus` | string | The state of the index generation's synonym mappings on the corresponding `mongot`. Only present if the index has synonyms defined. |
| `synonymMappingStatusDetails` | document | Contains the status of the index's synonym mappings on the corresponding `mongot`. This field (and its subfields) only appear if the index has synonyms defined. For more information, see search-mapping-details. |
| `definitionVersion` | document | Describes the index definition version that this index generation is being built with. |
| `definitionVersion.version` | integer | Version number that the index generation is using on the corresponding `mongot`. When you update an index definition, the updated index builds with an incremented version number. |
| `definitionVersion.createdAt` | date | Time when the index definition was created. |
| `definition` | document | The definition that this index is being built with. |

### Synonym Mapping Details

The following table describes the embedded fields of the following
objects:

- `statusDetail.mainIndex.synonymMappingStatusDetails.<synonymMapping>`
- `statusDetail.stagedIndex.synonymMappingStatusDetails<synonymMapping>`

| Field | Type | Description |
|---|---|---|
| `status` | string | Status for the synonym mapping across on the corresponding `mongot` process. |
| `queryable` | boolean | Indicates whether the synonym mapping can support queries on the corresponding `mongot` process. |
| `message` | string | Describes an error for the synonym mapping, if applicable. Only appears if the `status` for this synonym mapping is `FAILED`. |

### Atlas Search Index Statuses

The `status` field in the `getSearchIndexes()` output can be one of the
following:

* - Status
  - Description

* - `BUILDING`
  - The following scenarios can cause an index to be in the
    `BUILDING` state:

    - Atlas is building the index or re-building the index after an
      edit.

    - Atlas Search cannot keep up with indexing changes to the
      collection. In this case, Atlas rebuilds the index in the
      background.

    When the index is in the `BUILDING` state:

    - For a new index, Atlas Search cannot use the index for queries
      until the index build is complete.

    - For an existing index, Atlas Search uses the old index
      definition for queries until the index rebuild is complete.

    An index in the `BUILDING` state may be queryable or
    non-queryable. 

* - `DOES_NOT_EXIST`
  - The index does not exist. 

    An index in the `DOES_NOT_EXIST` state is always non-queryable. 

* - `DELETING`
  - Atlas is deleting the index.

    An index in the `DELETING` state is always non-queryable. 

* - `FAILED`
  - The index build failed. Indexes can enter the `FAILED` state
    due to an invalid index definition.

    An index in the `FAILED` state may be queryable or
    non-queryable. 

* - `PENDING`
  - Atlas has not yet started building the index.

    An index in the `PENDING` state is always non-queryable. 

* - `READY`
  - The index is ready and can support queries.

    An index in the `READY` state is always queryable. 

* - `STALE`
  - The index is queryable but has stopped replicating data from the
    indexed collection. Searches on the index may return out-of-date
    data.

    Indexes can enter the `STALE` state due to replication errors.

    An index in the `STALE` state is always queryable. 

## Examples

These examples demonstrate how to:

- getSearchIndexes-return-all

- getSearchIndexes-return-one

### Return All Search Indexes

The following example returns all Atlas Search indexes on the `movies`
collection. The `movies` collection contains two search indexes:
`default` and `synonym_mappings`.

```javascript
db.movies.getSearchIndexes()
```

Sample output:

```javascript
[
  {
    id: '6524096020da840844a4c4a7',
    name: 'default',
    status: 'BUILDING',
    queryable: true,
    latestDefinitionVersion: {
      version: 2,
      createdAt: ISODate("2023-10-09T14:51:57.355Z")
    },
    latestDefinition: {
      mappings: { dynamic: true },
      storedSource: { include: [ 'awards.text' ] }
    },
    statusDetail: [
      {
        hostname: 'atlas-n1cm1j-shard-00-02',
        status: 'BUILDING',
        queryable: true,
        mainIndex: {
          status: 'READY',
          queryable: true,
          definitionVersion: {
            version: 0,
            createdAt: ISODate("2023-10-09T14:08:32.000Z")
          },
          definition: { mappings: { dynamic: true, fields: {} } }
        },
        stagedIndex: {
          status: 'PENDING',
          queryable: false,
          definitionVersion: {
            version: 1,
            createdAt: ISODate("2023-10-09T14:51:29.000Z")
          },
          definition: {
            mappings: { dynamic: true, fields: {} },
            storedSource: true
          }
        }
      },
      {
        hostname: 'atlas-n1cm1j-shard-00-01',
        status: 'BUILDING',
        queryable: true,
        mainIndex: {
          status: 'READY',
          queryable: true,
          definitionVersion: {
            version: 0,
            createdAt: ISODate("2023-10-09T14:08:32.000Z")
          },
          definition: { mappings: { dynamic: true, fields: {} } }
        },
        stagedIndex: {
          status: 'PENDING',
          queryable: false,
          definitionVersion: {
            version: 1,
            createdAt: ISODate("2023-10-09T14:51:29.000Z")
          },
          definition: {
            mappings: { dynamic: true, fields: {} },
            storedSource: true
          }
        }
      },
      {
        hostname: 'atlas-n1cm1j-shard-00-00',
        status: 'BUILDING',
        queryable: true,
        mainIndex: {
          status: 'READY',
          queryable: true,
          definitionVersion: {
            version: 0,
            createdAt: ISODate("2023-10-09T14:08:32.000Z")
          },
          definition: { mappings: { dynamic: true, fields: {} } }
        }
      }
    ]
  },
  {
    id: '65240be420da840844a4d077',
    name: 'synonym_mappings',
    status: 'READY',
    queryable: true,
    latestDefinitionVersion: {
      version: 0,
      createdAt: ISODate("2023-10-09T14:19:16.305Z")
    },
    latestDefinition: {
      mappings: {
        dynamic: true,
        fields: {
          fullplot: { type: 'string' }
        }
      },
      synonyms: [
        {
          name: 'synonym_mapping',
          analyzer: 'lucene.english',
          source: { collection: 'synonyms' }
        }
      ]
    },
    synonymMappingStatus: 'READY',
    synonymMappingStatusDetail: [
      {
        synonym_mapping: {
          status: 'READY',
          queryable: true
        }
      }
    ],
    statusDetail: [
      {
        hostname: 'atlas-n1cm1j-shard-00-02',
        status: 'READY',
        queryable: true,
        mainIndex: {
          status: 'READY',
          queryable: true,
          definitionVersion: {
            version: 0,
            createdAt: ISODate("2023-10-09T14:19:16.000Z")
          },
          definition: {
            mappings: {
              dynamic: true,
              fields: {
                fullplot: {
                  type: 'string',
                  indexOptions: 'offsets',
                  store: true,
                  norms: 'include'
                }
              }
            },
            synonyms: [
              {
                name: 'synonym_mapping',
                analyzer: 'lucene.english',
                source: { collection: 'synonyms' }
              }
            ]
          },
          synonymMappingStatus: 'READY',
          synonymMappingStatusDetail: [
            {
              synonym_mapping: {
                status: 'READY',
                queryable: true
              }
            }
          ]
        }
      },
      {
        hostname: 'atlas-n1cm1j-shard-00-01',
        status: 'READY',
        queryable: true,
        mainIndex: {
          status: 'READY',
          queryable: true,
          definitionVersion: {
            version: 0,
            createdAt: ISODate("2023-10-09T14:19:16.000Z")
          },
          definition: {
            mappings: {
              dynamic: true,
              fields: {
                fullplot: {
                  type: 'string',
                  indexOptions: 'offsets',
                  store: true,
                  norms: 'include'
                }
              }
            },
            synonyms: [
              {
                name: 'synonym_mapping',
                analyzer: 'lucene.english',
                source: { collection: 'synonyms' }
              }
            ]
          },
          synonymMappingStatus: 'READY',
          synonymMappingStatusDetail: [
            {
              synonym_mapping: {
                status: 'READY',
                queryable: true
              }
            }
          ]
        }
      },
      {
        hostname: 'atlas-n1cm1j-shard-00-00',
        status: 'READY',
        queryable: true,
        mainIndex: {
          status: 'READY',
          queryable: true,
          definitionVersion: {
            version: 0,
            createdAt: ISODate("2023-10-09T14:19:16.000Z")
          },
          definition: {
            mappings: {
              dynamic: true,
              fields: {
                fullplot: {
                  type: 'string',
                  indexOptions: 'offsets',
                  store: true,
                  norms: 'include'
                }
              }
            },
            synonyms: [
              {
                name: 'synonym_mapping',
                analyzer: 'lucene.english',
                source: { collection: 'synonyms' }
              }
            ]
          },
          synonymMappingStatus: 'READY',
          synonymMappingStatusDetail: [
            {
              synonym_mapping: {
                status: 'READY',
                queryable: true
              }
            }
          ]
        }
      }
    ]
  }
]
```

### Return a Single Search Index

The following example returns the `synonym_mappings` index on the
`movies` collection:

```javascript
db.movies.getSearchIndexes("synonym_mappings")
```

Sample output:

```javascript
[
  {
    id: '65240be420da840844a4d077',
    name: 'synonym_mappings',
    status: 'READY',
    queryable: true,
    latestDefinitionVersion: {
      version: 0,
      createdAt: ISODate("2023-10-09T14:19:16.305Z")
    },
    latestDefinition: {
      mappings: {
        dynamic: true,
        fields: {
          fullplot: { type: 'string' }
        }
      },
      synonyms: [
        {
          name: 'synonym_mapping',
          analyzer: 'lucene.english',
          source: { collection: 'synonyms' }
        }
      ]
    },
    synonymMappingStatus: 'READY',
    synonymMappingStatusDetail: [
      {
        synonym_mapping: {
          status: 'READY',
          queryable: true
        }
      }
    ],
    statusDetail: [
      {
        hostname: 'atlas-n1cm1j-shard-00-02',
        status: 'READY',
        queryable: true,
        mainIndex: {
          status: 'READY',
          queryable: true,
          definitionVersion: {
            version: 0,
            createdAt: ISODate("2023-10-09T14:19:16.000Z")
          },
          definition: {
            mappings: {
              dynamic: true,
              fields: {
                fullplot: {
                  type: 'string',
                  indexOptions: 'offsets',
                  store: true,
                  norms: 'include'
                }
              }
            },
            synonyms: [
              {
                name: 'synonym_mapping',
                analyzer: 'lucene.english',
                source: { collection: 'synonyms' }
              }
            ]
          },
          synonymMappingStatus: 'READY',
          synonymMappingStatusDetail: [
            {
              synonym_mapping: {
                status: 'READY',
                queryable: true
              }
            }
          ]
        }
      },
      {
        hostname: 'atlas-n1cm1j-shard-00-01',
        status: 'READY',
        queryable: true,
        mainIndex: {
          status: 'READY',
          queryable: true,
          definitionVersion: {
            version: 0,
            createdAt: ISODate("2023-10-09T14:19:16.000Z")
          },
          definition: {
            mappings: {
              dynamic: true,
              fields: {
                fullplot: {
                  type: 'string',
                  indexOptions: 'offsets',
                  store: true,
                  norms: 'include'
                }
              }
            },
            synonyms: [
              {
                name: 'synonym_mapping',
                analyzer: 'lucene.english',
                source: { collection: 'synonyms' }
              }
            ]
          },
          synonymMappingStatus: 'READY',
          synonymMappingStatusDetail: [
            {
              synonym_mapping: {
                status: 'READY',
                queryable: true
              }
            }
          ]
        }
      },
      {
        hostname: 'atlas-n1cm1j-shard-00-00',
        status: 'READY',
        queryable: true,
        mainIndex: {
          status: 'READY',
          queryable: true,
          definitionVersion: {
            version: 0,
            createdAt: ISODate("2023-10-09T14:19:16.000Z")
          },
          definition: {
            mappings: {
              dynamic: true,
              fields: {
                fullplot: {
                  type: 'string',
                  indexOptions: 'offsets',
                  store: true,
                  norms: 'include'
                }
              }
            },
            synonyms: [
              {
                name: 'synonym_mapping',
                analyzer: 'lucene.english',
                source: { collection: 'synonyms' }
              }
            ]
          },
          synonymMappingStatus: 'READY',
          synonymMappingStatusDetail: [
            {
              synonym_mapping: {
                status: 'READY',
                queryable: true
              }
            }
          ]
        }
      }
    ]
  }
]
```
