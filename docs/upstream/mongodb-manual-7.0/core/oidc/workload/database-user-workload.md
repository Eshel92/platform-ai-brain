<!-- Converted from core/oidc/workload/database-user-workload.txt (reStructuredText). Includes are inlined. -->

# Authorize Users with Workload Identity Federation

You can add a database user to MongoDB using Workload Identity Federation. 
This approach enables your organization’s identity provider to manage 
user access, ensuring secure, centralized authentication for database 
operations.

## Before you Begin

- You must workload-external-provider. 
- You must configure-mongodb-workload.

**Note:**

Your `oidcIdentityProviders` configuration determines the 
approach you must take to authorize users:

- If the `useAuthorizationClaim` field is set to `false` to enable 
  internal authorization, authorize users with user IDs.

- If the field is set to `true`, authorize users with identity provider 
  groups.

## Steps

**add-idp-groups:**

**Step 1: Create MongoDB roles**

In the `admin` database, use the `db.createRole()` method to create 
roles that map the identity provider group roles to MongoDB roles.

Use the following format to create roles: 

```
<authNamePrefix>/<authorizationClaim>
```

The `oidcIdentityProviders` parameter provides the `authNamePrefix` 
field and the `authorizationClaim` field. For example: 

```javascript
db.createRole( { 
   role: "okta/Everyone", 
   privileges: [ ], 
   roles: [ "readWriteAnyDatabase" ] 
} )
```

**add-user-id:**

**Step 1: Switch to the $external database**

When you create a user, you must create it in the `$external` database. 
To switch to the `$external` database, run the following command:

```
use $external
```

**Step 2: Create a user**

To create users and add them to your MongoDB database, use the 
`db.createUser()` command.

Use the following format for the `user` field, where the `authNamePrefix` 
and `authorizationClaim` values come from the `oidcIdentityProviders` 
parameter:

```
<authNamePrefix>/<authorizationClaim>
```

To create a user in MongoDB with the `authNamePrefix` of `okta` and 
an `authorizationClaim` of `jane.doe`, run the following:

```javascript
db.createUser( {
   user: "okta/jane.doe", 
   roles: [
      {
         role: "readWriteAnyDatabase", 
         db: "admin"
      }
   ]
} )
```

## Next Steps

You can connect an application to MongoDB using Workload Identity 
Federation with the following supported drivers:

- `Java`
- `Kotlin`
- `Node.js`
- [PyMongo](https://www.mongodb.com/docs/languages/python/pymongo-driver/security/enterprise-authentication/#mongodb-oidc)
- `TypeScript`
- `C#`
- `Go`

## Learn More

- workload
- workforce
