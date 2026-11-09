<!-- Converted from tutorial/list-users.txt (reStructuredText). Includes are inlined. -->

# List Users in Self-Managed Deployments

To list all users, use `mongosh` to query the
system.users collection:

```sh
use admin
db.system.users.find()
```

**Important:**

Do not modify the system.users collection directly. To manage
users, use the designated user management commands.

To list all users of a sharded cluster that were
created through a `mongos`, connect to a
`mongos` and run the preceding command. MongoDB stores
users that are created through a `mongos` in the `admin`
database of the config servers.

To list all shard local users, connect to the respective shard directly and run
the preceding command. MongoDB stores *shard local* users in the
`admin` database of the shard itself. These *shard local* users are
independent from the users added to the sharded cluster through a
`mongos`. *Shard local* users are local to the shard and
are inaccessible to `mongos`.
