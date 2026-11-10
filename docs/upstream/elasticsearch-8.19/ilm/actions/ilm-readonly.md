<!-- Converted from ilm/actions/ilm-readonly.asciidoc (AsciiDoc). Includes are inlined. -->

### Read only

Phases allowed: hot, warm, cold.

Makes the index data read-only;
disables data write operations against the index.

To use the `readonly` action in the `hot` phase, the `rollover` action *must* be present.
If no rollover action is configured, ILM will reject the policy.

#### Options

None.

#### Example

```console
PUT _ilm/policy/my_policy
{
  "policy": {
    "phases": {
      "warm": {
        "actions": {
          "readonly" : { }
        }
      }
    }
  }
}
```
