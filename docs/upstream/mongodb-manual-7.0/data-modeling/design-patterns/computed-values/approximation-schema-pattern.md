<!-- Converted from data-modeling/design-patterns/computed-values/approximation-schema-pattern.txt (reStructuredText). Includes are inlined. -->

# Use the Approximation Pattern

Use the approximation pattern when you have values that change
frequently, but users don't need to know precise values. Instead of
updating values every time data changes, the approximation pattern
updates data based on a larger granularity, which results in fewer
updates and a lower application workload.

## About this Task

The approximation pattern is useful when values don't need to be
reported exactly. For example:

- City population
- Website visits
- Airline travelers

The preceding measurements are typically useful when approximated. The
application can save time and resources by updating stored values by
hundreds or thousands, depending on the scale of the data.

## Steps

In this example, an application displays population data for a city of
roughly 40,000 people. Application users are primarily looking for
overall trends and don't need to know the exact city population.

**Step 1: Insert sample data.**

```javascript
db.population.insertOne( {
   city: "New Perth",
   population: 40000,
   date: ISODate("2022-09-15")
} )
```

**Step 2: Implement the approximation pattern.**

The actual population value changes many times in a single day.
Rather than updating the population value with each change, use
application logic to insert a new document every time the
population changes by 100.

For example, your application logic might resemble the following:

```javascript
let population = 40000

function updateStoredPopulation(curr_population, new_population) {

   let population_change = Math.abs(curr_population - new_population)

   if (population_change >= 100) {
      db.population.insertOne(
         {
            city: "New Perth",
            population: new_population,
            date: Date()
         }
      )
      population = new_population
   }
}
```

**Note:**

The preceding example is only illustrative and does not use
accurate syntax. To learn the correct syntax for your
application, refer to your corresponding `driver
documentation`.

## Results

The preceding application logic might result in these documents:

```javascript
db.population.insertMany( [
   {
      city: "New Perth",
      population: 40100,
      date: ISODate("2024-09-20")
   },
   {
      city: "New Perth",
      population: 40200,
      date: ISODate("2024-10-01")
   },
   {
      city: "New Perth",
      population: 40300,
      date: ISODate("2024-10-09")
   },
] )
```

**Note:**

How the updated values are gathered depends on your scenario.
In this example, updated population values can be gathered from
census reports.

By updating the population with a granularity of 100, the approximation
pattern reduces the number of updates to 1% of the updates that would be
required to track individual population changes.

Users can see the population increasing over time, which meets their
needs of seeing high-level trends.

## Learn More

- computed-schema-pattern
- data-modeling-data-consistency
- schema-pattern-group-data
