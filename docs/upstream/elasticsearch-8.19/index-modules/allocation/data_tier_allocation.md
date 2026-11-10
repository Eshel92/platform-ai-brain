<!-- Converted from index-modules/allocation/data_tier_allocation.asciidoc (AsciiDoc). Includes are inlined. -->

### Index-level data tier allocation filtering

You can use the index-level `_tier_preference` setting to control
which data tier an index is allocated to.

This setting corresponds to the data node roles:

* data_content
* data_hot
* data_warm
* data_cold
* data_frozen

**Note:** The data role is not a valid data tier and cannot be used
with the `_tier_preference` setting. The frozen tier stores <<partially-mounted,partially
mounted indices>> exclusively.

#### Data tier allocation settings

`index.routing.allocation.include._tier_preference`::

    Assign the index to the first tier in the list that has an available node.
    This prevents indices from remaining unallocated if no nodes are available
    in the preferred tier.
    For example, if you set `index.routing.allocation.include._tier_preference`
    to `data_warm,data_hot`, the index is allocated to the warm tier if there
    are nodes with the `data_warm` role. If there are no nodes in the warm tier,
    but there are nodes with the `data_hot` role, the index is allocated to
    the hot tier.
    Used in conjunction with data tiers.
