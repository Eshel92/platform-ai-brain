<!-- Converted from ilm/actions/ilm-delete.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete

Phases allowed: delete.

Permanently removes the index.

#### Options

`delete_searchable_snapshot`::
(Optional, Boolean)
Deletes the searchable snapshot created in a previous phase.
Defaults to `true`.
This option is applicable when the <<ilm-searchable-snapshot,searchable
snapshot>> action is used in any previous phase.
If you set this option to `false`, use the <<delete-snapshot-api,Delete
snapshots API>> to remove {search-snaps} from your snapshot repository when
they are no longer needed.
If you manually delete an index before the Index lifecycle management delete phase runs, then
ILM will not delete the underlying {search-snap}. Use the
Delete snapshots API to remove the {search-snap} from
your snapshot repository when it is no longer needed.
See Reliability of {search-snaps} for
further information about deleting {search-snaps}.

**Warning:** If a policy with a searchable snapshot action is applied on an existing searchable snapshot index,
the snapshot backing this index will NOT be deleted because it was not created by this policy. If you want
to clean this snapshot, please delete it manually after the index is deleted using the delete snapshot API, you
can find the repository and snapshot name using the get index API.

#### Example

```console
PUT _ilm/policy/my_policy
{
  "policy": {
    "phases": {
      "delete": {
        "actions": {
          "delete" : { }
        }
      }
    }
  }
}
```
