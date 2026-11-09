<!-- Converted from tutorial/migrate-fts-vs-with-external-mongod-to-grpc.txt (reStructuredText). Includes are inlined. -->

:noprevnext:

# Migrate MongoDB Search and Vector Search Configuration for External MongoDB Enterprise Edition to gRPC

Starting in MongoDB Controllers for Kubernetes Operator v1.6, MongoDB Search and Vector Search uses the
gRPC protocol for search index queries and index management commands
issued by `mongod`. The Kubernetes Operator automatically migrates MongoDB
instances it manages directly on Kubernetes. However, if you deployed the
MongoDB Server outside of the Kubernetes cluster, you must update the
manually applied `setParameter` startup options to use the new
endpoints and protocol options for gRPC.

## Before You Begin

You must upgrade your external MongoDB Enterprise Edition to v8.2 or
later before upgrading your MongoDB Controllers for Kubernetes Operator to v1.6.

## Migrate Your External MongoDB Enterprise Edition Server Configuration

Once you upgrade MongoDB Controllers for Kubernetes Operator to v1.6, the new version of Kubernetes Operator:

- Reconciles existing MongoDBSearch resources.
- Toggles the new gRPC protocol option. 

When the MongoDBSearch resource is in the `Running` state, you can 
perform the following actions to migrate your external MongoDB
Enterprise Edition server configuration: 

**Step 1: Update the ports in the Kubernetes Service.**

In the `LoadBalancer` service that you created in step 4 to enable external access to
MongoDBSearch service, update the `port` and `targetPort`
mapping from `27027` to `27028`.  

**Step 2: Remove the keyfile reference.**

In the MongoDBSearch resource that you created in step 3, remove the 
`spec.source.external.keyfileSecretRef` field. You can also
delete the Kubernetes secret that was referenced in this field. 

**Step 3: Update parameters in Cloud Manager or Ops Manager instance.**

In your Cloud Manager or Ops Manager deployment configuration, make the following changes 
to the `setParameter` startup options and deploy the changes:

a. Modify `mongotHost` and `searchIndexManagementHostAndPort`
   options to use port number `27028`. 

#. Add a new option named `useGrpcForSearch` and set it to
   `true`. 

After deploying the changes, wait for the rolling restart of the
replica set to complete.

**Step 4: Verify MongoDB Search and Vector Search.**

Ensure MongoDB Search and Vector Search are working correctly by
running the `$listSearchIndexes` aggregation. Verify
that the output contains the search indexes you had created before
migrating.
