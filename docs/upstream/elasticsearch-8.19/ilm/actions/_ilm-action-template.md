<!-- Converted from ilm/actions/_ilm-action-template.asciidoc (AsciiDoc). Includes are inlined. -->

### Sample

Phases allowed: hot, warm, cold, frozen, delete.

Does a cool thing. 

#### Options

`sample_option1`::
(Optional, integer)
Number of something.

`sample_option2`::
(Required, string)
Name of something.

#### Example

```console
PUT _ilm/policy/my_policy
{
  "policy": {
    "phases": {
      "warm": {
        "actions": {
          "sample" : {
            "sample_option1" : 2
          }
        }
      }
    }
  }
}
```

##### Describe example

The sample action in the following policy does something interesting. 

```console
PUT _ilm/policy/my_policy
{
  "policy": {
    "phases": {
      "warm": {
        "actions": {
          "sample" : {
            "sample_option1" : 100,
            "sample_option2" : "interesting"
          }
        }
      }
    }
  }
}
```
