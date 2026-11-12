<!-- Part 3 of 4 of tutorial/remove-documents.md (split because the page is big). -->

[ <field1> => <value1>, ... ]
            ```

        - id: ruby
          content: |
            To specify equality conditions, use `<field> => <value>`
            expressions in the
            query filter document:

            ```ruby
            { <field1> => <value1>, ... }
            ```

        - id: scala
          content: |
            To specify equality conditions, use the
            `com.mongodb.client.model.Filters.eq_` method to create the
            query filter document:

            ```scala
            and(equal(<field1>, <value1>), equal(<field2>, <value2>) ...)
            ```

        - id: csharp
          content: |
            To specify equality conditions, construct a filter using the
            `Eq` method:

            ```csharp
            Builders<BsonDocument>.Filter.Eq(<field>, <value>);
            ```

      tabs:
        - id: shell
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```javascript
            { <field1>: { <operator1>: <value1> }, ... }
            ```

        - id: compass
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```javascript
            { <field1>: { <operator1>: <value1> }, ... }
            ```

        - id: python
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```python
            { <field1>: { <operator1>: <value1> }, ... }
            ```

        - id: motor
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```python
            { <field1>: { <operator1>: <value1> }, ... }
            ```

        - id: java-sync
          content: |

            In addition to the equality condition, MongoDB provides
            various query operators to specify
            filter conditions. Use the
            com.mongodb.client.model.Filters_ helper methods to
            facilitate the creation of filter documents. For example:

            ```java
            and(gte(<field1>, <value1>), lt(<field2>, <value2>), eq(<field3>, <value3>))
            ```

        - id: java-async
          content: |

            In addition to the equality condition, MongoDB provides
            various query operators to specify
            filter conditions. Use the
            com.mongodb.client.model.Filters_ helper methods to
            facilitate the creation of filter documents. For example:

            ```java
            and(gte(<field1>, <value1>), lt(<field2>, <value2>), eq(<field3>, <value3>))
            ```

        - id: nodejs
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```javascript
            { <field1>: { <operator1>: <value1> }, ... }
            ```

        - id: php
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```php
            [ <field1> => [ <operator1> => <value1> ], ... ]
            ```

        - id: perl
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```perl
            { <field1> => { <operator1> => <value1> }, ... }
            ```

        - id: ruby
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```ruby
            { <field1> => { <operator1> => <value1> }, ... }
            ```

        - id: scala
          content: |

            In addition to the equality condition, MongoDB provides
            various query operators to specify
            filter conditions. Use the
            `com.mongodb.client.model.Filters_` helper methods to
            facilitate the creation of filter documents. For example:

            ```scala
            and(gte(<field1>, <value1>), lt(<field2>, <value2>), equal(<field3>, <value3>))
            ```

        - id: csharp
          content: |
            In addition to the equality filter, MongoDB provides
            various query operators to specify
            filter conditions. Use the
            `FilterDefinitionBuilder`
            methods to create a filter document. For example:

            ```csharp
            var builder = Builders<BsonDocument>.Filter;
            builder.And(builder.Eq(<field1>, <value1>), builder.Lt(<field2>, <value2>));
            ```

      To delete all documents that match a deletion criteria, pass a
      filter parameter to the
      `deleteMany()`
      method.

      The following example removes all documents from the `inventory`
      collection where the `status` field equals `"A"`:

  - id: php
    content: |

      You can specify criteria, or filters, that identify the documents to
      delete. The filters use the same syntax
      as read operations.

      tabs:
        - id: shell
          content: |
            To specify equality conditions, use `<field>:<value>`
            expressions in the
            query filter document:

            ```javascript
            { <field1>: <value1>, ... }
            ```

        - id: compass
          content: |
            To specify equality conditions, use `<field>:<value>`
            expressions in the
            query filter document:

            ```javascript
            { <field1>: <value1>, ... }
            ```

        - id: python
          content: |
            To specify equality conditions, use `<field>:<value>`
            expressions in the
            query filter document:

            ```python
            { <field1>: <value1>, ... }
            ```

        - id: motor
          content: |
            To specify equality conditions, use `<field>:<value>`
            expressions in the
            query filter document:

            ```python
            { <field1>: <value1>, ... }
            ```

        - id: java-sync
          content: |
            To specify equality conditions, use the
            `com.mongodb.client.model.Filters.eq_` method to create the
            query filter document:

            ```java
            and(eq( <field1>, <value1>), eq( <field2>, <value2>) ...)
            ```

        - id: java-async
          content: |
            To specify equality conditions, use the
            com.mongodb.client.model.Filters.eq_ method to create the
            query filter document:

            ```java
            and(eq( <field1>, <value1>), eq( <field2>, <value2>) ...)
            ```

        - id: nodejs
          content: |
            To specify equality conditions, use `<field>:<value>`
            expressions in the
            query filter document:

            ```javascript
            { <field1>: <value1>, ... }
            ```

        - id: php
          content: |
            To specify equality conditions, use `<field> => <value>`
            expressions in the
            query filter document:

            ```php
            [ <field1> => <value1>, ... ]
            ```

        - id: ruby
          content: |
            To specify equality conditions, use `<field> => <value>`
            expressions in the
            query filter document:

            ```ruby
            { <field1> => <value1>, ... }
            ```

        - id: scala
          content: |
            To specify equality conditions, use the
            `com.mongodb.client.model.Filters.eq_` method to create the
            query filter document:

            ```scala
            and(equal(<field1>, <value1>), equal(<field2>, <value2>) ...)
            ```

        - id: csharp
          content: |
            To specify equality conditions, construct a filter using the
            `Eq` method:

            ```csharp
            Builders<BsonDocument>.Filter.Eq(<field>, <value>);
            ```

      tabs:
        - id: shell
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```javascript
            { <field1>: { <operator1>: <value1> }, ... }
            ```

        - id: compass
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```javascript
            { <field1>: { <operator1>: <value1> }, ... }
            ```

        - id: python
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```python
            { <field1>: { <operator1>: <value1> }, ... }
            ```

        - id: motor
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```python
            { <field1>: { <operator1>: <value1> }, ... }
            ```

        - id: java-sync
          content: |

            In addition to the equality condition, MongoDB provides
            various query operators to specify
            filter conditions. Use the
            com.mongodb.client.model.Filters_ helper methods to
            facilitate the creation of filter documents. For example:

            ```java
            and(gte(<field1>, <value1>), lt(<field2>, <value2>), eq(<field3>, <value3>))
            ```

        - id: java-async
          content: |

            In addition to the equality condition, MongoDB provides
            various query operators to specify
            filter conditions. Use the
            com.mongodb.client.model.Filters_ helper methods to
            facilitate the creation of filter documents. For example:

            ```java
            and(gte(<field1>, <value1>), lt(<field2>, <value2>), eq(<field3>, <value3>))
            ```

        - id: nodejs
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```javascript
            { <field1>: { <operator1>: <value1> }, ... }
            ```

        - id: php
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```php
            [ <field1> => [ <operator1> => <value1> ], ... ]
            ```

        - id: perl
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```perl
            { <field1> => { <operator1> => <value1> }, ... }
            ```

        - id: ruby
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```ruby
            { <field1> => { <operator1> => <value1> }, ... }
            ```

        - id: scala
          content: |

            In addition to the equality condition, MongoDB provides
            various query operators to specify
            filter conditions. Use the
            `com.mongodb.client.model.Filters_` helper methods to
            facilitate the creation of filter documents. For example:

            ```scala
            and(gte(<field1>, <value1>), lt(<field2>, <value2>), equal(<field3>, <value3>))
            ```

        - id: csharp
          content: |
            In addition to the equality filter, MongoDB provides
            various query operators to specify
            filter conditions. Use the
            `FilterDefinitionBuilder`
            methods to create a filter document. For example:

            ```csharp
            var builder = Builders<BsonDocument>.Filter;
            builder.And(builder.Eq(<field1>, <value1>), builder.Lt(<field2>, <value2>));
            ```

      To delete all documents that match a deletion criteria, pass a
      filter parameter to the
      `deleteMany()`
      method.

      The following example removes all documents from the `inventory`
      collection where the `status` field equals `"A"`:

  - id: ruby
    content: |

      You can specify criteria, or filters, that identify the documents to
      delete. The filters use the same syntax
      as read operations.

      tabs:
        - id: shell
          content: |
            To specify equality conditions, use `<field>:<value>`
            expressions in the
            query filter document:

            ```javascript
            { <field1>: <value1>, ... }
            ```

        - id: compass
          content: |
            To specify equality conditions, use `<field>:<value>`
            expressions in the
            query filter document:

            ```javascript
            { <field1>: <value1>, ... }
            ```

        - id: python
          content: |
            To specify equality conditions, use `<field>:<value>`
            expressions in the
            query filter document:

            ```python
            { <field1>: <value1>, ... }
            ```

        - id: motor
          content: |
            To specify equality conditions, use `<field>:<value>`
            expressions in the
            query filter document:

            ```python
            { <field1>: <value1>, ... }
            ```

        - id: java-sync
          content: |
            To specify equality conditions, use the
            `com.mongodb.client.model.Filters.eq_` method to create the
            query filter document:

            ```java
            and(eq( <field1>, <value1>), eq( <field2>, <value2>) ...)
            ```

        - id: java-async
          content: |
            To specify equality conditions, use the
            com.mongodb.client.model.Filters.eq_ method to create the
            query filter document:

            ```java
            and(eq( <field1>, <value1>), eq( <field2>, <value2>) ...)
            ```

        - id: nodejs
          content: |
            To specify equality conditions, use `<field>:<value>`
            expressions in the
            query filter document:

            ```javascript
            { <field1>: <value1>, ... }
            ```

        - id: php
          content: |
            To specify equality conditions, use `<field> => <value>`
            expressions in the
            query filter document:

            ```php
            [ <field1> => <value1>, ... ]
            ```

        - id: ruby
          content: |
            To specify equality conditions, use `<field> => <value>`
            expressions in the
            query filter document:

            ```ruby
            { <field1> => <value1>, ... }
            ```

        - id: scala
          content: |
            To specify equality conditions, use the
            `com.mongodb.client.model.Filters.eq_` method to create the
            query filter document:

            ```scala
            and(equal(<field1>, <value1>), equal(<field2>, <value2>) ...)
            ```

        - id: csharp
          content: |
            To specify equality conditions, construct a filter using the
            `Eq` method:

            ```csharp
            Builders<BsonDocument>.Filter.Eq(<field>, <value>);
            ```

      tabs:
        - id: shell
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```javascript
            { <field1>: { <operator1>: <value1> }, ... }
            ```

        - id: compass
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```javascript
            { <field1>: { <operator1>: <value1> }, ... }
            ```

        - id: python
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```python
            { <field1>: { <operator1>: <value1> }, ... }
            ```

        - id: motor
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```python
            { <field1>: { <operator1>: <value1> }, ... }
            ```

        - id: java-sync
          content: |

            In addition to the equality condition, MongoDB provides
            various query operators to specify
            filter conditions. Use the
            com.mongodb.client.model.Filters_ helper methods to
            facilitate the creation of filter documents. For example:

            ```java
            and(gte(<field1>, <value1>), lt(<field2>, <value2>), eq(<field3>, <value3>))
            ```

        - id: java-async
          content: |

            In addition to the equality condition, MongoDB provides
            various query operators to specify
            filter conditions. Use the
            com.mongodb.client.model.Filters_ helper methods to
            facilitate the creation of filter documents. For example:

            ```java
            and(gte(<field1>, <value1>), lt(<field2>, <value2>), eq(<field3>, <value3>))
            ```

        - id: nodejs
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```javascript
            { <field1>: { <operator1>: <value1> }, ... }
            ```

        - id: php
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```php
            [ <field1> => [ <operator1> => <value1> ], ... ]
            ```

        - id: perl
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```perl
            { <field1> => { <operator1> => <value1> }, ... }
            ```

        - id: ruby
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```ruby
            { <field1> => { <operator1> => <value1> }, ... }
            ```

        - id: scala
          content: |

            In addition to the equality condition, MongoDB provides
            various query operators to specify
            filter conditions. Use the
            `com.mongodb.client.model.Filters_` helper methods to
            facilitate the creation of filter documents. For example:

            ```scala
            and(gte(<field1>, <value1>), lt(<field2>, <value2>), equal(<field3>, <value3>))
            ```

        - id: csharp
          content: |
            In addition to the equality filter, MongoDB provides
            various query operators to specify
            filter conditions. Use the
            `FilterDefinitionBuilder`
            methods to create a filter document. For example:

            ```csharp
            var builder = Builders<BsonDocument>.Filter;
            builder.And(builder.Eq(<field1>, <value1>), builder.Lt(<field2>, <value2>));
            ```

      To delete all documents that match a deletion criteria, pass a
      filter parameter to the
      `delete_many()`
      method.

      The following example removes all documents from the `inventory`
      collection where the `status` field equals `"A"`:

  - id: scala
    content: |

      You can specify criteria, or filters, that identify the documents to
      delete. The filters use the same syntax
      as read operations.

      tabs:
        - id: shell
          content: |
            To specify equality conditions, use `<field>:<value>`
            expressions in the
            query filter document:

            ```javascript
            { <field1>: <value1>, ... }
            ```

        - id: compass
          content: |
            To specify equality conditions, use `<field>:<value>`
            expressions in the
            query filter document:

            ```javascript
            { <field1>: <value1>, ... }
            ```

        - id: python
          content: |
            To specify equality conditions, use `<field>:<value>`
            expressions in the
            query filter document:

            ```python
            { <field1>: <value1>, ... }
            ```

        - id: motor
          content: |
            To specify equality conditions, use `<field>:<value>`
            expressions in the
            query filter document:

            ```python
            { <field1>: <value1>, ... }
            ```

        - id: java-sync
          content: |
            To specify equality conditions, use the
            `com.mongodb.client.model.Filters.eq_` method to create the
            query filter document:

            ```java
            and(eq( <field1>, <value1>), eq( <field2>, <value2>) ...)
            ```

        - id: java-async
          content: |
            To specify equality conditions, use the
            com.mongodb.client.model.Filters.eq_ method to create the
            query filter document:

            ```java
            and(eq( <field1>, <value1>), eq( <field2>, <value2>) ...)
            ```

        - id: nodejs
          content: |
            To specify equality conditions, use `<field>:<value>`
            expressions in the
            query filter document:

            ```javascript
            { <field1>: <value1>, ... }
            ```

        - id: php
          content: |
            To specify equality conditions, use `<field> => <value>`
            expressions in the
            query filter document:

            ```php
            [ <field1> => <value1>, ... ]
            ```

        - id: ruby
          content: |
            To specify equality conditions, use `<field> => <value>`
            expressions in the
            query filter document:

            ```ruby
            { <field1> => <value1>, ... }
            ```

        - id: scala
          content: |
            To specify equality conditions, use the
            `com.mongodb.client.model.Filters.eq_` method to create the
            query filter document:

            ```scala
            and(equal(<field1>, <value1>), equal(<field2>, <value2>) ...)
            ```

        - id: csharp
          content: |
            To specify equality conditions, construct a filter using the
            `Eq` method:

            ```csharp
            Builders<BsonDocument>.Filter.Eq(<field>, <value>);
            ```

      tabs:
        - id: shell
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```javascript
            { <field1>: { <operator1>: <value1> }, ... }
            ```

        - id: compass
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```javascript
            { <field1>: { <operator1>: <value1> }, ... }
            ```

        - id: python
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```python
            { <field1>: { <operator1>: <value1> }, ... }
            ```

        - id: motor
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```python
            { <field1>: { <operator1>: <value1> }, ... }
            ```

        - id: java-sync
          content: |

            In addition to the equality condition, MongoDB provides
            various query operators to specify
            filter conditions. Use the
            com.mongodb.client.model.Filters_ helper methods to
            facilitate the creation of filter documents. For example:

            ```java
            and(gte(<field1>, <value1>), lt(<field2>, <value2>), eq(<field3>, <value3>))
            ```

        - id: java-async
          content: |

            In addition to the equality condition, MongoDB provides
            various query operators to specify
            filter conditions. Use the
            com.mongodb.client.model.Filters_ helper methods to
            facilitate the creation of filter documents. For example:

            ```java
            and(gte(<field1>, <value1>), lt(<field2>, <value2>), eq(<field3>, <value3>))
            ```

        - id: nodejs
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```javascript
            { <field1>: { <operator1>: <value1> }, ... }
            ```

        - id: php
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```php
            [ <field1> => [ <operator1> => <value1> ], ... ]
            ```

        - id: perl
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```perl
            { <field1> => { <operator1> => <value1> }, ... }
            ```

        - id: ruby
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```ruby
            { <field1> => { <operator1> => <value1> }, ... }
            ```

        - id: scala
          content: |

            In addition to the equality condition, MongoDB provides
            various query operators to specify
            filter conditions. Use the
            `com.mongodb.client.model.Filters_` helper methods to
            facilitate the creation of filter documents. For example:

            ```scala
            and(gte(<field1>, <value1>), lt(<field2>, <value2>), equal(<field3>, <value3>))
            ```

        - id: csharp
          content: |
            In addition to the equality filter, MongoDB provides
            various query operators to specify
            filter conditions. Use the
            `FilterDefinitionBuilder`
            methods to create a filter document. For example:

            ```csharp
            var builder = Builders<BsonDocument>.Filter;
            builder.And(builder.Eq(<field1>, <value1>), builder.Lt(<field2>, <value2>));
            ```

      To delete all documents that match a deletion criteria, pass a
      filter parameter to the
      `deleteMany()`
      method.

      The following example removes all documents from the `inventory`
      collection where the `status` field equals `"A"`:

  - id: csharp
    content: |

      You can specify criteria, or filters, that identify the documents to
      delete. The filters use the same syntax
      as read operations.

      tabs:
        - id: shell
          content: |
            To specify equality conditions, use `<field>:<value>`
            expressions in the
            query filter document:

            ```javascript
            { <field1>: <value1>, ... }
            ```

        - id: compass
          content: |
            To specify equality conditions, use `<field>:<value>`
            expressions in the
            query filter document:

            ```javascript
            { <field1>: <value1>, ... }
            ```

        - id: python
          content: |
            To specify equality conditions, use `<field>:<value>`
            expressions in the
            query filter document:

            ```python
            { <field1>: <value1>, ... }
            ```

        - id: motor
          content: |
            To specify equality conditions, use `<field>:<value>`
            expressions in the
            query filter document:

            ```python
            { <field1>: <value1>, ... }
            ```

        - id: java-sync
          content: |
            To specify equality conditions, use the
            `com.mongodb.client.model.Filters.eq_` method to create the
            query filter document:

            ```java
            and(eq( <field1>, <value1>), eq( <field2>, <value2>) ...)
            ```

        - id: java-async
          content: |
            To specify equality conditions, use the
            com.mongodb.client.model.Filters.eq_ method to create the
            query filter document:

            ```java
            and(eq( <field1>, <value1>), eq( <field2>, <value2>) ...)
            ```

        - id: nodejs
          content: |
            To specify equality conditions, use `<field>:<value>`
            expressions in the
            query filter document:

            ```javascript
            { <field1>: <value1>, ... }
            ```

        - id: php
          content: |
            To specify equality conditions, use `<field> => <value>`
            expressions in the
            query filter document:

            ```php
            [ <field1> => <value1>, ... ]
            ```

        - id: ruby
          content: |
            To specify equality conditions, use `<field> => <value>`
            expressions in the
            query filter document:

            ```ruby
            { <field1> => <value1>, ... }
            ```

        - id: scala
          content: |
            To specify equality conditions, use the
            `com.mongodb.client.model.Filters.eq_` method to create the
            query filter document:

            ```scala
            and(equal(<field1>, <value1>), equal(<field2>, <value2>) ...)
            ```

        - id: csharp
          content: |
            To specify equality conditions, construct a filter using the
            `Eq` method:

            ```csharp
            Builders<BsonDocument>.Filter.Eq(<field>, <value>);
            ```

      tabs:
        - id: shell
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```javascript
            { <field1>: { <operator1>: <value1> }, ... }
            ```

        - id: compass
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```javascript
            { <field1>: { <operator1>: <value1> }, ... }
            ```

        - id: python
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```python
            { <field1>: { <operator1>: <value1> }, ... }
            ```

        - id: motor
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```python
            { <field1>: { <operator1>: <value1> }, ... }
            ```

        - id: java-sync
          content: |

            In addition to the equality condition, MongoDB provides
            various query operators to specify
            filter conditions. Use the
            com.mongodb.client.model.Filters_ helper methods to
            facilitate the creation of filter documents. For example:

            ```java
            and(gte(<field1>, <value1>), lt(<field2>, <value2>), eq(<field3>, <value3>))
            ```

        - id: java-async
          content: |

            In addition to the equality condition, MongoDB provides
            various query operators to specify
            filter conditions. Use the
            com.mongodb.client.model.Filters_ helper methods to
            facilitate the creation of filter documents. For example:

            ```java
            and(gte(<field1>, <value1>), lt(<field2>, <value2>), eq(<field3>, <value3>))
            ```

        - id: nodejs
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```javascript
            { <field1>: { <operator1>: <value1> }, ... }
            ```

        - id: php
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```php
            [ <field1> => [ <operator1> => <value1> ], ... ]
            ```

        - id: perl
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```perl
            { <field1> => { <operator1> => <value1> }, ... }
            ```

        - id: ruby
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```ruby
            { <field1> => { <operator1> => <value1> }, ... }
            ```

        - id: scala
          content: |

            In addition to the equality condition, MongoDB provides
            various query operators to specify
            filter conditions. Use the
            `com.mongodb.client.model.Filters_` helper methods to
            facilitate the creation of filter documents. For example:

            ```scala
            and(gte(<field1>, <value1>), lt(<field2>, <value2>), equal(<field3>, <value3>))
            ```

        - id: csharp
          content: |
            In addition to the equality filter, MongoDB provides
            various query operators to specify
            filter conditions. Use the
            `FilterDefinitionBuilder`
            methods to create a filter document. For example:

            ```csharp
            var builder = Builders<BsonDocument>.Filter;
            builder.And(builder.Eq(<field1>, <value1>), builder.Lt(<field2>, <value2>));
            ```

      To delete all documents that match a deletion criteria, pass a
      filter parameter to the
      `IMongoCollection.DeleteMany()`
      method.

      The following example removes all documents from the `inventory`
      collection where the `status` field equals `"A"`:

  - id: go
    content: |

      You can specify criteria, or filters, that identify the documents to
      delete. The filters use the same syntax
      as read operations.

      tabs:
        - id: shell
          content: |
            To specify equality conditions, use `<field>:<value>`
            expressions in the
            query filter document:

            ```javascript
            { <field1>: <value1>, ... }
            ```

        - id: compass
          content: |
            To specify equality conditions, use `<field>:<value>`
            expressions in the
            query filter document:

            ```javascript
            { <field1>: <value1>, ... }
            ```

        - id: python
          content: |
            To specify equality conditions, use `<field>:<value>`
            expressions in the
            query filter document:

            ```python
            { <field1>: <value1>, ... }
            ```

        - id: motor
          content: |
            To specify equality conditions, use `<field>:<value>`
            expressions in the
            query filter document:

            ```python
            { <field1>: <value1>, ... }
            ```

        - id: java-sync
          content: |
            To specify equality conditions, use the
            `com.mongodb.client.model.Filters.eq_` method to create the
            query filter document:

            ```java
            and(eq( <field1>, <value1>), eq( <field2>, <value2>) ...)
            ```

        - id: java-async
          content: |
            To specify equality conditions, use the
            com.mongodb.client.model.Filters.eq_ method to create the
            query filter document:

            ```java
            and(eq( <field1>, <value1>), eq( <field2>, <value2>) ...)
            ```

        - id: nodejs
          content: |
            To specify equality conditions, use `<field>:<value>`
            expressions in the
            query filter document:

            ```javascript
            { <field1>: <value1>, ... }
            ```

        - id: php
          content: |
            To specify equality conditions, use `<field> => <value>`
            expressions in the
            query filter document:

            ```php
            [ <field1> => <value1>, ... ]
            ```

        - id: ruby
          content: |
            To specify equality conditions, use `<field> => <value>`
            expressions in the
            query filter document:

            ```ruby
            { <field1> => <value1>, ... }
            ```

        - id: scala
          content: |
            To specify equality conditions, use the
            `com.mongodb.client.model.Filters.eq_` method to create the
            query filter document:

            ```scala
            and(equal(<field1>, <value1>), equal(<field2>, <value2>) ...)
            ```

        - id: csharp
          content: |
            To specify equality conditions, construct a filter using the
            `Eq` method:

            ```csharp
            Builders<BsonDocument>.Filter.Eq(<field>, <value>);
            ```

      tabs:
        - id: shell
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```javascript
            { <field1>: { <operator1>: <value1> }, ... }
            ```

        - id: compass
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```javascript
            { <field1>: { <operator1>: <value1> }, ... }
            ```

        - id: python
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```python
            { <field1>: { <operator1>: <value1> }, ... }
            ```

        - id: motor
          content: |
            A query filter document can
            use the query operators to specify
            conditions in the following form:

            ```python
            { <field1>: { <operator1>: <value1> }, ... }
            ```

        - id: java-sync
          content: |

            In addition to the equality condition, MongoDB provides
            various query operators to specify
            filter conditions. Use the
            com.mongodb.client.model.Filters_ helper methods to
            facilitate the creation of filter documents. For example:

            ```java
            and(gte(<field1>, <value1>), lt(<field2>, <value2>), eq(<field3>, <value3>))
            ```

        - id: java-async
          content: |

            In addition to the equality condition, MongoDB provides
