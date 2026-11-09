<!-- Converted from core/indexes/index-types/index-text/text-index-versions.txt (reStructuredText). Includes are inlined. -->

# Text Index Versions on Self-Managed Deployments

Text indexes are available in the following versions:

| Text Index Version | Description |
|---|---|
| Version 3 | MongoDB 3.2 introduces version 3 of text indexes. Version 3 is the default version for text indexes created in MongoDB 3.2 and later. |
| Version 2 | MongoDB 2.6 introduces version 2 of text indexes. Version 2 is the default version for text indexes created in MongoDB 2.6 to 3.0. |
| Version 1 | MongoDB 2.4 introduces version 1 of text indexes. MongoDB 2.4 only supports version 1. |

## Change Index Version

**Important:**

Always use the default index version when possible. Only override the
default version if required for compatibility reasons.

To override the default version and specify a different version for your
text index, set the `textIndexVersion` option when you create an
index: 

```javascript
db.<collection>.createIndex( 
   { <field>: "text" }, 
   { "textIndexVersion": <version> } 
)
```

### Example

The following command creates a version 2 text index on the `content`
field:

```javascript
db.test.createIndex(
   { "content": "text" },
   { "textIndexVersion": 2 }
 )
```
