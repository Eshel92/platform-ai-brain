<!-- Converted from data-modeling/design-patterns/handle-computed-values.txt (reStructuredText). Includes are inlined. -->

# Handle Computed Values

If you want to return calculated data values to your application, you can 
improve performance by running computations in your database rather than when 
the data is requested. The application may require either precise calculations 
or approximate results. By using the Computed and the Approximation 
schema patterns, you can pre-compute and store the resulting values ahead of 
time (for example on insert or with a periodic task) so they are readily available 
when you request the data.

## Use Cases

| Scenario | Design Pattern Application |
|---|---|
| A consumer reporting company compiles data from several different sources to create rank-ordered lists like the "100 Best-Reviewed Gadgets". | Use the **computed pattern** to update the list periodically while the underlying data is updated independently. |
| Your application tracks the population of a city that contains 40,000 people. | Use the **approximation pattern** to update the population value in increments of 100. The computations are not precise but they are statistically valid. |

## Get Started

To learn how to apply design patterns for computed values, see these pages:

- computed-schema-pattern

- approximation-schema-pattern

## Learn More

- data-modeling-schema-design

- schema-design-patterns
