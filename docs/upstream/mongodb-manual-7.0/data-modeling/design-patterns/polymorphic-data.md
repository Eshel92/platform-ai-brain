<!-- Converted from data-modeling/design-patterns/polymorphic-data.txt (reStructuredText). Includes are inlined. -->

# Polymorphic Data

MongoDB uses a flexible data model, which means documents in a single
collection do not need to have the same structure. Polymorphic data is
data in a single collection that varies in document fields or data
types.

Generally, documents in a collection are similar in structure but may
contain slight variations depending on the application. To group
similar, non-identical documents in a single collection you can use the
Polymorphic and the
Inheritance schema design patterns.

These schema designs can improve performance by storing data based on
query access patterns, rather than storing data strictly based on
document shape.

## Use Cases

| Scenario | Design Pattern Application |
|---|---|
| Your application tracks professional athletes across different sports. Your queries access all athletes, but the attributes stored for each athlete vary depending on their sport. | Use the **polymorphic pattern** to group athletes in a single collection. Even though the documents have different shapes, they can still be accessed with a single query. |
| Your application tracks books in a bookstore. Books can be available in different forms: ebook, print, or audiobook. All books share the fields of `title`, `author`, and `genre` but have additional differing fields depending on their format. | Use the **inheritance pattern** to group books into a single collection. Each book format is a child entity of the parent entity of `book` that provides the shared fields of `title`, `author`, and `genre` across all formats. Despite the additional differing fields of the child entities, the shared fields from the parent entity allow them to be grouped into a single collection. |

## Get Started

- polymorphic-schema-pattern

- inheritance-schema-pattern

## Learn More

- data-modeling-schema-design

- schema-design-patterns
