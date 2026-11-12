<!-- Converted from management/connectors/action-types/index.asciidoc (AsciiDoc). Includes are inlined. -->

## Index connector and action

An index connector indexes a document into Elasticsearch.

### Create connectors in Kibana

You can create connectors in *{stack-manage-app} > {connectors-ui}*
or as needed when you're creating a rule. For example:

(Figure: management/connectors/images/index-connector.png)

#### Connector configuration

Index connectors must have a name and an Elasticsearch index.
You can optionally choose a field that indicates when the document was indexed.

### Test connectors

You can test connectors as you're creating or editing the connector in Kibana. For example:

(Figure: management/connectors/images/index-params-test.png)

Index connector actions contain a document in JSON format. For example, if you
have an index with the following properties:

```text
PUT test
{
    "settings" : {
        "number_of_shards" : 1
    },
    "mappings" : {
        "properties" : {
            "rule_id" : { "type" : "text" },
            "rule_name" : { "type" : "text" },
            "alert_id" : { "type" : "text" },
            "context_message": { "type" : "text" }
        }
    }
}
```

Your test document could contain the following properties and variables:

```text
{
    "rule_id": "{{rule.id}}",
    "rule_name": "{{rule.name}}",
    "alert_id": "{{alert.id}}",
    "context_message": "{{context.message}}"
}
```
