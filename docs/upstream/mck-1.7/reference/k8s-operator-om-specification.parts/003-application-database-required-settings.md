<!-- Part 3 of 5 of reference/k8s-operator-om-specification.md (split because the page is big). -->

## Application Database Required Settings

This section describes settings that you must use 
in addition to the required Ops Manager settings to
configure your Ops Manager Application Database.

**`spec.applicationDatabase.version`**

*Type*: string

*Required*. Version of MongoDB installed on the Ops Manager
`Application Database`.
You must specify a compatible enterprise MongoDB version based on the tag in the
`container registry`.
For example, `8.0.0-ubi8`. Starting in Kubernetes Operator version 1.20, tags no longer end in `-ent`.

**Important:**

Ensure that you choose a compatible MongoDB Server version.

Compatible versions differ depending on the base image that the
MongoDB database resource uses.

**Note:**

If you update this value to a later version of MongoDB for the 
Application Database, the feature compatibility version remains at the MongoDB version 
you're upgrading from to give you the option to downgrade if necessary.
If you want the feature compatibility version to match the new MongoDB version, 
you must manually set the 
`featureCompatibilityVersion`
parameter under `spec.applicationDatabase`.
