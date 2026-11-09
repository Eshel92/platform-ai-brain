<!-- Converted from tutorial/secure-oidc-auth.txt (reStructuredText). Includes are inlined. -->

:noprevnext:

# Configure Single Cluster OIDC Authentication

The Kubernetes Operator supports OpenID Connect (OIDC) as an authentication 
mechanism. When you configure OIDC authentication, client applications present 
a JSON Web Token (JWT) to the MongoDB resource. MongoDB validates the JWT 
against the configured OIDC Identity Provider (IdP) and uses claims within 
the token to determine the user's identity and, optionally, their group 
memberships for role-mapping.

This guide describes how to configure OIDC authentication for client 
applications that connect to your MongoDB deployments using the Kubernetes Operator.

**Note:**

You cannot secure a Standalone Instance of MongoDB with OIDC in a 
Kubernetes cluster.

## Considerations

When you enable OIDC authentication, consider the following:

- **Identity Providers:** You must have a pre-existing, configured OIDC 
  Identity Provider (IdP). The Kubernetes Operator does not manage the 
  IdP itself.
- **Authorization:** The Kubernetes Operator configures authentication 
  (verifying identity) via OIDC. Authorization (granting permissions) 
  is handled by mapping OIDC claims to MongoDB roles within the MongoDB 
  custom resource.
- **Federation:** MongoDB supports both Workload Identity Federation 
  (for machine-to-machine authentication) and Workforce Identity Federation 
  (for human user authentication).
- **TLS Encryption:** To improve security, it is highly recommended to deploy a 
  TLS-encrypted replica set or a TLS-encrypted sharded cluster. While OIDC 
  communication with your identity provider is secured by HTTPS, enabling TLS 
  on your MongoDB resource encrypts the connection between your client 
  application and the database. This protects the OIDC token and all other 
  database traffic from network threats.

## General Prerequisites

Before you configure OIDC authentication for your MongoDB deployments,
complete the following tasks:

- Ensure that you deploy the MongoDB Enterprise database resource.
  MongoDB Community databases don't support OIDC authentication.
- Deploy the replica set or
  deploy the sharded cluster
  whose client authentication you want to secure with OpenID Connect.

## OIDC Configuration Details

|  |  |  |  |
|---|---|---|---|
| Field | Type and Necessity | Description | Example |
| `spec.security.authentication.modes` | array of strings; required | An array of authentication mechanisms to enable. Must include "OIDC" to enable OIDC authentication. | `["SCRAM", "OIDC"]` |
| `spec.security.authentication.oidcProviderConfigs.configurationName` | string; required | A unique logical name for this provider configuration. This name is used when mapping roles. | `"example-provider"` |
| `spec.security.authentication.oidcProviderConfigs.issuerURI` | string; required | The URI of the OIDC provider's discovery endpoint. | `"https://dev-12345.provider.com"` |
| `spec.security.authentication.oidcProviderConfigs.clientId` | string; required | The client ID for the application registered with your OIDC provider. | `"0oa1b2c3d4e5f6g7h8"` |
| `spec.security.authentication.oidcProviderConfigs.audience` | string; required | The audience claim for the JWT. This must match the audience of the token issued by the IdP. | `"api://default"` |
| `spec.security.authentication.oidcProviderConfigs.userClaim` | string; optional | The JWT claim that MongoDB uses as the username. Defaults to `sub`. | `"sub"` |
| `spec.security.authentication.oidcProviderConfigs.groupsClaim` | string; optional | The JWT claim that contains the user's group memberships. Required if `authorizationType` is `GroupMembership`. | `"groups"` |
| `spec.security.authentication.oidcProviderConfigs.authorizationMethod` | string; required | The federation method. Can be `WorkloadIdentityFederation` or `WorkforceIdentityFederation`. | `"WorkforceIdentityFederation"` |
| `spec.security.authentication.oidcProviderConfigs.authorizationType` | string; required | The authorization model. Can be `UserID` or `GroupMembership`. | `"GroupMembership"` |
| `spec.security.authentication.oidcProviderConfigs.requestedScopes` | array of strings; optional | A list of additional scopes to request from the OIDC provider. | `["openid", "profile", "groups"]` |

## Understanding OIDC Authorization Models

OIDC configuration in MongoDB combines two key concepts: the **Federation Method** 
and the **Authorization Type**.

### Federation Method (`authorizationMethod`)

This setting tells MongoDB about the type of identity being authenticated.

- `WorkforceIdentityFederation`: Use this for **human users**. 
  This method is intended for people logging into systems, such as 
  developers, analysts, or administrators who authenticate via an IdP.

- `WorkloadIdentityFederation`: Use this for **applications or services** 
  (i.e., machine-to-machine communication). This method is for non-human 
  identities, such as a microservice, a batch job, or an automation script 
  that needs to connect to the database.

### Authorization Type (`authorizationType`)

This setting defines how MongoDB should grant permissions after a user or 
service is authenticated.

- `GroupMembership`: This is the most common and scalable approach. With 
  this type, MongoDB uses a specific claim in the JWT (defined by `groupsClaim`) 
  that contains a list of groups the user belongs to. You then map 
  these group names to MongoDB roles. Requires `groupsClaim` to be set.

- `UserID`: With this type, MongoDB uses a claim that uniquely identifies the 
  user (defined by `userClaim`, which defaults to `sub`). You then map 
  this specific, individual user ID to a MongoDBUser (you need to create the MongoDBUser 
  separately). This is more granular and is useful for granting permissions to 
  a single user or a specific service identity without using groups.

## Managing OIDC Roles and Permissions

After configuring an OIDC provider, you must grant permissions. The method 
you use to do this depends on the `authorizationType` you selected.

### Method 1: Role Mapping for GroupMembership

If you use `authorizationType: GroupMembership`, you grant permissions by 
adding role mappings to the `spec.security.roles` array in your MongoDB resource.
The role field must be formatted as `<configurationName>/<groupNameFromToken>`.

```yaml
roles:
 - role: "idp-human-users/app-devs" # Maps the "app-devs" group from the IdP
   db: "admin"
   roles:
     - role: "readWrite"
       db: "app-data"
```

### Method 2: User Creation for UserID

If you use `authorizationType: UserID`, you must create a separate 
`MongoDBUser` resource to grant permissions.

To learn more, see [Authentication and Authorization with OIDC/OAuth 2.0](https://www.mongodb.com/docs/manual/core/oidc/security-oidc/).

## Configure OIDC Client Authentication for a Replica Set

Follow these steps to configure OIDC for a replica set.

**Step 1: Retrieve your Kubernetes Operator replica set definition file.**

If you have an existing replica set definition file, open it. Otherwise, 
you can copy the entire working examples below.

**Step 2: Add the OIDC authentication settings.**

In your definition file, modify the `spec.security` section. Choose one or 
more of the following examples based on your use case. You can combine 
multiple provider configurations in the `oidcProviderConfigs` array.

**Example A: Workforce Federation with Group Membership**

Use this for authenticating human users based on their group membership in your IdP. 
This is the most common model for managing teams of users.

```yaml
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: my-oidc-replicaset
spec:
  type: ReplicaSet
  members: 3
  version: 7.0.11-ent
  opsManager:
    configMapRef:
      name: <my-project-configmap>
  credentials: <my-credentials-secret>
  security:
    authentication:
      modes: ["SCRAM", "OIDC"]
      oidcProviderConfigs:
        - configurationName: "idp-human-users"
          issuerURI: "https://<your-idp-domain>"
          clientId: "<your-client-id>"
          audience: "api://default"
          groupsClaim: "groups"
          authorizationMethod: "WorkforceIdentityFederation"
          authorizationType: "GroupMembership"
    roles:
      - role: "idp-human-users/app-devs"
        db: "admin"
        roles:
          - role: "readWrite"
            db: "app-data"
```

**Example B: Workload Federation with UserID**

Use this for authenticating an application or service with a specific 
identity. This is ideal for service accounts.

```yaml
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: my-oidc-replicaset
spec:
  type: ReplicaSet
  members: 3
  version: 7.0.11-ent
  opsManager:
    configMapRef:
      name: <my-project-configmap>
  credentials: <my-credentials-secret>
  security:
    authentication:
      modes: ["SCRAM", "OIDC"]
      oidcProviderConfigs:
        - configurationName: "billing-service-auth"
          issuerURI: "https://<your-idp-uri>"
          clientId: "<billing-service-client-id>"
          audience: "mongodb-api"
          userClaim: "sub"
          authorizationMethod: "WorkloadIdentityFederation"
          authorizationType: "UserID"
```

**Note:**

Note: To grant permissions for this identity, you must also create a 
`MongoDBUser` resource. The username in that resource must be set to 
`billing-service-auth/<user-subject-from-jwt>`. 

To learn more, see Manage Database Users Using OIDC Authentication.

**Example C: Workforce Federation with UserID**

Use this to grant a specific human user unique permissions not covered 
by their group memberships.

```yaml
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: my-oidc-replicaset
spec:
  type: ReplicaSet
  members: 3
  version: 7.0.11-ent
  opsManager:
    configMapRef:
      name: <my-project-configmap>
  credentials: <my-credentials-secret>
  security:
    authentication:
      modes: ["SCRAM", "OIDC"]
      oidcProviderConfigs:
        - configurationName: "idp-special-user"
          issuerURI: "https://<your-idp-domain>"
          clientId: "<your-client-id>"
          audience: "api://default"
          userClaim: "sub"
          authorizationMethod: "WorkforceIdentityFederation"
          authorizationType: "UserID"
```

**Note:**

Note: To grant permissions for this identity, you must also create a 
`MongoDBUser` resource. The username in that resource must be set to 
`billing-service-auth/<user-subject-from-jwt>`. 

To learn more, see Manage Database Users Using OIDC Authentication.

**Example D: Workload Federation with Group Membership**

Use this for authenticating a group of related services or applications 
that all require the same permissions.

```yaml
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: my-oidc-replicaset
spec:
  type: ReplicaSet
  members: 3
  version: 7.0.11-ent
  opsManager:
    configMapRef:
      name: <my-project-configmap>
  credentials: <my-credentials-secret>
  security:
    authentication:
      modes: ["SCRAM", "OIDC"]
      oidcProviderConfigs:
        - configurationName: "reporting-services"
          issuerURI: "https://<your-idp-uri>"
          clientId: "<reporting-services-client-id>"
          audience: "mongodb-api"
          groupsClaim: "service-roles"
          authorizationMethod: "WorkloadIdentityFederation"
          authorizationType: "GroupMembership"
    roles:
      - role: "reporting-services/report-generators"
        db: "admin"
        roles:
          - role: "read"
            db: "sales-data"
```

**Step 3: Apply the configuration.**

```sh
kubectl apply -f <your-replica-set-file>.yaml
```

**Step 4: Track the status of your deployment.**

```sh
kubectl get mdb <resource-name> -o yaml -w
```

## Configure OIDC Client Authentication for a Sharded Cluster

Use the following example to configure OIDC for a sharded cluster. The principles and 
configuration options are identical to a replica set.

```yaml
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: my-oidc-shardedcluster
spec:
  type: ShardedCluster
  shardCount: 2
  mongodsPerShardCount: 3
  mongosCount: 2
  configServerCount: 3
  version: 7.0.11-ent
  opsManager:
    configMapRef:
      name: <my-project-configmap>
  credentials: <my-credentials-secret>
  security:
    authentication:
      modes: ["SCRAM", "OIDC"]
      oidcProviderConfigs:
        # Provider 1: For human users (Workforce/Group)
        - configurationName: "idp0-human-users"
          issuerURI: "https://<your-idp0-domain>"
          clientId: "<human-users-client-id>"
          audience: "api://default"
          groupsClaim: "groups"
          authorizationMethod: "WorkforceIdentityFederation"
          authorizationType: "GroupMembership"
        # Provider 2: For service accounts (Workload/UserID)
        - configurationName: "service-accounts"
          issuerURI: "https://<your-idp-uri>"
          clientId: "<services-client-id>"
          audience: "mongodb-api"
          userClaim: "sub"
          authorizationMethod: "WorkloadIdentityFederation"
          authorizationType: "UserID"
    roles:
      # Role mapping for the human user group
      - role: "idp0-human-users/db-admins"
        db: "admin"
        roles:
          - role: "readWriteAnyDatabase"
            db: "admin"
```

## OIDC Troubleshooting

- **Manually Validate JWT Token:** Use a tool to decode the OIDC token.
   - **Core Claims:** Ensure the `iss` (issuer) and `aud` (audience) claims 
     in the token exactly match your OIDC provider configuration. Check that 
     the token is not expired (`exp` claim).
   - **Expected User/Group Claims:** Verify that the expected claims for user 
     identity (`userClaim`) and groups (`groupsClaim`) are present in the token 
     and contain the correct values.
- **Verify Username Format for UserID Auth:** The `MongoDBUser` username must 
  be in the exact format `<configurationName>/<userClaimValue>`. The `<configurationName>` 
  must match the name of the OIDC provider in your `MongoDB` resource. 
- **Confirm $external Database is Used:** For `UserID` authorization, the 
  `MongoDBUser` resource must specify `db: "$external"`. Users authenticated 
  by an external source are always resolved through this virtual database.
- **Check Group Role Mapping for GroupMembership Auth:** Ensure the role defined 
  in the MongoDB resource's `spec.security.roles` section is formatted 
  correctly as `<configurationName>/<groupName>`, where `<groupName>` exactly 
  matches a group in the JWT's `groupsClaim`.
- **Validate Assigned Role Permissions:** Check that the MongoDB role(s) 
  assigned to the OIDC user or group actually grant the necessary permissions 
  (e.g., `readWrite` on the correct database).
- **Verify MongoDBUser Resource Reference:** For `UserID` authorization, make 
  sure the `spec.mongodbResourceRef.name` in the `MongoDBUser` resource 
  correctly points to the name of your `MongoDB` deployment.
