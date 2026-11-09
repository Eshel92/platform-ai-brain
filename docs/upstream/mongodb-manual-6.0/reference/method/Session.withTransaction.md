<!-- Converted from reference/method/Session.withTransaction.txt (reStructuredText). Includes are inlined. -->

# Session.withTransaction()

## Definition

**`Session.withTransaction( <function> [, <options> ] )`**

*New in mongosh v1.1.0*

Runs a specified lambda function within a transaction. If there is an
error, the method retries the:

- commit operation, if there is a failure to commit.
- entire transaction, if the error permits.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `commitTransaction` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

The `Session.withTransaction()` method accepts the
[transaction options](https://mongodb.github.io/node-mongodb-native/4.8/interfaces/TransactionOptions.html).

## Behavior

The Node.js driver has a version of `Session.withTransaction()` that is
known as the [Callback API](https://www.mongodb.com/docs/drivers/node/current/fundamentals/transactions/#callback-api).
The `Callback API` also accepts an callback, however the return type
for the Node.js method must be a Promise. The `mongosh`
`Session.withTransaction()` method does not require a Promise. 

## Example

The following example creates the `balances` collection and uses a
transaction to transfer money between two customers. 

Create the `balances` collection:

```javascript
use accounts
db.balances.insertMany( [
  { customer: "Pat", balance: Decimal128( "35.88" ) },
  { customer: "Sasha", balance: Decimal128( "5.23" ) }
] )
```

Initialize some variables that are used in the transaction:

```javascript
var fromAccount = "Pat"
var toAccount = "Sasha"
var transferAmount = 1

var dbName = "accounts"
var collectionName = "balances"
```

Start a session, then run a transaction to update the accounts:

```javascript
var session = db.getMongo().startSession( { readPreference: { mode: "primary" } } );
session.withTransaction( async() => {  

   const sessionCollection = session.getDatabase(dbName).getCollection(collectionName);

   // Check needed values
   var checkFromAccount = sessionCollection.findOne(
      {
         "customer": fromAccount,
         "balance": { $gte: transferAmount }
      }
   )
   if( checkFromAccount === null ){
      throw new Error( "Problem with sender account" )
   } 

   var checkToAccount = sessionCollection.findOne(
      { "customer": toAccount }
   )
   if( checkToAccount === null ){
      throw new Error( "Problem with receiver account" )
   } 

   // Transfer the funds
   sessionCollection.updateOne(
      { "customer": toAccount },
      { $inc: { "balance": transferAmount } }
   )
   sessionCollection.updateOne(
      { "customer": fromAccount },
      { $inc: { "balance": -1 * transferAmount } }
   )

 } )
```

The lambda function includes initial checks to validate the operation
before updating the `balances` collection.

MongoDB automatically completes the transaction.

- If both `updateOne()` operations succeed,
  `Session.withTransaction()` commits the transaction when the callback
  returns.
- If an exception is thrown inside the callback,
  `Session.withTransaction()` ends the transaction and rolls back any
  uncommitted changes.

**Note:**

By default, MongoDB ends transactions that run for more than 60
seconds. If you want to extend the default timeout to experiment with
transactions in `mongosh`, see transaction-limit.
