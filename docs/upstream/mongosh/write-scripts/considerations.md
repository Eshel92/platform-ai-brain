<!-- Converted from write-scripts/considerations.txt (reStructuredText). Includes are inlined. -->

# Script Considerations

The results of database queries cannot be passed inside the following
contexts:

- Class constructor functions
- Non-async generator functions
- Callbacks to `.sort()` on an array
- JavaScript setters in classes

To access to the results of database calls, use [async functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function),
[async generator functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of),
or `.map()`.

## Constructors

The following constructors do not work: 

```javascript
// This code will fail
class FindResults {
   constructor() {
      this.value = db.students.find();
   }
}

// This code will fail
function listEntries() { return db.students.find(); }
class FindResults {
   constructor() {
      this.value = listEntries();
   }
}
```

Use an `async` function instead:

```javascript
class FindResults {
   constructor() {
      this.value = ( async() => {
         return db.students.find();
      } )();
   }
}
```

**Note:**

You can also create a method that performs a database operation
inside a class as an alternative to working with asynchronous
JavaScript.

```
class FindResults {
   constructor() { }

   init() { this.value = db.students.find(); }
 }
```

To use this class, first construct a class instance then call the
`.init()` method.

## Generator Functions

The following generator functions do not work: 

```javascript
// This code will fail
function* FindResults() {
   yield db.students.findOne();
}

// This code will fail
function listEntries() { return db.students.findOne(); }
function* findResults() {
   yield listEntries();
}
```

Use an `async generator function` instead: 

```javascript
function listEntries() { return db.students.findOne(); }
async function* findResults() {
   yield listEntries();
}
```

## Array Sort

The following array sort does not work: 

```javascript
// This code will fail
db.getCollectionNames().sort( ( collectionOne, collectionTwo ) => {
  return db[ collectionOne ].estimatedDocumentCount() - db[ collectionOne ].estimatedDocumentCount() )
} );
```

Use `.map()` instead. 

```javascript
db.getCollectionNames().map( collectionName => {
   return { collectionName, size: db[ collectionName ].estimatedDocumentCount() };
} ).sort( ( collectionOne, collectionTwo ) => {
   return collectionOne.size - collectionTwo.size;
} ).map( collection => collection.collectionName);
```

This approach to array sort is often more performant than the
equivalent unsupported code.

## JavaScript Setters

The following JavaScript setter does not work: 

```javascript
// This code will fail
class TestClass {
  value = 1;

  get property() {
    return this.value;
  }

  // does not work:
  set property(value) {
    this.value = db.test.findOne({ value });
  }
}
```
