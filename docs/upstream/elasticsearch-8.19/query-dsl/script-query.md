<!-- Converted from query-dsl/script-query.asciidoc (AsciiDoc). Includes are inlined. -->

### Script query

**Note:** Runtime fields provide a very similar feature that is
      more flexible. You write a script to create field values and they
      are available everywhere, such as `fields`,
      all queries, and aggregations.

Filters documents based on a provided script. The
`script` query is typically used in a filter context.

**Warning:** Using scripts can result in slower search speeds. See
scripts-and-search-speed.

#### Example request

```console
GET /_search
{
  "query": {
    "bool": {
      "filter": {
        "script": {
          "script": """
            double amount = doc['amount'].value;
            if (doc['type'].value == 'expense') {
              amount *= -1;
            }
            return amount < 10;
          """
        }
      }
    }
  }
}
```

You can achieve the same results in a search
query by using runtime fields. Use the
`fields` parameter on the 
`_search` API to fetch values as part of the
same query:

```console
GET /_search
{
  "runtime_mappings": {
    "amount.signed": {
      "type": "double",
      "script": """
        double amount = doc['amount'].value;
        if (doc['type'].value == 'expense') {
          amount *= -1;
        }
        emit(amount);
      """
    }
  },
  "query": {
    "bool": {
      "filter": {
        "range": {
          "amount.signed": { "lt": 10 }
        }
      }
    }
  },
  "fields": [{"field": "amount.signed"}]
}
```

#### Top-level parameters for `script`

`script`::
(Required, script object) Contains a script to run
as a query. This script must return a boolean value, `true` or `false`.

#### Notes

##### Custom Parameters

Like filters, scripts are cached for faster execution.
If you frequently change the arguments of a script, we recommend you store them
in the script's `params` parameter. For example:

```console
GET /_search
{
  "query": {
    "bool": {
      "filter": {
        "script": {
          "script": {
            "source": "doc['num1'].value > params.param1",
            "lang": "painless",
            "params": {
              "param1": 5
            }
          }
        }
      }
    }
  }
}
```

##### Allow expensive queries

Script queries will not be executed if `search.allow_expensive_queries`
is set to false.
