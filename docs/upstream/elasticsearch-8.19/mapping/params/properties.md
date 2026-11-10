<!-- Converted from mapping/params/properties.asciidoc (AsciiDoc). Includes are inlined. -->

### `properties`

Type mappings, `object` fields and `nested` fields
contain sub-fields, called `properties`. These properties may be of any
data type, including `object` and `nested`. Properties can
be added:

* explicitly by defining them when creating an index.
* explicitly by defining them when adding or updating a mapping type with the update mapping API.
* dynamically just by indexing documents containing new fields.

Below is an example of adding `properties` to a mapping type, an `object`
field, and a `nested` field:

```console
PUT my-index-000001
{
  "mappings": {
    "properties": { <1>
      "manager": {
        "properties": { <2>
          "age":  { "type": "integer" },
          "name": { "type": "text"  }
        }
      },
      "employees": {
        "type": "nested",
        "properties": { <3>
          "age":  { "type": "integer" },
          "name": { "type": "text"  }
        }
      }
    }
  }
}

PUT my-index-000001/_doc/1 <4>
{
  "region": "US",
  "manager": {
    "name": "Alice White",
    "age": 30
  },
  "employees": [
    {
      "name": "John Smith",
      "age": 34
    },
    {
      "name": "Peter Brown",
      "age": 26
    }
  ]
}
```

<1> Properties in the top-level mappings definition.
<2> Properties under the `manager` object field.
<3> Properties under the `employees` nested field.
<4> An example document which corresponds to the above mapping.

**Tip:** The `properties` setting is allowed to have different settings for fields
of the same name in the same index. New properties can be added to existing
fields using the update mapping API.

#### Dot notation

Inner fields can be referred to in queries, aggregations, etc., using _dot
notation_:

```console
GET my-index-000001/_search
{
  "query": {
    "match": {
      "manager.name": "Alice White" 
    }
  },
  "aggs": {
    "Employees": {
      "nested": {
        "path": "employees"
      },
      "aggs": {
        "Employee Ages": {
          "histogram": {
            "field": "employees.age", 
            "interval": 5
          }
        }
      }
    }
  }
}
```

**Important:** The full path to the inner field must be specified.
