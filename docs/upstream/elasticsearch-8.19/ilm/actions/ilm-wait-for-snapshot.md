<!-- Converted from ilm/actions/ilm-wait-for-snapshot.asciidoc (AsciiDoc). Includes are inlined. -->

### Wait for snapshot

Phases allowed: delete.

Waits for the specified SLM policy to be executed before removing the index.
This checks that an SLM policy has had a successful execution at some point after the wait action has started, and that the index is included in the snapshot.

#### Options

`policy`::
(Required, string)
Name of the SLM policy that the delete action should wait for.

#### Example

```console
PUT _ilm/policy/my_policy
{
  "policy": {
    "phases": {
      "delete": {
        "actions": {
          "wait_for_snapshot" : {
            "policy": "slm-policy-name"
          }
        }
      }
    }
  }
}
```
