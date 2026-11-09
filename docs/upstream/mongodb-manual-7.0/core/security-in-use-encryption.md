<!-- Converted from core/security-in-use-encryption.txt (reStructuredText). Includes are inlined. -->

# In-Use Encryption

MongoDB provides two approaches to In-Use Encryption:

- Queryable Encryption 
- Client-Side Field Level Encryption. 

## Choosing an In-Use Encryption Approach

You can use both Queryable Encryption and Client-Side Field Level Encryption in the same deployment, but they are 
incompatible with each other in the same collection.

## Queryable Encryption

To learn how Queryable Encryption and its components work and how to implement it in
your application, see qe-manual-feature-qe.

## Client-Side Field Level Encryption

To learn how Client-Side Field Level Encryption and its components work and how to implement it
in your application, see manual-csfle-feature.
