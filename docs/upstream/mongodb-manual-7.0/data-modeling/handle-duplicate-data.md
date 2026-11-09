<!-- Converted from data-modeling/handle-duplicate-data.txt (reStructuredText). Includes are inlined. -->

# Handle Duplicate Data

When you embed related data in a single document, you may duplicate data
between two collections. Duplicating data lets your application query
related information about multiple entities in a single query while
logically separating entities in your model.

## About this Task

One concern with duplicating data is increased storage costs. However,
the benefits of optimizing access patterns generally outweigh potential
cost increases from storage.

Before you duplicate data, consider the following factors:

- The performance benefit for reads when data is duplicated. Duplicating
  data can remove the need to perform joins across multiple collections,
  which can improve application performance.

- How often the duplicated data needs to be updated. The extra logic needed to 
  handle infrequent updates is less costly than performing joins (lookups) on 
  read operations. However, frequently updating duplicate data can cause heavy 
  workloads and performance issues. 

## Example: Duplicate Data in an E-Commerce Schema

The following example shows how to duplicate data in an e-commerce
application schema to improve data access and performance.

### Steps

**Step 1: Switch to the `eCommerce` database**

```javascript
use eCommerce
```

**Step 2: Populate the database**

Create the following collections in the `eCommerce` database:

| Collection Name | Description | Sample Document |
|---|---|---|
| `customers` | Stores customer information such as name, email, and phone number. | .. code-block:: javascript db.customers.insertOne( { customerId: 123, name: "Alexa Edwards", email: "a.edwards@randomEmail.com", phone: "202-555-0183" } ) |
| `products` | Stores product information such as price, size, and material. | .. code-block:: javascript db.products.insertOne( { productId: 456, product: "sweater", price: 30, size: "L", material: "silk", manufacturer: "Cool Clothes Co" } ) |
| `orders` | Stores order information such as date and total price. Documents in the `orders` collection embed the corresponding products for that order in the `lineItems` field. | .. code-block:: javascript db.orders.insertOne( { orderId: 789, customerId: 123, totalPrice: 45, date: ISODate("2023-05-22"), lineItems: [ { productId: 456, product: "sweater", price: 30, size: "L" }, { productId: 809, product: "t-shirt", price: 10, size: "M" }, { productId: 910, product: "socks", price: 5, size: "S" } ] } ) |

The following properties from the `products` collection are duplicated
in the `orders` collection:

- `productId`
- `product`
- `price`
- `size`

### Benefits of Duplicating Data

When the application displays order information, it displays the
corresponding order's line items. If the order and product information
were stored in separate collections, the application would need to
perform a `$lookup` to join data from two collections. Lookup
operations are often expensive and have poor performance.

The reason to duplicate product information as opposed to only embedding
line items in the `orders` collection is that the application only
needs a subset of product information when displaying orders. By only
embedding the required fields, the application can store additional
product details without adding unnecessary bloat to the `orders`
collection.

## Example: Duplicate Data for Product Reviews

The following example uses the [subset pattern](https://www.mongodb.com/blog/post/building-with-patterns-the-subset-pattern)
to optimize access patterns for an online store.

Consider an application where when user views a product, the application
displays the product's information and five most recent reviews. The
reviews are stored in both a `products` collection and a `reviews`
collection.

When a new review is written, the following writes occur:

- The review is inserted into the `reviews` collection.

- The array of recent reviews in the `products` collection is updated
  with `$pop` and `$push`.

### Steps

**Step 1: Switch to the `productsAndReviews` database**

```javascript
use productsAndReviews
```

**Step 2: Populate the database**

Create the following collections in the `productsAndReviews` database:

| Collection Name | Description | Sample Document |
|---|---|---|
| `products` | Stores product information. Documents in the `products` collection embed the five most recent product reviews in the `recentReviews` field. | .. code-block:: javascript db.products.insertOne( { productId: 123, name: "laptop", price: 200, recentReviews: [ { reviewId: 456, author: "Pat Simon", stars: 4, comment: "Great for schoolwork", date: ISODate("2023-06-29") }, { reviewId: 789, author: "Edie Short", stars: 2, comment: "Not enough RAM", date: ISODate("2023-06-22") } ] } ) |
| `reviews` | Stores all reviews for products (not only recent reviews). Documents in the `reviews` collection contain a `productId` field that indicates the product that the review pertains to. | .. code-block:: javascript db.reviews.insertOne( { reviewId: 456, productId: 123, author: "Pat Simon", stars: 4, comment: "Great for schoolwork", date: ISODate("2023-06-29") } ) |

### Benefits of Duplicating Data

The application only needs to make one call to the database to return
the all information it needs to display. If data was stored entirely in
separate collections, the application would need to join data from the
`products` and `reviews` collection, which could cause performance
issues.

Reviews are rarely updated, so it is not expensive to store duplicate
data and keeping the data consistent between collections is not a
challenge.

## Learn More

To learn how to keep duplicate data consistent, see
data-modeling-data-consistency.
