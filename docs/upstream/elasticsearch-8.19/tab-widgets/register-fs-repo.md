<!-- Converted from tab-widgets/register-fs-repo.asciidoc (AsciiDoc). Includes are inlined. -->

Linux and macOS installations support Unix-style paths:

```yaml
path:
  repo:
    - /mount/backups
    - /mount/long_term_backups
```

After restarting each node, use Kibana or the <<put-snapshot-repo-api,create
snapshot repository API>> to register the repository. When registering the
repository, specify the file system's path:

```console
PUT _snapshot/my_fs_backup
{
  "type": "fs",
  "settings": {
    "location": "/mount/backups/my_fs_backup_location"
  }
}
```

If you specify a relative path, Elasticsearch resolves the path using the first value in
the `path.repo` setting.

```console
PUT _snapshot/my_fs_backup
{
  "type": "fs",
  "settings": {
    "location": "my_fs_backup_location"        <1>
  }
}
```

<1> The first value in the `path.repo` setting is `/mount/backups`. This
relative path, `my_fs_backup_location`, resolves to
`/mount/backups/my_fs_backup_location`.

Clusters should only register a particular snapshot repository bucket once. 
If you register the same snapshot repository with multiple clusters, only one
cluster should have write access to the repository. On other clusters, register
the repository as read-only.

This prevents multiple clusters from writing to the repository at the same time
and corrupting the repository’s contents. It also prevents Elasticsearch from caching the
repository's contents, which means that changes made by other clusters will
become visible straight away.
To register a file system repository as read-only using the create snapshot
repository API, set the `readonly` parameter to true. Alternatively, you can
register a URL repository for the file
system.

```console
PUT _snapshot/my_fs_backup
{
  "type": "fs",
  "settings": {
    "location": "my_fs_backup_location",
    "readonly": true
  }
}
```

Windows installations support both DOS and Microsoft UNC paths. Escape any
backslashes in the paths. For UNC paths, provide the server and share name as a
prefix.

```yaml
path:
  repo:
    - "E:\\Mount\\Backups"                      <1>
    - "\\\\MY_SERVER\\Mount\\Long_term_backups" <2>
```

<1> DOS path
<2> UNC path

After restarting each node, use Kibana or the <<put-snapshot-repo-api,create
snapshot repository API>> to register the repository. When registering the
repository, specify the file system's path:
```console
PUT _snapshot/my_fs_backup
{
  "type": "fs",
  "settings": {
    "location": "E:\\Mount\\Backups\\My_fs_backup_location"
  }
}
```

If you specify a relative path, Elasticsearch resolves the path using the first value in
the `path.repo` setting.
```console
PUT _snapshot/my_fs_backup
{
  "type": "fs",
  "settings": {
    "location": "My_fs_backup_location"        <1>
  }
}
```

<1> The first value in the `path.repo` setting is `E:\Mount\Backups`. This
relative path, `My_fs_backup_location`, resolves to
`E:\Mount\Backups\My_fs_backup_location`.

Clusters should only register a particular snapshot repository bucket once. 
If you register the same snapshot repository with multiple clusters, only one
cluster should have write access to the repository. On other clusters, register
the repository as read-only.

This prevents multiple clusters from writing to the repository at the same time
and corrupting the repository’s contents. It also prevents Elasticsearch from caching the
repository's contents, which means that changes made by other clusters will
become visible straight away.
To register a file system repository as read-only using the create snapshot
repository API, set the `readonly` parameter to true. Alternatively, you can
register a URL repository for the file
system.
```console
PUT _snapshot/my_fs_backup
{
  "type": "fs",
  "settings": {
    "location": "my_fs_backup_location",
    "readonly": true
  }
}
```
