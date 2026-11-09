<!-- Converted from tutorial/manage-database-users-oidc.txt (reStructuredText). Includes are inlined. -->

:noprevnext:

# Manage Database Users Using OIDC Authentication

The Kubernetes Operator supports managing database users for deployments
running with TLS (Transport Layer Security) and OIDC cluster authentication enabled. This allows you to 
create individual database user objects that authenticate against your 
configured OIDC provider.

This method is primarily used when your OIDC provider is configured with an 
`authorizationType` of `UserID`. 

For `GroupMembership` authorization, roles are managed directly in the `MongoDB`
resource specification, not through individual `MongoDBUser` resources.

## Considerations

- `MongoDBUser` Resource: Each OIDC user managed this way requires a 
  corresponding `MongoDBUser` custom resource. The Kubernetes Operator uses this 
  resource to configure the user within MongoDB.

- `$external` Database: All users that authenticate via an external mechanism 
  like OIDC must be created in the `$external` virtual database. You must set 
  `spec.db` to "$external" in the `MongoDBUser` resource.

- Username Format: The spec.username must follow the format 
  <configurationName>/<userClaimValue>, combining the OIDC provider's 
  configuration name with the unique claim from the user's JWT. This 
  claim is specified by `userClaim` in your OIDC provider configuration and 
  defaults to `sub`.

- Authentication vs. Authorization: Your OIDC Identity Provider (IdP) is 
  responsible for authenticating the user (verifying their identity). The 
  `MongoDBUser` resource is responsible for authorizing the user (defining 
  what they have permission to do) within MongoDB.

## Prerequisites

Before managing database users, you must deploy a
replica set or
sharded cluster with OpenID Connect enabled.
enabled. Optionally, you can enable TLS (Transport Layer Security). To learn more, see
Secure a Database Resource.

## Add a Database User

**Step 1: Create a MongoDBUser YAML file.**

Create a file (e.g., `my-oidc-user.yaml`) to define the user.

- `metadata.name`: A unique name for the MongoDBUser resource within Kubernetes.
- `spec.username`: The user's OIDC identity, combining the oidc 
  provider's `configurationName` and the user's unique token claim in the 
  format `<configurationName>/<userClaimValue>`.
- `spec.db`: This must be `$external`.
- `spec.mongodbResourceRef.name`: The name of the `MongoDB` resource this user belongs to.
- `spec.roles`: An array of MongoDB roles to grant to this user.

Here is an example that creates a user with read-write access to the app-data database.

```yaml
apiVersion: mongodb.com/v1
kind: MongoDBUser
metadata:
  # A unique name for this Kubernetes resource.
  name: oidc-app-user-1
spec:
  # This username MUST match the 'userClaim' from the OIDC token.
  username: "idp0/a1b2c3d4e5f6g7h8"

  # OIDC users MUST be created in the $external database.
  db: "$external"

  # Point to the MongoDB deployment where this user should be created.
  mongodbResourceRef:
    name: my-oidc-replicaset

  # Grant MongoDB roles to the user.
  roles:
    - db: "app-data"
      name: "readWrite"
```

**Step 2: Apply the configuration.**

```sh
kubectl apply -f my-oidc-user.yaml
```

## Delete a Database User

To delete a database user, you simply delete the `MongoDBUser` resource 
associated with them. The Kubernetes Operator will automatically remove the user from 
the MongoDB database. Pass the `metadata.name` of the `MongoDBUser` resource 
to the following command:

```sh
kubectl delete mongodbuser oidc-app-user-1
```
