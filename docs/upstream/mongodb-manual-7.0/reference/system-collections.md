<!-- Converted from reference/system-collections.txt (reStructuredText). Includes are inlined. -->

# System Collections

## Synopsis

MongoDB stores system information in collections that use the
`<database>.system.*` namespace, which MongoDB reserves for
internal use. Do not create collections that begin with `system`.

MongoDB also stores some additional instance-local metadata in the
local database `local.replset.*`
namespace, specifically for replication purposes and in the config
database for sessions information.

MongoDB Atlas and other MongoDB cloud services store essential operational 
data in dedicated databases that use the prefix `__mdb_internal_*`. 
**Do not access or modify databases with this prefix.**
We recommend that you ignore these namespaces in administrative tools. For more 
information on these cloud-specific databases, see Internal Databases.

## Collections

System collections include these collections stored in the `admin` database:

**`admin.system.roles`**

The `admin.system.roles` collection stores custom roles that
administrators create and assign to users to provide access to
specific resources.

**`admin.system.users`**

The `admin.system.users` collection stores the user's
authentication credentials as well as any roles assigned to the user.
Users may define authorization roles in the
`admin.system.roles` collection.

**`admin.system.version`**

The `admin.system.version` collection stores metadata to 
support internal operations. Do not modify this collection unless
specifically instructed to in this documentation or by a MongoDB 
support engineer.

System collections include these collections stored in the `config` 
database:

**`config.system.indexBuilds`**

The `indexBuilds` collection stores 
information related to in-progress index builds.

### Database-Specific Collections

System collections also include these collections stored directly in
each database:

**`<database>.system.buckets`**

Stores the underlying data associated to a time series
collection. The `system.buckets`
collection stores data in an optimized format and schema for an
efficient representation of the persisted time series data.

Do not modify this collection.

**`<database>.system.profile`**

The `<database>.system.profile` collection stores database
profiling information. For information on profiling, see database-profiling.

**`<database>.system.js`**

The `<database>.system.js` collection stores special JavaScript
code for use in server side JavaScript. See
/tutorial/store-javascript-function-on-server for more
information.

**`<database>.system.views`**

The `<database>.system.views` collection contains
information about each view in the database.

Starting in MongoDB 5.0, for featureCompatibilityVersion set to `"5.0"` or greater, users can no longer write
directly to the `<database>.system.views` collection.
